# News & Media Coverage Audit — Yue Zhao / FORTIS Lab

*Last 5 runs (full change-log in `## Changes from Previous Audit` and in git history):*
*2026-07-19 (Claude coordinator + 10 Codex lanes via /prun): 269 candidate records to 258 unique URLs. Broke a three-round drought: net new **+5 Tier 0** (UK gov.uk production record, Saudi SDAIA, US DOE/ORNL, G7/OECD Salesforce, NIST NVD CVE) and **+5 Tier 1** (FLI Summer 2026, NTT Technical Review, 3 Nature-family papers), all direct-fetch verified. +6 Tier 2 including first editorial coverage of the auditing line (The Agent Times, WIDTH) and same-week pickup of the four newest papers. Resolved Ledger 2 #22 (SitePoint) as REMOVED, net -1. A mid-round gap (Implicit Execution Tracing never searched) was closed by a tenth lane, which also verified 7 third-party citations of Auditable Agents, 4 of them new. Details in "## 2026-07-19 Pass".*
*2026-06-14 (Codex independent broad parallel search): 9 lanes total: 5 structured lanes plus 4 broad follow-up lanes after the user asked to search less narrowly. Net new Tier 0/1 direct coverage verified: 0. Added 46 exact-URL candidate, drop, duplicate, and negative records to `news-search-candidates.jsonl`; strongest new items are low-tier or academic-downstream signals, not editorial ledger promotions. Main action items: Phase B review of new ADBench/Aegis/TDC academic-downstream rows, PyOD ecosystem rows, three China patent candidates, and a SitePoint recheck because the live page did not verify the prior `agent-audit` direct-coverage claim. Details in "## 2026-06-14 Codex Independent Broad Search".*
*2026-06-13 (Claude /workflows two-phase refresh): 84 Phase-A candidates to 67 Phase-B keeps; net new editorial ~0 (the sweep re-surfaced already-tracked ecosystem items: Grokipedia is Ledger 4 #70; Ericsson patent, DataCamp/Udemy courses, and the Manning/O'Reilly book already in Ledger 3). Genuinely new: Auditable Agents (arXiv:2604.05485) has 4 third-party downstream citations within weeks (bibliometric; flag for /citation-audit). Stanford HAI 2026 AI Index checked (Yue): does not name TrustLLM (negative). Details in "## 2026-06-13 Refresh".*
*2026-05-28 (Claude independent 8-lane rerun): net +0 counted ledger rows (Ledger 1/2/3/4/5 all +0); 4 marginal Phase-B keeps folded into existing rows, plus Negative Results and Topic Validation additions.*
*2026-05-28 (Codex /news-search + /citation-audit sweep): net +4 Ledger 3 (0 Ledger 1/2/4/5); citation-affiliation hook refreshed to 39 Tier 0 + 209 Tier 1 rows.*
*2026-05-20 (Codex /news-search rerun): net +4 Ledger 3 (0 Ledger 1/2/4/5).*
*All 8 core dimensions plus D9/D10 follow-up checks complete across the current inventory. Codex 2026-06-14 local parse: 112 publications + 19 tools; the 2026-05-28 citation-audit integration keeps its own non-survey subset basis.*
*Citation verification applied: every item names or cites the work, person, lab, or co-author.*

---

## 2026-07-19 Pass (Claude coordinator + 10 Codex lanes via `/prun`)

**Method.** Ten parallel Codex workers (`codex exec`, separate quota) ran Phase A; the Claude session
only coordinated, merged, and wrote. 269 candidate records to 258 unique URLs, all valid JSONL, in
`news-search-candidates.jsonl`. Nine lanes covered D1-D8 plus the open 2026-06-14 action items; a
tenth follow-up lane was added after a coverage gap was found mid-round (see "Gap found and closed").

**This round broke a three-round drought.** The 2026-05-28, 2026-06-13, and 2026-06-14 passes each
netted roughly zero new Tier 0/1 editorial coverage. This pass verified **5 Tier 0 and 5 Tier 1**
items, all by direct fetch (PDF text extraction via `pdf_term_scan.py`, or real-UA HTML), never from
a search snippet.

### Tier 0: Government, policy, and standards (Ledger 1, +5)

| # | Work cited | Source | Evidence |
|---|---|---|---|
| T0-a | PyOD | **UK Government**, gov.uk Algorithmic Transparency Record, London Borough of Sutton "Access Assure" | PyOD KNN documentation link in Tier 2 Model Specification, section 4.2.6. A UK government **production deployment** record, not a literature citation. |
| T0-b | PyOD | **Saudi SDAIA**, Deepfakes Guidelines v1 (Sept 2024) | `pdf_term_scan.py` confirmed PyOD on PDF p.10; canonical 33-page PDF plus OECD.AI mirror both fetched. |
| T0-c | TrustLLM | **US DOE / ORNL**, technical report ORNL/TM-2025/3935, "Scalable Workflow for Evaluating Trustworthiness of Large Language Models" (OSTI 3002371) | 11 literal TrustLLM occurrences in the 23-page PDF (pp. 5, 8, 9, 15, 20), including substantive workflow discussion and the bibliography. `pdf_term_scan.py` reports 12 term matches because the p.20 bibliography entry also matches the loaded full-paper-title term; corrected after independent recount, Codex review 2026-07-19. |
| T0-d | TrustLLM | **G7 Hiroshima AI Process / OECD**, Salesforce Transparency Report | TrustLLM confirmed on p.4 of the eight-page PDF. Caveat recorded: OECD hosts but explicitly leaves report responsibility with Salesforce. |
| T0-e | PyOD | **NIST NVD**, CVE-2026-15529 | Names `yzhao062` PyOD, affected versions 3.5.0/3.5.1/3.5.2, and links the canonical repo. **Adverse coverage** (a security advisory, not an endorsement). See "Security finding" below. |

### Tier 1 (Ledger 2, +5)

| # | Work cited | Source | Evidence |
|---|---|---|---|
| T1-a | TrustLLM | **FLI AI Safety Index, Summer 2026** (new edition) | TrustLLM on pp. 6, 10, 13, 45, and also pp. 25 and 42 on independent recount; p.25 gives the full title and arXiv:2401.05561 and p.45 defines and scores the benchmark. Distinct from the previously tracked editions. |
| T1-b | TrustLLM | **NTT Technical Review** (Japan) | TrustLLM on p.4; canonical benchmark repo is reference [4] on p.5. |
| T1-c | PyOD | **Nature Scientific Reports** s41598-026-45091-2 | Methods names eight PyOD algorithms; references cite the PyOD JMLR paper. |
| T1-d | PyOD | **Nature Scientific Reports** s41598-025-20514-8 | Methods states three outlier algorithms implemented with PyOD; cites Zhao et al. |
| T1-e | ADBench | **Nature Communications** s41467-025-56173-6 | Data Availability links the ADBench repository for benchmark anomaly datasets. |

### Tier 2: the four newest papers were picked up within days (Ledger 2, +6)

The papers added to the record on 2026-07-18 already have external coverage:

- **MemoHarness** (arXiv:2607.14159): dedicated Japanese feature at news-japan.ai naming the paper,
  all six control dimensions, and the dual-layer experience bank; found independently by three lanes.
- **SkillCenter** (arXiv:2607.07676): two Korean specialist features (storium.io) naming SkillCenter
  and SkillGate and reporting the 216,938 / 114,565 / 102,373 skill counts.
- **Auditable Agents / Implicit Execution Tracing**: the **Agent Times** feature naming Yue Zhao and
  explaining all five auditability pillars, and **WIDTH** applying the five dimensions and the
  overhead result to compliance infrastructure. First genuine editorial coverage of the auditing line.
- **Computer Vision News** (March 2019): newly surfaced dedicated PyOD feature, PDF pp.18-23, 24 hits.
- **Leiphone** (雷锋网): Chinese editorial translation naming PyOD with the full paper citation;
  human translator credited, so `editorial_translation` permits Tier 2.

### Gap found and closed mid-round

The first nine lanes returned 70 auditing-line candidates but almost all as topic-validation, and
**zero** for Implicit Execution Tracing (arXiv:2603.17445). Cause: the paper was never named in any
lane prompt, a lane-design omission, not an absence of coverage. A tenth lane was dispatched and
found **10 new items** for it, including a dedicated **Machine Brief** editorial explaining its
mechanism, results, and limitations, plus coverage on emergentmind, alphaXiv, sciencecast, wispaper,
fugumt, and takara.ai.

The same lane resolved an inconsistency in the Auditable Agents record. It verified **seven** current
third-party scholarly citations, four of them new: **AgentBound** (arXiv:2606.30970), **DEMM /
Decision Evidence Maturity Model** (arXiv:2605.04093), **Structural Governability**
(preprints.org 202605.0958), and **Programming Languages as Intermediate Representations**. Already
tracked: OpenClawBench, Proof-Carrying Agent Actions, Trace2Policy. One caveat recorded: *From Agent
Traces to Trust* (arXiv:2606.04990) cited Auditable Agents in v1, which validates the earlier entry,
but the current version differs.

**Auditability Card** now has external references (The Agent Times, DEMM, Emergent Mind) but no
independent completed Card, operationalizing benchmark, production adoption, or published critique.

### The auditing line's real problem is visibility, not absence

Across the auditing projects, roughly 19-20 candidates each landed in topic-validation: **McKinsey**
("The symbiotic enterprise"), **BCG** ("How Retail Banks Can Put AI Agents to Work"), **Deloitte**
("The AI advantage dilemma"), **KPMG** ("Agentic AI Gateway"), and the **NIST NCCoE Cyber AI Profile**
workshop are all actively writing about agent auditing, accountability, and governance without citing
this work. These are recorded in the Topic Validation appendix and are the highest-value citation
targets for the next cycle: a citation in any of them would be Tier 0/1.

### Ecosystem and academic downstream (recorded, pending row-level integration)

52 Tier 3 and 48 Tier 5 candidates were verified by the lanes but are **not yet folded into the main
ledger counts**, because deduplication against the 169 existing Ledger 3 rows is row-level work not
done in this pass. They are in `news-search-candidates.jsonl`. Strongest:

- **Three China patents**, each confirmed a unique family (not duplicates of the counted Actimize or
  Dun & Bradstreet families): `CN112989338B` (**Tencent**, COPOD, ¶0133/¶0165), `CN117216660B`
  (**DBAPPSecurity**, TODS, ¶0003), `CN117648656A` (**Chongqing University**, ADBench, ¶0125).
- **Praetor** (arXiv:2604.26274) deploys **Aegis** as a quantitative baseline: 12.8% attack success
  for Aegis versus 2.2% for Praetor, citing the exact title and arXiv:2603.12621.
- **PyCon US 2026** talk "When KPIs Go Weird: Anomaly Detection with Python"; **RSA Conference 2024**
  cloud-exfiltration session.
- University teaching material: **SFU CMPT 479/982 (Summer 2026) AI in Security**, **Uni Mannheim
  IE500 Data Mining**, plus a Chinese data-mining course.
- **Accenture** "Finance Function & AI Architect" job posting (found by two lanes). Per the skill's
  careers-page rule this needs a durable snapshot before counting; **snapshot pending**.
- Amplification: **Elvis Saravia / DAIR.AI** on X and **Latent Space AINews**, both on MemoHarness.

### Correction to existing counted data

**Ledger 2 row #22 (SitePoint) is resolved as REMOVED.** The 2026-06-14 pass flagged it UNVERIFIED;
this pass confirms the flag. The live 649-line article contains no Yue Zhao, FORTIS, USC, project
URL, arXiv:2603.22853, or HeadyZhang reference. Its only literal token is generic sample Docker YAML
(`services: agent-audit:` / `container_name: agent-audit-sandbox`). Wayback CDX returned no
snapshots, so the page did not change; the original claim was wrong. Reclassified to topic
validation. **Net −1 to Ledger 2.**

### Negative results (do not re-search)

- **OpenAlex reported zero citations** for both arXiv:2604.05485 and arXiv:2603.17445 while direct
  PDF verification found seven and several respectively. OpenAlex is visibly lagging for recent
  arXiv-only work; do not treat its zero as evidence of absence. This also bears on `/citation-audit`,
  which uses OpenAlex as a source.
- Google Scholar served a CAPTCHA; Connected Papers was transport-blocked; KPMG and LinkedIn PDFs
  were fetch-blocked in part.
- IMF and MIT policy PDFs scanned with no target matches.
- Hugging Face returned 404 for SEVA; SecRSS covered a different action-alignment paper; the Neurals
  result was a stale snippet.

### Verification status of this pass

Independent re-verification was run against this section rather than relying on the discovery workers' own
self-reported "verified" metadata, which is not evidence.

- **All 10 Tier 0 and Tier 1 rows were independently re-fetched and CONFIRMED.** Two rows needed adjustment. The
  ORNL count was corrected from 12 to 11. The FLI row understated its evidence by two pages.
- **The SitePoint removal was independently re-verified** by a separate fetch; see the Ledger 2 row #22 note.
- **Summary Statistics arithmetic checked**: Ledger 1 15+5=20; Ledger 2 73+5+6-1=83; total 296+16-1=311. Consistent.
- **Coverage matrix: produced.** See the "Coverage matrix" section below and `news-coverage-matrix.csv`
  (140 rows). It records that only 7 of 119 publications got an individual D5 search this round, so this pass
  is a targeted audit rather than a full one.

### Coverage matrix

Full per-item matrix: **`news-coverage-matrix.csv`** at the project root, one row for each of the
**140 inventory items** (119 publications + 21 tools) with columns for dimensions searched, Phase A
candidate count, kept / topic-only / dropped splits, and Phase B outcome.

Built by a 12-agent Claude workflow. The agents filtered naive token matches, which were mostly false
positives: the raw scan credited 53 candidates to the FORTIS paper and 42 to Auditable Agents purely
because the lab name and that phrase appear in candidate notes. After attribution those fall to their
real values.

**Outcome distribution across all 140 items**

| Phase B outcome | Items |
|---|---|
| kept (genuine coverage) | 30 |
| topic-only | 1 |
| dropped (all matches were false positives) | 9 |
| none (no candidate matched) | 100 |

**This pass was targeted, not a full audit.** Only **7 of 119 publications** received an individual
D5 smart-keyword search: the five newest papers plus the two follow-up targets. The other dimensions
(D1, D3, D4, D6, D7, D8) ran as broad sweeps that could surface any item, and D2 covered eight named
tools. The skill's full-audit mode requires a per-paper D5 search for every publication; that remains
outstanding and is the single largest coverage gap.

**Items with confirmed coverage this round**

| Item | kept | topic | dropped | strongest evidence |
|---|---|---|---|---|
| PyOD | 39 | 3 | 18 | https://www.gov.uk/algorithmic-transparency-records/london-b |
| Auditable Agents | 10 | 7 | 17 | https://theagenttimes.com/articles/action-assurance-framewor |
| When Only the Final Text Survives: Implicit Execution Trac | 8 | 0 | 6 | https://arxiv.org/abs/2606.00765 |
| MemoHarness: Agent Harnesses That Learn from Experience | 7 | 0 | 2 | https://news-japan.ai/1048/ |
| ADBench | 7 | 3 | 4 | https://www.nature.com/articles/s41467-025-56173-6 |
| ADBench: Anomaly Detection Benchmark | 7 | 3 | 4 | https://www.nature.com/articles/s41467-025-56173-6 |
| AEGIS: No Tool Call Left Unchecked -- A Pre-Execution Fire | 6 | 14 | 4 | https://arxiv.org/abs/2604.26274 |
| Aegis | 6 | 11 | 7 | https://news.ycombinator.com/item?id=48777144 |
| TrustLLM | 5 | 17 | 9 | https://www.osti.gov/servlets/purl/3002371 |
| SkillCenter: A Large-Scale Source-Grounded Skill Library f | 5 | 0 | 1 | https://www.storium.io/ai-%ec%97%90%ec%9d%b4%ec%a0%84%ed%8a% |
| TrustLLM: Trustworthiness in Large Language Models | 5 | 17 | 9 | https://www.osti.gov/servlets/purl/3002371 |
| Agent Safety Is Action Alignment | 5 | 1 | 0 | https://tenkai.blog/posts/2026-06-30/ |
| COPOD: Copula-Based Outlier Detection | 4 | 0 | 2 | https://www.nature.com/articles/s41598-026-45091-2 |
| GRADE: Graph Representation of LLM Agent Dependency and Ex | 4 | 2 | 7 | https://www.emergentmind.com/topics/agent-dependency-graph |
| agent-style | 4 | 0 | 2 | https://news.ycombinator.com/item?id=48919335 |
| SEVA: Self-Evolving Verification Agent with Process Reward | 3 | 0 | 0 | https://www.alphaxiv.org/abs/2607.07663 |
| awesome-auditable-ai | 2 | 0 | 2 | https://news.ycombinator.com/item?id=48777144 |
| agent-audit | 2 | 20 | 8 | https://reputagent.com/ecosystem/headyzhang-agent-audit |
| anywhere-agents | 2 | 0 | 0 | https://www.awesomeskills.dev/en/skill/yzhao062-anywhere-age |
| FlexRouter: Learning Complementary Model Sets for Flexible | 2 | 0 | 0 | https://research.adobe.com/publication/flexrouter-learning-c |
| SUOD | 2 | 0 | 0 | https://www.nature.com/articles/s41598-026-45091-2 |
| PyGOD | 1 | 0 | 0 | https://haebom.dev/d367nxm3qe9vkmj98pv1 |
| Therapeutics Data Commons: Machine Learning Datasets and T | 1 | 0 | 1 | https://arxiv.org/abs/2508.10899 |
| auditable | 1 | 2 | 43 | https://pypi.org/project/auditable/ |
| TODS | 1 | 0 | 0 | https://patents.google.com/patent/CN117216660B/en |
| TDC | 1 | 0 | 1 | https://arxiv.org/abs/2508.10899 |
| Agent Audit: A Security Analysis System for LLM Agent Appl | 1 | 3 | 3 | https://arxiv.org/pdf/2605.19362 |
| AD-AGENT | 1 | 0 | 0 | https://haebom.dev/d367nxm3qe9vkmj98pv1 |
| PyOD 2: A Python Library for Outlier Detection with LLM-po | 1 | 0 | 1 | https://dev.to/lovestaco/ways-devs-are-plugging-llms-into-an |
| Anomaly-Detection-Resources | 1 | 0 | 0 | https://zhoushengisnoob.github.io/courses/resources/DMCourse |

**Attribution caveat: 9 probable false negatives.** The zero-pool sanity check examined 36 of the 100
no-candidate items and found 9 where real coverage likely exists but was filed under a sibling work.
The candidate schema records each hit under a single `work`, so coverage that names several works at
once is credited to only one of them.

| Item | Why the token scan missed it |
|---|---|
| "Someone Hid It" (ICML 2026) | Record 198 names Yue Zhao and the paper. Missed on punctuation alone: a curly apostrophe in the title. |
| ECOD | The Nature Sci Rep paper says COPOD, ECOD, and Isolation Forest were implemented via PyOD, but the record is filed under PyOD. |
| SUOD (MLSys 2021) | Nature Sci Rep lists SUOD among eight PyOD algorithms; Zhejiang University lecture slides name it on p.92. |
| SUOD (AAAI-21 workshop) | Same two records name only the bare acronym, which cannot be resolved between the two SUOD papers. |
| AD-AGENT | Korean Daily Arxiv digest carries the exact title plus Yue Zhao, PyOD, and PyGOD, but is filed elsewhere. |
| TODS | Patent CN117216660B names TODS as prior art in Background paragraph 0003, as a paraphrase rather than the title. |
| AI Foundation for Therapeutic Science | Cited only as "TDC" or "Therapeutics Data Commons", never by title. |
| AD-LLM | Two candidates sit exactly on its topic but were recorded under other works. |
| ADMoE | Patent CN117648656A is a title-level conceptual match on multi-expert anomaly detection. |

These are attribution artifacts rather than missing discovery: the underlying sources are already in
`news-search-candidates.jsonl`. Fixing this needs a multi-work attribution field in the candidate
schema, which is a change to `references/candidate-schema.md` and is not made here.

### Registry harvest

New domains from confirmed hits this round, to append to `references/domain-registry.md`:
`gov.uk` (algorithmic-transparency-records), `sdaia.gov.sa`, `osti.gov`, `api.oecdai.org`,
`nvd.nist.gov`, `ntt-review.jp`, `news-japan.ai`, `storium.io`, `theagenttimes.com`, `width.com`,
`machinebrief.com`, `rsipvision.com`, `leiphone.com`, `emergentmind.com`, `alphaxiv.org`,
`sciencecast.org`, `wispaper.ai`, `fugumt.com`, `tldr.takara.ai`, `preprints.org`, `agentarxiv.org`.

### Security finding (not coverage; recorded for tracking)

**CVE-2026-15529** (NVD, published 2026-07-13, CVSS 3.1 6.3 MEDIUM,
`AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:L`) reports unsafe deserialization in
`pyod.utils.persistence.load`, which calls `joblib.load(path)` before envelope validation. It
corresponds to repo issue #697 (2026-06-10) and fix PR #698 ("Require explicit trust for
persistence.load"), which is open and mergeable but unmerged. The CVE lists 3.5.0/3.5.1/3.5.2; the
current release is 3.6.1 and the fix is unmerged, so the affected-version range will need updating
once a fix ships. Tracked here because an open NVD entry against PyOD affects the compliance posture
of the government and enterprise deployments recorded in Ledger 1 and Ledger 3.

---


## Consolidated Read: Claude 2026-06-13 + Codex 2026-06-14

Two independent broad searches (Claude `/workflows` two-phase, then Codex 9-lane parallel) reached the same headline: **net-new Tier 0/1 direct editorial coverage = 0.** Editorial and press coverage of the FORTIS works is saturated; both passes mostly re-surfaced already-tracked rows. Two methods converging raises confidence that the ledgers are comprehensive as of mid-June 2026.

**Where the new signal actually is** (all bibliometric, so route to `/citation-audit`, not the editorial ledgers):
- Auditable Agents (arXiv:2604.05485): 4 third-party citations within weeks (Claude deep-dive): 2606.04104, 2606.10457 (SF Express, an industry author), 2606.04990, 2605.29253.
- ADBench: 3 new citing arXiv rows (2606.12483, 2604.20255, 2602.03293); Aegis: 1 (2604.26274); TDC / TxGemma-adjacent: 1 (2508.10899) (Codex).

**New low-tier candidates for Phase B** (T3/T5; cluster-dedupe before any ledger change): three China patents, CN112989338B (COPOD), CN117216660B (TODS), CN117648656A (ADBench); PyOD ecosystem rows (Analytics Vidhya, TSB-AD, Databricks industry-solution repo, CSDN, Spanish Wikipedia); agent-security ecosystem (Aegis in Awesome-Agent-Harness, ReasonBreak using DoxBench, SafeSwitch / asqi TrustLLM). Full per-URL verdicts are in `news-search-candidates.jsonl` (147 records).

**One action that touches existing counted data:** Ledger 2 row #22 (SitePoint "OpenClaw Security Audit Guide") is flagged UNVERIFIED. Codex's live check found no agent-audit / Yue Zhao / FORTIS mention, no Wayback snapshot exists, and the page returns 403 to automated fetch. Confirm in a logged-in browser; if the mention is absent, demote the row and Ledger 2 drops from 73 to 72.

**Negatives recorded this cycle** (so future rounds skip them): ENISA AI cybersecurity framework and Stanford HAI 2026 AI Index (both checked, no TrustLLM), the White House 2026 AI policy framework PDF, the OpenAI GPT-5 system card PDF (no FORTIS hits), and the name collisions trustllm.eu and TraceAegis (arXiv:2606.11671).

---

## 2026-06-14 Codex Independent Broad Search

Codex ran a fresh search independent of the 2026-06-13 Claude refresh. The pass used the project-local `skills/news-search` workflow, parsed the current local inventory as 112 publications and 19 tools, and used exact-URL dedupe against `news-coverage-audit.md` plus `news-search-candidates.jsonl`.

Search coverage was deliberately broad: policy/PDF/foundation-model reports; media, security, and agent-risk press; ecosystem and tool adoption; smart-paper downstream usage; multilingual sources, patents, HN, Qiita, CSDN, GitHub README evidence, careers, procurement, and academic-downstream search. The first 5 structured lanes were followed by 4 less constrained lanes after the user asked for a bolder pass.

**Net new Tier 0/1 direct coverage verified: 0.** The run added **46** exact-URL scratch records to `news-search-candidates.jsonl`: candidates, drops, duplicate-existing family rows, topic-validation rows, and verified negatives. No official government, foundation-model-company, major policy, or major media source was found that newly names a FORTIS work beyond the already-counted ledger rows.

### New Phase B Candidates

- **Academic downstream, not editorial coverage:** new ADBench rows at arXiv:2606.12483, arXiv:2604.20255, and arXiv:2602.03293; an Aegis downstream benchmark row at arXiv:2604.26274; and a TDC / TxGemma-adjacent row at arXiv:2508.10899. These should route to citation-audit or academic-evidence review, not direct news-ledger promotion.
- **PyOD ecosystem and tutorial evidence:** Analytics Vidhya PyOD tutorial, nonconform arXiv and GitHub rows, TSB-AD, Databricks industry-solution repo, GitHub resource-list rows, CSDN PyOD tutorial URLs, Spanish Wikipedia pages, and low-signal Qiita / HN rows. These are useful completeness signals but should be cluster-deduped before any Ledger 3 change.
- **Agent-security ecosystem evidence:** Agent Banana Hugging Face Papers, Aegis in Awesome-Agent-Harness, ReasonBreak using DoxBench, SafeSwitch / asqi TrustLLM mentions, plus topic-validation rows on MCP over-privilege and task-scoped agent authorization.
- **Patent candidates needing Phase B:** CN112989338B (COPOD), CN117216660B (TODS), and CN117648656A (ADBench). Two patent rows surfaced in this pass were exact family duplicates of already-counted Actimize and Dun & Bradstreet patent evidence.

### Verified Negatives and Drops

- White House 2026 "National Policy Framework for Artificial Intelligence: Legislative Recommendations" PDF: checked as D8 government/policy evidence and found no FORTIS term hits.
- OpenAI GPT-5 system card PDF: checked as foundation-model-company evidence and found no FORTIS term hits.
- arXiv:2606.11671 "Runtime Skill Audit": the only Aegis hit was TraceAegis, a different work, so it is a name collision.
- trustllm.eu is a TrustLLM name collision and is not Yue/FORTIS TrustLLM benchmark coverage.
- Reddit search returned 403 in this pass; blocked Reddit queries are not absence evidence.

### Audit Recheck

- SitePoint "OpenClaw Security Audit Guide 2026" needs manual reconciliation. The current live page did not show a direct FORTIS `agent-audit`, USC, Yue Zhao, or FORTIS Lab mention during the 2026-06-14 pass, while the existing ledger classification treats the page as direct coverage. Check an archived snapshot before retaining that row as counted direct evidence.

---

## 2026-06-13 Refresh: New This Round (Claude /workflows Two-Phase Run)

Two-phase `/workflows` run (Phase A: 10 dimension agents in waves of 3 produced 84 candidates; Phase B: 12 verification batches plus 3 dedicated Auditable Agents agents in waves of 6 produced 67 keeps; per-URL verdicts merged into `news-search-candidates.jsonl`).

**Net new editorial coverage: about 0 counted ledger rows**, consistent with the two 2026-05-28 runs. The full re-sweep mostly re-surfaced already-tracked items. Phase B flagged several as new only because the in-prompt dedup brief did not enumerate the full Ledger 3 ecosystem list; a cross-check against the audit confirms they are already present (see "Already Tracked" below). The one genuinely new signal is the Auditable Agents downstream citations.

### Auditable Agents (arXiv:2604.05485): Early Downstream Citations

The dedicated deep-dive found **4 genuine third-party citations** of the paper within weeks of posting (full text plus bibliography verified; independent groups, no FORTIS author overlap). No press, blog, or community coverage yet (Hugging Face Papers returns 404). These are bibliometric, so they belong to `/citation-audit` rather than an editorial ledger; recorded here as a visibility signal:
- arXiv:2606.04104: reproduces all five auditability dimensions as the conceptual basis (strongest).
- arXiv:2606.10457: SF Express authors; credit it as "formaliz[ing] agent-auditability".
- arXiv:2606.04990: cites "Nian et al., 2026" / "Auditable agents" in the audit/trust-functions section.
- arXiv:2605.29253: names the paper by title; cites arXiv:2604.05485 in the intro and Section 2.2.
- Excluded: arXiv:2604.17299 (Cat-DPO) is a same-group self-citation.

### Already Tracked (Re-Confirmed This Round, Not Added)

The sweep re-verified these; all are already in the ledgers, so no count change:
- **Grokipedia (xAI)** entry for Yue Zhao: already Ledger 4 #70.
- **Ericsson patent WO2023166515A1** (PyOD citation in the Background): already tracked.
- **DataCamp / Udemy anomaly-detection courses** and the **Manning / O'Reilly "Outlier Detection in Python"** book (PyOD / ECOD / COPOD): already in Ledger 3.
- **~45 PyOD / PyGOD / combo tutorials** (Medium, Towards Data Science, Zhihu, Qiita, Velog, ClassCat, and others): covered by existing equivalent Ledger 3 rows; per-URL verdicts in `news-search-candidates.jsonl`. One worth a spot-check is the Sep 2025 Towards Data Science "Boosting Your Anomaly Detection With LLMs" piece, which cites the **PyOD 2** paper (Chen et al., arXiv:2412.12154) by name.

### Held: Needs Manual Verification (Not Yet Counted)

- **alphaXiv VisualTimeAnomaly** (arXiv:2502.17812) and **aimodels.fyi JailDAM** (arXiv:2504.03770): both confirmed FORTIS works (Yue Zhao co-author), but the aggregator pages returned a deterministic 403, so the on-page mention is unverifiable. T5 if confirmed.
- **CSDN PyOD tutorials** (HTTP 521 Cloudflare) and **Course Hero Deakin SIT719** (403): T3 tutorials, page bodies unreachable, not promoted from snippet alone.

### Negative / Dropped (Recorded so Future Rounds Skip)

- **ENISA, "Multilayer Framework for Good Cybersecurity Practices for AI"** PDF: fetched and checked, does **not** name TrustLLM (the snippet was a false positive). Verified-negative.
- **Stanford HAI 2026 AI Index (Responsible AI chapter)**: read in full and checked (Yue, 2026-06-13), does **not** name TrustLLM. Verified-negative; the earlier search-snippet match was a generic description of TrustLLM, not the report citing it.
- **Auditable Agents name collisions** (generic "auditable agents" / "AI agent audit" phrasing with no citation of arXiv:2604.05485): IBM Think, squirro.com, Medium (IndextDataLab and aiteacher), Hacker News item 47178697, arXiv:2605.06812 and arXiv:2604.25085 (distinct papers), GitHub Justin0504/Aegis (cites the Aegis paper arXiv:2603.12621, not Auditable Agents), GitHub HeadyZhang/agent-audit (unrelated same-name repo).
- **First-party** (correctly excluded): the NSF PAR record of the PI's own grant output (TOD), the TrustGen / TrustEval own repo, and the Auditable Agents arXiv record and USC author page.

### Citation-Audit Hook

`citation-affiliation-audit.md` last refreshed 2026-05-28 (16 days, still fresh under the 30-day gate); the integrated "## Citation Affiliation Evidence" section below remains current, so no re-integration this round.

---

## Ledger 1: Government & Policy Citations

Items where government bodies, policy organizations, or foundation model companies cite your work by name in official documents.

| # | Work Cited | Source | Detail | Date |
|---|-----------|--------|--------|------|
| 1 | TrustLLM | **U.S. Senate HSGAC** | Footnote 119, p.25: *"the trustworthiness of large language models is still being analyzed"* in "Hedge Fund Use of Artificial Intelligence" | Jun 2024 |
| 2 | TrustLLM | **U.S. Department of Defense (CDAO)** | Listed in the official "Generative AI Responsible AI Toolkit" (v1.0). Published by the Chief Digital and AI Office, Responsible AI Division. | Dec 2024 |
| 2b | PyOD | **U.S. Department of Defense (CDAO)** | Same official toolkit lists Python Outlier Detection (PyOD) as a dedicated **Production / High-maturity** OOD-detection tool entry (TOC p.3, full entry p.49); the recommendation column places PyOD inside reliability / governability / equitability assurance use; Stage 3 Assessment §3.1.10 links PyOD as the answer to the in-use monitoring question. URLs: `pyod.readthedocs.io` and `github.com/yzhao062/pyod` (the GitHub path itself names the author). | Dec 2024 |
| 3 | TrustLLM | **NIST AI 100-2e2025** | Named in Section 3.6 "Benchmarks for AML Vulnerabilities" as a benchmark for six dimensions of trust in LLMs. NIST Special Publication on Adversarial Machine Learning. | Mar 2025 |
| 4 | TrustLLM | **Future of Life Institute** | Official benchmark in AI Safety Index (Inaugural Edition). | Dec 2024 |
| 5 | TrustLLM | **Future of Life Institute** | Official benchmark in AI Safety Index (Summer 2025). Pages 5, 9, 11, 17, 34, 36, 37. | Jul 2025 |
| 6 | TrustLLM | **Future of Life Institute** | Official benchmark in AI Safety Index (Winter 2025). Pages 7, 11, 13, 21, 27, 43, 46. Full indicator definition p.46. | Dec 2025 |
| 7 | TrustLLM | **Future of Life Institute** | Dedicated TrustLLM Indicator Data Sheet with scores for 8 AI companies. | Nov 2025 |
| 8 | PyOD | **European Space Agency (ESA/ESOC)** | All 30 anomaly detection algorithms in the OPS-SAT spacecraft telemetry benchmark implemented using PyOD 1.1.2. Published in **Nature Scientific Data** (2025). | 2025 |
| 8b | TrustLLM | **International AI Safety Report 2026** | Citation #881. Led by Yoshua Bengio, authored by 100+ AI experts, backed by 30+ countries and international organisations. Published Feb 2026. | Feb 2026 |
| 8c | DoxBench | **Privacy International** | Cited on p.28, footnote 56: "Luo W., Qiming Z., Lu T., Liu X., Zhao Y., Xiang Z., Xiao C., 'Doxing via the Lens: Revealing Privacy Leakage in Image Geolocation for Agentic Multi-Modal Large Reasoning Model'" in "Nowhere to Hide? Privacy Risks and Policy Implications of AI Geolocation." | Feb 2026 |
| 8d | TrustLLM | **LLNL / DOE National Labs SafeAI report** | "Safety in Artificial Intelligence: Challenges and Opportunities for the U.S. National Labs and Beyond" cites "Position: TrustLLM: Trustworthiness in Large Language Models" as reference [34]. | Dec 2024 |
| 8e | TrustLLM | **MITRE LILAC v1 technical report** | "Emerging Risks and Mitigations for Public Chatbots: LILAC v1" cites TrustLLM in the text and reference list as a test case / metric for LLM trustworthiness. MITRE report MTR240382, approved for public release. | Sep 2024 |
| 8f | TDC | **Google DeepMind / Google Research TxGemma** | Official TxGemma report and Google Developers pages name Therapeutics Data Commons (TDC) as the task/data source for TxGemma training and evaluation across 66 therapeutic development tasks. | Apr 2025 |
| 8g | PyOD | **OpenAI Careers** | Official OpenAI Careers "Technical Intelligence Analyst, San Francisco" listing, Qualifications section: "Have experience with anomaly detection tools, such as PyOD, and discovery processes for surfacing novel or low-prevalence patterns." Operational adoption signal from a foundation-model company; placed in Ledger 1 as Tier 0(b)-equivalent foundation-model-company official content. Live URL is volatile (careers pages are pulled when roles close) and Wayback Save Page Now returns "Job failed" because OpenAI blocks the Internet Archive crawler; durable evidence is kept locally at [`news-snapshots/openai-careers-technical-intelligence-analyst-2026-05-07.md`](news-snapshots/openai-careers-technical-intelligence-analyst-2026-05-07.md) with browser-captured `.html` / `.pdf` sidecars in the same folder. | May 2026 |

**Source URLs:** [Senate PDF](https://www.hsgac.senate.gov/wp-content/uploads/2024.06.11-Hedge-Fund-Use-of-AI-Report.pdf) · [CDAO Toolkit](https://www.ai.mil/Portals/137/Documents/Resources%20Page/2024-12GenAI-Responsible-AI-Toolkit.pdf) · [NIST PDF](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2025.pdf) · [FLI Inaugural](https://futureoflife.org/ai-policy/ai-experts-major-ai-companies-have-significant-safety-gaps/) · [FLI Summer](https://futureoflife.org/ai-safety-index-summer-2025/) · [FLI Winter](https://futureoflife.org/ai-safety-index-winter-2025/) · [FLI Indicator Sheet](https://futureoflife.org/wp-content/uploads/2025/11/Indicator-TrustLLM_Benchmark.pdf) · [ESA OPS-SAT](https://www.nature.com/articles/s41597-025-05035-3) · [Intl AI Safety Report](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026) · [Privacy Intl](https://www.privacyinternational.org/report/5736/nowhere-hide-privacy-risks-and-policy-implications-ai-geolocation) · [LLNL SafeAI PDF](https://data-science.llnl.gov/sites/data_science/files/2024-12/SafeAIforDOE%20Digital.pdf) · [MITRE LILAC PDF](https://www.mitre.org/sites/default/files/2024-10/PR-24-2767-Emerging-Risks-Mitigations-Public-Chatbots-LILAC-v1.pdf) · [TxGemma report](https://storage.googleapis.com/research-media/txgemma/txgemma-report.pdf) · [Google TxGemma docs](https://developers.google.com/health-ai-developer-foundations/txgemma) · [OpenAI Careers](https://openai.com/careers/technical-intelligence-analyst-san-francisco/) · [snapshot](news-snapshots/openai-careers-technical-intelligence-analyst-2026-05-07.md)

**Dimension 8 (PDF deep search) status:** Searched 25+ governance PDFs + regulated verticals for all 105 papers + 19 tools. TrustLLM confirmed in Senate HSGAC, DoD CDAO, NIST AI 100-2e2025, FLI x4 (inaugural, summer, winter, indicator sheet), International AI Safety Report 2026, LLNL/DOE SafeAI, and MITRE LILAC. DoxBench confirmed in Privacy International report. PyOD confirmed in ESA OPS-SAT benchmark, DoD CDAO toolkit, and the official OpenAI Careers Technical Intelligence Analyst listing. TDC confirmed in Google/DeepMind TxGemma official report/docs. Deloitte Germany AIxAML was verified and recorded under ecosystem/industry evidence.

**D8 candidates resolved:**
- ~~**OWASP GenAI Solutions Landscape Q2 2026**~~ — manually checked Apr 10; no universities or academic tools listed. Cleared.

**Count: 15 government/policy/foundation-model citations (TrustLLM x10, PyOD x3, DoxBench x1, TDC x1)**

---

## Ledger 2: External Third-Party Media

Independent third-party coverage by outlets not affiliated with you, your lab, or your co-authors. These are the items a promotion committee would consider "external recognition."

**Inclusion rule:** Bare publication-listing pages from coauthor institutions are tracked in Ledger 3 unless they include clear editorial/news treatment. Legacy Ledger 2 research-listing rows are kept pending a future cleanup pass.

| # | Work Named | Outlet | Type | Headline | Date | Dim | URL |
|---|-----------|--------|------|----------|------|-----|-----|
| 5 | TrustLLM | **The Paper (澎湃新闻)** | Tier 1 Chinese news | "大语言模型的可信之路：TrustLLM全面揭秘" | 2024 | D7 | [Link](https://www.thepaper.cn/newsDetail_forward_26315865) |
| 6 | TrustLLM | Lawrence Livermore National Lab | National lab article | "Evaluating trust and safety of large language models" | 2024 | D3 | [Link](https://computing.llnl.gov/about/newsroom/evaluating-trust-safety-llms) |
| 7 | TrustLLM | Microsoft Research | Research listing | Listed as MS Research publication | 2024 | D3 | [Link](https://www.microsoft.com/en-us/research/publication/trustllm-trustworthiness-in-large-language-models/) |
| 8 | TrustGen | Hoover Institution (Stanford) | Research listing | Listed as Hoover research publication | 2026 | D3 | [Link](https://www.hoover.org/research/trustgen-platform-dynamic-benchmarking-trustworthiness-generative-foundation-models) |
| 9 | TrustGen | Microsoft Research | Research listing | Part of ICLR 2026 portfolio | 2026 | D3 | [Link](https://www.microsoft.com/en-us/research/publication/trustgen-a-platform-of-dynamic-benchmarking-on-the-trustworthiness-of-generative-foundation-models/) |
| 10 | TrustLLM | MarkTechPost | AI newsletter | "Navigating the Complexity of Trustworthiness in LLMs: A Deep Dive into the TRUST LLM Framework" | Jan 2024 | D3 | [Link](https://www.marktechpost.com/2024/01/16/navigating-the-complexity-of-trustworthiness-in-llms-a-deep-dive-into-the-trust-llm-framework/) |
| 11 | DrugAgent | MarkTechPost | Tech blog article | "Meet DrugAgent: A Multi-Agent Framework for Automating ML in Drug Discovery" | Dec 2024 | D3 | [Link](https://www.marktechpost.com/2024/12/01/meet-drugagent-a-multi-agent-framework-for-automating-machine-learning-in-drug-discovery/) |
| 12 | DrugAgent | Nature Biotechnology | Journal citation | Cited in "Agentic AI and the rise of in silico team science" — names DrugAgent as agent querying specialized databases for drug-target interactions | 2026 | D4 | [Link](https://www.nature.com/articles/s41587-026-03035-1) |
| 13 | TDC | Harvard Medical School News | University PR | "Can AI transform the way we discover new drugs?" | Nov 2022 | D3 | [Link](https://hms.harvard.edu/news/can-ai-transform-way-we-discover-new-drugs) |
| 14 | TDC | Phys.org | Science syndication | Syndication of Harvard article | Nov 2022 | D3 | [Link](https://phys.org/news/2022-11-ai-drugs.html) |
| 15 | TDC | Amazon Science | Industry research | "Cracking the code of how diseases affect the body" | May 2023 | D3 | [Link](https://www.amazon.science/research-awards/success-stories/cracking-the-code-of-how-diseases-affect-the-body) |
| 16 | BOND/PyGOD | Amazon Science | Industry research paper | "Graph Diffusion Models for Anomaly Detection" — cites Yue Zhao as co-author of BOND, cites PyGOD | 2024 | D3 | [Link](https://assets.amazon.science/0c/61/10782ada424e9bfb3eca22bc61b2/graph-diffusion-models-for-anomaly-detection.pdf) |
| 17 | Yue Zhao | USC Viterbi | University PR | "Spot the Difference: Safeguarding Cybersecurity with Graph Anomaly Detection" | Jan 2025 | D3 | [Link](https://viterbischool.usc.edu/news/2025/01/spot-the-difference-safeguarding-cybersecurity-with-graph-anomaly-detection/) |
| 18 | Yue Zhao | USC Viterbi | University PR | "From Censored Chatbots to Cinematic Visuals" (Ojas Nimase CRA award) | Mar 2026 | D3 | [Link](https://viterbischool.usc.edu/news/2026/03/from-censored-chatbots-to-cinematic-visuals-usc-undergraduates-push-the-boundaries-of-ai/) |
| 18b | Yue Zhao | USC Viterbi | University PR | "USC at ICLR 2025" — names Yue Zhao for MetaOOD | Apr 2025 | D3 | [Link](https://viterbischool.usc.edu/news/2025/04/usc-at-iclr-2025/) |
| 18c | Yue Zhao | USC Viterbi | University PR | "USC at ICML" — names Yue Zhao for molecule synthesis (Oral) | Jul 2024 | D3 | [Link](https://viterbischool.usc.edu/news/2024/07/usc-at-the-international-conferences-on-machine-learning-icml/) |
| 18d | Yue Zhao | USC Viterbi | University PR | "Ten New Faculty Members Join CS" — names Yue Zhao, PyOD, 16K stars | Sep 2023 | D3 | [Link](https://viterbischool.usc.edu/news/2023/09/ten-new-faculty-members-join-the-thomas-lord-department-of-computer-science/) |
| 18e | MultiOOD | USC ISI | University PR | "USC at NeurIPS 2024" — names MultiOOD, Yue Zhao | Dec 2024 | D5 | [Link](https://www.isi.edu/news/73818/usc-at-the-conference-on-neural-information-processing-systems-neurips-2024/) |
| 18f | TyphoFormer | Florida State U CS | University PR | "Dr Yushun Dong Received Awards (SIGSPATIAL, ICDM)" — names TyphoFormer | Dec 2025 | D5 | [Link](https://www.cs.fsu.edu/dr-yushun-dong-received-awards-sigspatial-icdm-and-has-paper-published-aaai2-wsdm-sigkdd/) |
| 19 | ICDM paper | CCC Blog | Research community | ICDM 2025 BlueSky Track Second Prize CCC Award | Dec 2025 | D3 | [Link](https://cccblog.org/2025/12/19/announcing-blue-sky-track-winners-at-icdm-2025/) |
| 20 | IET paper | AI Accelerator Institute | Industry blog | "Solving accountability in multi-agent AI systems" | 2026 | D3 | [Link](https://www.aiacceleratorinstitute.com/when-multi-agent-ai-systems-fail-who-takes-the-blame/) |
| 21 | Aegis | AI:PRODUCTIVITY | Tech news | "Aegis: Open-Source Firewall That Intercepts AI Agent Tool Calls" | Mar 2026 | D3 | [Link](https://aiproductivity.ai/news/aegis-open-source-firewall-ai-agent-tool-calls/) |
| 22 | agent-audit | SitePoint | Developer publication | **[REMOVED 2026-07-19: NOT COVERAGE]** "OpenClaw Security Audit Guide 2026". Flagged UNVERIFIED 2026-06-14; confirmed 2026-07-19 by full live fetch of the 649-line article: no Yue Zhao, FORTIS, USC, project URL, arXiv:2603.22853, or HeadyZhang reference. Its only literal token is generic sample Docker YAML (`services: agent-audit:` / `container_name: agent-audit-sandbox`). Wayback returned no snapshots, so the page did not change and the original claim was wrong. Independently re-verified 2026-07-19 by a separate fetch: `agent-audit` appears 3 times, all as a Docker service or container name (`services: agent-audit:`, `container_name: agent-audit-sandbox`); `USC` appears 3 times, all as the substring inside "obfuscated", which is the likely source of the original false positive; the only GitHub link in the article is `github.com/moby/moby`. Reclassified to Topic Validation; not counted. |
| 23 | StealthRank | LLMoGuy.com | AI blog | "StealthRank: Manipulating AI Search Results Through Stealthy Content Tweaks" | 2026 | D5 | [Link](https://www.llmoguy.com/stealthrank-manipulating-ai-search-results-through-stealthy-content-tweaks) |
| 24 | GLIP-OOD | Quantum Zeitgeist | Tech blog | "Graph AI Enables Zero-Shot OOD Detection: A New Frontier" | 2025 | D5 | [Link](https://quantumzeitgeist.com/graph-ai-enables-zero-shot-out-of-distribution-detection-a-new-frontier-in-graph-based-anomaly-detection/) |
| 25 | Computing Resources | DEV Community | Dev blog (external author) | Blog post; referenced in CSPaper Forum re: CVPR 2026 compute disclosure | 2025 | D5 | [Link](https://dev.to/paperium/the-role-of-computing-resources-in-publishing-foundation-model-research-1bfe) |
| 26 | PyOD | KDnuggets | Data science outlet | "An Overview of Outlier Detection Methods from PyOD" | 2019 | D3 | [Link](https://www.kdnuggets.com/2019/06/overview-outlier-detection-methods-pyod.html) |
| 27 | PyOD | Analytics Vidhya | Data science outlet | "An Awesome Tutorial to Learn Outlier Detection using PyOD" | 2019 | D3 | [Link](https://www.analyticsvidhya.com/blog/2019/02/outlier-detection-python-pyod/) |
| 28 | PyOD | The Data Scientist | Data science outlet | "Anomaly detection in Python using the pyod library" | -- | D3 | [Link](https://thedatascientist.com/anomaly-detection-in-python-using-the-pyod-library/) |
| 29 | PyOD | SmartDev | Tech blog | "Master AI Anomaly Detection: The Definitive Guide" | -- | D3 | [Link](https://smartdev.com/ai-anomaly-detection/) |
| 30 | PyOD | Towards Data Science | Data science blog | "Introducing Anomaly/Outlier Detection in Python with PyOD" | -- | D3 | [Link](https://towardsdatascience.com/introducing-anomaly-outlier-detection-in-python-with-pyod-40afcccee9ff/) |
| 31 | PyOD | Towards Data Science | Data science blog | "Real-Time Anomaly Detection With Python" (PyOD + PySAD) | Mar 2025 | D3 | [Link](https://towardsdatascience.com/real-time-anomaly-detection-with-python-36e3455e84e2/) |
| 32 | PyOD | Cake.ai | Industry guide | "Anomaly Detection Software: A Complete Guide" — recommends PyOD as "a strong starting point" | Aug 2025 | D2 | [Link](https://www.cake.ai/blog/open-source-anomaly-detection-tools) |
| 33 | PyOD | Milvus/Zilliz | Industry reference | "What are open-source libraries for anomaly detection?" — names PyOD as notable library | -- | D2 | [Link](https://milvus.io/ai-quick-reference/what-are-opensource-libraries-for-anomaly-detection) |
| 34 | TrustLLM | Prompting Guide | Educational reference | "Trustworthiness in LLMs" — references TrustLLM benchmark | -- | D7 | [Link](https://www.promptingguide.ai/research/trustworthiness-in-llms) |
| 34b | TrustLLM | **机器之心 (Jiqizhixin)** | Top-tier Chinese AI media | "大语言模型的可信之路：TrustLLM全面揭秘" | Feb 2024 | D7 | [Link](https://www.jiqizhixin.com/articles/2024-02-08-8) |
| 34c | TrustLLM | 腾讯新闻 (Tencent News) | Chinese news syndication | TrustLLM syndication | Feb 2024 | D7 | [Link](https://news.qq.com/rain/a/20240208A03WT900) |
| 34d | TrustLLM | 新浪财经 (Sina Finance) | Chinese finance/tech platform | TrustLLM syndication | Feb 2024 | D7 | [Link](https://finance.sina.cn/tech/2024-02-08/detail-inahicqm1653854.d.html) |
| 34e | TrustLLM | 懂AI (DongAIGC) | Chinese AI specialist | "TrustLLM:大型语言模型的可信度评估框架" | 2024 | D7 | [Link](https://www.dongaigc.com/a/trust-llm-reliability-assessment) |
| 34f | PyOD | 搜狐 (Sohu) | Major Chinese portal | "又一强大的异常检测开源工具库：PyOD" | 2023 | D7 | [Link](https://www.sohu.com/a/692330141_121118999) |
| 35 | TODS | Towards Data Science | Data science blog | "TODS: Detecting Outliers from Time Series Data" | -- | D3 | [Link](https://towardsdatascience.com/tods-detecting-outliers-from-time-series-data-2d4bd2e91381/) |
| 36 | DrugAgent | Awesome AI Agents for Healthcare | Curated list | Listed in community resource | -- | D3 | [Link](https://github.com/AgenticHealthAI/Awesome-AI-Agents-for-Healthcare) |
| 36b | TrustLLM | TechXplore | Science media | "Highlight solutions to make large language models trustworthy" | Aug 2024 | D10 | [Link](https://techxplore.com/news/2024-08-highlight-solutions-large-language-trustworthy.html) |
| 36c | PyOD | Ericsson Blog | Enterprise blog | "How to make anomaly detection more accessible" — names PyOD in E-ADF framework | Jul 2020 | D10 | [Link](https://www.ericsson.com/en/blog/2020/7/how-to-make-anomaly-detection-more-accessible) |
| 36d | PyOD/ADBench | Elder Research | Enterprise consulting | "Business Insights Meet Analytics Skills in Anomaly Detection" — recommends PyOD and ADBench | Mar 2025 | D10 | [Link](https://www.elderresearch.com/blog/business-insights-meet-analytics-skills-in-anomaly-detection/) |
| 36e | PyOD | KDnuggets | Data science outlet | "Outlier Detection Methods Cheat Sheet" — names PyOD, Yue Zhao | Feb 2019 | D10 | [Link](https://www.kdnuggets.com/2019/02/outlier-detection-methods-cheat-sheet.html) |
| 36f | PyOD | Data Reply IT | Enterprise consulting | "Anomaly Detection made easy with PyOD" (European IT consulting, Reply Group) | 2023 | D10 | [Link](https://medium.com/data-reply-it-datatech/anomaly-detection-made-easy-with-pyod-960faf6da4e5) |
| 36g | PyOD 2 | Towards Data Science | Data science blog | "Boosting Your Anomaly Detection With LLMs" — dedicated article on PyOD 2's LLM-powered model selection | Sep 2025 | D3 | [Link](https://towardsdatascience.com/boosting-your-anomaly-detection-with-llms/) |
| 36h | JailDAM | Brian D. Colwell | Security reference | "The Big List of AI Jailbreaking References and Resources" — curated list, names JailDAM and Yue Zhao | 2025 | D5 | [Link](https://briandcolwell.com/the-big-list-of-ai-jailbreaking-references-and-resources/) |
| 36i | PyOD | Number Analytics | Industry blog | "Advanced Nonparametric Outlier Identification" — names PyOD as "a comprehensive library for anomaly detection" | 2025 | D3 | [Link](https://www.numberanalytics.com/blog/advanced-nonparametric-outlier-identification) |
| 36j | DrugAgent | bioengineer.org | Science news | "Agentic AI Sparks In Silico Team Science Boom" — syndication of Nature Biotech article, names DrugAgent | Feb 2026 | D4 | [Link](https://bioengineer.org/agentic-ai-sparks-in-silico-team-science-boom/) |
| 36k | FaceLock | So Essentially (Substack) | Tech blog | "Edit Anyway My Face Generates Away" by Dhruv Diddi — covers FaceLock algorithm, names USC. Yue Zhao not named directly (last author). | Nov 2024 | D5 | [Link](https://soessentially.substack.com/p/edit-anyway-my-face-generates-away) |
| 36l | ADBench | BAAI Community (智源社区) | Chinese AI research community | "NeurIPS 2022 \| ADBench: 最全面的异常检测基准!" — dedicated article covering ADBench's 100,000 experiments | Sep 2022 | D7 | [Link](https://hub.baai.ac.cn/view/20597) |
| 36m | ADBench | BAAI Community (智源社区) | Chinese AI research community | "我们真的可以相信过去20年的异常检测领域的进展吗?" — provocative framing of ADBench findings | Sep 2022 | D7 | [Link](https://hub.baai.ac.cn/view/20607) |
| 36n | PyGOD | Towards Data Science | Data science blog | "Graph Neural Networks with PyG on Node Classification, Link Prediction, and Anomaly Detection" by Tomonori Masui — uses PyGOD for anomaly detection, 84.1% AUC | Oct 2022 | D3 | [Link](https://medium.com/data-science/graph-neural-networks-with-pyg-on-node-classification-link-prediction-and-anomaly-detection-14aa38fe1275) |
| 36o | PyGOD/BOND | BAAI Community (智源社区) | Chinese AI research community | "NeurIPS 2022 \| BOND: Benchmarking Unsupervised Anomalous Node Detection" — names PyGOD as companion library | Nov 2022 | D7 | [Link](https://hub.baai.ac.cn/view/21552) |
| 36p | Anomaly-Detection-Resources | paulvanderlaken.com | Data science blog | "Anomaly Detection Resources" — dedicated feature, names "CMU PhD student Yue Zhao" | Dec 2019 | D3 | [Link](https://paulvanderlaken.com/2019/12/19/anomaly-detection-resources/) |
| 36q | Anomaly-Detection-Resources | R-bloggers | R community aggregator | Syndication of paulvanderlaken article — large data science readership | Dec 2019 | D3 | [Link](https://www.r-bloggers.com/2019/12/anomaly-detection-resources/) |
| 36r | CS-Paper-Checklist | HelloGitHub | Open-source discovery platform | Featured in Monthly Vol. 110 (#36 in "Other" section), 1.6k stars | May 2025 | D3 | [Link](https://hellogithub.com/en/periodical/volume/110) |
| 36s | CS-Paper-Checklist | Efficient Coder (高效码农) | Tech blog | "The Ultimate CS Paper Writing Checklist: Expert Tips for High-Impact Research" — links to repo | May 2025 | D3 | [Link](https://www.xugj520.cn/en/archives/computer-science-paper-checklist-2.html) |
| 36t | TrustGen | Vector Institute | ICLR 2026 research roundup | "Vector researchers advance representation learning and deep learning research at ICLR 2026" — names TrustGen and Yue Zhao | Apr 2026 | D3 | [Link](https://vectorinstitute.ai/vector-researchers-advance-representation-learning-and-deep-learning-research-at-iclr-2026/) |
| 36u | FigEdit ("Charts Are Not Images") | Adobe Research | Research listing | "Charts Are Not Images: On the Challenges of Scientific Chart Editing" — names the ICLR 2026 paper and Yue Zhao | Apr 2026 | D3 | [Link](https://research.adobe.com/publication/charts-are-not-images-on-the-challenges-of-scientific-chart-editing/) |
| 36w | DoxBench | Sina / 机器之心Pro syndication | Chinese tech media | "一张照片、一句简单提示词，被ChatGPT人肉开盒" -- 机器之心Pro original reporting via Sina, names "南加州大学教授赵越（Yue Zhao）团队", paper title "Doxing via the Lens", and arXiv:2504.19373 | Apr 2026 | D7 | [Link](https://k.sina.cn/article_3996876140_ee3b7d6c001014qs2.html) |
| 36y | Auditable Agents | Awesome Agents | AI news / science brief | "MedGemma 1.5, Smarter MCTS, and Auditing AI Agents" -- editorial section "Auditable Agents -- 617 Reasons to Pay Attention" links arXiv:2604.05485 and names co-authors Yi Nian and Aojie Yuan; Yue Zhao not named directly (passes direct-mention rule via co-authors) | Apr 2026 | D5 | [Link](https://awesomeagents.ai/science/medgemma-mcts-auditable-agents/) |
| 36aa | No Attacker Needed / UCC paper | Promptfoo, RAXE Labs, SecTools.tw, Gist.Science, Fugu-MT | Mixed-source security cluster (one row per cluster convention) | "Unintentional Cross-User Contamination in Shared-State LLM Agents", arXiv:2604.01350. Editorial: RAXE RADAR-2026-004 (full author list including Yue Zhao). Templated DB entry: Promptfoo Security DB (paper named, no authors). AI-generated / aggregator (also referenced; would otherwise belong in Ledger 3 if split): SecTools.tw archive 793 ("本文由 AI 產生、整理與撰寫" disclaimer), Gist.Science DE auto-translated mirror, Fugu-MT machine-translation page. | Apr 2026 | D5/D7 | [Promptfoo](https://www.promptfoo.dev/lm-security-db/vuln/benign-cross-user-contamination-6ea37d04) · [RAXE](https://raxe.ai/labs/radar/radar-2026-004) · [SecTools](https://sectools.tw/archives/793) · [Gist DE](https://gist.science/de/paper/2604.01350) · [Fugu-MT](https://fugumt.com/fugumt/paper_check/2604.01350v1) |
| 36ab | The Autonomy Tax | The Autonomy Review | Agent research briefing | "Your Agent Pays a Tax Every Time It Plays It Safe..." directly covers "The Autonomy Tax: Defense Training Breaks LLM Agents" and links arXiv:2603.19423. | Mar 2026 | D4 | [Link](https://www.theautonomyreview.com/your-agent-pays-a-tax-every-time-it-plays-it-safe-and-san-francisco-just-marched-on-the-industry-449b296b) |
| 36ac | PyOD / ADBench | Fora Soft | Industry playbook | "The Ultimate Guide to Machine Learning Algorithms for Anomaly Detection (2026 Playbook)" names PyOD V3, ADEngine, the od-expert workflow, and ADBench benchmark datasets. | Jun 2025 / Apr 2026 update | D2/D10 | [Link](https://www.forasoft.com/blog/article/machine-learning-algorithms-anomaly-detection) |
| 36ad | Aegis | The Weather Report | Agent-security blog | "A firewall that learns from clean agent traces..." benchmarks Praetor against Aegis and cites "AEGIS: No Tool Call Left Unchecked, A Pre-Execution Firewall and Audit Layer for AI Agents." | May 2026 | D4/D5 | [Link](https://theweatherreport.ai/posts/praetor-agent-firewall/) |
| 36ae | SUOD | Rubik's Code | AI research blog | "Top 3 Artificial Intelligence Research Papers - February 2020" includes a dedicated section on "SUOD: Toward Scalable Unsupervised Outlier Detection." | Mar 2020 | D2/D7 | [Link](https://rubikscode.net/2020/03/02/top-3-artificial-intelligence-research-papers-february-2020/) |
| 36aj | TrustLLM | EthicAI, JOBIRUN, WebProNews | Policy/news explainer cluster | Third-party explainers about FLI AI Safety Index name TrustLLM alongside HELM/AIR-Bench/CAIS safety evaluations; JOBIRUN gives a Japanese report explainer, EthicAI covers Winter 2025 safety failures, and WebProNews mentions TrustLLM via the AI Safety Index. | 2025-2026 | D7/D10 | [EthicAI](https://ethicai.net/frontier-ai-safety-failures) · [JOBIRUN](https://jobirun.com/fli-ai-safety-index-report-summer-2025-overview/) · [WebProNews](https://www.webpronews.com/ai-frameworks-under-siege-rce-flaws-and-malware-surge-threaten-40-of-dev-pipelines/) |
| 36ak | TrustLLM | **Samsung SDS Insights** | Korean enterprise editorial | "LLM 평가 방법론" — names TrustLLM as flagship LLM trustworthiness evaluation framework; reference list cites Huang, Yue, et al. "TrustLLM: Trustworthiness in Large Language Models" arXiv:2401.05561 (Yue Zhao co-author). | 2026 | D7 | [Link](https://www.samsungsds.com/kr/insights/llm-evaluations.html) |
| 36al | agent-style | PyShine | Developer blog | "Agent Style: 21 Writing Rules That Make AI Agents Write Like Tech Pros" -- direct external article naming Yue Zhao, linking github.com/yzhao062/agent-style, and describing Claude Code, Codex CLI, Copilot, Cursor, and other integrations. Rule 1+2+6 met; no AI disclaimer found. Codex May 13 Phase A, Claude Phase B verified 2026-05-13. | Apr 2026 | D2 | [Link](https://pyshine.com/Agent-Style-21-Writing-Rules-for-AI-Coding-Agents/) |
| 36am | PyOD | The Fintech Mag | Fintech industry guide | "152 Fintech AI Tools and Their Low-Cost Alternatives" -- verbatim: "PyOD, a popular open-source Python library for outlier detection. PyOD offers 50+ anomaly detection algorithms and has become a go-to toolkit for fraud analytics in Python." Rule 1 met; no AI disclaimer found, though the systematic 152-tool enumeration pattern suggests heavy structural templating; flag for re-evaluation if the same pattern recurs. Codex May 13 Phase A, Claude Phase B verified 2026-05-13. | 2026 | D2 | [Link](https://thefintechmag.com/152-fintech-ai-tools-and-their-low-cost-alternatives-why-youre-overpaying-and-how-to-stop/) |
**Count: 73 external third-party items (71 prior + 2 May 13 rows verified by Claude 2026-05-13; #36al PyShine, #36am Fintech Mag). Four May 13 wide-run candidates (Microsoft Research TrustLLM, thepaper.cn TrustLLM, aiproductivity.ai Aegis, jiqizhixin TrustLLM) were initially proposed as Ledger 2 additions but dropped after Codex Round 1 review caught them as exact-URL duplicates of existing rows #7, #5, #21, #34b respectively; they are recorded in `news-search-candidates.jsonl` as `duplicate_existing` and the underlying May 13 verification work serves as an evidence upgrade to those four existing rows rather than as new counted rows.**

*Re-classification on 2026-04-29 web verification: #36v USC Viterbi (USC at ICLR 2026 institutional PR) dropped from the count entirely — USC institutional PR for conference papers is treated as out of scope and is not tracked in any ledger; legacy USC rows #17, #18, #18b-e are kept in place pending a future cleanup pass. #36x SecTools.tw 713 (Auditable Agents) and #36z SecTools.tw 854 (Agent Audit) moved to Ledger 3 #66ci and #66cj after both pages were found to carry an explicit "本文由 AI 產生、整理與撰寫" (AI-generated) disclaimer.*

---

## Ledger 3: Ecosystem Adoption (books, podcasts, courses, enterprise integrations, patents, platforms)

External parties building on, integrating, or teaching your tools -- not coverage about you, but adoption evidence.

*Note: rows added in the Apr 24 and Apr 29 sweeps use compact platform-cluster units; each row counts as one verified item while the detail cell lists the platforms found in that cluster.*

| # | Work Named | Type | Detail |
|---|-----------|------|--------|
| 37 | PyOD | **Book** | "Outlier Detection in Python" by Brett Kennedy (Manning/O'Reilly) -- Ch. 6, 7, 14 on PyOD |
| 38 | PyOD | **Book** | "Handbook of Anomaly Detection" by Chris Kuo (Columbia) -- entire book on PyOD |
| 39 | COPOD | **Book** | "Finding Ghosts in Your Data" by Kevin Feasel (Apress/O'Reilly) -- Ch. 12 on COPOD |
| 40 | PyOD | **Podcast** | Talk Python To Me #497: Outlier Detection with Python |
| 41 | PyOD | **Podcast** | Real Python Podcast #208: Detecting Outliers |
| 42 | PyOD | **Enterprise** | Databricks -- built Kakapo framework integrating PyOD with MLflow/Hyperopt |
| 43 | PyOD | **Enterprise** | Databricks -- insider threat risk detection solution using PyOD |
| 44 | PyOD | **Enterprise** | Walmart -- deployed for real-time pricing (1M+ daily updates, KDD 2019) |
| 45 | PyOD | **Enterprise** | Altair AI Studio -- industry whitepaper using PyOD's Isolation Forest for anomaly detection |
| 46 | PyOD | **Patent** | WO2023166515A1 (Ericsson) -- cites PyOD (Zhao et al., JMLR 2019) |
| 47 | PyOD | **Evaluation** | ESA OPS-SAT benchmark (promoted to Ledger 1 / Tier 0 as government agency citation). |
| 48 | PyOD | **Course** | DataCamp "Anomaly Detection in Python" -- dedicated PyOD chapter, 19.28M platform learners |
| 49 | PyOD | **Course** | Udemy "Anomaly Detection: ML, DL, AutoML" -- includes "PyOD: A comparison of 10 algorithms" lecture |
| 50 | PyOD | **Course** | Udemy "Certified Anomaly Detection & Outlier Analytics" -- uses PyOD alongside Scikit-learn |
| 51 | PyOD | **Course** | O'Reilly Video Edition -- "Outlier Detection in Python" with dedicated PyOD chapters |
| 52 | PyOD | **Platform** | Papers with Code -- author profile + PyOD/ADBench listed with results |
| 53 | PyOD | **Platform** | Kaggle -- 7+ dedicated notebooks |
| 60 | TrustLLM | **Platform** | Zhihu -- Chinese-language TrustLLM coverage |
| 61 | DoxBench | **Platform** | HuggingFace dataset + public leaderboard |
| 62 | TDC | **Platform** | HuggingFace organization page |
| 63 | Diffusion Survey | **Citations** | 1,846 Semantic Scholar citations, ACM Computing Surveys 2023 |
| 64 | COPOD/ECOD | **Academic** | "Two-phase Dual COPOD Method for Anomaly Detection in ICS" (arXiv 2305.00982) -- uses COPOD, ECOD, PyOD for critical infrastructure security |
| 65 | COPOD/ECOD | **Academic** | "Data-driven digital forensics: anomaly detection in Mozilla Firefox" (CEUR-WS Vol-4092) -- COPOD and ECOD as "most efficacious" methods |
| 66a | PyOD | **Course** | Manning liveProject "Using PyOD and Ensemble Methods" -- hands-on project teaching AD with PyOD |
| 66b | PyOD | **Platform** | GeeksforGeeks "Introduction to Anomaly Detection with Python" -- full PyOD walkthrough tutorial (Jul 2025) |
| 66c | PyOD | **Tutorial** | Generalist Programmer "Pyod: Python Package Guide 2025" -- standalone guide (Nov 2025) |
| 66d | PyOD 2 | **Tutorial** | Medium / Kuldeepkumawat -- "PyOD 2: Outlier Detection Powered by LLMs" (Mar 2025) |
| 66e | PyOD | **Book** | "Advanced Techniques for Anomaly Detection: Beyond the Basics" (Routledge/CRC Press, 2025) -- lists PyOD |
| 66f | PyOD | **Book** | "Anomaly Detection: Recent Advances, AI and ML Perspectives" (IntechOpen, 2024) -- lists PyOD |
| 66g | ECOD/LUNAR | **Book chapter** | Springer LNNS vol. 1445, "Novel Outlier Detection Using ECOD, LUNAR and Logistic Regression" (2026) |
| 66h | PyOD/SUOD | **Enterprise** | IQVIA -- healthcare fraud detection deployment on 123K+ pharmacy claims using PyOD/SUOD models |
| 66i | ADBench | **Benchmark** | Text-ADBench (arXiv Jul 2025, Jicong Fan et al.) -- external follow-on benchmark inspired by ADBench |
| 66j | TrustLLM | **Platform** | 腾讯云开发者社区 (Tencent Cloud Developer) -- Chinese TrustLLM coverage |
| 66k | COPOD/ECOD | **Patent** | EP4339817A1 (EU) -- cites COPOD |
| 66l | COPOD/ECOD | **Patent** | US20250217974A1 (US) -- cites COPOD and ECOD |
| 66m | PyOD | **Patent** | EP4662606A1 (EU) -- cites PyOD |
| 66n | PyOD | **Patent** | CN111666198A (China) -- cites PyOD |
| 66o | COPOD | **Patent** | CN112328424A (China) -- cites COPOD |
| 66p | PyOD/COPOD/ECOD | **Enterprise** | Ericsson research paper (arXiv 2308.10504) -- tests COPOD and ECOD, calls them "empirically best performing" |
| 66v | TrustLLM | **Platform** | Chinese: 专知 (Zhuanzhi) TrustLLM coverage |
| 66al | agent-audit | **Platform** | Hacker News Show HN submission (item 46918149) — "Agent Audit: Open-source security scanner for AI agents" |
| 66am | ADBench | **Platform** | Zhihu: "异常检测--ADBench (NeurIPS'22) is ALL You Need" technical review |
| 66an | ADBench | **Platform** | Zhihu: "异常检测基准 Anomaly detection benchmark" overview |
| 66ao | ADBench | **Platform** | CSDN: benchmark/dataset/baseline collection listing ADBench |
| 66ap | ADBench | **Platform** | CSDN: "赵越-图神经网络与异常检测" GNN talk coverage naming Yue Zhao |
| 66ar | ADBench | **Platform** | Kaggle notebook "anomaly detection using Adbench datasets" by valeriemokeira (Jan 2025) |
| 66at | DPU | **Platform** | GitHub Awesome-Out-Of-Distribution-Detection curated list (CVPR 2025 entry) |
| 66av | Treble | **Platform** | GitHub curated lists: Awesome-MLLM-Hallucination + Awesome-LVLM-Hallucination |
| 66ax | Political-LLM | **Recognition** | SSRN Top Download Paper for Decision Science (1,327 downloads, 5,137 abstract views) |
| 66az | Computing Resources | **Policy** | CVPR 2026 Compute Reporting Form — official policy pilot addressing same compute-transparency gap the paper quantified; discussed on LinkedIn by program chair Vladimir Pavlovic ([post](https://www.linkedin.com/posts/vladimir-pavlovic-a5528412_cvpr-2026-compute-reporting-form-author-activity-7384957217147457536-kd1X)), Sasha Luccioni ([post](https://www.linkedin.com/posts/sashaluccioniphd_cvpr-2026-compute-reporting-form-author-activity-7385993803515744256-uqM-)) |
| 66bi | Anomaly-Detection-Resources | **Platform** | Zhihu: third-party recommendation article linking to repo |
| 66bj | Anomaly-Detection-Resources | **Platform** | CSDN x2: human-written survey referencing repo + PyOD tutorial linking resources |
| 66bk | CS-Paper-Checklist | **Platform** | CSDN: dedicated article "提升计算机科学论文质量的实用指南" |
| 66bl | CS-Paper-Checklist | **Platform** | Scholar's Corner (lujie.ac.cn): listed under "Academic Writing Tips" with direct repo link |
| 66bp | Aegis | **Platform** | Hugging Face Papers, Gist.Science, ResearchTrend.AI, PULRC Portal, DeepDyve, alphaXiv, Cool Papers, Skillget, Hacker News Show HN, and a ResearchGate auto-mirror (publication 402147498, arXiv:2603.12621; added 2026-05-28, Tier 3 aggregator cap) name AEGIS and the tool-call firewall paper. |
| 66br | TrustGen | **Platform** | BAAI Community, CSDN, and the ICLR 2026 venue-official poster page (iclr.cc/virtual/2026/poster/10010583; added 2026-05-28) name TrustGen, Yue Zhao, the project page, arXiv link, and GitHub repo. |
| 66bs | PyOD / PyOD 3 | **Platform** | SourceForge mirror, newreleases.io v3.0.0 release tracker, AitFind project page, LibHunt alternatives, DeepWiki docs, and OSSInsight comparison pages name PyOD/PyOD 3. |
| 66bt | agent-audit | **Platform** | Skillget listing, ClawHub Agent Audit Scanner listing, SoftwareSeni awesome-ai-agents list, MCP Market server/skill listings, PyPI, piwheels, and Safety DB name agent-audit as an AI-agent/MCP security scanner. |
| 66bu | agent-style / anywhere-agents | **Platform** | [Replicate Hype](https://hype.replicate.dev/?filter=past_week&sources=GitHub%2CHuggingFace%2CReddit%2CReplicate) Apr 22 trending page lists `yzhao062/agent-style` and `yzhao062/anywhere-agents`; ToolHunter later published an external tool directory/review for `agent-style`; package registries and docs remain first-party or registry-only. |
| 66by | AD-LLM / NLP-ADBench | **Platform** | alphaXiv, Bytez, Moonlight, ChatPaper, ResearchTrend.AI, J-GLOBAL, Hugging Face Papers, SelectDataset, PromptLayer, Papers With Code, BAAI Community, aimodels.fyi, and the ACL Anthology venue-official EMNLP Findings 2025 proceedings page for NLP-ADBench (aclanthology.org/2025.findings-emnlp.133; added 2026-05-28) name AD-LLM and/or NLP-ADBench. |
| 66ca | Tool long tail | **Platform** | ADBench on Ecosyste.ms and Liner; TODS on Datahut, Context7, and Ecosyste.ms; TDC on AIPOCH; PyGOD on Cloudsmith, fxis.ai, Open Source Security Atlas, and Reddit r/MachineLearning; SUOD on Beeks/piwheels; combo on PythonFix, PyPIStats, Pepy, and conda-forge; TrustEval-toolkit on GitCode. |
| 66cb | ADBench | **Consulting** | [Deloitte Germany AIxAML PDF](https://www.deloitte.com/content/dam/assets-zone2/de/de/docs/services/consulting/2025/Deloitte-Compliance-AIxAML.pdf) cites Han et al. (2022), ADBench, as the source of an anomaly-detection figure in an anti-money-laundering transaction-monitoring solution. |
| 66cc | PyOD / TODS | **EU project** | SEDIMARK D3.1 (Energy efficient AI-based toolset for improving data quality, p.18) names PyOD and TODS as the Python libraries used for the SEDIMARK toolbox's outlier-detection module ("Outlier detection, implemented using python and building on libraries such as PyOD, tods, pythresh, pandas, scikit-learn, and river"); D5.2 also names the same libraries. EU Horizon Europe data-space project. |
| 66cd | PyOD | **Patent** | Actimize patent US20230267468A1 names Python Outlier Detection (PyOD) as a package usable for fraud/anomalous-transaction ML models. |
| 66ce | PyOD | **Tutorial / integration** | Code and Compile HiveMQ Edge-to-Cloud AI Pipeline uses PyOD `IForest`; PyCaret DeepWiki documents PyOD integration; Precision Federal, Ciencia de Datos, ProgmaticTech, and PyCon US 2026 tutorial pages also name or use PyOD. |
| 66cf | CS-Paper-Checklist | **Education / academic writing** | Stanford BIOMEDIN-212 scientific-writing slides link `yzhao062/cs-paper-checklist`; Sayed Mohsin Reza's May 2025 blog credits Dr. Yue Zhao and links the repo; SourcePulse also lists the project. |
| 66ck | LangSkills | **Academic / platform** | "Recipes for Agents: Understanding Skills and Their Open Questions" cites `LabRAI/LangSkills` as reference [32]; Safety DB and piwheels also list `langskills-rai`. |
| 66cl | PyOD / LSCP | **Patent** | US20230017157A1 (Flowhow / Ben-Gurion University medical-device protection) says 11 unsupervised anomaly detection algorithms were used, some implemented by the PyOD toolbox, and names LSCP among ensemble methods. |
| 66cm | PyOD / COPOD | **Patent** | WO2023192130A1 (Dun & Bradstreet semantic directions / entity targeting) names the open-source PyOD library, the `yzhao062/pyod` GitHub URL, LOF, COPOD, and the JMLR PyOD citation. |
| 66cn | PyOD | **Patent** | US12074893B2 (Visa user network activity anomaly detection; same family as US11711391B2 / WO2022082091A1) cites "PyOD: A Python Toolbox for Scalable Outlier Detection" in non-patent literature. |
| 66co | LSCP | **Patent** | CN111880983A/B (CAN bus anomaly detection, Beijing Topsec) cites Yue Zhao et al., "LSCP: Locally Selective Combination in Parallel Outlier Ensembles", as non-patent literature. |
| 66cp | PyOD / ECOD / COPOD | **Finance research / applied deployment** | Springer Nature Discover Data article "A hybrid framework of anomaly detection for mutual fund parent companies" uses four PyOD algorithms (KNN, ECOD, COPOD, IForest) in a Morningstar-linked mutual-fund parent-company anomaly-detection workflow. |
| 66cq | PyOD | **Audit workflow** | Syntora "Integrate AI Anomaly Detection into Your Audit Workflow" says its ledger anomaly-detection service would build a Python service using PyOD for Isolation Forest modeling. |
| 66cr | TrustLLM | **Academic citation cluster** | 2025-2026 downstream papers in npj Artificial Intelligence, Requirements Engineering, Engineering Applications of Artificial Intelligence, and npj Digital Medicine cite or discuss TrustLLM in trustworthiness / healthcare AI contexts. |
| 66cs | DoxBench | **Follow-on research / AI-assisted news** | ReasonBreak / "Disrupting Hierarchical Reasoning" evaluates on DoxBench for geographic privacy protection; AI CERTs News also names DoxBench and GeoMiner in a ChatGPT location-risk article, with an explicit AI-generated/assisted disclaimer. |
| 66cu | PyOD / PyOD 2 | **Scientific uptake** | ACS Analytical Chemistry article "Unsupervised Machine Learning for Differential Analysis in Proteomics" uses PyOD version 2; the 2026 ACS comment on that paper says the reviewed UMLAD algorithms primarily come from PyOD 2 and cites the PyOD 2 WWW Companion paper. |
| 66cv | PyOD | **Education / training** | Additional course and syllabus pages from Python Charmers, Datastat, RX-M, and WUNU name PyOD or PyOD docs in anomaly-detection training contexts. |
| 66cw | TDC | **Education / platform** | Harvard AIM2 course project page, IntuitionLabs biotech evaluation guide, Hugging Face TDC mirror, and Emergent Mind topic page name Therapeutics Data Commons (TDC) as a dataset/benchmark resource. |
| 66cz | ADMoE | **Institutional research listing** | Microsoft Research Redmond page lists "ADMoE: Anomaly Detection with Mixture-of-Experts from Noisy Labels", Yue Zhao, Microsoft co-authors, AAAI 2023, and the proprietary enterprise security dataset result. Demoted from initial Ledger 2 placement because it is a coauthor-institution publication listing. |
| 66da | AutoAudit | **Institutional research listing** | CMU Tepper Accounting AI Lab page lists "AutoAudit: Mining Accounting and Time-Evolving Graphs", Yue Zhao, and applied audit/accounting framing. Demoted from initial Ledger 2 placement because it is a coauthor-institution publication listing. |
| 66db | LLM-based Conversational User Simulation | **Institutional research listing** | Adobe Research page lists the EACL 2026 survey, publication date Mar 29 2026, Yue Zhao among authors, and intelligent-agents/NLP research areas. Demoted from initial Ledger 2 placement because it is a coauthor-institution publication listing. |
| 66dc | PersonaConvBench | **Institutional research listing** | Adobe Research page lists the NeurIPS 2025 MTI-LLM workshop paper, Yue Zhao among authors, and "Spotlight paper (top 5%)." Demoted from initial Ledger 2 placement because it is a coauthor-institution publication listing. |
| 66dd | CDCR-SFT | **External newsletter** | gatodo (Christopher Berry) "Bowling Shoe Agents" newsletter (Nov 25, 2025) — dedicated section "Mitigating Hallucinations in Large Language Models via Causal Reasoning" naming the paper title, CDCR-SFT, and the 95.33% CLADDER state-of-the-art result. [Link](https://www.gatodo.com/bowling-shoe-agents/) |
| 66de | PyOD | **Enterprise / open-source platform integration** | **Apache Software Foundation / apache/beam** (8.5K+ stars). First-class PyOD ModelHandler in `sdks/python/apache_beam/ml/anomaly/detectors/pyod_adapter.py` (`from pyod.models.base import BaseDetector as PyODBaseDetector`), accompanying `pyod_adapter_test.py`, example notebook `anomaly_detection_iforest.ipynb`, and YAML log_analysis pipeline. Apache Beam underlies Google Cloud Dataflow. [Link](https://github.com/apache/beam) |
| 66df | PyOD | **Enterprise / production analytics integration** | **PostHog / posthog** (34K+ stars, YC unicorn product analytics). Production alerting subsystem at `posthog/tasks/alerts/detectors/pyod_detectors/` with `BasePyODDetector` wrapper class and eight algorithm wrappers (KNN, IForest, COPOD, ECOD, OCSVM, LOF, PCA, HBOS) wrapping PyOD models for live-traffic alerting; the directory's other two files are `__init__.py` and `base_pyod.py`. [Link](https://github.com/PostHog/posthog) |
| 66dg | PyOD | **Official docs / community flavor** | **MLflow / mlflow** (25.8K+ stars, official AI engineering platform). MLflow Community Flavors documentation lists PyOD as canonical anomaly-detection flavor with worked KNN-detector code example via `mlflavors`; cross-listed across versions 2.4.x through 3.11. [Link](https://github.com/mlflow/mlflow/blob/master/docs/docs/classic-ml/community-model-flavors/index.mdx) |
| 66dh | PyOD / ADBench | **Pharma code adoption** | **Genentech (Roche) / data-detective** — modular validation framework for heterogeneous multimodal data on Genentech's official GitHub org. Dedicated `adbench_validator_method_factory.py`, `adbench_multimodal`, and `adbench_ood_inference` factories import from `pyod.models...` for drug-discovery data validation. Yue Zhao not among Genentech repo authors — true external T2 pharma adoption. [Link](https://github.com/Genentech/data-detective) |
| 66di | PyOD | **Aggregate code adoption** | **GitHub Dependents snapshot 2026-05-07:** 5,493 public repositories and 139 packages depend on `yzhao062/pyod` per the official GitHub Dependents network graph. Quantitative ecosystem-scale signal; sampled per-organization adopters above (Apache Beam, PostHog, MLflow, Genentech) were drawn from this leaderboard. Re-snapshot quarterly. [Link](https://github.com/yzhao062/pyod/network/dependents) |
| 66dj | PyOD | **Enterprise product docs** | Oracle Financial Services FCCM Automated Scenario Calibration docs have a dedicated `pyod` license subpage with the verbatim BSD 2-Clause `Copyright (c) 2018, Yue Zhao` notice. Codex May 13 Phase A draft also pointed at an Oracle IoT licensing URL (`/iot-asset-cloud/licensing-guide/index.html`) but that URL returned HTTP 404 on Claude Phase B verification 2026-05-13 and was dropped from this row. Codex May 13 Phase A, Claude Phase B verified 2026-05-13. [FCCM pyod](https://docs.oracle.com/en/industries/financial-services/ofs-analytical-applications/auto-scenario-calibration/25.03.01/ascli/pyod.html) |
| 66dk | TrustLLM | **Security education / benchmark resource** | RedTeams AI "AI Safety Benchmarks and Evaluation" names TrustLLM in a "Major Safety Benchmarks" table alongside HarmBench, SafetyBench, AdvBench, JailbreakBench, and MLCommons AI Safety. Editorial article with analysis, no AI disclaimer. Codex May 13 Phase A, Claude Phase B verified 2026-05-13. [Link](https://redteams.ai/topics/governance-compliance/evaluation) |
| 66dl | PyOD | **Integration docs** | PySAD documentation and PyPI page state verbatim: "PySAD also provides integrations for batch anomaly detectors of the PyOD"; both link `yzhao062/pyod`. Rule 1+6 met. Codex May 13 Phase A, Claude Phase B verified 2026-05-13. [Docs](https://pysad.readthedocs.io/) · [PyPI](https://pypi.org/project/pysad/0.3.1/) |
| 66dn | CDCR-SFT | **Templated daily-brief (AI-generated cap)** | "Mitigating Hallucinations in Large Language Models via Causal Reasoning" / CDCR-SFT / 95.33% CLADDER accuracy named in Growth Japan Technologies Japanese daily-brief ("ほぼテク" templated brief). Page carries verbatim AI-generated disclaimer "※）生成AIは、場合によって事実と異なる内容を含む可能性があります"; per `disclaimer-patterns.md`, `ai_generated` is capped at Tier 3. Moved from Codex Ledger 2 Phase A draft (originally proposed #36an) to Ledger 3 by Claude Phase B verification 2026-05-13. Complements the gatodo newsletter CDCR-SFT coverage already counted in Ledger 3 #66dd. [Link](https://www.growth-japan.com/blog/it-daily-brief-2026-0309) |
| 66do | TrustLLM | **2026 mainstream-venue academic citation cluster** | Six 2026 papers in Tier 1 venues cite TrustLLM (arXiv:2401.05561): ACS Environmental Science & Technology (Cheng et al., Apr 9 2026 -- LLM contaminants prioritization, doi:10.1021/acs.est.6c01342); Springer Requirements Engineering (Axetorn et al., Mar 16 2026 -- multi-agent LLM chatbot trust requirements, doi:10.1007/s00766-026-00457-w); ACM/IEEE HRI 2026 Companion (Seaborn & Yalcin, Mar 12 2026 -- Robotic Sycophancy scoping review, doi:10.1145/3776734.3794532); Wiley Thunderbird International Business Review (Shrivastav et al., Feb 12 2026, doi:10.1002/tie.70099); Springer CCIS (Danielienė et al., Jan 2026 -- Gen-AI for CISO tasks, doi:10.1007/978-3-032-16808-5_33); **ACM Computing Surveys** "Towards Trustworthy AI: A Review of Ethical and Robust Large Language Models" (doi:10.1145/3777382), a Tier 0-equivalent CS survey venue. Plus Springer Frontiers of Computer Science (s11704-025-50442-9) explicitly names TrustLLM in body. First six confirmed via OpenAlex citation graph 2026-05-13 (publisher pages variously 403-gated); ACM CSUR confirmed via user manual verification 2026-05-13. (2026, D6) [OpenAlex](https://api.openalex.org/works?filter=referenced_works%3AW4390833061) · [ACM CSUR](https://dl.acm.org/doi/10.1145/3777382) |
| 66dp | Aegis | **Third-party implementation citing FORTIS paper** | Justin0504/Aegis GitHub repo "Runtime policy enforcement for AI agents. Cryptographic audit trail, human-in-the-loop approvals, kill switch. Zero code changes." README cites the FORTIS paper verbatim: "AEGIS: No Tool Call Left Unchecked -- A Pre-Execution Firewall and Audit Layer for AI Agents. Aojie Yuan, Zhiyuan Su, Yue Zhao. arXiv:2603.12621, 2026." Third-party implementation building on the USC work, distinct from the canonical FORTIS repo. Rule 1+3 met. Claude Phase B verified 2026-05-13. (2026, D7) [Link](https://github.com/Justin0504/Aegis) |
| 66dt | PyOD 2 | **mala-lab Awesome Anomaly Detection Foundation Models** | Curated awesome list `mala-lab/Awesome-Anomaly-Detection-Foundation-Models` (TKDE survey companion) names PyOD 2 explicitly with verbatim entry `[Chen2025] PyOD 2: A Python Library for Outlier Detection with LLM-powered Model Selection in Arxiv, 2025. [paper](https://arxiv.org/abs/2412.12154) [code](https://github.com/yzhao062/pyod)`. Rule 1+6 met. Claude Phase B verified 2026-05-13. (2025, D7) [Link](https://github.com/mala-lab/Awesome-Anomaly-Detection-Foundation-Models) |
| 66dv | PyOD / anomaly detection | **Datawhale WeChat public-account lecture writeup** | "异常检测算法应用与实践_CMU赵越" -- Datawhale-organized online lecture by Yue Zhao (then-CMU affiliation) covering anomaly detection algorithms, applications, and practice. Datawhale is a major Chinese open-source ML / data-science community. Lecture writeup published via WeChat public account; sister-evidence to the Bilibili recording of the same talk. WeChat verification gate blocked WebFetch; user manually verified 2026-05-13 that the page names Yue Zhao and the PyOD anomaly-detection material. Treat as podcast / lecture-equivalent signal, similar shape to Talk Python To Me #497 (#40) and Real Python #208 (#41). Claude Phase B + user manual verification 2026-05-13. (2021-2022, D7) [Link](https://mp.weixin.qq.com/s/BwMe9l9yEGSYgATbvcK97w) |

*Tier-5 aggregator paper-pages, non-English how-to tutorials, and SecTools.tw AI-generated rows bucketed 2026-06-02 (presentation only; item counts preserved and still in the Ledger 3 total of 169; full per-row detail recoverable from git):*

- Aggregator paper-pages (Tier 5), one bucketed line per work (32 items total):
  - DoxBench -- aggregator paper-pages (Liner, Moonlight, Zhuanzhi, haebom, Gist.Science, ChatPaper, Hugging Face Papers) (2 items)
  - AD-AGENT -- aggregator paper-pages (Moonlight, aimodels.fyi, PT-Edge) (1 item)
  - MetaOOD -- aggregator paper-pages (Liner, aimodels.fyi) (1 item)
  - JailDAM -- aggregator paper-pages (aimodels.fyi, Bohrium) (1 item)
  - DPU -- aggregator paper-pages (Moonlight, paperreading.club) (1 item)
  - ICLR 2026 highlights (DoxBench, TrustGen, DecAlign, FigEdit) -- aggregator paper-pages (Paper Digest) (1 item)
  - Can MLLMs do TSAD? -- aggregator paper-pages (alphaXiv, Emergent Mind, Moonlight, aimodels.fyi) (2 items)
  - DyFlow -- aggregator paper-pages (Moonlight, ChatPaper, alphaXiv) (1 item)
  - FaceLock -- aggregator paper-pages (Liner, Moonlight) (1 item)
  - CoAct -- aggregator paper-pages (Moonlight, aimodels.fyi, Bytez, OpenTrain/HFEPX, DeepDyve) (1 item)
  - Agent Banana -- aggregator paper-pages (Moonlight) (1 item)
  - StealthRank -- aggregator paper-pages (Moonlight) (1 item)
  - Defenses Against Prompt Attacks -- aggregator paper-pages (alphaXiv, Bytez, Moonlight, ResearchTrend.AI, J-GLOBAL, AI Security News/Portal) (2 items)
  - Multimodal GEO -- aggregator paper-pages (Emergent Mind) (1 item)
  - ADBench -- aggregator paper-pages (Emergent Mind, alphaXiv) (2 items)
  - Political-LLM -- aggregator paper-pages (alphaXiv, aimodels.fyi) (1 item)
  - Computing Resources -- aggregator paper-pages (Hugging Face Papers) (1 item)
  - Treble -- aggregator paper-pages (Moonlight, alphaXiv) (1 item)
  - Cat-DPO -- aggregator paper-pages (alphaXiv, Bytez, Gist.Science, Moonlight, ResearchTrend.AI, haebom) (1 item)
  - Topology Matters -- aggregator paper-pages (alphaXiv, Bytez, Moonlight, aimodels.fyi, ChatPaper, ResearchTrend.AI, haebom) (1 item)
  - Auditable Agents -- aggregator paper-pages (alphaXiv, Bytez, Gist.Science, ResearchTrend.AI, Code of Paper, haebom) (1 item)
  - PersonaConvBench -- aggregator paper-pages (alphaXiv, Hugging Face Papers, Bytez, Moonlight, aimodels.fyi, ResearchTrend.AI) (1 item)
  - Mitigating Hallucinations via Causal Reasoning -- aggregator paper-pages (alphaXiv, Bytez, aimodels.fyi, ChatPaper, ResearchTrend.AI, J-GLOBAL, haebom) (1 item)
  - Secure On-Device Video OOD / SocialMaze / MGEO -- aggregator paper-pages (alphaXiv, Bytez, Moonlight, aimodels.fyi, ChatPaper, ResearchTrend.AI, Hugging Face dataset) (1 item)
  - The Autonomy Tax / Sovereign-OS -- aggregator paper-pages (Gist.Science, ResearchTrend.AI, DeepDyve) (1 item)
  - IET / Fairness or Fluency? / Someone Hid It -- aggregator paper-pages (Cool Papers, ChatPaper, GoatStack, ResearchTrend.AI) (1 item)
  - 2025-2026 paper long tail (DyFlow, M3OOD, ClimateLLM, Mole-PAIR, model-extraction surveys, CDCR-SFT, hurricane loss) -- aggregator paper-pages (Deep Paper, OSLLM.ai, Moonlight, aimodels.fyi, Cool Papers, Emergent Mind) (1 item)
  - May 13 multi-work cluster (TrustLLM, DoxBench, Auditable Agents, AEGIS, Agent Audit) -- aggregator paper-pages (Hugging Face Papers, alphaXiv, papers.cool) (1 item)
- Non-English tutorial adoption (PyOD/PyGOD/TODS/combo): Chinese x15, Japanese x4, Russian x1, German x1, Spanish x1, Korean x1 (23 items).
- AI-generated aggregator (Tier-3 capped): 3 near-identical SecTools.tw pages (Auditable Agents archive 713, Agent Audit archive 854, The Autonomy Tax archive 729) (3 items).

*Note: Nature Scientific Reports x3 ADBench scientific-uptake cluster (s41598-025-88050-z, s41598-024-72982-z, s41598-025-28976-6) demoted back to candidate pool in Codex Round 2 because the rows rested on WebSearch-snippet confirmation only; full-text fetch was Nature-IDP gated. Per the "snippet alone is not verified evidence" rule, awaiting direct article fetch before re-promotion.*

**Count: 169 ecosystem adoption items (154 main-ledger rows through May 13, +7 May 19 append-only verified rows, +4 May 20 append-only verified rows, +4 May 28 append-only verified rows).** (2026-06-13 sweep added 0: all candidates re-surfaced already-tracked rows; see the "## 2026-06-13 Refresh" section.)

---

## Ledger 4: First-Party & Community

Items authored by you, your students, or posted by your team. Useful context but not independent external coverage.

| # | Work | Type | Detail |
|---|------|------|--------|
| 66 | Aegis | DEV Community | Blog post by first author Aojie Yuan |
| 67 | agent-audit | GitHub Discussion | Scan results posted on OpenClaw repo by your team |
| 68 | AD-AGENT | Medium | Blog post by Yue Zhao |
| 69 | PyOD | Metrics | 39.11M+ downloads (pepy.tech), 9,770+ stars, 114 dependent packages, 58 contributors |
| 70 | -- | Encyclopedia | Grokipedia entry |
| 71 | Yue Zhao | Amazon Science | Author page on Amazon Science platform |

**Count: 19 first-party/community items (6 main-ledger rows plus 13 May 19 append-only verified rows).**

---

## Ledger 5: Awards & Recognitions

| # | Award | Year |
|---|-------|------|
| 72 | Amazon Research Award (AI for InfoSec) | Mar 2026 |
| 73 | Amazon Research Award (graph AD) | Dec 2024 |
| 74 | NVIDIA Academic Grant | Mar 2026 |
| 75 | Anthropic Claude for Open Source | Mar 2026 |
| 76 | NSF POSE Award #2346158 | 2024-2027 |
| 77 | ICDM BlueSky CCC 2nd Prize | Dec 2025 |
| 78 | SIGSPATIAL Best Short Paper | Nov 2025 |
| 79 | DPU -- CVPR Highlight (~3%) | 2025 |
| 80 | MultiOOD -- NeurIPS Spotlight (~2%) | 2024 |
| 81 | PersonaConvBench -- NeurIPS WS Spotlight | 2025 |
| 82 | Shawn Li -- Amazon ML Fellow | 2025-2026 |
| 83 | Capital One Research Award | 2024 |
| 84 | Google Cloud Research Innovators | 2024 |
| 85 | Norton Labs Fellowship | -- |
| 86 | Meta AI4AI Research Award | -- |
| 87 | CMU Presidential Fellowship | -- |
| 88 | AAAI New Faculty Highlights | 2024 |
| 89 | TDC -- Nature Chemical Biology | 2022 |
| 90 | PyOD — Wikipedia (en) "Anomaly detection" Software section names PyOD; reference list cites Zhao, Nasrullah, Li 2019 JMLR. [Link](https://en.wikipedia.org/wiki/Anomaly_detection) | continuous |

**Count: 20 awards/recognitions/encyclopedia entries (19 main-ledger rows plus the May 19 ACM SIGSPATIAL award-index row).**

---

## Upcoming Visibility Opportunities

1. **ICLR 2026** (Apr 24-28): DoxBench, FigEdit, DecAlign, TrustGen. DoxBench strongest outreach candidate.
2. **机器之心 ICLR 2026 Paper Sharing** (Apr 18, Beijing): DoxBench has readable Sina/机器之心Pro syndication recorded in #36w; continue watching for FigEdit/TrustGen.
3. **USC Viterbi "USC at ICLR 2026"** -- published Apr 23, not tracked (USC institutional PR for conference papers is out of scope).
4. **ACM AI and Agentic Systems** (May 26-29): agent-audit presentation.
5. **Agent Skills '26** (May 26, 2026 at ACM CAIS): organizer page names Yue Zhao / USC; watch for coverage of the 3,984-skills audit talk.
6. **ACL 2026** (Jul 2-7): CoAct, Defenses Against Prompt Attacks, Topology Matters.
7. **Adobe Research blog**: FigEdit research listing resolved in #36u; watch for a broader ICLR roundup.

---

## Negative Results

| Outlet Type | Searched | Result |
|-------------|----------|--------|
| Major business press | Forbes, Fortune, Bloomberg, WSJ, Reuters, FT | No hits |
| Top-tier tech press (except Tom's Hardware) | VentureBeat, TechCrunch, Wired, MIT Tech Review, IEEE Spectrum, The Verge, Ars Technica | No hits |
| Security press | Dark Reading, SecurityWeek, SC Magazine, Bleeping Computer, Krebs, The Record, CSO Online, CyberNews | No hits by name in these major outlets |
| Security blogs / databases | SecTools.tw, RAXE Labs, Promptfoo LLM Security DB, AI Security News, AI Security Portal | New direct hits for Auditable Agents, Agent Audit, No Attacker Needed, and Defenses Against Prompt Attacks recorded above |
| AI newsletters | The Batch, Import AI, The Gradient, Synced Review, Awesome Agents | Awesome Agents covered Auditable Agents; the other newsletter sources had no hits |
| Industry analysts | Gartner, Forrester, IDC | No hits by name. Forrester "AEGIS" is their own framework (name collision). |
| Consulting firms | McKinsey, Deloitte, PwC, Accenture, EY, KPMG | **Deloitte Germany AIxAML cites ADBench**. Other firm sources remain topic coverage only. |
| Think tanks | Stanford HAI, CSET, CAIS, Brookings, RAND, WEF, OECD, Turing | Topic coverage only |
| Foundation model system cards | OpenAI (8), Anthropic (5), Meta, Google, DeepSeek (2), Qwen, Phi-4, Cohere, Gemma, Yi; Apr 24 and Apr 29 re-checks included OpenAI GPT-5.5 / GPT-5.4 Thinking, Anthropic, DeepMind Gemini 3/3.1, Meta Llama, and Microsoft Phi candidates | No citations |
| Foundation model system cards / jobs (May 7) | OpenAI GPT-5.2/GPT-5.1/GPT-5/GPT-5.1-Codex-Max/ChatGPT Agent/o3/o4-mini/Deep Research/o1/gpt-oss; Anthropic Claude Mythos/Opus 4.6/Sonnet 4.6; DeepMind Gemini 3.1/Flash Image/Flash Audio/Flash-Lite; Meta, Mistral, xAI, Cohere exact searches | No new system-card citations. OpenAI Careers "Technical Intelligence Analyst" names PyOD and is recorded in Ledger 1 #8g (foundation-model-company official content). Earlier third-party mirrors of the Quantitative Threat Forecasting Analyst role naming PyOD 2.0 remain candidate-only unless an official OpenAI URL resurfaces. |
| Government (beyond Senate) | White House (3), NIST AI 600-1, GAO, Congress.gov, NSF.gov, OSTI.gov | No citations by name |
| International government | EU AI Office, ENISA, UK gov, OECD iLibrary, UNESCO, G7/G20 | **International AI Safety Report 2026 cites TrustLLM** (citation #881). Other sources: no citations by name. |
| **Regulated verticals (D8)** | OCC, FDIC, FINRA, SEC, CFTC (finance); FDA (healthcare); NASA, FAA (aerospace); CISA (cybersecurity); DARPA, MITRE, DOE (defense); telecom; insurance; security vendors (Splunk, Elastic, CrowdStrike, Palo Alto, Fortinet); Oracle financial-services product docs | **Deloitte Germany AIxAML cites ADBench**, LLNL/DOE SafeAI cites TrustLLM, and DoD CDAO names PyOD. Oracle FCCM product licensing docs name PyOD with the verbatim BSD `Copyright (c) 2018, Yue Zhao` notice and are recorded as Claude-verified row #66dj. Codex's May 13 draft also pointed at an Oracle IoT licensing URL but that URL returned HTTP 404 on Claude verification 2026-05-13 and was dropped. Other topic-relevant PDFs found but none cite target work by name. |
| MITRE / standards-adjacent (May 7) | MITRE LILAC v1, MITRE CWE, MITRE ATLAS exact searches | MITRE LILAC cites TrustLLM and is recorded in Ledger 1. MITRE CWE-1039 cites CommanderSong with Yue Zhao as co-author; USENIX/DBLP/arXiv confirm a real 2018 CommanderSong paper with a Yue Zhao author (USENIX affiliation: SKLOIS / UCAS), but CommanderSong is not in `data/publications.json`, so identity/inventory status is still pending. No MITRE ATLAS direct hit. |
| Standards bodies | MITRE ATLAS, MLCommons, Cloud Security Alliance | No citations |
| Korean tech (Tistory) | Searched | 3 PyOD tutorials found (D10) — corrected from prior negative |
| German tech (Heise.de) | Searched | No results on Heise; Gist.Science DE covers No Attacker Needed, and 5 earlier German sources found (D10) |
| Stanford AI Index 2026 (overview pages, full PDF, public CSV dataset) | Apr 24 | Confirmed negative for target terms and arXiv IDs. |
| Apr 24 full sweep topic-only / false positives | VentureBeat, The Hacker News, CSO Online, OpenAI Privacy Filter coverage, FLI Spring 2026, NIST AI 800-3, NIST AI 800-2 IPD, International AI Safety Report extended summary, OWASP GenAI Q2 2026 trio | No new direct citations. FLI Spring 2026 not released/found. New AEGIS hits mostly unrelated projects. ECOD false positives mostly "decode/decoding." |
| Name-collision false positives (Apr 16) | agentlayer.medium "Aegis+TrustLLM" smart contract audit | Different projects — arXiv:2403.16073 (not Yue Zhao's TrustLLM) and AgentLayer's web3 Aegis (not FORTIS Aegis). Cleared. |
| FM-co careers JDs + agent-governance vendor/consulting blogs (May 28 Claude) | OpenAI "Data Science Manager, Integrity"; Anthropic "ML/Research Engineer, Safeguards" and "Security Software Engineer, Detection & Response"; EY, Microsoft Agent Governance Toolkit, Databricks Unity AI Gateway, Acceldata, Beam AI, Sysdig, GovTech, Kai Waehner/Confluent, Ariel Softwares, Indext Data Lab, Waxell, LoginRadius | No FORTIS naming on direct fetch. FM-co JDs list generic "anomaly detection"/"classifiers" but NOT PyOD (distinct from #8g, which names PyOD verbatim). Beam AI "AEGIS framework" is a generic threat-modeling framework, not FORTIS Aegis. New commercial-product "Aegis" collisions (TechFides, CloudMatos, Authensor) recorded in disambiguation-registry.md. |

---

## Summary Statistics

| Ledger | Count |
|--------|-------|
| Government/Policy citations | 20 (15 prior + 5 verified 2026-07-19: UK gov.uk, Saudi SDAIA, US DOE/ORNL, G7/OECD Salesforce, NIST NVD) |
| External third-party media | 83 (73 prior + 5 Tier 1 and 6 Tier 2 verified 2026-07-19, minus 1 for the SitePoint #22 removal; prior basis: 71 prior + 2 May 13 rows verified by Claude 2026-05-13; 4 wide-run candidates were dropped as exact-URL duplicates of existing rows #5, #7, #21, #34b after Codex Round 1 review, and the May 13 verification work for those four URLs is recorded as evidence upgrades on those existing rows rather than new counted rows) |
| Ecosystem adoption | 169 (154 main-ledger rows through May 13 + 7 May 19 + 4 May 20 + 4 May 28 append-only verified rows) |
| First-party/community | 19 (6 main-ledger rows + 13 May 19 append-only verified rows) |
| Awards/recognitions | 20 (19 main-ledger rows + 1 May 19 append-only ACM SIGSPATIAL award-index row) |
| **Total verified items** | **311 (296 prior + 16 verified 2026-07-19, minus 1 SitePoint removal). 52 Tier 3 and 48 Tier 5 candidates from the 2026-07-19 pass are verified but NOT yet counted, pending row-level dedup against the 169 existing Ledger 3 rows; they are in `news-search-candidates.jsonl`.** |

- **107 papers + 19 tools** searched across all 8 core dimensions plus D9/D10 follow-up checks (citation-audit used 102 non-survey papers)
- **11,551 Google Scholar citations** (Apr 2026)
- **39.11M+ PyPI downloads** for PyOD
- **1,846 Semantic Scholar citations** for Diffusion Models survey
- **~285 Semantic Scholar citations** for TrustLLM
- **5+ books** with dedicated chapters on PyOD/COPOD/ECOD (Manning, Columbia, Apress, Routledge, IntechOpen)
- **2 podcasts** naming PyOD
- **5+ online courses/training pages** teaching PyOD (DataCamp, Udemy x2, O'Reilly video, Python Charmers / Datastat / RX-M / WUNU cluster)
- **8 enterprise integrations** (Databricks x2, Walmart, IQVIA, Apache Beam / Apache Software Foundation, PostHog, MLflow community flavor, Genentech/Roche Data Detective), 1 vendor whitepaper (Altair), 1 EU research project deliverable cluster (SEDIMARK Horizon Europe D3.1 p.18, D5.2), plus finance/audit workflow evidence from Discover Data and Syntora; PyOD GitHub Dependents aggregate snapshot 2026-05-07 = 5,493 repos + 139 packages
- **12 patents** citing PyOD/COPOD/ECOD/LSCP/SUOD (WIPO x2, EU x2, US x4, China x3, Slovakia x1)
- **1 Nature Scientific Data publication** using PyOD (ESA OPS-SAT)

---

## Topic Validation (NOT Direct Coverage)

For grant narratives only. These do not name your work.

Folded to per-theme counts 2026-06-02 (individual outlets recoverable from git history). Each theme is topic-proximity context only and does not name a FORTIS work; none of these counts feed the verified-item totals.

- **AI agent security:** ~38 outlets (e.g., Tom's Hardware, CSO Online, VentureBeat).
- **Consulting / think tanks:** ~36 outlets (e.g., McKinsey x4, Deloitte x5, KPMG x4).
- **ChatGPT geolocation (DoxBench topic):** 9 outlets (e.g., Tom's Hardware, Cybernews, OECD.AI Incident Monitor).
- **Government / regulatory (tools not cited):** ~24 outlets (e.g., FTC, SEC, EU AI Act enforcement).
- **Auditable agents (tools not cited):** ~26 outlets (e.g., ISACA x4, Fortune x3, HBR x3).
- **LLM election prediction (papers not cited):** ~25 outlets (e.g., Science (AAAS), MIT Tech Review, Nature x2).
- **Compute inequality in AI research (paper not cited):** ~11 outlets (e.g., HPCwire, VentureBeat, Stanford HAI AI Index 2025).
- **May 28 agent auditing / governance / skills (FORTIS tools not cited):** ~12 outlets (e.g., O'Reilly Radar, Databricks Unity AI Gateway, GitHub/VoltAgent). All verified to not name FORTIS work on direct fetch.

---

## Changes from Previous Audit

**May 20 independent Codex news-search rerun (wide parallel Phase A + conservative Phase B):**

This was an independent rerun, not a reuse of the May 19 audit. Six live parallel lanes covered D1/D2/D3/D5/D7 plus a replacement sweep; two attempted lanes failed because the thread pool and subagent context were exhausted. The main thread then covered the missing D4/D8/D10 checks with targeted web searches and direct fetches. Net: **+4 verified Ledger 3 rows** and several evidence upgrades to existing rows.

**Running total after May 20: 292 verified items (288 prior + 4 May 20 verified ledger rows).**

- **Ledger 1 (+0):** No new government, policy, foundation-model-system-card, or major PDF hit was verified. Current canonical Wells Fargo job page no longer contains PyOD, so the older Built In mirror remains held rather than promoted.

- **Ledger 2 (+0):** No new strong mainstream press or institutional feature. MarkTechPost does name TrustLLM in an MLCommons AI Safety Benchmark article, but it is a benchmark-list mention rather than dedicated TrustLLM coverage; recorded as an evidence upgrade to the existing TrustLLM explainer/media cluster, not a new row.

- **Ledger 3 (+4):**
  - **L3.1** (D10 patent) [SK2042023U1](https://patents.google.com/patent/SK2042023U1/en). Google Patents verifies one additional COPOD/ECOD/SUOD-related patent hit: the Slovakia utility model lists COPOD, ECOD, ABOD, SUOD, LODA, LOF, and related anomaly-detection methods. Patent tally rises from 11 to 12. CN114298123A was searched in the same lane but held because the direct page only verified generic outlier detection, not a FORTIS work.
  - **L3.2** (D5/D6 survey uptake) [MDPI Sensors 2026 survey](https://www.mdpi.com/1424-8220/26/8/2330) "Agentic and LLM-Based Multimodal Anomaly Detection: Architectures, Challenges, and Prospects" cites AD-LLM in the references and places AD-Agent in its taxonomy table with ADBench as evaluation data. This is direct scientific uptake of the FORTIS anomaly-detection agent line. (Verification note, Claude 2026-05-20: the survey is confirmed to exist and to be an agentic-AD survey via search, and is mirrored on Preprints.org 202602.1368 and TechRxiv, but the specific AD-LLM / AD-Agent / ADBench citation could not be independently re-confirmed because the MDPI page and the TechRxiv mirror both return HTTP 403 to automated fetch; Codex's direct-fetch claim stands pending a manual page check.)
  - **L3.3** (D3/D5 platform cluster) FORTIS over-privilege paper pages: [Hugging Face Papers](https://huggingface.co/papers/2605.09163), [Papers.cool](https://papers.cool/arxiv/2605.09163), [Moonlight ES](https://www.themoonlight.io/es/review/fortis-benchmarking-over-privilege-in-agent-skills), and [AI Native Daily Paper Digest](https://ainativefoundation.org/ai-native-daily-paper-digest-20260512/) name "FORTIS: Benchmarking Over-Privilege in Agent Skills"; Hugging Face and Papers.cool list Yue Zhao. Aggregator and digest surfaces only, so Ledger 3.
  - **L3.4** (D5 media-style platform) [Machine Brief](https://www.machinebrief.com/news/agent-audit-securing-llm-agents-beyond-the-model-w1qd) dedicated article "Agent Audit: Securing LLM Agents Beyond the Model" directly describes Agent Audit, its benchmark, its vulnerability counts, and its open-source/pip availability. Treated as low-tier external article, not Ledger 2.

- **Evidence upgrades, no new count:** Microsoft Research AFMR page names TrustLLM and links the arXiv paper; Virtue AI Research page lists TrustGen and Yue Zhao in the author list; AI Wiki Outliers has a PyOD section naming Yue Zhao; ResearchTrend.AI and Skillget add AEGIS/Justin0504-Aegis platform evidence; AIModels.fyi adds an AD-AGENT paper page. These strengthen existing rows or clusters without changing counts.

- **Held or dropped:** APIs.io PyOD could not be directly resolved; KI-Syndikat search snippets did not reproduce on the live page; LinkedIn agent-style result is login-gated; CSPaper Forum redirected to a removed article; Tom's Hardware geolocation article did not name DoxBench; the current Wells Fargo canonical job page no longer contains PyOD.

**May 28 Codex full sweep with local /news-search and /citation-audit skills (+4 Ledger 3, citation-affiliation refresh):**

This was an independent full-sweep refresh using four live parallel web lanes (policy/PDF/FM-co, media/outlets, ecosystem/tool adoption, and smart paper search) plus a regenerated OpenAlex + Dimensions citation-affiliation audit. The search covered the current `data/publications.json` and `data/open-source.json` inventory. Exact-URL duplicates and same-cluster resurfacing were treated as evidence upgrades, not new rows.

**Running total after May 28: 296 verified items (292 prior + 4 May 28 verified ledger rows).**

- **Ledger 1 (+0):** No new government, standards, foundation-model-system-card, analyst, or first-party foundation-model-company official source was promoted. The OpenAI "Technical Intelligence Analyst" careers page remains live and still names PyOD, but it is the exact URL already counted as #8g, so it is an evidence refresh only. Current high-authority PDFs and release pages checked by direct fetch or PDF text search included OpenAI Frontier Governance Framework, GPT-5.5 System Card, Anthropic Claude Opus 4.8 release page, and Anthropic's May 2026 AI-orchestrated cyber-espionage report; all were verified-negative for FORTIS terms.
- **Ledger 2 (+0):** Mainstream tech, business, security, institutional, and non-English press remained dry for new direct coverage. TechRadar's May 26 financial-services agent-security article is topic validation only because it discusses least privilege and auditability without naming Yue Zhao, FORTIS, PyOD, TrustLLM, Aegis, agent-audit, DoxBench, or a FORTIS paper title.
- **Ledger 3 (+4):**
  - **L3.1** (D3/D5 security blog) [ByteVanguard, "Tool-Enabled AI Agents and the Privilege Problem"](https://bytevanguard.com/2026/05/20/tool-enabled-ai-agents-and-the-privilege-problem/) references "arXiv: FORTIS - Benchmarking Over-Privilege in Agent Skills" in its source list and frames the article around over-privileged tool-enabled agents. Direct fetch verified the reference; no AI-generated disclaimer was found. Count as low-tier external security-blog / ecosystem evidence, not Ledger 2.
  - **L3.2** (D2 patent) [Justia / U.S. Patent 11,979,421, "Cluster-based outlier scoring of network traffic"](https://patents.justia.com/patent/11979421) says the model manager can use the PyOD Python toolkit for anomaly detection. Count as one new patent-family ecosystem row. The related application page is not counted separately.
  - **L3.3** (D5/D7 paper-discussion platform) [AgentArxiv discussion page for "No Attacker Needed: Unintentional Cross-User Contamination in Shared-State LLM Agents"](https://www.agentarxiv.org/papers/cmnkka8gm0001i3j1dnm8k09e) directly names the UCC paper and discusses its shared-state-agent failure mode. Count as a low-tier platform / discussion surface; it complements, but does not duplicate, the Promptfoo / RAXE / SecTools cluster for the same paper.
  - **L3.4** (D5 platform explainer) [AIModels.fyi TyphoFormer page](https://www.aimodels.fyi/papers/arxiv/typhoformer-language-augmented-transformer-accurate-typhoon-track) names "TyphoFormer: Language-Augmented Transformer for Accurate Typhoon Track Forecasting" and lists Yue Zhao among the authors. Count as a low-tier paper explainer / platform surface for the SIGSPATIAL award paper.
- **Evidence upgrades, no new count:** Google Cloud Dataflow's official notebook renders the Apache Beam anomaly-detection example and installs `pyod==2.0.3`, but this is the same Apache Beam PyOD integration already counted in #66de. Hugging Face's AEGIS paper page, AI News CX's Agent Audit article, English Moonlight FORTIS page, Hugging Face NLP-ADBench dataset, PySAD GitHub README, CSDN / Tistory PyOD tutorials, PyPI / ReadTheDocs package pages, and TrustEval-toolkit GitHub page strengthen existing platform, package, or integration clusters without changing counts.
- **Held or dropped:** Oracle AutoMLx anomaly-detection notebook remains held because direct fetch redirects to a documentation index; do not promote from the search snippet. Generalist Programmer's PyOD package guide was dropped as templated / SEO-style and technically unreliable. Gate.com Nesa profile mentions Yue Zhao and PyOD but is crypto-promotional, outside the date window, and too low-relevance for this audit.
- **Citation-affiliation hook:** Standalone `citation-affiliation-audit.md` was regenerated on 2026-05-28 via OpenAlex + Dimensions: 102 non-survey papers searched, OpenAlex found 43 papers with citations and 1,637 unique citing papers, Dimensions found 30 papers with citations and 1,186 unique citing papers, with 39 Tier 0 and 209 Tier 1 institution-affiliation rows. The embedded section below was refreshed from the canonical file.

*Older change-log entries trimmed 2026-06-02 for concision; full history recoverable from git.*

## Citation Affiliation Evidence (integrated from /citation-audit skill, 2026-05-28)

*The following section is integrated from citation-affiliation-audit.md per the news-search cross-skill citation-audit hook. Canonical copy lives in that separate file; this embed keeps the unified report self-contained for tenure / promotion / grant readers. Re-run the standalone audit with /citation-audit --source both to refresh.*

*Generated: 2026-05-28 via OpenAlex + Dimensions*

**What this is:** Papers that cite your work, where at least one author is affiliated with a notable institution.
This means "researchers AT [institution] cited your tool" -- not "[institution] officially endorses your tool."

Per-source coverage of the 102 non-survey papers:
- **OpenAlex**: 43 papers with citations; 1637 unique citing papers analyzed.
- **Dimensions**: 30 papers with citations; 1186 unique citing papers analyzed.

### Tier 0: Government, Space Agencies, National Labs, Defense, Foundation Model Cos

**39 entries**

| Category | Institution | Country | Your Work Cited | Citing Paper | Year | Source |
|----------|-----------|---------|----------------|-------------|------|--------|
| Central Bank | Deutsche Bundesbank | DE | ECOD: Unsupervised Outlier Detectio | Diffusion-Scheduled Denoising Autoencoders for Anomaly Detec | 2025 | openalex |
| Central Bank | Deutsche Bundesbank | DE | The Need for Unsupervised Outlier M | RECol: Reconstruction Error Columns for Outlier Detection | 2023 | openalex |
| Central Bank | Deutsche Bundesbank | Germany | The Need for Unsupervised Outlier M | RECol: Reconstruction Error Columns for Outlier Detection | 2023 | dimensions |
| Defense/Research | RAND Corporation | United States | COPOD: Copula-Based Outlier Detecti | A robust unsupervised method for outlier set detection | 2025 | dimensions |
| Foundation Model Co | OpenAI (United States) | US | Therapeutics Data Commons: Machine  | RL-Finetuning of OpenAI o1-mini to Enhance Biomedical Reason | 2025 | openalex |
| Foundation Model Co | Meta Platforms Inc | United States | COPOD: Copula-Based Outlier Detecti | Detecting Tiny Performance Regressions at Hyperscale | 2025 | dimensions |
| Foundation Model Co | Meta Platforms Inc | United States | COPOD: Copula-Based Outlier Detecti | TSB-AutoAD: Towards Automated Solutions for Time-Series Anom | 2025 | dimensions |
| Foundation Model Co | Meta Platforms Inc | United States | The Need for Unsupervised Outlier M | EasyAD: A Demonstration of Automated Solutions for Time-Seri | 2025 | dimensions |
| Foundation Model Co | Meta Platforms Inc | United States | The Need for Unsupervised Outlier M | TSB-AutoAD: Towards Automated Solutions for Time-Series Anom | 2025 | dimensions |
| Foundation Model Co | OpenAI (United States) | US | ADBench: Anomaly Detection Benchmar | Diffusion Models: A Comprehensive Survey of Methods and Appl | 2023 | openalex |
| Foundation Model Co | Google DeepMind (United Kingdom) | GB | Artificial Intelligence Foundation  | Scientific discovery in the age of artificial intelligence | 2023 | openalex |
| Foundation Model Co | Meta Platforms Inc | United States | COPOD: Copula-Based Outlier Detecti | Data-Efficient and Interpretable Tabular Anomaly Detection | 2023 | dimensions |
| Foundation Model Co | DeepMind Technologies Ltd | United Kingdom | Artificial Intelligence Foundation  | Scientific discovery in the age of artificial intelligence | 2023 | dimensions |
| International Lab | Deutsches Elektronen-Synchrotron DESY | DE | ECOD: Unsupervised Outlier Detectio | Data-Based Condition Monitoring and Disturbance Classificati | 2024 | openalex |
| National Lab | Argonne National Laboratory | US | TODS: An Automated Time Series Outl | A novel sensor-driven framework for preemptive failure detec | 2025 | openalex+dimensions |
| National Lab | Brookhaven National Laboratory | United States | COPOD: Copula-Based Outlier Detecti | Performance analysis and data reduction for exascale scienti | 2025 | dimensions |
| National Lab | Sandia National Laboratories | United States | COPOD: Copula-Based Outlier Detecti | Performance analysis and data reduction for exascale scienti | 2025 | dimensions |
| National Lab | Los Alamos National Laboratory | US | Therapeutics Data Commons: Machine  | Linear graphlet models for accurate and interpretable chemin | 2024 | openalex |
| National Lab | Los Alamos National Laboratory | US | Therapeutics Data Commons: Machine  | Linear Graphlet Models for Accurate and Interpretable Chemin | 2024 | openalex |
| National Lab | Brookhaven National Laboratory | US | Therapeutics Data Commons: Machine  | Leveraging Active Subspaces to Capture Epistemic Model Uncer | 2024 | openalex |
| National Lab | Pacific Northwest National Laboratory | US | Artificial Intelligence Foundation  | Current and future directions in network biology | 2024 | openalex+dimensions |
| National Lab | Brookhaven National Laboratory | US | Artificial Intelligence Foundation  | Current and future directions in network biology | 2024 | openalex+dimensions |
| National Lab | Sandia National Laboratories | US | LSCP: Locally Selective Combination | Ensemble Grammar Induction For Detecting Anomalies in Time S | 2020 | openalex |
| Research Institute | Fraunhofer Institute for Translational Medicine and Pharmacology | DE | Artificial Intelligence Foundation  | Human-supervised Agentic AI for Hypothesis Generation and Ex | 2026 | openalex |
| Research Institute | Fraunhofer Society | Germany | Artificial Intelligence Foundation  | Human-supervised Agentic AI for Hypothesis Generation and Ex | 2026 | dimensions |
| Research Institute | Fraunhofer Institute for Translational Medicine and Pharmacology | DE | Artificial Intelligence Foundation  | Computational drug repurposing: approaches, evaluation of in | 2025 | openalex |
| Research Institute | Fraunhofer Institute for Algorithms and Scientific Computing | DE | Artificial Intelligence Foundation  | Computational drug repurposing: approaches, evaluation of in | 2025 | openalex+dimensions |
| Research Institute | Fraunhofer Society | Germany | Artificial Intelligence Foundation  | Computational drug repurposing: approaches, evaluation of in | 2025 | dimensions |
| Research Institute | Fraunhofer Institute for Open Communication Systems | DE | PyOD: A Python Toolbox for Scalable | Morphological Profiling Dataset of EU-OPENSCREEN Bioactive C | 2024 | openalex |
| Research Institute | Fraunhofer Institute for Applied Information Technology | Germany | COPOD: Copula-Based Outlier Detecti | Privacy and Utility Evaluation of Synthetic Tabular Data for | 2024 | dimensions |
| Research Institute | Fraunhofer Institute for Mechatronic Systems Design | DE | TODS: An Automated Time Series Outl | Meta-learning for Automated Selection of Anomaly Detectors f | 2023 | openalex |
| Research Institute | Fraunhofer Institute for Mechatronic Systems Design | DE | LSCP: Locally Selective Combination | Meta-learning for Automated Selection of Anomaly Detectors f | 2023 | openalex |
| Research Institute | Fraunhofer Institute for Mechatronic Systems Design | Germany | TODS: An Automated Time Series Outl | Meta-learning for Automated Selection of Anomaly Detectors f | 2023 | dimensions |
| Space Agency | Deutsches Zentrum für Luft- und Raumfahrt e. V. (DLR) | DE | ADBench: Anomaly Detection Benchmar | Collaborative Representation-Based Attention Network for Hyp | 2025 | openalex |
| Space Agency | Jet Propulsion Laboratory | US | ADBench: Anomaly Detection Benchmar | Anomaly Detection for Spacecraft Radios Based on Open-Loop R | 2024 | openalex |
| US Government | National Institutes of Health | US | TrustLLM: Trustworthiness in Large  | Economics and Equity of Large Language Models: Health Care P | 2024 | openalex+dimensions |
| US Government | National Institutes of Health | US | Artificial Intelligence Foundation  | Current and future directions in network biology | 2024 | openalex |
| US Government | Centers for Disease Control and Prevention | US | ECOD: Unsupervised Outlier Detectio | Sequence-based detection of emerging antigenically novel inf | 2024 | openalex |
| US Government | National Institutes of Health | US | ECOD: Unsupervised Outlier Detectio | Unsupervised quality assurance for brain MR image rigid regi | 2023 | openalex |

### Tier 1: Big Tech, Finance, Pharma, Healthcare, Industrial

**209 entries**

| Category | Institution | Country | Your Work Cited | Citing Paper | Year | Source |
|----------|-----------|---------|----------------|-------------|------|--------|
| Big Tech | Huawei Technologies (China) | CN | Treble Counterfactual VLMs: A Causa | A Survey of Multimodal Hallucination Evaluation and Detectio | 2026 | openalex |
| Big Tech | Adobe Systems (United States) | US | DPU: Dynamic Prototype Updating for | Few-Shot Graph Out-of-Distribution Detection with LLMs | 2025 | openalex |
| Big Tech | Amazon (United States) | US | TrustLLM: Trustworthiness in Large  | REAL Sampling: Boosting Factuality and Diversity of Open-end | 2025 | openalex |
| Big Tech | Amazon (Germany) | DE | TrustLLM: Trustworthiness in Large  | REAL Sampling: Boosting Factuality and Diversity of Open-end | 2025 | openalex |
| Big Tech | Tencent (China) | CN | ADBench: Anomaly Detection Benchmar | M3DM-NR: RGB-3D Noisy-Resistant Industrial Anomaly Detection | 2025 | openalex |
| Big Tech | Amazon (United States) | US | ADBench: Anomaly Detection Benchmar | REACT: Residual-Adaptive Contextual Tuning for Fast Model Ad | 2025 | openalex |
| Big Tech | Intel (United Kingdom) | GB | ADBench: Anomaly Detection Benchmar | Beyond Academic Benchmarks: Critical Analysis and Best Pract | 2025 | openalex |
| Big Tech | Amazon (United States) | US | BOND: Benchmarking Unsupervised Out | TGTOD: A Global Temporal Graph Transformer for Outlier Detec | 2025 | openalex |
| Big Tech | IBM Research - Thomas J. Watson Research Center | US | Contrastive Attributed Network Anom | Deep Graph Anomaly Detection: A Survey and New Perspectives | 2025 | openalex |
| Big Tech | Tencent (China) | CN | Contrastive Attributed Network Anom | How to use Graph Data in the Wild to Help Graph Anomaly Dete | 2025 | openalex |
| Big Tech | Huawei Technologies (China) | CN | TODS: An Automated Time Series Outl | TAB: Unified Benchmarking of Time Series Anomaly Detection M | 2025 | openalex |
| Big Tech | Huawei Technologies (United States) | US | TODS: An Automated Time Series Outl | TAB: Unified Benchmarking of Time Series Anomaly Detection M | 2025 | openalex |
| Big Tech | IBM Research - Zurich | CH | Therapeutics Data Commons: Machine  | Foundation models for materials discovery – current state an | 2025 | openalex |
| Big Tech | IBM (United States) | US | Therapeutics Data Commons: Machine  | Foundation models for materials discovery – current state an | 2025 | openalex |
| Big Tech | IBM Research - Thomas J. Watson Research Center | US | Therapeutics Data Commons: Machine  | Foundation models for materials discovery – current state an | 2025 | openalex |
| Big Tech | Intel (United States) | US | Therapeutics Data Commons: Machine  | A framework for evaluating the chemical knowledge and reason | 2025 | openalex |
| Big Tech | Nvidia (United Kingdom) | GB | Therapeutics Data Commons: Machine  | Boosting the predictive power of protein representations wit | 2025 | openalex |
| Big Tech | Baidu (China) | CN | Employee Turnover Prediction with M | A Comprehensive Survey of Artificial Intelligence Techniques | 2025 | openalex |
| Big Tech | Microsoft Research (United Kingdom) | GB | NNG-Mix: Improving Semi-supervised  | Distribution Shifts at Scale: Out-of-distribution Detection  | 2025 | openalex |
| Big Tech | IBM Research - Zurich | CH | Artificial Intelligence Foundation  | Foundation models for materials discovery – current state an | 2025 | openalex |
| Big Tech | IBM (United States) | US | Artificial Intelligence Foundation  | Foundation models for materials discovery – current state an | 2025 | openalex |
| Big Tech | IBM Research - Thomas J. Watson Research Center | US | Artificial Intelligence Foundation  | Foundation models for materials discovery – current state an | 2025 | openalex |
| Big Tech | IBM (United States) | US | Artificial Intelligence Foundation  | GP-MoLFormer: a foundation model for molecular generation | 2025 | openalex |
| Big Tech | Microsoft Research Asia (China) | CN | Artificial Intelligence Foundation  | Controlling risks of AI in chemical science with agents | 2025 | openalex+dimensions |
| Big Tech | Amazon (United States) | US | ECOD: Unsupervised Outlier Detectio | REACT: Residual-Adaptive Contextual Tuning for Fast Model Ad | 2025 | openalex |
| Big Tech | Huawei Technologies (China) | CN | ECOD: Unsupervised Outlier Detectio | Compatible Unsupervised Anomaly Detection with Multi-Perspec | 2025 | openalex |
| Big Tech | Adobe Inc | United States | DPU: Dynamic Prototype Updating for | Few-Shot Graph Out-of-Distribution Detection with LLMs | 2025 | dimensions |
| Big Tech | Tencent Technology Shenzhen Co Ltd | China | Contrastive Attributed Network Anom | How to use Graph Data in the Wild to Help Graph Anomaly Dete | 2025 | dimensions |
| Big Tech | Huawei Technologies Co Ltd | China | TODS: An Automated Time Series Outl | TAB: Unified Benchmarking of Time Series Anomaly Detection M | 2025 | dimensions |
| Big Tech | Huawei Technologies Co Ltd | China | COPOD: Copula-Based Outlier Detecti | Compatible Unsupervised Anomaly Detection with Multi-Perspec | 2025 | dimensions |
| Big Tech | Amazon Web Services Inc | United States | COPOD: Copula-Based Outlier Detecti | REACT: Residual-Adaptive Contextual Tuning for Fast Model Ad | 2025 | dimensions |
| Big Tech | Baidu Inc | China | Employee Turnover Prediction with M | A Comprehensive Survey of Artificial Intelligence Techniques | 2025 | dimensions |
| Big Tech | Amazon Web Services Inc | United States | The Need for Unsupervised Outlier M | Hyperparameter Optimization in Machine Learning | 2025 | dimensions |
| Big Tech | Amazon (United States) | US | TrustLLM: Trustworthiness in Large  | Economics and Equity of Large Language Models: Health Care P | 2024 | openalex |
| Big Tech | Adobe Systems (United States) | US | TrustLLM: Trustworthiness in Large  | Benchmark suites instead of leaderboards for evaluating AI f | 2024 | openalex |
| Big Tech | Tencent (China) | CN | ADBench: Anomaly Detection Benchmar | IM-IAD: Industrial Image Anomaly Detection Benchmark in Manu | 2024 | openalex |
| Big Tech | Microsoft Research (United Kingdom) | GB | ADBench: Anomaly Detection Benchmar | Building AI Agents for Autonomous Clouds: Challenges and Des | 2024 | openalex |
| Big Tech | Tencent (China) | CN | ADBench: Anomaly Detection Benchmar | SoftPatch+: Fully unsupervised anomaly classification and se | 2024 | openalex |
| Big Tech | Huawei Technologies (China) | CN | Contrastive Attributed Network Anom | You Can't Ignore Either: Unifying Structure and Feature Deno | 2024 | openalex |
| Big Tech | Microsoft (United States) | US | Automatic Unsupervised Outlier Mode | End-to-End AutoML for Unsupervised Log Anomaly Detection | 2024 | openalex |
| Big Tech | Intel (United States) | US | Revisiting Time Series Outlier Dete | A Robust Framework for Evaluation of Unsupervised Time-Serie | 2024 | openalex |
| Big Tech | IBM Research - Ireland | IE | Therapeutics Data Commons: Machine  | Knowledge Enhanced Representation Learning for Drug Discover | 2024 | openalex |
| Big Tech | IBM Research - Zurich | CH | Therapeutics Data Commons: Machine  | Knowledge Enhanced Representation Learning for Drug Discover | 2024 | openalex |
| Big Tech | Huawei Technologies (China) | CN | XGBOD: Improving Supervised Outlier | Towards Online and Safe Configuration Tuning with Semi-super | 2024 | openalex |
| Big Tech | IBM Research - Ireland | IE | Artificial Intelligence Foundation  | Knowledge Enhanced Representation Learning for Drug Discover | 2024 | openalex |
| Big Tech | IBM Research - Zurich | CH | Artificial Intelligence Foundation  | Knowledge Enhanced Representation Learning for Drug Discover | 2024 | openalex |
| Big Tech | IBM Research - Thomas J. Watson Research Center | US | Artificial Intelligence Foundation  | A physics-inspired approach to the understanding of molecula | 2024 | openalex |
| Big Tech | Microsoft Research (United Kingdom) | GB | ECOD: Unsupervised Outlier Detectio | Outlier Detection in Temporal and Spatial Sequences Via Corr | 2024 | openalex |
| Big Tech | Amazon Web Services Inc | United States | TrustLLM: Trustworthiness in Large  | Economics and Equity of Large Language Models: Health Care P | 2024 | dimensions |
| Big Tech | Adobe Inc | United States | TrustLLM: Trustworthiness in Large  | Benchmark suites instead of leaderboards for evaluating AI f | 2024 | dimensions |
| Big Tech | Huawei Technologies Co Ltd | China | Contrastive Attributed Network Anom | You Can't Ignore Either: Unifying Structure and Feature Deno | 2024 | dimensions |
| Big Tech | IBM Research GmbH | Switzerland | AutoAudit: Mining Accounting and Ti | Graph Feature Preprocessor: Real-time Subgraph-based Feature | 2024 | dimensions |
| Big Tech | Amazon.com Inc | United States | COPOD: Copula-Based Outlier Detecti | Rethinking Robust Multivariate Time Series Anomaly Detection | 2024 | dimensions |
| Big Tech | IBM Research - India | India | COPOD: Copula-Based Outlier Detecti | Enabling Programmable Metric Flows | 2024 | dimensions |
| Big Tech | Samsung Electronics Co Ltd | South Korea | COPOD: Copula-Based Outlier Detecti | Relative Frequency-Rank Encoding for Unsupervised Network An | 2024 | dimensions |
| Big Tech | Tencent (China) | CN | ADBench: Anomaly Detection Benchmar | Improving Generalizability of Graph Anomaly Detection Models | 2023 | openalex |
| Big Tech | Microsoft Research (United Kingdom) | GB | ADBench: Anomaly Detection Benchmar | ADMoE: Anomaly Detection with Mixture-of-Experts from Noisy  | 2023 | openalex |
| Big Tech | Microsoft Research Asia (China) | CN | ADBench: Anomaly Detection Benchmar | UADB: Unsupervised Anomaly Detection Booster | 2023 | openalex |
| Big Tech | Alibaba Group (China) | CN | ADBench: Anomaly Detection Benchmar | ADPal: Automatic Detection of Troubled Users in Online Servi | 2023 | openalex |
| Big Tech | Tencent (China) | CN | BOND: Benchmarking Unsupervised Out | Improving Generalizability of Graph Anomaly Detection Models | 2023 | openalex |
| Big Tech | Microsoft Research (United Kingdom) | GB | BOND: Benchmarking Unsupervised Out | ADMoE: Anomaly Detection with Mixture-of-Experts from Noisy  | 2023 | openalex |
| Big Tech | Tencent (China) | CN | Contrastive Attributed Network Anom | Improving Generalizability of Graph Anomaly Detection Models | 2023 | openalex |
| Big Tech | Microsoft Research (United Kingdom) | GB | Automatic Unsupervised Outlier Mode | ADMoE: Anomaly Detection with Mixture-of-Experts from Noisy  | 2023 | openalex |
| Big Tech | Huawei Technologies (China) | CN | Revisiting Time Series Outlier Dete | DeepDiscord: Dual Contrastive Coding for Transferable Time S | 2023 | openalex |
| Big Tech | Huawei Technologies (United Kingdom) | GB | Revisiting Time Series Outlier Dete | DeepDiscord: Dual Contrastive Coding for Transferable Time S | 2023 | openalex |
| Big Tech | Alibaba Group (United States) | US | Revisiting Time Series Outlier Dete | DCdetector: Dual Attention Contrastive Representation Learni | 2023 | openalex |
| Big Tech | Alibaba Group (China) | CN | Revisiting Time Series Outlier Dete | DCdetector: Dual Attention Contrastive Representation Learni | 2023 | openalex |
| Big Tech | Microsoft Research (United Kingdom) | GB | SUOD: Accelerating Large-scale Unsu | TraceArk: Towards Actionable Performance Anomaly Alerting fo | 2023 | openalex |
| Big Tech | Microsoft (Norway) | NO | SUOD: Accelerating Large-scale Unsu | TraceArk: Towards Actionable Performance Anomaly Alerting fo | 2023 | openalex |
| Big Tech | Microsoft Research Asia (China) | CN | SUOD: Accelerating Large-scale Unsu | UADB: Unsupervised Anomaly Detection Booster | 2023 | openalex |
| Big Tech | IBM Research - Zurich | CH | Therapeutics Data Commons: Machine  | Accelerating material design with the generative toolkit for | 2023 | openalex |
| Big Tech | IBM (United Kingdom) | GB | Therapeutics Data Commons: Machine  | Accelerating material design with the generative toolkit for | 2023 | openalex |
| Big Tech | IBM Research - Tokyo | JP | Therapeutics Data Commons: Machine  | Accelerating material design with the generative toolkit for | 2023 | openalex |
| Big Tech | IBM Research - Almaden | US | Therapeutics Data Commons: Machine  | Accelerating material design with the generative toolkit for | 2023 | openalex |
| Big Tech | Google (United States) | US | Therapeutics Data Commons: Machine  | Olympus, enhanced: benchmarking mixed-parameter and multi-ob | 2023 | openalex |
| Big Tech | Microsoft Research (United Kingdom) | GB | AutoAudit: Mining Accounting and Ti | ADMoE: Anomaly Detection with Mixture-of-Experts from Noisy  | 2023 | openalex |
| Big Tech | Microsoft Research (United Kingdom) | GB | LSCP: Locally Selective Combination | ADMoE: Anomaly Detection with Mixture-of-Experts from Noisy  | 2023 | openalex |
| Big Tech | Microsoft Research Asia (China) | CN | Music Artist Classification with Co | MovieFactory: Automatic Movie Creation from Text using Large | 2023 | openalex |
| Big Tech | Nvidia (United States) | US | Artificial Intelligence Foundation  | Scientific discovery in the age of artificial intelligence | 2023 | openalex |
| Big Tech | Google (United Kingdom) | GB | Artificial Intelligence Foundation  | Scientific discovery in the age of artificial intelligence | 2023 | openalex |
| Big Tech | Microsoft Research Asia (China) | CN | Artificial Intelligence Foundation  | Scientific discovery in the age of artificial intelligence | 2023 | openalex+dimensions |
| Big Tech | Microsoft (Netherlands) | NL | Artificial Intelligence Foundation  | Scientific discovery in the age of artificial intelligence | 2023 | openalex |
| Big Tech | IBM Research - Zurich | CH | Artificial Intelligence Foundation  | Accelerating material design with the generative toolkit for | 2023 | openalex |
| Big Tech | IBM (United Kingdom) | GB | Artificial Intelligence Foundation  | Accelerating material design with the generative toolkit for | 2023 | openalex |
| Big Tech | IBM Research - Tokyo | JP | Artificial Intelligence Foundation  | Accelerating material design with the generative toolkit for | 2023 | openalex |
| Big Tech | IBM Research - Almaden | US | Artificial Intelligence Foundation  | Accelerating material design with the generative toolkit for | 2023 | openalex |
| Big Tech | IBM Research - Zurich | CH | Artificial Intelligence Foundation  | The rise of automated curiosity-driven discoveries in chemis | 2023 | openalex |
| Big Tech | IBM Research - Thomas J. Watson Research Center | US | Artificial Intelligence Foundation  | Evaluating the roughness of structure–property relationships | 2023 | openalex |
| Big Tech | Google (United States) | US | Artificial Intelligence Foundation  | Olympus, enhanced: benchmarking mixed-parameter and multi-ob | 2023 | openalex |
| Big Tech | Salesforce (United States) | US | ECOD: Unsupervised Outlier Detectio | Unsupervised Skin Lesion Segmentation via Structural Entropy | 2023 | openalex |
| Big Tech | Microsoft Research Asia (China) | CN | ECOD: Unsupervised Outlier Detectio | UADB: Unsupervised Anomaly Detection Booster | 2023 | openalex |
| Big Tech | Amazon (United Kingdom) | GB | ECOD: Unsupervised Outlier Detectio | Low-Count Time Series Anomaly Detection | 2023 | openalex |
| Big Tech | Amazon (United States) | US | ECOD: Unsupervised Outlier Detectio | Low-Count Time Series Anomaly Detection | 2023 | openalex |
| Big Tech | Amazon (United Kingdom) | GB | ECOD: Unsupervised Outlier Detectio | Low-count Time Series Anomaly Detection | 2023 | openalex |
| Big Tech | Tencent Technology Shenzhen Co Ltd | China | Contrastive Attributed Network Anom | Improving Generalizability of Graph Anomaly Detection Models | 2023 | dimensions |
| Big Tech | Google LLC | United States | COPOD: Copula-Based Outlier Detecti | Data-Efficient and Interpretable Tabular Anomaly Detection | 2023 | dimensions |
| Big Tech | Microsoft Research Asia (China) | China | COPOD: Copula-Based Outlier Detecti | UADB: Unsupervised Anomaly Detection Booster | 2023 | dimensions |
| Big Tech | IBM Research GmbH | Switzerland | Artificial Intelligence Foundation  | The rise of automated curiosity-driven discoveries in chemis | 2023 | dimensions |
| Big Tech | Nvidia Corp | United States | Artificial Intelligence Foundation  | Scientific discovery in the age of artificial intelligence | 2023 | dimensions |
| Big Tech | Huawei Technologies (France) | FR | Automatic Unsupervised Outlier Mode | Human readable network troubleshooting based on anomaly dete | 2022 | openalex |
| Big Tech | Samsung (South Korea) | KR | Revisiting Time Series Outlier Dete | Towards a Rigorous Evaluation of Time-Series Anomaly Detecti | 2022 | openalex |
| Big Tech | Alibaba Group (China) | CN | Revisiting Time Series Outlier Dete | TFAD | 2022 | openalex |
| Big Tech | Alibaba Group (United States) | US | Revisiting Time Series Outlier Dete | TFAD | 2022 | openalex |
| Big Tech | IBM Research - Thomas J. Watson Research Center | US | Revisiting Time Series Outlier Dete | Deep Learning for Time Series Anomaly Detection: A Survey | 2022 | openalex |
| Big Tech | Microsoft (Brazil) | BR | Employee Turnover Prediction with M | EMPLOYEE TURNOVER INTENTION - MAPPING PROFILES UNDER A DECIS | 2022 | openalex |
| Big Tech | Alibaba DAMO Academy | China | COPOD: Copula-Based Outlier Detecti | GraphAD | 2022 | dimensions |
| Big Tech | Huawei Technologies (France) | FR | SUOD: Toward Scalable Unsupervised  | The New Abnormal: Network Anomalies in the AI Era | 2021 | openalex |
| Big Tech | Alibaba Group (China) | CN | LSCP: Locally Selective Combination | A spatial-compositional feature fusion convolutional autoenc | 2021 | openalex |
| Big Tech | Adobe Systems (United States) | US | LSCP: Locally Selective Combination | IPOF: An Extremely and Excitingly Simple Outlier Detection B | 2021 | openalex |
| Big Tech | Tencent (China) | CN | Music Artist Classification with Co | Large-scale singer recognition using deep metric learning: a | 2021 | openalex |
| Big Tech | Adobe Systems (United States) | US | XGBOD: Improving Supervised Outlier | Towards addressing unauthorized sharing of subscriptions | 2021 | openalex |
| Big Tech | Adobe Systems (United States) | US | XGBOD: Improving Supervised Outlier | Virtual-SRE For Monitoring Large Scale Time-series Data | 2021 | openalex |
| Big Tech | IBM Research - Tokyo | Japan | AutoAudit: Mining Accounting and Ti | Cash flow prediction of a bank deposit using scalable graph  | 2021 | dimensions |
| Big Tech | Alibaba Group Holding Ltd | China | Combining Machine Learning Models u | A spatial-compositional feature fusion convolutional autoenc | 2021 | dimensions |
| Big Tech | QQ Music BU Tencent Music Entertainment (TME), Shenzhen, China | China | Music Artist Classification with Co | Large-scale singer recognition using deep metric learning: a | 2021 | dimensions |
| Big Tech | Alibaba Group (China) | CN | LSCP: Locally Selective Combination | Modeling Heterogeneous Statistical Patterns in High-dimensio | 2020 | openalex |
| Big Tech | Nvidia Corp | United States | Combining Machine Learning Models u | Machine Learning in Python: Main Developments and Technology | 2020 | dimensions |
| Big Tech | Samsung (South Korea) | KR | An Empirical Study of Touch-based A | The Personal Identification Chord | 2018 | openalex |
| Consulting | Deloitte (United States) | US | SUOD: Accelerating Large-scale Unsu | Fraud detection in healthcare claims using machine learning: | 2024 | openalex |
| Consulting | PricewaterhouseCoopers (Canada) | CA | DCSO: Dynamic Combination of Detect | LSCP: Locally Selective Combination in Parallel Outlier Ense | 2019 | openalex |
| Consulting | PricewaterhouseCoopers (Canada) | CA | Employee Turnover Prediction with M | LSCP: Locally Selective Combination in Parallel Outlier Ense | 2019 | openalex |
| Finance | BlackRock (United States) | US | ADBench: Anomaly Detection Benchmar | Can an unsupervised clustering algorithm reproduce a categor | 2024 | openalex |
| Finance | BlackRock (United States) | US | The Need for Unsupervised Outlier M | Can an unsupervised clustering algorithm reproduce a categor | 2024 | openalex |
| Finance | BlackRock Inc | United States | The Need for Unsupervised Outlier M | Can an unsupervised clustering algorithm reproduce a categor | 2024 | dimensions |
| Finance | Visa (United States) | US | ADBench: Anomaly Detection Benchmar | Tackling Diverse Minorities in Imbalanced Classification | 2023 | openalex |
| Finance | Capital One (United States) | US | TODS: An Automated Time Series Outl | From Detection to Action: a Human-in-the-loop Toolkit for An | 2023 | openalex |
| Finance | Visa (United Kingdom) | GB | TODS: An Automated Time Series Outl | Time Series Synthesis Using the Matrix Profile for Anonymiza | 2023 | openalex |
| Finance | Morgan Stanley (United States) | US | SynC: A Copula based Framework for  | A supervised generative optimization approach for tabular da | 2023 | openalex |
| Finance | Visa (United States) | US | XGBOD: Improving Supervised Outlier | Tackling Diverse Minorities in Imbalanced Classification | 2023 | openalex |
| Finance | BlackRock (United States) | US | The Need for Unsupervised Outlier M | Quantifying Outlierness of Funds from their Categories using | 2023 | openalex |
| Finance | Capital One NA | United States | TODS: An Automated Time Series Outl | From Detection to Action: a Human-in-the-loop Toolkit for An | 2023 | dimensions |
| Finance | BlackRock Inc | United States | The Need for Unsupervised Outlier M | Quantifying Outlierness of Funds from their Categories using | 2023 | dimensions |
| Healthcare | Mayo Clinic in Florida | US | TrustLLM: Trustworthiness in Large  | Ethical framework for responsible foundational models in med | 2025 | openalex |
| Healthcare | Cleveland Clinic London | United Kingdom | Combining Machine Learning Models u | Applications of Artificial Intelligence in Gastrointestinal  | 2024 | dimensions |
| Industrial | Robert Bosch (United States) | US | ADBench: Anomaly Detection Benchmar | Model Selection of Anomaly Detectors in the Absence of Label | 2025 | openalex |
| Industrial | Robert Bosch (Germany) | DE | XGBOD: Improving Supervised Outlier | The OPS-SAT benchmark for detecting anomalies in satellite t | 2025 | openalex |
| Industrial | Robert Bosch (United States) | US | The Need for Unsupervised Outlier M | Model Selection of Anomaly Detectors in the Absence of Label | 2025 | openalex |
| Industrial | Robert Bosch (Germany) | DE | ECOD: Unsupervised Outlier Detectio | The OPS-SAT benchmark for detecting anomalies in satellite t | 2025 | openalex |
| Industrial | Siemens SRL | Romania | TODS: An Automated Time Series Outl | A decentralised architecture for secure exchange of assets i | 2025 | dimensions |
| Industrial | Siemens (China) | CN | ADBench: Anomaly Detection Benchmar | PARs: Predicate-based Association Rules for Efficient and Ac | 2024 | openalex |
| Industrial | Honeywell (France) | FR | Employee Turnover Prediction with M | Identifying Survival-Changing Sequential Patterns for Employ | 2023 | openalex |
| Industrial | Robert Bosch (Germany) | DE | SUOD: Accelerating Large-scale Unsu | On Why the System Makes the Corner Case: AI-based Holistic A | 2022 | openalex |
| Industrial | Robert Bosch GmbH | Germany | COPOD: Copula-Based Outlier Detecti | On Why the System Makes the Corner Case: AI-based Holistic A | 2022 | dimensions |
| Industrial | Bosch Termotechnologia SA | Portugal | COPOD: Copula-Based Outlier Detecti | Predictive maintenance on sensorized stamping presses by tim | 2022 | dimensions |
| Pharma | AstraZeneca AB | Sweden | DrugAgent: Automating AI-aided Drug | Democratising real-world drug discovery through agentic AI | 2026 | dimensions |
| Pharma | AstraZeneca UK Ltd | United Kingdom | DrugAgent: Automating AI-aided Drug | Democratising real-world drug discovery through agentic AI | 2026 | dimensions |
| Pharma | Novartis (China) | CN | Therapeutics Data Commons: Machine  | Machine Learning for Toxicity Prediction Using Chemical Stru | 2025 | openalex |
| Pharma | Eli Lilly (United States) | US | Therapeutics Data Commons: Machine  | Machine Learning for Toxicity Prediction Using Chemical Stru | 2025 | openalex |
| Pharma | AstraZeneca (Sweden) | SE | Therapeutics Data Commons: Machine  | Machine Learning for Toxicity Prediction Using Chemical Stru | 2025 | openalex |
| Pharma | Pfizer (United States) | US | Therapeutics Data Commons: Machine  | Machine Learning for Toxicity Prediction Using Chemical Stru | 2025 | openalex |
| Pharma | Sanofi (France) | FR | Therapeutics Data Commons: Machine  | Machine Learning for Toxicity Prediction Using Chemical Stru | 2025 | openalex |
| Pharma | Merck & Co., Inc., Rahway, NJ, USA (United States) | US | Therapeutics Data Commons: Machine  | Data Scaling and Generalization Insights for Medicinal Chemi | 2025 | openalex |
| Pharma | Roche (Switzerland) | CH | Artificial Intelligence Foundation  | Combinatorial prediction of therapeutic perturbations using  | 2025 | openalex |
| Pharma | Merck & Co., Inc., Rahway, NJ, USA (United States) | US | Artificial Intelligence Foundation  | Combinatorial prediction of therapeutic perturbations using  | 2025 | openalex |
| Pharma | Merck & Co Inc | United States | Therapeutics Data Commons: Machine  | Data Scaling and Generalization Insights for Medicinal Chemi | 2025 | dimensions |
| Pharma | Eli Lilly and Co | United States | Therapeutics Data Commons: Machine  | Machine Learning for Toxicity Prediction Using Chemical Stru | 2025 | dimensions |
| Pharma | AstraZeneca AB | Sweden | Therapeutics Data Commons: Machine  | Machine Learning for Toxicity Prediction Using Chemical Stru | 2025 | dimensions |
| Pharma | Pfizer GmbH | Germany | Therapeutics Data Commons: Machine  | Machine Learning for Toxicity Prediction Using Chemical Stru | 2025 | dimensions |
| Pharma | Eli Lilly and Co Ltd | United Kingdom | Therapeutics Data Commons: Machine  | Machine Learning for Toxicity Prediction Using Chemical Stru | 2025 | dimensions |
| Pharma | Merck & Co Inc | United States | Therapeutics Data Commons: Machine  | Machine Learning for Toxicity Prediction Using Chemical Stru | 2025 | dimensions |
| Pharma | Merck & Co Inc | United States | Artificial Intelligence Foundation  | Combinatorial prediction of therapeutic perturbations using  | 2025 | dimensions |
| Pharma | AstraZeneca (Sweden) | SE | Therapeutics Data Commons: Machine  | Human-in-the-loop active learning for goal-oriented molecule | 2024 | openalex |
| Pharma | AstraZeneca (Sweden) | SE | Therapeutics Data Commons: Machine  | Using test-time augmentation to investigate explainable AI:  | 2024 | openalex |
| Pharma | AstraZeneca (Japan) | JP | Therapeutics Data Commons: Machine  | Registries in Machine Learning-Based Drug Discovery: A Short | 2024 | openalex |
| Pharma | AstraZeneca (Finland) | FI | Therapeutics Data Commons: Machine  | Registries in Machine Learning-Based Drug Discovery: A Short | 2024 | openalex |
| Pharma | AstraZeneca (United Kingdom) | GB | Therapeutics Data Commons: Machine  | Registries in Machine Learning-Based Drug Discovery: A Short | 2024 | openalex |
| Pharma | Novartis (Switzerland) | CH | Artificial Intelligence Foundation  | A call for an industry-led initiative to critically assess m | 2024 | openalex |
| Pharma | Merck & Co., Inc., Rahway, NJ, USA (United States) | US | Artificial Intelligence Foundation  | A call for an industry-led initiative to critically assess m | 2024 | openalex |
| Pharma | Pfizer (Germany) | DE | Artificial Intelligence Foundation  | A call for an industry-led initiative to critically assess m | 2024 | openalex |
| Pharma | AstraZeneca (Sweden) | SE | Artificial Intelligence Foundation  | A call for an industry-led initiative to critically assess m | 2024 | openalex |
| Pharma | Sanofi (France) | FR | Artificial Intelligence Foundation  | Deep Batch Active Learning for Drug Discovery | 2024 | openalex |
| Pharma | Sanofi (United States) | US | Artificial Intelligence Foundation  | Deep Batch Active Learning for Drug Discovery | 2024 | openalex |
| Pharma | Sanofi (China) | CN | Artificial Intelligence Foundation  | Deep Batch Active Learning for Drug Discovery | 2024 | openalex |
| Pharma | Sanofi (Germany) | DE | Artificial Intelligence Foundation  | Deep Batch Active Learning for Drug Discovery | 2024 | openalex |
| Pharma | Roche (Switzerland) | CH | Artificial Intelligence Foundation  | Combinatorial prediction of therapeutic perturbations using  | 2024 | openalex |
| Pharma | Merck & Co., Inc., Rahway, NJ, USA (United States) | US | Artificial Intelligence Foundation  | Combinatorial prediction of therapeutic perturbations using  | 2024 | openalex |
| Pharma | AstraZeneca (Brazil) | BR | Artificial Intelligence Foundation  | Representation Learning of Human Disease Mechanisms for a Fo | 2024 | openalex |
| Pharma | AstraZeneca (United States) | US | Artificial Intelligence Foundation  | Representation Learning of Human Disease Mechanisms for a Fo | 2024 | openalex |
| Pharma | AstraZeneca (Sweden) | SE | Artificial Intelligence Foundation  | Representation Learning of Human Disease Mechanisms for a Fo | 2024 | openalex |
| Pharma | AstraZeneca (United Kingdom) | GB | Artificial Intelligence Foundation  | Representation Learning of Human Disease Mechanisms for a Fo | 2024 | openalex |
| Pharma | AstraZeneca (Australia) | AU | Artificial Intelligence Foundation  | Representation Learning of Human Disease Mechanisms for a Fo | 2024 | openalex |
| Pharma | AstraZeneca AB | Sweden | Therapeutics Data Commons: Machine  | Human-in-the-loop active learning for goal-oriented molecule | 2024 | dimensions |
| Pharma | AstraZeneca UK Ltd | United Kingdom | Artificial Intelligence Foundation  | Representation Learning of Human Disease Mechanisms for a Fo | 2024 | dimensions |
| Pharma | AstraZeneca AB | Sweden | Artificial Intelligence Foundation  | Representation Learning of Human Disease Mechanisms for a Fo | 2024 | dimensions |
| Pharma | Novartis Pharma AG | Switzerland | Artificial Intelligence Foundation  | A call for an industry-led initiative to critically assess m | 2024 | dimensions |
| Pharma | AstraZeneca AB | Sweden | Artificial Intelligence Foundation  | A call for an industry-led initiative to critically assess m | 2024 | dimensions |
| Pharma | Merck & Co Inc | United States | Artificial Intelligence Foundation  | A call for an industry-led initiative to critically assess m | 2024 | dimensions |
| Pharma | Merck & Co Inc | United States | Artificial Intelligence Foundation  | Combinatorial prediction of therapeutic perturbations using  | 2024 | dimensions |
| Pharma | AstraZeneca (Sweden) | SE | Therapeutics Data Commons: Machine  | Machine learning for small molecule drug discovery in academ | 2023 | openalex |
| Pharma | Novartis (Switzerland) | CH | Therapeutics Data Commons: Machine  | Machine learning for small molecule drug discovery in academ | 2023 | openalex |
| Pharma | Novartis Institutes for BioMedical Research | None | Therapeutics Data Commons: Machine  | Machine learning for small molecule drug discovery in academ | 2023 | openalex |
| Pharma | Pfizer (Germany) | DE | Therapeutics Data Commons: Machine  | Equivariant Graph Neural Networks for Toxicity Prediction | 2023 | openalex |
| Pharma | Novartis (United States) | US | Artificial Intelligence Foundation  | Computer‐aided evaluation and exploration of chemical spaces | 2023 | openalex |
| Pharma | Novartis Institutes for Biomedical Research Inc | United States | Artificial Intelligence Foundation  | Computer‐aided evaluation and exploration of chemical spaces | 2023 | dimensions |
| Pharma | Sanofi China Investment Co Ltd | China | Artificial Intelligence Foundation  | Deep Batch Active Learning for Drug Discovery | 2023 | dimensions |
| Pharma | Sanofi Aventis Deutschland GmbH | Germany | Artificial Intelligence Foundation  | Deep Batch Active Learning for Drug Discovery | 2023 | dimensions |
| Pharma | Sanofi SA | France | Artificial Intelligence Foundation  | Deep Batch Active Learning for Drug Discovery | 2023 | dimensions |
| Pharma | Sanofi Pasteur Biologics LLC | United States | Artificial Intelligence Foundation  | Deep Batch Active Learning for Drug Discovery | 2023 | dimensions |
| Pharma | Novartis (Switzerland) | CH | Therapeutics Data Commons: Machine  | Chemoinformatics and Artificial Intelligence Colloquium: Pro | 2022 | openalex |
| Pharma | Novartis Institutes for BioMedical Research | None | Therapeutics Data Commons: Machine  | Chemoinformatics and Artificial Intelligence Colloquium: Pro | 2022 | openalex |
| Pharma | AstraZeneca (Sweden) | SE | Therapeutics Data Commons: Machine  | Hierarchical Clustering Split for Low-Bias Evaluation of Dru | 2021 | openalex |
| Pharma | AstraZeneca (United States) | US | Therapeutics Data Commons: Machine  | Hierarchical Clustering Split for Low-Bias Evaluation of Dru | 2021 | openalex |
| Retail | Walmart (United States) | US | PyOD: A Python Toolbox for Scalable | Anomaly Detection for an E-commerce Pricing System | 2019 | openalex |
| Telecom | Ericsson (Sweden) | SE | TODS: An Automated Time Series Outl | Resilient automatic model selection for mobility prediction | 2025 | openalex |
| Telecom | Global AI Accelerator, Ericsson, Chennai, India | India | COPOD: Copula-Based Outlier Detecti | Adaptive Thresholding Heuristic for KPI Anomaly Detection | 2024 | dimensions |
| Telecom | Ericsson (Sweden) | SE | ADBench: Anomaly Detection Benchmar | Data-Efficient Automatic Model Selection in Unsupervised Ano | 2022 | openalex |
| Telecom | Ericsson (Sweden) | SE | Automatic Unsupervised Outlier Mode | Data-Efficient Automatic Model Selection in Unsupervised Ano | 2022 | openalex |
| Telecom | Cisco Systems (United States) | US | TODS: An Automated Time Series Outl | Traffic Anomaly Detection Via Conditional Normalizing Flow | 2022 | openalex |
| Telecom | Cisco Systems Inc | United States | TODS: An Automated Time Series Outl | Traffic Anomaly Detection Via Conditional Normalizing Flow | 2022 | dimensions |

### Summary by Institution

| Institution | Category | Work-Citations |
|-----------|----------|---------------|
| Microsoft Research (United Kingdom) | Big Tech | 9 |
| Tencent (China) | Big Tech | 8 |
| Microsoft Research Asia (China) | Big Tech | 7 |
| AstraZeneca (Sweden) | Pharma | 7 |
| IBM Research - Zurich | Big Tech | 7 |
| Huawei Technologies (China) | Big Tech | 6 |
| Amazon (United States) | Big Tech | 6 |
| IBM Research - Thomas J. Watson Research Center | Big Tech | 6 |
| Adobe Systems (United States) | Big Tech | 5 |
| Alibaba Group (China) | Big Tech | 5 |
| AstraZeneca AB | Pharma | 5 |
| Merck & Co Inc | Pharma | 5 |
| Meta Platforms Inc | Foundation Model Co | 5 |
| Merck & Co., Inc., Rahway, NJ, USA (United States) | Pharma | 4 |
| National Institutes of Health | US Government | 3 |
| Ericsson (Sweden) | Telecom | 3 |
| BlackRock (United States) | Finance | 3 |
| Robert Bosch (Germany) | Industrial | 3 |
| Fraunhofer Institute for Mechatronic Systems Design | Research Institute | 3 |
| IBM (United States) | Big Tech | 3 |
| Novartis (Switzerland) | Pharma | 3 |
| IBM Research - Tokyo | Big Tech | 3 |
| Brookhaven National Laboratory | National Lab | 3 |
| Deutsche Bundesbank | Central Bank | 3 |
| Amazon Web Services Inc | Big Tech | 3 |
| Huawei Technologies Co Ltd | Big Tech | 3 |
| OpenAI (United States) | Foundation Model Co | 2 |
| Visa (United States) | Finance | 2 |
| Robert Bosch (United States) | Industrial | 2 |
| Huawei Technologies (France) | Big Tech | 2 |
| Samsung (South Korea) | Big Tech | 2 |
| Alibaba Group (United States) | Big Tech | 2 |
| Intel (United States) | Big Tech | 2 |
| Sanofi (France) | Pharma | 2 |
| Novartis Institutes for BioMedical Research | Pharma | 2 |
| IBM (United Kingdom) | Big Tech | 2 |
| IBM Research - Almaden | Big Tech | 2 |
| AstraZeneca (United States) | Pharma | 2 |
| IBM Research - Ireland | Big Tech | 2 |
| Google (United States) | Big Tech | 2 |
| Pfizer (Germany) | Pharma | 2 |
| Los Alamos National Laboratory | National Lab | 2 |
| AstraZeneca (United Kingdom) | Pharma | 2 |
| Sandia National Laboratories | National Lab | 2 |
| PricewaterhouseCoopers (Canada) | Consulting | 2 |
| Fraunhofer Institute for Translational Medicine and Pharmacology | Research Institute | 2 |
| Roche (Switzerland) | Pharma | 2 |
| Amazon (United Kingdom) | Big Tech | 2 |
| Adobe Inc | Big Tech | 2 |
| AstraZeneca UK Ltd | Pharma | 2 |
| Tencent Technology Shenzhen Co Ltd | Big Tech | 2 |
| IBM Research GmbH | Big Tech | 2 |
| Nvidia Corp | Big Tech | 2 |
| BlackRock Inc | Finance | 2 |
| Fraunhofer Society | Research Institute | 2 |
| Mayo Clinic in Florida | Healthcare | 1 |
| Amazon (Germany) | Big Tech | 1 |
| Jet Propulsion Laboratory | Space Agency | 1 |
| Siemens (China) | Industrial | 1 |
| Deutsches Zentrum für Luft- und Raumfahrt e. V. (DLR) | Space Agency | 1 |
| Intel (United Kingdom) | Big Tech | 1 |
| Microsoft (United States) | Big Tech | 1 |
| Huawei Technologies (United Kingdom) | Big Tech | 1 |
| Deloitte (United States) | Consulting | 1 |
| Microsoft (Norway) | Big Tech | 1 |
| Huawei Technologies (United States) | Big Tech | 1 |
| Argonne National Laboratory | National Lab | 1 |
| Cisco Systems (United States) | Telecom | 1 |
| Capital One (United States) | Finance | 1 |
| Visa (United Kingdom) | Finance | 1 |
| Novartis (China) | Pharma | 1 |
| Eli Lilly (United States) | Pharma | 1 |
| Pfizer (United States) | Pharma | 1 |
| Nvidia (United Kingdom) | Big Tech | 1 |
| AstraZeneca (Japan) | Pharma | 1 |
| AstraZeneca (Finland) | Pharma | 1 |
| Morgan Stanley (United States) | Finance | 1 |
| Baidu (China) | Big Tech | 1 |
| Honeywell (France) | Industrial | 1 |
| Microsoft (Brazil) | Big Tech | 1 |
| Nvidia (United States) | Big Tech | 1 |
| Google DeepMind (United Kingdom) | Foundation Model Co | 1 |
| Google (United Kingdom) | Big Tech | 1 |
| Microsoft (Netherlands) | Big Tech | 1 |
| Pacific Northwest National Laboratory | National Lab | 1 |
| Fraunhofer Institute for Algorithms and Scientific Computing | Research Institute | 1 |
| Novartis (United States) | Pharma | 1 |
| Sanofi (United States) | Pharma | 1 |
| Sanofi (China) | Pharma | 1 |
| Sanofi (Germany) | Pharma | 1 |
| AstraZeneca (Brazil) | Pharma | 1 |
| AstraZeneca (Australia) | Pharma | 1 |
| Salesforce (United States) | Big Tech | 1 |
| Centers for Disease Control and Prevention | US Government | 1 |
| Deutsches Elektronen-Synchrotron DESY | International Lab | 1 |
| Walmart (United States) | Retail | 1 |
| Fraunhofer Institute for Open Communication Systems | Research Institute | 1 |
| Siemens SRL | Industrial | 1 |
| Capital One NA | Finance | 1 |
| Cisco Systems Inc | Telecom | 1 |
| Eli Lilly and Co | Pharma | 1 |
| Pfizer GmbH | Pharma | 1 |
| Eli Lilly and Co Ltd | Pharma | 1 |
| RAND Corporation | Defense/Research | 1 |
| Amazon.com Inc | Big Tech | 1 |
| IBM Research - India | Big Tech | 1 |
| Samsung Electronics Co Ltd | Big Tech | 1 |
| Fraunhofer Institute for Applied Information Technology | Research Institute | 1 |
| Global AI Accelerator, Ericsson, Chennai, India | Telecom | 1 |
| Google LLC | Big Tech | 1 |
| Robert Bosch GmbH | Industrial | 1 |
| Alibaba DAMO Academy | Big Tech | 1 |
| Bosch Termotechnologia SA | Industrial | 1 |
| Cleveland Clinic London | Healthcare | 1 |
| Alibaba Group Holding Ltd | Big Tech | 1 |
| QQ Music BU Tencent Music Entertainment (TME), Shenzhen, China | Big Tech | 1 |
| Baidu Inc | Big Tech | 1 |
| Novartis Pharma AG | Pharma | 1 |
| Novartis Institutes for Biomedical Research Inc | Pharma | 1 |
| DeepMind Technologies Ltd | Foundation Model Co | 1 |
| Sanofi China Investment Co Ltd | Pharma | 1 |
| Sanofi Aventis Deutschland GmbH | Pharma | 1 |
| Sanofi SA | Pharma | 1 |
| Sanofi Pasteur Biologics LLC | Pharma | 1 |

### Coverage

**Sources used:** OpenAlex + Dimensions

#### OpenAlex

**Papers with citations:** 43/102

**Indexed but 0 citations (51):** Can Multimodal LLMs Perform Time Series , Charts Are Not Images: On the Challenges, CoAct: Co-Active LLM Preference Learning, Defenses Against Prompt Attacks Learn Su, Doxing via the Lens: Revealing Location-, Mitigating Hallucinations in Large Langu, "Someone Hid It": Query-Agnostic Black-B, Topology Matters: Measuring Memory Leaka, A Personalized Conversational Benchmark:, AD-AGENT: A Multi-agent Framework for En, Edit Away and My Face Will Not Stay: Per, Few-Shot Graph Out-of-Distribution Detec, JailDAM: Jailbreak Detection with Adapti, LLM-Empowered Patient-Provider Communica, Learning from the Storm: A Multivariate , MetaOOD: Automatic Selection of OOD Dete, Navigating Between Explainability and Ex, Secure On-Device Video OOD Detection Wit, SocialMaze: A Benchmark for Evaluating S, TRUSTEVAL: A Dynamic Evaluation Toolkit , ... and 31 more

**Not found (8):** DecAlign: Hierarchical Cross-Modal Align, TrustGen: A Platform of Dynamic Benchmar, DyFlow: Dynamic Workflow Framework for A, AutoDavis: Automatic and Dynamic Evaluat, ELECT: Toward Unsupervised Outlier Model, Auditable Agents... (ACL Workshop on Tow, Multimodal Generative Engine Optimizatio, Can Molecular Foundation Models Know Wha

#### Dimensions

**Papers with citations:** 30/102

**Indexed but 0 citations (70):** Can Multimodal LLMs Perform Time Series , Charts Are Not Images: On the Challenges, CoAct: Co-Active LLM Preference Learning, Defenses Against Prompt Attacks Learn Su, Mitigating Hallucinations in Large Langu, "Someone Hid It": Query-Agnostic Black-B, Topology Matters: Measuring Memory Leaka, TrustGen: A Platform of Dynamic Benchmar, A Personalized Conversational Benchmark:, AD-AGENT: A Multi-agent Framework for En, DyFlow: Dynamic Workflow Framework for A, Edit Away and My Face Will Not Stay: Per, Few-Shot Graph Out-of-Distribution Detec, JailDAM: Jailbreak Detection with Adapti, LLM-Empowered Patient-Provider Communica, Learning from the Storm: A Multivariate , MetaOOD: Automatic Selection of OOD Dete, NLP-ADBench: NLP Anomaly Detection Bench, Navigating Between Explainability and Ex, Retrieval-Reasoning Large Language Model, ... and 50 more

**Not found (2):** AutoDavis: Automatic and Dynamic Evaluat, Revisiting Time Series Outlier Detection

*OpenAlex coverage improves over time. Re-run in 3-6 months to capture newly indexed papers; Dimensions has better CS coverage and complements OpenAlex on per-paper citation graphs.*

*Cross-source dedup uses exact (institution, citing_title, cited_work) matching. Variants like 'Google' vs 'Google LLC' or punctuation-variant titles may produce near-duplicate rows that span sources.*
