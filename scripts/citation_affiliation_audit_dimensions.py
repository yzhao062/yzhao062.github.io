"""Dimensions Analytics API provider for the citation-affiliation audit.

Mirror of `citation_affiliation_audit.py` (OpenAlex), using Digital Science's
Dimensions DSL via `dimcli`. Designed to be both:
- callable as a module:  `fetch_dimensions_entries(papers, ...)` returns
  a list of Entry dicts conforming to the shape in `citation_audit_common`.
- runnable standalone:    writes `citation-affiliation-audit-dimensions.md`
  in the same Markdown shape as the OpenAlex script.

Auth: reads `DIMENSIONS_API_KEY` from .env, passes it to `dimcli.login(key=...)`
so credentials live in one place with the other repo secrets rather than in
`~/.dimcli/dsl.ini`.

Run:
    pip install dimcli python-dotenv
    python scripts/citation_affiliation_audit_dimensions.py [--limit N] [--max-citing-pages K]
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import time
from pathlib import Path
from typing import Iterable

from citation_audit_common import (
    TIER0_PATTERNS,
    TIER1_PATTERNS,
    classify_institution,
    dedup_entries,
    load_papers,
    normalize_arxiv_id,
    normalize_doi,
    short_label,
)

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
ENV_FILE = PROJECT_ROOT / ".env"

DIMENSIONS_FIELDS_PUB = "id+title+times_cited"
DIMENSIONS_FIELDS_CITING = (
    "id+title+year+authors+research_orgs"
)


def _ensure_dimcli_login(verbose: bool = False):
    """Authenticate to Dimensions using DIMENSIONS_API_KEY from .env.

    Returns a `dimcli.Dsl()` client. Raises RuntimeError on misconfiguration.
    """
    try:
        from dotenv import load_dotenv
    except ImportError as exc:
        raise RuntimeError("pip install python-dotenv") from exc
    try:
        import dimcli
    except ImportError as exc:
        raise RuntimeError("pip install dimcli") from exc

    if ENV_FILE.exists():
        load_dotenv(ENV_FILE)
    key = os.environ.get("DIMENSIONS_API_KEY", "").strip()
    if not key:
        raise RuntimeError(
            "DIMENSIONS_API_KEY missing from .env (see .env.example)"
        )

    dimcli.login(key=key, verbose=verbose)
    return dimcli.Dsl(verbose=verbose)


def _escape_dsl(value: str) -> str:
    """Escape a string for inclusion inside DSL double-quoted literals."""
    return value.replace("\\", "\\\\").replace('"', '\\"')


def _sanitize_dsl_for_phrase(value: str) -> str:
    """Sanitize a free-text string for use in a DSL ``for "..."`` clause.

    Dimensions DSL parses operators like ``:``, ``+``, ``-``, ``(``, ``)``,
    ``&``, ``|`` as syntax tokens even inside quoted phrases. A raw paper
    title with the common ``Title: Subtitle`` shape (or any of these
    characters) lexer-errors before the search runs. Replace every
    non-word non-space character with a space and collapse runs of
    whitespace, leaving a plain word bag.

    This is safe for the title-search fallback because:
    (a) we are using the search for fuzzy recall, not exact-phrase match;
    (b) the caller verifies the candidate with prefix-anchor + word-overlap
        scoring after fetching, so degrading to a bag of words does not
        weaken match quality;
    (c) the alternative (escaping every reserved character) is brittle
        because the DSL grammar can evolve.
    """
    cleaned = re.sub(r"[^\w\s]", " ", value)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def _query_dimensions(dsl, query: str, context: str):
    """Run a DSL query and raise on a non-empty `res.errors`.

    The `dimcli` client returns a result object whose `.errors` attribute is
    populated for DSL parse errors, missing field permissions, and transient
    API errors. Without this check, callers reading `res.publications` directly
    would silently treat error states as empty result sets, which turns a real
    API failure into a false negative audit row. `context` is included in the
    raised message so the failing call site is obvious from the traceback.
    """
    res = dsl.query(query)
    errs = getattr(res, "errors", None)
    if errs:
        raise RuntimeError(f"Dimensions {context} failed: {errs}")
    return res


def _find_dimensions_pub_id(dsl, title: str, paper_url: str):
    """Locate a Dimensions publication for a paper.

    Tries arXiv ID, then DOI, then a fuzzy title search using the same
    prefix-anchor + word-overlap rules as the OpenAlex finder.

    Returns (pub_id, found_title, times_cited) or (None, None, 0).
    """
    arxiv_id = normalize_arxiv_id(paper_url)
    if arxiv_id:
        # Dimensions stores arxiv_id with the `arXiv:` prefix; querying the
        # bare numeric form returns zero results even when the paper is
        # indexed (verified for ECOD via dimensions_probe2.py).
        prefixed = arxiv_id if arxiv_id.startswith("arXiv:") else f"arXiv:{arxiv_id}"
        q = (
            f'search publications where arxiv_id = "{_escape_dsl(prefixed)}" '
            f"return publications[{DIMENSIONS_FIELDS_PUB}] limit 1"
        )
        res = _query_dimensions(dsl, q, f"find pub by arxiv_id={prefixed}")
        if res.publications:
            p = res.publications[0]
            return p.get("id"), p.get("title", ""), p.get("times_cited", 0) or 0

    doi = normalize_doi(paper_url)
    if doi:
        q = (
            f'search publications where doi = "{_escape_dsl(doi)}" '
            f"return publications[{DIMENSIONS_FIELDS_PUB}] limit 1"
        )
        res = _query_dimensions(dsl, q, f"find pub by doi={doi}")
        if res.publications:
            p = res.publications[0]
            return p.get("id"), p.get("title", ""), p.get("times_cited", 0) or 0

    # Fuzzy title fallback. Sanitize before quoting because DSL operators
    # like `:` lexer-error even inside a quoted phrase. Scope to `title_only`
    # search type: the default `full_data` matches any body text containing
    # the keywords and scatters across irrelevant papers (verified for PyOD /
    # ECOD / ADBench / TrustLLM via dimensions_probe2.py).
    phrase = _escape_dsl(_sanitize_dsl_for_phrase(title))
    q = (
        f'search publications in title_only for "{phrase}" '
        f"return publications[{DIMENSIONS_FIELDS_PUB}] limit 5"
    )
    res = _query_dimensions(dsl, q, f"find pub by title={title[:60]!r}")
    candidates = res.publications or []
    if not candidates:
        return None, None, 0

    def words(t: str) -> set[str]:
        return set(re.findall(r"\w{3,}", (t or "").lower()))

    def norm(t: str) -> str:
        return re.sub(r"[^a-z0-9 ]", "", (t or "").lower()).strip()

    title_words = words(title)
    title_norm = norm(title)
    if not title_words:
        return None, None, 0

    prefix_match = re.match(r"^([A-Za-z0-9\-]+)\s*:", title)
    prefix_anchor = prefix_match.group(1).lower() if prefix_match else None

    # Pass 1: exact normalized title match
    for cand in candidates:
        if norm(cand.get("title", "")) == title_norm:
            return cand.get("id"), cand.get("title", ""), cand.get("times_cited", 0) or 0

    # Pass 2: prefix anchor + word overlap
    for cand in candidates:
        found_title = cand.get("title", "")
        found_norm = norm(found_title)
        found_words = words(found_title)
        if not found_words:
            continue
        overlap = len(title_words & found_words) / len(title_words)
        if prefix_anchor:
            if prefix_anchor not in found_norm:
                continue
            if overlap >= 0.5:
                return cand.get("id"), found_title, cand.get("times_cited", 0) or 0
        else:
            if overlap >= 0.7:
                return cand.get("id"), found_title, cand.get("times_cited", 0) or 0

    return None, None, 0


def _extract_institutions(citing_pub: dict) -> list[dict]:
    """Pull institution records from a Dimensions publication object.

    Prefers GRID-normalized `research_orgs`; falls back to `authors[].affiliations`.
    Returns a list of {name, country} dicts, deduplicated by name.
    """
    seen: set[str] = set()
    out: list[dict] = []

    for org in citing_pub.get("research_orgs", []) or []:
        if isinstance(org, dict):
            name = org.get("name") or ""
            country = org.get("country_name") or org.get("country") or ""
        else:
            name = str(org)
            country = ""
        if name and name not in seen:
            seen.add(name)
            out.append({"name": name, "country": country})

    if out:
        return out

    for author in citing_pub.get("authors", []) or []:
        for aff in author.get("affiliations", []) or []:
            if isinstance(aff, dict):
                name = aff.get("name") or aff.get("raw_affiliation") or ""
                country = aff.get("country_name") or aff.get("country") or ""
            else:
                name = str(aff)
                country = ""
            if name and name not in seen:
                seen.add(name)
                out.append({"name": name, "country": country})
    return out


def _get_citing_publications(dsl, pub_id: str, *, max_pages: int = 5, page_size: int = 1000):
    """Return citing-publication objects for a given Dimensions pub id.

    Paginates via DSL `skip` until `max_pages * page_size` is reached or
    the result set is exhausted.
    """
    results: list[dict] = []
    for page in range(max_pages):
        skip = page * page_size
        q = (
            f'search publications where reference_ids = "{_escape_dsl(pub_id)}" '
            f"return publications[{DIMENSIONS_FIELDS_CITING}] "
            f"limit {page_size} skip {skip}"
        )
        res = _query_dimensions(
            dsl, q, f"fetch citing publications for {pub_id} page {page}"
        )
        page_results = res.publications or []
        if not page_results:
            break
        results.extend(page_results)
        if len(page_results) < page_size:
            break
        time.sleep(0.2)
    return results


def fetch_dimensions_entries(
    papers: list[dict],
    *,
    max_citing_pages: int = 5,
    verbose: bool = True,
    log=print,
) -> dict:
    """Run the Dimensions citation-affiliation audit over the given papers.

    Returns a dict with keys:
        entries: list of Entry dicts (see citation_audit_common module docstring)
        found_count, zero_cite, not_found: ints/lists for the coverage section
        unique_citing: int (count of unique citing publication IDs)
    """
    dsl = _ensure_dimcli_login(verbose=False)

    found_works: dict[str, str] = {}
    not_found: list[str] = []
    zero_cite: list[str] = []

    if verbose:
        log("=" * 60)
        log("PHASE 1: Finding Dimensions publication IDs")
        log("=" * 60)

    for i, p in enumerate(papers):
        title = p["title"]
        venue = p.get("venue", "")
        short = f"{title[:50]}... ({venue})"
        if verbose:
            log(f"  [{i+1}/{len(papers)}] {short}")

        pub_id, _, cite_count = _find_dimensions_pub_id(dsl, title, p.get("paper_url", ""))
        if pub_id and cite_count > 0:
            found_works[pub_id] = short_label(title, venue)
            if verbose:
                log(f"    -> {pub_id} (times_cited={cite_count})")
        elif pub_id:
            zero_cite.append(short)
            if verbose:
                log(f"    -> {pub_id} (0 citations, skipping)")
        else:
            not_found.append(short)
            if verbose:
                log("    -> NOT FOUND")
        time.sleep(0.15)

    if verbose:
        log(f"\nFound {len(found_works)} papers with citations on Dimensions")
        log(f"0 citations: {len(zero_cite)}")
        log(f"Not found: {len(not_found)}")
        log("\n" + "=" * 60)
        log("PHASE 2: Fetching citing publications (per-work)")
        log("=" * 60)

    all_entries: list[dict] = []
    citing_ids: set[str] = set()

    for idx, (pub_id, short_name) in enumerate(found_works.items()):
        if verbose:
            log(f"  [{idx+1}/{len(found_works)}] {short_name}")
        citing = _get_citing_publications(dsl, pub_id, max_pages=max_citing_pages)
        if verbose:
            log(f"    -> {len(citing)} citing publications")

        for c in citing:
            cid = c.get("id")
            if cid:
                citing_ids.add(cid)
            institutions = _extract_institutions(c)
            for inst in institutions:
                tier, category = classify_institution(inst["name"])
                if tier is None:
                    continue
                all_entries.append({
                    "tier": tier,
                    "category": category,
                    "institution": inst["name"],
                    "country": inst.get("country", ""),
                    "cited_work": short_name,
                    "citing_title": c.get("title", ""),
                    "citing_id": cid or "",
                    "year": c.get("year"),
                    "source": "dimensions",
                })
                if verbose and tier == "T0":
                    log(f"    ** T0 [{category}] {inst['name'][:40]}")

        time.sleep(0.3)

    return {
        "entries": dedup_entries(all_entries),
        "found_count": len(found_works),
        "zero_cite": zero_cite,
        "not_found": not_found,
        "unique_citing": len(citing_ids),
    }


def _write_standalone_markdown(result: dict, total_papers: int, out_path: Path) -> None:
    entries = result["entries"]
    t0 = [e for e in entries if e["tier"] == "T0"]
    t1 = [e for e in entries if e["tier"] == "T1"]

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# Citation Affiliation Audit (Dimensions)\n\n")
        f.write(f"*Generated: {time.strftime('%Y-%m-%d')} via Dimensions Analytics API*\n\n")
        f.write(
            f"Surveys excluded. {result['found_count']} papers with citations on Dimensions "
            f"(out of {total_papers} non-survey papers). "
            f"{result['unique_citing']} unique citing publications analyzed.\n\n"
        )

        for tier_label, tier_entries in (("Tier 0", t0), ("Tier 1", t1)):
            f.write(f"## {tier_label}\n\n")
            f.write(f"**{len(tier_entries)} entries**\n\n")
            if tier_entries:
                f.write("| Category | Institution | Country | Your Work Cited | Citing Paper | Year |\n")
                f.write("|----------|-----------|---------|----------------|-------------|------|\n")
                for e in sorted(tier_entries, key=lambda x: (x["category"], -(x.get("year") or 0))):
                    ct = (e.get("citing_title") or "")[:60].replace("|", "/")
                    inst = e["institution"].replace("|", "/")
                    cw = e["cited_work"][:35].replace("|", "/")
                    f.write(
                        f"| {e['category']} | {inst} | {e['country']} | {cw} | {ct} | {e.get('year') or ''} |\n"
                    )
            f.write("\n")


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--limit", type=int, default=None,
        help="Process only the first N papers (for quick verification)."
    )
    parser.add_argument(
        "--max-citing-pages", type=int, default=5,
        help="Max pages of citing publications per work (page size 1000)."
    )
    parser.add_argument(
        "--out", default=str(PROJECT_ROOT / "citation-affiliation-audit-dimensions.md"),
        help="Output Markdown path."
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    print("Loading papers from publications.json...")
    papers = load_papers(str(PROJECT_ROOT))
    if args.limit:
        papers = papers[: args.limit]
    print(f"  {len(papers)} papers (after excluding surveys)\n")

    result = fetch_dimensions_entries(
        papers, max_citing_pages=args.max_citing_pages, verbose=True
    )

    out_path = Path(args.out)
    _write_standalone_markdown(result, len(papers), out_path)

    print(f"\n{'=' * 60}")
    print(f"DONE -> {out_path}")
    print(f"Papers found on Dimensions: {result['found_count']}/{len(papers)}")
    print(f"Unique citing publications: {result['unique_citing']}")
    t0 = sum(1 for e in result["entries"] if e["tier"] == "T0")
    t1 = sum(1 for e in result["entries"] if e["tier"] == "T1")
    print(f"Tier 0: {t0} entries")
    print(f"Tier 1: {t1} entries")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(main())
