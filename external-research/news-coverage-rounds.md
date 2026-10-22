# News-Search Round Notes, May to October 2026

Moved verbatim from `news-coverage-audit.md` on 2026-10-17, with relative links re-pointed to this folder; rounds from that date on are written here directly. These are the per-round method notes, verification write-ups, corrections and site-propagation records. They stay in the repository so earlier reasoning remains checkable and so `skills/news-search/scripts/build_identity_index.py` still indexes every URL and identifier they name. The counted evidence lives in the ledgers of `news-coverage-audit.md`; where a figure here disagrees with a ledger, the ledger is current. Section references such as "below" point within this file.

---

*Run history (full details in the dated pass sections and git history):*
*2026-10-17: Full Agy search (48 lanes, 43 verification units over 635 candidates) with a Claude refute pass over the 117 high-tier keeps, plus a cleanup of the audit's ledgers. Ledger 1 +2, Ledger 2 +3, Ledger 3 +96 rows and 276 clustered items, Ledger 5 +3, Ledger 6 +13, Ledger 7 +43. Patents: 116 distinct inventions. See the section below and the run archive.*
*2026-10-14: One-hour-capped targeted Codex pass. Ledger 1 +2, Ledger 2 +2, Ledger 3 +35; Hysen named-review status verified. Patents: 107 distinct inventions. Full inventory coverage is not claimed. See the bounded pass below.*
*2026-10-02: Codex coordinated the full Agy Gemini search over 151 inventory items and 218 domains. All 391 verification candidates resolved to a recorded outcome. New independent evidence: Ledger 1 +4, Ledger 2 +7, Ledger 3 +126, Ledger 6 +6, Ledger 7 +16; plus four first-party/community records and one historical Ai2 backfill. Patents: 97 distinct inventions. Nineteen sources remain held. See the 2026-10-02 pass below.*
*2026-09-22 (Phase A: 37 Agy lanes via /prun; Phase B: 16 Agy units over 378 candidates plus 2 surface-audit units): 37 of 37 lanes complete, zero FALLBACK. Phase A returned 1,014 records over 956 unique URLs, 779 absent from the index, and Phase B verified all 378 candidates with none deferred. **One net-new Tier 0 document, with a qualification.** A Japan MIC committee material adopts TrustLLM's six dimensions as the evaluation axes for a national AI-security evaluation platform. Takeshi Takahashi of NICT presented it, as he did the symposium deck at Ledger 1 row 20b, so it shows the work reaching a ministry venue rather than a second organisation adopting it. Net new: **Ledger 1 +1, Ledger 2 +14, Ledger 3 +117 items on 83 rows, Ledger 6 +3, Ledger 7 +30**. Another 75 records went to /citation-audit as a tracked JSONL manifest. **Patents move 49 to 94 distinct inventions.** Ledger 3 already held 89 patent rows and this round added 13, while 8 rows are second publications of an invention another row holds. **The published total of 582 was never reproducible**: the eight figures printed above it summed to 364, and four ledgers' count lines had stopped tracking their own tables. Recounted from the live tables, the ledgers hold **731 rows carrying 771 items**. The round's method result is a reverted rule. A rewrite of the Phase A tier rule rested on a movement count the verdict records cannot produce, because `tier_was` was written on 70 of 481 records. That field is now mandatory. Five awards were re-linked, four whose pages named no recipient and one whose page was dead, and the NVIDIA award was unlinked. Details in "## 2026-09-22 Pass".*
*2026-09-12 (Phase A: 32 Agy lanes via /prun, the first round with Codex out of discovery entirely; verification: 9 Claude agents via /workflows): 32 of 32 lanes complete, zero FALLBACK, 660 records over 616 unique URLs, 497 coverage candidates resolving to 454 unique URLs of which 304 were absent from the 1,929-URL index. Net new **+1 Ledger 1** (the Allen Institute for AI ships TrustLLM's JailbreakTrigger set as a task in `allenai/safety-eval` and as a Hugging Face dataset, and reports Tülu 3 scores on it at §7.2.1, the first frontier lab to carry this work as infrastructure rather than a citation), **+1 Ledger 1b** (SLAC OSTI 3005876, MetaOD's first appearance in a government document, a separate paper from the SLAC row already held), **+1 Ledger 2** (CrowdStrike threat research evaluating COPOD in a command-line malware ensemble), **+1 Ledger 3** (Databricks DAXS training 10,000 ECOD models over ~1.4B records, attributed to the linked repo because the post itself names neither ECOD nor PyOD). **Verification changed five of the thirteen claims it touched**: 4 of 9 were already-counted items reached by a new URL, including the KDD workshop copy of Ledger 6 row A2, and the Chemistry World row was refuted outright (51 configurations not 22, Yue Zhao named nowhere, critical of TDC rather than endorsing it). The round's most useful output is two site numbers, both sums presented as totals: `55M+` downloads is stale against **59,377,536** lifetime (pepy.tech) and a lane's "21.7M cumulative" was the 180-day pypistats retention window, which publishes no cumulative field; the **6,906** ecosystem dependent sum overstates by ~17% because the sibling libraries sit in each other's dependency closure and it counts pyod's own forks. **Seven standards tracks and seven specifications were fetched in full and none cites the agent-auditability line**, AAS-1 v0.1 nearest of all by arriving at the same framing independently; the UK AISI Inspect Evals Register is the one open submission window. The patent lane returned 65 distinct numbers, of which 49 were not already indexed. **A second, dedicated round then swept the auditing line** (12 Agy lanes + 13 Claude agents over three methods the lanes do not use), 12 of 12 complete, 504 records: **+6 net-new Ledger 6** plus one reverification, every one fetched with authors verified independent, covering five of the fourteen works, so **the standing note that Praetor was the only baseline precedent no longer holds**. The seventh, arXiv:2608.18351 against FORTIS, was already recorded on 2026-08-30 and is a reverification rather than a discovery, caught on review because the lane suppression list covered the ledger tables and the URL index but not the preceding pass's prose. **IET's zero is falsified** on two fetched bibliographies (Crew Scaler arXiv:2603.09002 reference [991]; DEMM arXiv:2605.04093 page 38), reversing this round's own first call of "open": a sweep that finds nothing across eight indexes does not outweigh a reference entry someone read. Plus 8 comparison finds from the lanes with **almost no overlap** with the workflow's seven, which is the round's methodological result. Two findings outrank the citation count: **seventeen surveys that draw this subfield's map carry none of the fourteen works** (and arXiv:2605.06812 carries GRADE's idea one month earlier, a priority problem rather than a visibility one), and **three of the seven confirmed citations were recovered by no service queried in this run**, two citing a repo URL that an identifier match cannot key on and one sitting on OpenReview; every sampled OpenAlex record carried empty outgoing reference metadata, which limits what a retrieval failure there can be read to mean. An earlier reading that vendors had adopted the line's vocabulary is **corrected**: a phrase-level sweep found the coinages have not leaked at all. The full name "Yue Zhao" appears in two of the seven citing documents, the Long-Horizon survey and the Audita PDF. **A third dispatch then verified every candidate both rounds had left unverified**: 16 Agy lanes over 420 candidates, 16 of 16 complete, 420 of 420 records, **319 confirmed, 63 dropped, 23 unreachable, 15 refuted**. Its headline is a measurement of Phase A rather than a new find: **110 tier downgrades, 310 unchanged, and zero upgrades**, a 26.2% one-directional error rate, with 5 of 6 Tier 0 claims failing to hold and **five candidate addresses that do not exist** (four GitHub repositories and one Hugging Face Space, all 404). All eight comparison finds hold, and four of them sat at an invented address whose real document Phase B located under a different owner. Confirmed additions: **49 of 49 patents** (39 CNIPA, 45 new rows), **+13 Ledger 6** (the auditing round's six net-new citers, the six deferred priority candidates that all verified, and PolicyFaultBench), **+6 Ledger 7**, **+11 Ledger 2** and **+57 Ledger 3**. Three standing negatives fall: CatchBench, No Attacker Needed and MemoHarness. Citing surveys move 4 to 7, so the omission share is 71% rather than 81%. **A fourth round then went back at everything still blocked** with 6 lanes sliced by alternate route: 22 confirmed, 8 still blocked with every route named, 6 verified-negative, 2 dropped, and **17 of the 25 blocked or gated items converted to a decision without touching a paywall**. The route that matters is Crossref's deposited reference lists, which settled both "must not be recorded as zeros" surveys through a 403 at both publishers: MDPI 10.3390/ai7080298 cites nothing of this lab's across 112 references, and **ACM Computing Surveys 10.1145/3837083 cites TrustLLM at reference 77** across 195. Packt companion repositories settled 6 subscription-reader books. **The six repository leads a sweep found and never fetched all six verified**, which with the six deferred priority candidates makes every deferred lead in this pass verify, twelve for twelve. The Autonomy Tax zero falls, and **GRADE was never at zero: Ledger 6 row A19 and Ledger 3 row 77 already held its citations while two sweeps published it as a zero**, because nobody ran the zeros question against the ledger. Five academic zeros hold, three of them alongside real code adoption. The identity-key defect that cost this pass six instances now has a script, `skills/news-search/scripts/build_identity_index.py`. Details in "## 2026-09-12 Pass".*
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

## 2026-10-21 Full Search, Time-Boxed Verification

Method and counts are in the [run archive](news-search-2026-10-21/README.md). This entry records the decisions and the process faults.

### Decisions

- A national cybersecurity agency page that republishes a CVE is the same vulnerability as the NVD record, so SingCERT, INCIBE-CERT, CERT.hr and the CISA enrichment fold into Ledger 1 row 13. Press coverage of the CVE stays in Ledger 2.
- A research paper by staff of a foundation-model company (Amazon Science, Microsoft Research) is not an official company document. It goes to Ledger 7 when it runs a tool, and to the citation audit otherwise.
- A public comment filed on regulations.gov belongs to its author, so the CGS Administrators response to a CMS request for information is a Ledger 3 enterprise document.
- A procurement specification issued by a judiciary council is an official government document (Ledger 1 row 35).
- A translation that republishes a counted government document is a mirror of that document, so the SECRSS translation of NIST AI 100-2e2025 is noted on Ledger 1 row 3 and is not a Ledger 2 row.
- Patents that cite TDC, the diffusion-models survey or TrustLLM are Ledger 3 rows outside the anomaly-detection patent count, as row 617 already was.
- Verification units never see the ledgers. The coordinator therefore re-checks every kept verdict by URL variant, DOI and PMC ID before it becomes a row; nine documents already held under other addresses were caught that way.
- A GitHub file is one document whatever ref its URL names (a commit hash, `HEAD`, `main`), and a repository root is the same document as its README. Review found 52 records that repeated a document under such variants (and two Ledger 4 copies of the LLNL report already cited in row 102); they are `already_recorded` or `duplicate` in the archive. DOI and PMC copies of 14 Ledger 7 articles were removed the same way.
- The citation audit now completes truncated author lists from `skills/citation-audit/references/full-author-lists.json` and folds diacritics in names, and direct-check outcomes live in `skills/citation-audit/references/citation-audit-overrides.json`.

### Process Faults

- zsh does not split an unquoted variable, so the first launch passed 42 unit ids as one argument. Both dispatchers rejected it before starting anything.
- The Claude discovery lanes had no time box and ran until the user's 30-minute limit, when the workflow was stopped. Their candidates were written progressively; the CJK lane's staged drafts were taken from its download folder.
- Two Agy discovery lanes ended in FALLBACK at the final message (a malformed tool call and an output-token overrun). Their answers were recovered from the stream events, and the truncated pdf-models lane was re-run with an output limit.
- A verification workflow was first launched with a placeholder argument and stopped before any agent returned.
- 79 Agy units on the Claude and GPT group exhausted it (five-hour window to 0%, weekly from 65% to 12%). The long-tail units failed, and their records stay unverified.
- The 45-minute verification limit left 829 records unverified, mostly long-tail Ledger 3 material. They are held in the archive for the next round.

### Propagated to the Site

- Patent figure 116 to 144 with the new country split, and claim-level 21 to 27: `opensource.html`, `files/bio.txt`, `index.html` (prerendered), `llms.txt`.
- Argentina (Buenos Aires council procurement) and Singapore (GovTech AI Playbooks) rows in the PyOD impact card, and both in the `llms.txt` government-tooling line.
- Held back: the NIST summer-fellowship abstract book (one student abstract) and the new Ledger 6 and Ledger 7 rows, which change no card's headline.

## 2026-10-17 Full Search and Audit Cleanup

Method, findings, corrections and the file list are in [the run archive](news-search-2026-10-17/README.md). Every candidate, with its verdict, quote, locator, refute outcome and ledger row, is in its `candidates.jsonl`. This entry keeps only what a later round has to act on.

Decisions that change how later rounds classify or count:

- Hysen Labs pages are AI-drafted catalog entries by the site's own editorial policy, so they belong in Ledger 3. This reverses the 2026-10-14 decision below; Ledger 2 row 50 is now Ledger 3 row 668.
- The OECD.AI catalogue's TrustLLM record was created by the catalogue's automation. It is a Ledger 3 listing, not an OECD citation.
- A policy organization's report that cites a work (RAND, CSET) is a Ledger 1 row, and so is a consulting firm's report. A consulting firm's client brochure (Deloitte AIxAML) is a Ledger 3 row. A co-author institution's own feature (LLNL) is a Ledger 4 row.
- Workshop organizer and committee roles are not awards.
- The FALAT entry in the disambiguation registry is reversed: arXiv:2606.00765 cites the lab's work.
- Ledger 3 counts its long tail in counted cluster rows (661 to 667) that point to the archive.
- A patent counts as a distinct invention only after a family check against its "Also Published As" list. The base fell from 107 to 106 because row 182 is a continuation of row 272, and two of this round's 13 patent rows merged into older rows. A recount over all 121 patent rows found 21 inventions that name a tool in numbered claims, where eleven had been published.
- A match in round prose is not a ledger row. Seventeen promotions written in earlier round prose had never reached one; this round re-verified them as candidates `O1` to `O15e` and `P1` to `P3`.

Two process faults are recorded. The coordinator stopped the Claude discovery workflow after misreading another model's weekly meter as this session's quota, and `dispatch_lanes.sh` failed its preflight on macOS, which has no GNU `timeout`. The script now falls back to `gtimeout` or a shell watchdog.

### Propagated to the Site

| Surface | Change |
|---|---|
| `opensource.html` | Patent row to 116 (China 85, US 19) and 21 claim-level inventions; Deloitte row reworded to a figure credit; SDAIA newsletter row added to the TrustLLM card; the LLNL row now names LLNL as a co-author institution, and the DOE methods-use summary no longer lists LLNL. |
| `files/bio.txt` and `index.html` | "cited in 116 patents"; `index.html` regenerated with `scripts/prerender_pages.py`. |
| `llms.txt` | Patent bullet to 116 with the new split and claim count; SDAIA added to the TrustLLM policy line. |

No homepage news item is added.

## 2026-10-14 Bounded Codex Search

The user capped this run at one hour: 2026-10-15 05:28:50 to 06:28:50 UTC. Three native Codex workers searched security vendors, institutional sources, and media/ecosystem sources while the coordinator checked patents. The configured Codex lane dispatcher was absent after bootstrap, so native workers replaced it. This targeted pass uses an inventory of 133 publications and 22 tools; it does not claim full inventory or seeded-domain coverage. The October 2 full matrix remains unchanged.

New counted evidence: Ledger 1 +2, Ledger 2 +2, and Ledger 3 +35. Hysen Labs retains its existing media classification because the current page records named editorial approval. Patent families move from 97 to 107, including four additional inventions whose numbered claims name a tool. These ledgers measure different evidence and have no combined impact total.

FERZ's October 9 article is the strongest match for the remembered vendor page. It cites Auditable Agents in an analysis contrasting audit evidence with runtime authorization. DataSpeckle's August article is another possible match. Argus Security also links the paper, but its founder/cofounder/advisor overlap makes it first-party evidence. Rivista AI published a separate October 8 feature. Agent Exchange implements the five dimensions in a scoring function; OpenClaw Aegis Signer cites AEGIS as inspiration for an after-execution signing plugin. Both codebases were inspected without executing them.

IBM's March 2021 report names PyOD in its fictional Anomaly Finder teaching example. This is educational evidence, not actual enterprise deployment. Oracle's environment and license documentation strengthens its existing row. BIS Working Paper 1245 and JRC146034 cite TrustLLM; these establish research citations, not benchmark adoption. Seagate requisition 15158 names PyOD as a desired skill, which establishes hiring demand rather than deployment. These older sources are historical backfills.

Several tempting claims were withheld or corrected. Google Assured OSS lists PyOD only in an older Japanese catalog among the checked versions; the current English page omits it. The Spanish Army MANPREDIC deployment remains held because a direct PyOD mention was not verified. A new drug-discovery review cites TDC, but its DrugAgent reference names a different paper. NRC Canada's TrustLLM discussion goes to citation handoff because its experiments use SORRY-Bench. The prior held TDC audit resolves to already-counted Ledger 7 S51. GAO-25-108519 was recovered from a public archive and checked in full; it contains no target citation. Oracle IoT remains unsupported.

Three small Agy prun units then completed 78 searches over recent government publications, security reports, and industry rules. ORNL, INL, and CrowdStrike were duplicates; the INL primary PDF was backfilled. CISA names PyOD under CVE-2026-15529, while the worker confused it with an adjacent unrelated CVE. EDPB names a different European TrustLLM project. No additional verified rule adoption was found. Partial OWASP landing-page checks and search-only results are not full-document negatives. See [the reviewed supplement](news-search-2026-10-14/prun-supplement.md).

The public impact page receives Oracle, BIS, JRC, FERZ, Rivista AI, and the two downstream-code examples. Patent figures are synchronized in the biography, prerendered homepage, and llms.txt. No homepage news item is added. The older citation-affiliation snapshot remains dated September 12 and incomplete; this run records handoffs without silently refreshing it.

Machine-readable outcomes, exact queries, per-item coverage, source hashes, and checks are in [the run archive](news-search-2026-10-14/README.md). Raw fetched files remain in the local scratch directory, outside the repository. Workers did not commit or push; publication was authorized separately after review.

---

## 2026-10-02 Full Search (Codex Coordinator, Agy Gemini Workers)

Searched all **129 publications and 22 tools** across D1-D8 and D10, including all **218 seeded domains**. The 39 discovery assignments plus replacement/gap-repair runs logged **2,219 search calls**. They produced 645 raw records, 556 normalized URLs and 551 document candidates. Local checks removed 121 already tracked documents and 39 first-party surfaces before all 391 remaining candidates received Phase B verdicts. Query coverage has no unassigned inventory items or unqueried seeded domains; search coverage does not guarantee that every external mention was found.

After coordinator review, **164 rows are added**: Ledger 1 +5 (including one historical backfill), Ledger 2 +7, Ledger 3 +126, Ledger 4 +4, Ledger 5 +0, Ledger 6 +6, and Ledger 7 +16. These ledgers measure different evidence types and should not be summed into an impact metric. The remaining outcomes are 35 routine academic citations handed off for a later citation audit, 29 topic-only sources, 12 verified negatives, 19 held sources, and 292 excluded records.

The strongest new direct evidence is the European Parliament study citing the election-reasoning paper, Bundesbank's COPOD/ECOD benchmark evaluation, the Swedish Defence Research Agency's ADBench resource listing, the 2024 interim international AI safety report citing the diffusion-model survey, and a Newsweek opinion essay discussing CHI-Bench. The six-dimensional TrustLLM benchmark as a whole is not claimed as an Ai2 dependency: Ai2 uses the 400-prompt JailbreakTrigger subset. That finding was already verified in September and receives its missing ledger row here.

Source review corrected several worker claims. Bundesbank evaluates four financial datasets; its discussion of 57 ADBench datasets concerns prior work. FOI lists an evaluation resource, which does not establish deployment. A government-hosted Swiss journal article belongs in scientific uptake. Theses remain ecosystem evidence. METI, CISA, Huawei's PMLR paper, the 2025 international AI safety report, CERN's talk/video, and several syndications were already counted. PDF/HTML, translated digest pages and corrected URLs for the same document count once.

Three newly verified patent families increase the distinct-invention count from **94 to 97**: CN114785965B (COPOD hyperspectral exposure), CN113093985B (LSCP sensor-link detection), and US20240045956A1 (ECOD malicious-source-code baseline). Country/publication-office distribution: China 72, US 15, WIPO 3, EPO 3, Germany 1, Japan 1, Korea 1, Slovakia 1. The COPOD patent explicitly names the algorithm in numbered claims; the other two are specification/method evidence.

The current citation-affiliation audit is dated **2026-09-12** and is explicitly incomplete: OpenAlex exhausted its daily budget before querying citing works. Its full current tables, institution summary and coverage section replace the stale embedded May copy below, with the warning retained. This run does not rerun bibliometric discovery or treat absent entries as zero citations.

Historical count corrections are separate from discovery: Ledger 4 previously claimed 13 prose items without corresponding records, and Ledger 5 counted its Foresight page twice. Ledger 7's inherited count included an unverified preprint, so its total is now labeled as records rather than universally confirmed peer-reviewed articles. The former grand total is removed because the ledgers overlap and use different counting units.

Execution note: D10 used Gemini CLI open-ended research, not the native Gemini Deep Research product. Four supplementary dispatch attempts automatically selected Agy's Claude model group; active attempts were stopped when detected, and the affected checks were rerun with Gemini explicitly pinned. The main discovery and verification batches used Gemini. Failed/interrupted attempts and their replacements are retained in the run ledger.

Reproducible records: [final candidate decisions](news-search-2026-10-02/candidates.jsonl), [query log](news-search-2026-10-02/queries.jsonl), [run manifest](news-search-2026-10-02/manifest.json), [citation handoff](news-search-2026-10-02/citation-handoff.jsonl), and [full inventory matrix](../news-coverage-matrix.csv). Short evidence descriptions, source locators, raw-file hashes and original worker decisions are retained. Downloaded source files remain in the local run cache rather than being republished.

### Propagated to Site

The impact cards in `opensource.html` now include Bundesbank, Caltech/NASA JPL, Swedish FOI, Ai2, Newsweek, European Parliament, international AI safety, and independent agent-auditing evidence. At the author's request, these findings appear on the impact page without a homepage news entry. The Ai2 description specifies the 400-prompt JailbreakTrigger subset; Newsweek remains labeled as opinion. Patent counts agree at 97 across the impact page, biography, generated homepage biography, and `llms.txt`. Both CV sources and the homepage link the Amazon award to the named recipient page.

## 2026-09-22 Pass (Phase A: 37 Agy lanes via `/prun`; Phase B: 16 Agy verification units over 378 candidates, plus 2 dedicated surface-audit units; coordinator-side patent family check and ledger recount)

One net-new Tier 0 document, Ledger 1 row 21, which is a NICT presentation submitted to a Japan
MIC committee rather than an independent adoption. The round's most consequential output is not a
promotion. For four rounds the
Summary Statistics table has been wrong, and the per-ledger count lines it copied had stopped tracking
their own tables. That is written up under "The Published Total Was Never Reproducible"
below. The largest verified addition is the patent figure, which moves from 49 to **94** on a basis
that is now stated and checkable.

### What the Round Ran

Phase A dispatched 37 Agy lanes and all 37 returned, with zero FALLBACK records. They produced 1,014
records over 956 unique URLs, of which 779 were absent from the identity index. Phase B verified
every candidate it was given: 16 units over **378 candidates**, no deferrals. Two further units
audited surfaces rather than candidates, one over the 94 patent publication numbers and one over the
9 award links on the site and in the CV.

The 378 verdicts split as follows.

| Verdict | Count |
|---|---|
| `candidate-promote` | 243 |
| `already_counted` (reached by a new URL) | 77 |
| `dropped` | 27 |
| `verified-negative` | 15 |
| `paywall_or_blocked` | 12 |
| `topic-validation` | 4 |
| **Total** | **378** |

Of the 243 promotions, one was refuted on re-fetch and two were the same document reached twice, so
**240 promotions** were placed. They land as Ledger 1 +1, Ledger 2 +14, Ledger 3 +117 items across 83
rows, Ledger 6 +3, Ledger 7 +30, and 75 records handed to `/citation-audit`. Those six figures sum to
240, which is the check that no promotion was placed twice or lost.

### The Published Total Was Never Reproducible

The Summary Statistics table published **582** as "the sum of the eight ledgers above". Those eight
figures sum to 364. No arithmetic connects the two, and none of the rounds that
quoted 582 checked it against the rows it claimed to summarize.

The second fault is larger and explains the first. Each per-ledger count line had stopped tracking its
own table:

| Ledger | Published count | Rows the table actually held |
|---|---|---|
| Ledger 2 | 80 | 108 |
| Ledger 3 | 170 | 331 |
| Ledger 6 | 11 | 34 |
| Ledger 7 | 15 | 48 |

Rounds were appending rows and writing the promotion into the pass section without updating the count
line under the table. The Summary then copied the stale count lines rather than counting the tables.
Both figures are now taken from the live tables: **731 rows carrying 771 counted items**. Each count
line carries the same number as the table above it, and the Summary states, per ledger, the rule that
separates rows from items.

The recount is not growth. This round's verification added 165 items, and one more is a 2026-09-12
promotion whose row is written here for the first time. The pre-round tables held 605 items against a
published 582, so 23 items were on the tables and outside the total before this round began.

Two smaller placement faults surfaced in Ledger 1b during the recount. The first is recorded rather
than fixed: the table's basis is DOE national-laboratory reports with substantive use, and rows G9
through G12, appended on 2026-08-13, fall outside it. Two of them (arxiv.org, pubs.rsc.org) are not
government documents at all. They stay uncounted until a round re-places them. The second is fixed.
On 2026-09-12 a pass promoted SLAC OSTI 3005876, MetaOD's first appearance in a government document,
and never wrote its row. It is now row G13, with the OSTI record and DOI re-fetched on 2026-09-22.

### Patents: 49 to 94, With the Basis Stated

The site published 49. Ledger 3 of this audit carried 89 rows with a patent publication number,
which is the figure the 49 should have tracked. This round added 13 more, giving 102 rows.

Eight of those 102 rows are a second or third publication of an invention another row already holds.
Four are CN applications published twice, as A and B kind codes: rows 159/234, 160/237, 164/247 and
165/250. Rows 176 and 269 are the two SK utility-model publications of one filing. Two more are family
members of row 66m's EP4662606A1, the KR row 175 and the CN row 266. The eighth, row 274, is the WO
publication of row 66cl's US20230017157A1. Subtracting those eight leaves **94 distinct inventions**.

All 13 additions were family-checked against the existing rows before being counted, by reading each
one's Google Patents sibling list and intersecting it with the numbers already on file. Zero were
family duplicates. The sibling lists ran from 12 to 36 publications each: CN113761292B (31),
CN115293481A (36), CN115567572B (34), CN116167004A (18), CN116633666A (30), CN117113250B (14),
CN117453502A (25), CN118606861A (27), CN118798628A (12), CN119937461A (25), CN120671044A (15),
CN121814397A (25) and EP4451150A1 (33). Two of the 13 timed out on the first attempt and resolved on
retry, which is the tool-reliability rule doing its job.

One caveat keeps the arithmetic honest. Two rows name more than one number for a single invention.
Row 66cn names US12074893B2 with US11711391B2 and WO2022082091A1 as siblings, and row 346 names
both the A and B publications of CN115293481. That is why the count of distinct publication numbers,
105, is higher than the invention count of 94. The basis published
on every surface is inventions, not publication numbers.

The jurisdiction split over the 94 is China 70, US 14, WIPO 3, EPO 3, Germany 1, Japan 1, Korea 1,
Slovakia 1. Note that the previous split labelled the EPO entries "EU", which is wrong: EP
publications come from the European Patent Office, whose membership is not the European Union.

### The Tier Rule Was Rewritten and Then Reverted the Same Day

`SKILL.md` said a Phase A tier is a ceiling, on evidence of 110 down and zero up over 420 candidates.
This round rewrote it to say a tier is a ceiling on a calibrated surface and a floor on a new one. The
evidence offered was 110 down and 20 up over 378 candidates, with 14 of the 20 from the thesis unit.

Two reviewers challenged the rewrite as too thin to justify on one round over one new surface. A
recount found something worse than thin evidence. The verdict records cannot produce
the claim at all: `tier_was` was written on 70 of 481 records, and only 56 carry both `tier_was` and
a final tier. A movement count over 378 candidates was never available. The rule is reverted, the
reason is recorded next to it, and `tier_was` is now a required field in the verdict schema rather
than an optional one.

This is the round's method result, and it generalizes past this rule. A calibration claim needs the
field that measures it to be mandatory at capture time, because nothing downstream can reconstruct a
tier that was never written down.

### Award Links: Five Replaced, One Unlinked

A dedicated unit fetched all 9 award links on the site and in the CV. Two name the PI and are
unchanged (Meta AI4AI and the Google Cloud research innovators directory). One is dead: Gen Digital
retired the whole Norton Labs news tree. The other six are live and name nobody, which makes them
decoration rather than evidence. Capital One accounts for two of the six, because `index.html` and
the CV linked the same award to two different pages and neither names a recipient. Each replacement
below was fetched and confirmed to name the PI in the award's own context.

| Award | Replacement | What the page says |
|---|---|---|
| AAAI New Faculty Highlights | `aaai.org/aaai-24-conference/nfh-24-program/` | The program lists "Towards Reproducible, Automated, and Scalable Anomaly Detection / Yue Zhao". Before, the link pointed at the call for proposals, which names nobody. |
| ACM SIGSPATIAL | `sigspatial.org/people/award-recipients/` | The recipients index names "Yue Zhao, University of Southern California" for TyphoFormer. Before, the link pointed at the 2025 conference home page. |
| Capital One | `capitalone.com/tech/ai/credif-spring-2025-ai-award-fellowship-recipients/` | Capital One's own recipients announcement. It replaces both previous links: the USC Viterbi article in the CV, which announces the creation of the center, and the CREDIF page in `index.html`. Neither named a recipient. |
| Foresight Institute | `foresight.org/grantees/2026-yue-zhao/` | A grantee page for the PI. The previous link now 301s to a live call for proposals. |
| NortonLifeLock | Wayback capture `20240414184544` of the 2022 fellowship winners page | The live page is dead with no successor anywhere on the Gen Digital site; the capture names the winners. |

The NVIDIA Academic Grant Program link is **unlinked rather than replaced**. The fetch found no
recipient list for the program and no public page naming this award and this recipient together. Pointing at the program description asserted evidence that does not
exist. The award text remains; only the link is gone. Both reviewers reached
this conclusion independently and both were right.

One disagreement is left for the user rather than resolved here. The CV dates the Capital One award
October 2024, while the replacement link is a spring 2025 recipients announcement. Either the date or
the link is wrong, and the audit cannot tell which from the outside.

### Handoffs and What This Round Did Not Do

The 75 records routed to `/citation-audit` are a tracked manifest at
`skills/news-search/handoffs/2026-09-22-citation-audit.jsonl`, one JSON object per record. Each
carries the cited work, the citing source, the resolved URL, the evidence quote, the citation
location, the bibliography format and a self-citation verdict. Importing them needs no new OpenAlex
pass, because every record was already fetched and read. Each self-citation verdict is read from the
verifier's notes and never inferred. Thirty-two are independent, and 3 pass the literal screen with a
proximity caveat. One is flagged as advisor-adjacent, and one is excluded because the PI's frequent
co-authors sit on the citing byline. For the remaining 38 the verifier recorded no screen, and those
need one before any of them is counted anywhere.

One record in that manifest is worth naming. *AI and Ethics* (Springer, 2026, single author Alex
Chengyu Li) cites Auditable Agents, the first peer-reviewed journal citation of the paper found so
far. It is not a Ledger 6 row, because Ledger 6 admits a citation only with body discussion or a
named-mechanism reference. This one is a reference-list entry in an article whose body is paywalled,
so the depth of engagement is unknown. An earlier draft of this round had placed it in Ledger 6.
Each of the three rows there instead, A35 to A37, quotes body text. A35 is a prior-art summary of
Auditable Agents (arXiv:2609.12582). A36 describes MemoHarness's mechanism in an NVIDIA, NTU and MIT
paper (arXiv:2609.20519). A37 is SteerBench-Work calling The Autonomy Tax "the closest prior
observation" to its own finding.

Ledger 3's 117 new items are carried on 83 rows, not 117. Six cluster rows hold 40 items between
them, covering the aggregator, tutorial, community, video, blog and platform classes, following the
folding convention used on 2026-06-02. Each cluster row carries one link per item, so every counted
item keeps its own address in the tracked file. Writing 117 separate narrative rows for
forum comments and marketplace listings would have grown the table by a third to carry the least
consequential evidence in it.

Three patent candidates stay uncounted, as they have since at least 2026-06-14, and the 94 does
not include them. They are CN112989338B (Tencent, COPOD at ¶0133 and ¶0165), CN117216660B
(DBAPPSecurity, TODS paraphrased as prior art at ¶0003) and CN117648656A (Chongqing University,
ADBench at ¶0125). Each needs the same two steps before it can count. Fetch the Google Patents page
and confirm the tool at the cited paragraph from the page text itself. Then intersect its sibling
list with the 105 publication numbers already on file. A row and a count change belong in the same
commit as that check.

Two mismatches between a table's rule and its practice surfaced, and both are left for the user.
Ledger 7 is titled peer-reviewed and its inclusion rule says so, yet it has admitted arXiv preprints
with substantive use since row S16. This round's S70, S77 and S78 follow that practice. Separately,
Ledger 2 rows 50 through 63, written on 2026-09-12, carry five cells under an eight-column header,
so they render misaligned. Neither is fixed here, because each needs a decision about the table
rather than about a row.

Three claims that an earlier draft of this section made are withdrawn, because the round cannot
support them. One is a tier-movement measurement over 378 candidates, for the reason given above.
Another is a count of coverage across five discovery dimensions, which nobody computed from the lane
outputs. The last is a reading of what OpenAlex returned. It rests on the empty outgoing-reference
metadata that the 2026-09-12 pass already recorded as a limit on what a retrieval failure there can
mean.

### Propagated to Site

| Surface | Change |
|---|---|
| `opensource.html` | Patent row 49 to 94, with the jurisdiction split and the "distinct inventions" basis. |
| `files/bio.txt` | "cited in 49 patents" to 94. |
| `llms.txt` | Patents bullet to 94 with the corrected split. |
| `index.html` | Bio prerender to 94; NVIDIA award unlinked; four award links replaced. |
| `cv/cv-full.tex`, `cv/cv-1page.tex` | Award links replaced; NVIDIA award unlinked. |
| `scripts/ci_check_site.py` | `index.html` added to the patent-count claim map. It carries the same bio sentence as `files/bio.txt` and was the one surface the gate did not watch. |

---

## 2026-09-12 Pass (general round: 32 Agy lanes via `/prun` + 9 Claude agents via `/workflows`; auditing-line round: 12 Agy lanes + 13 Claude agents; Phase B: 16 Agy lanes over 420 candidates; Phase C: 6 Agy lanes over everything still blocked)

**Method, and what changed.** This is the first round where Codex ran no discovery lanes. The
`news-search` dispatcher now sends lanes to Agy (Gemini 3.8 Flash High through the Antigravity CLI)
by default, with Codex reachable behind `--backend codex` and reserved for `/vet`. Two commits
carry the migration, `8a25c01` and `6a57501`, and both passed a dual review. The second review
round found a defect worth recording here because it would have falsified this entire pass: the
completeness test in `result_complete()` matched only Codex's FALLBACK header literal, so every
failed Agy lane would have graded as complete. The generalized regex was copied from
`anywhere-agents` 754833a.

Verification was handled differently from the 2026-08-30 pass. That round ran a broad adversarial
re-fetch of every high-tier claim. This round ran a narrower one: 9 agents over the three impact
metrics that feed the site and the five highest-value new claims. The narrow shape was the right
call for the metrics and the wrong call for the ledger check, for the reason in "Four Claims
Reported as New Were Already Counted" below.

**Scale.** 32 of 32 lanes returned a complete result, zero FALLBACK. 660 records over 616 unique
URLs. Verification spent 884,376 subagent tokens across 170 tool uses in 15.8 minutes.

| Class | Count |
|---|---|
| Coverage candidates | 497 |
| Verified negatives | 36 |
| Topic-validation and dropped | 122 |
| Gated, held for manual check | 5 |

Coverage candidates resolve to 454 unique URLs. 150 were already in the 1,929-URL index and 304
were not. New URLs by tier: T0 2, T1 11, T2 91, T3 130, T4 4, T5 66.

**A new URL is not a new row.** Of the 13 highest-value candidates put through verification, 4
became ledger rows, 4 were already-counted items reached by a different URL, 1 was refuted outright,
and 4 remain pending. The 2026-08-30 pass recorded 135 MIRROR verdicts and concluded that URL-level
dedup is not sufficient; this round demonstrated the same thing at a 4-in-9 rate on the items chosen
for their value.

### Tier 0: Confirmed New (Ledger 1, +1)

**The Allen Institute for AI uses TrustLLM's JailbreakTrigger set in its own safety evaluation
tooling.** Three artifacts agree: Ai2 hosts the set as the Hugging Face dataset
`allenai/tulu-3-trustllm-jailbreaktrigger-eval`, ships it as a task in `allenai/safety-eval`, and
reports Tülu 3 scores on it in the Tülu 3 technical report (arXiv:2411.15124). Ai2 was absent from
every ledger before this round.

Two corrections to the lane's claim, both of which change published wording. The report section is
**7.2.1**, with Tables 25 and 26, rather than the 5.2 / 5.3 the lane recorded; Section 5 covers
preference finetuning and mentions TrustLLM in neither v1 nor v5. The scope is **one 400-prompt
dataset from TrustLLM's safety dimension, rescored with Ai2's own WildGuard classifier**, rather
than TrustLLM entire, which spans six dimensions and more than 30 datasets. State the narrow scope;
it is still the strongest adoption signal in the round, because a frontier lab shipped the set as
infrastructure rather than citing the paper.

One open item: footnote 20 of the report says the reported runs used a personal fork,
`github.com/nouhadziri/safety-eval-fork`. The task is independently present in the `allenai` main
repo, so the adoption claim stands, but the origin of the published scores is unresolved.

### Ledger 1b: Government Technical Reports (+1)

**SLAC OSTI 3005876 cites MetaOD.** "Coincident learning for beam-based rf station fault
identification using phase information at the SLAC linac coherent light source", Physical Review
Accelerators and Beams 28, 124601, December 2025, DOE contract DE-AC02-76SF00515. Reference 26 is
MetaOD (Zhao, Rossi, Akoglu; arXiv:2009.10606), used as one of three thresholders benchmarked for
radio-frequency station fault detection.

This is a different document from the SLAC row already in this table (G3, OSTI 2426670, which cites
PyOD in its body at page 25). Same laboratory, same research programme, separate paper. To this
table's knowledge it is **MetaOD's first appearance in a government document**; Ledger 7 row S30
reaches MetaOD only through another group's paper.

The lane claimed the paper cites "MetaOD/PyOD". A full-text search of the 18-page PDF returns zero
hits for `pyod`. PyThresh is named in prose but carries no reference entry, so it cannot be counted
either. The row is MetaOD alone. Whether PyThresh's META thresholder implements the MetaOD algorithm
was not checked, and the linkage is reported as the SLAC authors' attribution.

### Ledger 2: External Third-Party Media (+1)

**CrowdStrike evaluated COPOD in a command-line malware detection ensemble.** "BERT Embeddings: A
Modern Machine-learning Approach for Detecting Malware from Command Lines", CrowdStrike blog,
January 2022. The post hyperlinks the COPOD paper directly, treats it as a parameter-free detector
inside a four-model ensemble, and names PyOD as the library used. CrowdStrike previously appeared in
this audit only as an unchecked entry in a D8 outlet list, never as a counted row.

### Ledger 3: Ecosystem Adoption (+1)

**Databricks DAXS trains 10,000 ECOD models over roughly 1.4 billion sensor records.** This is a
third Databricks row, separate from row 42 (Kakapo) and row 43 (insider threat risk detection). The
solution accelerator is for industrial predictive maintenance, and the scale figures are the post's
own.

**The attribution must sit on the repository, not the post.** PyOD appears zero times in 716 KB of
page HTML. The post carries no reference list, no arXiv link, and no DOI, so it cites neither the
ECOD paper nor any author. PyOD is pinned in the linked DAXS repository's `requirements.txt` as
`pyod==2.1.0`. A row that credits the post with naming ECOD would not survive a reader checking it.

### Four Claims Reported as New Were Already Counted

Each of these is a new URL against the 1,929-entry index and an already-counted item in the ledger.
All four were surfaced, verified as genuine, and reported to the user as new coverage before the
ledger check caught them.

| Claim | Already at |
|---|---|
| Talk Python To Me #497, Outlier Detection with Python | Ledger 3 row 40 |
| The Real Python Podcast #208, Detecting Outliers | Ledger 3 row 41 |
| Amazon Science, "10 Amazon Research Awards recipients announced" | Ledger 5 rows 72 and 73 |
| "Reason Less, Verify More", citing AEGIS as reference 12 | Ledger 6 row A2 (arXiv:2607.07405) |

The fourth is the instructive one. The lane surfaced the paper as a PDF hosted on the KDD 2026
Workshop on Evaluation and Trustworthiness of Agentic AI site, and the ledger holds it under its
arXiv ID. Same paper, two surfaces, and the workshop copy reads as a new citation of AEGIS until the
arXiv ID is recovered from it. It is an evidence upgrade to A2: the paper was **accepted at a KDD
2026 workshop**, which is non-archival. Authors are an independent researcher, IIT Kharagpur, and
MIT. AEGIS is cited as established prior work, never run as an experimental baseline.

Real Python #208 also needs its existing row read down rather than up. PyOD is one of eleven tool
links in the show notes, absent from the episode description, and no transcript is published.

**The fix**: a verification pass that checks a candidate against the source but not against the
ledger cannot distinguish new coverage from a new URL. The ledger check has to run first, on every
candidate, before verification budget is spent. It is cheap, it is local, and this round ran it
last.

### The Chemistry World Row Does Not Exist as Recorded

A lane recorded "Benchmark flaws may be distorting AI drug-discovery leaderboards" (Chemistry World,
Royal Society of Chemistry) as a Tier 1 industry-engineering hit that evaluates 22 benchmark
configurations from Therapeutics Data Commons.

The article audits **51** configurations across four sources: 7 Polaris, 22 TDC, 9 MoleculeNet, 13
DTI. **Yue Zhao is not named anywhere in it.** The only adjacent name is Yang Zhang of NUS, a
different researcher quoted as an outside commentator, which is what gave the row a plausible shape.
The article's stance is critical of the datasets themselves, TDC included, quoting "problems in most
datasets, notably train-test leakage and contradictory labels assigned to identical molecules". Its
"more than 10,000 citations" line is the aggregate for all four resources.

Recorded as a verified negative. Critical science journalism about a co-authored dataset is worth
knowing about, and it is not coverage under the citation rule, and it must never be framed as
endorsement.

### Two Site Numbers Were Wrong, Both Sums Presented as Totals

This is the most useful thing the round produced, and neither lane had it right.

**Downloads.** The publishable figure is **59,377,536 lifetime PyPI downloads** (pepy.tech,
2026-09-12), running about 3.6 million per month (pypistats.org, known mirrors excluded). Attribute
one source per number and never blend them: the two monthly figures differ by about 5.8%, their
filtering and coverage differ, and the contribution of CI traffic has not been measured. pypistats
documents mirror exclusion; it does not document CI exclusion, so the gap should not be attributed
to a single cause.

A lane recorded "over 21.7 million cumulative downloads without mirrors" from pypistats. That is the
sum of the 180-day window pypistats retains, 2026-03-17 to 2026-09-12, 180 daily points totalling
21,669,826. **pypistats publishes no cumulative field for any package and cannot**, because it
discards data older than 180 days. The site's own `55M+` was true and trailing the source by about
4.4 million. The two figures never conflicted: 21.7M over six months is 37% of the 59.4M lifetime,
which is the shape of a steep adoption curve.

Eight site locations carry the stale string: `index.html:287`, `opensource.html:335`,
`pyod.html:14` (og:description), `pyod.html:133`, `data/open-source.json:25`, `llms.txt:56`,
`cv/open-source.tex:11`, `cv/cv-1page.tex:123`.

A second-order break came with it. `index.html:484` and `files/bio.txt:2` say the projects "together
exceed 60 million downloads and 30,000 GitHub stars". With PyOD alone at 59.4M, that aggregate
collapses onto the single-project figure and reads as though the other projects contribute nothing.
It needs re-deriving from the individual totals. The same two lines say "As of August 2026, 5,560
public repositories and 159 packages depend on PyOD", now 5,567 and 160.

**Dependent repositories.** The publishable figure is **more than 5,500 public GitHub repositories**
(GitHub dependency graph, September 2026, count approximate), for PyOD alone.

One lane credited "the GitHub dependents graph and deps.dev" for 5,567 repositories and 160
packages, implying two sources in agreement. deps.dev reports neither. It returns
`{"dependentCount":100,"directDependentCount":63,"indirectDependentCount":38}` for pyod 3.6.5,
counts registry packages rather than repositories, and is scoped to a single version. Drop deps.dev
from that sentence.

The other lane's Libraries.io counter cannot serve as a counterweight, because it is broken data.
`libraries.io/pypi/pyod/dependent-repositories` is headed "73 repositories depend on pyod" and
renders exactly one row: `Granze/applause`, an AngularJS CSS presentation template last pushed
August 2015, three years before PyOD's first release in May 2018. Pagination is inert, with
`?page=1` and `?page=2` returning byte-identical 14,344-byte documents. Libraries.io's PyPI release
metadata is current (116 releases, 3.6.5 dated 2026-08-17), so the staleness is confined to its
repository crawl. Do not present 73 as a conservative lower bound and do not bracket it against
5,567.

Never describe this population as production deployments or as organizations. The first page of the
listing includes 0-star and 1-star entries. It counts repositories whose dependency manifest names
PyOD, which takes in coursework, forks, and abandoned scratch repos, and it misses private and
enterprise use entirely.

**The ecosystem sum must not be published.** A lane reported "6,906 dependent repositories and 193
package dependents" across ten repositories. The arithmetic is exact and all ten per-repo inputs
reproduce on the live pages, including all five claimed zeros. The construction is the problem: the
sibling libraries sit inside each other's dependency closure, since SUOD's `requirements.txt` lists
both `combo` and `pyod>=1.0` and combo's lists `pyod`. Measured overlap against the pyod dependent
list was 183 of 211 sampled combo dependents (87%) and 120 of 136 sampled SUOD dependents (88%),
and 9 of the 28 combo dependents absent from the pyod sample declare pyod anyway. The overstatement
is roughly 1,150 to 1,200 repositories, about 17%, and because the overlap rates are floors the true
overstatement is larger. The sum also counts `yzhao062/pyod` itself and six of its forks as
third-party reach. The four siblings contribute on the order of 170 distinct repositories, inside
the drift of a figure GitHub recomputes without notice.

**GitHub's header counts cannot be walked to confirmation by anyone, including the repository
owner.** `pytod` shows 14 and enumerates 10 rows; `pygod` shows 51 and enumerates 31; combo's
pagination died at 211 of 712 and pyod's at 2,432 of 5,567 with zero-row error pages. Two verifiers
disagreed on what this means and the disagreement is left standing: one called 5,567 reproducible on
the basis of two fetches returning identical numbers, the other tried to reproduce the count and
could not. The second is right about the epistemics. Both reached the same recommended wording, so
the published sentence is unaffected, and the number should never be defended as measured.

**Unresolved.** A lifetime download total excluding CI traffic and mirrors does not exist from any
free source: pepy states "Includes CI traffic" and puts the exclusion behind a paid tier, and
pypistats retains 180 days. For scale, the mirror component alone is 0.2% of the 180-day window,
21,714,571 with mirrors against 21,669,826 without. CI traffic is a separate, unmeasured category.

### The Agent-Auditability Line

**Seven standards tracks and seven specification documents were fetched in full, and not one cites
this line.** Recorded as verified negatives with the document read in each case, so the next round
does not repeat the work.

The nearest miss is worth stating precisely. **AAS-1, the Agent Auditability Standard** (`aas-1.org`,
v0.1, May 2026, CC0, published by BDA AI Agent Services / Kadikoy Limited via
`github.com/Kadikoy1/aas-1`) defines five record classes and twelve assertions, and treats agent
auditability as a first-class assurance property. That is the Auditable Agents framing
(arXiv:2604.05485) arriving independently in a standard. It does not cite the paper. Its v0.2
roadmap is open.

Also checked and negative: IETF `draft-sharif-agent-audit-trail-03`, standards-track work on agent
audit logging by R. Sharif of CyberSecAI, independent; CEN-CENELEC JTC 21 prEN 18229-1, which
addresses EU AI Act Article 12 logging directly and closed its public enquiry on 2026-08-20 at stage
40.60, plus prEN ISO/IEC 24970; ISO/IEC FDIS 24970 at stage 50.20, the international base standard
under it, and ISO/IEC 42006:2025 for AI management system auditing bodies; NIST NCCoE "Software and
AI Agent Identity and Authorization", concept paper 2026-02-05, comment closed 2026-04-02; NIST
CAISI's AI Agent Standards Initiative, announced February 2026, RFI closed 2026-03-09; OWASP's Top
10 for Agentic Applications 2026, Agent Observability Standard, Agentic Skills Top 10, and AISVS,
all grepped as full repositories; Cloud Security Alliance AI Controls Matrix v1.1; IEEE P3119.

One partial trace exists. An OWASP AISVS research sync (commit ac19fe0, PR #1148) mentions Aegis for
prompt-injection detection in a chapter research note. That research content was removed during the
1.0 consolidation, and the same note sits alongside Forrester's unrelated AEGIS and an AI-code tool
of the same name, so it does not support a row.

**One submission window is open.** The UK AI Safety Institute's Inspect Evals Register has accepted
submissions through a GitHub issue template (`register-submission.yml`) since 2026-05-08 and is
standing rather than a closed call. Every AISI grant programme (Challenge Fund, Systemic AI Safety
Grants, Alignment Fund) is closed to new applications.

**The vocabulary is in the hiring market and the name is not.** A careers lane read 3,099 active
requisitions across OpenAI, Anthropic, Databricks, xAI, Scale AI, Mistral, and Cohere, plus
enterprise portals, and returned eight verbatim matches on this line's subject matter sitting in
Responsibilities or Qualifications sections: Anthropic on deploying "automated safeguard evaluations
and behavioral" monitoring, OpenAI on "automated monitoring, anomaly detection", Databricks on
detection of prompt injection at production scale, plus xAI, Scale AI, NVIDIA, Capital One, and
Pfizer. Every one is topic-validation. None names a work, a person, or the lab.

**CatchBench has no external non-academic footprint.** Thirty-three targeted queries returned
nothing. The paper is arXiv:2608.22808, released August 2026 with 9 stars at the time of the sweep.
Recorded as an honest zero-footprint baseline rather than omitted. `yzhao062/catchbench`,
`yzhao062/grade`, `yzhao062/auditable`, `yzhao062/MetaOD`, and `yzhao062/awesome-auditable-ai` each
showed zero dependents.

### The Auditing-Line Round: Ledger 6, +6 Net New (7 Verified, 1 Already Recorded)

The general round covers this line only incidentally, so a dedicated round ran after it closed: 12
Agy lanes through `/prun` over the full 14-work inventory, then 13 Claude agents through
`/workflows` sweeping by three methods the lanes do not use (citation-graph triangulation across
eight indexes, reverse search from 44 neighbouring systems, and full-text plus code search). 12 of
12 lanes complete, zero FALLBACK, 504 records. The workflow spent 1,776,135 subagent tokens across
474 tool uses.

**The two halves found almost disjoint sets.** Of the workflow's seven confirmed citers and the
lanes' nine comparison finds, exactly one work appears in both. The methods surfaced different
candidates. Verifying the eight lane-only leads will determine whether they add citations beyond the
seven confirmed works; they stay outside the confirmed and net-new counts until then.

Seven citing works, each fetched, each with authors independent of the lab, all four verification
checks passing (the work exists at the identifier, its reference list carries the entry, the quoted
sentence is really in it, and the authors are not co-authors). They cover five of the fourteen works.

| Citing work | Identifier | Cites | How |
|---|---|---|---|
| Cloak and Detonate: Scanner Evasion and Dynamic Detection of Agent Skill Malware (HKUST) | arXiv:2607.02357v2 | Agent Audit | Reference [26]; 80.5% strict bypass under Structural Obfuscation (Figure 4). Table III separately reports alert-count reductions, 83.3% under Structural Obfuscation and 99.9% under SFS Packing. Bypassed skills and suppressed alerts have different denominators and must not be quoted as one range. |
| STARS: Skill-Triggered Audit for Request-Conditioned Invocation Safety (KAUST/PRADA, Shenzhen U, U Georgia) | arXiv:2604.10286 | Agent Audit | Numbers: the 0.380 AUPRC in its own abstract is the Agent Audit row, against its 0.439 |
| Task-Conditioned Least-Privilege Learning for Executable Terminal and MCP Agents (Purdue Northwest, Columbia) | arXiv:2608.18351 | FORTIS | Reference [6]; Tables IV and V over 600 Task 1 and 1,543 Task 2 items, plus a prior-art paragraph |
| Natural-Language Workflows Are Not Software Yet (Artic; Purdue) | arXiv:2608.21341 | CHI-Bench | Reference [36]; Figures 9 and 11 and Appendix Table VI measured entirely inside CHI-Bench's medical domain |
| HANSARD: A Reference Architecture for Forensic Readiness, Runtime Witnessing, and Graded Attribution (Harokopio, DUTH, U Western Macedonia) | arXiv:2608.22512 | Auditable Agents | PDF prints [5], HTML labels [20]; cited in three sections |
| Audita: certified auditing and causal attribution of adverse outcomes (Duke) | arXiv:2608.22160v2 | Auditable Agents | PDF prints [17] on page 16; `bib.bib76` is the HTML element id, not a printed number |
| Towards Long-Horizon Agents: A Survey (RUC, PKU, Tsinghua, SYSU, HKUST, NUS; 149 pages, 906 references) | OpenReview HyhfhlbWGh, DOI 10.20944/preprints202607.1328.v1 | AEGIS | Reference 783, and AEGIS names one of the survey's three boundary categories |

**The standing note that Praetor was the only baseline precedent no longer holds.** Six net-new
verified citers, plus the unverified lane set below, stand against the one that note recorded. The two
sets union to fifteen distinct candidates; do not report that as fifteen new confirmed citations. One
of the seven verified rows was already recorded on 2026-08-30, eight of the fifteen are unverified,
and at least one of those eight sits in a project that pass already counts.

**One of the seven is a reverification, not a discovery, so this round adds six.** The
2026-08-30 pass already recorded arXiv:2608.18351 and already falsified the FORTIS zero with it
(see that pass's "A standing negative was falsified"). This round fetched the paper again and
confirmed the reference number and both results tables, which is worth having, and it is not new
coverage. Net new external citers this round: **six**. The suppression list given to the lanes
covered Ledger 6 rows A1 to A20 and the known-URL index, and it did not cover the prose of the
preceding pass, which is how the duplicate reached a table.

The same gap affects the unverified set below: the 2026-08-30 pass already records HELM AI Kernel
merging AEGIS evidence-integrity proof tests and RedStamp merging a live AEGIS adapter, so the
Mindburn Labs `helm-ai-kernel` comparison document sits in a project this audit already counts.

**Two of the seven cite a repository URL rather than a paper, and neither names the author.** STARS
lists the entry as software, titled "Agent audit: static security analysis for ai agent
applications", tagged "Zhang (2026)", linking only `github.com/HeadyZhang/agent-audit`. Cloak and
Detonate writes "Headyzhang [26] adds tool-boundary AST taint tracking". Across both papers the
strings `2603.22853`, `Yue Zhao`, `USC` and `FORTIS` occur zero times, so a DOI-keyed or
identifier-keyed tracker registers neither.

Four of the seven report numbers, not two. The two Agent Audit citers benchmark the scanner itself;
the FORTIS citer reports results in Tables IV and V, and the CHI-Bench citer reports measured
evaluations in Figures 9 and 11 and Appendix Table VI.

**Name visibility across all seven is low.** "Yue Zhao" is spelled out in two of the seven citing
documents: reference 783 of the Long-Horizon survey, and reference [17] of the Audita PDF. FORTIS
appears as "S. Li et al."; CHI-Bench as "H. Chen ... H. Capps et al.", with Yue Zhao author 25 of
33. The two Agent Audit entries name only a GitHub handle.

**One taxonomy rule is missing and it affects three of these seven rows.** Two verifiers assigned
different strengths to the Purdue Northwest paper because the rules do not say where "ran the cited
benchmark and published its numbers" belongs. Both agree FORTIS is the measuring instrument rather
than a rival system: the baseline column in every table is the untrained Qwen3.5-4B policy. One
called that a component citation, the other upheld baseline-with-numbers. Settle it before the next
round's counts are compared with this one's.

### The Eight Comparison Finds All Hold, and Four Sat at a URL the Lane Invented

Phase B fetched all eight. Every one of the eight documents exists and cites the work. Four of the
eight URLs the lanes reported do not exist, and in each of those four the real document sits under a
different owner, which Phase B found only because the same lane had also emitted the correct URL as a
separate candidate.

| Comparison find | URL as reported | Real document | Verdict |
|---|---|---|---|
| PolicyFaultBench evaluating AEGIS in a comparative matrix | `researchsquare.com/article/rs-10502893` | same | **Confirmed.** Section 2, Table 1 taxonomy, reference 20. Authors Hasan Fadhil Qasim and Sarah Abdulzahra Kadim, University of Misan, Iraq. The lane's "Palumbo et al." attribution is wrong. |
| Mindburn Labs `helm-ai-kernel` benchmarking against AEGIS | `docs/AEGIS_COMPARISON.md` | `Mindburn-Labs/helm-ai-kernel` pull request #297 | **Confirmed.** Reports about 6.2 us allow and 5.7 us deny per call against AEGIS's published 8.3 ms. |
| ControlPlane comparing its HMAC receipts against AEGIS's hash chain | `docs/related-work.md`, owner unnamed | `hariom-s27/controlplane/docs/related-work.md` | **Confirmed.** A dedicated AEGIS subsection, plus Auditable Agents compared across five dimensions in the same table. |
| AgentShield against Agent Audit | `AgentShield-Security/AgentShield/docs/benchmark.md` | `affaan-m/agentshield/docs/BENCHMARK.md` | **404 as reported, confirmed at the real path.** Names only the repository URL and the handle, with no identifier and no author. |
| HandoffGraph against GRADE | `HandoffGraph/handoffgraph/docs/competitors.md` | `arbazkhan971/handoffgraph/docs/competitor-analysis.md` | **404 as reported, confirmed at the real path.** Cites arXiv:2606.22741 and `yzhao062/grade` as the prior art establishing the OBSERVED / DECLARED / INFERRED provenance taxonomy. |
| OneLive AI adopting MemoHarness's D1 to D6 taxonomy | `onelive-ai/onelive-engine/docs/strategy/memoharness-review.md` | `schubertsean-ui/onelive` pull request #35 | **404 as reported, confirmed at the real path.** Adopts the D1 to D6 defect taxonomy and the test-time retrieval constraints. |
| MCP Data Platform using No Attacker Needed as a baseline | `mcp-data/platform/issues/142` | `txn2/mcp-data-platform` issue #1163 | **404 as reported, confirmed at the real path.** Cites arXiv:2604.01350 as the primary literature baseline for organic contamination in shared agent stores. |
| Secure Agentic Framework registering AEGIS as `SRC-aegis-2603.12621` | `secure-agentic-framework/saf-mcp/techniques/SAF-T1103/README.md` | same | **Confirmed.** References item 16, line 240, under technique SAF-T1103 (Fake Tool Invocation). |

**The failure mode is specific, and it is not a search failure.** In all four cases the lane had the
project, the document type, the mechanism and the comparison right, then synthesized the organisation
name, the file path or the issue number. An invented `AgentShield-Security` organisation is exactly
what a plausible owner for a project called AgentShield would be named, and issue #142 is exactly the
kind of number an issue in an active repository carries. Nothing about the fabricated rows reads as
wrong, which is why four of them were written into this document as findings. One signal was
available: the lane emitted both URLs, so the worklist carried a near-duplicate pair whose owners
disagreed. Test for that before spending verification budget rather than after.

**The class does now have ledger representation, and it splits two ways.** PolicyFaultBench is an
academic preprint and takes a Ledger 6 row. The other seven are industry-side, either
security-framework specifications or companies benchmarking against the work inside their own
repositories, which is a different signal from a citation because it means the work is the thing to
beat. Those are recorded here and in Ledger 3 rather than in Ledger 6, whose scope is academic
citations.

### Seventeen Surveys Omit All Fourteen Works

This is the round's most useful structural finding, and it is not a coverage problem. Seventeen
surveys and taxonomies that draw this subfield's map carry none of the fourteen works, each
confirmed by fetching full text. Phase C added two more by reading their Crossref-deposited
bibliographies, so the count is **nineteen**: 10.3390/ai7080298 (MDPI *AI*, 112 references) and
10.1145/3837083 (ACM Computing Surveys, 195 references) each omit all fourteen, and the ACM survey
cites TrustLLM while doing so. Seven surveys do cite the line, after Phase B verified three more:
arXiv:2510.06445 v3 (agentic security, BRAC University and QCRI), arXiv:2606.10749 (LLM-agent
security, Nanjing University and TU Munich), and arXiv:2604.16548 (long-term memory security,
MemTensor and Shanghai Jiao Tong). The seventeen omitting surveys stand unchanged, and none of the
three is among them. The share of mapped surveys that omit the line therefore moves from 81% (17 of
21) to 71% (17 of 24): a smaller gap than this section first recorded, and still the dominant
case.

- **Against GRADE**, arXiv:2605.06812 "Towards Security-Auditable LLM Agents: A Unified Graph
  Representation" carries the same idea one month earlier and cites nothing from the line. EDGE
  (arXiv:2609.01360) and AgentFlow (arXiv:2607.01640) both build dependency-graph framing over agent
  runs and cite GRADE nowhere. This is a priority problem rather than a visibility problem.
- **Against IET**, arXiv:2606.04990 (`From Agent Traces to Trust: A Survey of Evidence Tracing and Execution Provenance in LLM Agents`) is the single most on-topic survey in existence for Auditable Agents, IET and GRADE, and cites none of the three. LEDGER (arXiv:2608.18398) covers implicit trace reconstruction and cites IET nowhere.
- **Against AEGIS**, the three systems closest to it in problem statement all mediate tool calls
  before execution and none cites it: ClawGuard (arXiv:2604.11790), "Before the Tool Call"
  (arXiv:2603.20953, concurrent), and Provably Secure Agent Guardrail (arXiv:2605.29251). Praetor
  and STARS are the only exceptions across the 44-system neighbour set.
- **Against FORTIS**, six direct skill-privilege neighbours cite nothing: SkillScope
  (arXiv:2605.05868), SkillGuard (arXiv:2606.03024), Behavioral Integrity Verification for AI Agent
  Skills (arXiv:2605.11770), Structured Security Auditing of Untrusted Agent Skills
  (arXiv:2604.25109), Evaluating Skills Not Just Agents (arXiv:2608.20614), and A Comprehensive
  Survey on Agent Skills (arXiv:2605.07358).

The one case running the other way is the strongest positioning evidence to date. The Long-Horizon
survey names one of its three boundary categories in AEGIS's own words, "Tool-call Boundary. Acting
as a pre-execution firewall, this mechanism inspects tool arguments before execution", makes AEGIS
the single named instantiation, and places it in the taxonomy figure.

### The Coinages Have Not Leaked, Which Corrects an Earlier Reading

A phrase-level sweep returned a clean null. No page uses "pre-execution firewall", the
observed / declared / inferred two-layer edge framing, or "autonomy tax" as a capability-cost term
without naming one of the fourteen works. Every string hit was one of the fourteen or a work citing
one.

An earlier reading of this round held that vendors had adopted the line's vocabulary. That was
overstated. What the vendor lane matched (Galileo's "tamper-evident audit trail", Witness AI's
"enforce policy before agents act") is generic security vocabulary predating agent work by decades.
The corrected reading is worse rather than better: the specific framings have not propagated at all.

The vendor sweep itself was thorough and returned zero. Forty-five commercial agent observability,
guardrail, governance and MCP-security vendors, 13,973 sitemap URLs, 2,460 fetched pages, six full
repository clones, zero citations of any of the fourteen works. Lakera's empirical audit of 221
OpenClaw skills addresses over-privilege at the skill layer, which is FORTIS's problem statement
exactly, and cites nothing. Sixteen frontier labs returned 54 verified negatives, with no system
card citing anything.

### What the Citation Services Returned, and What That Does Not Prove

Three of the seven confirmed citations were not recovered by any service queried in this run. Two
cite a repository URL with no arXiv identifier in the entry, so an identifier match has nothing to
key on. The third lives on OpenReview and preprints.org, and neither service returned it here; that
is one missing record each rather than evidence that those platforms go unindexed generally. An
identifier-only audit in this run would have reported Agent Audit as having survey-level coverage and
nothing more.

- **Semantic Scholar was the only source that produced an edge**, 69 across the fourteen works.
  OpenCitations, Crossref, DataCite, DataCite Event Data, OpenAIRE, Europe PMC and Inciteful
  contributed zero between them.
- **The queried services did not recover these edges in this run.** All fourteen sampled records
  had empty outgoing reference metadata on OpenAlex: resolved by DOI with correct titles and dates,
  then `referenced_works_count = 0` for every one and `cited_by_api_url = null`, while Semantic
  Scholar served 25 references for the same Praetor record. Citation retrieval was additionally
  limited by budget failures, and a 429 is not a successful empty list. Two cautions on how far this
  generalizes. An empty *outgoing* reference list does not establish that nothing cites the target,
  because OpenAlex models outgoing references and incoming citations separately. And fourteen records
  are a sample, not the population of 2026 preprints. What follows for practice: a recent-preprint
  absence needs another source and a direct document check, including a repository-URL search, before
  it is read as absence.
- **Inciteful is not an independent check on OpenAlex.** It returned zero in both directions for all
  fourteen targets and all eighteen already-counted citers, reproducing the same blind spot rather
  than testing it.
- **Date filters keyed on the indexed publication date drop revised surveys.** "A Survey on Agentic
  Security" (arXiv:2510.06445) carries a Semantic Scholar `publicationDate` of 2025-10-07, earlier
  than all fourteen works; its Agent Audit citation appears only in v3, submitted 2026-06-12.
- **Reference locators differ by format, so record the format alongside the locator.** Audita's PDF
  prints [17] on page 16; its HTML entry has element id `bib.bib76`. HANSARD's PDF prints [5], while
  its HTML labels the entry [20]. A summarizing fetch of STARS re-sorted its bibliography and would
  have produced a false correction, so the HTML numbers above were grepped from raw markup; the PDF
  numbers came from downloading and rendering the PDFs.

### Self-Citation and Cross-Citation Accounting

Seven co-author works were excluded before candidacy: arXiv 2604.17299 Cat-DPO, 2607.27670 JigShape,
2606.02976 Memory Retrieval for Changing Preferences and 2502.11059 ClimateLLM (Yue Zhao an author
on each); 2602.09341 Auditing Multi-Agent LLM Reasoning Trees and 2606.22844 RaMem (led by Wei Yang,
a FORTIS co-author); and 2607.15314 Cura 1T (actAVA AI, the CHI-Bench team).

Cross-citation inside the fourteen accounts for three apparent zeros exactly: WeClawArena's only
citer is CatchBench, and Action Alignment's and SkillCenter's only citer each is Auditable Agents.
AEGIS's six Semantic Scholar citers are all already counted or first-party.

### The IET Zero Is Falsified, and the Index Sweep Was Wrong

Both named documents carry the citation, and both were fetched and read. The Crew Scaler response to
the NIST CAISI RFI (arXiv:2603.09002) lists IET in its bibliography as "When only the final text
survives: implicit execution tracing for multi-agent attribution. External Links: 2603.17445", cited
as reference [991] with body citations in III-C15 and III-F10. DEMM (arXiv:2605.04093) names IET,
its authors and the DOI `10.48550/arXiv.2603.17445` in its page 38 bibliography, as Nian et al.
(2026b). Note the title variant: both cite it as "for multi-agent attribution" where
`data/publications.json` has "for multi-agent Auditing". Same arXiv identifier.

This round first recorded the question as open, on the strength of a workflow sweep reporting a hard
zero across eight indexes, 879 full texts and `site:arxiv.org`. That was the wrong call, and the
reasoning error is worth keeping: **a search that finds nothing does not outweigh a bibliography
entry that someone fetched and read.** The lane that reported the falsification was right, and it
was discounted in favour of the broader sweep because the sweep had covered more surfaces. Surface
count is not evidence.

Both citing works were already counted for other works, so this adds no ledger row. It removes a
standing negative and it corrects the earlier zero, and Phase C established the cause: Crew Scaler's
entry is reference **[991]**, beyond the depth cap automated reference parsers apply, and it uses the
title variant "Attribution" rather than the "Auditing" in `data/publications.json`; DEMM is PDF-only on
arXiv with no HTML5 metadata to extract. Two separate parser limits, and a "hard zero across eight
indexes" reveals neither.

### Three Standing Negatives Revisited

| Standing negative | Status after this round |
|---|---|
| FORTIS benchmark has zero confirmed external citers | **Already falsified on 2026-08-30**, by the same paper. This round reverified arXiv:2608.18351, including its reference number and both results tables. Not a new finding. |
| IET has zero confirmed external citers | **Falsified.** Crew Scaler (arXiv:2603.09002) cites it as reference [991]; DEMM (arXiv:2605.04093) carries its DOI on page 38. Both fetched. No ledger row, since both citing works are already counted. |
| CatchBench has zero external non-academic footprint | **Falsified.** The reading-notes lead was fetched: `inkeast/MessageDaily`, file `content/posts/2026-08-25-catchbench-paper-reading.md`, a dedicated third-party close reading dated one day after the paper posted, naming arXiv:2608.22808 and `yzhao062/catchbench`. The academic zero is untouched. |
| No Attacker Needed has no verified citer | **Falsified**, by two independent documents. arXiv:2606.10749 cites it as printed reference [213] with a body use in Section 8, and arXiv:2604.16548 reproduces its 57-71% contamination range in prose and in a Table 3 row. A third, `txn2/mcp-data-platform` issue #1163, uses it as a literature baseline. |
| MemoHarness has no verified citer | **Falsified.** arXiv:2608.30478 (Pera, Fudan and collaborators) cites it as prior art for the term "agent harness"; `technologyHu/research` pull request #2 is a dedicated survey report carrying a 17-row concept-to-code mapping table; `schubertsean-ui/onelive` pull request #35 adopts its D1 to D6 defect taxonomy. |

| The Autonomy Tax has no verified citer | **Falsified.** OmniScientist (arXiv:2608.13558, NUS and Oxford) cites it in its Introduction as foundation for agent tool use, alongside ReAct, Toolformer and Reflexion. Ledger 6 row A34. |
| GRADE has no verified citer | **Was never true, and this document already held the proof.** Ledger 6 row A19 (TraceCompiler, arXiv:2608.02680) and Ledger 3 row 77 ("Doomed from the Start", arXiv:2607.06503) were both recorded before the sweep that reported the zero. Phase C re-fetched both. |
| WeClawArena, SkillCenter, Agent Safety Is Action Alignment, CatchBench and IET have no external academic citer | **Holds**, across arXiv full text, ACL Anthology, OpenReview, thesis repositories and Asian scholarly databases. Read it as a statement about the literature only: three of the five have real code or editorial adoption recorded in Ledger 3 this round. WeClawArena's Anthology absence has a reason rather than a verdict, since EMNLP 2026 Findings is not yet published there. |

All four zeros this pass attributed to the verification cap are now falsified, and one of the four had
never been a zero. Recording them as explicit reversals rather than editing the numbers in place
follows the IET case above. A zero that a later fetch overturns is a finding about the method, and
correcting it silently destroys the only evidence that the method produced it.

### Verification Cap Is the Binding Constraint

The three workflow methods produced 94 candidates (26 graph-diff, 10 neighbour-cite, 58 full text).
Nine reached adversarial verification and two of those were the same work found twice, so seven
distinct works were checked and roughly 85 candidate slots were never examined. Four of the nine
per-work zeros were therefore cap artifacts rather than measured absences: GRADE, The Autonomy Tax,
No Attacker Needed and MemoHarness all returned candidates that nobody verified. **All four have since
been falsified**, No Attacker Needed and MemoHarness in Phase B and The Autonomy Tax in Phase C, and
GRADE turned out to have had two citations recorded in this document all along. Four named cap
artifacts, four reversals, none of them a measured absence.

Six already-named candidates were run the same day rather than deferred to the next round, and
**all six verified**: arXiv:2510.06445 v3 (to Agent Audit), 2608.23610 and 2608.12761 (to Auditable
Agents), 2606.10749 and 2604.16548 (to No Attacker Needed), and 2608.30478 (to MemoHarness). Six
named candidates, six confirmations, zero refutations.

That result reframes what the cap cost. It did not defer weak leads, it deferred the six strongest,
and it deferred them after the round had already been written up with three of their targets recorded
as zeros. A cap applied after candidate ranking is a cap on the top of the list. The two identifiers
the workflow derived by elimination also survived contact with the documents: arXiv:2604.16548 names
the No Attacker Needed author string in full, and arXiv:2608.30478 names MemoHarness by title.

Two identifier pairings the workflow derived by elimination were checked against
`data/publications.json` and both hold: No Attacker Needed is arXiv:2604.01350 and MemoHarness is
arXiv:2607.14159.

### Surfaces the Auditing Round Never Reached

Google Scholar in any form, 403 throughout, which is the one surface indexing preprint-to-preprint
edges that Semantic Scholar misses. Publisher-side full-text search at ACM, IEEE, Springer and
ScienceDirect, the only route to 131 journal-only citing works that were filtered but never fetched.
Theses and dissertations. MCP server registries and agent-skill marketplaces. No retry of the
OpenAlex list endpoints, which returned `Retry-After: 69687s` (about 19.4 hours) for the whole run.

Phase B closed three of the surfaces this list opened with. Its five code lanes read Hugging Face
dataset and Space cards, PyPI and npm package pages, and dependency trackers directly, which is how
the Ai2 TrustLLM dataset and the Splunk integration were settled.

Publisher full text stayed shut to a direct fetch, and Phase C got both answers anyway through
Crossref's deposited bibliographies: 10.3390/ai7080298 (MDPI) cites nothing of this lab's across 112
references, and 10.1145/3837083 (ACM Computing Surveys) cites TrustLLM at reference 77 across 195.
Neither is a zero, and neither needed the paywall. Of the twelve O'Reilly items, five were already
recorded and six were verified through Packt companion repositories and previews; of the Medium and
Zhihu blocks, four of nine yielded. What genuinely remains behind access control is small and named in
the Phase C section: two Gartner documents, one S&P Global 451 page, one member-only Medium post, three
Zhihu pages, and one book chapter.

### New Collision to Register

Meta's Llama 3 paper carries a "Yue Zhao" author or citation that is a different person. Add to
`references/disambiguation-registry.md`.

### Patents: 65 Candidates, 49 Fetched, 49 Confirmed

The patent lane returned **65** distinct patent numbers, not the 64 first recorded here, and it is the
largest single-class yield of the round, which matches the 2026-08-13 finding that patents drive most
Ledger 3 growth. Sixteen never entered verification because their URLs were already in the index; thirteen of
those are already recorded here, ten as Ledger 3 rows and three inside earlier pass sections. Phase B fetched the remaining **49** and confirmed
**49**: zero refutations, zero unreachable pages, the highest confirmation rate of any class in the
round. Ledger 3 rows 231 to 275 carry the 45 that were genuinely new, and the other four are
reverifications of rows 66n, 166, 177 and 178.

Use is mostly load-bearing rather than bibliographic. 29 of the 49 name the work inside the
specification body as a component the invention uses, 15 benchmark against it with numbers in a
results table, and 5 are reference-list or prior-art mentions. Two are claimed rather than merely
described: CN113076913A claims PyOD in Claim 3, and CN118316981A claims COPOD in Claims 1 and 5.
Works cited are PyOD (19), COPOD (7), ECOD (6), XGBOD (6), SUOD (4), PyGOD (2), CONAD (2), TODS,
LUNAR, and ADBench.

**The jurisdiction split is the finding worth carrying forward.** 39 of the 49 are CNIPA filings, 6
are US, 2 WO, 1 DPMA and 1 Slovak. Assignees are mostly Chinese universities and provincial
technology firms, with Rapid7, Valeo Schalter und Sensoren, Riva Health, Ramot at Tel Aviv
University, Alibaba Cloud (filing with Tsinghua), and China Telecom Fufu the recognisable names. The
corporate roster the earlier draft of this section listed, Visa, IBM, Tencent, NICE Actimize, Dun &
Bradstreet and Genentech, is the set that was suppressed as already recorded, so the two lists are
complements rather than rivals. This evidence is predominantly Chinese-language and predominantly
implementation rather than citation, which means an English-language or DOI-keyed sweep sees almost
none of it.

### Held, Pending Verification

- **291 new coverage URLs** never reached verification. **Cleared**: Phase B verified all 420
  unverified candidates from both rounds, the 291 included. See the Phase B section below.
- **Three Ledger 7 candidates**, all three now fetched. Nature *Scientific Reports*, "usfAD based
  effective unknown attack detection focused IDS framework", sources its baselines from PyOD and takes
  Ledger 7 row S43. IEEE TNNLS Text-ADBench is confirmed at row S44, which also upgrades Ledger 3 row
  66i from an arXiv preprint to a journal publication. IEEE TPAMI, "Representation Learning for
  Tabular Data: A Comprehensive Survey", cites ADBench as reference [99] in a one-sentence prior-art
  description and **does not qualify for Ledger 7** under that table's substantive-use rule, so it is
  routed to `/citation-audit` instead. Verifying a candidate and admitting it are separate decisions,
  and this one was verified and not admitted.
- **Five gated documents**, held rather than guessed: Gartner "Govern AI Using TRiSM", Gartner
  "Consult the Board: LLM Strategies", Gartner Peer Insights AI Security and Anomaly Detection,
  S&P Global 451 Research, and one Stack Overflow thread.
- **Whether Libraries.io's repository crawl is equally degraded for other packages** was not
  established; the finding is scoped to pyod.

### Phase B: All 420 Unverified Candidates Verified, and What Phase A Got Wrong

Both rounds above closed with more candidates than verification budget, so a third dispatch ran over
everything left: 16 Agy lanes through `/prun`, sliced by verification method rather than by subject
because fetching a patent, grepping a repository file and reading a CJK article cost different amounts
and need different instructions. 16 of 16 lanes complete, zero FALLBACK, **420 of 420 records
returned**, every one joining back to the worklist on normalized URL. No lane silently shrank its
denominator.

| Outcome | Count | Meaning |
|---|---|---|
| CONFIRMED | 319 | fetched, the work is named, the quote is in the source |
| DROPPED | 63 | first-party, machine-generated, a mirror, or not coverage |
| UNREACHABLE | 23 | paywall, anti-bot, or Cloudflare; not counted either way |
| REFUTED | 15 | fetched and the claim does not hold |

**The tier movement is the round's sharpest method finding: 110 downgrades, 310 unchanged, and zero
upgrades.** A 26.2% downgrade rate with no countervailing upgrades means Phase A's tier guesses are
biased in one direction rather than noisy. A guess that was merely imprecise would miss in both
directions; this one is optimistic, and optimistic by a quarter. Treat any Phase A tier as an upper
bound on what verification will support.

The bias concentrates at the top, where it costs most. Six candidates arrived as Tier 0 and **one
held**: the SLAC OSTI report citing MetaOD, already recorded above in Ledger 1b. One moved to Tier 2,
and four were topic-validation, pages about the subject matter that name no work and no person: the EU
GPAI Code of Practice page, the OECD AI transparency-report register, the UK AISI Inspect Evals index,
and a regulations.gov NIST docket.

The Tier 2 demotion is the round's only near-miss on an institution. A lane recorded the UK AI Safety
Institute as registering CHI-Bench, and the page is the **Inspect Harbor registry run by Meridian
Labs**, a third-party adapter index for AISI's `inspect` framework rather than an AISI publication.
Real coverage, wrong institution, three tiers of difference. The same lane also returned AISI's own
Inspect Evals index, which names nothing, so both the true negative and the misattributed positive
were in hand at once.

**Five candidate addresses did not exist.** Four GitHub repositories and one Hugging Face Space, all
404 on direct fetch: `AgentShield-Security/AgentShield`, `HandoffGraph/handoffgraph`,
`mcp-data/platform`, `onelive-ai/onelive-engine`, and `actava/chi-bench-leaderboard`. The four in the
auditing line are dissected in the comparison-finds section above; the pattern is that the lane knew
the document and synthesized its address. A sixth case is a milder version of the same thing, worth
separating rather than folding in: `edbiomedai/scmorph` exists and the cited `setup.py` does not,
because that project ships a `pyproject.toml`. A fan-out that reports a URL has not established that
the URL resolves, and four of the five invented addresses were written into this document as findings
before anyone fetched them.

**The worklist builder's first-party filter passed 47 first-party records, and Phase B dropped all
47.** That filter is mine, not the lanes', and it matches domains: anything under `yzhao062`,
`USC-FORTIS`, `pygod-team`, the lab site or the personal site. First-party material reaches
third-party domains constantly: 14 Hugging
Face Daily Papers landing pages for the lab's own papers, 7 alphaXiv preprint pages, 2 ACL Anthology
publication records, PyPI release pages for `pygod` and `catchbench`, Hugging Face Spaces under a
co-author's account, and a fork of `agent-audit` under `iflow-mcp`. First-party material is the single
largest reason a candidate was dropped, accounting for 46 of the 63 drops. Domain matching cannot
separate a paper's own listing on an aggregator from third-party coverage; whether the page's subject
is the lab's work, authored by the lab, is the test that does.

Two other flags behaved as the contract intends, and the difference between them matters. 41 records
were machine-generated, mostly daily-digest bots and scraped mirrors, and 39 of those were dropped.
29 were machine-translated reposts with no named human editor, and only 4 were dropped: the rest were
capped at Tier 3 and kept, because a machine translation of a real article is degraded coverage rather
than no coverage.

**Two dedup defects surfaced, both mechanical and both fixable.**

The first is language variants. Google Patents serves the same document at `/en`, `/zh`, `/fr` and
`/sk`, and the URL index holds patent links in all four (23, 9, 2 and 1 respectively). Three of the
four patents Phase B re-verified were already on file under a different language suffix than the
candidate arrived with: CN117520980A was indexed as `/zh`, US12184394B2 and US12242939B2 as `/fr`.
The fourth, CN111666198A, escaped for the reason in the next paragraph: Ledger 3 row 66n names it and
carries no link at all. The refreshed index at `skills/news-search/scratch/2026-09-12/known-urls.txt` now carries a
language-stripped key for every patent alongside the full URL, and it grew from 1,929 entries to
2,443.

The second is documents this record names without a URL. The SLAC OSTI report reached Phase B as a
candidate and was confirmed there, hours after being written into Ledger 1b in this same pass, because
that row names it as "SLAC OSTI 3005876" and carries no link. A URL-keyed suppression list cannot see
a document identified by accession number. Two already-counted items re-surfaced the same way at a
second surface, Real Python #208 as an Apple Podcasts URL and "Reason Less, Verify More" as a
workshop-hosted PDF, which is the third and fourth instance of the defect this pass already recorded
under "Four Claims Reported as New Were Already Counted". The suppression index needs identity keys
beyond the URL: arXiv ID, DOI, patent number, OSTI accession, podcast episode.

**One conflict is a taxonomy question rather than an error.** A Phase B lane returned the Chemistry
World article as a confirmed Tier 1 naming Therapeutics Data Commons, and this pass recorded the same
article as a verified negative on the grounds that Yue Zhao is named nowhere in it. Both readings of
the document agree on every fact. They disagree on whether third-party media that names a co-authored
work, critically, without naming the author counts as coverage. The verified negative stands for now,
and the rule needs writing down, because this is the second missing rule in the same pass: the other
is where "ran the cited benchmark and published its numbers" belongs.

What the 319 confirmations became is a smaller number than 319. Most are Tier 3 and Tier 5 adoption
evidence that this record has always tracked as counts rather than rows: 157 T3 and 52 T5, against 1
T0, 12 T1, 93 T2 and 4 T4. The rows added from them are the 45 patents in Ledger 3, the Ledger 7 and
Ledger 6 rows listed in this pass, and the ecosystem rows below. The full verdict set, one JSON object
per candidate with locator and quote, is at
`skills/news-search/scratch/2026-09-12/phase-b-verdicts.jsonl`.

### Phase C: Route-Around Verification of Everything Still Blocked

Phase B left 23 candidates unreachable and this pass carried five more gated documents, two
publisher-blocked surveys, six repository leads a sweep named but never fetched, and seven per-work
zeros resting on method rather than on a fetch. Every one of those is blocked on a **route** rather
than on a fact, so a third round ran 6 Agy lanes sliced by the alternate route each had to try.
6 of 6 complete, zero FALLBACK, 38 records.

| Outcome | Count |
|---|---|
| CONFIRMED | 22 |
| still blocked, every route named | 8 |
| verified-negative | 6 |
| dropped | 2 |

**Most blocks are bot detection rather than access control.** 25 blocked or gated items entered these
lanes and **17 reached a decision**; 8 stayed blocked with every route named. Three more were settled
locally before dispatch by the identity check described below, because they were already in this record.
The routes that worked are worth naming because none requires a subscription:

| Route | What it settled |
|---|---|
| **Crossref REST API** (`api.crossref.org/works/<doi>`) | Publishers deposit their **full reference lists** to Crossref for free. This settled both "must not be recorded as zeros" surveys in two requests, through a 403 at both publishers. |
| **Packt companion repositories** on GitHub | 5 of 9 subscription-reader books. A `from pyod.models.knn import KNN` in the chapter's own notebook is stronger evidence of use than the prose would have been. |
| **Stack Exchange API v2.3** | The Stack Overflow thread, through a Cloudflare challenge on the web page. |
| **Browser User-Agent on Medium** | 3 of 4 Medium posts. Medium's 403 is bot detection; only one of the four is genuinely member-only. |
| **`raw.githubusercontent.com`** | All 6 repository leads. |
| **Google Books preview, publisher TOC, public translation mirror** | 3 books with no companion repository. |

No paywall was bypassed. Where a claim sits behind one, the record says `still blocked` and names the
routes tried: two Gartner documents, one S&P Global 451 Research product page, one member-only Medium
post, three Zhihu pages behind an anti-bot captcha that survived four routes, and one Packt book whose
chapter topic is confirmed while the TrustLLM citation inside it is not.

**The Crossref reference-list route is the find worth carrying into the next round.** The audit's
standing note that publisher-side full text is "the only route to 131 journal-only citing works" is
wrong in one direction: for any work with a Crossref DOI, the deposited bibliography answers "does this
paper cite X" without reading the paper. It does not answer *where* in the body, so it establishes a
citation and not a Ledger 7 admission. Both blocked surveys resolved this way:

- **10.3390/ai7080298** is "Agentic AI Safety: A Structured Review of Open Problems and Their
  Regulatory Anchoring" (MDPI *AI*, 2026-08-04; Valenta, Rozinek, Horálek). **112 deposited references
  and not one names any work of this lab's.** A verified negative, and the eighteenth survey in this
  pass's survey census that omits the whole line.
- **10.1145/3837083** is "A Comparative Survey of Security Risks in AI Systems: From LLMs to AI Agents
  and Embodied Agents" (**ACM Computing Surveys**, 2026-08-22; Zhejiang University and Stony Brook).
  195 deposited references, and **reference 77 is TrustLLM**. A new citation at the field's highest-impact
  survey venue. Body placement is unknown behind the ACM wall, so this routes to `/citation-audit`
  rather than to Ledger 7. It also omits all fourteen auditing-line works, making it the nineteenth.

**Six leads a sweep found and never fetched: six confirmations, no bot digests, no first-party.** These
were recorded as "thin but non-zero" and written off. Fetched, they are: `Stage-11-Agentics/etch` citing
Implicit Execution Tracing by full title and arXiv ID, which is that work's only code-search footprint;
`choiceoh/Deneb`, which **implements** SkillCenter's source-grounding rule in Go rather than citing it;
`endomorphosis/ipfs_datasets_py` (22 stars) naming SkillCenter only through repository and Hugging Face
dataset handles, so no identifier-keyed search can see it; `ydyjya/Awesome-LLM-Safety` at **1,909 stars**
carrying Agent Safety Is Action Alignment with title, arXiv link and USC affiliation; `Tibsfox/gsd-skill-creator`
(69 stars) encoding the same paper's argument and quoting its numbers; and `smirby/aiextinctionrisk`
analysing it in an independent blog post.

Taken with the six deferred priority candidates that all verified earlier in this pass, **every lead
this audit deferred for lack of budget has since verified: twelve for twelve, across two batches
triaged by different methods.** That is now a measured property of the triage rather than an anecdote,
and it is the strongest argument this record contains against reporting a cap as if it cost nothing.

**Two standing zeros fall, and one was never a zero.**

- **The Autonomy Tax is cited.** OmniScientist (arXiv:2608.13558; Bobo Li, Hao Fei, Tianjie Ju, Mong Li
  Lee, Wynne Hsu, NUS and Oxford) cites it in its Introduction as foundation for agent tool use,
  alongside ReAct, Toolformer and Reflexion. This was the last of the four cap-artifact zeros still
  standing; all four are now falsified.
- **GRADE was never at zero, and this record already held the proof.** Two sweeps reported GRADE as
  having no external citer while **Ledger 6 row A19 (TraceCompiler, arXiv:2608.02680) and Ledger 3 row
  77 ("Doomed from the Start", arXiv:2607.06503) were already in this document**. Phase C re-confirmed
  both by fetching them. This is the round's dedup defect running in the opposite direction from every
  other instance: the lanes were given a suppression list so they would not re-report known coverage,
  and nobody ran the *zeros* question against the ledger, so a work with two recorded citations was
  published here as a zero. Check a zero against the record before reporting it, exactly as a candidate
  is checked.

**Five zeros hold, and the distinction between two kinds of zero now matters.** WeClawArena,
SkillCenter, Agent Safety Is Action Alignment, CatchBench, and Implicit Execution Tracing have **no
external academic citer**, confirmed across arXiv full text, ACL Anthology, OpenReview, theses
repositories and Asian scholarly databases. Three of those five have real non-academic adoption, found
in the same round: SkillCenter has two code adoptions, Agent Safety has three list-and-blog items, and
IET has one repository citation. A work can be adopted in code and uncited in the literature at the
same time, and a row that reports one number hides the other. WeClawArena's ACL Anthology check also
came back with a reason rather than a zero: **EMNLP 2026 Findings is not yet published in the
Anthology**, so its record cannot exist there yet.

**The IET index blindness finally has a mechanism.** This pass recorded IET's falsified zero with the
note that "whose precise cause remains unverified". Phase C names it: Crew Scaler's citation is
reference **[991]**, past the depth cap automated parsers apply to reference lists, and it uses the
title variant "Attribution" where this repo's own metadata says "Auditing"; DEMM is PDF-only on arXiv
with no HTML5 metadata to extract. Two different parser limits, neither of which a "hard zero across
eight indexes" reveals.

**Two more locators were mangled rather than invented**, which is the milder form of the Phase B
failure: the Towards Data Science COPOD URL carried a three-character suffix typo, and the Medium slug
was truncated mid-title. Both resolved to real articles once the canonical URL was recovered. Phase B's
five invented addresses and these two corrupted ones are the same failure at different severities, and
both are caught the same way: resolve the locator before believing the row.

**The already-counted rate on blocked items is as high as on any other class.** Of the 12 O'Reilly
items, five were already in this record: two books by title at rows 37 and 39, one video edition of row
37, and two Packt titles at rows 195 and 217 that were on file under Packt product URLs while the
candidates arrived as O'Reilly reader URLs. That is 5 of 12, and it is the fifth and sixth instance of
the same identity-key defect in one pass, which is what finally motivated the script described below.

### Method Defects in This Round, and the Fix

Five instrumentation failures, four of them producing a false zero, and all five were mine rather
than the lanes'.

1. **Ledger comparison against the wrong file, with the wrong normalization.** The first dedup run
   reported 0 of 576 URLs already tracked. It compared scheme-carrying URLs against
   `scratch/existing-urls.txt`, a 136-line file from May, when the live index is
   `scratch/2026-08-30/known-urls.txt` with 1,929 entries stored as bare host and path. Correct
   answer: 150 of 454 already tracked.
2. **Tier read without status.** An early count reported 25 Tier 0 candidates. Eleven were
   `status: verified-negative`, correctly labelled by the lanes, on documents read cover to cover
   that mention nothing: five NIST publications, a Treasury report, a PNNL report, and four WHO
   documents. The schema separates outcome from outlet class and the reading collapsed them. Real
   new Tier 0 was 2. **The lane contract needed no change**; zero rows were mislabelled.
3. **`grep -c` exits 1 when it prints 0**, so `|| echo 0` appended a second zero and every one of 32
   prompts was judged to be missing its result path when all 32 carried it.
4. **A process search matched its own command line.** Searching for `dispatch_lanes.sh` among
   running commands matched the search itself. The count was first called a quoting artifact, then
   wrongly corrected to a real count of three, and settled only by walking the parent chain
   (37856, 54900, 27804, 68460) to show it was the search's own process tree. Real answer: zero
   launchers. `scratchpad/check_launchers.py` now excludes explicit self-markers and requires the
   script path to sit immediately after the shell binary.

5. **The URL index treats one document as four.** Google Patents serves the same patent at `/en`,
   `/zh`, `/fr` and `/sk`, and the index holds patent links in all four. Three of the four patents
   Phase B re-verified were already on file under a different language suffix than the candidate
   carried. The refreshed index now stores a language-stripped key beside every patent URL. The
   general form of the defect is wider than patents: this pass recorded four already-counted items
   reached by a second surface, and Phase B added two more, so the index needs identity keys beyond
   the URL (arXiv ID, DOI, patent number, OSTI accession, podcast episode) rather than one more
   special case per platform.

A sixth non-defect is worth recording. Two harness notifications reported background wrapper tasks
killed for low memory while 8.0 GB of 31.7 GB was free and PyCharm held 3.7 GB. The lane launcher
survived both and completed all 32 units. A hand-written second-wave script would have
double-dispatched had it not been killed during its drain wait.

The X5 lane failed once with a genuine empty-response FALLBACK: Agy exited 0 after 9 search calls
having written 80,291 bytes of event-stream JSON and no result. An 855-byte delivery-requirement
addendum appended to the prompt recovered it on retry, and the retry exercised the dispatcher's
path-move fix for the first time, relocating the old FALLBACK to `previous-result.nRZmCV` rather
than overwriting it.

### Cross-Skill: citation-audit

`/citation-audit --source both` re-ran the same day and overwrote `citation-affiliation-audit.md`.
Net new: **zero Tier 0, one Tier 1** (AstraZeneca UK citing the AI foundation-models paper for
therapeutic science). Tier 0 holds at 20 entries; Tier 1 moved 64 to 65. Dimensions analyzed 1,415
unique citing papers, up from 1,402 on 2026-09-05.

**The OpenAlex leg failed the same way it did on 2026-09-05, and this time the mitigation was
working.** The Phase 1 identifier cache engaged and was rewritten during the run, and the
1000-credit free tier still ran out before a single citing-paper query: 0 of 46 works queried,
`Retry-After: 67847s`, about 18.8 hours. The run exhausted the available daily allowance despite
cache use. Neither the starting balance nor this invocation's standalone cost was measured, and the
same day's discovery work also queried OpenAlex, so whether a full pass fits a fresh allowance
remains unknown. Those 46 works are unknown, not zero. Two runs a week apart show the same outcome,
which is reason to measure the standalone cost against a fresh allowance before deciding to buy
credits or to let Dimensions carry the audit alone.

**A documentation defect turned up while checking that.** Both this skill's `SKILL.md` and the
script's own docstring named the cache `data/.openalex-id-cache.json`, while the code writes
`.cache/openalex-id-cache.json`. Fixed in both places. The wrong path produced a wrong conclusion
inside this session: the cache was briefly reported as never engaging, on the strength of an absent
file at the documented location.

**The two rounds cross-check each other on the auditing line, and the reason for the zero differs
between them.** No auditing-line work appears in the Tier 0 or Tier 1 tables. For AEGIS that is a
filtering outcome rather than a retrieval failure: Dimensions did return one citing publication, new
since 2026-09-05, and this audit's tier classifier excluded it because the citing authors sit at no
institution in its Tier 0 or Tier 1 banks. The service found the edge; the report's own scope rule
dropped it. The auditing round separately failed to retrieve most edges from eight citation indexes.
Those are two different mechanisms and should not be summed into a claim that bibliometrics cannot
see this line. What holds across both is narrower and still useful: the seven confirmed citers were
established by fetching and reading the citing documents, not by any index or affiliation table.

### Propagated to Site

Done in the same change. All eight stale `55M+` strings now read `59M+`. The two dependent counts in
`opensource.html` (lines 324 and 334, which had drifted apart during editing) both read 5,567
repositories and 160 packages, qualified as approximate per GitHub's own disclaimer, with the
snapshot date moved to September 2026. The bio paragraph in `index.html` and `files/bio.txt` keeps
its original single-sentence form and moves 60 million to **65 million**, the real five-package total
being 65,936,276 across pyod, combo, suod, pygod and pytod. Its dependency-count sentence was
dropped: a dated approximate repository count is audit telemetry rather than biography, and it is
already carried twice on `opensource.html`. `cv/open-source.tex` was regenerated from
`data/open-source.json` rather than hand-edited.

A review-process note worth keeping, because the objection that drove it was itself wrong. Both
reviewers pushed on whether "projects, including PyOD, ADBench, TrustLLM, agent-audit, and Aegis,
together exceed 65 million downloads" makes the download denominator clear enough, one of them
arguing the list credits repositories that ship no PyPI package. Acting on that expanded one sentence
into three and named ten projects, which the user rejected as the wrong register for a bio.

Checking the premise afterwards showed it was false. Four of the five named projects ship PyPI
packages whose recorded home page is the same repository: `agent-audit` (14 releases, from
2026-02-04), `adbench` (14 releases), `trustllm` (7 releases), and `pyod` itself. Only Aegis has no
package of its own; the `aegis` name on PyPI belongs to an unrelated project. So the sentence was
defensible for the reason the second reviewer gave, that "including" is non-exhaustive and a
portfolio total does not claim each named example contributes to it, and also for a reason neither
reviewer had: most of the named projects do ship packages.

Two things to carry forward. The precision belongs in this record, where the five-package denominator
is stated, rather than in the bio. And an objection that sounds rigorous still needs its premise
checked: this one survived two review rounds and a revision before anyone queried PyPI.

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

154 UNVERIFIABLE records are re-fetch targets rather than absent evidence.

**Two of the three long-blocked items are now cleared, through the Wayback Machine.** `ai.mil` and
`mitre.org` both refuse a scripted fetch and a browser user agent alike, and `WebFetch` gets the same
403, but each PDF has a live archived snapshot. Fetching those settled both rows against the document
rather than against a memory of it:

- **DoD CDAO Toolkit** (105 pages, snapshot 2025-10-06). PyOD appears in the Stage 3 Assessment at
  p14 as the answer to the in-use monitoring question, and at p49 as a full entry under
  Out-of-Distribution Detection Tools: *"Python library for detecting outlier objects in multivariate
  data. Includes more than 40 detection algorithms."* TrustLLM appears at p19 among the fairness tools
  and at p69 as *"Comprehensive framework for assessing the trustworthiness of LLMs across six
  dimensions."* Rows 2 and 2b are confirmed as written.
- **MITRE LILAC v1** (38 pages, snapshot 2025-10-18). Row 8e claims a body citation, and the string
  `TrustLLM` occurs only once, on p18, inside the reference list. The claim survives anyway because
  the report cites in author-year form: p17 reads *"There also exist test cases and metrics for
  evaluating LLMs according to dimensions of trustworthiness (Huang et al. 2024)"*, and that reference
  entry is the TrustLLM paper. Searching for the work's name alone would have produced a false
  correction here, which is the mirror image of the NICT miss above.

The **four Google Patents links** on `opensource.html` are still unreachable, and the reason matters.
`patents.google.com` returns 503 to every automated request from this host, a rate limit rather than a
missing page, so a human visitor most likely sees the patents fine. Their 49-patent figure does not
rest on them in any case; it was verified in the 2026-08-13 round from named assignees.

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

### Phase B Follow-Up: the Remediation Candidates Were Verified

The six remediation lanes left 258 candidates that had never been through fetch-and-verify. Five Codex
units took 180 of them, the whole T0 through T5 range, and returned **NEW 87, MIRROR 18,
ALREADY-COUNTED 4, TOPIC-ONLY 43, UNVERIFIABLE 25, DROP 3**. Per-unit results are kept at
`skills/news-search/scratch/2026-08-30/phase-b-verification/`.

**These 87 are verified but not yet placed as ledger rows, so every published count is unchanged.**
Ledger 1 stays at 37 and the total at 582. Placing them is the next round's first task, and it is
mostly Ledger 3 and Ledger 7 work: only one candidate reaches Tier 0.

What the verification changed:

- **One Tier 0.** The OECD.AI Catalogue of Tools and Metrics for Trustworthy AI carries a record for
  `anomaly-detection-resources`, published 2023-12-11, whose `githubLink` field is
  `https://github.com/yzhao062/anomaly-detection-resources`. An intergovernmental catalogue listing,
  on the precedent of row 16 (India TEC) and row 2c (Japan MoD), both of which count a body naming the
  tool in an official resource. The work is a curated reading list rather than a library, which is
  weaker than the other Tier 0 rows and should be annotated as such when the row is written.
- **A pharma-adoption surface the audit had never seen.** 21 records show industry running TDC in their
  methods: Schrodinger DeepAutoQSAR, Janssen / Johnson & Johnson, Bayer, Recursion (Nature
  Communications), AstraZeneca R&D, Genentech Safety Assessment, Ersilia, China's National Institutes
  for Food and Drug Control, and Ildong Pharmaceutical. Spot-checked against the primary source: Bayer's
  paper reads *"made accessible for benchmarking via Therapeutics Data Commons (TDC). To access the
  data 'PyTDC' (v0.4.1) is used with the group 'Caco2_Wang'"*. This is the surface the completeness
  critic predicted would be invisible, because the TDC paper of record carries no arXiv identifier.
- **Security venues opened for the first time.** Three USENIX Security 2025 papers, one NDSS 2026 paper,
  and a Security BSides Las Vegas 2025 talk. One USENIX paper states *"We used PyOD [78] to implement a
  base KNN with neighbors of 5 and leaf size of 30."*
- **A lead that did not survive.** The GOV.UK London Borough of Sutton record was reported as a
  remediation lane's strongest find. Phase B resolved it MIRROR: it is already Ledger 1 row 9. That is
  the whole reason candidates may not be counted before verification.

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
| PyOD 2.0 | **OpenAI Careers**, "Quantitative Threat Forecasting Analyst" | Qualifications block: *"Expertise with modern toolchains, NumPyro, TensorFlow Probability, PyMC, Darts, GluonTS/Chronos, sktime, **PyOD 2.0**, River, scikit-survival, and readiness to evaluate emerging libraries as the field evolves."* A **second, distinct** OpenAI posting naming PyOD, separate from #8g, and a stronger form: it pins a major version and places PyOD inside a named toolchain a hire is expected to already know. Live URL now 403s and the role is absent from the live Ashby feed (750 postings checked), but two Wayback captures of the canonical `openai.com` URL return HTTP 200. Committed sidecar at [`news-snapshots/openai-careers-quantitative-threat-forecasting-analyst-2025-08-10.md`](../news-snapshots/openai-careers-quantitative-threat-forecasting-analyst-2025-08-10.md). |
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

## Change Log, May 2026

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
