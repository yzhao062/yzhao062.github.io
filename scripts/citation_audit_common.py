"""Shared helpers for the citation-affiliation audit.

Used by both `citation_affiliation_audit.py` (OpenAlex) and
`citation_affiliation_audit_dimensions.py` (Dimensions). Owns:
- TIER0 / TIER1 institution regex patterns
- `match_patterns()` and `classify_institution()`
- `load_papers()` (reads data/publications.json, filters surveys)
- `dedup_entries()` and `normalize_doi()` / `normalize_arxiv_id()` helpers
- A shared `Entry` shape (plain dict) emitted by every source fetcher.

Entry shape (one row per (cited_work, citing_paper, institution)):

    {
        "tier": "T0" | "T1",
        "category": str,                # e.g., "Big Tech", "Space Agency"
        "institution": str,             # institution display name
        "country": str,                 # 2-letter country code if known
        "cited_work": str,              # short label for the user's paper
        "citing_title": str,            # title of the citing paper
        "citing_id": str,               # source-specific id (oa:..., dim:...)
        "year": int | None,
        "source": "openalex" | "dimensions",
    }
"""

from __future__ import annotations

import json
import os
import re
from typing import Iterable

EXCLUDE_TITLES_CONTAINING = [
    "comprehensive survey",
    "a survey on",
    "a survey of",
]

# Canonical display labels and ordering for source tokens. Used by the
# orchestrator's Markdown writer and by `dedup_entries` so the visible source
# column matches what the orchestrator docstrings promise (e.g.,
# `openalex+dimensions`, not the alphabetical `dimensions+openalex`).
SOURCE_DISPLAY: dict[str, str] = {
    "openalex": "OpenAlex",
    "dimensions": "Dimensions",
}
SOURCE_ORDER: list[str] = ["openalex", "dimensions"]


def _source_sort_key(token: str) -> tuple[int, str]:
    """Sort key that respects SOURCE_ORDER, with unknown tokens trailing."""
    if token in SOURCE_ORDER:
        return (SOURCE_ORDER.index(token), token)
    return (len(SOURCE_ORDER), token)


def source_display_label(token: str) -> str:
    """Render a single source token (e.g., 'openalex' -> 'OpenAlex')."""
    return SOURCE_DISPLAY.get(token, token.capitalize())

# Tier 0: government, space agencies, national labs, defense, foundation model cos,
# major international bodies. Patterns use \b on short acronyms to dodge substring
# collisions (e.g., \bNIST\b avoids "NISTagent").
TIER0_PATTERNS = [
    (r"European Space Agency|\bESA\b|ESOC|ESTEC", "Space Agency"),
    (r"NASA|Jet Propulsion Lab|\bJPL\b", "Space Agency"),
    (r"JAXA|Japan Aerospace", "Space Agency"),
    (r"\bISRO\b|Indian Space Research", "Space Agency"),
    (r"\bDLR\b|Deutsches Zentrum.*Luft", "Space Agency"),
    (r"\bCNES\b|Centre National d.Etudes Spatiales", "Space Agency"),
    (r"National Institute of Standards|\bNIST\b", "US Government"),
    (r"Department of Energy(?! Sci)(?!.*University)", "US Government"),
    (r"DARPA|Defense Advanced Research", "US Government"),
    (r"\bNOAA\b|National Oceanic", "US Government"),
    (r"National Institutes of Health|NIH Clinical Center", "US Government"),
    (r"Centers for Disease Control|\bCDC\b", "US Government"),
    (r"Food and Drug Admin|\bFDA\b", "US Government"),
    (r"Federal Aviation|\bFAA\b", "US Government"),
    (r"\bCISA\b|Cybersecurity.*Infrastructure", "US Government"),
    (r"Department of Homeland Security", "US Government"),
    (r"Federal Reserve|Board of Governors", "Central Bank"),
    (r"European Central Bank|\bECB\b", "Central Bank"),
    (r"\bBank for International Settlements\b", "Central Bank"),
    (r"Bundesbank", "Central Bank"),
    (r"Bank of England", "Central Bank"),
    (r"Bank of Japan", "Central Bank"),
    (r"People.s Bank of China|\bPBOC\b", "Central Bank"),
    (r"Los Alamos|LANL\b", "National Lab"),
    (r"Lawrence Livermore|\bLLNL\b", "National Lab"),
    (r"Sandia National", "National Lab"),
    (r"Oak Ridge|\bORNL\b", "National Lab"),
    (r"Argonne National", "National Lab"),
    (r"Brookhaven National", "National Lab"),
    (r"Pacific Northwest|\bPNNL\b", "National Lab"),
    (r"Idaho National|\bINL\b", "National Lab"),
    (r"Fermilab|Fermi National", "National Lab"),
    (r"SLAC National", "National Lab"),
    (r"\bCERN\b", "International Lab"),
    (r"\bDESY\b|Elektronen-Synchrotron", "International Lab"),
    (r"Max Planck", "Research Institute"),
    (r"Fraunhofer", "Research Institute"),
    (r"\bOpenAI\b", "Foundation Model Co"),
    (r"Anthropic", "Foundation Model Co"),
    (r"DeepMind|Google DeepMind", "Foundation Model Co"),
    (r"Meta\s*(AI|FAIR|Platforms)", "Foundation Model Co"),
    (r"Raytheon", "Defense"),
    (r"Lockheed Martin", "Defense"),
    (r"Northrop Grumman", "Defense"),
    (r"BAE Systems", "Defense"),
    (r"\bMITRE\b", "Defense/Research"),
    (r"RAND Corporation", "Defense/Research"),
    (r"Booz Allen", "Defense"),
    (r"Leidos", "Defense"),
    (r"World Health Organization", "International Org"),
    (r"\bIAEA\b|International Atomic Energy", "International Org"),
    (r"\bWorld Bank\b", "International Org"),
    (r"\bOECD\b", "International Org"),
    (r"\bNATO\b", "International Org"),
]

TIER1_PATTERNS = [
    (r"Google\b(?!.*DeepMind)", "Big Tech"),
    (r"Microsoft\b", "Big Tech"),
    (r"Amazon\b", "Big Tech"),
    (r"Apple\b(?!.*University)", "Big Tech"),
    (r"NVIDIA|Nvidia\b", "Big Tech"),
    (r"\bIntel\b(?!.*ligence)", "Big Tech"),
    (r"\bIBM\b", "Big Tech"),
    (r"Salesforce", "Big Tech"),
    (r"\bAdobe\b", "Big Tech"),
    (r"Samsung\b", "Big Tech"),
    (r"Huawei\b", "Big Tech"),
    (r"Tencent\b", "Big Tech"),
    (r"Alibaba\b", "Big Tech"),
    (r"Baidu\b", "Big Tech"),
    (r"ByteDance", "Big Tech"),
    (r"Goldman Sachs", "Finance"),
    (r"JPMorgan|J\.P\. Morgan", "Finance"),
    (r"Morgan Stanley", "Finance"),
    (r"Citadel\b", "Finance"),
    (r"Two Sigma", "Finance"),
    (r"BlackRock", "Finance"),
    (r"Bloomberg\b(?!.*University)", "Finance"),
    (r"Capital One", "Finance"),
    (r"Wells Fargo", "Finance"),
    (r"\bVisa\b(?!.*University)", "Finance"),
    (r"Pfizer", "Pharma"),
    (r"\bRoche\b", "Pharma"),
    (r"Novartis", "Pharma"),
    (r"AstraZeneca", "Pharma"),
    (r"\bMerck\b", "Pharma"),
    (r"Eli Lilly", "Pharma"),
    (r"Sanofi", "Pharma"),
    (r"Moderna", "Pharma"),
    (r"Mayo Clinic", "Healthcare"),
    (r"Cleveland Clinic", "Healthcare"),
    (r"Siemens\b", "Industrial"),
    (r"\bBosch\b", "Industrial"),
    (r"Honeywell", "Industrial"),
    (r"\bGeneral Electric\b|\bGE Research\b|\bGE Global Research\b", "Industrial"),
    (r"Ericsson", "Telecom"),
    (r"\bNokia\b", "Telecom"),
    (r"\bCisco\b", "Telecom"),
    (r"Qualcomm", "Telecom"),
    (r"\bTesla\b", "Automotive"),
    (r"SpaceX", "Aerospace"),
    (r"\bWalmart\b", "Retail"),
    (r"Deloitte", "Consulting"),
    (r"McKinsey", "Consulting"),
    (r"\bPwC\b|PricewaterhouseCoopers", "Consulting"),
    (r"Accenture", "Consulting"),
]


def match_patterns(name: str, patterns):
    """Return (category, pattern) for the first match, or (None, None)."""
    if not name:
        return None, None
    for pattern, category in patterns:
        if re.search(pattern, name, re.IGNORECASE):
            return category, pattern
    return None, None


def classify_institution(name: str):
    """Return ("T0"|"T1"|None, category|None) for an institution name."""
    cat, _ = match_patterns(name, TIER0_PATTERNS)
    if cat:
        return "T0", cat
    cat, _ = match_patterns(name, TIER1_PATTERNS)
    if cat:
        return "T1", cat
    return None, None


def load_papers(project_root: str):
    """Load non-survey papers from data/publications.json.

    Returns a list of dicts with keys: title, venue, year, id, paper_url.
    Surveys are filtered using EXCLUDE_TITLES_CONTAINING.
    """
    path = os.path.join(project_root, "data", "publications.json")
    with open(path, encoding="utf-8") as f:
        pubs = json.load(f)

    papers = []
    for p in pubs:
        title = p.get("title", "")
        lower = title.lower()
        if any(exc in lower for exc in EXCLUDE_TITLES_CONTAINING):
            continue
        papers.append({
            "title": title,
            "venue": p.get("venue", ""),
            "year": p.get("year"),
            "id": p.get("id", ""),
            "paper_url": p.get("paper_url", ""),
        })
    return papers


def short_label(title: str, venue: str, *, title_len: int = 45, venue_len: int = 20) -> str:
    """Compact label for a cited paper, used in the output tables."""
    return f"{title[:title_len]} ({venue[:venue_len]})"


def normalize_doi(paper_url: str):
    """Extract a bare DOI (no scheme/host) from a URL, or None."""
    if not paper_url:
        return None
    m = re.search(r"doi\.org/(.+)$", paper_url)
    if m:
        return m.group(1).strip()
    if paper_url.startswith("10."):
        return paper_url.strip()
    return None


def normalize_arxiv_id(paper_url: str):
    """Extract an arXiv ID (e.g., 2401.12345) from a URL, or None."""
    if not paper_url:
        return None
    if "arxiv.org" not in paper_url:
        return None
    m = re.search(r"(\d{4}\.\d{4,5})", paper_url)
    return m.group(1) if m else None


def dedup_entries(entries: Iterable[dict]) -> list[dict]:
    """Deduplicate entries by (institution, citing_title, cited_work).

    When the same entry appears from multiple sources, keep the first one
    and concatenate the source markers (e.g., "openalex+dimensions").
    """
    by_key: dict[tuple, dict] = {}
    for e in entries:
        key = (
            e.get("institution", ""),
            e.get("citing_title") or "",
            e.get("cited_work", ""),
        )
        existing = by_key.get(key)
        if existing is None:
            by_key[key] = dict(e)
            continue
        sources = set(existing.get("source", "").split("+"))
        sources.add(e.get("source", ""))
        sources.discard("")
        existing["source"] = "+".join(sorted(sources, key=_source_sort_key))
    return list(by_key.values())
