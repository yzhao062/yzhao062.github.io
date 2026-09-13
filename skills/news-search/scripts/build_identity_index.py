#!/usr/bin/env python3
"""Build a document-identity index from the audit record, and check candidates against it.

Why this exists. Every round before 2026-09-12 built its suppression set by collecting URL strings out
of `news-coverage-audit.md`. That is not a document identity, and the 2026-09-12 round paid for the
difference five times in one day:

  1. Google Patents serves one patent at `/en`, `/zh`, `/fr` and `/sk`. The index held all four, so a
     candidate arriving as `/en` missed the `/zh` copy already on file.
  2. Ledger 1b names a government report as "SLAC OSTI 3005876" with no link at all, so the report
     re-entered verification hours after being recorded.
  3. Ledger 3 row 41 names "Real Python Podcast #208" and the candidate arrived as an Apple Podcasts
     URL.
  4. Ledger 6 row A2 holds a paper under its arXiv ID and the candidate arrived as the workshop-hosted
     PDF of the same paper.
  5. Ledger 3 rows 37 and 39 name books by title, and the candidates arrived as O'Reilly reader URLs
     keyed by ISBN.

Each was fixed with one more special case. This script replaces the special cases: it extracts every
identifier a recorded document carries, not only its URL, and matches a candidate on any of them.

Usage:
    build_identity_index.py build [--audit PATH ...] [--out PATH]
    build_identity_index.py check --index PATH [--url URL ... | --stdin]

`build` writes one JSON object per line: the identifier, its kind, and where in the record it was
found. `check` reads candidate URLs and prints, for each, whether any identifier matches and which.
Exit status 0 always; the output is the answer.
"""
import argparse
import json
import os
import re
import sys
from collections import Counter

REPO_DEFAULT = [
    "news-coverage-audit.md",
    "citation-affiliation-audit.md",
]

# --- extractors ---------------------------------------------------------------------------------
# Each returns a set of canonical identifier strings for one line of the record.

URL_RE = re.compile(r"https?://[^\s)\]|>\"']+")
ARXIV_RE = re.compile(r"(?:arxiv[:\s/]*|abs/|pdf/)(\d{4}\.\d{4,5})", re.I)
DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Za-z0-9]+", re.I)
# CN/US/EP/WO/DE/SK/JP/KR publication numbers as Google Patents spells them
PATENT_RE = re.compile(r"\b([A-Z]{2}\d{6,12}[A-Z]?\d?)\b")
OSTI_RE = re.compile(r"OSTI[\s:#]*(\d{6,8})", re.I)
ISBN_RE = re.compile(r"\b(97[89]\d{10})\b")
YT_RE = re.compile(r"(?:youtube\.com/watch\?v=|youtu\.be/)([A-Za-z0-9_-]{11})")
# "Talk Python To Me #497", "Real Python Podcast #208", "Episode #208"
EPISODE_RE = re.compile(r"([A-Z][A-Za-z' ]{3,40}?)\s*#(\d{1,4})\b")


def norm_url(u):
    u = (u or "").strip().lower()
    u = re.sub(r"^[a-z][a-z0-9+.-]*://", "", u)
    u = re.sub(r"^www\.", "", u)
    u = u.split("#", 1)[0].rstrip("/")
    return u


def patent_key(u):
    """Language-stripped Google Patents key, so /en and /zh collapse to one document."""
    m = re.search(r"patents\.google\.com/patent/([a-z0-9]+)", u)
    return f"patent:{m.group(1).upper()}" if m else None


def identifiers(line):
    """Every identifier a single line of the record carries, as (kind, canonical) pairs."""
    out = set()
    for u in URL_RE.findall(line):
        n = norm_url(u)
        if n:
            out.add(("url", n))
        pk = patent_key(n)
        if pk:
            out.add(("patent", pk))
        for v in YT_RE.findall(u):
            out.add(("youtube", f"youtube:{v}"))
    for a in ARXIV_RE.findall(line):
        out.add(("arxiv", f"arxiv:{a}"))
    for d in DOI_RE.findall(line):
        d = d.rstrip(".,;)\"'").lower()
        out.add(("doi", f"doi:{d}"))
        # arXiv DOIs and arXiv IDs name the same document
        m = re.match(r"doi:10\.48550/arxiv\.(\d{4}\.\d{4,5})", d and f"doi:{d}")
        if m:
            out.add(("arxiv", f"arxiv:{m.group(1)}"))
    for p in PATENT_RE.findall(line):
        # Require a patent-ish context word so ordinary alphanumerics do not become patent keys.
        if re.search(r"patent|CNIPA|USPTO|EPO|WIPO|DPMA", line, re.I):
            out.add(("patent", f"patent:{p.upper()}"))
    for o in OSTI_RE.findall(line):
        out.add(("osti", f"osti:{o}"))
    for i in ISBN_RE.findall(line):
        out.add(("isbn", f"isbn:{i}"))
    for name, num in EPISODE_RE.findall(line):
        name = re.sub(r"\s+", " ", name).strip().lower()
        if len(name) > 3 and "podcast" in line.lower() or "episode" in line.lower():
            out.add(("episode", f"episode:{name}#{num}"))
    return out


def build(paths, out_path):
    seen = {}
    per_file = Counter()
    for path in paths:
        if not os.path.exists(path):
            print(f"  skip (missing): {path}", file=sys.stderr)
            continue
        with open(path, encoding="utf-8", errors="replace") as fh:
            for lineno, line in enumerate(fh, 1):
                for kind, ident in identifiers(line):
                    if ident not in seen:
                        seen[ident] = {"id": ident, "kind": kind,
                                       "source": f"{os.path.basename(path)}:{lineno}"}
                        per_file[os.path.basename(path)] += 1
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        for ident in sorted(seen):
            fh.write(json.dumps(seen[ident], ensure_ascii=False) + "\n")
    kinds = Counter(v["kind"] for v in seen.values())
    print(f"{len(seen)} identifiers -> {out_path}")
    print(f"  by kind : {dict(kinds.most_common())}")
    print(f"  by file : {dict(per_file.most_common())}")
    return seen


def candidate_identifiers(url):
    """The identifiers a bare candidate URL implies. Deliberately narrower than identifiers():
    a candidate has no prose, so only what the URL itself encodes counts."""
    out = set()
    n = norm_url(url)
    if n:
        out.add(f"url:{n}" if False else n)
    pk = patent_key(n)
    if pk:
        out.add(pk)
    for v in YT_RE.findall(url):
        out.add(f"youtube:{v}")
    for a in ARXIV_RE.findall(url):
        out.add(f"arxiv:{a}")
    for d in DOI_RE.findall(url):
        out.add(f"doi:{d.rstrip('.,;)').lower()}")
    for i in ISBN_RE.findall(url):
        out.add(f"isbn:{i}")
    for o in OSTI_RE.findall(url):
        out.add(f"osti:{o}")
    return out


def check(index_path, urls):
    idx = {}
    with open(index_path, encoding="utf-8") as fh:
        for line in fh:
            r = json.loads(line)
            idx[r["id"]] = r
    hit = 0
    for u in urls:
        matches = [(i, idx[i]) for i in candidate_identifiers(u) if i in idx]
        if matches:
            hit += 1
            for i, r in matches:
                print(f"MATCH  {r['kind']:<8} {i}  <- {r['source']}\n       {u}")
        else:
            print(f"new    {u}")
    print(f"\n{hit} of {len(urls)} candidates already recorded", file=sys.stderr)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build")
    b.add_argument("--audit", action="append", default=None,
                   help="record file to read; repeatable. Defaults to the two audit markdown files.")
    b.add_argument("--out", default="identity-index.jsonl")
    c = sub.add_parser("check")
    c.add_argument("--index", required=True)
    c.add_argument("--url", action="append", default=[])
    c.add_argument("--stdin", action="store_true", help="read candidate URLs from stdin, one per line")
    a = ap.parse_args()

    if a.cmd == "build":
        build(a.audit or REPO_DEFAULT, a.out)
    else:
        urls = list(a.url)
        if a.stdin:
            urls += [l.strip() for l in sys.stdin if l.strip()]
        if not urls:
            ap.error("give --url or --stdin")
        check(a.index, urls)


if __name__ == "__main__":
    main()
