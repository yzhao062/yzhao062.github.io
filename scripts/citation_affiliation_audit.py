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

Use `--source both` to merge OpenAlex and Dimensions entries. Cross-source
duplicates are deduplicated by (institution, citing title, cited work), so a
citation that both sources see is counted once but tagged as
`openalex+dimensions`.

Usage:
    python scripts/citation_affiliation_audit.py                         # OpenAlex only
    python scripts/citation_affiliation_audit.py --source both
    python scripts/citation_affiliation_audit.py --source dimensions
    python scripts/citation_affiliation_audit.py --limit 5               # quick OpenAlex check
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
    load_papers,
    normalize_arxiv_id,
    normalize_doi,
    short_label,
    source_display_label,
)

EMAIL = "yue.z@usc.edu"
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent


# ── OpenAlex provider ────────────────────────────────────────────────────


def _openalex_get(url: str):
    for attempt in range(5):
        try:
            req = urllib.request.Request(url)
            req.add_header("User-Agent", f"mailto:{EMAIL}")
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            if e.code == 429:
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
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode({
        "search": title,
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
                })

        cursor = data.get("meta", {}).get("next_cursor")
        if not cursor or len(data["results"]) < 200:
            break
        time.sleep(0.15)
    return results


def fetch_openalex_entries(papers: list[dict], *, verbose: bool = True, log=print) -> dict:
    """Return audit entries discovered through OpenAlex."""
    found_works: dict[str, str] = {}
    not_found: list[str] = []
    zero_cite: list[str] = []

    if verbose:
        log("=" * 60)
        log("PHASE 1: Finding OpenAlex IDs")
        log("=" * 60)

    for i, p in enumerate(papers):
        title = p["title"]
        venue = p.get("venue", "")
        short = f"{title[:50]}... ({venue})"
        if verbose:
            log(f"  [{i+1}/{len(papers)}] {short}")
        oa_id, _, cite_count = _find_openalex_id(title, paper_url=p.get("paper_url"))
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
        time.sleep(0.12)

    if verbose:
        log(f"\nFound {len(found_works)} papers with citations")
        log("\n" + "=" * 60)
        log("PHASE 2: Fetching citing papers (per-work)")
        log("=" * 60)

    entries: list[dict] = []
    citing_ids: set[str] = set()

    for idx, (oa_id, short_name) in enumerate(found_works.items()):
        if verbose:
            log(f"  [{idx+1}/{len(found_works)}] {short_name}")
        citing = _get_openalex_citing(oa_id)
        if verbose:
            log(f"    -> {len(citing)} citing papers")
        for c in citing:
            if c.get("id"):
                citing_ids.add(c["id"])
            for inst in c["institutions"]:
                tier, category = classify_institution(inst["name"])
                if tier is None:
                    continue
                entries.append({
                    "tier": tier,
                    "category": category,
                    "institution": inst["name"],
                    "country": inst.get("country", ""),
                    "cited_work": short_name,
                    "citing_title": c.get("title", ""),
                    "citing_id": c.get("id", ""),
                    "year": c.get("year"),
                    "source": "openalex",
                })
                if verbose and tier == "T0":
                    log(f"    ** T0 [{category}] {inst['name'][:40]}")
        time.sleep(0.5)

    return {
        "entries": dedup_entries(entries),
        "found_count": len(found_works),
        "zero_cite": zero_cite,
        "not_found": not_found,
        "unique_citing": len(citing_ids),
    }


# ── Output ───────────────────────────────────────────────────────────────


def _write_markdown(merged: dict, total_papers: int, out_path: Path) -> None:
    entries = merged["entries"]
    per_source: dict[str, dict] = merged["per_source"]
    t0 = [e for e in entries if e["tier"] == "T0"]
    t1 = [e for e in entries if e["tier"] == "T1"]

    src_names = list(per_source.keys())
    src_label = " + ".join(source_display_label(s) for s in src_names)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# Citation Affiliation Audit\n\n")
        f.write(f"*Generated: {time.strftime('%Y-%m-%d')} via {src_label}*\n\n")
        f.write(
            "**What this is:** Papers that cite your work, where at least one "
            "author is affiliated with a notable institution.\n"
        )
        f.write(
            "This means \"researchers AT [institution] cited your tool\" -- "
            "not \"[institution] officially endorses your tool.\"\n\n"
        )
        # Per-source headline numbers so combined runs do not present
        # max-across-sources as a single combined truth.
        f.write("Per-source coverage of the {0} non-survey papers:\n".format(total_papers))
        for src in src_names:
            ps = per_source[src]
            f.write(
                f"- **{source_display_label(src)}**: {ps['found_count']} papers with citations; "
                f"{ps['unique_citing']} unique citing papers analyzed.\n"
            )
        f.write("\n")

        for tier_label, tier_entries in (
            ("Tier 0: Government, Space Agencies, National Labs, Defense, Foundation Model Cos", t0),
            ("Tier 1: Big Tech, Finance, Pharma, Healthcare, Industrial", t1),
        ):
            f.write(f"## {tier_label}\n\n")
            f.write(f"**{len(tier_entries)} entries**\n\n")
            if tier_entries:
                f.write("| Category | Institution | Country | Your Work Cited | Citing Paper | Year | Source |\n")
                f.write("|----------|-----------|---------|----------------|-------------|------|--------|\n")
                for e in sorted(tier_entries, key=lambda x: (x["category"], -(x.get("year") or 0))):
                    ct = (e.get("citing_title") or "")[:60].replace("|", "/")
                    inst = e["institution"].replace("|", "/")
                    cw = e["cited_work"][:35].replace("|", "/")
                    f.write(
                        f"| {e['category']} | {inst} | {e['country']} | {cw} | {ct} | "
                        f"{e.get('year') or ''} | {e.get('source', '')} |\n"
                    )
            f.write("\n")

        f.write("## Summary by Institution\n\n")
        inst_counts: dict[tuple, int] = {}
        for e in entries:
            key = (e["institution"], e["category"])
            inst_counts[key] = inst_counts.get(key, 0) + 1
        f.write("| Institution | Category | Work-Citations |\n")
        f.write("|-----------|----------|---------------|\n")
        for (inst, cat), count in sorted(inst_counts.items(), key=lambda x: -x[1]):
            f.write(f"| {inst} | {cat} | {count} |\n")

        f.write("\n## Coverage\n\n")
        f.write(f"**Sources used:** {src_label}\n\n")
        for src in src_names:
            ps = per_source[src]
            f.write(f"### {source_display_label(src)}\n\n")
            f.write(f"**Papers with citations:** {ps['found_count']}/{total_papers}\n\n")
            if ps.get("zero_cite"):
                zc = ps["zero_cite"]
                f.write(f"**Indexed but 0 citations ({len(zc)}):** ")
                f.write(", ".join(z[:40] for z in zc[:20]))
                if len(zc) > 20:
                    f.write(f", ... and {len(zc)-20} more")
                f.write("\n\n")
            if ps.get("not_found"):
                nf = ps["not_found"]
                f.write(f"**Not found ({len(nf)}):** ")
                f.write(", ".join(n[:40] for n in nf[:20]))
                if len(nf) > 20:
                    f.write(f", ... and {len(nf)-20} more")
                f.write("\n\n")
        f.write(
            "*OpenAlex coverage improves over time. Re-run in 3-6 months to "
            "capture newly indexed papers; Dimensions has better CS coverage "
            "and complements OpenAlex on per-paper citation graphs.*\n\n"
        )
        f.write(
            "*Cross-source dedup uses exact (institution, citing_title, cited_work) "
            "matching. Variants like 'Google' vs 'Google LLC' or punctuation-variant "
            "titles may produce near-duplicate rows that span sources.*\n"
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
    args = parser.parse_args(list(argv) if argv is not None else None)

    print("Loading papers from publications.json...")
    papers = load_papers(str(PROJECT_ROOT))
    if args.limit:
        papers = papers[: args.limit]
    print(f"  {len(papers)} papers (after excluding surveys)\n")

    results: list[tuple[str, dict]] = []

    if args.source in ("openalex", "both"):
        print(">>> Running OpenAlex provider\n")
        results.append(("openalex", fetch_openalex_entries(papers, verbose=True)))

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

    merged = _merge_results(results)
    out_path = Path(args.out)
    _write_markdown(merged, len(papers), out_path)

    t0 = sum(1 for e in merged["entries"] if e["tier"] == "T0")
    t1 = sum(1 for e in merged["entries"] if e["tier"] == "T1")
    print(f"\n{'=' * 60}")
    print(f"DONE -> {out_path}")
    print(f"Sources: {' + '.join(merged['per_source'].keys())}")
    for src, ps in merged["per_source"].items():
        print(f"  {src}: {ps['found_count']}/{len(papers)} papers with citations, "
              f"{ps['unique_citing']} unique citing papers")
    print(f"Tier 0: {t0} entries")
    print(f"Tier 1: {t1} entries")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(main())
