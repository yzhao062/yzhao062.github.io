# Full Coverage Search, November 17, 2026

This archive backs the 2026-11-17 round of `news-coverage-audit.md`. It was a full search weighted toward the agent-auditing line and its related lines, and it was the first round under the High-Value Evidence Only rule in `skills/news-search/SKILL.md`: blog posts, tutorials, aggregator pages, personal repositories, curated lists, forum posts and platform listings were neither searched for nor counted. The plan, including the changes made while the round ran, is in [PLAN.md](PLAN.md).

## Method

Discovery ran 45 Agy lanes and 9 Claude Workflow agents. Ten lanes covered the auditing line and the nine related-line works; the Claude agents used methods the lanes do not use (citation-graph triangulation, reverse search from neighbouring agent-security systems, code full-text search, patent and standards full text, and a check of works with zero or one recorded citer). The lanes logged 5,737 queries and returned 1,058 records over 873 documents; 192 were already on file. Three Agy lanes were stopped early when the Gemini five-hour quota ran low, and the books-and-courses lane was redone by a Claude agent.

All verification ran on Claude Workflow agents, in four waves over 726 documents: the auditing line and every Tier 0 or Tier 1 claim first, then general Tier 2 and high-value Ledger 3 items, then patents with a family check, then general academic claims. Two refute passes challenged 108 high-value keeps (95 confirmed, 12 reclassified, 1 unverifiable), including a random sample of 20 new patents (19 confirmed, 1 a family member already on file). Google Patents refused automated access, so patent families were checked through SureChEMBL priority data and a base-number match against the audit rather than the Also Published As list. Kept verdicts were re-checked against the record by document identity, and new patents were cross-checked for shared families.

## Findings Worth Surfacing

| Source | Verified Evidence | Ledger |
|---|---|---|
| [NIST SP 2400-102e2026, initial public draft](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.2400-102e2026.ipd.pdf) | *Adversarial Machine Learning: A Taxonomy and Terminology* repeats the TrustLLM sentence (PDF p.71, reference [211]); public comments are open until 2026-12-18 | Ledger 1 row 36 |
| 33 external papers on the agent-auditing and related lines | Body discussion or comparison of CHI-Bench, Auditable Agents, Topology Matters (including an EMNLP 2026 main-conference paper), agent-audit, MemoHarness, No Attacker Needed, AEGIS, GRADE and others | Ledger 6 rows A74 onward |
| [US 2026/0238651 A1](https://www.surechembl.org/api/patent/get_patent/US-20260238651-A1) | A patent application on constraint enforcement for agentic LLM systems discusses AEGIS as prior art in seven passages, the first patent document on file that cites the auditing line. Its applicant is the sole author of Ledger 6 row A12, so it is not an independent second signal | Ledger 3 |
| Enterprise and teaching use of the auditing line | An enterprise AI safety handbook (Orcaworks) recommends the AEGIS paper; a University of Washington Tacoma cybersecurity course runs agent-audit in a classroom activity | Ledger 3 |
| [CFO Dive](https://www.cfodive.com/news/why-ai-agents-go-rogue-means-cfos-tech-cybersecurity/833441/) and Korean trade press | CFO Dive quotes Yue Zhao on when to deploy AI agents; ETNews and Digital Chosun report drug-discovery models evaluated on TDC | Ledger 2 |
| Patents | 89 new Chinese anomaly-detection inventions, so the distinct-invention count moves from 144 to 233; four US and two WIPO patents are held from the count until a family check | Ledger 3 |
| Peer-reviewed methods use | 33 articles run PyOD, PyGOD, ADBench, NLP-ADBench or TDC in their methods | Ledger 7 |

## Corrections and Limits

Of 18 Phase A Tier 0 claims, one held. The rest were CVE mirrors folded into Ledger 1 row 13, documents already on file under other addresses, research papers by foundation-model company staff, or misclassified. A Ministry of Health, Labour and Welfare report that uses TDC was moved from Ledger 1b to Ledger 3, because a University of Tokyo grantee wrote it and the ministry system only hosts it. The Project Syndicate commentary by Angela Huyue Zhang and Yue Zhao, with its six republications, is one Ledger 4 row: the PI wrote it.

The claim-level patent figure stays at twenty-seven: verification flagged 20 of the new inventions as naming a tool in a numbered claim, and a claims-text recount has not yet confirmed them. Twenty auditing-line topic-only records were logged without verification, ten records stayed blocked, and 66 verified records were long tail under the new rule, six of them set on review of the generated rows (a conference speaker bio, four general articles that name a work once in passing, and an AI Radar rewrite of the USC feature); with one long-tail record that was never verified, `candidates.jsonl` marks 67 records `long_tail`. A Mongolian developer blog (devx.mn) rewrote the USC Viterbi AEGIS feature and attributes a direct quotation to Yue Zhao; one verifier could not find that quotation in the USC feature, and the round did not re-check it. The page is not counted.

## Files

- `PLAN.md`: the round plan and the decisions made while it ran.
- `candidates.jsonl`: every Phase A record with its verification status, verdict fields, ledger row and the coordinator's notes.
- `queries.jsonl`: every logged Agy discovery query with its lane.
- `manifest.json`: counts and run status.

Workers did not commit or push.
