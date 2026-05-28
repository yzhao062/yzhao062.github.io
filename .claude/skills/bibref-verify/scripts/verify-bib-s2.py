#!/usr/bin/env python3
"""Cross-verify a .bib file against the Semantic Scholar Graph API.

Reads `S2_API_KEY` from the environment (or `.env` in CWD).
Writes a Markdown report alongside the bib (or to --out).

Usage:
    <python> <skill-dir>/scripts/verify-bib-s2.py papers/<paper>/refs.bib
    <python> <skill-dir>/scripts/verify-bib-s2.py papers/<paper>/refs.bib --out /tmp/report.md

    where <skill-dir> is the directory containing this skill's SKILL.md
    (for example, skills/bibref-verify in a source checkout or
    .claude/skills/bibref-verify after pack deployment). On Windows, prefer
    the Miniforge / conda interpreter (e.g.
    C:/Users/<u>/miniforge3/envs/py312/python.exe); the bare `python`
    may resolve to the Windows Store alias and fail.
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
from difflib import SequenceMatcher
from pathlib import Path

S2_BASE = "https://api.semanticscholar.org/graph/v1"
FIELDS = "title,authors,year,venue,externalIds,publicationVenue,publicationTypes"
ARXIV_RX = re.compile(r"(\d{4}\.\d{4,6})")


def load_dotenv(path):
    if not path.exists():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)$", line)
        if not m:
            continue
        key, value = m.group(1), m.group(2).strip()
        if (value.startswith('"') and value.endswith('"')) or (
            value.startswith("'") and value.endswith("'")
        ):
            value = value[1:-1]
        os.environ.setdefault(key, value)


def parse_bib(text):
    text = re.sub(r"^%.*$", "", text, flags=re.MULTILINE)
    entries, pos = [], 0
    while True:
        m = re.search(r"@(\w+)\s*\{", text[pos:])
        if not m:
            break
        etype = m.group(1).lower()
        if etype in ("comment", "string", "preamble"):
            pos += m.end()
            continue
        body_start = pos + m.end()
        depth, i = 1, body_start
        while i < len(text) and depth > 0:
            c = text[i]
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
            i += 1
        body = text[body_start:i - 1]
        pos = i
        comma = body.find(",")
        if comma < 0:
            continue
        key = body[:comma].strip()
        fields = parse_fields(body[comma + 1:])
        entries.append({"type": etype, "key": key, "fields": fields})
    return entries


def parse_fields(text):
    fields, i, n = {}, 0, len(text)
    while i < n:
        while i < n and text[i] in " \t\n\r,":
            i += 1
        if i >= n:
            break
        m = re.match(r"([A-Za-z][A-Za-z0-9_-]*)\s*=\s*", text[i:])
        if not m:
            break
        name = m.group(1).lower()
        i += m.end()
        if i >= n:
            break
        c = text[i]
        if c == "{":
            depth, j = 1, i + 1
            while j < n and depth > 0:
                if text[j] == "{":
                    depth += 1
                elif text[j] == "}":
                    depth -= 1
                j += 1
            value = text[i + 1:j - 1]
            i = j
        elif c == '"':
            j = i + 1
            while j < n and text[j] != '"':
                j += 1
            value = text[i + 1:j]
            i = j + 1 if j < n else j
        else:
            m2 = re.match(r"(\w+)", text[i:])
            if not m2:
                break
            value = m2.group(1)
            i += m2.end()
        fields[name] = value.strip()
    return fields


def extract_arxiv(fields):
    for fkey in ("eprint", "journal", "url", "howpublished", "note"):
        v = fields.get(fkey, "")
        if not v:
            continue
        m = ARXIV_RX.search(v)
        if m:
            return m.group(1)
    return None


def normalize_title(s):
    s = re.sub(r"\\[a-zA-Z]+\s*", "", s)
    s = re.sub(r"[\{\}]", "", s)
    s = re.sub(r"[^a-z0-9 ]", " ", s.lower())
    s = re.sub(r"\s+", " ", s).strip()
    return s


def split_authors(s):
    s = re.sub(r"\\['`^\"~=\.cuvHrtdb]\s*", "", s)
    s = re.sub(r"[\{\}]", "", s)
    parts = [p.strip() for p in re.split(r"\s+and\s+", s)]
    out = []
    for p in parts:
        if not p or p.lower() == "others":
            continue
        if "," in p:
            last, first = p.split(",", 1)
            out.append((last.strip(), first.strip()))
        else:
            tokens = p.split()
            if tokens:
                out.append((tokens[-1], " ".join(tokens[:-1])))
    return out


def s2_get(url, headers):
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers=headers, method="GET")
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.status, json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < 3:
                time.sleep(2 + attempt * 2)
                continue
            return e.code, None
        except Exception:
            if attempt < 3:
                time.sleep(2 + attempt * 2)
                continue
            return None, None
    return None, None


def s2_batch(ids, headers):
    url = f"{S2_BASE}/paper/batch?fields={FIELDS}"
    body = json.dumps({"ids": ids}).encode("utf-8")
    req_headers = {**headers, "Content-Type": "application/json"}
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, data=body, headers=req_headers, method="POST")
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.status, json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < 2:
                time.sleep(3 + attempt * 3)
                continue
            try:
                err_body = e.read().decode("utf-8", errors="replace")
            except Exception:
                err_body = ""
            return e.code, err_body
        except Exception:
            if attempt < 2:
                time.sleep(3 + attempt * 3)
                continue
            return None, None
    return None, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("bib", help="path to .bib file")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    bib_path = Path(args.bib).resolve()
    if not bib_path.exists():
        print(f"ERROR: bib file not found: {bib_path}", file=sys.stderr)
        return 1
    out_path = Path(args.out).resolve() if args.out else bib_path.parent / "S2-VERIFY-REPORT.md"

    load_dotenv(Path.cwd() / ".env")
    api_key = os.environ.get("S2_API_KEY", "").strip()
    if not api_key or "PASTE" in api_key.upper():
        print("ERROR: S2_API_KEY not set or placeholder. Edit .env or export it.", file=sys.stderr)
        return 2
    headers = {"x-api-key": api_key}

    text = bib_path.read_text(encoding="utf-8")
    entries = parse_bib(text)
    print(f"Parsed {len(entries)} entries", file=sys.stderr)

    ax_entries, title_entries = [], []
    for e in entries:
        ax = extract_arxiv(e["fields"])
        e["arxiv"] = ax
        e["s2"] = None
        if ax:
            ax_entries.append(e)
        else:
            title_entries.append(e)
    print(f"  arXiv batch: {len(ax_entries)}; title search: {len(title_entries)}", file=sys.stderr)

    # Batch lookup arXiv-ID entries
    for chunk_start in range(0, len(ax_entries), 200):
        chunk = ax_entries[chunk_start:chunk_start + 200]
        ids = [f"arXiv:{e['arxiv']}" for e in chunk]
        status, data = s2_batch(ids, headers)
        if status != 200 or not isinstance(data, list):
            # Mark chunk as failed so categorize/report distinguishes from a true S2 miss
            for e in chunk:
                e["batch_failed"] = True
                e["batch_status"] = status
            print(f"  batch chunk {chunk_start}: status={status} body={str(data)[:200]}", file=sys.stderr)
            continue
        for j, item in enumerate(data):
            chunk[j]["s2"] = item
        time.sleep(1)
    print(f"  batch done", file=sys.stderr)

    # Title-search fallback covers (a) entries without arXiv IDs and
    # (b) arXiv entries whose batch lookup returned None or whose chunk failed.
    # This avoids labeling legitimate arXiv papers as NOT-FOUND when S2 simply
    # has no arXiv-keyed record but does have a title-keyed one.
    fallback_entries = list(title_entries)
    fallback_arxiv_retry_count = 0
    for e in ax_entries:
        if e.get("s2") is None and e["fields"].get("title"):
            fallback_entries.append(e)
            fallback_arxiv_retry_count += 1
    if fallback_arxiv_retry_count:
        print(f"  title fallback: {len(fallback_entries)} entries (incl {fallback_arxiv_retry_count} arXiv retries)", file=sys.stderr)

    # Title search fallback
    for idx, e in enumerate(fallback_entries):
        title = e["fields"].get("title", "")
        if not title:
            continue
        norm = normalize_title(title)
        q = urllib.parse.quote(norm[:160])
        url = f"{S2_BASE}/paper/search?query={q}&limit=3&fields={FIELDS}"
        status, data = s2_get(url, headers)
        time.sleep(1.2)
        if status != 200 or not isinstance(data, dict):
            e["s2_match_method"] = f"search HTTP {status}"
            continue
        best, best_sim = None, 0.0
        for cand in data.get("data") or []:
            cand_norm = normalize_title(cand.get("title", "") or "")
            sim = SequenceMatcher(None, norm, cand_norm).ratio()
            if sim > best_sim:
                best_sim, best = sim, cand
        if best and best_sim >= 0.85:
            e["s2"] = best
            e["s2_match_method"] = f"title sim={best_sim:.2f}"
        else:
            e["s2_match_method"] = f"title best sim={best_sim:.2f} (<0.85)"

    # Categorize. Distinguish API-ERROR (S2 lookup never completed cleanly:
    # batch chunk failed AND no title fallback succeeded; or title fallback
    # hit a non-200 HTTP status) from NOT-FOUND (S2 returned cleanly with
    # no match — the real hallucination signal). Mixing them under
    # "NOT-FOUND" would falsely flag legitimate papers whenever the API
    # rate-limits or transiently fails.
    not_found, drifts, matches, api_errors = [], [], [], []
    for e in entries:
        s2 = e.get("s2")
        if s2 is None:
            method = e.get("s2_match_method", "") or ""
            if method.startswith("search HTTP "):
                api_errors.append(e)
            elif e.get("batch_failed") and not method:
                api_errors.append(e)
            else:
                not_found.append(e)
            continue

        ent_issues = []

        bib_title = normalize_title(e["fields"].get("title", ""))
        s2_title = normalize_title(s2.get("title", "") or "")
        sim = SequenceMatcher(None, bib_title, s2_title).ratio()
        if sim < 0.75:
            ent_issues.append(("TITLE-MISMATCH", f"sim={sim:.2f}: bib='{bib_title[:50]}' vs s2='{s2_title[:50]}'"))

        bib_authors = split_authors(e["fields"].get("author", ""))
        bib_surnames = [a[0].lower() for a in bib_authors[:3]]
        s2_authors = s2.get("authors") or []
        s2_names = [(p.get("name") or "").lower() for p in s2_authors]
        if bib_surnames:
            matched = sum(1 for s in bib_surnames if any(s in n for n in s2_names))
            need = min(2, len(bib_surnames))
            if matched < need:
                ent_issues.append((
                    "AUTHOR-MISMATCH",
                    f"bib lead surnames {bib_surnames}; s2 first 5 = {[n[:25] for n in s2_names[:5]]} (n={len(s2_names)})"
                ))

        bib_year_raw = e["fields"].get("year", "").strip()
        bib_year = re.sub(r"[^\d]", "", bib_year_raw)
        s2_year = s2.get("year")
        if bib_year.isdigit() and s2_year and abs(int(bib_year) - int(s2_year)) > 1:
            ent_issues.append(("YEAR-MISMATCH", f"bib={bib_year} vs s2={s2_year}"))

        bib_journal = (e["fields"].get("journal", "") or "").lower()
        s2_venue = (s2.get("venue") or "").strip()
        if "arxiv" in bib_journal and s2_venue and "arxiv" not in s2_venue.lower():
            ent_issues.append(("VENUE-UPGRADE", f"bib '{bib_journal[:40]}' → s2 '{s2_venue}'"))

        if ent_issues:
            drifts.append((e, ent_issues))
        else:
            matches.append(e)

    # Write report
    out = []
    out.append("# S2 Cross-Verification — `" + bib_path.name + "`")
    out.append("")
    out.append(f"- Source: `{bib_path}`")
    out.append("- Method: Semantic Scholar Graph API (`paper/batch` for arXiv IDs; `paper/search` fallback at sim≥0.85)")
    out.append(f"- Entries parsed: **{len(entries)}**")
    out.append(f"- arXiv batch: {len(ax_entries)} | title search: {len(title_entries)}")
    out.append(f"- **NOT-FOUND** (hallucination suspected): **{len(not_found)}**")
    out.append(f"- **API-ERROR** (S2 lookup did not complete; not a hallucination signal): **{len(api_errors)}**")
    out.append(f"- **DRIFT** (S2 disagrees on at least one field): **{len(drifts)}**")
    out.append(f"- **MATCH**: **{len(matches)}**")
    out.append("")
    out.append("## NOT-FOUND — hallucination suspected")
    out.append("")
    if not_found:
        out.append("| Key | arXiv | Title (truncated) | Method / reason |")
        out.append("|---|---|---|---|")
        for e in not_found:
            t = (e["fields"].get("title", "") or "").replace("|", "/")[:70]
            ax = e.get("arxiv") or "-"
            method = e.get("s2_match_method", "arXiv batch returned null")
            out.append(f"| `{e['key']}` | `{ax}` | {t} | {method} |")
    else:
        out.append("(none)")
    out.append("")
    out.append("## API-ERROR — S2 lookup did not complete (manual check needed)")
    out.append("")
    if api_errors:
        out.append("| Key | arXiv | Title (truncated) | Failure reason |")
        out.append("|---|---|---|---|")
        for e in api_errors:
            t = (e["fields"].get("title", "") or "").replace("|", "/")[:70]
            ax = e.get("arxiv") or "-"
            bs = e.get("batch_status")
            method = e.get("s2_match_method") or (f"batch HTTP {bs}" if bs else "batch lookup failed")
            out.append(f"| `{e['key']}` | `{ax}` | {t} | {method} |")
    else:
        out.append("(none)")
    out.append("")
    out.append("## DRIFT — fields mismatched with S2")
    out.append("")
    if drifts:
        out.append("| Key | arXiv | Issues |")
        out.append("|---|---|---|")
        for e, issues in drifts:
            ax = e.get("arxiv") or "-"
            issue_str = " <br> ".join(
                f"**{kind}**: {detail}".replace("|", "/") for kind, detail in issues
            )
            out.append(f"| `{e['key']}` | `{ax}` | {issue_str} |")
    else:
        out.append("(none)")
    out.append("")
    out.append("## MATCH (S2 confirms title, lead authors, year, venue)")
    out.append("")
    out.append(f"{len(matches)} entries matched cleanly.")
    out.append("")
    out.append("<details>")
    out.append("<summary>Click to expand key list</summary>")
    out.append("")
    for e in matches:
        out.append(f"- `{e['key']}`")
    out.append("")
    out.append("</details>")

    out_path.write_text("\n".join(out), encoding="utf-8")
    print(f"Report: {out_path}", file=sys.stderr)
    print(f"NOT-FOUND={len(not_found)} API-ERROR={len(api_errors)} DRIFT={len(drifts)} MATCH={len(matches)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
