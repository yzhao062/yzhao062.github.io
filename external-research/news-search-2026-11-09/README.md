# Incremental Coverage Search, November 9, 2026

This archive backs the 2026-11-09 round of `news-coverage-audit.md`. The round searched items dated from 2026-10-15, nineteen days after the 2026-10-21 full search, and verified the 35 Tier 2 records that round had held.

## Method

Discovery ran 11 Agy lanes and 3 Claude Workflow lanes. Five covered the agent-auditing Standing Lane (web, academic citers, standards) and the works added since the last round (FrontierPhysics, the paper on depth in terminal tasks, PersonaCUABench and agentpile). The others covered government and foundation-model documents, patents, English press, non-English coverage and peer-reviewed methods use. The lanes logged 873 queries and returned 113 records after deduplication by document identity; with the held records, the round handled 148.

Fifteen Agy units verified the 110 records that were neither already recorded nor topic-only. Kept verdicts were re-checked against the record by URL, arXiv ID, DOI, PMC ID and ref-insensitive GitHub path, and new Ledger 7 titles were taken from Crossref. Eight Claude agents then tried to refute the 16 highest-value keeps: the Ledger 6 and Ledger 2 candidates and the BlackRock preprint. Twelve held, and four Ledger 2 candidates moved to Ledger 3 because their pages are machine-written or company posts. Review of the staged round moved a fifth, the AccuKnox post, to Ledger 3 as vendor product content, and found one Ledger 7 article already held under its PMC page.

## Findings Worth Surfacing

| Source | Verified Evidence | Ledger |
|---|---|---|
| Ten external papers on the agent-auditing line | Related-work discussion of Auditable Agents (five papers), the FORTIS over-privilege benchmark (two), WeClawArena, CatchBench and AEGIS, by authors outside the lab | Ledger 6 rows A64 to A73 |
| [BlackRock authors, arXiv:2512.05559](https://arxiv.org/abs/2512.05559) | A data-quality control system for regulated financial environments uses PyOD as its primary outlier-detection engine and benchmarks on ADBench datasets (PDF p.6 and p.9) | Ledger 3 row 854 |
| Lantern Pharma SEC 8-K exhibits and the Boltz BoltzMol-1 report | Company documents that report results on Therapeutics Data Commons tasks | Ledger 3 rows 855 to 857 |
| Peer-reviewed methods use | 24 articles run TDC, PyOD and its detectors, or ADBench in their methods | Ledger 7 rows S256 to S279 |

The checked government, standards and foundation-model sources yielded no new direct mention for the ledgers. Thirty checked records discuss related topics without naming a work. The patent searches found no new qualifying patent in the window, so the distinct-invention count remains 144.

## Corrections Made in This Round

Ledger 2 row 81, an AI Weekly brief from an earlier round, moved to Ledger 3 row 863, because aiweekly.co drafts its coverage with AI-assisted workflows. Ledger 3 row 551 counts four pages one per link, and its three extra items now enter the Ledger 3 total. The three agentpile package-index pages are first-party under the package-index rule and are not counted.

## Limits

The 718 Tier 3 and 74 Tier 5 records held on 2026-10-21 remain unverified.

## Files

- `candidates.jsonl`: all 148 records with status, verdict fields, ledger row or cluster, and match source for already-recorded items.
- `queries.jsonl`: every logged discovery query with its lane and executor.
- `manifest.json`: counts and run status.

Workers did not commit or push.
