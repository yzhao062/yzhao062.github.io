#!/usr/bin/env python3
"""Smoke test for Dimensions Analytics API access.

Verifies that DIMENSIONS_API_KEY in .env is valid and that the scientometric
access tier returned by Digital Science includes the fields needed by the
citation-affiliation audit:

    times_cited        citation count
    reference_ids      papers this paper cites
    authors            author objects with affiliations (fallback)
    research_orgs      GRID-normalized institution objects -- the primary
                       field the audit provider reads for affiliation matching
    category_for       Fields of Research classification (paid-tier signal)

Usage:
    pip install dimcli python-dotenv
    python skills/citation-audit/scripts/dimensions_smoke_test.py
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
ENV_FILE = REPO_ROOT / ".env"

PROBE_QUERY = """
search publications
    for "\\"PyOD\\" \\"anomaly detection\\" Python"
return publications[id+title+year+times_cited+reference_ids+authors+research_orgs+category_for]
limit 5
"""

FIELDS = [
    "id",
    "title",
    "year",
    "times_cited",
    "reference_ids",
    "authors",
    "research_orgs",
    "category_for",
]


def _field_summary(value: object) -> str:
    if value is None:
        return "NULL"
    if isinstance(value, list):
        return f"list[{len(value)}]"
    if isinstance(value, str):
        snippet = value if len(value) <= 60 else value[:57] + "..."
        return f"str: {snippet!r}"
    return f"{type(value).__name__}: {value!r}"


def main() -> int:
    try:
        from dotenv import load_dotenv
    except ImportError:
        print("ERROR: pip install python-dotenv", file=sys.stderr)
        return 1

    try:
        import dimcli
    except ImportError:
        print("ERROR: pip install dimcli", file=sys.stderr)
        return 1

    if not ENV_FILE.exists():
        print(f"ERROR: .env not found at {ENV_FILE}", file=sys.stderr)
        return 1
    load_dotenv(ENV_FILE)

    key = os.environ.get("DIMENSIONS_API_KEY", "").strip()
    if not key:
        print("ERROR: DIMENSIONS_API_KEY missing or empty in .env", file=sys.stderr)
        return 1

    print(f"Authenticating to Dimensions (key length: {len(key)} chars)...")
    dimcli.login(key=key, verbose=False)
    dsl = dimcli.Dsl(verbose=False)

    print(f"Running probe query against PyOD...\n")
    res = dsl.query(PROBE_QUERY)

    if res.errors:
        print("Query returned errors:")
        for err in res.errors:
            print(f"  {err}")
        return 1

    pubs = res.publications or []
    print(f"Returned {len(pubs)} publications.\n")
    if not pubs:
        print("No results. Access tier may not include publication search,")
        print("or the query string did not match the corpus.")
        return 1

    print("Field availability per result:\n")
    for idx, pub in enumerate(pubs, 1):
        title = pub.get("title", "?")
        if len(title) > 70:
            title = title[:67] + "..."
        print(f"[{idx}] {title}")
        for field in FIELDS:
            print(f"    {field:<16} {_field_summary(pub.get(field))}")
        print()

    print("Coverage check across all results:")
    for field in FIELDS:
        populated = sum(1 for p in pubs if p.get(field) not in (None, [], ""))
        status = "OK" if populated == len(pubs) else f"populated in {populated}/{len(pubs)}"
        print(f"    {field:<16} {status}")

    # Affiliation-source check: the provider prefers research_orgs (GRID-normalized)
    # and falls back to authors[].affiliations. The audit needs at least one of these
    # populated per result to classify institutions.
    research_orgs_present = sum(1 for p in pubs if p.get("research_orgs"))
    authors_affil_present = 0
    for p in pubs:
        for author in p.get("authors", []) or []:
            if author.get("affiliations"):
                authors_affil_present += 1
                break
    either_present = 0
    for p in pubs:
        if p.get("research_orgs"):
            either_present += 1
            continue
        for author in p.get("authors", []) or []:
            if author.get("affiliations"):
                either_present += 1
                break
    print(
        f"    research_orgs (preferred):                       "
        f"{research_orgs_present}/{len(pubs)}"
    )
    print(
        f"    authors[].affiliations (fallback):               "
        f"{authors_affil_present}/{len(pubs)}"
    )
    print(
        f"    at least one affiliation source per result:      "
        f"{either_present}/{len(pubs)}"
    )
    if either_present < len(pubs):
        print(
            "    WARNING: some results have no affiliation data; the audit will "
            "skip them."
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
