"""Scan a PDF for FORTIS Lab terms using PyMuPDF and report hits with page + context.

Usage: python pdf_term_scan.py <pdf_path>

Term list combines a curated SEED_TERMS set (tool names, author signals, distinctive
phrases) with every paper title in data/publications.json and every project name in
data/open-source.json plus their arXiv IDs. The skill's full-audit-mode contract
(SKILL.md + references/search-strategy.md) requires scanning every paper and tool;
hard-coding terms causes silent false negatives on titles not in the seed list.
"""
import fitz
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]

SEED_TERMS = {
    "PyOD", "TrustLLM", "TrustGen", "agent-audit", "Aegis", "ADBench", "ADMoE",
    "SUOD", "TODS", "COPOD", "ECOD", "LSCP", "PyGOD", "BOND", "JailDAM",
    "DoxBench", "MetaOOD", "AD-LLM", "AD-AGENT", "NLP-ADBench", "FaceLock",
    "anywhere-agents", "agent-style", "TrustEval", "TyphoFormer", "ClimateLLM",
    "FigEdit", "Auditable Agents", "Sovereign-OS", "MAMA", "CDCR-SFT",
    "StealthRank", "Multimodal GEO", "Charts Are Not Images",
    "Yue Zhao", "Zhao Y.", "yzhao062", "Zhao et al",
}


def _arxiv_id(url):
    marker = "arxiv.org/abs/"
    if not url or marker not in url:
        return None
    return url.split(marker, 1)[1].split("?", 1)[0].split("#", 1)[0].strip().rstrip("/")


def load_terms(repo_root=REPO_ROOT):
    terms = set(SEED_TERMS)
    for rel_path, field in (
        ("data/publications.json", "title"),
        ("data/open-source.json", "name"),
    ):
        path = repo_root / rel_path
        if not path.exists():
            continue
        for row in json.loads(path.read_text(encoding="utf-8")):
            value = str(row.get(field, "")).strip()
            if value:
                terms.add(value)
            arxiv = _arxiv_id(str(row.get("paper_url", "")))
            if arxiv:
                terms.add(arxiv)
    # Sort by length desc so multi-word titles match before substrings; tie-break by name.
    return sorted(terms, key=lambda t: (-len(t), t.lower()))


TERMS = load_terms()


FALSE_POSITIVE_CTX = {
    "ECOD": ["decod", "encod", "decoding", "encoding", "code", "Code"],
    "BOND": ["bonds", "bonded", "bonding"],
    "MAMA": ["mammal", "Obama", "Mahama"],
    "SUOD": ["pseudo"],
}


def scan(pdf_path):
    doc = fitz.open(pdf_path)
    hits = []
    for pno in range(len(doc)):
        page = doc[pno]
        text = page.get_text("text")
        for term in TERMS:
            # Word-boundary regex for short tool names to avoid false positives
            if len(term) <= 4 and term.isupper():
                pattern = r"\b" + re.escape(term) + r"\b"
                flags = 0
            else:
                pattern = re.escape(term)
                flags = re.IGNORECASE
            for m in re.finditer(pattern, text, flags=flags):
                start = max(0, m.start() - 120)
                end = min(len(text), m.end() + 120)
                ctx = text[start:end].replace("\n", " ").replace("  ", " ").strip()
                # Filter known false positives based on adjacent characters
                fp_markers = FALSE_POSITIVE_CTX.get(term, [])
                # Look at characters immediately around the match
                pre = text[max(0, m.start() - 4):m.start()]
                post = text[m.end():m.end() + 4]
                if any(fp.lower() in (pre + post).lower() for fp in fp_markers):
                    continue
                hits.append((pno + 1, term, ctx))
    doc.close()
    return hits


if __name__ == "__main__":
    path = sys.argv[1]
    hits = scan(path)
    if not hits:
        print(f"NO_MATCHES :: {path}")
    else:
        print(f"HITS :: {path} :: {len(hits)} matches")
        for page, term, ctx in hits:
            print(f"  p{page} [{term}] {ctx}")
