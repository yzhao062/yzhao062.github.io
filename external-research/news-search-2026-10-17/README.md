# Full Coverage Search and Audit Cleanup, October 17, 2026

This archive backs the 2026-10-17 round of `news-coverage-audit.md`. Its readers are the site owner and whoever maintains the audit next. The round ran a full external search over the publication and tool inventory. It also cleaned up the audit itself, whose ledgers had drifted from their own inclusion rules.

## Method

Discovery ran 41 Agy lanes through `/prun`, then 7 Agy follow-up lanes and 3 Claude Workflow lanes; the 4,126 logged queries span all 48 Agy lanes. The merged Phase A set held 709 records. An identity index over the audit, the round notes and the earlier archives removed known items, and first-party status was decided by authorship. That left 653 candidates, of which 62 topic-only or verified-negative records were logged without re-verification.

Phase B ran 43 Agy verification units. Each unit fetched every source itself, read PDFs as text and checked authors against the inventory co-author list. The units returned 635 verdicts with none missing: the 591 candidates left after the logged-only records, plus 44 orphan and promotion records (`O` and `P` IDs). A cross-vendor pass then tried to refute every high-tier keep (Ledgers 1, 1b, 2, 5, 6 and 7). Twelve Claude agents re-fetched 117 claims and upheld 26, corrected 57, refuted 33 and could not verify 1. Only upheld or corrected rows entered the audit.

Two process faults are recorded. The coordinator stopped the Claude discovery workflow after reading another model's weekly meter as this session's quota; the seven unfinished scopes were re-run as the Agy follow-up lanes. The lane dispatcher's preflight calls GNU `timeout`, which macOS lacks, so the first launch exited 127; the lanes were relaunched with `NEWS_SEARCH_AGY_PREFLIGHT=off`. The dispatcher now falls back to `gtimeout` or a shell watchdog with the same exit codes.

## Findings Worth Surfacing

| Source | Verified Evidence | Scope |
|---|---|---|
| [SDAIA](https://sdaia.gov.sa/en/MediaCenter/KnowledgeCenter/AINewsletter/AINewsletter03Oct2024.pdf) | Weekly newsletter *AI in a Week*, issue 155 (Oct 2024), p.11, reports TrustLLM | Ledger 1 row 29; was Ledger 2 row 44 |
| [Deloitte Germany](https://www.deloitte.com/content/dam/assets-zone2/de/de/docs/services/consulting/2025/Deloitte-Compliance-AIxAML.pdf) | AIxAML client brochure credits a figure to ADBench (footnote 1, p.3) | Ledger 3 row 66cb; a figure credit in a brochure, not a report |
| Lantern Pharma and Recursion SEC filings | A 10-K, an 8-K exhibit and a 10-Q report results on TDC benchmarks | Ledger 3 rows 581 to 583 |
| Org-owned code | Microsoft, IBM, Oracle, LinkedIn, Alibaba, AWS samples and OpenAI evals call or pin PyOD or ship TrustLLM data | Ledger 3 code rows |
| [CSET](https://cset.georgetown.edu/) reference guide | "Operationalizing AI Guidance" cites the model-extraction survey | Ledger 1 row 32; found as an orphan in round prose |
| Agent-auditing citers | 13 external papers cite or benchmark Auditable Agents, MemoHarness, AEGIS, Agent Audit, CatchBench, SkillCenter, No Attacker Needed or Implicit Execution Tracing | Ledger 6 |
| Peer-reviewed methods use | 43 articles run TDC (24), PyOD and its detectors (16), or SUOD, ADBench and TAGFN in their methods | Ledger 7 |

Ten patents are new distinct inventions (8 China, 2 US), so the patent total moves from 106 to 116. Thirteen new patent rows were family-checked against the rows on file through each Google Patents "Also Published As" list. IBM US11979421B2 is the grant of row 270, and CrowdStrike US12499217B2 shares a family with row 66k (EP4339817A1); both merged into the older rows. Row 617 cites the diffusion-models survey, which is outside the anomaly-detection basis. The base is 106, one below the published 107. The cleanup found that row 182 (US20250365294A1) is a continuation of row 272. A recount of the Google Patents claims text for all 121 patent rows found 21 inventions that name a tool in numbered claims, where eleven had been published. Two of them are new this round, Heimdal Security (US20260172434A1) and China Three Gorges University (CN120780693A), both reciting ECOD.

## Corrections and Limits

The refute pass moved several claims down. The OECD.AI catalogue record for TrustLLM was created by the catalogue's own automation, so it is a Ledger 3 platform listing. The quoted OECD.AI entry for anomaly-detection-resources does not exist on the page. Committee and workshop organizer roles are not awards. The two Spanish Wikipedia pages are translations of English pages already counted. Hysen Labs states that every analysis is drafted by an AI pipeline, so its pages are catalog entries. That reverses the 2026-10-14 decision, and the older Hysen row moved to Ledger 3 with the three new ones. Fourteen Ledger 2 candidates became Ledger 3 rows (community posts, AI-assisted blogs, vendor briefs).

The ledger cleanup moved 51 misfiled rows between ledgers, and four more changed ledger later (`cleanup-moves.json`). After review, the RAND report joined CSET in Ledger 1 as policy citations, and the LLNL feature moved to Ledger 4 because LLNL is a co-author institution. It sent 17 rows out of the tables (`cleanup-handoffs.json`); 10 went to the citation audit as reference-list citations. Smaller fixes merged the two CDAO toolkit rows and deleted an Amazon Science author page that belongs to a different Yue Zhao. Four CN A/B publication pairs and the Ledger 6 abs/PDF duplicates were removed. Seventeen promotions recorded in round prose had no ledger row; they were re-verified here as the `O` and `P` candidates. The FALAT disambiguation entry is reversed: arXiv:2606.00765 cites the lab's work.

An Agy unit recovered the missing URLs of four Ledger 2 rows. Its NTT Technical Review address pointed to a different article that does not mention TrustLLM; row 36ao now cites the November 2025 article whose PDF names TrustLLM on p.4. Review found three Ledger 5 award rows, moved in from Ledger 2, that duplicated existing rows, and one podcast episode recorded under two storefront URLs; both were merged. Held items are in `candidates.jsonl`: one unverifiable Preprints.org paper and 11 paywalled or blocked sources.

Seven cluster rows, 661 to 667, count the long-tail Ledger 3 items: aggregator pages, platform listings, tutorials, individual code, curated lists, videos and forum threads. Each cluster row shows five examples; every item with its quote and locator is in `candidates.jsonl` under its `cluster` field.

## Files and Reproduction

- `candidates.jsonl`: all 697 records with Phase B status, tier, quote, locator, refute verdict and reason, and the ledger row or cluster each entered.
- `queries.jsonl`: the Agy discovery queries.
- `citation-handoff.jsonl`: 73 ordinary academic citations for `/citation-audit`.
- `row-map.json`: candidate ID to ledger row.
- `cleanup-moves.json` and `cleanup-handoffs.json`: the cleanup's row moves and removals.
- `manifest.json`: counts and run status.

The citation-affiliation audit was re-rendered the same day with canonical-organization dedup and a self and co-author screen. OpenAlex spent its daily credit budget resolving identifiers, so that file is Dimensions-only until OpenAlex is re-run after its 00:00 UTC reset. Workers did not commit or push.
