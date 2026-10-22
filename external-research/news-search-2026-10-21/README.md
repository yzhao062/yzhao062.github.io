# Full Coverage Search, October 21, 2026

This archive backs the 2026-10-21 round of `news-coverage-audit.md`. It ran four days after the 2026-10-17 round, so its value is what that round missed: new pages, a second search engine on the same scopes, and deeper sources.

## Method

Discovery ran 43 Agy lanes, 14 Codex lanes and 10 Claude Workflow lanes over the full publication and tool inventory. Codex and Claude lanes repeated the highest-value Agy scopes (government PDFs, foundation-model documents, the agent-auditing line, patents, journal methods use) on different search engines. The lanes logged about 11,000 queries and produced 1,908 records after deduplication by document identity; the re-run of one truncated lane added 18, for 1,926 in all. The identity index matched 364 records to documents already on file and 43 to first-party pages, and verification found 5 and 27 more. Review of the integrated rows then matched 46 more kept records to documents on file and 24 to other records of this round (GitHub URLs that differ only in ref, DOI and PMC copies), for 415 already-recorded and 43 duplicate records in all. The 39 topic-only records were logged apart from the ledgers.

Verification was time-boxed at 45 minutes. Claude units checked the 152 Tier 0 and Tier 1 claims, Codex units the 55 patents (with a Google Patents family check) and 25 other high-value items, and Agy units the rest. Each unit fetched the source, read PDFs as text, and compared the citing author block with the publication author lists. Kept verdicts were then re-checked against the record by URL variant, DOI and PMC ID, because the units never saw the ledgers. 652 candidates received a verdict; 829 are held as `unverified` in `candidates.jsonl` for the next round.

## Findings Worth Surfacing

| Source | Verified Evidence | Ledger |
|---|---|---|
| [Singapore GovTech AI Playbooks](https://playbooks.aip.gov.sg/mlops-playbook/Chapter_5_B%3A_Model_Development_Data_Processing/) | The MLOps Playbook's data-processing chapter lists pyod among outlier-detection tools | Ledger 1 row 33 |
| [Buenos Aires City Council of the Magistracy](https://consejo.jusbaires.gob.ar/institucional/documentacion/compras-y-contrataciones/download?id=54A177F8EEA57EF5150FA923329FFF2E) | Procurement resolution RESO SAGYP 432/25, PDF p.60: AI-agent security tests must validate training data with anomaly analysis using PyOD | Ledger 1 row 35 |
| Patents | 28 new anomaly-detection inventions (US 14, China 11, Korea 2, Türkiye 1), six naming a tool in a numbered claim; nine more were family members of inventions on file | Ledger 3 |
| Agent-auditing citers | Five external papers, including SkillVetBench (arXiv:2606.00925) on agent-audit | Ledger 6 rows A59 to A63 |
| Peer-reviewed methods use | 99 articles run TDC, PyOD and its detectors, or ADBench in their methods | Ledger 7 |

No government, standards or foundation-model document names the agent-auditing line yet. The closest new item is a National Research Council Canada repository whose AI-safety digest links agent-audit (Ledger 3 cluster).

## Corrections and Limits

Nine government and foundation-model hits were documents the ledgers already hold under other addresses (NIST, TxGemma, Tx-LLM, the TEC standard, the FLI Summer 2025 index, OpenAI evals). Four national cybersecurity agency pages that republish CVE-2026-15529 fold into Ledger 1 row 13. Research papers by Amazon and Microsoft staff are not foundation-model company documents; they went to Ledger 7 or the citation audit. A public comment on regulations.gov belongs to its author (a Medicare contractor), so it is Ledger 3. Patents that cite TDC, the diffusion-models survey or TrustLLM are Ledger 3 rows outside the anomaly-detection patent count.

The 829 unverified records are mostly long-tail Ledger 3 material: Chinese tutorials and posts staged by the CJK lane, and two batches of verification units that hit the time limit or the Agy Claude and GPT quota. They are not counted.

## Files

- `candidates.jsonl`: all 1,926 records with status, verdict fields, ledger row or cluster, and match source for already-recorded items.
- `queries.jsonl`: every logged discovery query with its lane and executor.
- `manifest.json`: counts and run status.

The citation-affiliation audit was re-run the same day on OpenAlex and Dimensions, both complete. Workers did not commit or push.
