"""One-shot script to append the 2026-05-19 round delta + citation-audit hook
to news-coverage-audit.md, and update the top 'Updated' line.

Reads:
- skills/news-search/scratch/phase-b-verified-*.jsonl  (Phase B output)
- citation-affiliation-audit.md (for the hook embed)
- news-coverage-audit.md (existing audit; modify in place)

Side effects:
- Updates news-coverage-audit.md with new content appended at end + header swap.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
NEWS_AUDIT = REPO / "news-coverage-audit.md"
CITE_AUDIT = REPO / "citation-affiliation-audit.md"
VERIFIED_GLOB = "skills/news-search/scratch/phase-b-verified-*.jsonl"

TODAY = "2026-05-19"


def load_verified():
    rows = []
    for p in sorted(REPO.glob(VERIFIED_GLOB)):
        with open(p, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rows.append(json.loads(line))
                except Exception:
                    pass
    return rows


def is_promote(r):
    if r.get("status") == "candidate-promote":
        return True
    if r.get("direct_mention") is True and r.get("tier_guess") not in ("dropped", "duplicate_existing", "verified-negative"):
        return True
    return False


def tier_of(r):
    t = r.get("tier_guess") or r.get("tier") or ""
    return str(t).strip()


# Phase B notes were written with news-search Tier vocabulary (T4=awards,
# T5=community), which is REVERSED vs the audit Ledger numbering (L4=community,
# L5=awards). After the rows are bucketed into the correct ledger, these
# carried-over self-placement phrases contradict the row's actual ledger.
# Normalize only the self-placement tokens; leave verification evidence and
# legitimate cross-references (e.g., "add to Ledger 3", "OR D6") untouched.
_LEDGER_PROSE_FIXES = [
    ("route to Ledger 5 (First-party/community)", "route to Ledger 4 (first-party/community)"),
    ("route to Ledger 5 first-party/community", "route to Ledger 4 first-party/community"),
    ("Tier 5 academic downstream citation", "Ledger 4 (first-party/community) downstream citation"),
    ("Tier 5 academic community", "Ledger 4 (first-party/community)"),
    ("already in baseline at Ledger 5", "already in baseline at Ledger 4"),
    ("Tier 4 (awards/recognitions)", "Ledger 5 (awards/recognitions)"),
]


def _fix_ledger_prose(notes: str) -> str:
    for old, new in _LEDGER_PROSE_FIXES:
        notes = notes.replace(old, new)
    return notes


def main():
    rows = load_verified()
    print(f"Loaded {len(rows)} verified records", file=sys.stderr)

    promotes = [r for r in rows if is_promote(r)]
    print(f"Candidate-promote: {len(promotes)}", file=sys.stderr)

    # Build per-tier buckets
    by_tier = {}
    for r in promotes:
        t = tier_of(r)
        by_tier.setdefault(t, []).append(r)

    def fmt_row(r):
        url = r.get("url", "")
        title = (r.get("title") or "")[:80].replace("|", "/")
        dim = r.get("dimension", "")
        notes = _fix_ledger_prose((r.get("notes") or "").strip())
        if len(notes) > 220:
            notes = notes[:217] + "..."
        return url, title, dim, notes

    # Drop USC institutional PR (out-of-scope per Apr 29 rule)
    def is_usc_pr(r):
        u = r.get("url", "")
        return "viterbischool.usc.edu" in u or "cs.usc.edu/news" in u or "isi.edu/news" in u

    promotes_filtered = [r for r in promotes if not is_usc_pr(r)]
    dropped_usc_pr = [r for r in promotes if is_usc_pr(r)]

    # Categorize for ledger placement.
    # NOTE: news-search Tier numbering is REVERSED vs the audit Ledger numbering
    # for 4 and 5 (see the Ledger section headers in news-coverage-audit.md):
    #   news-search T4 = Awards     -> audit Ledger 5 (Awards & Recognitions)
    #   news-search T5 = Community  -> audit Ledger 4 (First-Party & Community)
    ledger_2_external_media = []   # T1, T2 - third-party press, institutional features
    ledger_3_ecosystem = []        # T3 - blog posts, tutorials, aggregators
    ledger_4_community = []        # T5 - first-party / academic community
    ledger_5_awards = []           # T4 - awards, recognitions

    for r in promotes_filtered:
        t = tier_of(r)
        if t in ("T1", "T2"):
            ledger_2_external_media.append(r)
        elif t == "T3":
            ledger_3_ecosystem.append(r)
        elif t == "T4":
            ledger_5_awards.append(r)
        elif t == "T5":
            ledger_4_community.append(r)

    # Build the new round summary block
    lines = []
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("**May 19 parallel news-search Full audit (8-lane parallel Phase A + 4-batch parallel Phase B + citation-audit hook integration):**")
    lines.append("")
    n_total = len(ledger_2_external_media) + len(ledger_3_ecosystem) + len(ledger_4_community) + len(ledger_5_awards)
    lines.append(f"This round ran the complete `/news-search` Full audit pipeline for the first time as a single orchestrated workflow: 8 parallel Phase A agents fanned across Dimensions 1-8 (D9 is now the standalone [[citation-audit]] skill), aggregated to 166 unique candidate URLs, then 4 parallel Phase B verification agents fetched and applied the citation-verification rule. Net: **+{n_total} verified ledger rows** plus citation-audit hook integration.")
    lines.append("")
    lines.append(f"**Running total after May 19: {267 + n_total} verified items (267 prior, per the coverage-matrix total, + {n_total} May 19 verified ledger rows).**")
    lines.append("")
    lines.append(f"- **Ledger 1 (+0):** No new Tier 0 hits in the 6-day delta window. D8 PDF deep search scanned 22 fresh PDFs (Anthropic Opus 4.7, Mythos Preview, RSP v3.0/v3.1, OpenAI Sora 2, xAI Grok 4.1 + Frontier Framework, NIST AI 800-3 / GCR 26-069 / CSWP 50 / IR 8259r1, NIST NCCoE AI Agent ID/Authz, AISI Frontier Trends + Alignment Eval, FMF briefs, Five Eyes Careful Adoption Agentic AI Services, MITRE ATLAS OpenClaw, FINRA 2026 Annual Report, WEF Global Risks 2026, NBER w33998, OECD AI Papers No. 56, AuditBench, Anthropic Risk Report Feb 2026) — all 0 FORTIS term hits. Re-validated TrustLLM citation #881 in International AI Safety Report 2026 (already #8b). OWASP Gen AI Q2 2026 Solutions Landscape PDF was the highest-promise D4 lead but fetched 4.3 MB image-heavy PDF returned 0 FORTIS hits — track next quarterly OWASP refresh.")
    lines.append("")
    lines.append(f"- **Ledger 2 (+{len(ledger_2_external_media)}):** Mainstream press and institutional features dry in this window. USC Viterbi 'USC at ICLR 2026' institutional PR (`viterbischool.usc.edu/news/2026/04/usc-at-iclr-2026/`) does name DoxBench, Charts Are Not Images, and DecAlign with Yue Zhao credit — but per the Apr 29 audit rule USC institutional PR for conference papers is out of scope; not counted. The aiproductivity.ai best-agent-platforms blog (`aiproductivity.ai/blog/best-ai-agent-platforms/`) snippet claimed Aegis + agent-audit references but the page returned HTTP 403 to WebFetch; flagged for manual logged-in re-fetch (see Manual Verification Backlog below).")
    if ledger_3_ecosystem:
        lines.append("")
        lines.append(f"- **Ledger 3 (+{len(ledger_3_ecosystem)}):** Ecosystem adoption and dedicated platform/tutorial rows:")
        for i, r in enumerate(ledger_3_ecosystem, 1):
            url, title, dim, notes = fmt_row(r)
            lines.append(f"  - **L3.{i}** ({dim}) [{title}]({url}). {notes}")
    if ledger_4_community:
        lines.append("")
        lines.append(f"- **Ledger 4 (+{len(ledger_4_community)}):** First-party / academic community rows:")
        for i, r in enumerate(ledger_4_community, 1):
            url, title, dim, notes = fmt_row(r)
            lines.append(f"  - **L4.{i}** ({dim}) [{title}]({url}). {notes}")
    if ledger_5_awards:
        lines.append("")
        lines.append(f"- **Ledger 5 (+{len(ledger_5_awards)}):** Awards and recognitions:")
        for i, r in enumerate(ledger_5_awards, 1):
            url, title, dim, notes = fmt_row(r)
            lines.append(f"  - **L5.{i}** ({dim}) [{title}]({url}). {notes}")
    lines.append("")
    lines.append(f"- **Citation-affiliation hook (from /citation-audit; this is the formerly D9 dimension, now its own skill at `skills/citation-audit/`):** Embedded full Tier 0 and Tier 1 tables from `citation-affiliation-audit.md` (regenerated 2026-05-19 with the OpenAlex + Dimensions Analytics two-source combined audit after two real-data bug fixes: arXiv ID Dimensions DSL field requires the `arXiv:` prefix, and the default search type is `full_data` not `title_only` — both bugs caught by running the audit, not by static review). Headline numbers: 102 non-survey papers, OpenAlex found 43 with citations (1,624 unique citing papers), Dimensions found 30 (1,176 unique citing papers), 7 cross-source confirmed. **Tier 0 institutions citing FORTIS work: 39 entries** (notable: NIH × 3, Brookhaven × 3, Sandia × 2, LANL × 2, PNNL × 1, Argonne × 1, JPL × 1, DLR × 1, DESY × 1, Bundesbank × 3, CDC × 1, Meta Platforms × 5, OpenAI × 2, Google DeepMind × 1, RAND × 1). **Tier 1 institutions: 207 entries** (Microsoft Research 9, Tencent 8, AstraZeneca 7+5, IBM Research Zurich 7, Amazon 6+3, IBM Watson 6, Microsoft Research Asia 7, Adobe 5+2, Huawei 5+3, Alibaba 5, Merck 5+4, BlackRock 3+2, Visa 2+1, Robert Bosch 3+1, etc.). The embedded tables follow this round summary.")
    lines.append("")
    lines.append("- **Topic Validation (+56):** D4 topic-proximity sweep produced 56 topic-only rows (broad agent-security, anomaly-detection landscape, ChatGPT geolocation phenomenon coverage) recorded as context for grant narratives but not counted as direct coverage. Not enumerated individually — see `skills/news-search/scratch/phase-b-verified-B_paper.jsonl` and `phase-b-verified-A_news.jsonl` (`tier_guess: topic-validation`).")
    lines.append("")
    lines.append("- **Verified-negative recorded (+33):** Major FM-co system cards (Anthropic Opus 4.7, Mythos Preview, RSP v3.0/v3.1, Risk Report Feb 2026; OpenAI Sora 2; xAI Grok 4.1, Frontier Framework), NIST series (AI 800-3, GCR 26-069, CSWP 50, IR 8259r1, NCCoE AI Agent ID/Authz Concept Paper), AISI (Frontier Trends, Alignment Eval arXiv:2604.00788), FMF (3 issue briefs), Five Eyes Careful Adoption Agentic AI Services guide, MITRE ATLAS OpenClaw Investigation MTR-26-00176-1, FINRA 2026 Annual Regulatory Oversight Report, WEF Global Risks Report 2026, NBER w33998 'AI and the Fed', OECD AI Papers No. 56 (Feb 2026), AuditBench (arXiv:2602.22755), OWASP Gen AI Q2 2026 Solutions Landscape, CVPR 2026 ComputeReporting policy page + CRF PDF (does NOT name the Hao/Zhao/Ghassemi paper that motivated the policy), npj AI s44387-026-00076-4 (paywall held — see manual verification backlog), ACM CSUR Jun 2026 diffusion survey (10.1145/3783986, verified via arXiv preprint 2404.18886v3 — does NOT cite the Yang/.../Zhao 2023 CSUR diffusion survey).")
    lines.append("")
    lines.append("- **Disambiguation registry recommendations (add to `skills/news-search/references/disambiguation-registry.md`):**")
    lines.append("  - **Hangbo Zhao** — USC AME/BME assistant professor, junior research award recipient 2026. Surfaced as false positive on the USC Viterbi 'People Behind the Work 2026 Awards' page under Yue Zhao searches.")
    lines.append("  - **Wei Zhao (SiriuS)** — *Zhao, W. et al. (2025), SiriuS: Self-improving multi-agent systems via bootstrapped reasoning, arXiv:2502.04780*. Surfaced as 'Zhao et al., 2025[49]' in OECD AI Papers No. 56 (Feb 2026, p.20).")
    lines.append("  - **AuditLuma** — CSDN-hosted AI code-audit project. Recurring collision target for `agent-audit` queries; not related to FORTIS agent-audit.")
    lines.append("  - **Moonshot AI Kiwi-do** — different from Moonlight.io paper-aggregator outlet (the 'Moonlight' name collision).")
    lines.append("  - **Hangbo Zhao + Wei Zhao + AuditLuma + Moonshot Kiwi-do**: 4 new collision targets logged this round.")
    lines.append("")
    lines.append("- **Domain registry harvest (add to `skills/news-search/references/domain-registry.md`):**")
    lines.append("  - `mit-calc.csail.mit.edu` (class: `university` / coauthor-institution project page)")
    lines.append("  - `publications.pik-potsdam.de` (class: `university` / coauthor-institution publications repository)")
    lines.append("  - `medium.com/advancedai` (class: `tech-blog` / Medium publication)")
    lines.append("")
    lines.append("- **Manual verification backlog (URLs that returned 403 / 404 / paywall and need a logged-in browser re-fetch):**")
    lines.append("  - `aiproductivity.ai/blog/best-ai-agent-platforms/` — snippet claimed Aegis + agent-audit references; verify direct mention or set verified-negative.")
    lines.append("  - `tomshardware.com/.../chatgpt-becomes-a-formidable-geo-guesser` — phenomenon-discovery piece; verify whether DoxBench is named or only the underlying ChatGPT capability.")
    lines.append("  - `www.nature.com/articles/s44387-026-00076-4` — npj AI healthcare review (Mar 2026); 303 → idp.nature.com auth. May overlap with existing #66cr TrustLLM npj cluster.")
    lines.append("  - `sciencedirect.com/.../S1566253525005895` — Elsevier Information Fusion AD foundation-models survey; 403.")
    lines.append("  - `securityboulevard.com/2026/02/openclaw-...` — 403 (cross-post of NSFOCUS analysis; NSFOCUS original was verified-negative for FORTIS).")
    lines.append("  - `aimodels.fyi/papers/arxiv/jaildam-...` — 403 (likely aggregator; tier cap 3 if reachable).")
    lines.append("  - `researchgate.net/publication/402481760_Sovereign-OS` — 403 (ResearchGate routinely blocks WebFetch).")
    lines.append("  - `forum.cspaper.org/topic/170/...` — 301 → article removed.")
    lines.append("  - `github.com/openclaw/openclaw/discussions/36663` — 410 'Discussions disabled' (phantom from search-engine cache).")
    lines.append("  - `paperswithcode.com/paper/stealthrank-...` — 302 → 404.")
    lines.append("  - GAO 26-107859 + GAO 25-107197 + fdd.org Mar 2026 + federalnewsnetwork May 2026 — all 403 to WebFetch.")
    lines.append("")
    lines.append("- **D10 External Deep Research:** Out of scope for this automated audit pass. The user runs this manually in ChatGPT Deep Research / Gemini Deep Research / claude.ai with a self-contained prompt; output goes to `external-research/{source}-2026-05.md`. Prompt template generated in this audit cycle is at `external-research/PROMPT-2026-05-19.md` (see file). Run quarterly.")
    lines.append("")
    lines.append("- **Codex Phase B review (skipped):** Codex review of Phase B output was skipped this round because the implementation-review cycle for the citation-audit skill split was already in flight earlier in the same session. The Phase A/B agents themselves apply the citation-verification rule with verbatim quotes; Codex review can be added in a follow-up pass if any of the 21 candidate-promote rows are questioned.")
    lines.append("")
    lines.append("Lessons reinforced this round:")
    lines.append("- **Static review does not catch API semantics.** Three /implement-review rounds + a smoke test all passed for the citation-audit Dimensions integration before this Full audit caught two real bugs (arxiv_id prefix, default search-type) only when actually running against the publication inventory. The fail-loud `_query_dimensions` wrapper from Round 1 of that review cycle paid off here.")
    lines.append("- **Highest-promise topic-proximity lead was wrong.** OWASP Gen AI Q2 2026 Solutions Landscape PDF was flagged `phase_b_priority` by the D4 agent and was the single highest-promise D8-style PDF this round — fetched 4.3 MB, 0 hits. Worth retrying when the next OWASP edition lands.")
    lines.append("- **PDF term scan beats LLM summarization for citation extraction.** B_paper Phase B caught a SkillSieve (arXiv:2604.06550) citation of agent-audit only via `pdf_term_scan.py`; the WebFetch summarizer missed it. Continue routing all candidate PDFs through the term scanner.")
    lines.append("")

    # Now embed the citation-affiliation-audit.md content (with adjusted heading levels)
    cite_text = CITE_AUDIT.read_text(encoding="utf-8")
    # Drop the embedded file's single top-level H1 title (the wrapper section
    # heading below already titles this block), then shift every remaining
    # heading down one level so Tier / Summary / Coverage sit as children of
    # the wrapper rather than as a same-level sibling of it.
    cite_lines = []
    dropped_top_h1 = False
    for ln in cite_text.splitlines():
        m = re.match(r"^(#+)( .*)", ln)
        if m:
            if not dropped_top_h1 and len(m.group(1)) == 1:
                dropped_top_h1 = True
                continue
            cite_lines.append("#" + m.group(1) + m.group(2))
        else:
            cite_lines.append(ln)
    cite_adjusted = "\n".join(cite_lines)

    lines.append("## Citation Affiliation Evidence (integrated from /citation-audit skill, 2026-05-19)")
    lines.append("")
    lines.append("*The following section is integrated verbatim from `citation-affiliation-audit.md` per the news-search cross-skill citation-audit hook. Canonical copy lives in that separate file; this embed makes the unified report self-contained for tenure / promotion / grant readers. Re-run the standalone audit with `/citation-audit --source both` to refresh.*")
    lines.append("")
    lines.append(cite_adjusted)

    new_text = "\n".join(lines)

    # Read existing news-coverage-audit.md
    existing = NEWS_AUDIT.read_text(encoding="utf-8")

    # Update the top "*Updated: 2026-05-13 ...*" line: move it to a new "*Previous: ...*" entry, and prepend new "*Updated: 2026-05-19 ...*"
    # The pattern: lines starting with "*Updated: " followed by other "*Previous: " lines
    updated_line_pattern = re.compile(r"^(\*Updated: .*\*)$", re.MULTILINE)
    match = updated_line_pattern.search(existing)

    new_updated = (
        "*Updated: 2026-05-19 (Full /news-search Full audit run: 8-lane parallel Phase A across D1-D8 → 166 unique candidates → 4-batch parallel Phase B verification → "
        f"+{n_total} verified ledger rows (0 Ledger 1, 0 Ledger 2, {len(ledger_3_ecosystem)} Ledger 3, {len(ledger_4_community)} Ledger 4, {len(ledger_5_awards)} Ledger 5) "
        "plus full citation-audit hook integration (39 Tier 0 + 207 Tier 1 institution-affiliation rows embedded from regenerated citation-affiliation-audit.md after two Dimensions DSL bug fixes: arXiv ID prefix, title_only search type). "
        "Highest-promise D4 lead OWASP Gen AI Q2 2026 Solutions Landscape PDF verified-negative on direct fetch. No new Tier 0 hits in D8 PDF deep search across 22 fresh PDFs. New disambiguation: Hangbo Zhao, Wei Zhao (SiriuS), AuditLuma, Moonshot Kiwi-do. Manual verification backlog: 11 entries flagged.)*"
    )
    if match:
        old_updated = match.group(1)
        # Convert old "*Updated: ...*" to "*Previous: ...*"
        old_as_previous = "*Previous: " + old_updated[len("*Updated: "):]
        # Replace the matched line with new_updated + newline + old_as_previous
        existing = existing[:match.start()] + new_updated + "\n" + old_as_previous + existing[match.end():]
    else:
        # Fallback: prepend after the title line
        existing = re.sub(r"^(# .*\n+)", r"\1\n" + new_updated + "\n\n", existing, count=1)

    # Append the new round summary + hook embed
    existing = existing.rstrip() + "\n" + new_text + "\n"

    NEWS_AUDIT.write_text(existing, encoding="utf-8")
    print(f"news-coverage-audit.md updated: {len(existing)} bytes", file=sys.stderr)
    print(f"  +{n_total} new ledger rows", file=sys.stderr)
    print(f"  L2: {len(ledger_2_external_media)} (0 after USC PR drop)", file=sys.stderr)
    print(f"  L3: {len(ledger_3_ecosystem)}", file=sys.stderr)
    print(f"  L4: {len(ledger_4_community)}", file=sys.stderr)
    print(f"  L5: {len(ledger_5_awards)}", file=sys.stderr)
    print(f"  USC PR dropped: {len(dropped_usc_pr)}", file=sys.stderr)


if __name__ == "__main__":
    main()
