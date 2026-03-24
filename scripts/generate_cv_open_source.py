#!/usr/bin/env python3
"""Generate cv/open-source.tex from data/open-source.json.

Single source of truth: data/open-source.json is maintained for the website.
This script generates the LaTeX fragment that cv/cv-full.tex includes via
\\input{open-source.tex}.

Usage:
    python scripts/generate_cv_open_source.py
"""

import json
import math
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
JSON_PATH = REPO_ROOT / "data" / "open-source.json"
TEX_PATH = REPO_ROOT / "cv" / "open-source.tex"


def format_stars(n: int) -> str:
    """Format star count: 9755 -> '9.7K', 1007 -> '1K', 92 -> '92'."""
    if n >= 1000:
        val = n / 1000
        if val == int(val):
            return f"{int(val)}K"
        return f"{val:.1f}K"
    return str(n)


def format_date(iso_str: str) -> str:
    """Format ISO date to 'Mon. YYYY': '2026-03-01T...' -> 'Mar. 2026'."""
    dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
    month = dt.strftime("%b")
    return f"{month}. {dt.year}"


def escape_latex(text: str) -> str:
    """Escape characters that are special in LaTeX."""
    # Use a sentinel for backslash to avoid double-escaping braces
    BACKSLASH_SENTINEL = "\x00BACKSLASH\x00"
    text = text.replace("\\", BACKSLASH_SENTINEL)
    replacements = [
        ("&", r"\&"),
        ("%", r"\%"),
        ("$", r"\$"),
        ("#", r"\#"),
        ("_", r"\_"),
        ("{", r"\{"),
        ("}", r"\}"),
        ("~", r"\textasciitilde{}"),
        ("^", r"\textasciicircum{}"),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    text = text.replace(BACKSLASH_SENTINEL, r"\textbackslash{}")
    return text


def build_links(entry: dict) -> str:
    """Build 'Links: docs | paper | demo' string from entry URLs."""
    parts = []
    if entry.get("docs_url"):
        parts.append(rf'\href{{{entry["docs_url"]}}}{{docs}}')
    if entry.get("paper_url"):
        parts.append(rf'\href{{{entry["paper_url"]}}}{{paper}}')
    if entry.get("demo_url"):
        parts.append(rf'\href{{{entry["demo_url"]}}}{{demo}}')
    if parts:
        return " Links: " + " | ".join(parts) + "."
    return ""


def format_item(entry: dict) -> str:
    """Format a single JSON entry as a LaTeX \\item line."""
    name = entry["name"]
    repo_url = entry["repo_url"]
    category = escape_latex(entry["category"])
    date = format_date(entry["last_updated_at"])
    stars = format_stars(entry["stars"])
    desc = escape_latex(entry["description"])
    links = build_links(entry)

    return (
        rf"\item \textbf{{\href{{{repo_url}}}{{{name}}}}} "
        rf"(\textit{{{category}}}; updated {date}; "
        rf"\textcolor{{uscred}}{{{stars} stars}}) "
        rf"{desc}{links}"
    )


def generate():
    with open(JSON_PATH, encoding="utf-8") as f:
        entries = json.load(f)

    primary = [e for e in entries if e["role"] == "Primary"]
    collabs = [e for e in entries if e["role"] == "Collaborator"]

    # Sort by stars descending within each group
    primary.sort(key=lambda e: e["stars"], reverse=True)
    collabs.sort(key=lambda e: e["stars"], reverse=True)

    lines = []
    lines.append(r"% Auto-generated from data/open-source.json by scripts/generate_cv_open_source.py")
    lines.append(r"% Do not edit manually — edit the JSON and re-run the script.")
    lines.append(r"\section{\sc Selected Open-Source Software, Benchmarks, and Systems}")
    lines.append(r"\vspace{-0.08in}")
    lines.append(r"{\small")
    lines.append(
        r"Representative open-source research artifacts spanning anomaly detection, "
        r"trustworthy AI, agent security, and research tooling."
    )
    lines.append(r"\vspace{-0.08in}")
    lines.append("")

    # Primary contributions
    lines.append(r"\subsubsection*{Primary Contributions}")
    lines.append(r"\begin{itemize}[leftmargin=*,itemsep=0.12em,topsep=0.1em]")
    for entry in primary:
        lines.append(format_item(entry))
    lines.append(r"\end{itemize}")
    lines.append(r"\vspace{-0.1in}")
    lines.append("")

    # Selected collaborations
    lines.append(r"\subsubsection*{Selected Collaborations}")
    lines.append(r"\begin{itemize}[leftmargin=*,itemsep=0.12em,topsep=0.1em]")
    for entry in collabs:
        lines.append(format_item(entry))
    lines.append(r"\end{itemize}")
    lines.append(r"\vspace{-0.1in}")
    lines.append(r"}")
    lines.append("")

    tex_content = "\n".join(lines)
    TEX_PATH.write_text(tex_content, encoding="utf-8")
    print(f"Generated {TEX_PATH} ({len(primary)} primary + {len(collabs)} collaborations)")


if __name__ == "__main__":
    generate()
