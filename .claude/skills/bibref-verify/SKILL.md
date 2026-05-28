---
name: bibref-verify
description: Use when auditing a paper's existing .bib for hallucinated citations or stale metadata before submission, especially when bib entries came from co-authors or automated tools and may include fabricated authors, future arXiv IDs, or preprints already published in peer-reviewed venues. Companion to bibref-filler (which adds new citations); this skill audits existing ones.
---

# bibref-verify

## Overview

Audits an existing `.bib` for hallucinated citations and stale metadata. Output: a single `REFERENCE-CHECK.md` with audit findings and ready-to-paste BibTeX fixes. **Read-only on the `.bib` file**; the user applies fixes manually.

Distinct scope from `bibref-filler` (a separate shared skill, typically bootstrapped to `.agent-config/repo/skills/` rather than tracked in the project repo): `bibref-filler` adds new citations to prose during drafting; `bibref-verify` audits existing entries before submission. The two skills do not overlap.

## When to Use

- Paper or proposal is approaching submission for a venue that desk-rejects on hallucinated citations (NeurIPS, ICML, ICLR, KDD, NSF, NIH, etc.)
- The `.bib` contains entries the user did not personally add (co-author contributions, automated bib generators, AI assistants)
- Suspected failure modes: arXiv IDs with future `YYMM`, BibTeX keys that look like raw arXiv IDs, papers cited as `arxiv preprint` that may have been published since
- The user wants a third-party verification trail for reviewer scrutiny

Skip when: the paper is in early draft and most citations are placeholder; the bib has fewer than 10 entries (manual review is faster); the user only needs to ADD new citations (use `bibref-filler` if available).

## Pipeline (one-shot, 4 passes, ~15-20 min)

| Pass | Method | Output |
|---|---|---|
| A. Distributed web-search | `ceil(N/24)` parallel agents (max 8); each verifies a contiguous chunk of the `.bib` via WebSearch + WebFetch | per-agent verdict tables, returned as Agent tool results |
| B. S2 cross-verification | Resolve the helper relative to this `SKILL.md`: set `<skill-dir>` to the directory containing this file (for example, `skills/bibref-verify` in a source checkout or `.claude/skills/bibref-verify` after pack deployment), then run `<python> <skill-dir>/scripts/verify-bib-s2.py <bib-path>`, where `<python>` is the project interpreter (on Windows, prefer the Miniforge / conda interpreter such as `C:/Users/<u>/miniforge3/envs/py312/python.exe`; do not rely on the Windows Store `python` alias). Reads `S2_API_KEY` from env or `.env`; arXiv batch + title-search fallback at sim ≥ 0.85 | `<bib-dir>/S2-VERIFY-REPORT.md` |
| C. Codex review | Write the consolidated draft to `<bib-dir>/REFERENCE-CHECK.md`, then invoke the `implement-review` skill, Round 1, with the report path as the artifact under review | `Review-Codex.md` at repo root |
| D. Targeted web-fetch (conditional) | If Codex Round 1 raises pushbacks, dispatch one parallel verification agent per disputed claim, fetching the canonical source (OpenReview, journal page, arXiv abstract) | per-claim verdict (CONFIRMED / REFUTED / INCONCLUSIVE) |

After all passes finish, consolidate into the final `<bib-dir>/REFERENCE-CHECK.md`, overwriting the draft.

**Order note**: The pipeline order above is the normalized recommended workflow. The validation history described under "Real-world impact" ran passes in a different order because Pass B (S2) was added mid-session; this canonical order is cleaner because Pass C (Codex) sees both web-search and S2 evidence consolidated in a single artifact.

### Pass A details

Per-agent prompt must include:
- The exact `.bib` file path and a contiguous line range to verify
- Red flags: future-`YYMM` arXiv IDs (e.g., `2611.xxxxx` after May 2026); duplicate arXiv IDs across multiple keys with different author lists; year ≥ current with no clear venue; 25+ author lists on non-consortium papers; `(in preparation)` placeholders
- Output format: markdown table with one row per entry, columns `Key | Verdict | Evidence | Notes` where Verdict is one of VERIFIED / DRIFT / REFUTED / INCONCLUSIVE
- Hard constraint: do NOT modify any file (read-only audit)

Dispatch all agents in a single message with multiple Agent tool calls so they run concurrently.

### Pass B known false positives

S2 has weak indexing for several categories. Treat S2 NOT-FOUND on these as INCONCLUSIVE, not HALLUCINATION:

- **Books and pre-arXiv-era papers** (Hebb 1949, Shannon 1948, Cover 2006, Newman 2010, Lovasz 1993, etc.). Title-search picks the wrong paper, producing AUTHOR-MISMATCH or YEAR-MISMATCH.
- **Transformer Circuits Thread web posts** (`elhage2021mathematical`, `Bricken2023Monosemanticity`, `Templeton2024ScalingMonosemanticity`, `ameisen2025circuit`). S2 does not index TCT.
- **Diacritics encoding mismatches** — bib `\'i` vs S2 `í` causes substring-match failure even when the names refer to the same person (e.g., `garc\\ia-perez` vs `garcía-pérez`).
- **Version-year mismatches** — S2 sometimes returns the arXiv-preprint year rather than the final journal or proceedings year. The bib year is usually correct for the published version; do not auto-flag as DRIFT without web verification.
- **Short or generic-title matches** — for older or broad-topic works (e.g., classical theorems cited by short title), S2 title-search may pick a related-but-wrong paper. Verify against the canonical publisher page before classifying as DRIFT or REFUTED.
- **GitHub issue and pull-request citations** — bib keys that point to a GitHub-repository issue or PR (typical patterns: `<repo>-<number>`, `<owner-repo>-<number>`, or a `url` field linking to `github.com/<owner>/<repo>/{issues,pull}/<n>`) cite real artifacts that S2 does not index. Common in benchmark and robustness papers that ground each subtype to a documented production failure. Verify via direct WebFetch of the issue URL.
- **Vendor product or SDK documentation pages** — model-spec, API-reference, and product-doc citations (e.g., model spec pages on a vendor's `docs/` site, SDK reference pages, public roadmap entries) are not S2-indexable. Verify via WebFetch of the URL itself.

Verify these via Pass A's web-search results or by direct WebFetch of the publication page.

### Pass C handoff

Pass C uses the existing `implement-review` skill. The artifact under review is `<bib-dir>/REFERENCE-CHECK.md` (the draft consolidation from Passes A + B), not the `.bib` itself. Codex's role is sanity-check, not redo-the-audit.

The Pass-C prompt should ask Codex to:
1. Independently verify each REFUTED and DRIFT classification via WebFetch of the canonical source
2. Spot-check 5-10 entries from the VERIFIED bucket for false negatives
3. Take an explicit position on the recommended fix actions (the scope-challenge contract from `implement-review`)

### Pass D triggers (conditional)

Pass D runs only if Codex Round 1 raises factual pushbacks (REFUTED on a finding the audit had marked DRIFT or VERIFIED). For each disputed claim, dispatch one verification agent in parallel:
- Fetch the canonical source URL Codex cited
- Compare bib metadata vs canonical source field by field
- Return CONFIRMED (Codex correct), REFUTED (Codex wrong), or INCONCLUSIVE

Bundle all verification agents into one message of parallel Agent tool calls. One agent per claim, not bundled.

## Consolidation: REFERENCE-CHECK.md format

Single Markdown file at `<bib-dir>/REFERENCE-CHECK.md`. Sections in this order:

1. **Header** — date, methods table (4 passes), source bib path, status line ("check only, no edits to the .bib file")
2. **Global summary** — severity counts table (HALLUCINATION / DRIFT-venue / DRIFT-metadata / INCONCLUSIVE / VERIFIED) with totals that sum to the bib entry count
3. **Red — HALLUCINATION** — must-fix entries with real arXiv IDs but fabricated authors. One row per entry: `Key (line) | Real authors | bib's authors | Action`. Include a ready-to-paste corrected `@type{}` block for each.
4. **Yellow — DRIFT (venue upgrade)** — arXiv preprints already published. One row per entry: `Key | Now published in (venue, year, vol/issue/article-id, DOI)`. Include corrected entry block.
5. **Yellow — DRIFT (metadata error)** — year, pages, co-author list, or BibTeX field-layout errors. Include corrected entry block.
6. **Gray — INCONCLUSIVE** — textbooks S2 cannot index, `(in preparation)` placeholders. No fix action; user discretion.
7. **Retracted claims** (only if any) — Pass-A findings overturned by Passes B/C/D, kept for traceability.
8. **Side findings** — duplicate keys; same paper with two different keys; cite-vs-bib gap. Out of audit scope but worth flagging.
9. **Verification artifacts** — paths to `S2-VERIFY-REPORT.md`, `Review-Codex.md`, the script. Plus the exact command to re-run.

For every non-VERIFIED entry, include a ready-to-paste fix as a fenced BibTeX block. Example:

```bibtex
@inproceedings{huben2024sparse,
  title={Sparse Autoencoders Find Highly Interpretable Features in Language Models},
  author={Huben, Robert and Cunningham, Hoagy and Smith, Logan Riggs and Ewart, Aidan and Sharkey, Lee},
  booktitle={The Twelfth International Conference on Learning Representations},
  year={2024}
}
```

## Required infrastructure

- `<skill-dir>/scripts/verify-bib-s2.py`, where `<skill-dir>` is the directory containing this `SKILL.md` (`skills/bibref-verify` in a source checkout, `.claude/skills/bibref-verify` after pack deployment); uses Python stdlib only, no third-party deps
- `S2_API_KEY` in `.env` at the repo root (or as a user-level env var)
- Codex availability for Pass C (terminal channel or IDE plugin)
- `WebSearch` and `WebFetch` tools available to parallel agents

Graceful degradation:
- No `S2_API_KEY` → skip Pass B, warn the user, the audit is meaningfully degraded but still useful
- Codex unavailable → skip Passes C + D, warn the user, run only A + B
- Pass D never auto-runs if Codex Round 1 has no pushbacks

## Output location

Default: `<bib-dir>/REFERENCE-CHECK.md` (always emitted) and `<bib-dir>/S2-VERIFY-REPORT.md` (emitted only when Pass B runs; absent in S2-degraded mode).

When Pass B or Pass C is skipped because of missing infrastructure, the consolidated `REFERENCE-CHECK.md` must mark the audit as degraded in its status line (for example, `Status: check only, no edits to .bib; S2-degraded — no S2_API_KEY`). This prevents downstream readers from treating a partial audit as a full one.

For paper submodules (Overleaf-bridged), this places the reports inside the submodule directory. The submodule's `git status` will show the files as untracked. The user decides whether to commit and push to Overleaf or keep local-only.

## Common mistakes

| Mistake | Fix |
|---|---|
| Skipping Pass B because "Pass A already covered web-search" | S2 catches venue-upgrade misses Pass A consistently misses (~5/144 in observed cases). The two are independent sources, not redundant. |
| Treating S2 NOT-FOUND on books / pre-arXiv papers as a hallucination signal | Whitelist these categories (see Pass B section). S2 does not index them well. |
| Modifying the `.bib` during the audit | The skill is audit-only by design. All fixes are user-applied via copy-paste from `REFERENCE-CHECK.md`. |
| Sequential web-search instead of parallel agents in Pass A | Serial Pass A takes 30+ minutes for a 100-entry bib. Always dispatch in parallel. |
| Sending the whole `.bib` to Codex in Pass C instead of the consolidated `REFERENCE-CHECK.md` | Codex's role is to sanity-check the audit, not redo it. Send the report path. |
| Auto-committing the report to a paper submodule | The report is local-by-default. Some collaborators do not want the audit visible in Overleaf history; let the user decide. |
| Hardcoding `python` as the interpreter on Windows | The Windows Store stub for `python` may not work. Use the user's miniforge / conda Python explicitly, e.g., `C:/Users/<u>/miniforge3/envs/py312/python.exe`. |

## Security notes

- `S2_API_KEY` is account-level read-only access to public papers; leakage risk is low (someone could spend the user's rate limit budget) but the key still belongs in `.env`, not in the repo
- The `.bib` file is never modified by the skill; the report is the only artifact
- Reports placed inside paper submodules push to Overleaf if the user commits them — flag this before commit

## Real-world impact

Case A: 144-entry academic-paper bib (typical NeurIPS-style submission):
- Pass A flagged 4 hallucinated entries (real arXiv IDs with fabricated author lists) and 9 metadata DRIFTs; 2 of those Pass-A claims were later retracted by Codex after independent web verification
- Pass B caught 5 venue-upgrade misses Pass A had not detected (arXiv preprints already accepted at peer-reviewed venues)
- Pass C confirmed convergence after resolving S2's expected false positives via targeted WebFetch
- Pass D (1 round, 5 parallel agents) verified all 5 of Codex's disputed claims
- Final: 4 HALLUCINATION + 16 DRIFT + 2 INCONCLUSIVE + 122 VERIFIED

Case B: 55-entry bib with heavy non-academic citations (~33% GitHub issues / vendor-doc URLs):
- Pass B returned 18 NOT-FOUND, all confirmed false positives via Pass A (GitHub issues + vendor docs are not S2-indexable)
- Pass A flagged 1 HALLUCINATION where the bib's author list shared only 2 of 9 names with the real published paper's author list, plus 8 DRIFTs across issue-paraphrase mischaracterization, venue/title drift, missing arXiv ID, and editorial paraphrase
- Pass C confirmed all classifications and caught report-internal arithmetic errors; no factual pushback so Pass D did not trigger
- Final: 1 HALLUCINATION + 8 DRIFT + 0 INCONCLUSIVE + 46 VERIFIED. Demonstrates the skill scales to bibs with heavy non-academic citations as long as Pass B false positives are correctly classified.
