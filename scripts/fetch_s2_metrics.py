#!/usr/bin/env python3
"""Fetch Semantic Scholar citation metrics for publications.json.

Usage:
    python scripts/fetch_s2_metrics.py
    python scripts/fetch_s2_metrics.py --limit 10

The script reads S2_API_KEY from the environment or from the repo-local .env
file. It writes data/s2-metrics.json and never prints the API key.

Output notes:
    - matched counts input publication records with S2 matches.
    - unique_matched counts distinct S2 paperId values used for citation totals.
    - duplicate_s2_paper_matches lists publication records sharing one S2 paperId.
    - identifier_low_similarity_matches lists identifier-backed matches whose
      S2 title differs enough from the local title to merit human review.
    - duplicate publication records carry duplicate_of in papers[].
"""

from __future__ import annotations

import argparse
import datetime as dt
import difflib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PUBLICATIONS_PATH = ROOT / "data" / "publications.json"
OUTPUT_PATH = ROOT / "data" / "s2-metrics.json"
API_BASE = "https://api.semanticscholar.org/graph/v1"
FIELDS = ",".join(
    [
        "paperId",
        "corpusId",
        "title",
        "year",
        "venue",
        "publicationVenue",
        "publicationDate",
        "url",
        "externalIds",
        "citationCount",
        "influentialCitationCount",
        "referenceCount",
        "authors",
    ]
)


def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("'\"")
        if key and key not in os.environ:
            os.environ[key] = value


def require_api_key() -> str:
    load_env_file(ROOT / ".env")
    api_key = os.environ.get("S2_API_KEY", "").strip()
    if not api_key:
        raise SystemExit("S2_API_KEY is missing. Add it to .env or the environment.")
    return api_key


def read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8-sig") as f:
        return json.load(f)


def write_json(path: Path, payload: Any) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
        f.write("\n")


def normalize_title(title: str) -> str:
    title = title.lower().replace("&amp;", "and")
    title = re.sub(r"\{|\}", "", title)
    return re.sub(r"[^a-z0-9]+", " ", title).strip()


def title_similarity(left: str, right: str) -> float:
    left_norm = normalize_title(left)
    right_norm = normalize_title(right)
    if not left_norm or not right_norm:
        return 0.0
    if left_norm == right_norm:
        return 1.0

    seq_score = difflib.SequenceMatcher(None, left_norm, right_norm).ratio()
    left_tokens = set(left_norm.split())
    right_tokens = set(right_norm.split())
    token_score = len(left_tokens & right_tokens) / max(len(left_tokens | right_tokens), 1)
    return max(seq_score, token_score)


def extract_identifier(publication: dict[str, Any]) -> str | None:
    url = str(publication.get("paper_url", "")).strip()
    if not url:
        return None

    arxiv_match = re.search(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?", url)
    if arxiv_match:
        return f"ARXIV:{arxiv_match.group(1)}"

    doi_match = re.search(r"(?:doi\.org/|doi:)(10\.\d{4,9}/[^\s?#]+)", url, re.IGNORECASE)
    if doi_match:
        return f"DOI:{doi_match.group(1)}"

    return None


def api_request(
    api_key: str,
    path: str,
    *,
    params: dict[str, str | int] | None = None,
    method: str = "GET",
    body: dict[str, Any] | None = None,
    retries: int = 8,
) -> Any:
    url = f"{API_BASE}{path}"
    if params:
        url = f"{url}?{urllib.parse.urlencode(params)}"

    data = None
    headers = {
        "User-Agent": "yzhao062.github.io-s2-metrics/1.0",
        "x-api-key": api_key,
    }
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"

    for attempt in range(retries + 1):
        request = urllib.request.Request(url, data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                raw = response.read().decode("utf-8")
                return json.loads(raw) if raw else None
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return None
            if exc.code in {429, 500, 502, 503, 504} and attempt < retries:
                retry_after = exc.headers.get("Retry-After")
                if retry_after and retry_after.isdigit():
                    delay = float(retry_after)
                elif exc.code == 429:
                    delay = min(90.0, 10.0 * (attempt + 1))
                else:
                    delay = min(30.0, float(2**attempt))
                print(f"  [wait] S2 HTTP {exc.code}; retrying in {delay:g}s", flush=True)
                time.sleep(delay)
                continue
            detail = exc.read().decode("utf-8", errors="replace")[:300]
            raise RuntimeError(f"S2 API HTTP {exc.code} for {path}: {detail}") from exc
        except urllib.error.URLError as exc:
            if attempt < retries:
                delay = min(30.0, float(2**attempt))
                print(f"  [wait] S2 network error; retrying in {delay:g}s", flush=True)
                time.sleep(delay)
                continue
            raise RuntimeError(f"S2 API network error for {path}: {exc}") from exc


def fetch_by_identifier(api_key: str, identifier: str) -> dict[str, Any] | None:
    return api_request(
        api_key,
        f"/paper/{urllib.parse.quote(identifier, safe=':')}",
        params={"fields": FIELDS},
    )


def fetch_identifier_batch(api_key: str, identifiers: list[str]) -> dict[str, dict[str, Any] | None]:
    if not identifiers:
        return {}
    response = api_request(
        api_key,
        "/paper/batch",
        params={"fields": FIELDS},
        method="POST",
        body={"ids": identifiers},
    )
    if not isinstance(response, list):
        return {identifier: None for identifier in identifiers}
    if len(response) != len(identifiers):
        print(
            f"  [warn] S2 batch returned {len(response)} results for {len(identifiers)} identifiers",
            flush=True,
        )
    results: dict[str, dict[str, Any] | None] = {}
    for idx, identifier in enumerate(identifiers):
        paper = response[idx] if idx < len(response) else None
        results[identifier] = paper if isinstance(paper, dict) else None
    return results


def fetch_by_title_match(api_key: str, title: str) -> dict[str, Any] | None:
    return api_request(
        api_key,
        "/paper/search/match",
        params={"query": title, "fields": FIELDS},
    )


def fetch_by_title_search(api_key: str, title: str, year: int | None = None) -> dict[str, Any] | None:
    response = api_request(
        api_key,
        "/paper/search",
        params={"query": title, "limit": 10, "fields": FIELDS},
    )
    if not isinstance(response, dict) or not isinstance(response.get("data"), list):
        return None

    best: tuple[float, dict[str, Any]] | None = None
    for candidate in response["data"]:
        if not isinstance(candidate, dict):
            continue
        score = title_similarity(title, str(candidate.get("title", "")))
        candidate_year = candidate.get("year")
        if isinstance(year, int) and isinstance(candidate_year, int):
            if abs(candidate_year - year) <= 1:
                score += 0.03
            elif abs(candidate_year - year) > 3:
                score -= 0.05
        if best is None or score > best[0]:
            best = (score, candidate)

    return best[1] if best else None


def fetch_by_title(api_key: str, publication: dict[str, Any]) -> tuple[dict[str, Any] | None, str]:
    title = str(publication.get("title", "")).strip()
    year = publication.get("year")
    year_int = year if isinstance(year, int) else None

    match = fetch_by_title_match(api_key, title)
    if match and title_similarity(title, str(match.get("title", ""))) >= 0.92:
        return match, "title-match"

    search = fetch_by_title_search(api_key, title, year=year_int)
    if search:
        if not match:
            return search, "title-search"
        search_score = title_similarity(title, str(search.get("title", "")))
        match_score = title_similarity(title, str(match.get("title", "")))
        if search_score > match_score:
            return search, "title-search"
        return match, "title-match"

    if match:
        return match, "title-match"
    return None, "title-match"


def summarize_author_names(paper: dict[str, Any], limit: int = 8) -> list[str]:
    authors = paper.get("authors")
    if not isinstance(authors, list):
        return []
    names: list[str] = []
    for author in authors[:limit]:
        if isinstance(author, dict) and author.get("name"):
            names.append(str(author["name"]))
    return names


def build_record(publication: dict[str, Any], s2_paper: dict[str, Any], matched_by: str) -> dict[str, Any]:
    return {
        "id": publication.get("id", ""),
        "title": publication.get("title", ""),
        "venue": publication.get("venue", ""),
        "year": publication.get("year", ""),
        "matched_by": matched_by,
        "title_match_score": round(
            title_similarity(str(publication.get("title", "")), str(s2_paper.get("title", ""))),
            4,
        ),
        "s2": {
            "paperId": s2_paper.get("paperId"),
            "corpusId": s2_paper.get("corpusId"),
            "title": s2_paper.get("title"),
            "url": s2_paper.get("url"),
            "venue": s2_paper.get("venue"),
            "year": s2_paper.get("year"),
            "publicationDate": s2_paper.get("publicationDate"),
            "citationCount": s2_paper.get("citationCount") or 0,
            "influentialCitationCount": s2_paper.get("influentialCitationCount") or 0,
            "referenceCount": s2_paper.get("referenceCount") or 0,
            "externalIds": s2_paper.get("externalIds") or {},
            "authors": summarize_author_names(s2_paper),
        },
    }


def annotate_duplicate_papers(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Mark duplicate S2 paper IDs in place and return a compact summary."""
    seen: dict[str, dict[str, Any]] = {}
    duplicates: list[dict[str, Any]] = []

    for record in records:
        paper_id = str(record.get("s2", {}).get("paperId") or "")
        if not paper_id:
            continue
        if paper_id not in seen:
            seen[paper_id] = record
            continue

        first = seen[paper_id]
        record["duplicate_of"] = first.get("id", "")
        duplicates.append(
            {
                "paperId": paper_id,
                "canonical_id": first.get("id", ""),
                "duplicate_id": record.get("id", ""),
                "canonical_title": first.get("title", ""),
                "duplicate_title": record.get("title", ""),
                "citationCount": record.get("s2", {}).get("citationCount") or 0,
                "influentialCitationCount": record.get("s2", {}).get("influentialCitationCount") or 0,
            }
        )

    return duplicates


def collect_identifier_low_similarity(records: list[dict[str, Any]], threshold: float = 0.75) -> list[dict[str, Any]]:
    flagged: list[dict[str, Any]] = []
    for record in records:
        if not str(record.get("matched_by", "")).startswith("identifier:"):
            continue
        score = float(record.get("title_match_score") or 0.0)
        if score >= threshold:
            continue
        flagged.append(
            {
                "id": record.get("id", ""),
                "title": record.get("title", ""),
                "s2_title": record.get("s2", {}).get("title"),
                "paperId": record.get("s2", {}).get("paperId"),
                "score": score,
            }
        )
    return flagged


def unique_records_by_paper_id(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[str] = set()
    unique: list[dict[str, Any]] = []
    for record in records:
        paper_id = str(record.get("s2", {}).get("paperId") or "")
        if paper_id:
            if paper_id in seen:
                continue
            seen.add(paper_id)
        unique.append(record)
    return unique


def fetch_metrics(limit: int | None = None, sleep_seconds: float = 1.0) -> dict[str, Any]:
    api_key = require_api_key()
    publications = read_json(PUBLICATIONS_PATH)
    if not isinstance(publications, list):
        raise SystemExit(f"Expected a list in {PUBLICATIONS_PATH}")

    selected = publications[:limit] if limit else publications
    records: list[dict[str, Any]] = []
    unmatched: list[dict[str, Any]] = []
    low_confidence: list[dict[str, Any]] = []
    identifiers = [identifier for publication in selected if (identifier := extract_identifier(publication))]
    batch_results = fetch_identifier_batch(api_key, identifiers)
    if identifiers:
        print(f"Loaded {sum(1 for paper in batch_results.values() if paper)}/{len(identifiers)} identifier matches via S2 batch.")
        time.sleep(sleep_seconds)

    for idx, publication in enumerate(selected, 1):
        title = str(publication.get("title", "")).strip()
        if not title:
            continue

        print(f"[{idx}/{len(selected)}] {title[:80]}")
        identifier = extract_identifier(publication)
        s2_paper: dict[str, Any] | None = None
        matched_by = "title"

        if identifier:
            s2_paper = batch_results.get(identifier)
            if s2_paper:
                matched_by = f"identifier:{identifier.split(':', 1)[0]}"
            else:
                s2_paper = fetch_by_identifier(api_key, identifier)
                time.sleep(sleep_seconds)
                if s2_paper:
                    matched_by = f"identifier:{identifier.split(':', 1)[0]}"

        if not s2_paper:
            s2_paper, matched_by = fetch_by_title(api_key, publication)
            time.sleep(sleep_seconds)

        if not s2_paper or not s2_paper.get("paperId"):
            unmatched.append({"id": publication.get("id", ""), "title": title, "reason": "no S2 match"})
            print("  [miss] no S2 match")
            continue

        record = build_record(publication, s2_paper, matched_by)
        if record["title_match_score"] < 0.82 and not str(record["matched_by"]).startswith("identifier:"):
            low_confidence.append(
                {
                    "id": record["id"],
                    "title": title,
                    "s2_title": record["s2"].get("title"),
                    "score": record["title_match_score"],
                }
            )
            print(f"  [low] title score {record['title_match_score']}: {record['s2'].get('title')}")
        else:
            print(
                "  [ok] "
                f"{record['s2']['citationCount']} citations, "
                f"{record['s2']['influentialCitationCount']} influential"
            )
        records.append(record)

    duplicate_s2_papers = annotate_duplicate_papers(records)
    identifier_low_similarity_matches = collect_identifier_low_similarity(records)
    unique_records = unique_records_by_paper_id(records)
    total_citations = sum(int(record["s2"].get("citationCount") or 0) for record in unique_records)
    total_influential = sum(int(record["s2"].get("influentialCitationCount") or 0) for record in unique_records)
    top_by_citations = sorted(
        unique_records,
        key=lambda item: int(item["s2"].get("citationCount") or 0),
        reverse=True,
    )[:15]

    return {
        "generated_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "source": "Semantic Scholar Graph API",
        "input_publications": len(selected),
        "matched": len(records),
        "unique_matched": len(unique_records),
        "unmatched": len(unmatched),
        "low_confidence": len(low_confidence),
        "duplicate_s2_papers": len(duplicate_s2_papers),
        "identifier_low_similarity": len(identifier_low_similarity_matches),
        "totals": {
            "citationCount": total_citations,
            "influentialCitationCount": total_influential,
        },
        "top_by_citations": [
            {
                "id": record["id"],
                "title": record["title"],
                "citationCount": record["s2"].get("citationCount") or 0,
                "influentialCitationCount": record["s2"].get("influentialCitationCount") or 0,
                "s2_url": record["s2"].get("url"),
            }
            for record in top_by_citations
        ],
        "duplicate_s2_paper_matches": duplicate_s2_papers,
        "identifier_low_similarity_matches": identifier_low_similarity_matches,
        "unmatched_publications": unmatched,
        "low_confidence_matches": low_confidence,
        "papers": records,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=None, help="Only process the first N publications.")
    parser.add_argument("--sleep", type=float, default=1.0, help="Delay between API calls.")
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH, help="Output JSON path.")
    args = parser.parse_args()

    payload = fetch_metrics(limit=args.limit, sleep_seconds=args.sleep)
    write_json(args.output, payload)
    print(
        "\nDone: "
        f"{payload['matched']}/{payload['input_publications']} matched, "
        f"{payload['unique_matched']} unique S2 papers, "
        f"{payload['unmatched']} unmatched, "
        f"{payload['low_confidence']} low-confidence, "
        f"{payload['duplicate_s2_papers']} duplicate, "
        f"{payload['identifier_low_similarity']} identifier-low-similarity."
    )
    print(
        "Totals: "
        f"{payload['totals']['citationCount']} citations, "
        f"{payload['totals']['influentialCitationCount']} influential citations."
    )
    try:
        output_label = args.output.relative_to(ROOT)
    except ValueError:
        output_label = args.output
    print(f"Wrote {output_label}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\nInterrupted.")
