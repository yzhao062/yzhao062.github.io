#!/usr/bin/env python3
"""Fetch paper metadata (abstracts, etc.) from arXiv and Semantic Scholar APIs.

Usage:
    python scripts/fetch_paper_metadata.py
"""

import json
import re
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
JSON_PATH = REPO_ROOT / "data" / "publications.json"


def fetch_arxiv_metadata(arxiv_id: str) -> dict | None:
    """Fetch metadata from arXiv API given an arXiv ID like '2603.19423'."""
    url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            xml_data = resp.read().decode("utf-8")
        root = ET.fromstring(xml_data)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        entry = root.find("atom:entry", ns)
        if entry is None:
            return None
        title_el = entry.find("atom:title", ns)
        abstract_el = entry.find("atom:summary", ns)
        title = title_el.text.strip().replace("\n", " ") if title_el is not None else ""
        abstract = abstract_el.text.strip().replace("\n", " ") if abstract_el is not None else ""
        # Clean up multiple spaces
        title = re.sub(r"\s+", " ", title)
        abstract = re.sub(r"\s+", " ", abstract)
        return {"title": title, "abstract": abstract}
    except Exception as e:
        print(f"  [arXiv error] {arxiv_id}: {e}")
        return None


def _normalize_title(title: str) -> str:
    """Normalize title for fuzzy comparison."""
    return re.sub(r"[^a-z0-9]", "", title.lower())


def fetch_semantic_scholar(title: str) -> dict | None:
    """Fetch metadata from Semantic Scholar API given a paper title."""
    encoded = urllib.parse.quote(title)
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={encoded}&limit=3&fields=title,abstract"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "yzhao062-website-sync/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        if not data.get("data"):
            return None
        query_norm = _normalize_title(title)
        for paper in data["data"]:
            result_norm = _normalize_title(paper.get("title", ""))
            # Require significant overlap to avoid wrong-paper matches
            if query_norm[:30] in result_norm or result_norm[:30] in query_norm:
                return {
                    "title": paper.get("title", ""),
                    "abstract": paper.get("abstract") or "",
                }
        print(f"  [S2 no match] {title[:50]}... (top result: {data['data'][0].get('title', '')[:50]})")
        return None
    except Exception as e:
        print(f"  [S2 error] {title[:50]}...: {e}")
        return None


def extract_arxiv_id(paper: dict) -> str | None:
    """Extract arXiv ID from paper_url or other fields."""
    url = paper.get("paper_url", "")
    m = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", url)
    if m:
        return m.group(1)
    return None


def main():
    with open(JSON_PATH, encoding="utf-8") as f:
        papers = json.load(f)

    total = len(papers)
    fetched = 0
    skipped = 0
    failed = []

    for i, paper in enumerate(papers):
        # Skip if abstract already exists and is non-empty
        if paper.get("abstract"):
            skipped += 1
            continue

        title = paper.get("title", "")
        arxiv_id = extract_arxiv_id(paper)

        print(f"[{i+1}/{total}] {title[:60]}...")

        metadata = None

        # Try arXiv first if we have an ID
        if arxiv_id:
            metadata = fetch_arxiv_metadata(arxiv_id)
            time.sleep(0.5)  # Rate limit

        # Fall back to Semantic Scholar
        if not metadata or not metadata.get("abstract"):
            metadata = fetch_semantic_scholar(title)
            time.sleep(1.0)  # S2 rate limit is stricter

        if metadata and metadata.get("abstract"):
            paper["abstract"] = metadata["abstract"]
            fetched += 1
        else:
            failed.append(title)
            paper.setdefault("abstract", "")

    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(papers, f, indent=4, ensure_ascii=False)
        f.write("\n")

    print(f"\nDone: {fetched} abstracts fetched, {skipped} already had abstracts, {len(failed)} failed.")
    if failed:
        print("Failed to fetch:")
        for t in failed:
            print(f"  - {t}")


if __name__ == "__main__":
    main()
