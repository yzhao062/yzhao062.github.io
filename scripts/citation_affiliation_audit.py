"""Citation Affiliation Audit (orchestrator).

Searches papers in `data/publications.json` (excluding surveys), finds their
IDs on one or more bibliometric sources, then queries citing papers for
notable institution affiliations.

Sources supported:
- OpenAlex (default; no credentials required, but undercounts CS papers
  significantly -- e.g., PyOD shows ~24 citations on OpenAlex versus
  1,000+ on Google Scholar).
- Dimensions Analytics API (requires `DIMENSIONS_API_KEY` in `.env`,
  scientometric researcher access tier). Better CS coverage in practice.

Use `--source both` to merge OpenAlex and Dimensions entries. Rows are
deduplicated by (canonical organization, normalized citing title, cited work),
so a citation that both sources see is counted once but tagged as
`openalex+dimensions`. Citing papers authored by the PI or by two or more
frequent co-authors are excluded and listed separately.

Usage:
    python scripts/citation_affiliation_audit.py                         # OpenAlex only
    python scripts/citation_affiliation_audit.py --source both
    python scripts/citation_affiliation_audit.py --source dimensions
    python scripts/citation_affiliation_audit.py --limit 5               # quick OpenAlex check
    python scripts/citation_affiliation_audit.py --from-raw .cache/citation-audit-raw.json
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Iterable

from citation_audit_common import (
    classify_institution,
    dedup_entries,
    load_coauthors,
    load_papers,
    load_work_authors,
    normalize_arxiv_id,
    normalize_doi,
    normalize_title,
    screen_self_citation,
    short_label,
    source_display_label,
)

EMAIL = "yue.z@usc.edu"
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent


# ── OpenAlex provider ────────────────────────────────────────────────────


class OpenAlexBudgetExhausted(RuntimeError):
    """OpenAlex refused the request because the daily credit budget is spent.

    OpenAlex moved to a metered model: the free tier is 1000 credits (US$0.10)
    per day, reset at midnight UTC, and every request costs one credit. Once the
    budget is gone every subsequent call returns HTTP 429 with a `Retry-After`
    measured in hours. Retrying inside a run cannot recover, so this is raised
    to abort the pass instead of letting empty results look like zero citations.
    """

    def __init__(self, retry_after: int):
        self.retry_after = retry_after
        hours = retry_after / 3600.0
        super().__init__(
            f"OpenAlex daily credit budget exhausted; resets in {hours:.1f}h "
            f"(Retry-After: {retry_after}s)"
        )


def _openalex_polite(url: str) -> str:
    """Add the polite-pool `mailto` parameter, which OpenAlex rate-limits less."""
    if "mailto=" in url:
        return url
    sep = "&" if "?" in url else "?"
    return f"{url}{sep}mailto={urllib.parse.quote(EMAIL)}"


def _openalex_get(url: str):
    url = _openalex_polite(url)
    for attempt in range(5):
        try:
            req = urllib.request.Request(url)
            req.add_header("User-Agent", f"citation-audit/1.0 (mailto:{EMAIL})")
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            if e.code == 429:
                # A long Retry-After means the daily budget is gone, not that we
                # are briefly over the burst rate. Sleeping cannot help.
                try:
                    retry_after = int(e.headers.get("Retry-After", "0"))
                except (TypeError, ValueError):
                    retry_after = 0
                if retry_after > 120:
                    raise OpenAlexBudgetExhausted(retry_after) from None
                wait = 3 * (attempt + 1)
                print(f"    Rate limited, waiting {wait}s...")
                time.sleep(wait)
            elif e.code == 404:
                return None
            else:
                print(f"    HTTP {e.code}")
                return None
        except Exception as e:
            print(f"    Error: {e}")
            time.sleep(2)
    return None


def _find_openalex_id(title: str, paper_url: str | None = None):
    """Find OpenAlex work ID via arXiv ID > DOI > strict title match."""
    arxiv_id = normalize_arxiv_id(paper_url or "")
    if arxiv_id:
        url = (
            f"https://api.openalex.org/works/https://arxiv.org/abs/{arxiv_id}"
            "?select=id,title,cited_by_count"
        )
        data = _openalex_get(url)
        if data and data.get("id"):
            oa_id = data["id"].replace("https://openalex.org/", "")
            return oa_id, data.get("title", ""), data.get("cited_by_count", 0)
        time.sleep(0.1)

    doi = normalize_doi(paper_url or "")
    if doi:
        url = (
            f"https://api.openalex.org/works/https://doi.org/{doi}"
            "?select=id,title,cited_by_count"
        )
        data = _openalex_get(url)
        if data and data.get("id"):
            oa_id = data["id"].replace("https://openalex.org/", "")
            return oa_id, data.get("title", ""), data.get("cited_by_count", 0)
        time.sleep(0.1)

    # Title fallback with prefix-anchor + word-overlap matching
    # Punctuation such as "?" in a title makes the search endpoint return HTTP 400,
    # which used to be recorded as "not found"; search on a plain word bag instead.
    search_text = re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", title)).strip()
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode({
        "search": search_text,
        "per_page": "5",
        "select": "id,title,cited_by_count,publication_year",
    })
    data = _openalex_get(url)
    if not data or not data.get("results"):
        return None, None, 0

    def words(t: str) -> set[str]:
        return set(re.findall(r"\w{3,}", t.lower()))

    def norm(t: str) -> str:
        return re.sub(r"[^a-z0-9 ]", "", t.lower()).strip()

    title_words = words(title)
    title_norm = norm(title)
    if not title_words:
        return None, None, 0

    prefix_match = re.match(r"^([A-Za-z0-9\-]+)\s*:", title)
    prefix_anchor = prefix_match.group(1).lower() if prefix_match else None

    for w in data["results"]:
        if norm(w.get("title", "")) == title_norm:
            oa_id = w["id"].replace("https://openalex.org/", "")
            return oa_id, w.get("title", ""), w.get("cited_by_count", 0)

    for w in data["results"]:
        found_title = w.get("title", "")
        found_norm = norm(found_title)
        found_words = words(found_title)
        if not found_words:
            continue
        overlap = len(title_words & found_words) / len(title_words)
        if prefix_anchor:
            if prefix_anchor not in found_norm:
                continue
            if overlap >= 0.5:
                oa_id = w["id"].replace("https://openalex.org/", "")
                return oa_id, found_title, w.get("cited_by_count", 0)
        else:
            if overlap >= 0.7:
                oa_id = w["id"].replace("https://openalex.org/", "")
                return oa_id, found_title, w.get("cited_by_count", 0)

    if data["results"]:
        print(f"    No match passed verification: \"{data['results'][0].get('title', '')[:50]}\"")
    return None, None, 0


def _get_openalex_citing(work_id: str, max_pages: int = 50):
    """Citing-paper records for a single OpenAlex work."""
    results: list[dict] = []
    cursor = "*"
    for _ in range(max_pages):
        url = "https://api.openalex.org/works?" + urllib.parse.urlencode({
            "filter": f"cites:{work_id}",
            "per_page": "200",
            "cursor": cursor,
            "select": "id,title,publication_year,authorships",
        })
        data = _openalex_get(url)
        if not data or not data.get("results"):
            break

        for w in data["results"]:
            seen: set[str] = set()
            inst_details: list[dict] = []
            authors = [
                (a.get("author") or {}).get("display_name", "")
                for a in w.get("authorships", [])
            ]
            for authorship in w.get("authorships", []):
                for inst in authorship.get("institutions", []):
                    name = inst.get("display_name", "")
                    if name and name not in seen:
                        seen.add(name)
                        inst_details.append({
                            "name": name,
                            "country": inst.get("country_code", ""),
                        })
            if inst_details:
                citing_id = w.get("id", "").replace("https://openalex.org/", "")
                results.append({
                    "id": citing_id,
                    "title": w.get("title", ""),
                    "year": w.get("publication_year"),
                    "institutions": inst_details,
                    "authors": [a for a in authors if a],
                })

        cursor = data.get("meta", {}).get("next_cursor")
        if not cursor or len(data["results"]) < 200:
            break
        time.sleep(0.15)
    return results


# Not under data/: ci_check_site.py requires every JSON there to be a top-level
# array of site data, and this is a derived local cache rather than site content.
OPENALEX_ID_CACHE = PROJECT_ROOT / ".cache" / "openalex-id-cache.json"


def _load_id_cache() -> dict:
    try:
        return json.loads(OPENALEX_ID_CACHE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _save_id_cache(cache: dict) -> None:
    try:
        OPENALEX_ID_CACHE.parent.mkdir(parents=True, exist_ok=True)
        OPENALEX_ID_CACHE.write_text(json.dumps(cache, indent=1, sort_keys=True), encoding="utf-8")
    except Exception as e:  # a cache failure must never abort the audit
        print(f"    (could not write OpenAlex id cache: {e})")


def fetch_openalex_entries(papers: list[dict], *, verbose: bool = True, log=print) -> dict:
    """Return audit entries discovered through OpenAlex.

    Phase 1 resolutions are cached in `.cache/openalex-id-cache.json`. The free
    OpenAlex tier allows 1000 requests per day, and resolving 116 papers can
    spend most of that before a single citing-paper query runs, so re-runs read
    identifiers from the cache and spend the budget on Phase 2 instead.
    """
    found_works: dict[str, str] = {}
    not_found: list[str] = []
    zero_cite: list[str] = []
    budget_error: str | None = None

    cache = _load_id_cache()
    cache_hits = 0

    if verbose:
        log("=" * 60)
        log("PHASE 1: Finding OpenAlex IDs")
        log("=" * 60)

    try:
        for i, p in enumerate(papers):
            title = p["title"]
            venue = p.get("venue", "")
            short = f"{title[:50]}... ({venue})"
            key = (p.get("paper_url") or title).strip()
            if verbose:
                log(f"  [{i+1}/{len(papers)}] {short}")
            if key in cache:
                oa_id, cite_count = cache[key]["id"], cache[key]["cited_by"]
                cache_hits += 1
            else:
                oa_id, _, cite_count = _find_openalex_id(title, paper_url=p.get("paper_url"))
                # Cache only resolved works: a miss may be an HTTP error or an indexing lag,
                # and caching it would stop every later run from trying again.
                if oa_id:
                    cache[key] = {"id": oa_id, "cited_by": cite_count}
                time.sleep(0.12)
            if oa_id and cite_count > 0:
                found_works[oa_id] = short_label(title, venue)
                if verbose:
                    log(f"    -> {oa_id} (cited_by={cite_count})")
            elif oa_id:
                zero_cite.append(short)
                if verbose:
                    log(f"    -> {oa_id} (0 citations, skipping)")
            else:
                not_found.append(short)
                if verbose:
                    log("    -> NOT FOUND")
    except OpenAlexBudgetExhausted as e:
        budget_error = str(e)
        if verbose:
            log(f"\n  !! {e}")
            log("  !! Phase 1 stopped early. Resolved identifiers are cached for the next run.")
    finally:
        _save_id_cache(cache)

    if verbose and cache_hits:
        log(f"\n  ({cache_hits} identifiers served from cache, {len(papers) - cache_hits} looked up)")

    if verbose:
        log(f"\nFound {len(found_works)} papers with citations")
        log("\n" + "=" * 60)
        log("PHASE 2: Fetching citing papers (per-work)")
        log("=" * 60)

    entries: list[dict] = []
    citing_ids: set[str] = set()
    works_queried = 0
    works_unqueried: list[str] = []

    for idx, (oa_id, short_name) in enumerate(found_works.items()):
        if budget_error:
            works_unqueried.append(short_name)
            continue
        if verbose:
            log(f"  [{idx+1}/{len(found_works)}] {short_name}")
        try:
            citing = _get_openalex_citing(oa_id)
        except OpenAlexBudgetExhausted as e:
            budget_error = str(e)
            works_unqueried.append(short_name)
            if verbose:
                log(f"    !! {e}")
                log("    !! Aborting the OpenAlex pass. Remaining works are reported as")
                log("       NOT QUERIED rather than as zero citations.")
            continue
        works_queried += 1
        if verbose:
            log(f"    -> {len(citing)} citing papers")
        for c in citing:
            if c.get("id"):
                citing_ids.add(c["id"])
            for inst in c["institutions"]:
                tier, category, org = classify_institution(inst["name"])
                if tier is None:
                    continue
                entries.append({
                    "tier": tier,
                    "category": category,
                    "org": org,
                    "institution": inst["name"],
                    "country": inst.get("country", ""),
                    "cited_work": short_name,
                    "citing_title": c.get("title", ""),
                    "citing_id": c.get("id", ""),
                    "authors": c.get("authors", []),
                    "year": c.get("year"),
                    "source": "openalex",
                })
                if verbose and tier == "T0":
                    log(f"    ** T0 [{category}] {inst['name'][:40]}")
        time.sleep(0.5)

    if verbose and budget_error:
        log(f"\n  !! OpenAlex pass INCOMPLETE: {works_queried} of {len(found_works)} works queried.")
        log(f"  !! {len(works_unqueried)} works were never queried and are NOT zero-citation results.")

    return {
        "entries": dedup_entries(entries),
        "found_count": len(found_works),
        "zero_cite": zero_cite,
        "not_found": not_found,
        "unique_citing": len(citing_ids),
        "budget_error": budget_error,
        "works_queried": works_queried,
        "works_unqueried": works_unqueried,
    }


# ── Output ───────────────────────────────────────────────────────────────


COUNTRY_NAMES = {
    "US": "United States", "GB": "United Kingdom", "CN": "China", "DE": "Germany",
    "FR": "France", "JP": "Japan", "KR": "South Korea", "IN": "India",
    "CH": "Switzerland", "SE": "Sweden", "IE": "Ireland", "CA": "Canada",
    "AU": "Australia", "NL": "Netherlands", "IT": "Italy", "ES": "Spain",
    "SG": "Singapore", "BR": "Brazil", "PT": "Portugal", "RO": "Romania",
    "BE": "Belgium", "DK": "Denmark", "FI": "Finland", "NO": "Norway",
    "AT": "Austria", "IL": "Israel", "TW": "Taiwan", "HK": "Hong Kong",
    "PL": "Poland", "CZ": "Czechia", "GR": "Greece", "TR": "Turkey",
    "SA": "Saudi Arabia", "AE": "United Arab Emirates", "MX": "Mexico",
    "NZ": "New Zealand", "ZA": "South Africa", "RU": "Russia",
}


def _country_label(raw: str) -> str:
    """Render ", "-joined country names or ISO codes as unique full names."""
    out: list[str] = []
    for c in (raw or "").split(", "):
        name = COUNTRY_NAMES.get(c.strip().upper(), c.strip()) if len(c.strip()) == 2 else c.strip()
        if name and name not in out:
            out.append(name)
    return ", ".join(out)


def _cell(text: str, max_len: int | None = None) -> str:
    text = (text or "").replace("|", "/").replace("\n", " ").strip()
    if max_len and len(text) > max_len:
        text = text[:max_len].rsplit(" ", 1)[0].rstrip(",;:-") + "\u2026"
    return text


def _n(count: int, noun: str) -> str:
    return f"{count:,} {noun}" + ("" if count == 1 else "s")


WORK_AUTHORS = load_work_authors(str(PROJECT_ROOT))
# Outcomes of direct checks on individual rows. The indexes cannot know them, so they are
# reapplied on every render instead of being hand-edited into the report.
_OVERRIDES_PATH = PROJECT_ROOT / "skills" / "citation-audit" / "references" / "citation-audit-overrides.json"
OVERRIDES = (json.loads(_OVERRIDES_PATH.read_text(encoding="utf-8")).get("overrides", [])
             if _OVERRIDES_PATH.exists() else [])


def _override(e: dict) -> dict | None:
    """The first checked override matching an entry's citing title, org and work cited."""
    for o in OVERRIDES:
        if o["citing_title"] != e.get("citing_title"):
            continue
        if o.get("org") and o["org"] != e.get("org"):
            continue
        if o.get("cited_work") and o["cited_work"] != e.get("cited_work"):
            continue
        return o
    return None


def _screen(entries: list[dict], coauthors: dict):
    """Split merged entries into kept rows and excluded self / co-author rows."""
    kept: list[dict] = []
    excluded: list[dict] = []
    possible: list[dict] = []
    for e in entries:
        o = _override(e)
        if o and o["action"] == "drop":
            excluded.append({**e, "verdict": "checked", "matched": [o["reason"]]})
            continue
        if o and o["action"] == "relabel":
            e = {**e, "cited_work": o["to"]}
        verdict, names = screen_self_citation(
            e.get("authors") or [], coauthors, WORK_AUTHORS.get(e.get("cited_work", ""))
        )
        if verdict in ("self", "coauthor"):
            excluded.append({**e, "verdict": verdict, "matched": names})
            continue
        if o and o["action"] == "flag":
            possible.append({**e, "matched": [o["reason"]] + names})
        elif verdict == "possible":
            possible.append({**e, "matched": names})
        kept.append(e)
    return kept, excluded, possible


TIER_HEADINGS = (
    ("T0", "Tier 0: Government, National Labs, Space Agencies, Central Banks, Defense, "
           "Research Institutes, Foundation Model Companies"),
    ("T1", "Tier 1: Big Tech, Finance, Pharma, Healthcare, Industrial, Telecom"),
)


def _write_markdown(merged: dict, total_papers: int, out_path: Path, coauthors: dict,
                    generated: str) -> None:
    per_source: dict[str, dict] = merged["per_source"]
    kept, excluded, possible = _screen(merged["entries"], coauthors)

    src_names = list(per_source.keys())
    src_label = " + ".join(source_display_label(s) for s in src_names)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# Citation Affiliation Audit\n\n")
        f.write(f"*Generated {generated} via {src_label} over {total_papers} non-survey papers "
                "in `data/publications.json`.*\n\n")
        f.write(
            "Each row is a citing paper with at least one author at a notable organization. "
            "It means researchers at that organization cited the work, not that the "
            "organization endorses it. Self-citations and co-author citations are excluded. "
            "Both sources undercount computer-science citations, so treat every figure as a "
            "lower bound.\n\n"
        )

        f.write("| Source | Papers with citations | Unique citing papers | Run status |\n")
        f.write("|---|---:|---:|---|\n")
        for src in src_names:
            ps = per_source[src]
            status = "complete"
            if ps.get("budget_error"):
                status = (f"incomplete: {ps.get('works_queried', 0)} works queried, "
                          f"{len(ps.get('works_unqueried') or [])} never queried")
            f.write(f"| {source_display_label(src)} | {ps['found_count']} / {total_papers} | "
                    f"{ps['unique_citing']:,} | {status} |\n")
        f.write("\n")

        # An API failure must never be readable as a zero-citation finding.
        incomplete = [(s, per_source[s]) for s in src_names if per_source[s].get("budget_error")]
        if incomplete:
            f.write("> [!WARNING]\n")
            f.write("> **This run is incomplete.** One or more sources stopped early, so the numbers\n")
            f.write("> are a floor, and an absent citation here is not evidence of no citation.\n")
            for src, ps in incomplete:
                f.write(f">\n> - **{source_display_label(src)}**: {ps['budget_error']}\n")
            f.write("\n")

        for tier, heading in TIER_HEADINGS:
            rows = [e for e in kept if e["tier"] == tier]
            orgs = {e.get("org") or e["institution"] for e in rows}
            papers = {normalize_title(e.get("citing_title") or "") for e in rows}
            f.write(f"## {heading}\n\n")
            f.write(f"**{_n(len(rows), 'row')}: {_n(len(papers), 'citing paper')}, "
                    f"{_n(len(orgs), 'organization')}.**\n\n")
            if not rows:
                continue
            f.write("| Category | Organization | Country | Work Cited | Citing Paper | Year | Source |\n")
            f.write("|---|---|---|---|---|---|---|\n")
            for e in sorted(rows, key=lambda x: (x["category"], x.get("org") or "", -(x.get("year") or 0))):
                f.write(
                    f"| {e['category']} | {_cell(e.get('org') or e['institution'])} | "
                    f"{_cell(_country_label(e.get('country', '')))} | {_cell(e['cited_work'])} | "
                    f"{_cell(e.get('citing_title'), 90)} | {e.get('year') or ''} | "
                    f"{e.get('source', '')} |\n"
                )
            f.write("\n")

        f.write("## Summary by Organization\n\n")
        by_org: dict[tuple, dict] = {}
        for e in kept:
            key = (e.get("org") or e["institution"], e["category"], e["tier"])
            agg = by_org.setdefault(key, {"papers": set(), "works": set()})
            agg["papers"].add(normalize_title(e.get("citing_title") or ""))
            agg["works"].add(e["cited_work"])
        f.write("| Organization | Category | Tier | Citing Papers | Works Cited |\n")
        f.write("|---|---|---|---:|---:|\n")
        for (org, cat, tier), agg in sorted(
            by_org.items(), key=lambda x: (x[0][2], -len(x[1]["papers"]), x[0][0])
        ):
            f.write(f"| {org} | {cat} | {tier[1]} | {len(agg['papers'])} | {len(agg['works'])} |\n")
        f.write("\n")

        f.write("## Excluded and Flagged Citations\n\n")
        n_self = sum(1 for e in excluded if e["verdict"] == "self")
        n_chk = sum(1 for e in excluded if e["verdict"] == "checked")
        n_co = len(excluded) - n_self - n_chk
        f.write(
            f"Excluded: {_n(n_self, 'row')} where the PI is a citing author, {_n(n_co, 'row')} "
            "where an author of the cited work or two or more frequent co-authors are, and "
            f"{_n(n_chk, 'row')} that a direct check of the paper refuted. A frequent "
            "co-author shares two or more papers with the PI. "
            f"Flagged but kept: {_n(len(possible), 'row')} where exactly one frequent co-author "
            "who did not write the cited work matches, since one common name is weak evidence, "
            "or where a direct check could not confirm the citation or affiliation.\n\n"
        )
        for label, rows in (("Excluded", excluded), ("Flagged, kept", possible)):
            if not rows:
                continue
            f.write(f"<details><summary>{label} ({_n(len(rows), 'row')})</summary>\n\n")
            f.write("| Organization | Work Cited | Citing Paper | Year | Matched Authors or Reason |\n")
            f.write("|---|---|---|---|---|\n")
            for e in sorted(rows, key=lambda x: (x.get("org") or "", x.get("citing_title") or "")):
                f.write(
                    f"| {_cell(e.get('org') or e['institution'])} | {_cell(e['cited_work'])} | "
                    f"{_cell(e.get('citing_title'), 90)} | {e.get('year') or ''} | "
                    f"{_cell(', '.join(e['matched']))} |\n"
                )
            f.write("\n</details>\n\n")

        f.write("## Coverage\n\n")
        for src in src_names:
            ps = per_source[src]
            nf = ps.get("not_found") or []
            if ps.get("budget_error"):
                f.write(f"- **{source_display_label(src)}**: stopped early, see the warning above; "
                        f"{ps.get('works_queried', 0)} works queried.\n")
                continue
            f.write(
                f"- **{source_display_label(src)}**: {ps['found_count']} papers with citations, "
                f"{len(ps.get('zero_cite') or [])} indexed with zero citations, {len(nf)} not found"
                + (f": {'; '.join(_cell(n) for n in nf)}." if nf else ".")
                + "\n"
            )
        f.write(
            "\nRows are deduplicated by (organization, normalized citing title, work cited). "
            "Legal entities of one company, a preprint and its journal version, and the two "
            "sources' records of one paper therefore count once. Recent preprints are indexed "
            "with a lag; re-run each semester.\n"
        )


def _merge_results(results: list[tuple[str, dict]]) -> dict:
    """Combine per-source results into a single merged result.

    Args:
        results: list of (source_name, provider_result) tuples in execution order.

    Returns:
        Dict with:
            entries: union of all entries, deduplicated by
                (institution, citing_title, cited_work). Cross-source duplicates
                collapse to one row with `source = "openalex+dimensions"`.
            per_source: dict from source_name to its raw provider result, so the
                Markdown writer can emit per-source coverage subsections rather
                than reporting a misleading max/concat across sources.
    """
    all_entries: list[dict] = []
    per_source: dict[str, dict] = {}
    for source, r in results:
        all_entries.extend(r.get("entries", []))
        per_source[source] = {
            "found_count": r.get("found_count", 0),
            "zero_cite": list(r.get("zero_cite", [])),
            "not_found": list(r.get("not_found", [])),
            "unique_citing": r.get("unique_citing", 0),
            "budget_error": r.get("budget_error"),
            "works_queried": r.get("works_queried", 0),
            "works_unqueried": list(r.get("works_unqueried", [])),
        }
    return {
        "entries": dedup_entries(all_entries),
        "per_source": per_source,
    }


# ── CLI ──────────────────────────────────────────────────────────────────


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Citation-affiliation audit across OpenAlex and Dimensions."
    )
    parser.add_argument(
        "--source",
        choices=["openalex", "dimensions", "both"],
        default="openalex",
        help="Bibliometric source(s) to query (default: openalex; use 'both' for combined OpenAlex + Dimensions).",
    )
    parser.add_argument(
        "--limit", type=int, default=None,
        help="Process only the first N papers (for quick verification)."
    )
    parser.add_argument(
        "--max-citing-pages-dimensions", type=int, default=5,
        help="Max pages of citing publications per work for Dimensions (page size 1000)."
    )
    parser.add_argument(
        "--out",
        default=str(PROJECT_ROOT / "citation-affiliation-audit.md"),
        help="Output Markdown path.",
    )
    parser.add_argument(
        "--raw-out",
        default=str(PROJECT_ROOT / ".cache" / "citation-audit-raw.json"),
        help="Where to save merged raw entries, so the report can be re-rendered without re-querying.",
    )
    parser.add_argument(
        "--from-raw", nargs="+", default=None,
        help="Re-render the report from one or more saved --raw-out files instead of querying any "
             "source. Files from separate single-source runs are merged; a later file's source wins.",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)
    coauthors = load_coauthors(str(PROJECT_ROOT))

    if args.from_raw:
        entries: list[dict] = []
        per_source: dict[str, dict] = {}
        generated, total = "", 0
        for raw_file in args.from_raw:
            raw = json.loads(Path(raw_file).read_text(encoding="utf-8"))
            # A refreshed provider replaces only its own share of each entry; an entry that
            # another provider also found keeps that provider instead of being dropped.
            surviving = []
            for e in entries:
                kept_src = [x for x in e.get("source", "").split("+") if x and x not in raw["per_source"]]
                if kept_src:
                    surviving.append({**e, "source": "+".join(kept_src)})
            entries = surviving + raw["entries"]
            per_source.update(raw["per_source"])
            generated = max(generated, raw["generated"])
            total = max(total, raw["total_papers"])
        ordered = {s: per_source[s] for s in ("openalex", "dimensions") if s in per_source}
        merged = {"entries": dedup_entries(entries), "per_source": ordered}
        _write_markdown(merged, total, Path(args.out), coauthors, generated)
        print(f"Re-rendered {args.out} from {', '.join(args.from_raw)}")
        return 0

    print("Loading papers from publications.json...")
    papers = load_papers(str(PROJECT_ROOT))
    if args.limit:
        papers = papers[: args.limit]
    print(f"  {len(papers)} papers (after excluding surveys)\n")

    results: list[tuple[str, dict]] = []
    generated = time.strftime("%Y-%m-%d")
    raw_path = Path(args.raw_out)

    def checkpoint() -> None:
        """Save what has been fetched so far, so a later provider's crash keeps it."""
        merged_so_far = _merge_results(results)
        try:
            raw_path.parent.mkdir(parents=True, exist_ok=True)
            raw_path.write_text(json.dumps({
                "generated": generated,
                "total_papers": len(papers),
                "per_source": merged_so_far["per_source"],
                "entries": merged_so_far["entries"],
            }, indent=1), encoding="utf-8")
        except Exception as e:  # the raw dump is a convenience; never abort the audit on it
            print(f"    (could not write raw entries: {e})")

    if args.source in ("openalex", "both"):
        print(">>> Running OpenAlex provider\n")
        results.append(("openalex", fetch_openalex_entries(papers, verbose=True)))
        checkpoint()

    if args.source in ("dimensions", "both"):
        print("\n>>> Running Dimensions provider\n")
        # Imported lazily so the OpenAlex-only path does not require dimcli.
        from citation_affiliation_audit_dimensions import fetch_dimensions_entries
        results.append((
            "dimensions",
            fetch_dimensions_entries(
                papers,
                max_citing_pages=args.max_citing_pages_dimensions,
                verbose=True,
            ),
        ))

    checkpoint()
    merged = _merge_results(results)
    out_path = Path(args.out)
    _write_markdown(merged, len(papers), out_path, coauthors, generated)

    kept, excluded, _ = _screen(merged["entries"], coauthors)
    t0 = sum(1 for e in kept if e["tier"] == "T0")
    t1 = sum(1 for e in kept if e["tier"] == "T1")
    print(f"\n{'=' * 60}")
    print(f"DONE -> {out_path}")
    print(f"Sources: {' + '.join(merged['per_source'].keys())}")
    incomplete = False
    for src, ps in merged["per_source"].items():
        print(f"  {src}: {ps['found_count']}/{len(papers)} papers with citations, "
              f"{ps['unique_citing']} unique citing papers")
        if ps.get("budget_error"):
            incomplete = True
            print(f"    !! INCOMPLETE: {ps['budget_error']}")
            print(f"    !! {ps.get('works_queried', 0)} works queried, "
                  f"{len(ps.get('works_unqueried') or [])} never queried "
                  f"(these are unknown, not zero).")
    print(f"Tier 0: {t0} entries")
    print(f"Tier 1: {t1} entries")
    print(f"Excluded self / co-author rows: {len(excluded)}")
    print("=" * 60)
    if incomplete:
        print("Exit 3: at least one source stopped early. Re-run after the budget resets;\n"
              "        cached identifiers mean the next run spends its budget on citing papers.")
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
