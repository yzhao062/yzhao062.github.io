"""Shared helpers for the citation-affiliation audit.

Used by both `citation_affiliation_audit.py` (OpenAlex) and
`citation_affiliation_audit_dimensions.py` (Dimensions). Owns:
- TIER0 / TIER1 institution regex patterns
- `match_patterns()` and `classify_institution()`
- `load_papers()` (reads data/publications.json, filters surveys)
- `dedup_entries()` and `normalize_doi()` / `normalize_arxiv_id()` helpers
- `load_coauthors()`, `load_work_authors()` and `screen_self_citation()` for the self / co-author screen
- A shared `Entry` shape (plain dict) emitted by every source fetcher.

Entry shape (one row per (cited_work, citing_paper, organization)):

    {
        "tier": "T0" | "T1",
        "category": str,                # e.g., "Big Tech", "Space Agency"
        "org": str,                     # canonical organization, e.g. "AstraZeneca"
        "institution": str,             # raw institution display name(s), "; "-joined after dedup
        "country": str,                 # country name or code if known, ", "-joined after dedup
        "cited_work": str,              # short label for the user's paper
        "citing_title": str,            # title of the citing paper
        "citing_id": str,               # source-specific id (oa:..., dim:...)
        "authors": list[str],           # citing-paper author names, for the self-citation screen
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
    (r"European Space Agency|\bESA\b|ESOC|ESTEC", "Space Agency", "European Space Agency"),
    (r"NASA|Jet Propulsion Lab|\bJPL\b", "Space Agency", "NASA / JPL"),
    (r"JAXA|Japan Aerospace", "Space Agency", "JAXA"),
    (r"\bISRO\b|Indian Space Research", "Space Agency", "ISRO"),
    (r"\bDLR\b|Deutsches Zentrum.*Luft", "Space Agency", "DLR"),
    (r"\bCNES\b|Centre National d.Etudes Spatiales", "Space Agency", "CNES"),
    (r"National Institute of Standards|\bNIST\b", "US Government", "NIST"),
    (r"Department of Energy(?! Sci)(?!.*University)", "US Government", "US Department of Energy"),
    (r"DARPA|Defense Advanced Research", "US Government", "DARPA"),
    (r"\bNOAA\b|National Oceanic", "US Government", "NOAA"),
    (r"National Institutes of Health|NIH Clinical Center", "US Government", "NIH"),
    (r"Centers for Disease Control|\bCDC\b", "US Government", "CDC"),
    (r"Food and Drug Admin|\bFDA\b", "US Government", "FDA"),
    (r"Federal Aviation|\bFAA\b", "US Government", "FAA"),
    (r"\bCISA\b|Cybersecurity.*Infrastructure", "US Government", "CISA"),
    (r"Department of Homeland Security", "US Government", "DHS"),
    (r"Federal Reserve|Board of Governors", "Central Bank", "Federal Reserve"),
    (r"European Central Bank|\bECB\b", "Central Bank", "European Central Bank"),
    (r"\bBank for International Settlements\b", "Central Bank", "Bank for International Settlements"),
    (r"Bundesbank", "Central Bank", "Deutsche Bundesbank"),
    (r"Bank of England", "Central Bank", "Bank of England"),
    (r"Bank of Japan", "Central Bank", "Bank of Japan"),
    (r"People.s Bank of China|\bPBOC\b", "Central Bank", "People's Bank of China"),
    (r"Los Alamos|LANL\b", "National Lab", "Los Alamos National Laboratory"),
    (r"Lawrence Livermore|\bLLNL\b", "National Lab", "Lawrence Livermore National Laboratory"),
    (r"Sandia National", "National Lab", "Sandia National Laboratories"),
    (r"Oak Ridge|\bORNL\b", "National Lab", "Oak Ridge National Laboratory"),
    (r"Argonne National", "National Lab", "Argonne National Laboratory"),
    (r"Brookhaven National", "National Lab", "Brookhaven National Laboratory"),
    (r"Pacific Northwest|\bPNNL\b", "National Lab", "Pacific Northwest National Laboratory"),
    (r"Idaho National|\bINL\b", "National Lab", "Idaho National Laboratory"),
    (r"Fermilab|Fermi National", "National Lab", "Fermilab"),
    (r"SLAC National", "National Lab", "SLAC National Accelerator Laboratory"),
    (r"\bCERN\b", "International Lab", "CERN"),
    (r"\bDESY\b|Elektronen-Synchrotron", "International Lab", "DESY"),
    (r"Max Planck", "Research Institute", "Max Planck Society"),
    (r"Fraunhofer", "Research Institute", "Fraunhofer"),
    (r"\bOpenAI\b", "Foundation Model Co", "OpenAI"),
    (r"Anthropic", "Foundation Model Co", "Anthropic"),
    (r"DeepMind|Google DeepMind", "Foundation Model Co", "Google DeepMind"),
    (r"Meta\s*(AI|FAIR|Platforms)", "Foundation Model Co", "Meta"),
    (r"Raytheon", "Defense", "Raytheon"),
    (r"Lockheed Martin", "Defense", "Lockheed Martin"),
    (r"Northrop Grumman", "Defense", "Northrop Grumman"),
    (r"BAE Systems", "Defense", "BAE Systems"),
    (r"\bMITRE\b", "Defense/Research", "MITRE"),
    (r"RAND Corporation", "Defense/Research", "RAND Corporation"),
    (r"Booz Allen", "Defense", "Booz Allen Hamilton"),
    (r"Leidos", "Defense", "Leidos"),
    (r"World Health Organization", "International Org", "World Health Organization"),
    (r"\bIAEA\b|International Atomic Energy", "International Org", "IAEA"),
    (r"\bWorld Bank\b", "International Org", "World Bank"),
    (r"\bOECD\b", "International Org", "OECD"),
    (r"\bNATO\b", "International Org", "NATO"),
]

TIER1_PATTERNS = [
    (r"Google\b(?!.*DeepMind)", "Big Tech", "Google"),
    (r"Microsoft\b", "Big Tech", "Microsoft"),
    (r"Amazon\b", "Big Tech", "Amazon"),
    (r"Apple\b(?!.*University)", "Big Tech", "Apple"),
    (r"NVIDIA|Nvidia\b", "Big Tech", "NVIDIA"),
    (r"\bIntel\b(?!.*ligence)", "Big Tech", "Intel"),
    (r"\bIBM\b", "Big Tech", "IBM"),
    (r"Salesforce", "Big Tech", "Salesforce"),
    (r"\bAdobe\b", "Big Tech", "Adobe"),
    (r"Samsung\b", "Big Tech", "Samsung"),
    (r"Huawei\b", "Big Tech", "Huawei"),
    (r"Tencent\b", "Big Tech", "Tencent"),
    (r"Alibaba\b", "Big Tech", "Alibaba"),
    (r"Baidu\b", "Big Tech", "Baidu"),
    (r"ByteDance", "Big Tech", "ByteDance"),
    (r"Goldman Sachs", "Finance", "Goldman Sachs"),
    (r"JPMorgan|J\.P\. Morgan", "Finance", "JPMorgan Chase"),
    (r"Morgan Stanley", "Finance", "Morgan Stanley"),
    (r"Citadel\b", "Finance", "Citadel"),
    (r"Two Sigma", "Finance", "Two Sigma"),
    (r"BlackRock", "Finance", "BlackRock"),
    (r"Bloomberg\b(?!.*University)", "Finance", "Bloomberg"),
    (r"Capital One", "Finance", "Capital One"),
    (r"Wells Fargo", "Finance", "Wells Fargo"),
    (r"\bVisa\b(?!.*University)", "Finance", "Visa"),
    (r"Pfizer", "Pharma", "Pfizer"),
    (r"\bRoche\b", "Pharma", "Roche"),
    (r"Novartis", "Pharma", "Novartis"),
    (r"AstraZeneca", "Pharma", "AstraZeneca"),
    (r"\bMerck\b", "Pharma", "Merck"),
    (r"Eli Lilly", "Pharma", "Eli Lilly"),
    (r"Sanofi", "Pharma", "Sanofi"),
    (r"Moderna", "Pharma", "Moderna"),
    (r"Mayo Clinic", "Healthcare", "Mayo Clinic"),
    (r"Cleveland Clinic", "Healthcare", "Cleveland Clinic"),
    (r"Siemens\b", "Industrial", "Siemens"),
    (r"\bBosch\b", "Industrial", "Bosch"),
    (r"Honeywell", "Industrial", "Honeywell"),
    (r"\bGeneral Electric\b|\bGE Research\b|\bGE Global Research\b", "Industrial", "General Electric"),
    (r"Ericsson", "Telecom", "Ericsson"),
    (r"\bNokia\b", "Telecom", "Nokia"),
    (r"\bCisco\b", "Telecom", "Cisco"),
    (r"Qualcomm", "Telecom", "Qualcomm"),
    (r"\bTesla\b", "Automotive", "Tesla"),
    (r"SpaceX", "Aerospace", "SpaceX"),
    (r"\bWalmart\b", "Retail", "Walmart"),
    (r"Deloitte", "Consulting", "Deloitte"),
    (r"McKinsey", "Consulting", "McKinsey"),
    (r"\bPwC\b|PricewaterhouseCoopers", "Consulting", "PwC"),
    (r"Accenture", "Consulting", "Accenture"),
]


def match_patterns(name: str, patterns):
    """Return (category, canonical_org) for the first match, or (None, None)."""
    if not name:
        return None, None
    for pattern, category, canonical in patterns:
        if re.search(pattern, name, re.IGNORECASE):
            return category, canonical
    return None, None


def classify_institution(name: str):
    """Return (tier, category, canonical_org) for an institution name.

    Every element is None when the name matches neither tier. The canonical
    organization collapses legal entities of one company ("AstraZeneca AB",
    "AstraZeneca UK Ltd") so a citing paper counts once per organization.
    """
    cat, org = match_patterns(name, TIER0_PATTERNS)
    if cat:
        return "T0", cat, org
    cat, org = match_patterns(name, TIER1_PATTERNS)
    if cat:
        return "T1", cat, org
    return None, None, None


# ── Self / co-author citation screen ────────────────────────────────────

PI_NAME = "Yue Zhao"


def name_key(name: str) -> frozenset:
    """Order-insensitive key for a person name.

    Lowercases, joins hyphenated given names, strips footnote marks, and drops
    single-letter initials, so "Ryan A. Rossi", "Rossi, Ryan" and "Ryan Rossi"
    share a key, as do "Yue Zhao" and "Zhao Yue".
    """
    cleaned = re.sub(r"[-‐‑]", "", name or "")
    tokens = re.findall(r"[^\W\d_]+", cleaned.lower())
    return frozenset(t for t in tokens if len(t) > 1)


_PLACEHOLDER_TOKENS = {"many", "other", "others", "et", "al", "authors"}


def _placeholder(key: frozenset) -> bool:
    """True for author-list fillers such as "and many others" or "et al.", which are not names."""
    return bool(key & _PLACEHOLDER_TOKENS)


def load_coauthors(project_root: str, min_papers: int = 2) -> dict:
    """Map name_key -> display name for the PI and frequent co-authors.

    Reads the author strings in data/publications.json. A co-author must share
    at least `min_papers` papers with the PI; the threshold keeps one-off
    collaborators with common names from screening out unrelated citers.
    """
    path = os.path.join(project_root, "data", "publications.json")
    with open(path, encoding="utf-8") as f:
        pubs = json.load(f)
    counts: dict[frozenset, int] = {}
    display: dict[frozenset, str] = {}
    for p in pubs:
        seen: set[frozenset] = set()
        for raw in re.split(r",|\band\b", p.get("authors", "") or ""):
            raw = re.sub(r"[*†‡♠♣♥♦\d]", "", raw).strip(" .")
            key = name_key(raw)
            if len(key) < 2 or key in seen or _placeholder(key):
                continue
            seen.add(key)
            counts[key] = counts.get(key, 0) + 1
            display.setdefault(key, raw)
    out = {k: display[k] for k, c in counts.items() if c >= min_papers}
    out[name_key(PI_NAME)] = PI_NAME
    return out


def load_work_authors(project_root: str) -> dict:
    """Map each paper's table label (see short_label) to its authors' name keys.

    Two papers that share a label (the two SUOD papers) share one author set.
    """
    path = os.path.join(project_root, "data", "publications.json")
    with open(path, encoding="utf-8") as f:
        pubs = json.load(f)
    out: dict[str, set] = {}
    for p in pubs:
        keys = out.setdefault(short_label(p.get("title", "")), set())
        for raw in re.split(r",|\band\b", p.get("authors", "") or ""):
            key = name_key(re.sub(r"[*†‡♠♣♥♦\d]", "", raw).strip(" ."))
            if len(key) >= 2 and not _placeholder(key):
                keys.add(key)
    return out


def screen_self_citation(authors: Iterable[str], coauthors: dict, cited_authors: set | None = None):
    """Classify a citing paper by its author list.

    Returns (verdict, matched_names) where verdict is:
      "self"      the PI is an author;
      "coauthor"  any author of the cited work is an author (a co-author citing their
                  own paper, however few papers they share with the PI), or two or more
                  frequent co-authors are;
      "possible"  exactly one frequent co-author matches who did not write the
                  cited work (kept, but listed, because one common name is weak evidence);
      None        no match.
    """
    pi = name_key(PI_NAME)
    matched: list[str] = []
    own_work = False
    is_self = False
    for a in authors or []:
        key = name_key(a)
        if key == pi:
            is_self = True
        elif cited_authors and key in cited_authors:
            own_work = True
            name = coauthors.get(key, a)
            if name not in matched:
                matched.append(name)
        elif key in coauthors and coauthors[key] not in matched:
            matched.append(coauthors[key])
    if is_self:
        return "self", [PI_NAME] + matched
    if len(matched) >= 2 or own_work:
        return "coauthor", matched
    if matched:
        return "possible", matched
    return None, []


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


def short_label(title: str, venue: str = "", *, max_len: int = 42) -> str:
    """Compact, readable label for a cited paper, used in the output tables.

    A short pre-colon name ("COPOD: Copula-Based ...") becomes the label.
    Otherwise the title is cut at a word boundary. The venue is left out: both
    sources must produce the same label for cross-source dedup, and the label
    only has to identify the work among the PI's own papers.
    """
    title = (title or "").strip()
    m = re.match(r"^([^:]{2,24}):\s", title)
    if m:
        return m.group(1).strip()
    if len(title) <= max_len:
        return title
    cut = title[:max_len].rsplit(" ", 1)[0].rstrip(",;:-")
    return cut + "…"


def normalize_title(title: str) -> str:
    """Lowercase alphanumeric form of a title, for matching versions of one paper."""
    return re.sub(r"[^a-z0-9]+", " ", (title or "").lower()).strip()


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
    """Deduplicate entries by (organization, normalized citing title, cited work).

    Keying on the canonical organization collapses legal entities of one
    company; keying on the normalized title collapses a preprint and its journal
    version, and the two sources' records of one paper. Merged rows keep the
    latest year and the union of sources, raw institution names, countries, and
    authors.
    """
    by_key: dict[tuple, dict] = {}
    for e in entries:
        key = (
            e.get("org") or e.get("institution", ""),
            normalize_title(e.get("citing_title") or ""),
            e.get("cited_work", ""),
        )
        existing = by_key.get(key)
        if existing is None:
            by_key[key] = dict(e)
            by_key[key]["authors"] = list(e.get("authors") or [])
            continue
        sources = set(existing.get("source", "").split("+"))
        sources.update(e.get("source", "").split("+"))
        sources.discard("")
        existing["source"] = "+".join(sorted(sources, key=_source_sort_key))
        for field, sep in (("institution", "; "), ("country", ", ")):
            vals = [v for v in (existing.get(field) or "").split(sep) if v]
            for v in (e.get(field) or "").split(sep):
                if v and v not in vals:
                    vals.append(v)
            existing[field] = sep.join(vals)
        if (e.get("year") or 0) > (existing.get("year") or 0):
            existing["year"] = e.get("year")
            existing["citing_title"] = e.get("citing_title") or existing.get("citing_title")
        for a in e.get("authors") or []:
            if a not in existing["authors"]:
                existing["authors"].append(a)
    return list(by_key.values())
