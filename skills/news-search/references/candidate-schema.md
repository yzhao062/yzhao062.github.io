# Phase A Candidate Schema

Phase A of `news-search` writes one JSON-Lines record per candidate to `news-search-candidates.jsonl` at the project root. Phase B reads and classifies each record. The two phases share this schema.

## Record Fields

### Core fields (Phase A and Phase B)

| Field | Type | Set in | Notes |
|---|---|---|---|
| `url` | string | A | Canonical URL of the page or PDF that surfaced the work. |
| `title` | string | A | Page title or PDF title. Empty string if unavailable. |
| `snippet` | string | A | Short text snippet from search results or page intro. <= 500 chars. |
| `dimension` | string | A | Which Dimension produced the candidate (`D1` through `D10`, plus extensions like `D2-careers`, `D7-code`, `D7-talks`, `D8`). |
| `surfacing_query` | string | A | The exact search query that produced the URL. Lets us re-run the same query later. |
| `outlet_class` | string | A | Class from `references/domain-registry.md` (e.g., `gov-pdf`, `eu-research-project`, `patent`, `china-tech-media`, `security-blog`, `ai-aggregator`, `tier1-tech-press`, plus extensions like `foundation-model`, `big-tech-careers`, `finance-careers`, `pharma-careers`, `security-careers`, `gov-careers`, `industrial-careers`, `retail-asia-careers`, `job-aggregator`, `github-dependents`, `github-aggregate`, `course-training`, `book`, `university`, `unknown`). |
| `fetched_at` | string (ISO 8601) | A | Timestamp of search/fetch. Empty if not fetched in Phase A. |
| `work` | string | A | Free-text label of the FORTIS work the candidate is about (e.g., `PyOD`, `TrustLLM`, `OpenAI Quantitative Threat Forecasting Analyst`, `verified-negative D8 PDF scan`). |
| `source` | string | A | Free-text label of the publishing entity / outlet / repo (e.g., `OpenAI`, `Wells Fargo Principal Platform Engineer R-512394`, `Apache Software Foundation / apache/beam`). |
| `flags` | string[] | B | Detection flags set in Phase B. Empty in Phase A. See `references/disclaimer-patterns.md`. |
| `direct_mention` | object | B | `{names: string[], rule: int}`. Which name (work/person/lab/co-author/URL) matched the citation verification rule, and which rule clause (1-6). Empty in Phase A. |
| `tier_guess` | string | B | Provisional tier from Phase A or Phase B before audit promotion. Values: `T0` / `T0(b)` / `T1` / `T2` / `T3` / `T4` / `T5`, or `topic-validation`, `dropped`, `dropped_name_collision`, `paywall_or_blocked`, `phase_b_priority`, `phase_b_candidate`, `phase_b_blocked`, `verified-negative`, `first_party`, `already_tracked`, `out_of_scope_news`, `audit-enhancement`, `duplicate_existing`, `T0-quantitative`. The legacy `tier` field is an alias kept for older entries. |
| `status` | string | A or B | Lifecycle marker (see "Status Lifecycle" below). |
| `registry_status` | string | B | `existing` if the candidate's registered domain is already listed in `references/domain-registry.md`, `new` if Phase B's harvest step appended it this round. Empty in Phase A, on dropped candidates, and on topic-validation candidates. Drives the Registry harvest summary in the audit output. |
| `ledger` | string | B | After promotion, the audit ledger and row ID where the candidate now lives (e.g., `Ledger 1 #8g`, `Ledger 3 #66cy`). Empty until promotion. |
| `notes` | string | B | One-line note for the audit row. Empty in Phase A. |

### Evidence fields (used when the candidate is JD / careers / volatile content)

| Field | Type | When | Notes |
|---|---|---|---|
| `quote` | string | B | Single verbatim quote from the source naming the work, captured at discovery time. Use when the page is volatile and may go stale (careers pages, news articles). |
| `quote_responsibilities` / `quote_qualifications` / `quote_<section>` | string | B | Multiple-quote variant for postings that name the tool in more than one section. Each suffix names the source section. |
| `section` | string | B | Where the quote appears in the source (e.g., `Qualifications`, `Responsibilities`, `Tech Stack`, `Footnote 119, p.25`). |
| `mirrors` | string[] | B | List of mirror URLs (Greenhouse / Lever / Ashby / DFJ Growth / Glassdoor / LinkedIn / Indeed / Hiring Our Heroes for JDs; aggregator domains for press). Captured when the canonical URL is volatile or behind a Cloudflare / SSR shell. |
| `comp_band` / `locations` / `clearance` | string | B | Optional careers-page metadata. |
| `import_path` / `import_line` / `stars` / `primary_purpose` | string / int | B | Optional GitHub-code-search dependent metadata. |
| `page` | string | B | Optional PDF page reference for `D8` records. |
| `evidence` | string | B | Optional free-text evidence summary (used by older entries; new entries should prefer `quote` + `section`). |
| `sample_size` / `hits` / `count_repos` / `count_packages` / `linkedin_pyod_us_count` | int | B | Optional aggregate counters used by sweep-summary records and the GitHub-dependents aggregate row. |
| `disambiguation` | string | B | Optional explicit note when the candidate could collide with a same-name different project. Cross-reference `references/disambiguation-registry.md`. |
| `speaker_affil` | string | B | Optional industry / institution affiliation when the candidate is a podcast / talk / video. |

## Status Lifecycle

The `status` field tracks where each record sits in the Phase A → Phase B → ledger pipeline. Phase B uses it to decide what action to take.

| Status | Set by | Phase B action |
|---|---|---|
| `candidate` | A or B | New, not yet processed by Phase B promotion logic. Phase B may promote, demote, or hold depending on tier and verification. |
| `candidate-promote` | B | Phase B has verified the citation and assigned a tier; the row is ready to be written to a ledger in the next audit-update step. The audit-update step (separate from Phase B) does the actual ledger write and then moves the status to `counted`. |
| `counted` | B (post-promotion) | The row has been written to a ledger and the corresponding `ledger` field is set (e.g., `Ledger 3 #66cy`). Subsequent Phase B passes leave it alone. |
| `dropped` | B | The candidate failed direct mention or first-party / already-tracked / disambiguation drop. Stays in the candidate file with a drop reason in `notes`. |
| `dropped_name_collision` | B | A specific drop subtype: the match is on a same-name different person or project. Cross-reference `references/disambiguation-registry.md`. |
| `verified-negative` | B | A D8 PDF or sweep target that was directly checked (e.g., text-extracted via `pdf_term_scan.py`) and confirmed to not name FORTIS work. Kept in the file as cumulative negative evidence so future rounds skip the same target. |
| `paywall_or_blocked` | B | The page was 403 / Cloudflare / SSR shell at fetch time and could not be fully verified. Held for a manual fetch from a logged-in browser session. |

The legacy `tier` field is kept as an alias for `tier_guess` on older entries; new entries use `tier_guess` plus `status`.

## Lifecycle

1. Phase A produces candidates with all `A` fields filled and all `B` fields empty or null. Default `status` is `candidate`.
2. Phase B reads each record, fetches the page, and applies the five-step Phase B flow in `SKILL.md`: pre-tier filter (first-party / already-tracked / disambiguation drops), direct-mention / topic-validation routing, disclaimer / aggregator detection, tier assignment, and registry harvest status. The `B` fields are filled in the course of those five steps. Tier 0 / Tier 1 candidates that rest only on a WebSearch snippet must have the source re-fetched before promotion (run `pdf_term_scan.py` for PDFs, real-UA HTTP for web pages); see the "Snippet alone is not verified evidence" rule in `search-strategy.md`.
3. Phase B sets `status: candidate-promote` for rows it intends to send to a ledger. The audit-update step writes the row to the ledger, fills `ledger`, and flips status to `counted`.
4. Phase B writes direct-coverage rows (`tier_guess` is Tier 0 through Tier 5) to the coverage ledgers in `news-coverage-audit.md`, and topic-only rows (`tier_guess == 'topic-validation'`) to the Topic Validation appendix in the same file. Coverage ledgers and the appendix are distinct outputs; do not merge them.
5. Phase B keeps dropped rows (`status` in `dropped`, `dropped_name_collision`, `paywall_or_blocked`, or `verified-negative`) in `news-search-candidates.jsonl` with their `flags[]` and `notes` so drop decisions remain auditable, never silently discarded.
6. The full candidates file stays at the project root through the audit. Delete or archive after the audit is committed.

## Why Two Phases

- **Phase A is cheap and parallelizable.** Discovery queries are independent and re-runnable. Caching the candidate list lets a re-run skip the slow step.
- **Phase B is slow and judgment-heavy.** Page fetches, disclaimer scans, and direct-mention checks are sequential and benefit from being done once.
- **The candidate list is reviewable before classification.** A user or a second reviewer can scan the candidate set and catch wrong query routing or wrong outlet-class tagging before Phase B turns the candidates into ledger rows that later need restructuring.
- **Drops are auditable.** Every dropped candidate keeps its `flags[]` and `status` in `dropped` / `dropped_name_collision` / `verified-negative` / `paywall_or_blocked` (with `tier_guess` carrying the same drop reason on legacy entries) so the audit shows what was rejected and why, not only what was kept.

## File Location and Git Handling

- Candidates file: `news-search-candidates.jsonl` at the project root.
- Add `news-search-candidates.jsonl` to `.git/info/exclude` (local, untracked) before the first run so `git add -A` does not stage it. The audit-output file `news-coverage-audit.md` is the committable deliverable; the candidates file is scratch.
