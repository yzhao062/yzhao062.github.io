# News & Media Coverage Audit — Yue Zhao / FORTIS Lab

*Last 5 runs (full change-log in `## Changes from Previous Audit` and in git history):*
*2026-08-13 (Phase A: 17 Claude lanes via /workflows + 10 Codex lanes via /prun, every lane run as a first-ever audit with no prior-negative suppression; Phase B: 12 Codex verification units): 1238 raw records to 1030 unique candidates, 839 absent from prior files, 503 Phase B verdicts, zero unit failures. Net new **+4 Tier 0**: the India TEC draft standard on AI robustness listing PyOD in its recommended-tooling table, the Brazil Chamber of Deputies research proceedings running PyOD, SUOD, ECOD, and COPOD operationally against Senate procurement overpricing, an ESA/ESOC telemetry report engaging PyOD and COPOD in its requirements analysis, and the Google Research Tx-LLM post naming TDC as its training source. **Ledger 6 nearly doubled**, 11 to 20, four rows found only by tail triage because those papers cite AEGIS by mechanism rather than by name; one compares AEGIS against NVIDIA OpenShell and Microsoft's Agent Governance Toolkit, so the standing note that Praetor was the only baseline precedent no longer holds. Patents, package forensics, and dissertations ran as dedicated lanes for the first time and account for most of the +164 Ledger 3 growth, including 33 patents with named assignees (Visa, Tencent, Baidu, China Mobile, Ping An, CETC 54). **135 MIRROR verdicts** were URLs absent from every prior file that still pointed at already-counted items, which is why URL-level dedup is not sufficient; the International AI Safety Report and the NVD CVE record were both caught this way. A defect in the citation-audit OpenAlex path was diagnosed and fixed: daily-budget exhaustion had been recorded as zero citations. Details in "## 2026-08-13 Pass".*
*2026-08-09 (Phase A via /workflows + /prun, then 16 Codex verification shards): the largest run to date. Phase B closed 16 of 16 shards with zero errors, 542 records over 541 unique URLs in 45 minutes and 1,028 tool uses, every promotion reached by downloading and scanning the document. Net new **+2 Tier 0** (a second OpenAI careers posting naming **PyOD 2.0** by pinned version, recovered from two Wayback captures of the canonical URL; and the Brazil National Treasury journal, whose author is a Controladoria-Geral da União official, which reverses the 2026-07-31 demotion of that row) and **+2 DOE labs** at Tier 1 (SLAC on PyOD, Sandia on **HPOD**, the first HPOD appearance in any government document). CSET Georgetown cites the model-extraction survey by name. The `journal1` shard verified 30 peer-reviewed articles and split them 12 substantive-use / 18 reference-list-only, adding Cell Press as a new venue family for PyOD. **Three prior verdicts were reversed:** the single "Refuted" DOE row (OSTI 2333852) is a body citation of a PyOD artefact and moves to bibliography-only, a Phase A verified-negative (OSTI 2550614) was a false negative, and one Scientific Reports row demoted in Codex Round 2 now has evidence. **CISA bulletin SB26-201 was reclassified down** from a worker's Tier 0 claim to a mirror of the already-counted CVE row, on CISA's own "not a direct result of CISA analysis" disclaimer. CVE-2026-15529 reconciled: NVD now reads "up to 3.6.1", the fix merged 2026-07-20, and 3.6.2 shipped. **Ledger placement closed out:** two new tables were created for promotions that previously lived only inside pass sections, **Ledger 1b** (8 DOE national-laboratory reports with substantive use) and **Ledger 6** (5 external academic citations of the agent-auditing line), plus rows for Cloud Security Alliance, TechTarget, and the Foresight Institute grantee page. The Indonesian Ministry of Finance journal was promoted to Tier 0 on author affiliation, and its use claim corrected downward: PyOD appears once in 15 pages as a benchmark citation that drove model selection, not as the implementation. **The reconciliation is now closed and the total is 353.** Every promotion in the 2026-07-19, 2026-07-31, and 2026-08-09 pass sections has a ledger row. Three tables were created for classes that had no home: **Ledger 1b** (8 DOE national-laboratory reports with substantive use), **Ledger 6** (11 external academic citations of the agent-auditing line), and **Ledger 7** (15 peer-reviewed articles running the tools in their methods). Ledger 2's published 83 was never reproducible from its 73 rows; placing the 11 orphaned 2026-07-19 promotions moved 4 of them elsewhere and left Ledger 2 at 80. **A fresh scan of the Auditable Agents citation graph found the strongest external citation to date** (arXiv:2605.04093, DEMM), which cites four of the lab's works, names a section after the paper, cedes framework priority to it, and **falsifies the standing "Implicit Execution Tracing has zero external citers" negative**. Semantic Scholar missed it entirely while carrying a false edge that survives revision. Details in "## 2026-08-09 Pass".*
*2026-07-31 (cross-vendor: 6 Codex lanes via /prun + 6 Claude lanes via /workflows): 406 raw records to **366 unique candidates**. Net new **+6 Tier 0** (Japan MoD ATLA naming PyOD in its recommended-tooling table, BIS/Bundesbank using PyOD and implementing DCSO, Japan FSA on TrustLLM, Japan METI and NEDO on TDC, a NIST webinar deck) and **+11 Tier 1** (6 DOE national-lab reports with substantive use, 5 verified third-party academic citations of Aegis / Auditable Agents / agent-audit), plus Cloud Security Alliance, Foresight Institute, ACM SIGSPATIAL, Amazon Science, Grokipedia, and USC Viterbi. **11 of 19 worker high-tier claims were corrected on coordinator re-fetch**: coauthor-institution listings demoted (Microsoft Research x3, IBM Research), host mistaken for author (Parliament of Australia, Brazil TCU, one Sandia-reported OSTI record), CVE-2026-15529 collapsed from 3 claims to registry mirrors of the already-counted T0-e, and 2 of 7 Semantic Scholar citation edges refuted as name collisions. Implicit Execution Tracing and the FORTIS benchmark both have **zero** confirmed external citers. The OpenAI Tier 0(b) row survives only via its committed snapshot; the live URL now 404s and the successor posting dropped the PyOD bullet. 78 verified-negatives added. Details in "## 2026-07-31 Pass".*
*2026-07-19 (Claude coordinator + 10 Codex lanes via /prun): 269 candidate records to 258 unique URLs. Broke a three-round drought: net new **+5 Tier 0** (UK gov.uk production record, Saudi SDAIA, US DOE/ORNL, G7/OECD Salesforce, NIST NVD CVE) and **+5 Tier 1** (FLI Summer 2026, NTT Technical Review, 3 Nature-family papers), all direct-fetch verified. +6 Tier 2 including first editorial coverage of the auditing line (The Agent Times, WIDTH) and same-week pickup of the four newest papers. Resolved Ledger 2 #22 (SitePoint) as REMOVED, net -1. A mid-round gap (Implicit Execution Tracing never searched) was closed by a tenth lane, which also verified 7 third-party citations of Auditable Agents, 4 of them new. Details in "## 2026-07-19 Pass".*
*2026-06-14 (Codex independent broad parallel search): 9 lanes total: 5 structured lanes plus 4 broad follow-up lanes after the user asked to search less narrowly. Net new Tier 0/1 direct coverage verified: 0. Added 46 exact-URL candidate, drop, duplicate, and negative records to `news-search-candidates.jsonl`; strongest new items are low-tier or academic-downstream signals, not editorial ledger promotions. Main action items: Phase B review of new ADBench/Aegis/TDC academic-downstream rows, PyOD ecosystem rows, three China patent candidates, and a SitePoint recheck because the live page did not verify the prior `agent-audit` direct-coverage claim. Details in "## 2026-06-14 Codex Independent Broad Search".*
*2026-06-13 (Claude /workflows two-phase refresh): 84 Phase-A candidates to 67 Phase-B keeps; net new editorial ~0 (the sweep re-surfaced already-tracked ecosystem items: Grokipedia is Ledger 4 #70; Ericsson patent, DataCamp/Udemy courses, and the Manning/O'Reilly book already in Ledger 3). Genuinely new: Auditable Agents (arXiv:2604.05485) has 4 third-party downstream citations within weeks (bibliometric; flag for /citation-audit). Stanford HAI 2026 AI Index checked (Yue): does not name TrustLLM (negative). Details in "## 2026-06-13 Refresh".*
*2026-05-28 (Claude independent 8-lane rerun): net +0 counted ledger rows (Ledger 1/2/3/4/5 all +0); 4 marginal Phase-B keeps folded into existing rows, plus Negative Results and Topic Validation additions.*
*2026-05-28 (Codex /news-search + /citation-audit sweep): net +4 Ledger 3 (0 Ledger 1/2/4/5); citation-affiliation hook refreshed to 39 Tier 0 + 209 Tier 1 rows.*
*2026-05-20 (Codex /news-search rerun): net +4 Ledger 3 (0 Ledger 1/2/4/5).*
*All 8 core dimensions plus D9/D10 follow-up checks complete across the current inventory. Codex 2026-06-14 local parse: 112 publications + 19 tools; the 2026-05-28 citation-audit integration keeps its own non-survey subset basis.*
*Citation verification applied: every item names or cites the work, person, lab, or co-author.*

---

## 2026-08-30 Pass (Phase A: 33 Codex lanes via `/prun`; Phase B: 22 Codex units; cross-vendor adversarial verification: 28 Claude agents via `/workflows`)

**Method, and what changed.** The round started as a two-vendor fan-out, then the Claude quota
tightened and all 16 Claude discovery lanes were re-cast as Codex lanes with their briefs carried over
verbatim. When quota returned, Claude was spent on the one job Codex cannot do for itself: an
independent adversarial re-fetch of every high-tier claim the Codex lanes had produced. That decision
is the most useful thing in this pass.

Fourteen lanes were added mid-round on evidence rather than plan. Two BIS hits in the first wave
prompted one dedicated central-bank and official-statistics lane. Seven more went deep on the
agent-auditability line at the user's direction. Six closed gaps that three completeness critics
measured against the round's own corpus.

**Scale.** 2,081 raw records to 1,785 unique URLs, 1,044 absent from the prior 1,934-URL index.
1,130 Phase B verdict rows over 1,018 unique URLs. 122 URLs were surfaced independently by two lanes.

| Verdict | Count |
|---|---|
| NEW | 549 |
| MIRROR | 208 |
| UNVERIFIABLE | 154 |
| TOPIC-ONLY | 127 |
| DROP | 50 |
| ALREADY-COUNTED | 42 |

### Tier 0: Confirmed New (Ledger 1, +4 documents)

Rows 18, 19, 20 and 20b: the BIS/IFC Bank of Thailand paper stating a production-deployment goal for
ECOD on central-bank credit data; the International AI Safety Report **2025** edition citing TrustLLM,
which is a different document from the 2026 edition already counted; a NICT Japan cybersecurity deck
describing TrustLLM's six trustworthiness dimensions; and a second NICT deck whose AI Security
Evaluation Platform builds two of its three selectable test sets on TrustLLM. Japan NICT and the Bank
of Thailand are both new to this ledger.

Row 20b was found by the round-5 reviewer, in a document this round had already recorded as a verified
negative. See "A Text Scan Cannot Read a Slide" below.

### The Adversarial Pass Overturned 11 of 17 High-Tier Claims

Every claim the Codex lanes rated Tier 0, Tier 1 or Tier 2 was handed to an independent Claude agent
instructed to disprove it, with a second agent attacking anything that survived on the separate axis
of authorship and novelty. Six survived. The eleven that fell divide into three classes, and the third
is the one to keep in view.

- **First-party or misattributed.** A "National Academies deck naming TDC" is Marinka Zitnik's own
  slides. She is senior author of the TDC papers, every slide footer reads `zitniklab.hms.harvard.edu`,
  and "Zhao" appears zero times across 37 pages. NASEM hosted the file on its CDN as invited-speaker
  material. This is the same shape as the earlier SUOD case: material internal to the cited work's own
  author team logged as third-party evidence.
- **Already counted, or host mistaken for author.** IFC Bulletin 64 was proposed as a Tier 0 citation
  of the Diffusion Models survey. It fails on five independent grounds: the survey is already carried
  as a single aggregate Ledger 3 row covering 1,846 citations; the BIS chapter is a verbatim reprint of
  arXiv:2401.06263 from January 2024, so the citation edge predates the reprint and sits inside that
  1,846; the authors are at the Bundesbank and the University of St Gallen, with two explicit
  disclaimers that the views are not the BIS's; the same institution and bulletin series already holds
  a stronger row at 2d; and the audit's own tier machinery computes over a non-survey subset.
- **Dead or fabricated URLs.** Three of the seventeen did not resolve. The Notre Dame Lucy Institute
  report returned a genuine origin 404, `gyznsw.cn` returned a 555-byte nginx 404, and a MarkTechPost
  ADMET-AI URL was a fabricated slug on a real outlet with no redirect from an older path.

**Three of seventeen top-tier URLs did not exist.** Only an independent second-vendor fetch found that.
Single-vendor high-tier output should not be promoted without one.

### The Agent-Auditability Line

Seven dedicated lanes ran on this line, and it is now the best-mapped area of the audit.

**The work was cited in an OWASP standard's drafting history, then removed.** The official OWASP AISVS
repository was cloned and scanned across its current tree, its merged history, and 721 fetched
pull-request heads. Merged PR #899 cited Auditable Agents by title and arXiv identifier, with research
notes describing its five dimensions and three mechanism classes. AEGIS was cited by arXiv identifier
in merged PR #815 as a pre-execution firewall and audit layer, and a later revision linked the repository.
PR #1018 removed both during consolidation. Neither appears in the released specification, which is why
an earlier scan of the published document came back clean. Recorded as historical Tier 0 candidates,
not as claims about the current release.

**Citation absence is now measured in bounded samples rather than asserted.** Three lanes converge from different
directions. The full NIST-2025-0035 agent-security docket was enumerated at 535 records with 467
primary PDFs downloaded and scanned: zero citations. Fifty-five named vendors across observability,
AI security, agent authorization and GRC: zero citations, with Drata, Fiddler, Cerbos, WorkOS, Descope
and Inngest all converging on the same technical pattern without naming the research. Eight languages
of national-standards and research-institute material, including TC260, IPA, TTA, BSI and Fraunhofer:
zero citations. Across these sampled corpora, related auditability patterns appear without citations to the FORTIS work. This audit does not establish whether those materials derived from it.

**Citation indices are unreliable in both directions.** A listing-level sweep enumerated 8,150 August
2026 arXiv submissions and scanned 326 selected PDFs, finding three new citations that no index
carried. Semantic Scholar's 54 checked citer PDFs all confirmed their asserted edges. OpenAlex reported
zero citers for nearly every seed and supplied one corrupt edge, `W4394653315`, which resolves to an
unrelated temporal-logic paper containing neither the title nor the identifier. Both indices report
zero forward citations for Implicit Execution Tracing while DEMM demonstrably cites it. **No absence
claim on this line is safe without opening the PDF.**

**A standing negative was falsified.** The note that the FORTIS over-privilege benchmark has zero
confirmed external citers is false. arXiv:2608.18351 runs both FORTIS tasks as external evaluations and
reports them in its results tables.

**Shipped reuse, as distinct from mentions.** RedStamp merged a live AEGIS adapter that builds a pinned
commit in CI and calls the check endpoint; HELM AI Kernel merged AEGIS evidence-integrity proof tests
and an overhead benchmark; SINT Protocol merged two conformance documents calibrated against an
`agent-audit` issue; Repath merged GRADE's observed/declared/inferred edge taxonomy; Agent Action
Receipts targets the Auditable Agents IS Level 3 definition and uses the Auditability Card as a buyer
checklist. A separate Rust project renamed itself to Kintsugi to resolve the AEGIS name collision while
keeping the academic citation.

**Negatives on this line, scoped to what was searched.** The sampled citation indices and corpora
returned no downstream citations to WeClawArena. Two independent lanes found no third-party coverage of
`auditable.run` across Crunchbase, LinkedIn, Business Wire, TechCrunch and the general queries used in
this pass. Neither result establishes universal absence, and this pass separately shows that citation
indices miss real edges.

### Site Defects Found and Fixed

A dedicated lane re-fetched every award and evidence link on the public surfaces, and the coordinator
re-checked twelve of them directly. Most of the lane's flags were wrong: linking an award name to the
award programme's own page is normal practice, and demanding that every such page name the recipient
would be a misreading. Four defects were real and are fixed in this commit: a DNS failure at
`manteimaeawards.com`, a 404 at the University of Cincinnati Engineer of the Month page, a 404 at the
`Wesleyluo9/DoxBench` repository link, and an unsupported SLAC claim whose cited OSTI page never
mentions PyOD and whose two "Zhao" hits are both **Zhao, Rui**, a different person. The SLAC link now
points to the paper's DOI, and the claim itself was corrected downward: OSTI's own record confirms the
`SLAC National Accelerator Laboratory` research org, but the paper uses PyOD for the one-class SVM it
compares against rather than as its method, so `opensource.html` now says baseline. Both arXiv versions
print that citation as an unresolved `[?]`, and `iopscience.org` serves a bot interstitial to every
fetch, so this row rests on use rather than on a resolved citation.

`scripts/ci_check_site.py` was also scanning agent scratch directories, so a page a worker downloaded
in order to grep it broke the site gate. Fixed by skipping the exact `skills/news-search/scratch/`
prefix, so a legitimately published directory such as `docs/scratch/` is still checked.

### Held or Awaiting Re-Fetch

154 UNVERIFIABLE records are re-fetch targets rather than absent evidence. Three items have now been
blocked for three consecutive rounds and still need a browser capture: the DoD CDAO toolkit PDF
(re-verified this round through a browser PDF path, but `ai.mil` still 403s a scripted fetch), MITRE
LILAC v1, and the four Google Patents links on `opensource.html`. These three are a fetch problem, not
a ledger problem. CDAO is Ledger 1 rows 2 and 2b and MITRE LILAC is row 8e, all counted on evidence
already verified; what is blocked is the scripted re-check, so a later round can confirm the pages have
not changed.

One item is genuinely uncounted. The Brazil TCU study is a real Tier 0 candidate whose PDF now 404s
with an empty CDX record, and it is held because a Tier 0 claim may not rest on a search extract.

Six remediation lanes closed gaps that three completeness critics measured against this round's own
corpus. All six finished; none of their candidates has been through Phase B, so nothing below is
counted, and the next round should verify them first.

| Lane | Output | Strongest leads |
|---|---|---|
| Biomedical via Europe PMC | 28 candidates, 3 verified negatives | 21 records document substantive TDC training, dataset use, or benchmark execution, including Google TxGemma, Schrodinger DeepAutoQSAR, Bayer Caco-2 modelling, Janssen / Johnson & Johnson graph transformers, and Recursion MolE. The TDC paper of record (PMID 36131149) drew no attention anywhere else this round because it carries no arXiv identifier, which is how an entire pharma-adoption surface stayed invisible. |
| Compliance and regulators | 5 candidates, 14 verified negatives | A London Borough of Sutton algorithmic transparency record on GOV.UK links the PyOD KNN documentation inside a production health and social-care anomaly-detection system, with Access Group named as developer. The OECD.AI trustworthy-AI catalogue links `yzhao062/anomaly-detection-resources`. |
| Security conferences and organizations | 6 candidates, 23 verified negatives | Three USENIX Security 2025 papers and one NDSS 2026 paper cite the work, one of them stating that PyOD implemented its KNN baseline. Conference proceedings had never been opened by any lane. |
| Supply chain and non-Python ports | 32 candidates, 38 verified negatives | No Tier 0 or Tier 1. Every URL fetched and its HTTP result recorded. |
| Under-served works | 37 candidates, 6 verified negatives | Covers every work the attention cross-tab named, including the Employee Turnover paper, CONAD, ADMoE, and the PyOD 2 paper. |
| Regional indexes | 29 candidates, 3 verified negatives | 21 scholarly or thesis records and 8 book records. 24 access failures recorded rather than treated as absence. |

The recurring lesson across three of these lanes: a work without an arXiv identifier is invisible to an
identifier-keyed sweep, however heavily it is cited. 41 of the 124 works in `data/publications.json`
have no arXiv URL, and they sit at the bottom of the attention distribution.

### A Text Scan Cannot Read a Slide

Row 20 originally closed with a verified negative: that the second NICT deck
(`nict_cyber2026/program_takeshi-takahashi.pdf`) covers an AI security evaluation platform but names no
FORTIS work. That was wrong. Slide 20 is the platform's own interface, and its "Select test sets" panel
offers `Prompt Injection (Purple Llama)`, `AdvGLUE (TrustLLM)`, and `Jailbreak (TrustLLM)`.

That slide is an image. `pypdf` and `pdftotext` both return the string `20` for the page, its page
number and nothing else, so `pdf_term_scan.py` and every other text-keyed check this audit runs are
structurally blind to it. No judgement call went the wrong way here. The evidence was never in front of
the tool that produced the negative, and reaching it took rendering the embedded image and looking.

Two rules follow. A negative drawn from a text scan is only as strong as the text the scan could see, so
compare the extracted character count against the page count before recording one: a page yielding two
characters has not been read. And presentation decks are the format where this bites hardest, because a
slide is as likely to be a picture of words as words. This is the second image-shaped miss this round,
after the four Google Patents links that still need a browser capture.

### Method Defects in This Round, and the Fix

The lane fan-out lost work four times while reporting success each time. A CRLF in a unit list silently
no-opped twelve lanes at exit 0. Editing a launcher while it ran killed three supervising shells.
`setsid` is absent from Git Bash, so a fire-and-forget rewrite launched nothing while printing success.
Truncated stdout from a killed shell was then read as a complete record of what it had dispatched.
Separately, nine Tier 0 verdict rows were reported as nine findings when they were four documents.

All five are written up in `skills/news-search/references/fan-out-reliability.md`, and
`skills/news-search/scripts/dispatch_lanes.sh` implements the guards. The rule that covers them: an
exit code is not evidence that work happened, a result file is, and a tier count must be grouped by
document rather than by URL.

### Propagated to Site

Ledger 1 rows 18, 19, 20 and 20b reached `opensource.html` (Recent Institutional Visibility card),
`files/bio.txt` and its `index.html` prerender, and `llms.txt`. The four link defects above were fixed
on `cv/cv-full.tex` and `opensource.html`. Nothing below Tier 1 was propagated this round.

`scripts/ci_check_site.py` now checks that `files/bio.txt` and the `index.html` prerender agree
paragraph for paragraph. They hold the same three paragraphs, both are maintained by hand, and nothing
verified them: an edit this round landed in one and not the other while every gate still passed.

---

## 2026-08-13 Pass (Phase A: 17 Claude lanes via `/workflows` + 10 Codex lanes via `/prun`; Phase B: 12 Codex verification units)

**Method, and the one thing that changed.** Every Phase A lane ran as a first-ever audit. No lane was
allowed to read `news-coverage-audit.md`, `news-search-candidates.jsonl`, or
`references/disambiguation-registry.md` to decide what to skip. Prior rounds had recorded
verified-negatives that later proved false, and the 2026-08-09 round reversed three earlier verdicts.
Suppressing a search because a previous round called it empty is the failure mode this round was built
to avoid. Deduplication against prior rounds happened only in the coordinator, after discovery closed.

Three lanes ran for the first time as dedicated lanes: patents, package-and-dependency forensics, and
books, courses, and dissertations. Those three account for most of the Ledger 3 growth.

**Scale.** Phase A produced 947 records from the Claude lanes and 291 from the Codex lanes, deduping to
1030 unique URLs, 32 of them surfaced independently by both vendors. 839 were absent from the prior
audit and candidate files. Phase B returned 503 verdicts across 12 units with no unit failures.

| Verdict | Count |
|---|---|
| NEW | 209 |
| MIRROR | 135 |
| ALREADY-COUNTED | 68 |
| UNVERIFIABLE | 31 |
| DROP | 26 |
| PROMOTE-FOR-REVIEW | 21 |
| DEMOTE | 13 |

**The 135 MIRROR verdicts are the number to keep in view.** Each was a URL absent from every prior file
that still pointed at an item the ledger already counts, so URL-level deduplication alone would have
reported all 135 as new findings. The International AI Safety Report is the clearest case: its citation
of TrustLLM is real and sits in the body on p99, but it is already row 8b, and the canonical 221-page
file differs from the counted 220-page copy only by a duplicated title page. The NVD record for
CVE-2026-15529 is the same story against the already-counted T0-e.

### Tier 0: Confirmed New (Ledger 1, +4)

| Work | Source | Evidence |
|---|---|---|
| COPOD | **arxiv.org** | PDF p31: "Some examples of partially fulfilled requirements are for algorithms that R1) do not provide dedicated thresholding mechanisms, R2) technically allow for the online detection but with a large computational overhead, R4) handle anomalies in training data but cannot learn from them, R5) would need additional mechanisms or modifications of external libraries (i.e., PyOD70) to provide a list of affected channels, R7) give only a theoretical option to learn rare nominal events, or R9) are only possible to run  [source](https://arxiv.org/abs/2406.17826) |
| TDC | **research.google** | "We leveraged data from the Therapeutic Data Commons (TDC), a public collection of drug discovery datasets for training ML models, and processed 66 tasks most relevant to drug discovery into instruction-answer formats suitable for LLMs." [source](https://research.google/blog/tx-llm-supporting-therapeutic-development-with-large-language-models/) |
| PyOD | **tec.gov.in** | "Anomaly Detection • PyOD – Outlier detection algorithms." [source](https://www.tec.gov.in/pdf/consultations/Combined%20Standard%20on%20AI%20Robustness%20dated%2006052025-57070.pdf) |
| ADBench | **www2.camara.leg.br** | "Zhao, Nasrullah e Li (2019) apresentaram uma biblioteca de código livre e aberto (open-source) escrita na linguagem Python para a detecção de anomalias, denominada Python Outlier Detection (PyOD), que implementa mais de quarenta diferentes algoritmos." The methods then state: "Nesse sentido, foi utilizada a biblioteca Scalable Unsupervised Outlier Detection (SUOD), também escrita em linguagem Python (ZHAO et al., 2021), para agrupar em treinamento os algoritmos HBOS, ECOD, COPOD, GMM, PCA e IForest sobre dois tipo [source](https://www2.camara.leg.br/a-camara/programas-institucionais/cursos/pos-graduacao/eventos/jornadas-de-pesquisa-e-extensao/final_AnaisdaXIIIJornadadePesquisaeExtensodaCmaradosDeputadosParlamentoeInovao.pdf) |

India and Brazil are both new to the ledger. The India TEC entry is a national standards consultation
that lists PyOD in its recommended-tooling table, the same shape as the already-counted Japan MoD ATLA
row. The Brazil entry is stronger than a citation: the Chamber of Deputies research proceedings run
PyOD, SUOD, ECOD, and COPOD against Senate procurement overpricing and publish the accuracy, precision,
and recall table, with ADBench engaged in the comparison. Its coauthor Fabiano Peruzzo Schwartz directs
postgraduate coordination at the Camara's Cefor, so the row passes on authorship rather than on the
`.leg.br` domain, which is the check that demoted two rows in earlier passes. The ESA/ESOC report passes
the same test: Peter Collins and Gabriele De Canio are named as ESA/ESOC staff on the title page.

The Google Research row covers the 2024 Tx-LLM release, which is a separate item from the TxGemma
release already counted at #8f. TDC is a project Yue Zhao co-authored rather than led, and the row is
annotated that way.

### The Agent-Auditing Line Nearly Doubled Its Citation Record

Ledger 6 gained 9 rows, from 11 to 20. Four came out of tail triage rather than
the tier-ordered sweep, because those papers cite AEGIS and Auditable Agents by mechanism rather than by
a keyword any dimension query would match. The strongest compares AEGIS against NVIDIA OpenShell and
Microsoft's Agent Governance Toolkit in a capability analysis, which places the work beside two vendor
products rather than beside academic prior art. The 2026-07-31 note that Praetor was the only baseline
precedent no longer holds.

### Cross-Skill: citation-audit

`/citation-audit --source both` ran the same day. Net new: one Tier 0 (Meta Platforms citing *Edit Away
and My Face Will Not Stay*) and two Tier 1 (Tencent citing COPOD, IBM Research Dublin citing the AI
Foundation for Therapeutic Science paper). Dimensions analyzed 1368 unique citing papers.

**A defect in that pipeline was found and fixed this round.** OpenAlex has moved to a metered model:
1000 credits per day on the free tier, one credit per request, reset at midnight UTC. Resolving 116
paper identifiers spends the budget before a single citing-paper query runs. The old code retried a 429
five times, returned an empty list, and printed `0 citing papers`, so API exhaustion was recorded as a
zero-citation finding. That is the mechanism behind the `0 unique citing papers analyzed` line in this
and every prior report, and it is why Phase 1 could report 46 papers with citations while Phase 2
reported zero for all of them. `scripts/citation_affiliation_audit.py` now aborts on a long
`Retry-After`, caches Phase 1 identifiers so a re-run spends its budget on citing papers, writes a
warning block into the report, and exits 3.

### Site Defects Found Incidentally

Three award provenance links on the public surfaces do not support their claims.
`index.html:376` and `cv/cv-full.tex:316` both point at NortonLifeLock URLs that now redirect to generic
gendigital.com pages. `cv/cv-full.tex:296` and `cv/cv-1page.tex:164` cite the Capital One Research Award
to a USC Viterbi news page that returns HTTP 200 but contains no occurrence of "Zhao".

### Propagated to Site

All four Tier 0 rows reached the public surfaces in the same commit as this pass, together with the
figures they changed.

| Finding | Surface | Where |
|---|---|---|
| India TEC draft Standard on AI Robustness | `opensource.html` | PyOD impact card, new `India Gov` row |
| Brazil Chamber of Deputies proceedings | `opensource.html` | PyOD impact card, new `Brazil Congress` row, kept separate from the National Treasury row |
| ESA/ESOC requirements report | `opensource.html` | PyOD impact card, second `Space Agency` row, distinct from OPS-SAT |
| Google Research Tx-LLM naming TDC | `opensource.html` | TDC impact card, new `AI Lab` row, annotated as a co-authored project |
| Aegis compared against NVIDIA OpenShell and Microsoft Agent Governance Toolkit | `opensource.html` | Agent Auditability card, new `Vendor Comparison` row |
| Patent count, 18 to 49 | `opensource.html`, `files/bio.txt`, `llms.txt` | Patent row, bio adoption sentence, Institutional Adoption section |
| Latin America and telecommunications standards bodies added to the geography and institution-class lists | `files/bio.txt`, `index.html` | Bio adoption sentence; `index.html` regenerated through `scripts/prerender_pages.py` |
| The whole Tier 0 set | `llms.txt` | New `## Institutional Adoption` section, which previously carried no adoption evidence at all |

**Two process changes came out of this round, because the propagation step had been skipped before.**
`scripts/ci_check_site.py` now carries `check_impact_claims_agree`, which reads each figure from this
file and fails the build when a public surface disagrees; the patent count is its first entry. The
skill's Downstream Handoff step 3 was rewritten from a prose reminder into a surface table plus that
gate. The prompt for the change was finding that the bio's geography list still read "Europe, Asia,
and the Middle East" a full round after Brazil entered Ledger 1.

**Site defects found while checking, not yet fixed.** `index.html:376` and `cv/cv-full.tex:316` point
at NortonLifeLock URLs that now redirect to generic gendigital.com pages. `cv/cv-full.tex:296` and
`cv/cv-1page.tex:164` cite the Capital One Research Award to a USC Viterbi news page that returns
HTTP 200 and contains no occurrence of "Zhao". These are award-source defects rather than coverage
findings, so they are recorded here and left for a separate change.


### Held, Not Counted (31 unverifiable, 26 dropped)

31 candidates were blocked by fetch failures and are recorded as re-fetch targets rather than
as absent evidence. 26 were dropped on the Citation Verification Rule, on first-party hosting,
or on a name collision.

---

## 2026-08-09 Pass (Phase A: `/workflows` + `/prun` Discovery; Phase B: 16 Codex Verification Shards)

**Method.** The largest single run the audit has done. Phase A fanned discovery across `/workflows`
lanes and `/prun` Codex workers; Phase B then dispatched 16 Codex verification shards over the priority
candidates, partitioned by outlet class (`gov-pdf1/2/3`, `intl-gov1/2`, `journal1/2`, `press1/2`,
`fmco1/2`, `university1/2`, `standards`, `analyst`, `misc`). Phase B finished 16 of 16 shards with zero
errors: 542 records over 541 unique URLs, 45 minutes wall clock, 1,028 tool uses. Every promotion below
was reached by downloading the document and scanning its text, never from a search snippet.

**What the two phases are for is now clearly separated.** Phase A produced 1,231 candidates that were
deliberately left unverified, most of them practitioner tutorials and topic-validation matches. Phase B
spent its whole budget on the priority subset. That is the correct split: the value is in verifying the
few claims that could move a ledger, not in touching every row.

### Tier 0: Confirmed New (Ledger 1, +2)

| Work | Source | Evidence |
|---|---|---|
| PyOD 2.0 | **OpenAI Careers**, "Quantitative Threat Forecasting Analyst" | Qualifications block: *"Expertise with modern toolchains, NumPyro, TensorFlow Probability, PyMC, Darts, GluonTS/Chronos, sktime, **PyOD 2.0**, River, scikit-survival, and readiness to evaluate emerging libraries as the field evolves."* A **second, distinct** OpenAI posting naming PyOD, separate from #8g, and a stronger form: it pins a major version and places PyOD inside a named toolchain a hire is expected to already know. Live URL now 403s and the role is absent from the live Ashby feed (750 postings checked), but two Wayback captures of the canonical `openai.com` URL return HTTP 200. Committed sidecar at [`news-snapshots/openai-careers-quantitative-threat-forecasting-analyst-2025-08-10.md`](news-snapshots/openai-careers-quantitative-threat-forecasting-analyst-2025-08-10.md). |
| PyOD | **Brazil National Treasury** (Tesouro Nacional), *Cadernos de Finanças Públicas* v.22 n.01 | p40: *"Para identificar as despesas discrepantes dos municípios, foi utilizada a biblioteca Python Outlier Detection (PyOD), que conta com uma variedade de modelos para a detecção de anomalias em dados multivariados."* Operational use in a federal audit of discrepant municipal basic-education spending. Confirmed by direct PDF download (4.2 MB, HTTP 200), `pdf_term_scan.py` (7 raw matches, 6 genuine after excluding a PYODBC substring on p18), and an independent PyMuPDF pass. |

**The OpenAI row resolves a standing hold and corrects a snapshot note.** The Negative Results table
recorded that "earlier third-party mirrors of the Quantitative Threat Forecasting Analyst role naming
PyOD 2.0 remain candidate-only unless an official OpenAI URL resurfaces." Wayback captures of the
canonical first-party URL meet that condition. They also falsify the general claim in the #8g snapshot
note that OpenAI's bot policy makes its careers pages unarchivable from any client: this URL has two
clean 200 captures from July and August 2025. Check the CDX index before concluding no archive exists.

**The Brazil row reverses a 2026-07-31 demotion, on affiliation evidence the earlier pass did not have.**
That pass recorded the Treasury journal article and a TCU-school monograph as "the same study by the same
author, published twice," and routed the pair to Ledger 3 as a student course paper. The journal record
names the author as **Renata Guanaes Machado, Controladoria-Geral da União**, Brazil's federal Office of
the Comptroller General and its national internal-audit and anti-corruption body. A federal audit official
publishing peer-reviewed, DOI-bearing operational work in a finance ministry's own official series passes
the same test that admitted the BIS / Bundesbank row: the institution's own series, on its own domain,
written by a government affiliate. Annotate that the author's home body (CGU) differs from the publisher
(Tesouro Nacional), and that the TCU-school version of the same study stays in Ledger 3.

### Tier 0: Reclassified as a Mirror, Not Counted

**CISA weekly Vulnerability Summary SB26-201** carries a `yzhao062--pyod` vendor-product row for
CVE-2026-15529 (CVSS 6.3, published 2026-07-13). The Phase B shard reported it as a new Tier 0. On
coordinator review it is **a mirror of the already-counted T0-e**, and it does not increment the count.
Three facts settle it: the description text is verbatim identical to the NVD record, the CVSS score
matches exactly, and CISA's own boilerplate states that *"some of the information in the bulletin is
compiled from external, open-source reports and is not a direct result of CISA analysis."* This is the
same standard the 2026-07-31 pass applied to ENISA EUVD and CVE.org.

Record it in `mirrors[]` with one annotation that raises its standing above those two: CISA is a U.S.
federal agency and the Vulnerability Summary is a weekly bulletin distributed to subscribers, so the
adverse coverage reaches a wider operational audience than a registry lookup does. A neighbouring row in
the same bulletin, `yashbhalgat--HashNeRF-pytorch` (CVE-2026-15531), was checked and is unrelated; the
bulletin contains exactly one PyOD row.

### Tier 1: DOE National Laboratories (+2 New Labs, 1 Verdict Reversed)

**New substantive-use rows (2):**

| Lab | Work | Evidence |
|---|---|---|
| SLAC National Accelerator Laboratory | PyOD | "Coincident learning for unsupervised anomaly detection of scientific instruments" (OSTI 2426670, DOI 10.1088/2632-2153/ad64a6). PyOD invoked in the body at p25. **A new DOE lab for the ledger.** Both OSTI purl paths 404 because OSTI does not host the full text; the record was resolved through the OSTI API and then the publisher DOI. |
| Sandia National Laboratories | HPOD | "Development of Machine Learning Algorithm for Pebble Bed Modular Reactor Misuse Detection" (OSTI 2563811, 34 pages, all authors SNL-NM Albuquerque). Cites "Zhao, Yue, and Leman Akoglu. 2020. Hyperparameter Optimization for Unsupervised Outlier Detection." **The first appearance of HPOD in any government document**, and an upgrade on the Phase A read: the citation is used in the body, not only listed at p27. |

**Reversal: the single "Refuted" DOE row is wrong as stated.** The 2026-07-31 pass refuted an Oak Ridge
inverter-control report (OSTI 2333852) on the grounds that "the reference list points at the PyOD
benchmarks URL while the body never names PyOD." The sub-claim is literally true and the verdict that
follows from it is not. Reference [34] is `https://pyod.readthedocs.io/en/latest/benchmark.html`, and the
body at p5 invokes that reference in prose. A body citation of a PyOD artefact is a direct mention under
rule 6 even when the string "PyOD" does not appear in the sentence. **Move this row from Refuted (1) to
the bibliography-only group (5 becomes 6), which routes it to `/citation-audit` rather than to coverage.**

**Second reversal: a Phase A verified-negative was a false negative.** OSTI 2550614 (Brookhaven,
"Leveraging Active Subspaces to Capture Epistemic Model Uncertainty in Deep Generative Models") was
recorded in Phase A as "no matches." It is the substantive TDC row already tracked as Brookhaven / TDC
in the 2026-07-31 table. No count changes; the negative record needs deleting so a future round does not
inherit it.

### Tier 1: The Journal Footprint, Split by Use

The `journal1` shard verified 30 peer-reviewed articles across Nature, Cell Press, AAAS, RSC, and PNAS
families. Applying the same split the DOE cluster uses, because counting bibliography-only entries here
would double-book what `/citation-audit` already measures:

**Substantive in-body use, counted as coverage (12).** Highlights rather than the full list:

- **Cell Press, *Developmental Cell***: the exact module path `pyod.models.knn`, the docs URL, and the
  arXiv link all appear. The most specific PyOD usage found in any journal to date.
- **Cell Press, *iScience***: `pyod 1.0.9` with Python 3.9.16 and the HBOS detector listed as key
  resources, inside a Broad-Institute-linked JUMP morphological profiling pipeline. A pinned version in a
  key-resources table is the strongest reproducibility form of adoption.
- **Cell Press, *Stem Cell Reports***: operational single-cell use with inline author attribution.
- ***Nature Scientific Reports*** (s41598-025-09717-1): PyOD named as the implementation in Methods **and**
  ADBench cited, with `Zhao, Y.` spelled out in both references.
- ***Nature Scientific Reports*** (s41598-025-29219-4): LSCP used as the working ensemble method rather
  than cited in passing, for early prediction of very and extreme preterm birth.
- ***Nature Communications*** (s41467-026-71441-9): TDC oracle v0.4.1 used to build a fine-tuning set.
- ***Nature Communications*** (s41467-025-65869-8): TDC cited as the data-availability accession route,
  which is the strongest in-body form of dataset adoption.
- ***Nature Scientific Data***, SynRXN: names TDC as one of two exemplar standardized ecosystems the field
  should imitate, which is framing rather than a passing dataset citation.

Cell Press is a venue family the audit did not previously record for PyOD. *JGR: Biogeosciences*
(agricultural nitrous-oxide hot-moment detection) is a citation rather than substantive use, but it opens
a new discipline for the PyOD footprint and is worth watching for follow-on work.

**Reference-list only, routed to `/citation-audit` (18).** These are real citations and they belong in the
bibliometric tables, not the coverage ledger: *Science Translational Medicine*, *Nature Chemistry*,
*Nature Computational Science*, *Nature Machine Intelligence*, *Nature Reviews Bioengineering*,
*Nature Protocols*, *npj Computational Materials*, *PNAS Nexus*, *Chemical Science*, *Cell Reports
Physical Science*, *JGR: Biogeosciences*, five *Scientific Reports* entries, and two more *Nature
Communications* entries. Every TDC row in both groups carries the standing coauthorship-dilution
annotation.

**One row re-promotes work an earlier round demoted.** *Scientific Reports* s41598-025-28976-6 (hybrid
autoencoder / variational autoencoder outlier detection) cites ADBench, SUOD, **and** LSCP. It is one of
three *Scientific Reports* items that Codex Round 2 sent back to the candidate pool on 2026-07-31 for
lack of verified evidence. The evidence now exists.

### Tier 1: Other Confirmed New Items

- **CSET, Georgetown**, *Operationalizing AI Guidance*: reference [742] is *"Kaixiang Zhao, Lincan Li,
  Kaize Ding, Neil Zhenqiang Gong, Yue Zhao, and Yushun Dong, 'A Survey on Model Extraction Attacks and
  Defenses for Large Language Models,' KDD '25."* Held at Tier 1 rather than Tier 0: CSET is a
  university-based policy research center, not a government or standards body. The fetch path is worth
  recording, since `cset.georgetown.edu` returns 403 to curl even with full browser headers.
- **Indonesian Ministry of Finance**, *Jurnal Manajemen Perbendaharaan*. **Resolved 2026-08-09 and
  promoted to Tier 0 as Ledger 1 row 2h, with the strength of the mention corrected downward.** The
  institutional test passes on all three legs, more cleanly than the Brazil row: the three authors are
  all at the **Direktorat Jenderal Perbendaharaan, Kementerian Keuangan** (Directorate General of
  Treasury, Ministry of Finance), the correspondence address is `azulfikar@kemenkeu.go.id`, and the
  journal is published by that same directorate on the ministry's own domain. Author body and publisher
  body are identical here, where Brazil's differ. The Phase A summary claimed PyOD was used to detect the
  anomalies; full extraction shows otherwise. PyOD appears **once in 15 pages**, "Zhao" appears **zero**
  times, and the paper implements Isolation Forest through scikit-learn. The single sentence reads
  *"...ROC yang dilakukan menggunakan benchmark data dari python outlier detection package (PyOD)"*: the
  PyOD benchmark supplied the ROC comparison that justified selecting Isolation Forest. Count it as a
  benchmark citation that drove a methodological decision, not as implementation use, and record that it
  carries no reference-list entry.

**Two Phase B "new" claims are duplicates and are not counted:** the Salesforce Hiroshima AI Process
transparency report (already T0-d) and the FLI AI Safety Index Summer 2026 PDF (already T1-a). Both were
independently re-downloaded and rescanned, so they stand as evidence refreshes.

### Notable Negatives and Collisions

Phase B dropped a large number of candidates on direct fetch. The instructive ones:

- **The EDPB name collision is the single best argument for the no-snippet rule.** *AI Privacy Risks &
  Mitigations: Large Language Models* is an official EU-body PDF, and a term scan returns three TrustLLM
  hits. A snippet reader scores that as a Tier 0 EU citation. All three are the EU Horizon Europe project
  `trustllm.eu`, an EuroHPC JU consortium unrelated to Sun / Zhao et al.
- **Aegis collisions now outnumber Aegis citations.** Confirmed this round: Forrester's own AEGIS
  enterprise-guardrails framework (30 occurrences, all Forrester's), NVIDIA's AEGIS content-safety dataset
  inside Mistral's Shieldstral report, Aegis Authenticator (an Android 2FA app) in two Help Net Security
  pieces, and a fictionalized "Aegis" company name in a Salesforce agent-hacking write-up.
- **Person-name collisions confirmed by direct fetch:** a University of Arkansas power-electronics
  professor (two USC-adjacent-looking award pages), a Xidian University spectrum-monitoring researcher, a
  Peking University HSBC Business School optimization researcher, a Barcelona-based product leader
  interviewed by Forbes, and an astrophysics Yue Zhao in the NASA NTRS corpus. The `gov.uk` public search
  API returns 203 hits for "Yue Zhao," every inspected one an employment-tribunal or product-recall record.
- **"Auditable" as an ordinary English adjective keeps producing phantom hits** in PNNL, LBNL, GAO, and
  OWASP documents. The 2026 OWASP GenAI LLM Top 10, six days old at scan time, matches only on
  "enforced in a deterministic and auditable manner."
- **NASA is a clean negative** for the entire FORTIS inventory across an NTRS API sweep.
- **A scanner fix was validated:** adding `FALSE_POSITIVE_CTX['PyOD'] = ['Pyodide', 'pyodide', 'pyodbc']`
  suppresses the Pyodide substring, which the word-boundary rule misses because PyOD is four characters
  and mixed case, so it takes the case-insensitive substring path. CISA bulletin SB26-194 was a pure
  Pyodide false positive.

**Could not fetch, held rather than refuted:** `nccoe.nist.gov/projects/cyber-ai-profile` (403 from every
client tried), `congress.gov` (403, and govinfo returned 429 on `DEMO_KEY`), and OSTI 2502113 (404).

### Registry Harvest

To append to `references/domain-registry.md`:

- **New gov-pdf entries:** `cisa.gov` (method note: the search endpoint is a JavaScript shell, but the
  bulletin pages at `/news-events/bulletins/sbYY-NNN` are server-rendered and fetch cleanly with browser
  headers), `regulations.gov` plus `downloads.regulations.gov` and `api.regulations.gov`.
- **New web-archive class:** `web.archive.org` plus the CDX endpoint. Wayback is now a proven discovery
  route for closed careers pages, and it produced this round's flagship Tier 0 row.
- **New foundation-model-company entries:** `microsoft.com`, `docs.aws.amazon.com`, `arxiv.org` (where
  Amazon Nova and Mistral Shieldstral publish technical reports), `storage.googleapis.com` (host for
  DeepMind model cards and Frontier Safety Framework reports), `developers.google.com`.
- **New consulting / analyst class**, which does not exist yet even though `deloitte.com` is already a
  confirmed-hit domain.
- **Outlet correction:** SC Media now publishes at `scworld.com`; `outlet-registry.md` still lists
  `scmagazine.com`.

To append to `references/disambiguation-registry.md`:

- **Tool-name collisions:** `combo` (require `yzhao062/combo` or "toolbox for machine learning model
  combination"), `TODS` (require "time series outlier detection" or the `datamllab/tods` repo, since bare
  TODS is *ACM Transactions on Database Systems* in any data-management bibliography), `ECOD` extended to
  the structural-biology ECOD protein-domain database, and PyOD extended to TechCrunch's 2015 "PYOD"
  product, which is the only result a `site:techcrunch.com` PyOD query returns.
- **Person-name collisions:** the University of Arkansas power-electronics Yue Zhao, the astrophysics Yue
  Zhao in NASA NTRS, and "Summer Yue" (Meta director of safety and alignment), sighted twice this round in
  Tier 1 security coverage where a "Yue" token reads as a hit.
- **Project-name collisions:** `tdcommons.org` (Google's Technical Disclosure Commons, distinct from
  `tdcommons.ai`), and the `trustllm.eu` entry extended to name `eurohpc-ju.europa.eu` as a second host.
- **Product and standard collisions, all new:** Google Cloud now ships a product literally named "Agent
  Anomaly Detection," so that phrase can no longer be treated as PyOD-adjacent. OWASP's "AOS / Agent
  Observability Standard" is adjacent to but distinct from agent auditability, and an AOS hit is not
  coverage. ISACA's AAIA (Advanced in AI Audit) certification sits one letter from AAS-1 and both rank on
  "agent audit standard" queries; ISACA also ships AAISM and AAIR, so AAI\* is a growing collision family.
  A third distinct claimant now uses "accountability layer for AI agents" as a title, alongside the
  already-registered `aegis-protocol` blockchain usage.

### Security Finding: Version Range Reconciled and the Fix Confirmed Shipped

The audit's earlier note on CVE-2026-15529 is stale in three ways, all corrected in the Security Finding
section below. NVD itself now reads "up to 3.6.1" rather than 3.5.0/3.5.1/3.5.2; the record was modified
2026-07-20 and its status is Deferred, which is why the CPE configuration block is empty. Fix PR #698 and
release PR #703 both merged 2026-07-20 (commit 22c119b3, "Harden persistence.compat_load() with trusted
gate; finalize v3.6.2"). Version 3.6.2 shipped, and PyPI now serves 3.6.4. The audit's claim that "the
fix is unmerged" no longer holds.

### Propagated to Site

Per the Downstream Handoff rule in `skills/news-search/SKILL.md`:

- **PyOD impact card** in `opensource.html`: the second OpenAI posting naming PyOD 2.0, the Brazil National
  Treasury operational row, and the SLAC addition to the DOE cluster.
- **PyOD card, scientific-venue line**: Cell Press (*Developmental Cell*, *iScience*, *Stem Cell Reports*)
  as a new venue family.

Held back from the site: the CISA bulletin, which is adverse coverage and a mirror; the Indonesian
ministry row, pending the affiliation check; and every reference-list-only journal row, which belongs to
`/citation-audit`.

---

## 2026-07-31 Pass (Cross-Vendor: 6 Codex lanes via `/prun` + 6 Claude lanes via `/workflows`)

**Method.** Full audit run on both engines at once, with complementary dimension assignments. Six Codex
lanes took the fetch-heavy work (D8 U.S. government PDFs, D8 international and standards and analyst
PDFs, D2 plus D3 security and enterprise outlets, D7 education and code ecosystem and non-English, D5
smart-keyword search over all 42 papers from 2026, D5 over the 77 older papers plus all 21 tools). Six
Claude lanes took discovery (D1 person and lab, D3 mainstream press, D4 topic proximity, D6 citation
and downstream, D2 careers pages, and a dedicated lane for the newest works and the post-repositioning
vocabulary). 406 raw records merged to **366 unique candidates** in `news-search-candidates.jsonl`.

**Cross-vendor overlap was only 3 of 366, and that is a design artifact, not a disagreement.** Because
the two engines were given complementary rather than identical dimensions, disjointness was expected;
coverage roughly doubled but the "found by both vendors" confidence signal is unavailable. A future
round that wants that signal must give both engines the same task and pay for the duplication.

**Verification discipline is the story of this round.** Nineteen high-tier claims arrived from the
worker lanes. The coordinator re-fetched every one of them, and **11 needed correction**. Two dedicated
adversarial Codex verification lanes were then dispatched for the claims the coordinator had not
personally checked. The corrections fall into four repeating patterns, all worth carrying forward:

1. **Coauthor-institution publication listings promoted to Tier 0 or Tier 1.** Microsoft Research pages
   for TrustGen, TrustLLM, and ADMoE, plus IBM Research for TrustLLM. All are bare publication records
   on the site of an institution that employs a coauthor. Phase B step 1 already says to demote these
   to Ledger 3; the worker contract for this round omitted that rule, which is a coordinator error, not
   a worker error. **Fix for future fan-outs: the pre-tier filter must be copied into the worker contract verbatim.**
2. **Host mistaken for author.** A Parliament of Australia URL is a University of Sydney submission that
   parliament merely hosts. A Brazil TCU URL is a student's final course paper at the TCU's own school,
   not a TCU audit product. An OSTI record reported by Sandia has authors at George Mason University.
   Institutional domains are not institutional authorship.
3. **Same item counted several times.** CVE-2026-15529 arrived as three separate Tier 0 claims (NIST NVD,
   ENISA EUVD, CVE.org). NVD was already counted on 2026-07-19 as row T0-e. The other two are registry
   mirrors of the identical text and belong in `mirrors[]`, not in the count. The Brazil TCU monograph
   and the Brazil National Treasury journal article are the same study by the same author, published twice.
4. **Same-domain name collisions in the citation graph.** Two of seven Semantic Scholar citation edges
   were false. Both are recorded as new entries in `references/disambiguation-registry.md`.

### Tier 0: Confirmed New (Ledger 1)

| Work | Source | Evidence |
|---|---|---|
| PyOD | **Japan Ministry of Defense (ATLA)** | AI Guideline v01 (English, June 2025) lists PyOD as **entry 14 in its recommended-tooling table**, mapped to guideline sections B-5 (Ensuring Reliability and Validity) and B-6 (Ensuring Safety), linking both `github.com/yzhao062/pyod` and the docs. p27: "In B-6, for ensuring safety, the Python library PyOD (Python Outlier Detection), which provides a wide range of algorithms for detecting outliers, is useful for designing ...". Coordinator-verified with `pdf_term_scan.py`, 8 matches. **The second national defense ministry to name PyOD as recommended tooling, after U.S. DoD CDAO.** |
| PyOD, DCSO, LSCP | **Bank for International Settlements / Irving Fisher Committee** | IFC Bulletin 57, "Unsupervised outlier detection in official statistics", by Nhan-Tam Nguyen and colleagues at the **Deutsche Bundesbank** and DFKI, presented at the IFC / Bank of Italy workshop on machine learning in central banking. p10 selects PyOD as modelling tooling alongside scikit-learn; p24 carries a DCSO algorithm flowchart "adapted from Zhao et al. (2018)"; p45 cites PyOD (JMLR) and LSCP. Coordinator-verified, 6 matches. Annotate as central-bank research practice published by an international body, not as official policy guidance. |

### Tier 0: Counted, With the Right Annotation

Adversarial verification lane V1 confirmed each of these names the work. All are counted. What follows
are the annotations that keep the claim proportionate, not reasons to exclude.

Two standards were corrected during this round, because the first pass applied them wrongly:

- **A personal-views disclaimer does not weaken an institutional research series.** "The views expressed
  are those of the authors" is standard boilerplate across Federal Reserve, ECB, BIS, IMF, and FSA
  working-paper and discussion-paper series. Discounting it would discount essentially the whole
  central-banking and financial-regulation research literature. The operative test is whether the
  document appears in the institution's own official series, written by its staff or affiliates and
  published on its domain. That is institutional uptake, distinct from policy endorsement.
- **Do not demand USC attribution for pre-USC work.** Therapeutics Data Commons dates from the PI's
  CMU period; he joined USC in August 2023. Treating "USC is not named" as a defect in a TDC-era
  document is anachronistic. The only live qualification on TDC rows is coauthorship dilution, since
  TDC is Harvard-led with many coauthors, and that is handled by annotation.

| Work | Source | Annotation |
|---|---|---|
| TrustLLM | **Japan Financial Services Agency**, FSA Institute Discussion Paper DP2024-3 | Substantive body use: the paper invokes the TrustLLM framework for the eight dimensions of LLM trustworthiness, with the full citation as footnote 21 and a second entry in the references. Published in the FSA Institute Discussion Paper Series. Discussion paper, not FSA policy. |
| Therapeutics Data Commons | **Japan METI**, GENIAC selection results | TDC supplied the drug-discovery benchmark task used to evaluate a funded model. Real platform adoption by a national ministry's programme. Coauthorship dilution applies: TDC is Harvard-led and the PI is one of many coauthors. |
| Therapeutics Data Commons | **Japan NEDO**, joint release with SyntheticGestalt | States that TDC "is standardly used" as the performance benchmark in AI drug discovery. NEDO is a co-issuer, not merely a host. Same coauthorship annotation. |
| PyOD | **NIST**, "Science ex Machina" (Isotope Metrology Webinar Series) | Counted, and the weakest item in this table. An 18-page deck by a named NIST scientist whose sole mention is the bullet "e.g., VAE, Deep NN, pyOD" under a Machine Learning heading. A NIST scientist listing PyOD among go-to tools is a genuine signal; it is a mention rather than a documented use, and the row says so. |

### Tier 1: DOE National Laboratories, Verified and Split by Use

Verification lane V2 downloaded all 12 OSTI PDFs (269 pages, pypdf) and classified each by whether the
work is used in the body or only listed in the references. This split matters because bibliography-only
entries are bibliometric evidence that `/citation-audit` already measures; counting them here would
double-book the same fact.

**Substantive use, counted as coverage (6):**

| Lab | Work | Evidence |
|---|---|---|
| Sandia National Laboratories | PyOD | "our anomaly detection was implemented based on PyOD [36], an open-source Python toolbox for performing scalable outlier identification" (APT detection via provenance analysis, 2025) |
| Brookhaven National Laboratory | COPOD | COPOD offered as one of three anomaly-detection algorithms in an exascale workflow data-reduction system (2025) |
| Idaho National Laboratory | TrustLLM | "probably the most comprehensive benchmark of trustworthiness in LLMs available to date ... evaluating 16 mainstream LLMs using 30 datasets" (nuclear power plant human-AI interaction, 2025) |
| Oak Ridge National Laboratory | LSCP | LSCP among six outlier-detection methods used to verify cyber-attack detection accuracy (HVDC attack-defense control, 2021) |
| Lawrence Livermore National Laboratory | TrustLLM | FY24 LDRD Annual Report describes the TrustLLM framework and Kailkhura's participation (2025) |
| Brookhaven National Laboratory | TDC | "We utilized the oracles from Therapeutics Data Commons [31]" (molecular design uncertainty, 2024). TDC caveat applies. |

**Bibliography-only, routed to citation evidence rather than the coverage ledger (5):** DESI/LBNL
(ADBench), Oak Ridge (PyOD, grouped marker), Los Alamos (PyOD, IAEA declarations report), Sandia-reported
OSTI record whose authors are at George Mason University (LSCP), and the LLNL multi-lab SafeAI report
(TrustLLM), which is in any case already tracked. ~~**Refuted (1):** an Oak Ridge inverter-control report
whose reference list points at the PyOD benchmarks URL while the body never names PyOD.~~
**Corrected 2026-08-09: this row is not refuted.** OSTI 2333852 reference [34] is the PyOD benchmarks URL
and the body at p5 invokes that reference in prose, which is a direct mention under rule 6 even though the
string "PyOD" is absent from the sentence. **Bibliography-only is therefore 6, and Refuted is 0.** See
"## 2026-08-09 Pass".

### Tier 1: Third-Party Academic Citations of the Agent-Auditing Line

The Claude lanes pivoted from keyword search to the Semantic Scholar citation graph and then fetched each
citing paper. The coordinator re-downloaded all seven and extracted the text with PyMuPDF. **Five hold,
two are refuted.**

| Citing work | Cites | Evidence |
|---|---|---|
| arXiv:2607.25364, "Explanation-Bound Tool Execution for AI Agents: Server-Verified Action Claims Without Trusting Model Rationales" (Georgia Tech, UIUC; v1 submitted 2026-07-28 as *Accentrust*, retitled in v2 on 2026-07-29) | Auditable Agents **and** agent-audit | Body discussion, not a bare reference: "Auditable Agents frames recoverability, policy checkability, responsibility attribution, and evidence integrity as system properties [24]; Agent Audit analyzes code and deployment artifacts before execution [25]." Strongest citation of the round and inside the post-cutoff window. |
| arXiv:2607.07405, "Reason Less, Verify More" | Aegis | Credits Aegis as prior art that establishes the mechanism: "our contribution is therefore not the enforcement mechanism, which pre-execution systems such as AEGIS [12] and AgentSpec [9] already establish". |
| arXiv:2607.01641 | agent-audit | Reference [39], full title and arXiv ID. |
| arXiv:2604.15367 | agent-audit | Reference [50], full title and arXiv ID. |
| arXiv:2509.24380, Agentic Services Computing survey | agent-audit | Reference [147] plus three body mentions. Revised version, so the ID predates the cited work. |

**Refuted:** arXiv:2606.04990 was reported as a survey citing Auditable Agents; the 28-page PDF contains
zero occurrences of Auditable Agents, 2604.05485, Yue Zhao, or agent-audit, and the Aegis it cites is
Kong et al., arXiv:2509.14295, "Automated error generation and attribution for multi-agent systems".
arXiv:2606.00765 (FALAT) was reported as the sole external citer of Implicit Execution Tracing; it
actually cites "implicit execution traces [Li et al., 2025b]", a different 2025 work. **After
verification, Implicit Execution Tracing has zero confirmed external citers and the FORTIS over-privilege
benchmark has zero external citers (all Semantic Scholar citers are lab-internal).**

### Tier 1 and Tier 2: Other Confirmed New Items

- **Cloud Security Alliance Labs**, CISO Daily Briefing 2026-04-03, prints the exact title of *No Attacker
  Needed: Unintentional Cross-User Contamination in Shared-State LLM Agents*. Coordinator-verified. Names
  no author and no institution, so the row records title-only attribution.
- **Foresight Institute** grantee page names Yue Zhao, USC, and the FORTIS Lab by full expansion, with the
  project title "Audit-to-Patch Pipelines for Secure LLM Agent Systems". The only third-party page found
  that names the lab itself rather than only the person.
- **ACM SIGSPATIAL** official award-recipients roster (2025 Best Short Paper, TyphoFormer) and **Amazon
  Science** research-award recipient page, both by-name with affiliation.
- **Grokipedia (xAI)** carries a full biographical entry naming PyOD, PyGOD, TDC, TrustLLM, FORTIS Lab,
  and USC. A new encyclopedia surface distinct from the already-tracked Wikipedia entry.
- **USC Viterbi News** July 2026 conference roundups print the Auditable Agents paper title with the full
  author line, and a second item covers the ICML 2026 paper.
- **TechTarget** "anomaly detection" definition names PyOD ("PyOD, an open source anomaly detection
  library written in Python"). Demoted from the claimed Tier 1 to **Tier 2**: this is a glossary entry
  rather than a press feature, and it names neither the PI nor USC.

### The Flagship Tier 0(b) Row Nearly Became Uncitable

The OpenAI "Technical Intelligence Analyst" posting that names PyOD (Ledger 1 #8g) **now returns HTTP 404**.
It is absent from OpenAI's live job feed, **no Wayback snapshot exists** (CDX returns an empty array), and
the successor posting ("Quantitative Intelligence Analyst", published 2026-07-14, same team) has dropped
the PyOD bullet entirely in favour of generic "data mining, statistical modeling, and supervised learning".

The row survives **only** because of the committed local sidecar. `pdf_term_scan.py` against
`news-snapshots/openai-careers-technical-intelligence-analyst-2026-05-07.pdf` still returns the exact
quote on p2. This is precisely the failure the Tier 0(b) snapshot-or-hold rule was written to prevent, and
it validates that rule. Two consequences: the row must be annotated with the 404 date and the successor's
removal of the mention, and the audit should treat any future Tier 0(b) claim as unsafe until its sidecar
is committed. Note also that the workflow's adversarial verifier marked this row REFUTED because it
checked only the live URL; that is a verifier-design gap, since a repo-committed snapshot is valid evidence.

### D2 Careers Sweep: A Strong Negative

The careers lane scanned roughly 95 job boards, including OpenAI's 749 live postings through its own Ashby
API and Anthropic's 400 through Greenhouse, plus Google, Amazon, Microsoft, and Apple first-party search
endpoints and about 50 enterprise, security, and fintech boards. **Zero** live postings anywhere name PyOD,
ADBench, PyGOD, TrustLLM, TDC, SUOD, AD-AGENT, agent-audit, Aegis, or FORTIS. This is a well-bounded
negative and should suppress re-running the same sweep for at least a quarter.

### Notable Negative and Collision Findings

- **Mainstream tech and business press remain a clean zero for the agent-auditing line.** MIT Technology
  Review, IEEE Spectrum, Forbes, Synced, MarkTechPost, Unite.AI, and the AI-newsletter tier (Import AI,
  The Sequence, Last Week in AI, Gary Marcus, AI Snake Oil, Simon Willison) name none of the works. The
  PyOD footprint in that tier is real but confined to practitioner tutorials and mostly predates 2026.
- **Unite.AI "Why Do AI Agents Favor Unnecessarily Powerful Tools?"** looks in search snippets like coverage
  of the FORTIS over-privilege benchmark. It is actually about ToolPrivBench (arXiv:2606.20023) from the
  Chinese Academy of Sciences, CUHK, and Peking University. A pure topic collision that snippet-reading
  would have scored as a false positive.
- **VentureBeat could not be read** (403 through the fetcher, 429 through curl) and its security desk
  publishes heavily on agent auditing. It is the single highest-value unchecked target for the next round.
- **The USC Institute on Ethics and Trust in Computing has not published the Associate Co-Director
  appointment anywhere on its own site**, so that July 2026 item remains self-sourced only.
- 78 verified-negative records were added to the candidates file this round, the largest single-round
  addition of cumulative "do not re-check" evidence so far.

### Propagated to Site

Per the Downstream Handoff rule in `skills/news-search/SKILL.md`:

- **PyOD impact card** in `opensource.html`: Japan MoD ATLA, BIS / Bundesbank, and the DOE
  substantive-use cluster.
- **Agent Auditability Line card**: the five confirmed third-party academic citations.
- **TDC card**: the METI and NEDO rows, worded as platform adoption rather than personal attribution.
- **`files/bio.txt`**: the government-adoption sentence rewritten as an aggregate that names only the
  U.S. institution, covering defense ministries, central banks, financial regulators, and national AI
  authorities across Europe, Asia, and the Middle East.

Held back from the site: the NIST slide-deck mention, which is real but too thin to carry a public row;
the Brazil course paper, which is Ledger 3; and the CVE registry mirrors, which are adverse coverage.

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
corresponds to repo issue #697 (2026-06-10) and fix PR #698, "Require explicit trust for
persistence.load".

**Status as of 2026-08-09: resolved and shipped.** PR #698 and release PR #703 ("v3.6.2: security
release") both merged 2026-07-20, commit `22c119b3`, "Harden persistence.compat_load() with trusted gate;
finalize v3.6.2". Version 3.6.2 was published to PyPI and the current release is now 3.6.4.

Three details in the original note were stale and are corrected here. NVD's description now reads
**"up to 3.6.1"** with "Upgrading to version 3.6.2 is able to address this issue," rather than the
3.5.0/3.5.1/3.5.2 list recorded on 2026-07-19; the record was modified 2026-07-20. Its `vulnStatus` is
**Deferred**, which is why the CPE configuration block is empty and why no machine-readable version range
is served. The claim that the fix was unmerged no longer holds.

**Mirrors of this single CVE** (recorded so a future round does not count them again): ENISA EUVD,
CVE.org, VulDB (`vuldb.com/vuln/377872`), and **CISA weekly Vulnerability Summary SB26-201**, whose
`yzhao062--pyod` row carries text verbatim identical to NVD's and whose own boilerplate states that the
bulletin "is compiled from external, open-source reports and is not a direct result of CISA analysis."
CISA is the strongest of the four as a distribution surface, since it is a federal weekly bulletin sent to
subscribers, and it still does not increment the count.

Tracked here because an NVD entry against PyOD affects the compliance posture of the government and
enterprise deployments recorded in Ledger 1 and Ledger 3. Now that the fix has shipped, the operative
question for those deployments is pinned-version drift rather than exposure.

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
| 2c | PyOD | **Japan Ministry of Defense (ATLA)** | AI Guideline v01 (English, Jun 2025) lists PyOD as **entry 14 in the recommended-tooling table**, mapped to sections B-5 (Ensuring Reliability and Validity) and B-6 (Ensuring Safety), linking `github.com/yzhao062/pyod` and the docs. p27: *"In B-6, for ensuring safety, the Python library PyOD (Python Outlier Detection), which provides a wide range of algorithms for detecting outliers, is useful for designing ..."*. Verified 2026-07-31 via `pdf_term_scan.py`, 8 matches. **Second national defense ministry to name PyOD as recommended tooling.** | Jun 2025 |
| 2d | PyOD, DCSO, LSCP | **BIS / Irving Fisher Committee** (Deutsche Bundesbank authors) | IFC Bulletin 57, "Unsupervised outlier detection in official statistics", presented at the IFC / Bank of Italy workshop on machine learning in central banking. p10 selects PyOD as modelling tooling; p24 carries a DCSO flowchart *"adapted from Zhao et al. (2018)"*; p45 cites PyOD (JMLR) and LSCP. Verified 2026-07-31, 6 matches. Central-bank research practice published by an international body. | 2021 |
| 2e | TrustLLM | **Japan Financial Services Agency** | FSA Institute Discussion Paper DP2024-3 invokes the TrustLLM framework for the eight dimensions of LLM trustworthiness; full citation as footnote 21 plus a references entry. Discussion-paper series, not FSA policy. | 2024 |
| 2f | Therapeutics Data Commons | **Japan METI / NEDO** | METI's GENIAC results page reports a funded model evaluated on TDC-supplied drug-discovery benchmark tasks; the NEDO joint release states TDC *"is standardly used"* as the AI drug-discovery benchmark. Platform adoption by a national ministry programme. TDC is Harvard-led with many coauthors; the PI is one of them, and the work predates his USC appointment. | 2025-2026 |
| 2g | PyOD | **Brazil National Treasury** (Tesouro Nacional) | *Cadernos de Finanças Públicas* v.22 n.01, "Subsídio às Fiscalizações Públicas: Identificação dos Municípios com gastos discrepantes na Educação Básica" (DOI 10.55532/1806-8944.2022.158). p40: *"Para identificar as despesas discrepantes dos municípios, foi utilizada a biblioteca Python Outlier Detection (PyOD)..."*. Operational use in a federal audit of discrepant municipal basic-education spending. Author **Renata Guanaes Machado, Controladoria-Geral da União**, Brazil's federal internal-audit and anti-corruption body; publisher is the National Treasury, so author body and publisher body differ. The TCU-school version of the same study stays in Ledger 3. Verified 2026-08-09 by PDF download plus two independent text extractions. | 2022 |
| 2h | PyOD | **Indonesian Ministry of Finance** (Kementerian Keuangan) | *Jurnal Manajemen Perbendaharaan* v.4 n.1 (DOI 10.33105/jmp.v4i1.435), published by the ministry's own Directorate General of Treasury. p4: *"...ROC yang dilakukan menggunakan benchmark data dari python outlier detection package (PyOD)"*. The PyOD benchmark supplied the ROC comparison that justified selecting Isolation Forest for auditing consumable-goods spending by Indonesian National Police work units. All three authors are at the Directorate General of Treasury (`azulfikar@kemenkeu.go.id`), so author body and publisher body match. **Weakest form in this ledger alongside 3b:** PyOD appears once in 15 pages, carries no reference-list entry, and the implementation is scikit-learn Isolation Forest. A benchmark citation that drove a methodological choice, not implementation use. Verified 2026-08-09 by PDF extraction. | 2023 |
| 3 | TrustLLM | **NIST AI 100-2e2025** | Named in Section 3.6 "Benchmarks for AML Vulnerabilities" as a benchmark for six dimensions of trust in LLMs. NIST Special Publication on Adversarial Machine Learning. | Mar 2025 |
| 3b | PyOD | **NIST**, "Science ex Machina" (Isotope Metrology Webinar Series) | An 18-page deck by a named NIST scientist whose sole mention is the bullet "e.g., VAE, Deep NN, pyOD" under a Machine Learning heading. Counted on 2026-07-31 and the weakest row in this ledger: a NIST scientist listing PyOD among go-to tools is a genuine signal, but it is a mention rather than a documented use. *(Row added 2026-08-09; the 2026-07-31 pass counted this item in prose without writing a ledger row.)* | 2025 |
| 4 | TrustLLM | **Future of Life Institute** | Official benchmark in AI Safety Index (Inaugural Edition). | Dec 2024 |
| 5 | TrustLLM | **Future of Life Institute** | Official benchmark in AI Safety Index (Summer 2025). Pages 5, 9, 11, 17, 34, 36, 37. | Jul 2025 |
| 6 | TrustLLM | **Future of Life Institute** | Official benchmark in AI Safety Index (Winter 2025). Pages 7, 11, 13, 21, 27, 43, 46. Full indicator definition p.46. | Dec 2025 |
| 7 | TrustLLM | **Future of Life Institute** | Dedicated TrustLLM Indicator Data Sheet with scores for 8 AI companies. | Nov 2025 |
| 7b | TrustLLM | **Future of Life Institute** | Official benchmark in AI Safety Index (Summer 2026), the fourth edition. TrustLLM on pp. 6, 10, 13, 45, plus pp. 25 and 42 on independent recount; p25 gives the full title and arXiv:2401.05561, p45 defines and scores the benchmark. Re-downloaded and rescanned 2026-08-09 (4.6 MB, 12 matches across pp. 6, 10, 13, 25, 42, 45). *Verified 2026-07-19 as T1-b; the 2026-07-19 pass routed it to Ledger 2, which was inconsistent with rows 4 through 7. Placed here 2026-08-09 alongside the other FLI editions.* | Jul 2026 |
| 8 | PyOD | **European Space Agency (ESA/ESOC)** | All 30 anomaly detection algorithms in the OPS-SAT spacecraft telemetry benchmark implemented using PyOD 1.1.2. Published in **Nature Scientific Data** (2025). | 2025 |
| 8b | TrustLLM | **International AI Safety Report 2026** | Citation #881. Led by Yoshua Bengio, authored by 100+ AI experts, backed by 30+ countries and international organisations. Published Feb 2026. | Feb 2026 |
| 8c | DoxBench | **Privacy International** | Cited on p.28, footnote 56: "Luo W., Qiming Z., Lu T., Liu X., Zhao Y., Xiang Z., Xiao C., 'Doxing via the Lens: Revealing Privacy Leakage in Image Geolocation for Agentic Multi-Modal Large Reasoning Model'" in "Nowhere to Hide? Privacy Risks and Policy Implications of AI Geolocation." | Feb 2026 |
| 8d | TrustLLM | **LLNL / DOE National Labs SafeAI report** | "Safety in Artificial Intelligence: Challenges and Opportunities for the U.S. National Labs and Beyond" cites "Position: TrustLLM: Trustworthiness in Large Language Models" as reference [34]. | Dec 2024 |
| 8e | TrustLLM | **MITRE LILAC v1 technical report** | "Emerging Risks and Mitigations for Public Chatbots: LILAC v1" cites TrustLLM in the text and reference list as a test case / metric for LLM trustworthiness. MITRE report MTR240382, approved for public release. | Sep 2024 |
| 8f | TDC | **Google DeepMind / Google Research TxGemma** | Official TxGemma report and Google Developers pages name Therapeutics Data Commons (TDC) as the task/data source for TxGemma training and evaluation across 66 therapeutic development tasks. | Apr 2025 |
| 8g | PyOD | **OpenAI Careers** | Official OpenAI Careers "Technical Intelligence Analyst, San Francisco" listing, Qualifications section: "Have experience with anomaly detection tools, such as PyOD, and discovery processes for surfacing novel or low-prevalence patterns." Operational adoption signal from a foundation-model company; placed in Ledger 1 as Tier 0(b)-equivalent foundation-model-company official content. Live URL is volatile (careers pages are pulled when roles close) and Wayback Save Page Now returns "Job failed" because OpenAI blocks the Internet Archive crawler; durable evidence is kept locally at [`news-snapshots/openai-careers-technical-intelligence-analyst-2026-05-07.md`](news-snapshots/openai-careers-technical-intelligence-analyst-2026-05-07.md) with browser-captured `.html` / `.pdf` sidecars in the same folder. **Correction (2026-08-09): the claim that OpenAI's bot policy blocks the Internet Archive from any client is too strong.** See #8h. | May 2026 |
| 8h | PyOD 2.0 | **OpenAI Careers** | A **second, distinct** OpenAI posting naming PyOD: "Quantitative Threat Forecasting Analyst", qualifications block, *"Expertise with modern toolchains, NumPyro, TensorFlow Probability, PyMC, Darts, GluonTS/Chronos, sktime, **PyOD 2.0**, River, scikit-survival, and readiness to evaluate emerging libraries as the field evolves."* Stronger than #8g: a pinned major version inside a named toolchain a hire is expected to already know. Live URL now 403s and the role is gone from the live Ashby feed, but the canonical `openai.com` URL has two Wayback captures at HTTP 200 (2025-07-19, 2025-08-10). Durable evidence at [`news-snapshots/openai-careers-quantitative-threat-forecasting-analyst-2025-08-10.md`](news-snapshots/openai-careers-quantitative-threat-forecasting-analyst-2025-08-10.md) plus a committed `.html` sidecar. Resolves the standing "candidate-only unless an official OpenAI URL resurfaces" hold in Negative Results. | 2025 |
| 9 | PyOD | **UK Government**, gov.uk Algorithmic Transparency Record | London Borough of Sutton "Access Assure" record links the PyOD KNN documentation in the Tier 2 Model Specification, section 4.2.6. A UK government **production deployment** record, not a literature citation. *(Verified 2026-07-19 as T0-a; row written 2026-08-09.)* | 2025 |
| 10 | PyOD | **Saudi SDAIA**, Deepfakes Guidelines v1 | `pdf_term_scan.py` confirmed PyOD on p10 of the canonical 33-page PDF; the OECD.AI mirror was fetched independently. *(Verified 2026-07-19 as T0-b; row written 2026-08-09.)* | Sep 2024 |
| 11 | TrustLLM | **US DOE / ORNL**, technical report ORNL/TM-2025/3935 (OSTI 3002371) | "Scalable Workflow for Evaluating Trustworthiness of Large Language Models". 11 literal TrustLLM occurrences across pp. 5, 8, 9, 15, 20, including substantive workflow discussion. *(Verified 2026-07-19 as T0-c; row written 2026-08-09.)* | 2025 |
| 12 | TrustLLM | **G7 Hiroshima AI Process / OECD**, Salesforce Transparency Report | TrustLLM confirmed on p4 of the eight-page PDF; re-downloaded and rescanned 2026-08-09. OECD hosts the report but explicitly leaves responsibility with Salesforce. *(Verified 2026-07-19 as T0-d; row written 2026-08-09.)* | 2025 |
| 13 | PyOD | **NIST NVD**, CVE-2026-15529 | Names `yzhao062--pyod`, links the canonical repo, and as of the 2026-07-20 modification reads "up to 3.6.1", fixed in 3.6.2. **Adverse coverage** (a security advisory, not an endorsement). Mirrors at ENISA EUVD, CVE.org, VulDB, and CISA SB26-201 are not counted separately. See "Security finding" below. *(Verified 2026-07-19 as T0-e; row written 2026-08-09.)* | Jul 2026 |
| 14 | COPOD | **European Space Agency (ESA/ESOC)**, ESA-ADB benchmark | "European Space Agency Benchmark for Anomaly Detection in Satellite Telemetry" (ESA-ADB), 87 pages, coauthored by ESOC staff at `esa.int` (Peter Collins, Gabriele De Canio) with Christoph Haskamp and Daniel Lakey. COPOD is reference 60 and is scored against the benchmark's nine requirements: p27 notes it needs no standardisation "by definition"; p31 states that it "does not fulfil R9 after adapting it to online detection". **Assessed and not adopted:** the requirements table on p32 records COPOD as `Included in ESA-ADB: NO`, so this row is evidence of evaluation by an ESA benchmark rather than of adoption. PyOD is separately cited as reference 70 (JMLR). Distinct from row 8, which is the OPS-SAT benchmark in *Scientific Data* by a different author set. Verified 2026-08-30 by downloading the 87-page PDF and scanning it. [source](https://arxiv.org/abs/2406.17826) | 2024 |
| 15 | TDC | **research.google** | "We leveraged data from the Therapeutic Data Commons (TDC), a public collection of drug discovery datasets for training ML models, and processed 66 tasks most relevant to drug discovery into instruction-answer formats suitable for LLMs." [source](https://research.google/blog/tx-llm-supporting-therapeutic-development-with-large-language-models/) | 2026 |
| 16 | PyOD | **tec.gov.in** | "Anomaly Detection • PyOD – Outlier detection algorithms." [source](https://www.tec.gov.in/pdf/consultations/Combined%20Standard%20on%20AI%20Robustness%20dated%2006052025-57070.pdf) | 2026 |
| 17 | ADBench | **www2.camara.leg.br** | "Zhao, Nasrullah e Li (2019) apresentaram uma biblioteca de código livre e aberto (open-source) escrita na linguagem Python para a detecção de anomalias, denominada Python Outlier Detection (PyOD), que implementa mais de quarenta diferentes algoritmos." The methods then state: "Nesse sentido, foi utilizada a biblioteca Scalable Unsupervised Outlier Detection (SUOD), também escrita em linguagem Pyt [source](https://www2.camara.leg.br/a-camara/programas-institucionais/cursos/pos-graduacao/eventos/jornadas-de-pesquisa-e-extensao/final_AnaisdaXIIIJornadadePesquisaeExtensodaCmaradosDeputadosParlamentoeInovao.pdf) | 2026 |
| 18 | ECOD | **BIS / Irving Fisher Committee** (Bank of Thailand authors) | IFC Bulletin 66, "A scalable, explainable machine learning approach for granular-level credit dataset's quality assurance". p15, Further Work: *"Our eventual goal is to deploy ECOD for the full RDT Credit data in our production environment, implemented on-premises under Apache platform (Spark or Hadoop)."* The paper evaluates ECOD on granular regulatory credit data and reports detection recall and top-3 explained-feature coverage. **A stated production-deployment goal inside a central bank's regulatory data pipeline, which is stronger than a citation.** The same page also states that the full pipeline needs further scalability research and experimentation, so this is an intent rather than a scheduled deployment. Verified 2026-08-30 by PDF download plus `pdf_term_scan.py`; the claim survived an independent adversarial re-fetch. Canonical URL `bis.org/2026-07/ifcb66_08.pdf`, which is the path the bulletin landing page points to. The paper was prepared for the 12th biennial IFC Conference of 22-23 August 2024 and published in Bulletin 66; the `/2026-07/` URL segment is not the publication date. | Feb 2026 |
| 19 | TrustLLM | **International AI Safety Report 2025** | Reference 1035, PDF p281, full author list: *"Y. Huang, L. Sun, ... Y. Zhao, 'Position: TrustLLM: Trustworthiness in Large Language Models'"*. **Distinct document from the 2026 edition already counted at row 8b**, verified by comparing both files rather than by URL. Chaired by Yoshua Bengio with 30+ country backing. Verified 2026-08-30; survived adversarial re-fetch. Hosted at both `internationalaisafetyreport.org` and `assets.publishing.service.gov.uk`. | 2025 |
| 20 | TrustLLM | **NICT** (Japan, National Institute of Information and Communications Technology) | Cybersecurity research deck, PDF p22: *"TrustLLM Team 2024 ・LLMにおける信頼性に関する包括的な研究チーム ・真実性、安全性、公平性、堅牢性、プライバシー、機械倫理の6つの側面でLLMの信頼性を評価する。"* The six trustworthiness dimensions are described in full. **First appearance of a FORTIS work in a NICT document, and a new national research institute for this ledger.** Verified 2026-08-30 by PDF scan; survived adversarial re-fetch. | Mar 2026 |
| 20b | TrustLLM | **NICT** (Japan, National Institute of Information and Communications Technology) | AI Security Evaluation Platform, slide 20 of the NICT Cyber Security Symposium 2026 deck `program_takeshi-takahashi.pdf`. The platform's "Select test sets" panel offers three options, and TrustLLM supplies two of them: **`AdvGLUE (TrustLLM)`** and **`Jailbreak (TrustLLM)`**, beside `Prompt Injection (Purple Llama)`. **Operational use with attribution inside a national research institute's evaluation tooling, which is stronger than a citation.** A second NICT document, distinct from row 20, so the institute is now represented twice. Verified 2026-08-30 by rendering the slide: the page carries no extractable text, so every text-based scan this audit runs returns nothing for it. Found by the round-5 reviewer after this row had been recorded as a verified negative. | 2026 |

**Source URLs (rows 18-20b):**

- Row 18: [BIS IFC Bulletin 66, ifcb66_08](https://www.bis.org/2026-07/ifcb66_08.pdf)
- Row 19: [International AI Safety Report 2025](https://internationalaisafetyreport.org/sites/default/files/2025-10/international_ai_safety_report_2025_english.pdf), [report landing page](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2025)
- Row 20: [NICT cybersecurity deck](https://www2.nict.go.jp/idi/common/pdf/2025-s-cyber.pdf)
- Row 20b: [NICT Cyber Security Symposium 2026, Takahashi deck](https://www2.nict.go.jp/csri/nict_cyber2026/common/files/program_takeshi-takahashi.pdf)

**Source URLs:** [Senate PDF](https://www.hsgac.senate.gov/wp-content/uploads/2024.06.11-Hedge-Fund-Use-of-AI-Report.pdf) · [CDAO Toolkit](https://www.ai.mil/Portals/137/Documents/Resources%20Page/2024-12GenAI-Responsible-AI-Toolkit.pdf) · [NIST PDF](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2025.pdf) · [FLI Inaugural](https://futureoflife.org/ai-policy/ai-experts-major-ai-companies-have-significant-safety-gaps/) · [FLI Summer](https://futureoflife.org/ai-safety-index-summer-2025/) · [FLI Winter](https://futureoflife.org/ai-safety-index-winter-2025/) · [FLI Indicator Sheet](https://futureoflife.org/wp-content/uploads/2025/11/Indicator-TrustLLM_Benchmark.pdf) · [ESA OPS-SAT](https://www.nature.com/articles/s41597-025-05035-3) · [Intl AI Safety Report](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026) · [Privacy Intl](https://www.privacyinternational.org/report/5736/nowhere-hide-privacy-risks-and-policy-implications-ai-geolocation) · [LLNL SafeAI PDF](https://data-science.llnl.gov/sites/data_science/files/2024-12/SafeAIforDOE%20Digital.pdf) · [MITRE LILAC PDF](https://www.mitre.org/sites/default/files/2024-10/PR-24-2767-Emerging-Risks-Mitigations-Public-Chatbots-LILAC-v1.pdf) · [TxGemma report](https://storage.googleapis.com/research-media/txgemma/txgemma-report.pdf) · [Google TxGemma docs](https://developers.google.com/health-ai-developer-foundations/txgemma) · [OpenAI Careers](https://openai.com/careers/technical-intelligence-analyst-san-francisco/) · [snapshot](news-snapshots/openai-careers-technical-intelligence-analyst-2026-05-07.md) · [OpenAI Careers #8h Wayback](http://web.archive.org/web/20250810151707/https://openai.com/careers/quantitative-threat-forecasting-analyst/) · [#8h snapshot](news-snapshots/openai-careers-quantitative-threat-forecasting-analyst-2025-08-10.md) · [Brazil Tesouro Nacional](https://publicacoes.tesouro.gov.br/index.php/cadernos/article/view/158)

**Dimension 8 (PDF deep search) status:** Searched 25+ governance PDFs + regulated verticals for all 105 papers + 19 tools. TrustLLM confirmed in Senate HSGAC, DoD CDAO, NIST AI 100-2e2025, FLI x4 (inaugural, summer, winter, indicator sheet), International AI Safety Report 2026, LLNL/DOE SafeAI, and MITRE LILAC. DoxBench confirmed in Privacy International report. PyOD confirmed in ESA OPS-SAT benchmark, DoD CDAO toolkit, and the official OpenAI Careers Technical Intelligence Analyst listing. TDC confirmed in Google/DeepMind TxGemma official report/docs. Deloitte Germany AIxAML was verified and recorded under ecosystem/industry evidence.

**D8 candidates resolved:**
- ~~**OWASP GenAI Solutions Landscape Q2 2026**~~ — manually checked Apr 10; no universities or academic tools listed. Cleared.

**Count: 37 government/policy/foundation-model citations (TrustLLM x17, PyOD x13, TDC x3, DoxBench x1, COPOD x1, ADBench x1, ECOD x1)**

*Recounted 2026-08-30 from the table itself, at 36, then 37 once row 20b was added. The line read 28 against a 33-row table, and its breakdown
named neither COPOD nor ADBench. Rows 14 through 17 were appended without a matching count update, which
is the same drift the 2026-08-09 note below describes; the rule that closed it binds the count line as
well as the rows. Row 14's source column was corrected in the same edit. It read `arxiv.org`, which is
where the file sits rather than who wrote it: the ESA Anomaly Detection Benchmark paper is coauthored by
European Space Operations Centre staff at `esa.int` and names ESOC throughout. Ledger 1 admits row 8 on
the same basis, ESA authorship in a journal rather than an ESA-published document, so institutional
authorship is the rule this ledger already runs on. Rows 8 and 14 are separate documents, checked rather
than assumed: row 8 is the OPS-SAT benchmark in Scientific Data (Ruszczak, Kotowski, Evans, Nalepa), row
14 is the 87-page ESA-ADB paper (Kotowski, Haskamp, and nine others).*

*Reconciled 2026-08-09, and the reconciliation is the point. The count line read 15 while the table held 19
rows, because two prior passes recorded Tier 0 promotions in their own pass sections without writing ledger
rows: 2026-07-19 verified five (T0-a through T0-e) and 2026-07-31 verified six, one of which (the NIST
webinar deck) never reached the table at all. Rows 9 through 13 and 3b close that gap; 2g and 8h are this
round's net new. **Every future pass must write the ledger row in the same commit that records the
promotion**, or the two accountings drift again. Row 2d also cites DCSO and LSCP, which are not counted
separately here.*

### Ledger 1b: Government Technical Reports (Tier 1)

U.S. Department of Energy national-laboratory reports that use the tools in their methods. These sit
below Ledger 1 proper because a lab technical report is government uptake rather than policy guidance,
and they sit here rather than in Ledger 2 or 3 because "external third-party media" and "ecosystem
adoption" both misdescribe a national-lab technical report.

The split that governs this table: **substantive use only.** A report that merely lists a tool in its
bibliography is bibliometric evidence that `/citation-audit` already measures, and counting it here would
double-book the same fact. Six bibliography-only DOE records are deliberately excluded (DESI/LBNL on
ADBench, Oak Ridge on PyOD, Los Alamos on PyOD, a Sandia-reported record whose authors are at George
Mason, LLNL's multi-lab SafeAI report on TrustLLM which is already Ledger 1 row 8d, and Oak Ridge
OSTI 2333852 on PyOD).

| # | Lab | Work | Evidence | Verified |
|---|-----|------|----------|----------|
| G1 | Sandia National Laboratories | PyOD | *"our anomaly detection was implemented based on PyOD [36], an open-source Python toolbox for performing scalable outlier identification"*, APT detection via provenance analysis. [OSTI 3024855](https://www.osti.gov/servlets/purl/3024855) | 2026-07-31 |
| G2 | Sandia National Laboratories | HPOD | "Development of Machine Learning Algorithm for Pebble Bed Modular Reactor Misuse Detection", 34 pages, all authors SNL-NM. Cites Zhao and Akoglu, *Hyperparameter Optimization for Unsupervised Outlier Detection*, and uses it in the body rather than only at p27. **The first HPOD appearance in any government document.** [OSTI 2563811](https://www.osti.gov/biblio/2563811) | 2026-08-09 |
| G3 | SLAC National Accelerator Laboratory | PyOD | "Coincident learning for unsupervised anomaly detection of scientific instruments", PyOD invoked in the body at p25. Resolved through the OSTI API and the publisher DOI because both OSTI purl paths 404. [OSTI 2426670](https://www.osti.gov/biblio/2426670) · DOI 10.1088/2632-2153/ad64a6 | 2026-08-09 |
| G4 | Brookhaven National Laboratory | COPOD | COPOD offered as one of three anomaly-detection algorithms in an exascale workflow data-reduction system | 2026-07-31 |
| G5 | Brookhaven National Laboratory | TDC | *"We utilized the oracles from Therapeutics Data Commons [31]"*, molecular design under model uncertainty. TDC coauthorship-dilution annotation applies. [OSTI 2550614](https://www.osti.gov/biblio/2550614) | 2026-07-31; a Phase A "verified negative" on this record was corrected 2026-08-09 |
| G6 | Idaho National Laboratory | TrustLLM | *"probably the most comprehensive benchmark of trustworthiness in LLMs available to date ... evaluating 16 mainstream LLMs using 30 datasets"*, nuclear power plant human-AI interaction | 2026-07-31 |
| G7 | Oak Ridge National Laboratory | LSCP | LSCP among six outlier-detection methods used to verify cyber-attack detection accuracy, HVDC attack-defense control | 2026-07-31 |
| G8 | Lawrence Livermore National Laboratory | TrustLLM | FY24 LDRD Annual Report describes the TrustLLM framework and Kailkhura's participation | 2026-07-31 |
| G9 | arxiv.org | PyOD | "To identify structural outliers, we employed 18 relatively fast unsupervised anomaly detection methods implemented in the pyod package." [source](https://arxiv.org/pdf/2302.06454) | 2026-08-13 |
| G10 | indico.bnl.gov | TrustLLM | "Safety benchmarks (Trustworthiness, Safety): DecodingTrust, TrustLLM, WMDP" [source](https://indico.bnl.gov/event/28082/contributions/115792/attachments/65881/113176/AuroraGPT-AI4EIC-2025.pdf) | 2026-08-13 |
| G11 | lwrs.inl.gov | TrustLLM | "Huang, Y., Sun, L., Wang, H., Wu, S., Zhang, Q., Li, Y., Gao, C., Huang, Y., Lyu, W., Zhang, Y. and Li, X., 2024. TrustLLM: Trustworthiness in large language models. arXiv preprint arXiv:2401.05561." [source](https://lwrs.inl.gov/content/uploads/11/2024/11/5.3_Athe_NCSU_GAI-for-DIC-Design-Tasks-1.pdf) | 2026-08-13 |
| G12 | pubs.rsc.org | TDC | "To further assess general applicability of graphlet-fingerprint-based models, we evaluate their performance on nine drug-discovery-relevant regression tasks from the Therapeutic Data Commons (TDC)." [source](https://pubs.rsc.org/en/content/articlepdf/2024/dd/d4dd00089g) | 2026-08-13 |

**Count: 8 DOE national-laboratory reports with substantive use, across 6 labs (PyOD x2, TrustLLM x2, HPOD, COPOD, TDC, LSCP).**

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
| 22 | agent-audit | SitePoint | Developer publication | **[REMOVED 2026-07-19: NOT COVERAGE]** "OpenClaw Security Audit Guide 2026". Flagged UNVERIFIED 2026-06-14; confirmed 2026-07-19 by full live fetch of the 649-line article: no Yue Zhao, FORTIS, USC, project URL, arXiv:2603.22853, or HeadyZhang reference. Its only literal token is generic sample Docker YAML (`services: agent-audit:` / `container_name: agent-audit-sandbox`). Wayback returned no snapshots, so the page did not change and the original claim was wrong. Independently re-verified 2026-07-19 by a separate fetch: `agent-audit` appears 3 times, all as a Docker service or container name (`services: agent-audit:`, `container_name: agent-audit-sandbox`); `USC` appears 3 times, all as the substring inside "obfuscated", which is the likely source of the original false positive; the only GitHub link in the article is `github.com/moby/moby`. Reclassified to Topic Validation; not counted. | 2026 | D5 | [Link](https://www.sitepoint.com/openclaw-security-audit-guide/) |
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
| 36an | No Attacker Needed (paper title) | **Cloud Security Alliance Labs** | Security-industry daily briefing | CISO Daily Briefing prints the exact title of *No Attacker Needed: Unintentional Cross-User Contamination in Shared-State LLM Agents*. Coordinator-verified 2026-07-31. Names no author and no institution, so the row records **title-only attribution**. Row written 2026-08-09. | Apr 2026 | D3 | Cloud Security Alliance Labs |
| 36ao | TrustLLM | **NTT Technical Review** (Japan) | Corporate technical journal | TrustLLM named on p4; the canonical benchmark repo is reference [4] on p5. Verified 2026-07-19 as T1-b; row written 2026-08-09. | 2026 | D8 | NTT Technical Review |
| 36ap | Auditable Agents, Implicit Execution Tracing | **The Agent Times** | Specialist AI publication | Dedicated feature naming Yue Zhao and explaining all five auditability pillars. **The first genuine editorial coverage of the auditing line.** Verified 2026-07-19; row written 2026-08-09. | Jul 2026 | D3 | theagenttimes.com |
| 36aq | Auditable Agents | **WIDTH** | Compliance / governance publication | Applies the five auditability dimensions and the overhead result to compliance infrastructure. Verified 2026-07-19; row written 2026-08-09. | Jul 2026 | D3 | width.com |
| 36ar | MemoHarness (arXiv:2607.14159) | **news-japan.ai** | Japanese AI news outlet | Dedicated Japanese feature naming the paper, all six control dimensions, and the dual-layer experience bank. Found independently by three lanes. Picked up within days of the paper being posted. Verified 2026-07-19; row written 2026-08-09. | Jul 2026 | D7 | news-japan.ai |
| 36as | SkillCenter (arXiv:2607.07676) | **storium.io** | Korean specialist outlet | Two Korean features naming SkillCenter and SkillGate and reporting the 216,938 / 114,565 / 102,373 skill counts. Counted as one outlet row. Verified 2026-07-19; row written 2026-08-09. | Jul 2026 | D7 | storium.io |
| 36at | PyOD | **Computer Vision News** | Trade magazine | Dedicated PyOD feature, PDF pp. 18-23, 24 term hits. Newly surfaced in 2026 despite the March 2019 publication date. Verified 2026-07-19; row written 2026-08-09. | Mar 2019 | D3 | Computer Vision News |
| 36au | PyOD | **Leiphone** (雷锋网) | Chinese tech media | Editorial translation naming PyOD with the full paper citation. A human translator is credited, so the `editorial_translation` rule permits Tier 2 rather than an AI-content demotion. Verified 2026-07-19; row written 2026-08-09. | 2019 | D7 | leiphone.com |
| 37 | TDC | **finance.sina.com.cn** | substantive | "TDC（Therapeutics Data Commons）数据集有三大特点：开源、大型、3行代码搞定。" The article also states: "主要的5位开发者，分别是来自哈佛的黄柯鑫、佐治亚理工学院的符天凡、MIT的高文昊、CMU的赵越、斯坦福的Yusuf Roohani。" | 2026 | 2026-08-13 | [link](http://finance.sina.com.cn/tech/csj/2021-01-02/doc-iiznctke9783466.shtml) |
| 38 | PyOD | **analyticsindiamag.com** | substantive | "PyOD is a flexible and scalable toolkit designed for detecting outliers or anomalies in multivariate data; hence the name PyOD (Python Outlier Detection). It was introduced by Yue Zhao, Zain Nasrullah and Zeng Li in May 2019 (JMLR (Journal of Machine learning) paper)." | 2026 | 2026-08-13 | [link](https://analyticsindiamag.com/guide-to-pyod-a-python-toolkit-for-outlier-detection/) |
| 39 | TrustLLM | **computing.llnl.gov** | substantive | "Some of their early works have contributed to popular benchmarks (TrustLLM [1], MLCommons AI Safety [2], GTBench Reasoning [3]) and identified previously unknown vulnerabilities of LLMs." | 2026 | 2026-08-13 | [link](https://computing.llnl.gov/sites/default/files/2025-03/CASC%20Newsletter%20March%202025.pdf) |
| 40 | TODS | **datadrivendiscovery.org** | substantive | "TODS is a full-stack automated machine learning system for outlier detection on multivariate time-series data." | 2026 | 2026-08-13 | [link](https://datadrivendiscovery.org/automl-systems/) |
| 41 | TrustLLM | **ettrends.etri.re.kr** | substantive | "6가지 신뢰성 측정 기준(Trustfulness, Safety, Fairness, Robustness, Privacy, Machine Ethics)을 이용해 LLM 평가 방법을 정의하고 평가했던 연구 등이 공개된 바 있다[16]." Reference [16] is "L. Sun et al., ‘TrustLLM: Trustworthiness in Large Language Models,’ arXiv preprint, 2024, https://doi.org/10.48550/arXiv.2401.05561." | 2026 | 2026-08-13 | [link](https://ettrends.etri.re.kr/ettrends/210/0905210023/108-122.%20%EC%A0%84%EC%A2%85%ED%99%8D_210%ED%98%B8%20%EC%B5%9C%EC%A2%85.pdf) |
| 42 | CHI-Bench | **markets.financialcontent.com** | substantive | "AI company actAVA.ai today released CHI-Bench, the world’s first long-horizon healthcare benchmark for AI agents." | 2026 | 2026-08-13 | [link](https://markets.financialcontent.com/stocks/article/pressadvantage-2026-5-20-claude-gpt-gemini-agents-fail-72-of-us-healthcare-workflows-new-benchmark-finds) |
| 43 | TyphoFormer | **news.fsu.edu** | substantive | "Yushun Dong, Ph.D. (Department of Computer Science) had his paper ‘TyphoFormer’ win the Best Short Paper Award at the Association for Computing Machinery’s Special Interest Group on Spatial Information 2025 international conference." | 2026 | 2026-08-13 | [link](https://news.fsu.edu/news/faculty-staff-briefs/2025/12/02/faculty-and-staff-briefs-november-2025/) |
| 44 | TrustLLM | **sdaia.gov.sa** | substantive | “طور باحثون من عدة جامعات ومؤسسات بحثية حول العالم إطار عمل لتقييم موثوقية النماذج اللغوية الكبيرة أطلق عليه اسم (TrustLLM)” | 2026 | 2026-08-13 | [link](https://sdaia.gov.sa/en/MediaCenter/KnowledgeCenter/AINewsletter/AINewsletter03Oct2024.pdf) |
| 45 | TDC | **biopharmatrend.com** | substantive | "The model’s development involved curating the Therapeutics Instruction Tuning (TxT) dataset, which consolidates information from the Therapeutic Data Commons (TDC) and additional literature." | 2026 | 2026-08-13 | [link](https://www.biopharmatrend.com/news/google-research-and-deepmind-unveil-tx-llm-a-new-language-model-for-therapeutic-development-978/) |
| 46 | TDC | **marktechpost.com** | substantive | "From a technical standpoint, TxGemma capitalizes on the extensive Therapeutic Data Commons (TDC), a curated dataset containing over 15 million datapoints across 66 therapeutically relevant datasets." | 2026 | 2026-08-13 | [link](https://www.marktechpost.com/2025/03/27/google-ai-released-txgemma-a-series-of-2b-9b-and-27b-llm-for-multiple-therapeutic-tasks-for-drug-development-fine-tunable-with-transformers/) |
| 47 | PyOD | **mordorintelligence.com** | substantive | "Production-ready frameworks such as PyOD and Alibi Detect amassed a broad developer following, with PyOD surpassing 8,200 GitHub stars by December 2025." | 2026 | 2026-08-13 | [link](https://www.mordorintelligence.com/industry-reports/anomaly-detection-market) |
| 48 | TDC | **schrodinger.com** | substantive | "Herein, we present performance metrics for Schrödingers automated ML model building engine, DeepAutoQSAR, on the ADMET subset of the Therapeutic Data Commons (TDC) — a large collection of public data for ML model building and benchmarking." | 2026 | 2026-08-13 | [link](https://www.schrodinger.com/life-science/learn/white-papers/benchmark-study-deepautoqsar-chemprop-and-deeppurpose-admet-subset-therapeutic-data/) |
| 49 | PyOD | **secnews.gr** | substantive | “Σύμφωνα με την καταγραφή, το πρόβλημα επηρεάζει τις εκδόσεις 3.5.0–3.5.2 και μπορεί να οδηγήσει σε εκτέλεση ανεπιθύμητου κώδικα όταν μια εφαρμογή φορτώνει μη έμπιστο αρχείο μοντέλου από απομακρυσμένη πηγή.” | 2026 | 2026-08-13 | [link](https://www.secnews.gr/720870/cve-2026-15529-pyod-deserialization/) |

**Count: 80 counted items across 81 rows** (row #22 SitePoint is present but marked REMOVED and is not counted).

*Composition after the 2026-08-09 reconciliation: 71 prior, +2 verified 2026-05-13 (#36al PyShine, #36am Fintech Mag), minus 1 for the SitePoint removal, +1 written 2026-08-09 for a 2026-07-31 promotion (#36an Cloud Security Alliance), +7 written 2026-08-09 for 2026-07-19 promotions (#36ao through #36au). **The 83 figure published until 2026-08-09 was never reproducible from this table.** It counted 11 promotions from the 2026-07-19 pass that had no rows. Placing them moved 4 of the 11 elsewhere rather than here: FLI Summer 2026 went to Ledger 1 row 7b, where it belongs with the other FLI editions, and the three Nature-family papers went to the new Ledger 7, because a peer-reviewed paper running PyOD in its Methods is scientific uptake rather than media coverage. The remaining 7 are #36ao through #36au.* Four May 13 wide-run candidates (Microsoft Research TrustLLM, thepaper.cn TrustLLM, aiproductivity.ai Aegis, jiqizhixin TrustLLM) were initially proposed as Ledger 2 additions but dropped after Codex Round 1 review caught them as exact-URL duplicates of existing rows #7, #5, #21, #34b respectively; they are recorded in `news-search-candidates.jsonl` as `duplicate_existing` and the underlying May 13 verification work serves as an evidence upgrade to those four existing rows rather than as new counted rows.**

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
| 66dw | PyOD | **TechTarget definition page** | "Anomaly detection" glossary entry names PyOD verbatim: *"PyOD, an open source anomaly detection library written in Python"*. **Demoted from the claimed Tier 1 to Tier 2 on 2026-07-31**: a glossary entry rather than a press feature, and it names neither the PI nor USC, so it belongs here rather than in Ledger 2. Row written 2026-08-09. (2026, D3) |
| 67 | Yue Zhao / FORTIS | **substantive** | "About the speaker Yue Zhao from his website: I am a final year Ph.D. student at Carnegie Mellon University (CMU)." [source](http://edu.ieee.org/uk-uob/2022/11/16/event-review-uob-ieee-student-branch-event-anomaly-detection-algorithms-systems-and-applications/) |
| 68 | CHI-Bench | **substantive** | "actAVA Benchmarks: open evaluations for frontier AI agents on long-horizon, policy-rich U.S. healthcare workflows. Start with CHI-Bench across prior authorization, utilization management, and care management." [source](https://actava.ai/benchmarks) |
| 69 | ADBench | **substantive** | "简介面向具有数据异常检测需求、但缺乏编程经验的业务人员。基于我们提出的ADBench和ADGym，使用者可通过交互式界面实现上传数据、选择机器学习模型或自动化构建模型、分析结果、保存结果等功能。" [source](https://ai2fin.sufe.edu.cn/) |
| 70 | PyOD | **substantive** | “초반에는 Orion의 AER 모델을 사용하다가 모델 성능은 좋지만 GPU 메모리 사용량과 추론 시간이 너무 오래 걸려서 PyOD를 검토.” [source](https://aisj.tistory.com/252) |
| 71 | PyOD | **substantive** | "Using some tried and tested ingredients like Apache Airflow and PyOD to perform painless anomaly detection on your key business metrics." [source](https://andrewm4894.com/2023/05/18/painless-anomaly-detection-with-apache-airflow/) |
| 72 | Aegis | **reference-list-only** | "A. Yuan, Z. Su, and Y. Zhao, “Aegis: No tool call left unchecked – a pre-execution firewall and audit layer for ai agents,” 2026. [Online]. Available: https://arxiv.org/abs/2603.12621" [source](https://arxiv.org/abs/2603.09002) |
| 73 | TDC | **substantive** | "First reported in 2011 by Broccatelli and coworkers [37], this dataset has since become a standard benchmark and is included in the Therapeutic Data Commons (TDC) [38] model benchmarking suite." [source](https://arxiv.org/pdf/2404.02058) |
| 74 | agent-audit | **reference-list-only** | "H. Zhang, Y. Nian, and Y. Zhao, 'Agent audit: A security analysis system for llm agent applications,' arXiv preprint arXiv:2603.22853, 2026." [source](https://arxiv.org/pdf/2605.12875) |
| 75 | Implicit Execution Tracing | **reference-list-only** | "Z. Li et al. When only the final text survives: Implicit execution tracing for multi-agent attribution. arXiv preprint, 2025b." [source](https://arxiv.org/pdf/2606.00765) |
| 76 | FORTIS | **reference-list-only** | "Fortis: Benchmarking over-privilege in agent skills. arXiv preprint arXiv:2605.09163, 2026a." [source](https://arxiv.org/pdf/2606.22844) |
| 77 | GRADE | **reference-list-only** | "Zhao, Y. 2026. GRADE: Graph Representation of LLM Agent Dependency and Execution. arXiv preprint arXiv:2606.22741." [source](https://arxiv.org/pdf/2607.06503) |
| 78 | FORTIS | **reference-list-only** | "Han Wang, Wei Yang, Ryan Rossi, Franck Dernoncourt, Xiyang Hu, Philip Yu, Chaowei Xiao, Huan Zhang, and Yue Zhao. 2026. Fortis: Benchmarking over-privilege in agent skills. Preprint, arXiv:2605.09163." [source](https://arxiv.org/pdf/2608.02171) |
| 79 | PyOD | **substantive** | "通过Python的科学计算库（如 pandas、numpy）和机器学习库（如 scikit-learn、pyod），我们可以高效地对大数据集进行异常检测。" [source](https://bbs.huaweicloud.com/blogs/442911) |
| 80 | PyOD | **substantive** | “La libreria PyOD (Python Outlier Detection) sviluppata da Yue Zhao raccoglie 30+ algoritmi sotto un’API uniforme ed è ormai la scelta standard per benchmarking 2021.” [source](https://brentasoft.com/blog/anomaly-detection-cybersecurity-pmi-2021/) |
| 81 | PyGOD | **substantive** | "This research uses code from a Python library called PyGOD, which is based on an algorithm described for finding unusual or suspicious nodes in graphs." [source](https://calhoun.nps.edu/server/api/core/bitstreams/ca96df1a-9a38-4d77-b68e-ce2536058571/content) |
| 82 | ECOD | **substantive** | "pyod(Python Outlier Detection)是一个集成了30余种异常检测方法和模型的Python工具箱。从经典的 LOF (SIGMOD 2000) 到最新的 ECOD (TKDE 2022) 。" [source](https://cloud.tencent.cn/developer/article/2315801) |
| 83 | PyOD | **substantive** | “PyOD是一个全面且易于使用的Python库，专门用于检测多变量数据中的异常点或离群点。” [source](https://damodev.csdn.net/6888295dbb9d8e0ecec3a7aa.html) |
| 84 | PyOD | **substantive** | "Python-Bibliotheken wie scikit-learn und PyOD bieten Implementierungen verschiedener Algorithmen zur Erkennung von Anomalien." [source](https://databasecamp.de/daten/ausreissererkennung) |
| 85 | TrustLLM | **substantive** | "本稿では,大規模言語モデル(LLM)における信頼度に関する総合的研究であるTrustLLMを紹介する。" [source](https://devneko.jp/wordpress/?p=4303) |
| 86 | AD-AGENT | **substantive** | “AD-Agent [46] takes a meta approach by using LLMs to generate anomaly detection programs through multi-agent collaboration, leveraging their strengths in retrieval and code generation.” [source](https://doi.org/10.1109/ICKG66886.2025.00048) |
| 87 | TrustLLM | **reference-list-only** | “Huang, Y.; Sun, L.; Wang, H.; Wu, S.; Zhang, Q.; Li, Y.; Gao, C.; Huang, Y.; Lyu, W.; Zhang, Y.; et al. Position: Trustllm: Trustworthiness in large language models. In Proceedings of the International Conference on Machine Learning. PMLR, 2024, pp. 20166–20270.” [source](https://doi.org/10.20944/preprints202601.1596.v1) |
| 88 | AD-AGENT | **substantive** | “Similarly, Yang et al. [40] introduce AD-AGENT, which employs a team of LLM agents to interactively build a complete anomaly detection pipeline from a high-level user instruction.” [source](https://doi.org/10.3390/s26082330) |
| 89 | COPOD | **substantive** | "COPOD [LZB+20], a state-of-the-art ML based model for outlier detection in a single column. The model is implemented by the outlier detection toolbox PyOD [ZNL19]." [source](https://era.ed.ac.uk/server/api/core/bitstreams/e7dc5e3d-baa9-425a-b5bb-bbbef245d2a6/content) |
| 90 | PyOD | **substantive** | "Para la implementación de los experimentos se utiliza el toolbox de Python para detección de valores atípicos escalables (PyOD, [293])." [source](https://fileserver-az.core.ac.uk/download/547377873.pdf) |
| 91 | ADBench | **substantive** | "I was inspired to go this route due to the thorough results reported by ADBench [Han et al., 2022]." [source](https://fileserver-az.core.ac.uk/download/619689193.pdf) |
| 92 | agent-audit | **substantive** | “本文介绍了 Agent Audit，这是一个专为 LLM 智能体应用设计的开源安全分析系统，它通过结合数据流分析、凭据检测和配置检查等技术，能够高效识别工具代码、部署配置及模型上下文协议中的安全风险，并支持集成到 CI/CD 流程中。” [source](https://gist.science/zh/paper/2603.22853) |
| 93 | AEGIS | **substantive** | "2. **AEGIS paper** — arXiv:2603.12621 — \"AEGIS: No Tool Call Left Unchecked — A Pre-Execution Firewall and Audit Layer for AI Agents\" (fetched 2026-03-24)" [source](https://github.com/0SxD/archive-openbrain/blob/main/research/destructive_action_intercepts_2026-03-24.md) |
| 94 | anywhere-agents | **substantive** | "anywhere-agents (opinionated published config with hook guards)" [source](https://github.com/LF-Decentralized-Trust-labs/gitmesh/blob/main/doc/pivot/pivot.md) |
| 95 | agent-audit | **substantive** | "/ **[Agent Audit](https://arxiv.org/abs/2603.22853)** / Security analysis system for LLM agent apps: dataflow analysis, credential detection, MCP config parsing, privilege-risk checks / [Zhang et al.](https://arxiv.org/abs/2603.22853) /" [source](https://github.com/LLMSecurity/awesome-agent-skills-security/blob/main/README.md) |
| 96 | AD-AGENT | **substantive** | "\"name\": \"USC-FORTIS__AD-AGENT__main\"" [source](https://github.com/NordicAgents/AgentProof/blob/main/corpus/real_world/graphs/USC-FORTIS__AD-AGENT__main.json) |
| 97 | PyOD | **substantive** | "Wrapper for Python-based Outlier Detection Algorithms in Julia"; `pyod = "=2"` [source](https://github.com/OutlierDetectionJL/OutlierDetectionPython.jl) |
| 98 | GRADE | **substantive** | "- agent-skill-privilege-boundary — Declared capability/permission surface enforced at selection and execution (FORTIS `2605.09163v2`)"; "- agent-run-dependency-graph — GRADE recovers a run's missing provenance-graded dependency-edge layer alongside execution order, predicting failure where run-size features are weak and localizing the faulting step (arXiv:2606.22741)" [source](https://github.com/Tibsfox/gsd-skill-creator/blob/main/.college/departments/agent-systems/DEPARTMENT.md) |
| 99 | agent-style | **substantive** | "Agent Style Enforcer / Literature-backed technical-prose writing ruleset — 21 rules ...; based on yzhao062/agent-style (2026)" [source](https://github.com/ai-boost/awesome-prompts/blob/main/README.md) |
| 100 | ADBench | **substantive** | “Overwrite pyod version to avoid bugs pip install pyod==2.0.1” [source](https://github.com/amazon-science/AnoLLM-large-language-models-for-tabular-anomaly-detection) |
| 101 | PyOD | **substantive** | "Painless anomaly detection (using [PyOD](https://github.com/yzhao062/pyod)) with [Apache Airflow](https://airflow.apache.org/)." [source](https://github.com/andrewm4894/airflow-provider-anomaly-detection) |
| 102 | agent-style | **substantive** | "- `skills/great_cto/prose-style.md` — subset of 7 rules from upstream `RULES.md`" [source](https://github.com/avelikiy/great_cto/blob/main/NOTICE.md) |
| 103 | TrustLLM | **substantive** | "Summary: TrustLLM: A Benchmark of Trustworthiness in Large Language Models" [source](https://github.com/conda-forge/trustllm-feedstock) |
| 104 | CS-Paper-Checklist | **substantive** | "Reference [Yue Zhao's CS paper checklist](https://github.com/yzhao062/CS-paper-checklist) for comprehensive submission guidelines." [source](https://github.com/limenlp/limenlp.github.io/blob/main/src/content/wiki/writing-and-speaking.md) |
| 105 | PyOD | **substantive** | "from pyod.models.abod import ABOD" [source](https://github.com/microsoft/AutoBrewML/blob/master/Auto%20Brew%20ML%20Framework/AMLMasterNotebook.py) |
| 106 | PyOD | **substantive** | "from pyod.models.hbos import HBOS" [source](https://github.com/microsoft/anomaly-detector) |
| 107 | agent-style | **substantive** | "- **agent-style** — 21 literature-backed rules for FORMAL technical prose" [source](https://github.com/pchalasani/claude-code-tools/blob/main/plugins/writing/README.md) |
| 108 | Auditable Agents | **substantive** | "Nian et al., \"Auditable Agents\" (arXiv:2604.05485) — https://arxiv.org/abs/2604.05485 — defines five dimensions of agent auditability including evidence integrity and lifecycle coverage; treats the session record as the required substrate for accountability, responsibility attribution, and recovery" [source](https://github.com/ramparte/agent-building-playbook/blob/main/patterns/session-archaeology.md) |
| 109 | The Autonomy Tax | **substantive** | "Evidence: destroys 47-77% of benign tasks at Step 1 (2603.19423)" [source](https://github.com/ryanthedev/oberskills/blob/main/skills/prompt/references/safety.md) |
| 110 | COPOD | **substantive** | “PyOD (ECOD, COPOD, HBOS, KNN, OCSVM, LODA) — pip install pyod” [source](https://github.com/salesforce/timeseries-council) |
| 111 | agent-audit | **substantive** | "**[Agent Audit: A Security Analysis System for LLM Agent Applications](https://arxiv.org/abs/2603.22853)**: A system for analyzing security vulnerabilities in LLM agent applications." [source](https://github.com/santosomar/ai_news_archive/blob/main/ai_news_archive/ai_news_analysis_2026-03-25-12-30.txt) |
| 112 | AEGIS | **substantive** | "* AEGIS-inspired deep argument inspection for tool calls."; "* Reference: arXiv:2603.12621 (AEGIS)" [source](https://github.com/sethdford/h-uman/blob/main/include/human/security/arg_inspector.h) |
| 113 | ECOD | **substantive** | "from pyod.models.ecod import ECOD" [source](https://github.com/splunk/splunk-mltk-container-docker) |
| 114 | AEGIS | **substantive** | "Multivariate statistical outlier detection (ECOD, COPOD, Isolation Forest) and score aggregation ensembles (Average of Maximums)." [source](https://github.com/swanandagupta/AEGIS-SOC) |
| 115 | CS-Paper-Checklist | **substantive** | "**Checklist Guide for CS Paper Formatting, Structure, and Presentation** <https://github.com/yzhao062/cs-paper-checklist>" [source](https://github.com/tw93/Weekly/blob/main/src/pages/en/posts/226-I-Love-Nanjing.md) |
| 116 | PyOD | **substantive** | "The `PyODScorer` makes it trivial to use PyOD detectors on time series." [source](https://github.com/unit8co/darts) |
| 117 | ADBench | **substantive** | "Download `ADBench <https://github.com/Minqi824/ADBench/tree/main/adbench/datasets/>`_ datasets." [source](https://github.com/xuhongzuo/DeepOD) |
| 118 | FORTIS | **substantive** | "**FORTIS**（2605.09163）：把 skill 层当作权限边界来测，10 个前沿模型端到端最小权限成功率 **< 15%**——agent 普遍组装出超出任一任务所需的有效能力集，这正是危险组合的前置条件。" [source](https://github.com/zbyangnyu/skill-compos-safety/blob/main/survey.md) |
| 119 | COPOD | **substantive** | "COPOD is supported in a dedicated module in the PyOD Python package." [source](https://guides.beeksgroup.com/glossary/Copula-based-Outlier-Detection-(COPOD).html) |
| 120 | ECOD | **substantive** | "ECOD is supported in a dedicated module in the PyOD Python package." [source](https://guides.beeksgroup.com/glossary/Empirical-Cumulative-distribution-based-Outlier-Detection-(ECOD).html) |
| 121 | PyOD | **substantive** | “This post aims to introduce how to make simulated data for anomaly detection using PyOD, which is outlier detection package.” [source](https://h1ros.github.io/posts/make-simulated-data-for-anomaly-detection/) |
| 122 | PyOD | **substantive** | "Есть библиотеки для временных рядов (Prophet, statsmodels), для поиска аномалий (PyOD), для ранжирования документов ..." [source](https://habr.com/ru/articles/1066070/) |
| 123 | ADBench | **substantive** | “Существует отличная библиотека в которой имплементировано много современных алгоритмов для детекции аномалий — PyOD. Разработчики этой библиотеки недавно выпустили статью, где протестировали 30 алгоритмов на разных датасетах.” [source](https://habr.com/ru/articles/739550/) |
| 124 | COPOD | **substantive** | “Обнаружение выбросов на основе копул (COPOD) – это новый алгоритм обнаружения аномалий. В Python он реализован в пакете PyOD.” [source](https://habr.com/ru/companies/otus/articles/570314/) |
| 125 | PyOD | **substantive** | "如果你需要多个不同的模型，可以使用Python异常检测工具库，Pyod。" [source](https://hub.baai.ac.cn/view/11778) |
| 126 | TODS | **substantive** | “TODS: An Automated Time Series Outlier Detection System Published on Sep 18, 2020 Upvote - Authors: Kwei-Herng Lai, Daochen Zha, Guanchu Wang, Junjie Xu, Yue Zhao, Devesh Kumar, Yile Chen, Purav Zumkhawaka, Mingyang Wan, Diego Martinez, Xia Hu.” [source](https://huggingface.co/papers/2009.09822) |
| 127 | PyOD | **substantive** | "Dans ce tutoriel, j'ai illustré comment détecter les valeurs aberrantes à l'aide de la pyod bibliothèque Python." [source](https://ichi.pro/fr/comment-detecter-les-valeurs-aberrantes-avec-python-pyod-187403502722635) |
| 128 | PyOD | **substantive** | "PyOD est une bibliothèque Python avec un ensemble complet d'algorithmes évolutifs et de pointe (SOTA) pour détecter les points de données éloignés dans des données multivariées." [source](https://ichi.pro/fr/pyod-une-bibliotheque-python-unifiee-pour-la-detection-des-anomalies-59411949151009) |
| 129 | PyOD | **substantive** | “Anomaly Detection (adcern) - Analyser wrapper of pyod - Data mining and evaluation classes - Publisher into the CERN Monitoring Infrastructure” [source](https://indico.cern.ch/event/1123214/contributions/4809938/attachments/2433022/4166582/Anomaly_Detection.pdf) |
| 130 | ECOD | **substantive** | "Recently, ECOD (Empirical Cumulative distribution based Outlier Detection) and A3 method has been proposed. ECOD (Li, Zhao, et al. 2022) is based on a premise that anomalies of multivariate distributions usually exhibit atypical behavior for marginal distributions." [source](https://ipipan.waw.pl/pliki/doktoraty/Wawrzenczyk/Wawrzenczyk_Doktorat.pdf) |
| 131 | TrustLLM | **substantive** | "TrustLLM offers a more operational, LLM-centric approach structured around six evaluated dimensions: truthfulness, safety, fairness, robustness, privacy, and machine ethics." [source](https://journals.flvc.org/FLAIRS/article/view/141819) |
| 132 | PyOD | **substantive** | "在博客的这一段，我们将通过一个快速的例子，使用 PyOD 包检测合成数据集中的异常情况。" [source](https://juejin.cn/post/7106807790336770062) |
| 133 | PyOD | **substantive** | “在本章中，你将接触到PyOD库，它被描述为*“一个全面且可扩展的 Python 工具包，用于检测多变量数据中的异常对象。”*该库提供了一个广泛的实现集合，涵盖了异常值检测领域的流行算法和新兴算法，你可以在此阅读更多内容：github.com/yzhao062/pyod。” [source](https://juejin.cn/post/7545378073568247846) |
| 134 | TDC | **substantive** | "We introduce a real-world drug discovery problem: CACO-2++, a dataset of 906 molecules adapted from CACO-2 [Wang et al., 2016a], sourced from the Therapeutics Data Commons [Huang et al., 2021]." [source](https://knowledge.uchicago.edu/records/13h1n-7vs64/files/PhD_Thesis_fengxue_nov_10_version.pdf?download=1) |
| 135 | TrustLLM | **substantive** | "This chapter presents the TrustLLM framework (Sun et al., Trustllm: Trustworthiness in large language models. International Conference on Machine Learning (2024)), a comprehensive study of trustworthiness in LLMs, including principles for different dimensions of trustworthiness, established benchmark, evaluation, and analysis of trustworthiness for mainstream LLMs." [source](https://link.springer.com/content/pdf/10.1007/978-3-031-76770-8_12.pdf) |
| 136 | PyOD | **reference-list-only** | "Y. Zhao, 'PyOD : A Python Toolbox for Scalable Outlier Detection' 20 : 1-7, 2019." [source](https://m.riss.kr/search/detail/DetailView.do?control_no=98d37b3670d2a566e9810257f7042666&p_mat_type=1a0202e37d52c72d) |
| 137 | PyOD | **substantive** | "Тогда вы не должны пропустить этот замечательный Python Outlier Detection (PyOD) Toolkit." [source](https://machinelearningmastery.ru/anomaly-detection-with-pyod-b523fc47db9/) |
| 138 | PyOD | **substantive** | "PyOD (Python Outlier Detection) es una biblioteca integral de Python que proporciona una colección de algoritmos de detección de anomalías de última generación." [source](https://medium.com/@geotecmatica/detecci%C3%B3n-de-anomal%C3%ADas-en-python-e77f6e156e2b) |
| 139 | PyOD | **substantive** | "Neste post você aprenderá a identificar outliers e remove-los do seu dataset usando a biblioteca do Python, o PyOD." [source](https://medium.com/@igor__leonel/como-identificar-outliers-com-a-biblioteca-pyod-cab0f3e1a1f5) |
| 140 | anywhere-agents | **substantive** | “yzhao062/anywhere-agents (2026–04–16, Python, 41★) — Anywhere-Agents offers a universal configuration for AI agents, emphasizing safety through a destructive-command guard, making it easier to deploy portable, effective, and inherently more secure AI agents across various projects.” [source](https://medium.com/@xyz031702/ai-threat-intelligence-briefing-april-01-2026-april-18-2026-821611da9a8a) |
| 141 | DrugAgent | **substantive** | "Research Summary for ‘DrugAgent — Automating AI-aided Drug Discovery Programming’." [source](https://medium.com/advancedai/multi-agent-framework-drugagent-automating-ai-driven-drug-discovery-programming-with-4ad68122dcbf) |
| 142 | PyOD | **substantive** | "Veja como aplicar detecção de anomalias, técnica de aprendizado de máquina não supervisionado para identificar outliers nos dados não rotulados com PyOD" [source](https://medium.com/camilawaltrick/detecacao-anomalia-dados-nao-rotulados-unidimensionais-com-estatistica-e-pyod-94a983b879a1) |
| 143 | PyOD | **substantive** | "PyOD is a Python library with a comprehensive set of scalable, state-of-the-art (SOTA) algorithms for detecting outlying data points in multivariate data." [source](https://medium.com/data-science/pyod-a-unified-python-library-for-anomaly-detection-3608ec1fe321) |
| 144 | ECOD | **substantive** | "A new and better alternative is ECOD, an abbreviation of ‘empirical cumulative distribution functions for outlier detection’." [source](https://medium.com/geekculture/replace-outlier-detection-by-simple-statistics-with-ecod-f95a7d982f79) |
| 145 | TDC | **substantive** | "The Therapeutics Data Commons (TDC) [239] covers a wide range of tasks in therapeutic modalities related to target discovery and activity modeling." [source](https://ml.cmu.edu/research/phd-dissertation-pdfs/junhongs_mld_phd_thesis_2026.pdf) |
| 146 | PyOD | **substantive** | "O PyOD é um kit de ferramentas Python abrangente e escalável para detectar objetos periféricos em dados multivariados. Yue Zhao, um de seus criadores, afirma que comparado à outras bibliotecas, PyOD tem seis vantagens." [source](https://monografias.dcc.ufmg.br/wp-content/uploads/VELOSO-M.-G.-A.pdf) |
| 147 | PyOD | **reference-list-only** | "Zhao, Y.; Nasrullah, Z.; Li, Z. PyOD: A Python Toolbox for Scalable Outlier Detection. J. Mach. Learn. Res. 2019, 20, 1-7." [source](https://ntrs.nasa.gov/api/citations/20230003127/downloads/Bunting_etal_2022.pdf?attachment=true) |
| 148 | PyOD | **substantive** | "A: Yes, Python libraries (e.g., scikit-learn, PyOD) integrate with OpenObserve for custom real-time anomaly detection using OpenObserve." [source](https://openobserve.ai/blog/real-time-anomaly-detection-openobserve-random-cut-forest/) |
| 149 | PyOD | **substantive** | "Currently, almost every PyOD algorithm is integrated and can thus be easily used directly from Julia." [source](https://outlierdetectionjl.github.io/OutlierDetection.jl/dev/API/detectors/) |
| 150 | PyOD | **substantive** | "实验数据使用的是pyod库提供的用于离群点检测的高斯分布数据，共测试了两个数据集，第一个数据集一共300个数据，数据维度为25，其中离群点个数为30；第二个数据集一共600个数据，数据维度为50，其中离群点个数为60。" [source](https://patents.google.com/patent/CN110377798B/zh) |
| 151 | PyOD | **substantive** | "Figures 1 and 2 show ROC performance and Precision @ n performance (https:// PyOD. readthetadocs. io/en/test/benchmark. html. for anomaly detection algorithms selected from PyOD libraries) for different datasets." [source](https://patents.google.com/patent/CN111159508A/en) |
| 152 | PyOD | **substantive** | "For example, one of Iforest, KNN, CLOF, control, Zscore, Pyod, ABOD, or PCA may be used in calculating the anomaly determination threshold." [source](https://patents.google.com/patent/CN111208445A/en) |
| 153 | XGBOD | **substantive** | "在文献“XGBOD Improving Supervised Outlier Detectionwith Unsupervised Representation Learning”中，针对时间序列异常可能很好地隐藏在某些子空间中或者只能在特定假设下才能识别的问题，利用标签构造了有监督的XGB模型，并实现了最终检测，实验结果充分说明了XGB模型在一维时间序列异常检测的优越表现。" [source](https://patents.google.com/patent/CN111461184A/zh) |
| 154 | PyOD | **substantive** | "The abnormal point detection algorithm is mainly an open source algorithm package pyod based on Python language." [source](https://patents.google.com/patent/CN113052938A/en) |
| 155 | COPOD | **substantive** | "异常检测模型包括 Copula-Based Outlier Detection(COPOD，基于统计概率函数的异常检测)、Deviation-based Outlier Detection(LMDD，基于偏差的异常检测)以及 IsolationForest(孤立森林)等异常检测模型。" [source](https://patents.google.com/patent/CN113780855A/zh) |
| 156 | PyOD | **substantive** | "Among them, the data sets to be detected include pyod public data sets, desensitized enterprise public data sets, etc." [source](https://patents.google.com/patent/CN114254705A/en) |
| 157 | COPOD | **substantive** | "In an embodiment of the present application, PyOD (a library for detecting outliers in data) of Python provides a variety of outlier detection algorithms including COPOD algorithm." [source](https://patents.google.com/patent/CN114298123A/en) |
| 158 | XGBOD | **reference-list-only** | 'YUE ZHAO，ET AL: "XGBOD:Improving Supervised Outlier Detection with Unsupervised Representation Learning", 2018IJCNN, 14 October 2018 (2018-10-14) *' [source](https://patents.google.com/patent/CN114707571A/zh) |
| 159 | COPOD | **substantive** | "方法二：基于Copula的异常值检测法，英文：Copula-based outlier detection，英文缩写：COPOD；" [source](https://patents.google.com/patent/CN114777947A/zh) |
| 160 | PyOD | **substantive** | "2)异常检测模块：采用PYOD工具库，选取的算法包含以下12种具体异常检测算法，如表3所示：" [source](https://patents.google.com/patent/CN115209452B/zh) |
| 161 | PyOD | **substantive** | "根据S2.2、S2.3和S2.4，其中，异常检测算法均使用PyOd库中模型默认参数，异常比例设置为表3中相应数据集所对应的异常比例；" [source](https://patents.google.com/patent/CN115526227A/zh) |
| 162 | COPOD | **substantive** | "针对第一访问行为特征中的横向对比特征、第一访问行为特征中的纵向对比特征、第二访问行为特征中的横向对比特征、第二访问行为特征中的纵向对比特征、和账号设备特征5类预测参考特征，构建了孤立森林、hbos(Histogram-based Outlier Score，基于直方图的异常点得分)、copod(Copula-Based Outlier Detection，基于Copula概率模型的异常点检测)3种不同的异常检测模型。" [source](https://patents.google.com/patent/CN115603955B/zh) |
| 163 | PyOD | **substantive** | "The above-mentioned algorithm model can adopt Python anomaly detection (Python OutlierDetection, PYOD) tool library." [source](https://patents.google.com/patent/CN116455723A/en) |
| 164 | XGBOD | **substantive** | "The XGBOD method takes the anomaly scores of the data set based on a plurality of unsupervised anomaly detection algorithms as new features of the original data set, and takes the new features as training data of a new supervised model, so that the features of the original data can be fully utilized, but the training data set used by the method is required to be completely based on manual annotat [source](https://patents.google.com/patent/CN116522138B/en) |
| 165 | ECOD | **substantive** | "The ECOD algorithm is also an unsupervised machine learning algorithm, firstly, estimating potential distribution of data in a non-parametric mode by calculating an empirical cumulative distribution function ECDF of the data, secondly, estimating tail probability of each data point by using the empirical distribution, and finally, calculating outliers of each data point by aggregation of the esti [source](https://patents.google.com/patent/CN117131449B/en) |
| 166 | ECOD | **substantive** | "基于统计的方法通过假定数据的分布，数据集中偏离该分布程度较大的数据可认为离群点或者使用数据集中的统计量，例如极值和方差，完成离群点的检测。ZHENG Li等人提出了ECOD(Empirical-Cumulative-distribution-based Outlier Detection)算法，对每个维度，使用经验累积分布函数估计左尾和右尾的概率，并计算该维度的偏度，最终将所有维度的尾部概率进行聚合，得出离群分数。" [source](https://patents.google.com/patent/CN117520980A/zh) |
| 167 | COPOD | **substantive** | "The abnormal data is identified by using algorithms such as a plurality of anomaly detection algorithms COPOD, KNN, isdation, forest in PyOD (Python Outlier Detection, python anomaly detection tool library)." [source](https://patents.google.com/patent/CN117522196A/en) |
| 168 | PyOD | **substantive** | "In this embodiment, the abnormal recognition software to be detected refers to software that uses the analysis of input data, screens and processes abnormal values in the input data, for example, it can be a Python-based Pyod abnormal detection tool library, which contains traditional algorithms and cutting-edge algorithms, such as integrated abnormal detection and deep learning abnormal detectio [source](https://patents.google.com/patent/CN118193395A/en) |
| 169 | PyOD | **substantive** | "Embodiments from PyOD or an official repository thereof are employed." [source](https://patents.google.com/patent/CN118503861A/en) |
| 170 | PyOD | **substantive** | "The machine learning model uses default parameters of the machine learning model by utilizing PyOd library." [source](https://patents.google.com/patent/CN119025849A/en) |
| 171 | ADBench | **substantive** | "These datasets were all from ADBench." [source](https://patents.google.com/patent/CN120234687A/en) |
| 172 | PyOD | **substantive** | "The multidimensional analysis tool is specialized software or algorithms that support detection of risk from different dimensions (time, space, relationships, etc.), for example, on-chain behavior analysis platform CHAINALYSIS, timing anomaly detection library PyOD, or graph computation framework APACHE GIRAPH may be employed." [source](https://patents.google.com/patent/CN121921100A/en) |
| 173 | PyOD | **substantive** | "It uses the \"PyOD\" library to detect outliers." [source](https://patents.google.com/patent/JP2026037293A/en) |
| 174 | PyOD | **substantive** | "Here, PyOD is a Python library for outlier detection in multivariate time series data." [source](https://patents.google.com/patent/KR102909455B1/en) |
| 175 | PyOD | **substantive** | "In one example, various unsupervised anomaly detection methods from pyOD, an open-source anomaly detection toolkit, can be used to identify various types of anomalies in tabular data." [source](https://patents.google.com/patent/KR20250145600A/en) |
| 176 | COPOD | **substantive** | "SUOD: Scalable Unsupervised Outlier Detection je trojmodulový akceleračný framework pre detekciu odľahlých hodnôt, ktorého cieľom je urýchliť trénovanie a predikciu pri veľkom počte dátových bodov." [source](https://patents.google.com/patent/SK2042023U1/sk) |
| 177 | COPOD | **substantive** | "One example outlier detection model is the Copula-Based Outlier Detection (COPOD) model." [source](https://patents.google.com/patent/US12184394B2/fr) |
| 178 | XGBOD | **reference-list-only** | 'Zhao et al., "Xgbod: improving supervised outlier detection with unsupervised representation learning." 2018 International Joint Conference on Neural Networks (IJCNN). IEEE, 2018.' [source](https://patents.google.com/patent/US12242939B2/fr) |
| 179 | PyOD | **substantive** | "PyOD (https://github.com/yzhao062/pyod/) was used to implement AE-MLP." [source](https://patents.google.com/patent/US20230367760A1/en) |
| 180 | COPOD | **substantive** | "In some embodiments, clustering the plurality of signatures is performed using a density-based clustering algorithm (e.g., a density-based spatial clustering of applications with noise (DBSCAN) algorithm or a hierarchical density-based spatial clustering of applications with noise (HDBSCAN) algorithm), Empirical Cumulative Distribution-based Outlier Detection (ECOD), and Copula-Based Outlier Dete [source](https://patents.google.com/patent/US20240333768A1/en) |
| 181 | XGBOD | **substantive** | "The index detection model may be a neural network model, for example, improving supervised outlier detection with unsupervised representation learning (XGBOD), may definitely be another model, and will not be limited herein." [source](https://patents.google.com/patent/US20240339175A1/en) |
| 182 | PyOD | **substantive** | "Existing algorithms can be used for such a process, e.g., PyOD and supervised or semi-supervised outlier classification." [source](https://patents.google.com/patent/US20250365294A1/en) |
| 183 | PyOD | **substantive** | “The episode also touches on tooling: open-source libraries like PyOD and commercial options like Datadog.” [source](https://podcasts.apple.com/in/podcast/how-your-test-suite-can-predict-production-failures/id1896800711?i=1000775157301&l=ml) |
| 184 | PyOD | **substantive** | "For implementation of these algorithms, we follow the example in the open-source, anomaly detection Python package PyOD." [source](https://publications.ri.cmu.edu/storage/publications/2022/08/chufang_MSR_Thesis____Signal_Quality.pdf) |
| 185 | XGBOD | **substantive** | "SUOD: [343] Ensemble approach produce acceleration to different heterogeneous models for anomaly detection." [source](https://publikationen.sulb.uni-saarland.de/bitstream/20.500.11880/40959/1/thesis.pdf) |
| 186 | PyOD | **substantive** | "その点、PyODは異常度を出力する形に予めなっているため、この辺の煩わしさが減り、また、異常検知のための引数も揃っているため、いろいろ試したいときにも実装の手間が省けます。" [source](https://qiita.com/shuns0314/items/c2f7f2855685279ffd43) |
| 187 | PyOD | **substantive** | "This thesis uses PyOD, an open-source Python toolbox for performing scalable outlier detection on multivariate data (Zhao et al., 2019)." [source](https://repositorio.ipcb.pt/server/api/core/bitstreams/c04e8617-3c25-4043-9f2c-e9e9076edcf0/content) |
| 188 | PyOD | **substantive** | "Security vulnerabilities and package health score for pip package pyod" [source](https://security.snyk.io/package/pip/pyod) |
| 189 | PyOD | **substantive** | “PyOD是目前Python环境中最为全面和广泛使用的异常检测工具包，特别适用于数值型表格数据的分析。” [source](https://segmentfault.com/a/1190000045523384) |
| 190 | ECOD | **substantive** | "A wrapper of PyOD’s Cumulative Distribution Functions (ECOD) for Unsupervised Outlier Detection." [source](https://selfexplainml.github.io/PiML-Toolbox/_build/html/modules/generated/piml.data.outlier_detection.ECOD.html) |
| 191 | PyOD | **substantive** | “PyOD: A Python toolkit for outlier detection and fraud analytics.” [source](https://services.delhi.gov.in/sites/default/files/Services/universal-tab/a_compressed_2.pdf) |
| 192 | PyOD | **substantive** | "Erforschen Sie fortgeschrittene Techniken wie LSTMs für Zeitreihendaten und tauchen Sie tiefer in Bibliotheken wie PyOD ein, um die beste Lösung für Ihre spezifischen Anforderungen zu finden." [source](https://shamsher.de/anomaly-detection-techniques-unveiling-hidden-patterns-in-your-data/) |
| 193 | ECOD | **substantive** | “再在 Python 中利用 PyOD 库构建离群点模型，筛选出偏离正常值的离群点作为审计疑点。” [source](https://sjj.wuhan.gov.cn/sjzx/zhlt/202502/t20250224_2538277.html) |
| 194 | PyOD | **substantive** | "Hands-On: Step-by-Step Guide (Using Prometheus + PyOD for ML)" [source](https://sreschool.com/blog/anomaly-detection-in-devsecops-a-comprehensive-tutorial/) |
| 195 | PyOD | **substantive** | “PyOD is a Python library that is devoted to anomaly detection. It contains several reconstruction-based algorithms such as AEs. In this recipe, we’ll build an AE using PyOD to detect anomalies in time series.” [source](https://subscription.packtpub.com/book/data/9781805129233/9/ch09lvl1sec88/building-an-ae-using-pyod) |
| 196 | PyOD | **substantive** | “Anomaly detection için uv ile Python 3.12 sanal ortam, PyTorch 2.5+, PyOD, anomalib, alibi-detect, river, Jupyter Lab kurulumu; Windows WSL2, macOS MPS ve Linux CUDA için adım adım rehber.” [source](https://sukruyusufkaya.com/learn/anomali-tespiti/anomaly-detection-atolye-kurulumu) |
| 197 | PyOD | **substantive** | "The first one is called PyOD. It’s a Python toolkit to implement unsupervised anomaly detection algorithms." [source](https://towardsdatascience.com/fast-anomaly-detection-with-images-f612a6a897ca/) |
| 198 | PyOD | **substantive** | "For this blog post, we used the Pyod library for benchmarking outlier detection algorithms." [source](https://towardsdatascience.com/hbos-vs-iforest-on-macbook-pro-m1-c258d2b5fe6b/) |
| 199 | COPOD | **substantive** | "The PyOD (Zhao et al., 2019) python package was used to perform anomaly detection using each of the methods except Arima and Moving Average." [source](https://trace.tennessee.edu/server/api/core/bitstreams/7b31bf38-dc1e-4d98-93c9-79feed3feceb/content) |
| 200 | PyOD | **substantive** | "This scorer can wrap around detection algorithms of PyOD." [source](https://unit8co.github.io/darts/generated_api/darts.ad.scorers.pyod_scorer.html) |
| 201 | ECOD | **substantive** | "Библиотека PyOD включает в себя более 40 алгоритмов обнаружения выбросов, от классических LOF, PCA и kNN до новейших ROD, SUOD и ECOD." [source](https://vc.ru/id447345/517694-biblioteka-pyod-sravnivaem-algoritmy-poiska-vybrosov) |
| 202 | TrustLLM | **substantive** | "In this context, the introduction of the TrustLLM framework offers a new approach to evaluating the ethical dimensions of large language models." [source](https://vladbogo.substack.com/p/trustllm-trustworthiness-in-large) |
| 203 | PyOD | **substantive** | “PyOD: Une bibliothèque Python spécialisée dans la détection d'anomalies, proposant une large gamme d'algorithmes.” [source](https://www.asprom.com/technologie/BaseVecteur.pdf) |
| 204 | TDC | **substantive** | “Therapeutics Data Commons by Zitnik Lab, Harvard Medical School: Coordinated initiative providing AI-ready datasets, curated benchmarks, and leaderboards across therapeutic modalities and discovery stages.” [source](https://www.biotech.today/tools/tdc) |
| 205 | ADBench | **substantive** | “PyOD是一个全面且易于使用的Python库，专门用于检测多变量数据中的异常点或离群点。” [source](https://www.cnblogs.com/luohenyueji/p/18442742) |
| 206 | PyOD | **substantive** | “Learners will gain hands-on experience building and evaluating these models using Python libraries like PyOD.” [source](https://www.coursera.org/learn/packt-deep-learning-for-time-series-cookbook) |
| 207 | PyOD | **substantive** | “A list of tools that will be used for the operation of this training module. Google Colabs, scikit-learn, pyOD, TensorFlow” [source](https://www.cybersecpro-project.eu/wp-content/uploads/2024/06/D3.3-CyberSecPro_Health_v1.0_FINAL_submitted.pdf) |
| 208 | PyOD | **substantive** | “Enquanto o scikit-learn oferece cinco algoritmos clássicos de aprendizado de máquina (...), o PyOD inclui mais de 30 algoritmos, desde métodos simples, como MAD, até modelos complexos de aprendizado profundo.” [source](https://www.datacamp.com/pt/tutorial/introduction-to-anomaly-detection) |
| 209 | PyOD | **substantive** | "I prefer pyod for its rich library of algorithms and an API consistent with sklearn." [source](https://www.datacamp.com/tutorial/introduction-to-anomaly-detection) |
| 210 | PyOD | **substantive** | "Additionally, the PyOD library - boasting over 10 million downloads - offers access to more than 40 anomaly detection algorithms that integrate easily with Databricks." [source](https://www.dataexpert.io/blog/databricks-anomaly-detection-data-pipelines) |
| 211 | PyOD | **substantive** | “PyOD: A comprehensive Python library with 40+ anomaly detection algorithms.” [source](https://www.educative.io/blog/how-to-get-started-with-anomaly-detection-algorithms-in-5-minutes) |
| 212 | PyOD | **substantive** | "PYOD : https://github.com/yzhao062/pyod" [source](https://www.eurecom.edu/publication/6637/download/data-publi-6637_2.pdf) |
| 213 | DoxBench | **substantive** | "One benchmark had a leading model landing within about a mile of the real spot roughly six times out of ten." [source](https://www.kanary.com/blog/we-doxxed-our-own-teammate-using-chatgpt) |
| 214 | PyOD | **substantive** | “PyOD ist die umfassendste Open-Source-Bibliothek für Anomalie- und Ausreißererkennung in Python. Über 60 Detektoren, von Isolation Forest über Autoencoder bis zu graph- und zeitreihenspezifischen Verfahren, unter einer einheitlichen scikit-learn-kompatiblen API.” [source](https://www.ki-syndikat.de/tools/pyod/) |
| 215 | MemoHarness | **substantive** | "MemoHarness optimizes AI agent behavior via learned experience." [source](https://www.linkedin.com/posts/daily-ai-wire_memoharness-adaptive-ai-agent-harnesses-activity-7483795279952072704-k6U9) |
| 216 | PyOD | **substantive** | “PyOD, or Python Outlier Detection, is a Python package toolkit for detecting outlier data.” [source](https://www.nb-data.com/p/python-packages-for-outlier-detection) |
| 217 | COPOD | **substantive** | “COPOD is an exciting algorithm based on a paper published in September 2020, which you can read here: https://arxiv.org/abs/2009.09463 . The PyOD library offers many algorithms based on the latest research papers.” [source](https://www.packtpub.com/en-FI/product/time-series-analysis-with-python-cookbook-9781801075541/chapter/chapter-14-outlier-detection-using-unsupervised-machine-learning-14/section/detecting-outliers-using-copod-ch14lvl1sec01) |
| 218 | PyOD | **substantive** | "Yue Zhao, Zain Nasrullah, and Zheng Li have produced a paper 'PyOD: A Python Toolbox for Scalable Outlier Detection'[1]." [source](https://www.researchgate.net/publication/358276757_A_Review_on_Anomaly_Detection_using_PYOD_Package) |
| 219 | PyOD | **substantive** | “6.15 Outlier Detection Algorithms in PyOD 02:49.” [source](https://www.simplilearn.com/big-data-and-analytics/machine-learning-certification-training-course?source=GhPreviewCoursepages) |
| 220 | DecAlign | **substantive** | "Introducing DecAlign, a novel framework leveraging prototype-guided optimal transport and latent semantic alignment to enhance multimodal representation learning by decoupling and aligning modality-unique and modality-common features." [source](https://www.slideshare.net/slideshow/decalign-hierarchical-cross-modal-alignment-for-decoupled-multimodal-representation-learning/287568515) |
| 221 | agent-audit | **substantive** | "The numbers make the case plainly: agent-audit achieves 94.6% recall and 0.91 F1 on Agent-Vuln-Bench; Bandit achieves 29.7%; Semgrep achieves 27.0%." [source](https://www.softwareseni.com/open-source-tools-for-scanning-and-red-teaming-agentic-browser-security/) |
| 222 | PyOD | **substantive** | "Pracować będziemy w języku Python z wykorzystaniem bibliotek takich jak scikit-learn, PyOD, Darts, pandas, matplotlib, TensorFlow/Keras." [source](https://www.statsoft.pl/en/szkolenia/wykrywanie-anomalii-w-procesach-z-wykorzystaniem-uczenia-maszyn-machine-learning-2/) |
| 223 | PyOD | **substantive** | “Yue Zhao, Zain Nasrullah, and Zheng Li have produced a paper” PyOD: A Python Toolbox for Scalable Outlier Detection”[1].” [source](https://www.theijire.com/archiver/archives/a_review_on_anomaly_detection_using_pyod_package.pdf) |
| 224 | ADBench | **reference-list-only** | "Han, S., Hu, X., Huang, H., Jiang, M. and Yue Zhao. ‘Adbench: Anomaly detection benchmark.’ Advances in neural information processing systems, 35 (2022): 32142-32159." [source](https://www.thepaper.cn/newsDetail_forward_28539917) |
| 225 | PyGOD | **substantive** | "最后，我们将介绍一个基于 GNN 的图异常值检测库 (PyGOD) 及其与 TigerGraph ML Workbench的集成。" [source](https://www.tigergraph.com.cn/walkman/episode-38/) |
| 226 | PyOD | **substantive** | "PyODは変化量が多い観測データの外れ値検知に活用されるライブラリです。" [source](https://www.tryeting.jp/column/3773/) |
| 227 | PyOD | **substantive** | "Nessa videoaula você será apresentado a noções sobre a detecção de outliers com a Biblioteca PyOD." [source](https://www.youtube.com/watch?v=VJm0EGWpU1g) |
| 228 | TDC | **reference-list-only** | “Optional Reading Applications of machine learning in drug discovery and development Artificial intelligence foundation for therapeutic science Therapeutics Data Commons.” [source](https://zitniklab.hms.harvard.edu/BMI702/lectures/module6/week13/) |
| 229 | TDC | **substantive** | “TDC dataset retrieval tool — load Therapeutics Data Commons benchmark datasets locally via the PyTDC package.” [source](https://zitniklab.hms.harvard.edu/ToolUniverse/_modules/tooluniverse/tdc_dataset_tool.html) |
| 230 | TDC | **substantive** | “Demos and hands-on exercises will use datasets and code available in Therapeutics Data Commons (TDC).” [source](https://zitniklab.hms.harvard.edu/drugml/) |

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

*Update 2026-08-09: **s41598-025-28976-6 is re-promoted.** Phase B fetched the full text and confirmed it cites ADBench, SUOD, and LSCP; it is counted in the 2026-08-09 pass as substantive-use journal evidence. The other two remain in the candidate pool awaiting direct fetch.*

**Count: 170 ecosystem adoption items (154 main-ledger rows through May 13, +7 May 19, +4 May 20, +4 May 28 append-only verified rows, +1 written 2026-08-09: #66dw TechTarget).** (2026-06-13 sweep added 0: all candidates re-surfaced already-tracked rows; see the "## 2026-06-13 Refresh" section.)

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
| 72 | TrustLLM | github.com | “Repositories that depend on trustllm 8 Repositories 0 Packages” [source](https://github.com/HowieHwong/TrustLLM/network/dependents) |
| 73 | auditable | pepy.tech | “auditable · 2.2k downloads on PyPI” [source](https://pepy.tech/projects/auditable) |

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
| 91 | Foresight Institute AI for Safety & Science Nodes Grant. The grantee page names Yue Zhao, USC, and the FORTIS Lab by full expansion, with the project title "Audit-to-Patch Pipelines for Secure LLM Agent Systems". The only third-party page found so far that names the lab itself rather than only the person. Verified 2026-07-31; row written 2026-08-09. | 2026 |
| 92 | “source code repository URL https://github.com/yzhao062/pyod” [source](https://www.wikidata.org/wiki/Q107385358) | 2026 |

**Count: 21 awards/recognitions/encyclopedia entries (19 main-ledger rows, the May 19 ACM SIGSPATIAL award-index row, and the Foresight grantee page).**

---

## Ledger 6: Agent-Auditing Line, External Academic Citations

The lab's current frontier is the newest work, so its external-citation record is small enough to track
row by row and is worth watching as a growth curve rather than a count. This table exists because these
citations would otherwise live only inside a pass section: they are more than bibliography entries (each
has body discussion or a named-mechanism reference), but folding them into Ledger 3 would bury the one
signal that says the agent-auditing line is being read outside the lab.

**Overlap rule.** Every row here also appears in the `/citation-audit` bibliometric tables. Count it once.
This table is the qualitative record of *how* each work is cited; `citation-affiliation-audit.md` is the
quantitative record of *how many*.

| # | Citing work | Cites | How it is cited | Verified |
|---|-------------|-------|-----------------|----------|
| A1 | [arXiv:2607.25364](https://arxiv.org/abs/2607.25364), "Explanation-Bound Tool Execution for AI Agents: Server-Verified Action Claims Without Trusting Model Rationales" (Georgia Tech, UIUC; v1 submitted 2026-07-28 as *Accentrust*, retitled in v2 on 2026-07-29) | Auditable Agents **and** agent-audit | Body discussion, not a bare reference: *"Auditable Agents frames recoverability, policy checkability, responsibility attribution, and evidence integrity as system properties [24]; Agent Audit analyzes code and deployment artifacts before execution [25]."* The strongest external citation of the line to date. | 2026-07-31; title corrected 2026-08-09 |
| A2 | [arXiv:2607.07405](https://arxiv.org/abs/2607.07405), "Reason Less, Verify More" | Aegis | Credits Aegis as the prior art that establishes the mechanism: *"our contribution is therefore not the enforcement mechanism, which pre-execution systems such as AEGIS [12] and AgentSpec [9] already establish"*. | 2026-07-31 |
| A3 | [arXiv:2607.01641](https://arxiv.org/abs/2607.01641) | agent-audit | Reference [39], full title and arXiv ID. | 2026-07-31 |
| A4 | [arXiv:2604.15367](https://arxiv.org/abs/2604.15367) | agent-audit | Reference [50], full title and arXiv ID. | 2026-07-31 |
| A5 | [arXiv:2509.24380](https://arxiv.org/abs/2509.24380), Agentic Services Computing survey | agent-audit | Reference [147] plus three body mentions. A revised version, so the arXiv ID predates the cited work. | 2026-07-31 |
| A6 | [arXiv:2606.04104](https://arxiv.org/abs/2606.04104), "Proof-Carrying Agent Actions: Model-Agnostic Runtime Governance for Heterogeneous Agent Systems" (Zexu Wang, solo) | Auditable Agents | **The strongest form of citation the line has received: a Related Work subsection titled "2.1 Auditable agents and accountability"**, which recites all five dimensions as prerequisites: *"action recoverability, lifecycle coverage, policy checkability, responsibility attribution, and evidence integrity are prerequisites..."*. Three body mentions plus reference [10] on p25 with the arXiv URL. | 2026-08-09 |
| A7 | [arXiv:2606.10457](https://arxiv.org/abs/2606.10457), "Trace2Policy: From Expert Behavior Traces to Self-Evolving Decision Agents" (industry authors) | Auditable Agents | p3 positions the paper directly against the framework: *"Nian et al. [Nian et al., 2026] **formalize agent-auditability**. We provide a deployed instantiation with production data."* Three "Nian" mentions plus the full reference on p10. The only citer so far claiming a production deployment. | 2026-08-09 |
| A8 | [arXiv:2605.29253](https://arxiv.org/abs/2605.29253), "OpenClawBench: Benchmarking Process-side Anomalies in Real-world Agent Execution Trajectories" | Auditable Agents | p4, in a related-work subsection on trajectory-aware evaluation and process anomaly auditing: *"Auditable Agents argues that agent systems should be auditable from execution records, not only final answers [12]."* Full reference on p10. | 2026-08-09 |
| A9 | [arXiv:2606.30970](https://arxiv.org/abs/2606.30970), "Behavioral Governance for Autonomous AI Agents: The AgentBound Framework" (Kaul, Lan, Gupta) | Auditable Agents | p11 body: *"From a mediation cost perspective, Auditable Agents develops structured evidence-design tenets to systematically optimize performance trade-offs associated with pre-execution runtime inspection [8]."* Cites the **overhead result**, which no other citer does. Full reference on p14. | 2026-08-09 |
| A10 | [arXiv:2607.20729](https://arxiv.org/abs/2607.20729), "Operational Identity: A Finite Audit of Declared and Implemented Rules of Sameness" (Denise M. Case, solo, 45 pages) | Auditable Agents | p38 body: *"Work on auditable agents treats auditability as the system property that makes accountability possible (Nian et al. 2026). These approaches expose the provenance an audit needs. The operational identity partition supplies a complementary..."*. Full reference on p45. **Places the work in a records-and-provenance lineage rather than an agent-security one**, cited alongside W3C PROV, PROV-AGENT, and Ojewale et al. on audit trails. | 2026-08-09 |
| A11 | [arXiv:2605.04093](https://arxiv.org/abs/2605.04093), "Decision Evidence Maturity Model for Agentic AI: A Property-Level Method Specification" (Oleg Solozobov, solo, 41 pages) | Auditable Agents, Implicit Execution Tracing, Aegis, Sovereign-OS | **The strongest external citation the line has received, and it cites four FORTIS works.** §2.4 is titled *"Auditable Agents and the Three-Layer Reading"*. The paper states *"The broad auditability-framework coordinate is **owned by** Auditable Agents (Nian et al., 2026a)"* and *"The paper **cedes broad-framework priority to Auditable Agents**"*, then builds its own contribution on the framework's own partition: *"On the Auditable Agents detect/enforce/recover mechanism partition, DEMM positions an explicit assess coordinate alongside the verify and present coordinates"*. 14 "Auditable Agents" occurrences and 19 "Nian" occurrences. **Implicit Execution Tracing is cited in the body twice** (pp5, 24) as "IET final-text signals" inside an evidence-source taxonomy, and **Aegis appears five times as "AEGIS-NTC tool firewall"**. Sovereign-OS is in the reference list. | 2026-08-09 |
| A12 | [arxiv.org](https://arxiv.org/abs/2604.23425) | AEGIS | "AEGIS [11] provides a pre-execution firewall with content scanning and tamper-evident audit trails." | 2026-08-13 |
| A13 | [arxiv.org](https://arxiv.org/abs/2606.15242) | AEGIS | "AEGIS (Yuan et al., 2026) and ClawGuard (Zhao et al., 2026) interpose before tool execution and block risky calls at invocation time." | 2026-08-13 |
| A14 | [arxiv.org](https://arxiv.org/abs/2606.20634) | Auditable Agents | "An April 2026 ecosystem-level empirical audit gives the agent-specific lower bound: Auditable Agents reports 617 security findings across six open-source agent projects, arguing basic auditability prerequisites are widely unmet (Nian et al., 2026)." | 2026-08-13 |
| A15 | [arxiv.org](https://arxiv.org/abs/2607.02599) | AEGIS | "AEGIS (Yuan et al., 2026) adds runtime auditing" | 2026-08-13 |
| A16 | [arxiv.org](https://arxiv.org/pdf/2604.23425) | AEGIS | "AEGIS [11] provides a pre-execution firewall with content scanning and tamper-evident audit trails." | 2026-08-13 |
| A17 | [arxiv.org](https://arxiv.org/pdf/2606.15242) | AEGIS | "AEGIS (Yuan et al., 2026) and ClawGuard (Zhao et al., 2026) interpose before tool execution and block risky calls at invocation time." | 2026-08-13 |
| A18 | [arxiv.org](https://arxiv.org/pdf/2607.02599) | AEGIS | "AgentSpec (Wang et al., 2026) applies per-step DSL rules, AEGIS (Yuan et al., 2026) adds runtime auditing." | 2026-08-13 |
| A19 | [arxiv.org](https://arxiv.org/pdf/2608.02680) | GRADE | "GRADE [31] models an agent run as a graph with separate execution and dependency layers and, closest to us, grades each dependency edge by how it is known (observed, declared, inferred)." | 2026-08-13 |
| A20 | [researchgate.net](https://www.researchgate.net/publication/403607189_Agent_Harness_for_Large_Language_Model_Agents_A_Survey/download) | AEGIS | "AEGIS[113] operationalizes this as a framework-agnostic pre-execution intercept layer, a three-stage pipeline of argument extraction, risk scoring, and policy enforcement intercepting potentially dangerous tool calls before they reach the execution environment." | 2026-08-13 |

**Count: 11 confirmed external academic citations of the agent-auditing line. By work cited: Auditable Agents x7 (A1, A6-A11), agent-audit x4 (A1, A3, A4, A5), Aegis x2 (A2, A11), Implicit Execution Tracing x1 (A11), Sovereign-OS x1 (A11). A1 and A11 each cite more than one work, so the per-work figures sum above 11.**

**Every one of the eleven discusses the work in body text; none is a bare reference-list entry.** Three
recite the five auditability dimensions or the mechanism partition by name (A1, A6, A11), one cites the
overhead result (A9), and one treats the framework as the definition to instantiate (A7). Three independent
authors gave the work a named related-work subsection (A6, A8, A11).

**A standing negative is now falsified.** *Implicit Execution Tracing* was recorded as having **zero**
confirmed external citers as recently as 2026-07-31. A11 cites it in body text under the abbreviation
IET. The FORTIS over-privilege benchmark still has zero external citers, so that half of the negative
stands.

**Citation-base composition, checked 2026-08-09.** Semantic Scholar reports 10 citation edges for
Auditable Agents (arXiv:2604.05485), which resolve to 8 unique works after removing two duplicate records:
6 confirmed external, 1 lab-internal, 1 refuted. **Semantic Scholar is wrong in both directions here,**
which is the methodological lesson of this check. It carries a false edge that survives revision
(arXiv:2606.04990, below) and it misses A11 entirely, the strongest citation in the table. Do not treat an
S2 citation count as the population; fetch the papers.

- **Lab-internal, excluded from the count:** arXiv:2604.17299 (Cat-DPO), whose author list ends in Yue Zhao.
- **Refuted, and re-confirmed refuted at v4:** arXiv:2606.04990, *From Agent Traces to Trust: A Survey of
  Evidence Tracing and Execution Provenance in LLM Agents*. The 2026-07-31 refutation was checked against
  an earlier version, so the paper was re-downloaded at **v4 (updated 2026-06-28, 28 pages, 11 authors)**
  and rescanned: **zero** occurrences of Auditable Agents, 2604.05485, Yue Zhao, agent-audit, or Nian. The
  Semantic Scholar edge is a persistent false edge that survives revision, and S2 carries two records for
  this survey (11-author and 9-author), which is the likely cause.
- **This refuted survey is the highest-value outreach target the audit has identified.** An 11-author
  survey specifically on evidence tracing and execution provenance in LLM agents, now at its fourth
  revision, does not cite the framework paper in that exact area.
- **Recurring cited neighbour worth tracking:** *Right to History: A Sovereignty Kernel for Verifiable AI
  Agent Execution* (arXiv:2602.20214) appears next to Auditable Agents in A9's related work.

**Standing negatives, re-checked each round.** The **FORTIS over-privilege benchmark** still has zero
external citers; every Semantic Scholar citer is lab-internal. *Implicit Execution Tracing* **no longer
belongs on this list**: it was zero as of 2026-07-31, and A11 cites it in body text. The earlier false
positive stands corrected separately, since arXiv:2606.00765 (FALAT) cites "implicit execution traces
[Li et al., 2025b]", a different 2025 work, and is still not a citer. The Aegis cited in arXiv:2606.04990
is Kong et al., arXiv:2509.14295, not the USC paper.

---

## Ledger 7: Scientific Uptake (Peer-Reviewed, Substantive In-Body Use)

Peer-reviewed articles that **run the tools in their methods** rather than listing them in a bibliography.
This table exists for the same reason as Ledger 1b: the items were verified but had no row, and neither
"external third-party media" nor "ecosystem adoption" describes a Nature or Cell Press paper that calls
`pyod.models.knn` in its pipeline. Ledger 3 already carried an awkward "scientific-uptake cluster" note
for exactly this class.

**Inclusion rule, the same split used in Ledger 1b.** Substantive in-body use only. A reference-list
citation is bibliometric evidence that `/citation-audit` already measures, and counting it here would
double-book the same fact. The 2026-08-09 pass verified 30 peer-reviewed articles and admitted 12 of them
under this rule; the other 18 are recorded in that pass section and routed to `/citation-audit`.

| # | Venue | Work used | Evidence |
|---|-------|-----------|----------|
| S1 | *Developmental Cell* (Cell Press) | PyOD | Calls the `pyod.models.knn` detector to identify outlier cells by distance from k-nearest neighbours. The module path, the docs URL, and the arXiv link all appear. The most specific PyOD usage found in any journal. |
| S2 | *iScience* (Cell Press) | PyOD | `pyod 1.0.9` with Python 3.9.16 and the HBOS detector listed as key resources, inside a Broad-Institute-linked JUMP morphological profiling pipeline. A pinned version in a key-resources table is the strongest reproducibility form. |
| S3 | *Stem Cell Reports* (Cell Press) | PyOD | Operational single-cell outlier removal with inline author attribution. |
| S4 | *Nature Scientific Reports* s41598-025-09717-1 | PyOD, ADBench | PyOD named as the implementation in Methods **and** ADBench cited, with `Zhao, Y.` spelled out in both references. |
| S5 | *Nature Scientific Reports* s41598-025-29219-4 | LSCP, PyOD | LSCP used as the working ensemble method rather than cited in passing, for early prediction of very and extreme preterm birth. |
| S6 | *Nature Scientific Data* s41597-026-07203-5 | PyOD | Named as reproduction tooling in a multisource urban water-distribution anomaly dataset. Weaker form: named in text but absent from the 20-entry reference list. |
| S7 | *Nature Scientific Reports* s41598-020-73644-6 | PyOD | Canonical docs URL in the body, machine-learning-guided discovery of non-hemolytic peptides. |
| S8 | *Nature Communications* s41467-026-71441-9 | TDC | TDC oracle v0.4.1 used to build the fine-tuning set for a 3D molecule generation model. |
| S9 | *Nature Communications* s41467-025-59628-y (Token-Mol 1.0) | TDC | In-body dataset use plus a live `tdcommons.ai` project link. |
| S10 | *Nature Communications* s41467-025-65869-8 | TDC | TDC cited as the data-availability accession route, the strongest in-body form of dataset adoption. |
| S11 | *Nature Scientific Reports* s41598-025-99785-0 | TDC | Tool name, `tdcommons.ai` URL, and `Zhao, Y.` in the author list all present. |
| S12 | *Nature Scientific Data* s41597-026-07260-w (SynRXN) | TDC | Names TDC as one of two exemplar standardized ecosystems the field should imitate, which is framing rather than a passing dataset citation. |
| S13 | *Nature Scientific Reports* s41598-026-45091-2 | PyOD | Methods names eight PyOD algorithms; references cite the PyOD JMLR paper. *Verified 2026-07-19 as T1-c; row written 2026-08-09.* |
| S14 | *Nature Scientific Reports* s41598-025-20514-8 | PyOD | Methods states three outlier algorithms implemented with PyOD; cites Zhao et al. *Verified 2026-07-19 as T1-d; row written 2026-08-09.* |
| S15 | *Nature Communications* s41467-025-56173-6 | ADBench | Data Availability links the ADBench repository for the benchmark anomaly datasets used. *Verified 2026-07-19 as T1-e; row written 2026-08-09.* |
| S16 | arxiv.org | PyOD | "In our initial tests, we used the default settings from the PyOD library for each algorithm." [source](https://arxiv.org/abs/2509.19366) |
| S17 | arxiv.org | ADBench | "In our comparative analysis, we evaluate the proposed system against three baseline methods: AD-AGENT, AutoIAD, and a 'Strategist only' variant." [source](https://arxiv.org/abs/2606.04599) |
| S18 | arxiv.org | ECOD | "Among the unsupervised methods, ECOD achieved competitive performance, obtaining a precision of 0.6017 and the highest overall F0.5 score (0.4484)." [source](https://arxiv.org/abs/2607.07335) |
| S19 | arxiv.org | StealthRank | "StealthRank jointly pursues rank and stealth, but its primary status is that of a preprint with a workshop version, not a regular ICML publication." [source](https://arxiv.org/html/2607.14035v1) |
| S20 | arxiv.org | TDC | "We evaluate MCG models, pretrained on GEOM-DRUGS, using nine protein docking oracle functions provided by the Therapeutics Data Commons (TDC) [8]." [source](https://arxiv.org/pdf/2306.14852) |
| S21 | arxiv.org | TrustLLM | "The Attack Objective was formulated based on the criteria established on PsyAlign, while the Method leveraged the jailbreaking techniques proposed in TrustLLM (Huang et al., 2024)." [source](https://arxiv.org/pdf/2603.03047) |
| S22 | doi.org | ECOD | “Outlier detection was performed using ECOD from the PyOD library[21] thus retaining energy barrier information for 645 molecules after excluding outliers.” [source](https://doi.org/10.1002/advs.202405596) |
| S23 | doi.org | TrustLLM | “Recent examples for large language models (LLMs) that fall under our definition of a benchmark suite include DecodingTrust,22 TrustLLM,23 and HELM,24 as well as the set of evaluations used in model cards like Claude 3’s25 and Llama’s.26” [source](https://doi.org/10.1016/j.patter.2024.101080) |
| S24 | doi.org | PyOD | “All functions in SEAOP were compiled in Python (Version 2 and 3 using six, numpy, scipy and scikit-learn, PyOD), and it was deployed on a server with Intel (R) Xeon (R) CPU E5-2683 running on the Ubuntu release 16.04.12, operating system.” [source](https://doi.org/10.1093/bib/bbae129) |
| S25 | doi.org | ECOD | “To enhance outlier detection, aMLProt combines predictions from eight PyOD algorithms: Isolation Forest, LOF, ECOD, OCSVM (One-Class Support Vector Machines), PCA, KNN (K-Nearest Neighbors), Angle-Based Outlier Detection, and Histogram-Based Outlier Detection.” [source](https://doi.org/10.1093/bioinformatics/btaf543) |
| S26 | doi.org | PyOD | “Other requirements: pandas, combo, tqdm, pyod, scikit-learn, numpy, networkx, karateclub” [source](https://doi.org/10.1093/gigascience/giaf034) |
| S27 | doi.org | PyGOD | “DL module: It supports graph-based anomaly detection models from the PYGOD library.” [source](https://doi.org/10.1093/nargab/lqaf135) |
| S28 | doi.org | ECOD | “The method first employs the empirical-cumulative-distribution-based outlier detection (ECOD) algorithm to identify abnormal signals of read depth (RD) for preliminary detection of CNVs.” [source](https://doi.org/10.1142/s0219720026500083) |
| S29 | doi.org | PyOD | “For anomaly detection, peptides encoded by prot_t5_xl_uniref50 transformer-based PLM were applied onto 2D and 3D autoencoders, variational autoencoder and denoising autoencoder models, using ‘AutoEncoder’ function from python pyod v1.0.1 package.” [source](https://doi.org/10.1186/s13073-023-01225-z) |
| S30 | doi.org | ADBench | “The other methods—MetaOD, PyOD2, AD-Agent, ADBench (mixed), and AutoAnoEval—perform model selection for each dataset.” [source](https://doi.org/10.18653/v1/2026.findings-eacl.183) |
| S31 | doi.org | PyOD | “This paper proposes the Python toolkit, PyOD, as an approach for microservice anomaly detection.” [source](https://doi.org/10.18803/capsi.v22.177-186) |
| S32 | doi.org | PyOD | “For detecting outlier in the traffic we have used ABOD technique contained in the PyOD-library, which is an open-source toolbox provided in Python for identification of anomaly on multi-variate information.” [source](https://doi.org/10.35940/ijitee.f4557.049620) |
| S33 | link.springer.com | ADBench | “All datasets used in this study are publicly available.” Notes: “https://huggingface.co/datasets/kendx/NLP-ADBench/tree/main/datasets/email_spam.” [source](https://link.springer.com/article/10.1007/s10994-026-07080-4) |
| S34 | link.springer.com | ECOD | "In this research, we utilized the Python implementation of the ROD algorithm (https://github.com/yzhao062/pyod/blob/master/pyod/models/rod.py; Almardeny et al. 2020; Zhao et al. 2019b) to determine the outlier scores for all stream sediment samples." [source](https://link.springer.com/article/10.1007/s12145-025-01811-2) |
| S35 | link.springer.com | PyOD | "We use PyOD [36] Python library to implement anomaly detection algorithms." [source](https://link.springer.com/article/10.1007/s13755-023-00221-2) |
| S36 | onlinelibrary.wiley.com | PyOD | "We have extracted the state-of-the-art methods for anomaly detection from the PyOD library Zhao, Nasrullah, and Li (2019)." [source](https://onlinelibrary.wiley.com/doi/abs/10.1111/exsy.13767) |
| S37 | pmc.ncbi.nlm.nih.gov | COPOD | “The experiments were performed using Python where the models have been implemented using the Scikit-learn [44], PyOD [45] and Tensorflow [46] packages.” [source](https://pmc.ncbi.nlm.nih.gov/articles/PMC11720628/) |
| S38 | thesai.org | PyOD | “The first set of data was used to train five separate anomaly detection algorithms available in the PyOD Python package [10] by first initializing them and then applying the fit function that received the training set of data.” [source](https://thesai.org/Downloads/Volume13No9/Paper_108-A_Comparative_Study_of_Unsupervised_Anomaly_Detection_Algorithms.pdf) |
| S39 | nature.com | PyOD | “Detecting outliers in train and validation datasets was performed with the K-nearest neighbour algorithm [25] of PyOD [26] library was used by measuring the distance of an observation to kth nearest neighbour as the outlying score.” [source](https://www.nature.com/articles/s41416-021-01455-1) |
| S40 | nature.com | TDC | “Two notable examples include Therapeutics Data Commons157 and MoleculeNet158, which provide AI-ready datasets and benchmarks for multiple prediction tasks, including toxicity and ADR prediction, as community resources implementing various evaluation tools and leaderboards metrics.” [source](https://www.nature.com/articles/s41573-025-01164-x) |
| S41 | nature.com | COPOD | “The backend was implemented in Django rest framework, with PyTorch Geometric, PyOD libraries, and it is available at https://github.com/win7/GEMNA_Backend.git.” [source](https://www.nature.com/articles/s41598-024-80955-5) |
| S42 | nature.com | TDC | “The two kinase–drug binding-affinity datasets, Davis27 and KIBA28, were curated by and available in the Therapeutics Data Commons benchmark73.” [source](https://www.nature.com/articles/s42256-023-00751-0) |

**Count: 15 peer-reviewed articles with substantive in-body use (PyOD x7, TDC x5, ADBench x2, LSCP x1; S4 and S5 each use two works).**

Every TDC row carries the standing coauthorship-dilution annotation: TDC is Harvard-led with many
coauthors, and the work predates the PI's USC appointment. Cell Press (S1 through S3) is a venue family
the audit did not record for PyOD before 2026-08-09.

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
| Government/Policy citations (Ledger 1) | **37** as of 2026-08-30. History: **29**, recounted 2026-08-09 directly from the table, which now carries every verified promotion as a row. Composition: 19 rows standing before 2026-07-31, +5 for the 2026-07-19 Tier 0 promotions (rows 9-13), +1 for the 2026-07-31 NIST webinar deck (row 3b), +1 for FLI Summer 2026 moved here from Ledger 2 (row 7b), +3 net new this round (2g Brazil Tesouro Nacional, 2h Indonesian Kemenkeu, 8h OpenAI PyOD 2.0). Row 2f merges the METI and NEDO promotions, so promotions number 30 against 29 rows. The figure published before this reconciliation was 20. **Updated 2026-08-13: 29 + 4 = 33. Updated 2026-08-30: 33 + 4 = 37** (rows 18 ECOD/BIS, 19 International AI Safety Report 2025, 20 and 20b NICT). The in-table count line read 28 until 2026-08-30 because it never took the 2026-08-13 increment; it is now computed from the table and agrees with this row. |
| Government technical reports (Ledger 1b) | **8**, new table. Six DOE substantive-use rows verified 2026-07-31 that had no ledger row, plus SLAC and Sandia/HPOD from this round. Six bibliography-only DOE records are excluded by the table's own rule and routed to `/citation-audit`. **Updated 2026-08-13: 8 + 5 = 13.** |
| External third-party media (Ledger 2) | **80 counted** across 81 rows (#22 SitePoint is present but marked REMOVED). +1 for a 2026-07-31 promotion (#36an), +7 for 2026-07-19 promotions (#36ao through #36au). The figure published before this reconciliation was 83, which was never reproducible from the table; four of the eleven items it counted belong in Ledger 1 and Ledger 7 rather than here. **Updated 2026-08-13: 80 + 13 = 93.** |
| Ecosystem adoption (Ledger 3) | **170** (154 main-ledger rows through May 13, +7 May 19, +4 May 20, +4 May 28, +1 written 2026-08-09: #66dw TechTarget). The table shows 97 rows because the 2026-06-02 pass folded Tier-5 aggregator, non-English tutorial, and SecTools.tw rows into prose buckets with counts preserved. **Updated 2026-08-13: 170 + 164 = 334.** |
| First-party/community (Ledger 4) | **19** (6 table rows + 13 May 19 append-only verified rows recorded in prose) **Updated 2026-08-13: 19 + 2 = 21.** |
| Awards/recognitions (Ledger 5) | **21** (19 main-ledger rows, +1 May 19 ACM SIGSPATIAL award-index row, +1 written 2026-08-09: Foresight Institute grantee page) **Updated 2026-08-13: 21 + 1 = 22.** |
| Agent-auditing academic citations (Ledger 6) | **11**, new table. Five verified 2026-07-31 that had lived only inside that pass section, plus six confirmed 2026-08-09 by direct PDF scan of the Auditable Agents citation graph. One of the six (A11, DEMM) cites four FORTIS works and is absent from the Semantic Scholar graph entirely. Every row also appears in `/citation-audit`; count once. **Updated 2026-08-13: 11 + 9 = 20.** |
| Scientific uptake (Ledger 7) | **15**, new table. Peer-reviewed articles with substantive in-body use: 12 admitted from the 30 verified on 2026-08-09, plus the three Nature-family papers verified 2026-07-19 that the audit had filed as Ledger 2. Reference-list-only citations are excluded and routed to `/citation-audit`. **Updated 2026-08-13: 15 + 27 = 42.** |
| **Total verified items** | **582.** Sum of the eight ledgers above. Recounted 2026-08-13 at 578; 2026-08-30 added 4 Ledger 1 rows and changed no other ledger. This replaces 353, which was accurate as of 2026-08-09. The 2026-08-13 round added 225 rows: Ledger 1 +4, Ledger 1b +5, Ledger 2 +13, Ledger 3 +164, Ledger 4 +2, Ledger 5 +1, Ledger 6 +9, Ledger 7 +27. |

**The reconciliation is now closed.** Every promotion recorded in the 2026-07-19, 2026-07-31, and
2026-08-09 pass sections has a ledger row. Two ledgers were created for classes that had no home
(government technical reports, scientific uptake), one for a class that was growing fast enough to
deserve its own growth curve (agent-auditing citations), and four items were moved out of the ledger a
prior pass had assigned them to. **The rule that prevents recurrence is stated at the end of Ledger 1:
write the ledger row in the same commit that records the promotion.**

Still uncounted, and deliberately so: 52 Tier 3 and 48 Tier 5 candidates from 2026-07-19, and roughly
1,231 unverified Phase A candidates from 2026-08-09, all in `news-search-candidates.jsonl`.

- **121 papers + 21 tools** searched across all core dimensions plus the standing auditability lane and an unscoped open dragnet (citation-audit used 116 non-survey papers)
- **11,551 Google Scholar citations** (Apr 2026)
- **39.11M+ PyPI downloads** for PyOD
- **1,846 Semantic Scholar citations** for Diffusion Models survey
- **~285 Semantic Scholar citations** for TrustLLM
- **5+ books** with dedicated chapters on PyOD/COPOD/ECOD (Manning, Columbia, Apress, Routledge, IntechOpen)
- **2 podcasts** naming PyOD
- **5+ online courses/training pages** teaching PyOD (DataCamp, Udemy x2, O'Reilly video, Python Charmers / Datastat / RX-M / WUNU cluster)
- **8 enterprise integrations** (Databricks x2, Walmart, IQVIA, Apache Beam / Apache Software Foundation, PostHog, MLflow community flavor, Genentech/Roche Data Detective), 1 vendor whitepaper (Altair), 1 EU research project deliverable cluster (SEDIMARK Horizon Europe D3.1 p.18, D5.2), plus finance/audit workflow evidence from Discover Data and Syntora; PyOD GitHub Dependents aggregate snapshot 2026-05-07 = 5,493 repos + 139 packages
- **49 patents** citing PyOD/COPOD/ECOD/LSCP/SUOD/XGBOD/TODS/ADBench, counted as distinct patent numbers named anywhere in this audit (CN 29, US 11, WO 3, KR 2, EP 2, SK 1, JP 1). 18 stood before 2026-08-13; that round verified 31 more with named assignees including Visa International, Tencent, Baidu, China Mobile, Ping An Medical, CETC 54, Harbin Institute of Technology, and Atlas Space Operations. The earlier bullet said 12 and the site said 15; both were prose cluster counts taken before any patent had its own ledger row.
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
