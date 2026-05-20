---
name: citation-audit
description: Systematic bibliometric audit of citing-paper author affiliations across OpenAlex and Dimensions Analytics. Use when the user wants to find which notable institutions (government agencies, foundation model companies, national labs, Big Tech, finance, pharma) have authors who cite their published work. Pair with the news-search skill for full external-impact evidence; this skill is the bibliometric half, news-search is the editorial-coverage half. Also use for legacy prompts: "citation audit", "affiliation audit", "citation-affiliation audit", or "Dimension 9 audit" (this skill was previously Dimension 9 inside news-search; split out 2026-05).
---

# Citation Affiliation Audit

Find citing papers where at least one author is affiliated with a notable institution. Surfaces adoption evidence that web search and PDF search miss entirely.

**Important framing:** This finds "researchers AT [institution] cited your tool", not "[institution] officially endorses your tool." The distinction matters for grant narratives and tenure materials. Use the framing "researchers at NASA / JPL / NIH cited [paper]" rather than "NASA cited [paper]" unless the citing paper itself names the institution as the work's home.

## When to Use

- Before tenure / promotion materials
- Before grant applications requiring broader-impact evidence
- After major citation milestones (1000+ Scholar citations, an inclusion in a foundation-model system card)
- Once per semester as a periodic audit
- As a sub-step inside the [[news-search]] full audit (the news-search skill hooks this audit's output into its final report; see "Integration with news-search" below)

## Inputs

- `data/publications.json` -- all papers (titles, venues, years, paper_url for arXiv/DOI extraction)
- (Optional, for `--source both` / `dimensions`) `.env` with `DIMENSIONS_API_KEY` from Digital Science scientometric tier
- Prior `citation-affiliation-audit.md` if it exists (this run overwrites it; older Tier 0 rows can be eyeballed for stability)

## Sources

Two bibliometric sources, orchestrated by `scripts/citation_affiliation_audit.py`:

- **OpenAlex** (no credentials required). Standard open citation graph. Undercounts CS papers severely -- PyOD shows ~24 citations on OpenAlex versus 1,000+ on Google Scholar -- but covers a broad swath of the literature and is the safe no-credential default.
- **Dimensions Analytics API** (requires `DIMENSIONS_API_KEY` in `.env`, scientometric researcher access tier from Digital Science). Stronger CS coverage in practice, plus GRID-normalized `research_orgs` institution affiliations.

The orchestrator defaults to `--source openalex`. Use `--source both` for the strongest combined audit when Dimensions credentials are configured; `--source dimensions` runs only Dimensions.

## Pipeline

1. **Load ALL papers** from `data/publications.json` (not a hand-picked subset). Only surveys are excluded via title keywords (`comprehensive survey`, `a survey on`, `a survey of`).
2. **Locate each paper on every enabled source** by arXiv ID, then DOI, then a strict title match. Title matching uses a two-pass strategy: exact normalized-title match first, then prefix-anchor (pre-colon acronym like `PyOD:`, `TrustGen:`) plus high word overlap (50%+ with prefix, 70%+ without).
3. **Query citing papers per work**. OpenAlex uses `filter=cites:{work_id}`; Dimensions uses `where reference_ids = "<pub_id>"`. Per-work queries preserve the mapping from each citing paper back to which of your works it cites; aggregate batch queries would lose that attribution.
4. **Extract author institution affiliations** from every citing paper. Dimensions provides GRID-normalized `research_orgs` directly; OpenAlex returns `authorships[].institutions[].display_name`. The shared classifier in `scripts/citation_audit_common.py` matches both against the same Tier 0 / Tier 1 regex banks (see "Tier definitions" below).
5. **Deduplicate** by `(institution, citing title, cited work)`. A citation seen by both sources collapses to one row with `source = openalex+dimensions`.
6. **Write results** to `citation-affiliation-audit.md` at the repo root, with a `Source` column on the Tier 0 / Tier 1 tables and per-source Coverage subsections.

The shared logic lives in `scripts/citation_audit_common.py`. The two source modules (`scripts/citation_affiliation_audit.py` for OpenAlex, `scripts/citation_affiliation_audit_dimensions.py` for Dimensions) can also be invoked standalone for debugging.

## Comprehensiveness Rule

**Search every paper, not just the high-profile ones.** You do not know where the gold lies. The ESA OPS-SAT citation came from PyOD (obvious), but NASA JPL cited a less obvious paper. The CDC cited ECOD, not PyOD. Deutsche Bundesbank cited ECOD. Morgan Stanley cited XGBOD. Coverage can come from any paper.

The script reads `data/publications.json` and searches ALL non-survey entries. Do not skip papers because they have low citation counts or seem unlikely to have notable adopters.

## Tier Definitions

The authoritative source for tier classification is the regex banks in `scripts/citation_audit_common.py` (`TIER0_PATTERNS` and `TIER1_PATTERNS`). The lists below are a human-readable summary of what those banks match as of the latest commit; if a name is in one place but not the other, the code wins and this prose is stale.

The classifier uses regex patterns on institution names:

- **Tier 0**: Government agencies (NIST, NASA / JPL, NIH, CDC, FDA, DARPA, NOAA, FAA, CISA, DHS), space agencies (ESA, JAXA, ISRO, DLR, CNES), national labs (LANL, LLNL, Sandia, ORNL, Argonne, Brookhaven, PNNL, INL, Fermilab, SLAC), defense contractors (Raytheon, Lockheed, Northrop, BAE, MITRE, RAND, Booz Allen, Leidos), foundation model companies (OpenAI, Anthropic, DeepMind, Meta AI), central banks (Federal Reserve, ECB, BIS, Bundesbank, Bank of England, BoJ, PBoC), and international bodies (WHO, IAEA, World Bank, OECD, NATO).
- **Tier 1**: Big Tech (Google, Microsoft, Amazon, Apple, NVIDIA, Intel, IBM, Salesforce, Adobe, Samsung, Huawei, Tencent, Alibaba, Baidu, ByteDance), finance (Goldman, JPMorgan, Morgan Stanley, Citadel, Two Sigma, BlackRock, Bloomberg, Capital One, Wells Fargo, Visa), pharma / healthcare (Pfizer, Roche, Novartis, AstraZeneca, Merck, Eli Lilly, Sanofi, Moderna, Mayo Clinic, Cleveland Clinic), industrial (Siemens, Bosch, Honeywell, GE), telecom (Ericsson, Nokia, Cisco, Qualcomm), automotive / aerospace (Tesla, SpaceX), retail (Walmart), consulting (Deloitte, McKinsey, PwC, Accenture).

Tier order matters: a citing-paper row matches at most one tier, Tier 0 wins on tie. Some patterns use `\b` boundaries on short acronyms (e.g., `\bNIST\b`) to dodge substring collisions.

When adding a new pattern, place Tier 0 organizations in the Tier 0 list and check for substring conflicts with existing patterns (e.g., `Google` is in Tier 1 with a `(?!.*DeepMind)` exclusion so Google DeepMind lands in Tier 0).

## What to Exclude

- **Survey papers** are filtered automatically by title keyword. OpenAlex conflates papers with similar titles, producing high false-positive rates on surveys.
- **Papers with ambiguous short names** (e.g., `BOND` matching biology papers). The script uses the same prefix-anchor + word-overlap thresholds described in step 2 of the Pipeline section (50% overlap with a prefix-anchor like `PyOD:`, 70% without). If the match is rejected, the paper appears in the `not_found` list.
- **Grant-funded affiliations vs. employment**: NIH appears as an affiliation on many papers, but most are university researchers with NIH grants, not NIH intramural staff. The output uses the framing "researchers AT [institution]" to avoid overclaiming. NIH Clinical Center and NIH intramural programs are stronger signals than generic `National Institutes of Health`.

## Run Modes

| Mode | When | Command |
|------|------|---------|
| **Quick check** | First time, smoke-test access | `python scripts/citation_affiliation_audit.py --source both --limit 5` |
| **OpenAlex only** (default) | No Dimensions credentials, or quota-conscious | `python scripts/citation_affiliation_audit.py` |
| **Dimensions only** | Compare Dimensions coverage vs OpenAlex independently | `python scripts/citation_affiliation_audit.py --source dimensions` |
| **Full combined** | Semester audit, tenure prep, major milestone | `python scripts/citation_affiliation_audit.py --source both` |
| **Dimensions API smoke test** | After getting a new key or before a real run | `python skills/citation-audit/scripts/dimensions_smoke_test.py` |

Full combined run takes ~50-80 minutes (OpenAlex pass ~30-60 min + Dimensions pass ~10-20 min). Use `--limit N` to scope to the first N papers for a quick verification pass.

## Known Limitations

- **Coverage gaps still exist with both sources.** Even with `--source both`, the audit lags Google Scholar on CS citation counts. Treat the output as a lower-bound estimate, not a census.
- **Google Scholar has no API.** Scholar has the most complete citation data but cannot be queried programmatically. For high-priority papers where the combined audit returns few results, run a manual Scholar spot-check.
- **Semantic Scholar** has good citing-paper recall on some venues but affiliation data is mostly empty, so it is weak for this specific audit. Useful only as a third-pass title-discovery step.
- **Re-run periodically.** Both OpenAlex and Dimensions backfill over time. A paper that shows 0 citations today may show 50 in six months. Re-run at least once per semester. Recent preprints (2026) will only appear in future runs.
- **Identifier resolution order.** Each source tries arXiv ID, then DOI, then a strict title match. arXiv lookup is the most reliable for CS papers but still requires the source to have ingested the paper.
- **Source disagreements are signal.** When OpenAlex and Dimensions disagree on whether a paper has notable citations, prefer the higher-recall source for follow-up rather than picking one as ground truth.
- **Exact-string cross-source dedup.** The merge key is `(institution, citing_title, cited_work)`. Variants like `Google` vs `Google LLC` or punctuation-variant titles may produce near-duplicate rows that span sources. The audit Markdown footer carries a caveat. Fuzzy dedup is deferred until the audit becomes the source of record for exact counts.

## Improving Coverage

OpenAlex alone covers ~50% of papers as of Apr 2026. The integrated **Dimensions Analytics API** path closes a meaningful share of that gap on CS papers; run `--source both` for the strongest combined coverage.

Setup (one-time):

1. Get a key from `app.dimensions.ai` -> account settings -> API (scientometric researcher access tier from Digital Science).
2. Add `DIMENSIONS_API_KEY=<key>` to `.env` (see `.env.example`). Access expires 2027-01-01 unless renewed.
3. `pip install dimcli python-dotenv` if not already present.
4. Verify with `python skills/citation-audit/scripts/dimensions_smoke_test.py` before the first real run; the smoke test checks `research_orgs`, citation graph fields, and classification access.

Additional gap-closers still useful when Dimensions falls short:

- **Semantic Scholar API** (`api.semanticscholar.org/graph/v1/paper/{id}/citations`): better CS coverage than OpenAlex on some venues, but affiliation data is mostly empty. Useful as a third-pass title-discovery step, then cross-reference titles back to OpenAlex or Dimensions for institution data.
- **Web of Science / Scopus APIs**: best affiliation data but require USC library credentials. Use for manual verification of Tier 0 claims that show up in only one source.
- **Re-running the script** every 3-6 months is the simplest way to improve coverage, since both OpenAlex and Dimensions backfill continuously.

## Output

Results go to `citation-affiliation-audit.md` at the repo root. The file includes:

- **Header**: per-source headline numbers (papers with citations + unique citing papers per source), so combined runs do not present `max(...)` as a single combined truth.
- **Tier 0 table**: Category, Institution, Country, Your Work Cited, Citing Paper, Year, Source.
- **Tier 1 table**: same columns.
- **Summary by institution**: aggregated counts per (institution, category).
- **Coverage subsections**: per-source breakdown of papers with citations, indexed-but-zero-citations, and not-found lists. Per-source so a paper missing from OpenAlex but found by Dimensions does not appear in a combined "not found" list.
- **Methodology footer**: framing reminder (researchers AT institution, not endorsement) + cross-source dedup caveat.

## Integration with [[news-search]]

The [[news-search]] skill runs editorial-coverage discovery across D1-D8 + D10 (press, government PDFs, ecosystem, deep-research-tool output). Its final report is `news-coverage-audit.md`. When the user runs the news-search Full audit, it should read the existing `citation-affiliation-audit.md` and integrate the full citation evidence as a cross-skill section. This contract is authored here and mirrored semantically in `skills/news-search/SKILL.md`'s "Cross-skill: citation-audit integration" section (same three states, same full-table embedding rule, same no-silent-auto-invoke policy; wording differs to fit each skill's surrounding context). If you change one side, update the other in the same commit.

1. **Before starting** news-search Full audit, check whether `citation-affiliation-audit.md` exists at the project root and record its modification time.
2. If the file is **missing**, tell the user: "Citation affiliation audit has never run on this project; recommend running `/citation-audit --source both` (or `--source openalex` if no Dimensions credentials) before the news-search full audit." Do not auto-invoke without confirmation; a full citation audit is 30-80 minutes and may use Dimensions quota.
3. If the file is **fresh** (modified within the last 30 days), copy the citation audit's **full Tier 0 table, full Tier 1 table, Summary by Institution subsection, and per-source Coverage subsections** verbatim into `news-coverage-audit.md` under `## Citation Affiliation Evidence (integrated from citation-audit)`. Add a one-line freshness stamp and a link back to `citation-affiliation-audit.md` as the canonical separate copy.
4. If the file is **stale** (older than 30 days), integrate the same full content, mark the section header as `## Citation Affiliation Evidence (stale, regenerate via /citation-audit)`, and surface the staleness to the user. Do not silently truncate to a top-hit summary.

The hook is read-only from news-search's perspective. It never re-runs the citation audit silently; the user decides whether to regenerate. Verbatim full-table embedding is intentional: `news-coverage-audit.md` is the single artifact tenure / promotion or grant reviewers scan, so the impact story must be self-contained rather than asking the reader to follow a link.

## Related Skills

- [[news-search]]: editorial coverage of FORTIS work (press, government PDFs, ecosystem, deep-research-tool output). Pairs with this skill for combined external-impact evidence.
- [[bibref-verify]]: audits an existing `.bib` for hallucinated entries before paper submission. Not related to citation-affiliation audit, but adjacent in bibliometric workflows.
