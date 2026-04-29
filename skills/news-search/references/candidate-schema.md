# Phase A Candidate Schema

Phase A of `news-search` writes one JSON-Lines record per candidate to `news-search-candidates.jsonl` at the project root. Phase B reads and classifies each record. The two phases share this schema.

## Record Fields

| Field | Type | Set in | Notes |
|---|---|---|---|
| `url` | string | A | Canonical URL of the page or PDF that surfaced the work. |
| `title` | string | A | Page title or PDF title. Empty string if unavailable. |
| `snippet` | string | A | Short text snippet from search results or page intro. <= 500 chars. |
| `dimension` | string | A | Which Dimension produced the candidate (`D1` through `D10`). |
| `surfacing_query` | string | A | The exact search query that produced the URL. Lets us re-run the same query later. |
| `outlet_class` | string | A | Class from `references/domain-registry.md` (e.g., `gov-pdf`, `eu-research-project`, `patent`, `china-tech-media`, `security-blog`, `ai-aggregator`, `tier1-tech-press`, `unknown`). |
| `fetched_at` | string (ISO 8601) | A | Timestamp of search/fetch. Empty if not fetched in Phase A. |
| `flags` | string[] | B | Detection flags set in Phase B. Empty in Phase A. See `references/disclaimer-patterns.md`. |
| `direct_mention` | object | B | `{names: string[], rule: int}`. Which name (work/person/lab/co-author/URL) matched the citation verification rule, and which rule clause (1-6). Empty in Phase A. |
| `tier` | string | B | Tier 0 through Tier 5, or `topic-validation`, or `dropped`. Empty in Phase A. |
| `registry_status` | string | B | `existing` if the candidate's registered domain is already listed in `references/domain-registry.md`, `new` if Phase B's harvest step appended it this round. Empty in Phase A, on dropped candidates, and on topic-validation candidates. Drives the Registry harvest summary in the audit output. |
| `notes` | string | B | One-line note for the audit row. Empty in Phase A. |

## Lifecycle

1. Phase A produces candidates with all `A` fields filled and all `B` fields empty or null.
2. Phase B reads each record, fetches the page, and applies the four-step Phase B flow in `SKILL.md`: direct-mention / topic-validation routing, disclaimer / aggregator detection, tier assignment, and registry harvest status. The `B` fields are filled in the course of those four steps.
3. Phase B writes direct-coverage rows (`tier` is Tier 0 through Tier 5) to the coverage ledgers in `news-coverage-audit.md`, and topic-only rows (`tier == 'topic-validation'`) to the Topic Validation appendix in the same file. Coverage ledgers and the appendix are distinct outputs; do not merge them.
4. Phase B keeps dropped rows (`tier == 'dropped'`) in `news-search-candidates.jsonl` with their `flags[]` and `notes` so drop decisions remain auditable, never silently discarded.
5. The full candidates file stays at the project root through the audit. Delete or archive after the audit is committed.

## Why Two Phases

- **Phase A is cheap and parallelizable.** Discovery queries are independent and re-runnable. Caching the candidate list lets a re-run skip the slow step.
- **Phase B is slow and judgment-heavy.** Page fetches, disclaimer scans, and direct-mention checks are sequential and benefit from being done once.
- **The candidate list is reviewable before classification.** A user or a second reviewer can scan the candidate set and catch wrong query routing or wrong outlet-class tagging before Phase B turns the candidates into ledger rows that later need restructuring.
- **Drops are auditable.** Every dropped candidate keeps its `flags[]` and `tier=dropped` so the audit shows what was rejected and why, not only what was kept.

## File Location and Git Handling

- Candidates file: `news-search-candidates.jsonl` at the project root.
- Add `news-search-candidates.jsonl` to `.git/info/exclude` (local, untracked) before the first run so `git add -A` does not stage it. The audit-output file `news-coverage-audit.md` is the committable deliverable; the candidates file is scratch.
