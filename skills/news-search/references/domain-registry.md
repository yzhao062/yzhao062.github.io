# Domain Registry

Seed domains by source class. Phase A queries fan out to seeded domains in addition to the open dragnet, never instead of it. The registry is a recall floor, not a filter.

The registry is grown from each round's confirmed hits (see "Post-Round Harvest" in `SKILL.md`). Once a quarter, run a registry-disabled pass to surface outlet classes the registry has not seen yet.

## Class to outlet_class Field Value

The leftmost column gives the value Phase A writes to the `outlet_class` field of each candidate (see `references/candidate-schema.md`).

## Government / Policy PDFs (`gov-pdf`)

Highest priority for Tier 0 evidence. PDFs hosted at these domains are routinely missed by general web search; use Dimension 8 directly.

| Domain | Notes |
|---|---|
| dod.gov | DoD CDAO Generative AI RAI Toolkit lists PyOD and TrustLLM. |
| nist.gov | NIST AI RMF, AI 600-series. NIST AI 100-2e2025 cites TrustLLM. |
| nvlpubs.nist.gov | NIST special publications PDF host. |
| congress.gov | Bills, committee reports, hearings. |
| senate.gov | Senate committee report PDFs (HSGAC TrustLLM citation). |
| house.gov | House committee report PDFs. |
| crsreports.congress.gov | Congressional Research Service. |
| gao.gov | GAO accountability reports. |
| whitehouse.gov | Executive orders, OMB memos, OSTP reports. |
| federalregister.gov | RFIs, rules. |
| nsf.gov | NSF announcements, dear colleague letters, program solicitations, awards (path /awardsearch). |
| energy.gov | Department of Energy publications front-end. |
| osti.gov | DOE / national lab technical reports. |
| cisa.gov | Weekly Vulnerability Summary bulletins carry `vendor--product` rows; SB26-201 names `yzhao062--pyod`. **Method note:** the site search endpoint is a JavaScript shell and returns nothing to a fetcher, but bulletin pages at `/news-events/bulletins/sbYY-NNN` are server-rendered and fetch cleanly with browser headers. Bulletin text is compiled from NVD, so treat hits as mirrors of an NVD record rather than as independent citations. Added 2026-08-09. |
| regulations.gov | Federal dockets and public comments; also `downloads.regulations.gov` and `api.regulations.gov` for attachment text. NIST-2025-0035 (CAISI RFI) swept 2026-08-09. Added 2026-08-09. |

## EU and International Government (`eu-gov`, `intl-gov`)

`eu-gov`:

| Domain | Notes |
|---|---|
| europa.eu | EU AI Act, EU AI Office. |
| ec.europa.eu | European Commission policy documents. |
| enisa.europa.eu | ENISA cybersecurity reports. |

`intl-gov`:

| Domain | Notes |
|---|---|
| oecd.ai | OECD AI Policy Observatory. |
| oecd.org | OECD reports. |
| internationalaisafetyreport.org | International AI Safety Report (cites TrustLLM). |
| gov.uk | UK government AI papers. |
| aisi.gov.uk | UK AI Safety Institute. |
| canada.ca | Canadian federal AI documents. |
| imda.gov.sg | Singapore IMDA Model AI Governance Framework. |

## EU Research Projects (`eu-research-project`)

EU Horizon and Framework Programme deliverables are PDFs hosted on project sites or aggregators. They cite open-source tools by name (PyOD, TODS) in toolkit descriptions. Discovered this round via SEDIMARK D3.1 p.18.

| Domain | Notes |
|---|---|
| cordis.europa.eu | EU research project metadata, deliverable links. |
| zenodo.org | Open-access repository for EU project deliverables. |
| sedimark.eu | SEDIMARK project (cites PyOD in D3.1 p.18). |
| swforum.eu | EU software-engineering project consortium pages. |

## Patents (`patent`)

Patents citing tool names appear via Google Patents and WIPO. Discovered this round via Actimize patent US20230267468A1 citing PyOD.

| Domain | Notes |
|---|---|
| patents.google.com | Google Patents full-text search and citation links. |
| patentscope.wipo.int | WIPO global patent database. |
| uspto.gov | USPTO patent search and PAIR. |

## China Tech Media (`china-tech-media`)

Editorial Chinese-language coverage of arXiv preprints. Distinct from machine-translated aggregators (which go in `ai-aggregator`). Discovered this round via Sina / 机器之心Pro DoxBench feature.

| Domain | Notes |
|---|---|
| sina.com.cn | Sina news (hosts 机器之心Pro and other tech media). |
| jiqizhixin.com | 机器之心 (Synced China). Editorial. |
| 36kr.com | 36氪 startup and tech media. |
| infoq.cn | InfoQ China. |
| paperweekly.site | PaperWeekly (curated paper highlights). |
| csdn.net | CSDN developer community. |
| zhihu.com | Zhihu Q&A platform; tool tutorials. |
| leiphone.com | 雷锋网 (Lei Feng Net). |

## Security Research Blogs (`security-blog`)

Vendor and independent security research blogs that publish original analyses naming tools or papers. Distinct from generic security press (which goes in `tier1-security-press`) and AI-generated security catalogs (which go in `ai-aggregator`).

| Domain | Notes |
|---|---|
| huntress.com | Huntress security research. |
| snyk.io | Snyk vulnerability research. |
| hiddenlayer.com | HiddenLayer ML security. |
| promptfoo.dev | Promptfoo prompt-injection research. |
| raxelabs.com | RAXE Labs RADAR. |
| protectai.com | Protect AI ML security research. |
| paloaltonetworks.com | Unit 42 threat research. |

## AI-Generated and Aggregator Sites (`ai-aggregator`)

Sites that auto-generate or auto-aggregate content about arXiv papers. Hard cap at Tier 3 by Phase B. See `references/disclaimer-patterns.md` for detection patterns.

| Domain | Notes |
|---|---|
| papers.cool | Cool Papers (auto-aggregated arXiv summaries). |
| chatpaper.com | ChatPaper (LLM-summarized papers). |
| goatstack.ai | GoatStack newsletter (auto-curated). |
| alphaxiv.org | alphaXiv (community + auto layer). |
| sectools.tw | SecTools.tw (本文由 AI 產生 disclaimer). |
| paperdigest.org | PaperDigest. |

## Tier 1 Press (`tier1-tech-press`, `tier1-security-press`, `tier1-business-press`)

The existing `outlet-registry.md` covers these in full. Cross-reference: that file lists all Tier 1 domains by category; this file gives Phase A a per-class outlet_class tag for the candidate record.

## Foundation Model Companies (`foundation-model`)

System cards and safety reports cite benchmarks like TrustLLM directly. Tier 0 if cited by name.

| Domain | Notes |
|---|---|
| openai.com | OpenAI system cards, preparedness framework. |
| anthropic.com | Anthropic model cards, RSP, safety reports. |
| deepmind.google | Google DeepMind technical reports. |
| ai.meta.com | Meta AI Llama documentation. |
| mistral.ai | Mistral model documentation. |
| x.ai | xAI Grok system cards. |
| cohere.com | Cohere model cards. |
| microsoft.com | Named in the SKILL.md D8 list but absent from this table until 2026-08-09. Added 2026-08-09. |
| docs.aws.amazon.com | Amazon / AWS model documentation; also named in D8 but previously unseeded. Added 2026-08-09. |
| developers.google.com | Google Health AI Developer Foundations; hosts the TxGemma pages that name TDC. Added 2026-08-09. |
| storage.googleapis.com | CDN host for DeepMind model cards and Frontier Safety Framework reports (the TxGemma report lives here). The registry previously listed only `deepmind.google`. Added 2026-08-09. |
| arxiv.org | Several foundation-model technical reports publish here rather than on the company domain (Amazon Nova, Mistral Shieldstral). Added 2026-08-09. |

## Web Archive (`web-archive`)

Wayback is a discovery route, not only a fallback. Careers pages and press pages are pulled when roles close or sites reorganize, and a canonical first-party URL captured by the Internet Archive is first-party evidence. The 2026-08-09 flagship Tier 0 row (OpenAI "Quantitative Threat Forecasting Analyst" naming PyOD 2.0) exists only because of two Wayback captures.

| Domain | Notes |
|---|---|
| web.archive.org | Snapshot host. Fetch a capture at `/web/<timestamp>/<url>`. Added 2026-08-09. |
| web.archive.org/cdx/search/cdx | CDX index API. **Query this before concluding that no archive exists.** The 2026-05-07 note on the OpenAI #8g row claimed OpenAI's bot policy makes its careers pages unarchivable from any client; CDX shows two clean HTTP 200 captures of a sibling careers URL from July and August 2025. Added 2026-08-09. |

## Consulting and Analyst Firms (`analyst`)

A confirmed-hit class with no registry entry until 2026-08-09. Analyst and consulting reports are the surface where a governance framework gets named for enterprise buyers, so a hit here carries different weight than a press mention. Beware the registered Forrester AEGIS collision.

| Domain | Notes |
|---|---|
| deloitte.com | Deloitte Germany AIxAML is an existing confirmed hit, already recorded under ecosystem evidence. Added 2026-08-09. |
| forrester.com | Publishes its own "AEGIS" enterprise-guardrails framework. Any AEGIS hit here needs the arXiv:2603.12621 disambiguator. Added 2026-08-09. |
| gartner.com | Agent-governance and enterprise-coding-agent reports. No FORTIS naming found as of 2026-08-09. Added 2026-08-09. |
| idc.com | Not yet swept. Added 2026-08-09. |

## Thesis and Dissertation Repositories (`thesis-repository`)

New class, 2026-09-22. The first round to sweep this surface returned 28 confirmed items from 33
candidates, so the recall cost of leaving it unregistered was high. This table registers 37 hosts:
five cross-national aggregators, which come first because a single query there reaches many
institutions, and 32 individual repositories. Those 32 are the repositories a confirmed item came
from, not the whole population worth querying. A clean sweep of this table is therefore not a clean
sweep of the surface. Two access patterns recur: Cloudflare challenges (Cal State, TDX) and Anubis
proof-of-work challenges (Kiel, Tampere). A DSpace 7 REST path,
`/server/api/core/bitstreams/<uuid>/content`, walked past one AWS WAF challenge where the web UI
did not.

| Domain | Notes |
|---|---|
| oatd.org, core.ac.uk, base-search.net, openaire.eu, ndltd.org | Cross-national aggregators; start here. NDLTD added 2026-09-22 after the first sweep ran without it. |
| diva-portal.org | Sweden. Added 2026-09-22. |
| tdx.cat, upcommons.upc.edu | Catalonia; TDX enforces Cloudflare. Added 2026-09-22. |
| theses.fr, hal.science | France; theses.fr carries several non-CS doctoral candidates named Yue Zhao. HAL is the national open archive and holds deposited theses that theses.fr does not index; it was missed by the first sweep and is unswept. Added 2026-09-22. |
| rcaap.pt, repositorio.ufu.br, repositorio.unicamp.br | Portugal and Brazil. Added 2026-09-22. |
| shodhganga.inflibnet.ac.in | India. Added 2026-09-22. |
| trove.nla.gov.au | Australia; OCR scans misread "good" as "PyOD". Added 2026-09-22. |
| hdl.handle.net | Handle resolver fronting many repositories. Added 2026-09-22. |
| dash.harvard.edu, escholarship.org, hammer.purdue.edu, vtechworks.lib.vt.edu, digitalcommons.fau.edu, digital.library.txst.edu, scholarworks.brandeis.edu, scholarworks.calstate.edu, researchdiscovery.drexel.edu | US institutional repositories with confirmed hits. Added 2026-09-22. |
| ora.ox.ac.uk, norma.ncirl.ie | UK and Ireland. Added 2026-09-22. |
| macau.uni-kiel.de, media.suub.uni-bremen.de, repositum.tuwien.at, studenttheses.uu.nl, aaltodoc.aalto.fi, trepo.tuni.fi, researchportal.tuni.fi, dspace.cuni.cz | Continental Europe; Kiel and Tampere use Anubis anti-bot challenges. Added 2026-09-22. |
| open.uct.ac.za, research.sabanciuniv.edu, digital.car.chula.ac.th | Africa and Asia. Added 2026-09-22. |

## MCP Registries and Agent-Skill Marketplaces (`mcp-registry`)

New class, 2026-09-22. Agent tooling now has its own distribution surfaces, and the FORTIS
over-privilege benchmark targets agent skills directly, so a listing here is on-topic rather than
incidental. The first sweep found PyOD on two of them and clean zeros everywhere else.

| Domain | Notes |
|---|---|
| hvtracker.net | HVTrust registry; scored a PyOD MCP server at 73.6, grade B. Confirmed hit. Added 2026-09-22. |
| mcpagentsmarket.com | Carries a PyOD agent-skill listing. Confirmed hit. Added 2026-09-22. |
| mcp.so, mcpservers.org, smithery.ai, glama.ai, pulsemcp.com, cursor.directory | Swept 2026-09-22, no FORTIS work. Smithery and Glama both carry unrelated projects named Aegis and agent-audit. Added 2026-09-22. |
| modelcontextprotocol.io | The specification and the official servers repository; clean zero, and the security addenda are worth re-checking each revision. Added 2026-09-22. |

## Gap Domains Added 2026-09-22

These already carried counted ledger rows and were missing from this file anyway, which is its own
finding about the harvest step.

| Domain | Class | Notes |
|---|---|---|
| soumu.go.jp | intl-gov | Japan's Ministry of Internal Affairs and Communications. Ledger 1 row 21. |
| ai.mil | gov-pdf | DoD CDAO. Ledger 1 rows 2 and 2b. Akamai-protected; the Wayback Machine serves it. |
| sdaia.gov.sa | intl-gov | Saudi Data and AI Authority. Ledger 1 row 10. Serves fine to an ordinary browser User-Agent. |
| pmc.ncbi.nlm.nih.gov | academic-repository | A repository rather than an outlet. Tier the journal, never the host. |
| readthedocs.io | code-ecosystem | Documentation hosting; tier the project, never the host. |

## Adding New Entries

When a confirmed Phase B hit comes from a domain not in the registry:

1. Decide its class. If no class fits, create one (lowercase-hyphenated name).
2. Append a row under that class with a short note that anchors the round when it was added.
3. Commit the registry change with the audit. Future Phase A runs will seed queries against the new domain by default.

This is the post-round harvest step. Without it the registry freezes; with it, recall improves monotonically across rounds.

## Domains Added 2026-10-02

Domains first confirmed in this run. Keep the document-level tier, authorship and duplicate checks when reusing these seeds.

### Education and Research Repositories

| Domain | Verified Example |
|---|---|
| viterbischool.usc.edu | [AI Location Bias, AI Missing Vocal Clues: USC Viterbi and USC Stevens at ICML 2026](https://viterbischool.usc.edu/news/2026/07/ai-location-bias-ai-missing-vocal-clues-usc-viterbi-and-usc-stevens-at-icml-2026/); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| webthesis.biblio.polito.it | [Unsupervised Anomaly Detection on Multivariate Time Series in an Oracle Database](https://webthesis.biblio.polito.it/27687/1/tesi.pdf); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| thesis.unipd.it | [Machine Learning approaches for Anomaly Detection in Industrial IoT scenarios](https://thesis.unipd.it/retrieve/f471966e-c42e-49f1-b3ac-0fd2520a0b9c/Convento_Enrico.pdf); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| sites.usc.edu | [IETC Retreat – USC Institute on Ethics and Trust in Computing](https://sites.usc.edu/ietc/ietc-retreat/); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| theses.liacs.nl | [Adaptive Data Profiling with ML-Based Quality Checks for ETL Pipeline Quality and Cost Optimization](https://theses.liacs.nl/pdf/2025-2026-KomeiliZadehKKoorosh.pdf); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| edoc.ub.uni-muenchen.de | [Adaptive Exploration of Intrinsic Data Properties for Clustering, Outlier Detection, and Dimensionality Reduction](https://edoc.ub.uni-muenchen.de/35154/1/Qian_Li.pdf); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| tdr.lib.ntu.edu.tw | [Enhanced Anomaly Detection: A Comprehensive Ensemble Approach Using Over 100 Models (增強型異常檢測：使用超過100 個模型的綜合集成方法)](https://tdr.lib.ntu.edu.tw/bitstream/123456789/94149/1/ntu-112-2.pdf); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| mavmatrix.uta.edu | [AI for Life Sciences: From Geometric Protein Modeling to Multimodal Drug Design](https://mavmatrix.uta.edu/cgi/viewcontent.cgi?article=1014&context=cse_dissertations2); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| scholarworks.aub.edu.lb | [A Reinforcement Learning and Time Series Forest Based Model Selection for Unsupervised Anomaly Detection Techniques in Time Series Electricity Consumption](https://scholarworks.aub.edu.lb/bitstreams/fedae00b-b6f4-4359-b4d1-86f7cb305d3a/download); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| arno.uvt.nl | [Detecting Purchases as Anomalies: Using Anomaly Detection Methods for Classifying and Predicting Purchasing Intent in Clickstream Data of a Fashion E-Commerce Site](http://arno.uvt.nl/show.cgi?fid=158081); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| kiss.resources.caltech.edu | [Detecting the Unexpected: An Introduction to Anomaly Detection Methods](https://kiss.resources.caltech.edu/uploads/2026/09/technosignatures-wagstaff.pdf); verified 2026-10-02. Source class does not establish editorial independence or deployment. |

### Community, Industry, and Research Resources

| Domain | Verified Example |
|---|---|
| emergentmind.com | [Emergent Mind: Persona Query Benchmark Topics](https://www.emergentmind.com/topics/persona-query-benchmark); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| github.com | [Awesome Agentic Workflow Optimization](https://github.com/IBM/awesome-agentic-workflow-optimization/blob/main/README.md); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| themoonlight.io | [[Literature Review] From Selection to Generation: A Survey of LLM-based Active Learning](https://www.themoonlight.io/en/review/from-selection-to-generation-a-survey-of-llm-based-active-learning); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| dev.to | [Ways Devs Are Plugging LLMs Into Anomaly Detection - DEV Community](https://dev.to/lovestaco/ways-devs-are-plugging-llms-into-anomaly-detection-1b3o); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| towardsdatascience.com | [From FOMO to Opportunity: Analytical AI in the Era of LLM Agents &#124; Towards Data Science](https://towardsdatascience.com/from-fomo-to-opportunity-analytical-ai-in-the-era-of-llm-agents/); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| note.com | [Can AI Think "What If"? — The Frontier of Counterfactual Reasoning in Large Language Models｜laughman-ai](https://note.com/betaitohuman/n/nf47d88b7ffeb); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| prtimes.jp | [SyntheticGestalt、分子AIモデル「ZAO」「KOYA」を提供開始 &#124; SyntheticGestalt株式会社のプレスリリース](https://prtimes.jp/main/html/rd/p/000000019.000123750.html); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| guides.beeksgroup.com | [Scalable Unsupervised Outlier Detection (SUOD)](https://guides.beeksgroup.com/glossary/Scalable-Unsupervised-Outlier-Detection-(SUOD).html); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| python.plainenglish.io | [3 Methods to Solve Your Data Quality Problem Using Python &#124; by Sarah Floris &#124; Jun, 2022 &#124; Python in Plain English](https://python.plainenglish.io/3-methods-to-solve-your-data-quality-problem-using-python-931878204a64); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| medium.com | [Handbook of Anomaly Detection: (11) XGBOD](https://medium.com/dataman-in-ai/handbook-of-anomaly-detection-11-xgbod-d86dea6c5342); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| datalawgy.substack.com | [What is new in data, technology & digital laws? - A weekly overview](https://datalawgy.substack.com/p/what-is-new-in-data-technology-and-02e); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| reddit.com | [[R] Diffusion Models: A Comprehensive Survey of Methods and Applications](https://www.reddit.com/r/MachineLearning/comments/xhpu00/r_diffusion_models_a_comprehensive_survey_of/); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| itransition.com | [Anomaly Detection Services & Solutions](https://www.itransition.com/machine-learning/anomaly-detection); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| rubythalib.ai | [Tutorial PyOD: Deteksi Anomali dan Outlier dengan Python](https://rubythalib.ai/en/articles/tutorial-pyod-deteksi-anomali-dan-outlier-dengan-python); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| news.guthlabs.ai | [MetaPersona paper links synthetic populations to empirical social-science studies](https://news.guthlabs.ai/articles/metapersona-paper-links-synthetic-populations-to-empirical-social-science-studies-66899172); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| aicoder.com | [CUA-SWE Unifies Computer-Use Agents and Visual Software Engineering: Multimodal Code-GUI Benchmarking Redefines Debugging — AICoder](https://aicoder.com/news/news-20261001-cua-swe-computer-use-visual-software-engineering); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| cctest.ai | [CUA-SWE Evaluates Software Agents That Can See and Act - CCTest](https://cctest.ai/en/articles/cua-swe-brings-computer-use-agents-into-the-software-engineering-loop); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| paperpulse.ukurup.com | [PaperPulse Daily Summary - September 18, 2026](https://paperpulse.ukurup.com/summary/2026/09/18/daily-summary.html); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| youtube.com | [Putting AI to the test - Episode 4 &#124; Can AI solve a jigsaw? - YouTube](https://www.youtube.com/shorts/NrcLRd1nTaY); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| sues.fun | [ScholarPulse 日报 2026-07-09 &#124; Jones Ray](https://sues.fun/pulse/2026-07-09/); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| puzzlebyrinth.com | [Li et al.: Measuring Whether AI Really Sees Shape, via Jigsaw Puzzles — Fukai Reads &#124; Puzzlebyrinth（パズルラビリンス）](https://puzzlebyrinth.com/de/articles/paper-li-jigshape); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| llm-hacking.com | [Do prompt-injection attacks survive a real RAG pipeline? — LLM-Hacking](https://www.llm-hacking.com/hacks/prompt-injection-survival-realistic-rag.md/); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| bigdataieee.org | [IEEE Big Data Cup 2026](https://bigdataieee.org/BigData2026/cup/); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| mountaintheory.ai | [The Third State &#124; Mountain Theory](https://mountaintheory.ai/the-third-state/); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| mindpattern.ai | [CatchBench Scores 72 Auditors Across 1,187 Configs and Publishes 71 of 118 Contrasts as Unresolved Rather Than Ranked &#124; MindPattern](https://mindpattern.ai/f/22077); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| neurosnap.ai | [ADMET-AI - Predict ADMET properties of small molecules &#124; Neurosnap](https://neurosnap.ai/how-to-use/ADMET-AI); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| nomitech.com | [Benchmark Outlier Detection: Enterprise AI Model Choice](https://www.nomitech.com/benchmarking/benchmarking-outlier-detection-enterprise-ai); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| intuitionlabs.ai | [Fine-Tuning Foundation Models for Pharmaceutical R&D](https://intuitionlabs.ai/articles/fine-tuning-foundation-models-pharma-rd); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| skillsdirectory.com | [My Router (Grade A) - Claude Skill &#124; Skills Directory](https://www.skillsdirectory.com/skills/yzhao062-my-router-anywhere-agents); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| dcai.csail.mit.edu | [Class Imbalance, Outliers, and Distribution Shift - Introduction to Data-Centric AI](https://dcai.csail.mit.edu/2024/imbalance-outliers-shift/); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| books.google.com | [Time Series Analysis with Python Cookbook: Practical recipes for exploratory data analysis, data preparation, forecasting, and anomaly detection](https://books.google.com/books/about/Time_Series_Analysis_with_Python_Cookboo.html?id=7RB1EAAAQBAJ); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| analyticsvidhya.com | [Different Techniques of Anomaly Detection - Analytics Vidhya](https://www.analyticsvidhya.com/blog/2023/01/learning-different-techniques-of-anomaly-detection/); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| charstring.tistory.com | [Char :: 에이전트 AI - AgentOps 보안 정적 분석 Agent Audit](https://charstring.tistory.com/2285); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| libraries.io | [@eshaank08/agentcheck 0.1.2 on npm - Libraries.io - security & maintenance data for open source software](https://libraries.io/npm/@eshaank08%2Fagentcheck); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| zenovel.com | [AI in Drug Discovery (2026): What Pharma Leaders Must Know Now](https://zenovel.com/how-artificial-intelligence-is-transforming-drug-discovery-in-2026/); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| vibesecadvisory.com | [Shadow-Mode Traces Before AI Agent Write Access &#124; VibeSec Advisory](https://vibesecadvisory.com/blog/shadow-mode-traces-before-agent-write-access/); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| qiita.com | [PyODライブラリで、異常値（外れ値）の検出 #pyod - Qiita](https://qiita.com/amber27182818/items/4c5c1db24f4ddc48285a); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| cloud.tencent.com | [14种数据异常值检验的方法！-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/2013353); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| kaggle.com | [Outlier Detection in Python using PyOD Library &#124; Kaggle](https://www.kaggle.com/code/taruntiwarihp/outlier-detection-in-python-using-pyod-library); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| skills.rest | [pytdc: Load TDC datasets and benchmarks for drug discovery machine learning &#124; skills.rest](https://skills.rest/skill/pytdc-felixboehm); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| tam5917.hatenablog.com | [Pythonの異常検知パッケージPyODのフォーマットに従って、カーネル密度推定に基づく異常検知を実装した - 備忘録](https://tam5917.hatenablog.com/entry/2021/08/09/203647); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| slowsteadystat.tistory.com | [PyOD 라이브러리로 간단하게 이상치 탐지하기](https://slowsteadystat.tistory.com/25); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| dadev.tistory.com | [Best Anomaly Detection Library : Kats, ARUNDO-ADTK, PyOD, Luminaire - Dev. DA](https://dadev.tistory.com/entry/Best-Anomaly-Detection-Library); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| daewonyoon.tistory.com | [[번역&#124;SO] 시계열데이터의 이상탐지를 위한 패키지](https://daewonyoon.tistory.com/289); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| studysmarter.fr | [Valeurs aberrantes: Détection & Analyse &#124; StudySmarter](https://www.studysmarter.fr/resumes/informatique/fintech/valeurs-aberrantes/); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| talks.python.org.br | [Detectando Anomalias no Mundo Real com IA :: Python Brasil 2024 :: pretalx](https://talks.python.org.br/pythonbrasil-2024/talk/SDYLT3/); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| ibsec.com.br | [10 Práticas Comprovadas para Detectar e Prevenir Exfiltração de Dados em Ambientes de Nuvem &#124; IBSEC](https://ibsec.com.br/10-praticas-para-prevenir-exfiltracao-de-dados-em-ambientes-de-nuvem/); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| smarterarticles.co.uk | [When the Machine Lies: Building Defences Against AI's Most Dangerous Flaw](https://smarterarticles.co.uk/when-the-machine-lies-building-defences-against-ais-most-dangerous-flaw); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| clinicalbenchmarks.ai | [CHI-Bench results: 43 AI model rows &#124; Clinical Benchmarks](https://clinicalbenchmarks.ai/benchmarks/chi-bench); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| huggingface.co | [HydroSophyTech/ToxiMol-benchmark · Datasets at Hugging Face](https://huggingface.co/datasets/HydroSophyTech/ToxiMol-benchmark); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| informatik.uni-wuerzburg.de | [We Need to Rethink Benchmarking in Anomaly Detection](https://www.informatik.uni-wuerzburg.de/datascience/?cHash=58239fde74660e7474650e5293ee050e&tx_extbibsonomycsl_publicationlist%5Baction%5D=download&tx_extbibsonomycsl_publicationlist%5Bcontroller%5D=Document&tx_extbibsonomycsl_publicationlist%5BfileName%5D=We+Need+to+Rethink+Benchmarking+in+Anomaly+Detection.pdf&tx_extbibsonomycsl_publicationlist%5BintraHash%5D=6ba0f8197de45c41cd078beecc7c5a0d&tx_extbibsonomycsl_publicationlist%5BuserName%5D=dmir); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| andrewm4894.com | [Anomaly Detection Resources &#124; Andrew Maguire](https://andrewm4894.com/2021/01/03/anomaly-detection-resources/); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| mlcompendium.com | [Anomaly Detection &#124; Machine & Deep Learning Compendium](https://www.mlcompendium.com/predictive-ml/anomaly-detection); verified 2026-10-02. Source class does not establish editorial independence or deployment. |

### Academic Research

| Domain | Verified Example |
|---|---|
| biodatamining.biomedcentral.com | [Distinguishing cancer patients’ mild and severe symptoms in radiotherapy via zero-shot and few-shot large language model-based probabilistic prompts](https://biodatamining.biomedcentral.com/articles/10.1186/s13040-026-00547-z); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| openreview.net | [Revisiting "Edit Away and My Face Will not Stay: Personal Biometric Defense against Malicious Generative Editing"](https://openreview.net/forum?id=5Q1gr80AXU); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| doi.org | [Anonymization-Guided Latent Perturbation for Source-Identity Reduction with Limited Edit Deviation in Instruction-Guided Image Editing](https://doi.org/10.3390/s26196003); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| mdpi.com | [Streaming-Based Anomaly Detection in ITS Messages](https://www.mdpi.com/2076-3417/13/12/7313); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| academic.oup.com | [MCOD: a memory-constrained deep learning framework for robust outlier detection in quantitative proteomics](https://academic.oup.com/bib/article/27/5/bbag507/8836554); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| kdd-eval-workshop.github.io | [Reason Less, Verify More: Deterministic Gates Recover a Silent Policy-Violation Failure Mode in Tool-Using LLM Agents](https://kdd-eval-workshop.github.io/agenticai-evaluation-kdd2026/assets/papers/56_Reason_Less_Verify_More_Det.pdf); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| aclanthology.org | [RLHS: Mitigating Misalignment in RLHF with Hindsight Simulation](https://aclanthology.org/2026.findings-acl.556/); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| proceedings.mlr.press | [AnomSeer: Reinforcing Multimodal LLMs to Reason for Time-Series Anomaly Detection](https://proceedings.mlr.press/v306/zhang26aw.html); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| proceedings.neurips.cc | [An Evidence-Based Post-Hoc Adjustment Framework for Anomaly Detection Under Data Contamination](https://proceedings.neurips.cc/paper_files/paper/2025/hash/a3c1e6c8872aac5a445a821cdb523e70-Abstract-Conference.html); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| cydcampus.admin.ch | [Behavioral fingerprinting to detect ransomware in resource-constrained devices](https://www.cydcampus.admin.ch/dam/en/sd-web/8-cE1O8btVFX/Behavioral%20fingerprinting%20to%20detect%20ransomware%20in%20resource-constrained%20devices.pdf); verified 2026-10-02. Source class does not establish editorial independence or deployment. |

### Editorial Media

| Domain | Verified Example |
|---|---|
| drugdiscoverynews.com | [AI-Powered ADMET prediction: How machine learning is changing drug candidate selection &#124; Drug Discovery News](https://www.drugdiscoverynews.com/ai-powered-admet-prediction-how-machine-learning-is-changing-drug-candidate-selection-17356); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| kdnuggets.com | [10 Underappreciated Python Packages for Machine Learning Practitioners](https://www.kdnuggets.com/2021/01/10-underappreciated-python-packages-machine-learning-practitioners.html); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| aiweekly.co | [BlindBias Attacks Black-Box LLMs via Sampled Text Alone, 92.9% Fewer API Calls &#124; Found First &#124; AI Weekly](https://aiweekly.co/editors-blog/found-first-blindbias-attacks-black-box-llms-via-sampled-text-alone-92-9-fewer); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| newsweek.com | [Have Health Care’s AI Ambitions Hit a Reliability Wall?](https://www.newsweek.com/have-health-cares-ai-ambitions-hit-a-reliability-wall-12235130); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| news.qq.com | [德州农工大学团队打造AI修图神器：让图片编辑从“随便改改”到“精雕细琢”_腾讯新闻](https://news.qq.com/rain/a/20260211A0616600); verified 2026-10-02. Source class does not establish editorial independence or deployment. |

### Government and Policy

| Domain | Verified Example |
|---|---|
| bundesbank.de | [AnoMATE: Mixed-type Tabular Embeddings for Anomaly Detection](https://www.bundesbank.de/resource/blob/933522/8ab95aaef884a2817a91bcf6df0587ad/472B63F073F071307366337C94F8C870/2026-03-anomate-data.pdf); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
| foi.se | [Utredning av stödverktyg och metodik för utvärdering av AI-metoder](https://www.foi.se/rest-api/report/FOI-R--5453--SE); verified 2026-10-02. Source class does not establish editorial independence or deployment. |
