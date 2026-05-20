# News & Media Coverage Audit — Yue Zhao / FORTIS Lab

*Updated: 2026-05-19 (Full /news-search Full audit run: 8-lane parallel Phase A across D1-D8 → 166 unique candidates → 4-batch parallel Phase B verification → +21 verified ledger rows (0 Ledger 1, 0 Ledger 2, 7 Ledger 3, 13 Ledger 4, 1 Ledger 5) plus full citation-audit hook integration (39 Tier 0 + 207 Tier 1 institution-affiliation rows embedded from regenerated citation-affiliation-audit.md after two Dimensions DSL bug fixes: arXiv ID prefix, title_only search type). Highest-promise D4 lead OWASP Gen AI Q2 2026 Solutions Landscape PDF verified-negative on direct fetch. No new Tier 0 hits in D8 PDF deep search across 22 fresh PDFs. New disambiguation: Hangbo Zhao, Wei Zhao (SiriuS), AuditLuma, Moonshot Kiwi-do. Manual verification backlog: 11 entries flagged.)*
*Previous: 2026-05-13 (Claude independent wide 8-lane parallel news-search Phase A + Phase B, then Codex Round 1 review: +8 net new rows on top of Codex Phase A (0 unique Ledger 2 + 8 Ledger 3) plus 4 evidence upgrades to existing Ledger 2 rows after Codex caught 4 duplicate-URL candidates that the Phase A lane skip-list missed. Headline finds: Microsoft Research first-party publication listing names Yue Zhao with USC affiliation #26 on the TrustLLM page; thepaper.cn dedicated Chinese TrustLLM feature with verbatim arXiv link; TrustLLM 2026 mainstream-venue academic citation cluster confirmed via OpenAlex graph across ACS Env Sci Tech, Springer Requirements Engineering, ACM/IEEE HRI 2026, Wiley TIBR, Springer CCIS, Springer Frontiers of CS; Justin0504/Aegis third-party implementation cites arXiv 2603.12621 by name; first Russian-language Habr cluster (Otus, Garda, Rosatom); Japanese developer-blog expansion (codemajin, tam5917, Qiita); Juejin Chinese tutorial; mala-lab Awesome AD Foundation Models awesome list; aggregator paper-page cluster across HuggingFace Papers / DoxBench dataset / alphaxiv / papers.cool. Manual-verification outcomes 2026-05-13: Stanford HAI 2026 AI Index Responsible AI chapter dropped to verified-negative after the user confirmed the WebSearch snippet was a search-engine summarizer synthesis and the PDF does not name TrustLLM; aiproductivity.ai Aegis article and jiqizhixin.com TrustLLM feature verified by the user but recorded as evidence upgrades to existing rows #21 and #34b respectively (not new rows); Datawhale WeChat lecture by Yue Zhao (then CMU) added as new Ledger 3 #66dv; ACM Computing Surveys "Towards Trustworthy AI" review (doi:10.1145/3777382) folded into the #66do TrustLLM 2026 mainstream-venue cluster.)*
*Previous: 2026-05-13 (Codex Phase A wide news-search draft + Claude Phase B verification: +6 verified, +1 demoted Ledger 2 to Ledger 3, +2 source URLs dropped from inside cluster rows; PyShine covers agent-style, The Fintech Mag names PyOD as fintech fraud-detection alternative, Oracle FCCM product docs name PyOD/Yue Zhao (Oracle IoT half dropped after URL 404), RedTeams AI lists TrustLLM, PySAD docs integrate PyOD, non-English PyOD/ADBench cluster narrowed to Volcengine + GitCode + Sohu after Inferri 403 and Qiita duplicate of #42 Databricks Kakapo, Growth Japan CDCR-SFT moved to Ledger 3 after AI-generated disclaimer found on source page; topic-only May 2026 agent-security press added below).*
*Previous: 2026-05-07 (weekly parallel news-search skill sweep + Codex Round 1 review promotions: +34 verified items; MITRE LILAC cites TrustLLM, Google/DeepMind TxGemma uses TDC in official report/docs, OpenAI Careers names PyOD, Samsung SDS Korean editorial covers TrustLLM, Apache Beam / PostHog / MLflow / Genentech ship first-class PyOD integration code, gatodo newsletter covers CDCR-SFT, Wikipedia Anomaly detection lists PyOD, PyOD GitHub Dependents aggregate snapshot 5,493 repos + 139 packages; OpenAI/Anthropic/DeepMind system-card re-checks stayed negative).*
*Previous: 2026-04-29 (parallel news-search skill deep sweep: +12 verified items; DoD CDAO names PyOD as Production / High-maturity OOD tool with embedded workflow link, Sina / 机器之心Pro covers DoxBench, RAXE + Promptfoo cluster covers UCC paper (Ledger 2), plus tool and platform ecosystem additions; ledger placement refined same day after manual PDF + web verification of every new source; USC Viterbi ICLR roundup dropped — USC institutional PR for conference papers is out of scope).*
*Previous: 2026-04-24 (parallel 5-agent full sweep: +19 verified items; LLNL/DOE SafeAI report cites TrustLLM, Deloitte Germany PDF cites ADBench as industry evidence, plus platform/tool ecosystem additions).*
*Previous: 2026-04-22 (full-range parallel audit across 5 agents, plus targeted search — zero new verified third-party coverage; Stanford AI Index 2026 and 4 foundation-model system cards confirmed as negative after full-text PDF scan).*
*Previous: 2026-04-16 (5-day delta check — no new verified items; three D8 candidates flagged for next PDF pass).*
*Earlier: 2026-04-11 (targeted searches: agent-audit, Aegis, Auditable Agents, agent/LLM/VLM last-author works, DPU, Political-LLM, Treble, ADBench, Computing Resources, plus under-searched high-star tools).*
*All 8 core dimensions plus D9/D10 follow-up checks complete across all 124 items (105 papers + 19 tools).*
*Citation verification applied: every item names or cites the work, person, lab, or co-author.*

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
| 22 | agent-audit | SitePoint | Developer publication | "OpenClaw Security Audit Guide 2026" — links to agent-audit USC project page | 2026 | D4 | [Link](https://www.sitepoint.com/openclaw-security-audit-detecting-malicious-ai-agent-plugins/) |
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
| 54 | PyOD | **Platform** | CSDN -- 10+ Chinese-language tutorials |
| 55 | PyOD | **Platform** | Zhihu -- 4+ Chinese-language articles on PyOD |
| 56 | PyOD | **Platform** | Tencent Cloud developer -- Chinese PyOD tutorial |
| 57 | PyOD | **Platform** | aidoczh.com -- full Chinese translation of PyOD documentation |
| 58 | PyOD | **Platform** | Qiita -- Japanese PyOD tutorial |
| 59 | PyOD | **Platform** | ClassCat -- Japanese PyOD overview |
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
| 66q | PyOD | **Platform** | Korean: 3 tutorials (Tistory, JunPyoPark, DataNetworkAnalysis) |
| 66r | PyOD | **Platform** | Japanese: 4 additional sources (Codemajin, DataPowerNow, Scutum, TRYETING) |
| 66s | PyOD | **Platform** | German: 5 sources (ichi.pro, Hahn-Schickard/EmbedML, Konfuzio, Acervo Lima, KI Blog) |
| 66t | PyOD | **Platform** | Spanish: 2 tutorials (Aprende Machine Learning, Medium/Carlos Millan) |
| 66u | PyOD | **Platform** | Chinese: 智东西 (Zhidx) lecture preview, Bilibili video (9.3K+ views) |
| 66v | TrustLLM | **Platform** | Chinese: 专知 (Zhuanzhi) TrustLLM coverage |
| 66w | DoxBench | **Platform** | Liner.com quick review + Moonlight.io literature review |
| 66x | AD-AGENT | **Platform** | Moonlight.io literature review; later platform listings include aimodels.fyi and PT-Edge |
| 66y | MetaOOD | **Platform** | Liner.com quick review + aimodels.fyi paper details |
| 66z | JailDAM | **Platform** | aimodels.fyi paper details + Bohrium (Chinese academic platform) |
| 66aa | DPU | **Platform** | Moonlight.io literature review + paperreading.club |
| 66ab | Multiple (ICLR 2026) | **Platform** | Paper Digest ICLR 2026 highlights (DoxBench, TrustGen, DecAlign, FigEdit) |
| 66ac | Can MLLMs do TSAD? | **Platform** | alphaXiv discussion page |
| 66ad | DyFlow | **Platform** | Moonlight.io literature review + ChatPaper summary + alphaXiv overview |
| 66ae | FaceLock | **Platform** | Liner.com quick review + Moonlight.io literature review |
| 66af | CoAct | **Platform** | Moonlight.io literature review + aimodels.fyi paper details + Bytez viewer; Apr 29 pass added OpenTrain/HFEPX and DeepDyve pages |
| 66ag | Agent Banana | **Platform** | Moonlight.io literature review |
| 66ah | StealthRank | **Platform** | Moonlight.io literature review |
| 66ai | Defenses Against Prompt Attacks | **Platform** | alphaXiv overview page |
| 66aj | Can MLLMs do TSAD? | **Platform** | Emergent Mind editorial summary + Moonlight.io + aimodels.fyi (extends 66ac) |
| 66ak | Multimodal GEO | **Platform** | Emergent Mind topic page |
| 66al | agent-audit | **Platform** | Hacker News Show HN submission (item 46918149) — "Agent Audit: Open-source security scanner for AI agents" |
| 66am | ADBench | **Platform** | Zhihu: "异常检测--ADBench (NeurIPS'22) is ALL You Need" technical review |
| 66an | ADBench | **Platform** | Zhihu: "异常检测基准 Anomaly detection benchmark" overview |
| 66ao | ADBench | **Platform** | CSDN: benchmark/dataset/baseline collection listing ADBench |
| 66ap | ADBench | **Platform** | CSDN: "赵越-图神经网络与异常检测" GNN talk coverage naming Yue Zhao |
| 66aq | ADBench | **Platform** | Emergent Mind dedicated topic page (updated Feb 2026) |
| 66ar | ADBench | **Platform** | Kaggle notebook "anomaly detection using Adbench datasets" by valeriemokeira (Jan 2025) |
| 66as | ADBench | **Platform** | alphaXiv discussion page |
| 66at | DPU | **Platform** | GitHub Awesome-Out-Of-Distribution-Detection curated list (CVPR 2025 entry) |
| 66au | Treble | **Platform** | Moonlight.io literature review + alphaXiv overview |
| 66av | Treble | **Platform** | GitHub curated lists: Awesome-MLLM-Hallucination + Awesome-LVLM-Hallucination |
| 66aw | Political-LLM | **Platform** | alphaXiv (19 upvotes, 133 views) + aimodels.fyi paper summary |
| 66ax | Political-LLM | **Recognition** | SSRN Top Download Paper for Decision Science (1,327 downloads, 5,137 abstract views) |
| 66ay | Computing Resources | **Platform** | Hugging Face Papers page for arXiv:2510.13621 |
| 66az | Computing Resources | **Policy** | CVPR 2026 Compute Reporting Form — official policy pilot addressing same compute-transparency gap the paper quantified; discussed on LinkedIn by program chair Vladimir Pavlovic ([post](https://www.linkedin.com/posts/vladimir-pavlovic-a5528412_cvpr-2026-compute-reporting-form-author-activity-7384957217147457536-kd1X)), Sasha Luccioni ([post](https://www.linkedin.com/posts/sashaluccioniphd_cvpr-2026-compute-reporting-form-author-activity-7385993803515744256-uqM-)) |
| 66ba | PyGOD | **Platform** | Zhihu x3: dedicated intro article, GNN+AD talk coverage, BOND benchmark article (all name PyGOD) |
| 66bb | PyGOD | **Platform** | CSDN x5: dedicated PyGOD intro, GNN talk coverage, PyGOD+PyOD methods, JMLR tutorial, troubleshooting guide |
| 66bc | TODS | **Platform** | Zhihu x3: outlier type detection, open-source system intro, "powerful time series anomaly detection tool" recommendation |
| 66bd | TODS | **Platform** | Tencent Cloud Developer: detailed TODS tutorial with code examples (Jul 2021) |
| 66be | TODS | **Platform** | CSDN x2 + DongAI + GitCode + Explinks + Showapi: Chinese-language tutorials and overviews (2021-2025) |
| 66bf | combo | **Platform** | Zhihu: "combo: Python机器学习模型合并工具库简介" introduction (2019) |
| 66bg | combo | **Platform** | Tencent Cloud/Datawhale: full combo introduction + AAAI 2020 context (Dec 2019) |
| 66bh | combo | **Platform** | CSDN x2: combo library articles (2020, 2024) |
| 66bi | Anomaly-Detection-Resources | **Platform** | Zhihu: third-party recommendation article linking to repo |
| 66bj | Anomaly-Detection-Resources | **Platform** | CSDN x2: human-written survey referencing repo + PyOD tutorial linking resources |
| 66bk | CS-Paper-Checklist | **Platform** | CSDN: dedicated article "提升计算机科学论文质量的实用指南" |
| 66bl | CS-Paper-Checklist | **Platform** | Scholar's Corner (lujie.ac.cn): listed under "Academic Writing Tips" with direct repo link |
| 66bm | Cat-DPO | **Platform** | New arXiv aggregator and AI-news listings after Apr 22: alphaXiv, Bytez, Gist.Science, Moonlight, ResearchTrend.AI, AI Navigate, haebom/slashpage. |
| 66bn | Topology Matters | **Platform** | alphaXiv, Bytez, Moonlight, aimodels.fyi, ChatPaper, ResearchTrend.AI, and haebom/slashpage pages name the memory-leakage paper and Yue Zhao. |
| 66bo | Auditable Agents | **Platform** | alphaXiv, Bytez, Gist.Science, ResearchTrend.AI, Code of Paper, and haebom/slashpage pages name the paper and Yue Zhao. |
| 66bp | Aegis | **Platform** | Hugging Face Papers, Gist.Science, ResearchTrend.AI, PULRC Portal, DeepDyve, alphaXiv, Cool Papers, Skillget, and Hacker News Show HN pages name AEGIS and the tool-call firewall paper. |
| 66bq | DoxBench | **Platform** | Additional DoxBench coverage on Zhuanzhi, haebom/slashpage, Gist.Science, ResearchTrend.AI, ChatPaper, and Hugging Face Papers; Liner already recorded in 66w. |
| 66br | TrustGen | **Platform** | BAAI Community and CSDN pages name TrustGen, Yue Zhao, the project page, arXiv link, and GitHub repo. |
| 66bs | PyOD / PyOD 3 | **Platform** | SourceForge mirror, newreleases.io v3.0.0 release tracker, AitFind project page, LibHunt alternatives, DeepWiki docs, and OSSInsight comparison pages name PyOD/PyOD 3. |
| 66bt | agent-audit | **Platform** | Skillget listing, ClawHub Agent Audit Scanner listing, SoftwareSeni awesome-ai-agents list, MCP Market server/skill listings, PyPI, piwheels, and Safety DB name agent-audit as an AI-agent/MCP security scanner. |
| 66bu | agent-style / anywhere-agents | **Platform** | [Replicate Hype](https://hype.replicate.dev/?filter=past_week&sources=GitHub%2CHuggingFace%2CReddit%2CReplicate) Apr 22 trending page lists `yzhao062/agent-style` and `yzhao062/anywhere-agents`; ToolHunter later published an external tool directory/review for `agent-style`; package registries and docs remain first-party or registry-only. |
| 66bv | PersonaConvBench | **Platform** | alphaXiv, Hugging Face Papers, Bytez, Moonlight, aimodels.fyi, and ResearchTrend.AI pages name the personalized conversation benchmark. |
| 66bw | Defenses Against Prompt Attacks | **Platform** | Bytez, Moonlight, ResearchTrend.AI, J-GLOBAL, AI Security News, and AI Security Portal pages name the surface-heuristics prompt-attack paper; alphaXiv already recorded in 66ai. |
| 66bx | Mitigating Hallucinations via Causal Reasoning | **Platform** | alphaXiv, Bytez, aimodels.fyi, ChatPaper, ResearchTrend.AI, J-GLOBAL, and haebom/slashpage pages name the causal-reasoning hallucination paper. |
| 66by | AD-LLM / NLP-ADBench | **Platform** | alphaXiv, Bytez, Moonlight, ChatPaper, ResearchTrend.AI, J-GLOBAL, Hugging Face Papers, SelectDataset, PromptLayer, Papers With Code, BAAI Community, and aimodels.fyi pages name AD-LLM and/or NLP-ADBench. |
| 66bz | Secure On-Device Video OOD / SocialMaze / MGEO | **Platform** | alphaXiv, Bytez, Moonlight, aimodels.fyi, ChatPaper, ResearchTrend.AI, Hugging Face dataset, and ResearchTrend/MGEO pages name these 2025-2026 papers. |
| 66ca | Tool long tail | **Platform** | ADBench on Ecosyste.ms and Liner; TODS on Datahut, Context7, and Ecosyste.ms; TDC on AIPOCH; PyGOD on Cloudsmith, fxis.ai, Open Source Security Atlas, and Reddit r/MachineLearning; SUOD on Beeks/piwheels; combo on PythonFix, PyPIStats, Pepy, and conda-forge; TrustEval-toolkit on GitCode. |
| 66cb | ADBench | **Consulting** | [Deloitte Germany AIxAML PDF](https://www.deloitte.com/content/dam/assets-zone2/de/de/docs/services/consulting/2025/Deloitte-Compliance-AIxAML.pdf) cites Han et al. (2022), ADBench, as the source of an anomaly-detection figure in an anti-money-laundering transaction-monitoring solution. |
| 66cc | PyOD / TODS | **EU project** | SEDIMARK D3.1 (Energy efficient AI-based toolset for improving data quality, p.18) names PyOD and TODS as the Python libraries used for the SEDIMARK toolbox's outlier-detection module ("Outlier detection, implemented using python and building on libraries such as PyOD, tods, pythresh, pandas, scikit-learn, and river"); D5.2 also names the same libraries. EU Horizon Europe data-space project. |
| 66cd | PyOD | **Patent** | Actimize patent US20230267468A1 names Python Outlier Detection (PyOD) as a package usable for fraud/anomalous-transaction ML models. |
| 66ce | PyOD | **Tutorial / integration** | Code and Compile HiveMQ Edge-to-Cloud AI Pipeline uses PyOD `IForest`; PyCaret DeepWiki documents PyOD integration; Precision Federal, Ciencia de Datos, ProgmaticTech, and PyCon US 2026 tutorial pages also name or use PyOD. |
| 66cf | CS-Paper-Checklist | **Education / academic writing** | Stanford BIOMEDIN-212 scientific-writing slides link `yzhao062/cs-paper-checklist`; Sayed Mohsin Reza's May 2025 blog credits Dr. Yue Zhao and links the repo; SourcePulse also lists the project. |
| 66cg | The Autonomy Tax / Sovereign-OS | **Platform** | Gist.Science, ResearchTrend.AI, and DeepDyve pages name the 2026 agent-governance papers and Yue Zhao. |
| 66ch | IET / Fairness or Fluency? / Someone Hid It | **Platform** | Cool Papers, ChatPaper, GoatStack, and ResearchTrend.AI pages name these 2026 LLM evaluation, attribution, and retrieval-security papers with Yue Zhao. |
| 66ci | Auditable Agents | **Platform** | SecTools.tw 2.0 archive 713 ([link](https://sectools.tw/archives/713)) carries an "本文由 AI 產生、整理與撰寫" (AI-generated) disclaimer at the top and bottom; the page names "Auditable Agents", arXiv:2604.05485, and the full author list including Yue Zhao. Downgraded from initial Ledger 2 #36x placement on 2026-04-29 web verification. |
| 66cj | Agent Audit | **Platform** | SecTools.tw 2.0 archive 854 ([link](https://sectools.tw/archives/854)) carries the same "本文由 AI 產生、整理與撰寫" (AI-generated) disclaimer; the page names "Agent Audit: A Security Analysis System for LLM Agent Applications", arXiv:2603.22853, and the author list (Haiyue Zhang et al.; Yue Zhao not directly named on this page, but Haiyue Zhang is co-author). Downgraded from initial Ledger 2 #36z placement on 2026-04-29 web verification. |
| 66ck | LangSkills | **Academic / platform** | "Recipes for Agents: Understanding Skills and Their Open Questions" cites `LabRAI/LangSkills` as reference [32]; Safety DB and piwheels also list `langskills-rai`. |
| 66cl | PyOD / LSCP | **Patent** | US20230017157A1 (Flowhow / Ben-Gurion University medical-device protection) says 11 unsupervised anomaly detection algorithms were used, some implemented by the PyOD toolbox, and names LSCP among ensemble methods. |
| 66cm | PyOD / COPOD | **Patent** | WO2023192130A1 (Dun & Bradstreet semantic directions / entity targeting) names the open-source PyOD library, the `yzhao062/pyod` GitHub URL, LOF, COPOD, and the JMLR PyOD citation. |
| 66cn | PyOD | **Patent** | US12074893B2 (Visa user network activity anomaly detection; same family as US11711391B2 / WO2022082091A1) cites "PyOD: A Python Toolbox for Scalable Outlier Detection" in non-patent literature. |
| 66co | LSCP | **Patent** | CN111880983A/B (CAN bus anomaly detection, Beijing Topsec) cites Yue Zhao et al., "LSCP: Locally Selective Combination in Parallel Outlier Ensembles", as non-patent literature. |
| 66cp | PyOD / ECOD / COPOD | **Finance research / applied deployment** | Springer Nature Discover Data article "A hybrid framework of anomaly detection for mutual fund parent companies" uses four PyOD algorithms (KNN, ECOD, COPOD, IForest) in a Morningstar-linked mutual-fund parent-company anomaly-detection workflow. |
| 66cq | PyOD | **Audit workflow** | Syntora "Integrate AI Anomaly Detection into Your Audit Workflow" says its ledger anomaly-detection service would build a Python service using PyOD for Isolation Forest modeling. |
| 66cr | TrustLLM | **Academic citation cluster** | 2025-2026 downstream papers in npj Artificial Intelligence, Requirements Engineering, Engineering Applications of Artificial Intelligence, and npj Digital Medicine cite or discuss TrustLLM in trustworthiness / healthcare AI contexts. |
| 66cs | DoxBench | **Follow-on research / AI-assisted news** | ReasonBreak / "Disrupting Hierarchical Reasoning" evaluates on DoxBench for geographic privacy protection; AI CERTs News also names DoxBench and GeoMiner in a ChatGPT location-risk article, with an explicit AI-generated/assisted disclaimer. |
| 66ct | The Autonomy Tax | **Platform** | SecTools.tw archive 729 carries an AI-generated disclaimer and directly names "The Autonomy Tax: Defense Training Breaks LLM Agents", Shawn Li, Yue Zhao, arXiv:2603.19423, and DOI 10.48550/arXiv.2603.19423. |
| 66cu | PyOD / PyOD 2 | **Scientific uptake** | ACS Analytical Chemistry article "Unsupervised Machine Learning for Differential Analysis in Proteomics" uses PyOD version 2; the 2026 ACS comment on that paper says the reviewed UMLAD algorithms primarily come from PyOD 2 and cites the PyOD 2 WWW Companion paper. |
| 66cv | PyOD | **Education / training** | Additional course and syllabus pages from Python Charmers, Datastat, RX-M, and WUNU name PyOD or PyOD docs in anomaly-detection training contexts. |
| 66cw | TDC | **Education / platform** | Harvard AIM2 course project page, IntuitionLabs biotech evaluation guide, Hugging Face TDC mirror, and Emergent Mind topic page name Therapeutics Data Commons (TDC) as a dataset/benchmark resource. |
| 66cx | 2025-2026 paper long tail | **Platform** | Direct paper pages/reviews for DyFlow (Deep Paper), M3OOD (OSLLM.ai/Nemati), ClimateLLM (Moonlight), Mole-PAIR / molecular foundation model uncertainty (aimodels.fyi), model-extraction surveys (Moonlight / Cool Papers), graph foundation model extraction (Cool Papers), CDCR-SFT (Emergent Mind), and hurricane economic-loss prediction (Moonlight) name the relevant papers and/or Yue Zhao. |
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
| 66dm | PyOD / ADBench | **Non-English platform cluster** | May 13 sweep, kept after Claude verification: Volcengine PyOD industrial anomaly-detection article (names PyOD as "首选专门库"; Stack Exchange attribution footer marks partial aggregator), GitCode ADBench tutorial (human-authored tutorial, no AI disclaimer), Sohu UniOD article using ADBench datasets on 57 datasets (republished from PaperWeekly, partial aggregator). Dropped on verification: Inferri (HTTP 403 Forbidden, unverifiable) and Qiita / Databricks Japan tutorial (explicitly a translation of the Databricks Kakapo blog already counted as Ledger 3 #42). Codex May 13 Phase A, Claude Phase B verified 2026-05-13. [Volcengine](https://www.volcengine.com/article/123503) · [GitCode](https://blog.gitcode.com/bf8c3f9b2c0e352317dc95dcc3bd738b.html) · [Sohu](https://www.sohu.com/a/996242967_121119001) |
| 66dn | CDCR-SFT | **Templated daily-brief (AI-generated cap)** | "Mitigating Hallucinations in Large Language Models via Causal Reasoning" / CDCR-SFT / 95.33% CLADDER accuracy named in Growth Japan Technologies Japanese daily-brief ("ほぼテク" templated brief). Page carries verbatim AI-generated disclaimer "※）生成AIは、場合によって事実と異なる内容を含む可能性があります"; per `disclaimer-patterns.md`, `ai_generated` is capped at Tier 3. Moved from Codex Ledger 2 Phase A draft (originally proposed #36an) to Ledger 3 by Claude Phase B verification 2026-05-13. Complements the gatodo newsletter CDCR-SFT coverage already counted in Ledger 3 #66dd. [Link](https://www.growth-japan.com/blog/it-daily-brief-2026-0309) |
| 66do | TrustLLM | **2026 mainstream-venue academic citation cluster** | Six 2026 papers in Tier 1 venues cite TrustLLM (arXiv:2401.05561): ACS Environmental Science & Technology (Cheng et al., Apr 9 2026 -- LLM contaminants prioritization, doi:10.1021/acs.est.6c01342); Springer Requirements Engineering (Axetorn et al., Mar 16 2026 -- multi-agent LLM chatbot trust requirements, doi:10.1007/s00766-026-00457-w); ACM/IEEE HRI 2026 Companion (Seaborn & Yalcin, Mar 12 2026 -- Robotic Sycophancy scoping review, doi:10.1145/3776734.3794532); Wiley Thunderbird International Business Review (Shrivastav et al., Feb 12 2026, doi:10.1002/tie.70099); Springer CCIS (Danielienė et al., Jan 2026 -- Gen-AI for CISO tasks, doi:10.1007/978-3-032-16808-5_33); **ACM Computing Surveys** "Towards Trustworthy AI: A Review of Ethical and Robust Large Language Models" (doi:10.1145/3777382), a Tier 0-equivalent CS survey venue. Plus Springer Frontiers of Computer Science (s11704-025-50442-9) explicitly names TrustLLM in body. First six confirmed via OpenAlex citation graph 2026-05-13 (publisher pages variously 403-gated); ACM CSUR confirmed via user manual verification 2026-05-13. | 2026 | D6 | [OpenAlex](https://api.openalex.org/works?filter=referenced_works%3AW4390833061) · [ACM CSUR](https://dl.acm.org/doi/10.1145/3777382) |
| 66dp | Aegis | **Third-party implementation citing FORTIS paper** | Justin0504/Aegis GitHub repo "Runtime policy enforcement for AI agents. Cryptographic audit trail, human-in-the-loop approvals, kill switch. Zero code changes." README cites the FORTIS paper verbatim: "AEGIS: No Tool Call Left Unchecked -- A Pre-Execution Firewall and Audit Layer for AI Agents. Aojie Yuan, Zhiyuan Su, Yue Zhao. arXiv:2603.12621, 2026." Third-party implementation building on the USC work, distinct from the canonical FORTIS repo. Rule 1+3 met. Claude Phase B verified 2026-05-13. | 2026 | D7 | [Link](https://github.com/Justin0504/Aegis) |
| 66dq | PyOD / COPOD / ECOD / HBOS | **Russian Habr corporate-blog cluster** | Three independent Russian-language Habr corporate-blog articles cite PyOD by name (first Russian-language coverage in the audit): (a) Otus.ru (Russian online-education provider) translation of an Alexandra Amidon COPOD tutorial verbatim "COPOD реализован в пакете PyOD (https://github.com/yzhao062/pyod)"; (b) Garda (Makves senior ML Mikhail Vasilev) original Russian piece on HBOS and ECOD, cites the ECOD arXiv ID 2201.00382 and pyOD as the reference implementation; (c) Rosatom (Russian state nuclear corporation) corporate Habr blog naming PyOD as the specialized library for point-anomaly metrics. Rule 1+6 met for all three. Claude Phase B verified 2026-05-13. | 2021-2025 | D7 | [Otus](https://habr.com/ru/companies/otus/articles/570314/) · [Garda](https://habr.com/ru/companies/garda/articles/895148/) · [Rosatom](https://habr.com/ru/companies/rosatom/articles/687270/) |
| 66dr | PyOD | **Japanese developer blog expansion** | Three additional Japanese PyOD tutorials beyond the existing generic Qiita listing #58: (a) codemajin.net dedicated Japanese PyOD tutorial with verbatim github.com/yzhao062/pyod link; (b) tam5917.hatenablog.com personal blog implementing a PyOD-format KDE detector and linking pyod.readthedocs.io plus the repo; (c) Qiita PyOD tutorial by `amber27182818`, verbatim "Python Outlier Detection（PyOD）は、現在最も人気のあるPython異常検知ツールライブラリ". Expands the Japanese developer-community footprint. Claude Phase B verified 2026-05-13. | 2021-2026 | D7 | [codemajin](https://www.codemajin.net/anomaly-detection-with-pyod/) · [tam5917](https://tam5917.hatenablog.com/entry/2021/08/09/203647) · [Qiita amber27182818](https://qiita.com/amber27182818/items/4c5c1db24f4ddc48285a) |
| 66ds | PyOD / SUOD | **Juejin (掘金) Chinese developer community** | Juejin tutorial "【异常检测】一、介绍并安装使用Python异常检测工具箱pyod" verbatim clones `git clone https://github.com/yzhao062/pyod.git` and links to Yue Zhao's CMU SUOD paper PDF at `andrew.cmu.edu/user/yuezhao2/papers/21-mlsys-suod.pdf`. Rule 6 (canonical URL + author paper PDF) + Rule 2 (PI name on author PDF) met. Juejin is ByteDance's Chinese developer community. Claude Phase B verified 2026-05-13. | 2022 | D7 | [Link](https://juejin.cn/post/7110496036220567566) |
| 66dt | PyOD 2 | **mala-lab Awesome Anomaly Detection Foundation Models** | Curated awesome list `mala-lab/Awesome-Anomaly-Detection-Foundation-Models` (TKDE survey companion) names PyOD 2 explicitly with verbatim entry `[Chen2025] PyOD 2: A Python Library for Outlier Detection with LLM-powered Model Selection in Arxiv, 2025. [paper](https://arxiv.org/abs/2412.12154) [code](https://github.com/yzhao062/pyod)`. Rule 1+6 met. Claude Phase B verified 2026-05-13. | 2025 | D7 | [Link](https://github.com/mala-lab/Awesome-Anomaly-Detection-Foundation-Models) |
| 66du | TrustLLM / DoxBench / Auditable Agents / AEGIS / Agent Audit | **Aggregator paper-page cluster (May 13)** | Aggregator surfacing of recent FORTIS arXiv papers, kept at Tier 5 as weak platform-tail evidence (aggregator pages are capped at Tier 3 by `disclaimer-patterns.md`; we hold the conservative T5 floor): HuggingFace Papers TrustLLM page lists Yue Zhao with verbatim "26. University of Southern California" affiliation; HuggingFace Datasets DoxBench page Yue Zhao link points to `viterbi-web.usc.edu/~yzhao010/`; alphaxiv pages for 2604.05485 / 2603.12621 / 2603.22853; papers.cool pages for 2604.05485 (full author list including Yue Zhao) and 2603.12621. Aggregator pages do not advance tier but document coverage breadth. Claude Phase B verified 2026-05-13. | 2024-2026 | D7 | [HF TrustLLM](https://huggingface.co/papers/2401.05561) · [HF DoxBench](https://huggingface.co/datasets/MomoUchi/DoxBench) · [alphaxiv AA](https://www.alphaxiv.org/abs/2604.05485) · [alphaxiv AEGIS](https://www.alphaxiv.org/abs/2603.12621) · [papers.cool AA](https://papers.cool/arxiv/2604.05485) · [papers.cool AEGIS](https://papers.cool/arxiv/2603.12621) |
| 66dv | PyOD / anomaly detection | **Datawhale WeChat public-account lecture writeup** | "异常检测算法应用与实践_CMU赵越" -- Datawhale-organized online lecture by Yue Zhao (then-CMU affiliation) covering anomaly detection algorithms, applications, and practice. Datawhale is a major Chinese open-source ML / data-science community. Lecture writeup published via WeChat public account; sister-evidence to the Bilibili recording of the same talk. WeChat verification gate blocked WebFetch; user manually verified 2026-05-13 that the page names Yue Zhao and the PyOD anomaly-detection material. Treat as podcast / lecture-equivalent signal, similar shape to Talk Python To Me #497 (#40) and Real Python #208 (#41). Claude Phase B + user manual verification 2026-05-13. | 2021-2022 | D7 | [Link](https://mp.weixin.qq.com/s/BwMe9l9yEGSYgATbvcK97w) |

*Note: Nature Scientific Reports x3 ADBench scientific-uptake cluster (s41598-025-88050-z, s41598-024-72982-z, s41598-025-28976-6) demoted back to candidate pool in Codex Round 2 because the rows rested on WebSearch-snippet confirmation only; full-text fetch was Nature-IDP gated. Per the "snippet alone is not verified evidence" rule, awaiting direct article fetch before re-promotion.*

**Count: 154 ecosystem adoption items (141 prior + 5 earlier May 13 rows from Codex draft + 8 May 13 rows from Claude independent wide run, last of which is #66dv Datawhale lecture writeup unlocked via user manual verification 2026-05-13; ACM Computing Surveys "Towards Trustworthy AI" review folded into the existing #66do TrustLLM 2026 academic cluster, also via user manual verification)**

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

**Count: 6 first-party/community items**

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

**Count: 19 awards/recognitions/encyclopedia entries**

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

---

## Summary Statistics

| Ledger | Count |
|--------|-------|
| Government/Policy citations | 15 |
| External third-party media | 73 (71 prior + 2 May 13 rows verified by Claude 2026-05-13; 4 wide-run candidates were dropped as exact-URL duplicates of existing rows #5, #7, #21, #34b after Codex Round 1 review, and the May 13 verification work for those four URLs is recorded as evidence upgrades on those existing rows rather than new counted rows) |
| Ecosystem adoption | 154 (141 prior + 13 May 13 rows verified by Claude 2026-05-13; 5 from Codex Phase A draft and 8 from Claude independent wide run + manual-verified unlock) |
| First-party/community | 6 |
| Awards/recognitions | 19 |
| **Total verified items** | **267 (252 prior + 15 May 13 rows verified by Claude 2026-05-13, of which 1 ACM CSUR was folded into the #66do cluster via user manual verification and 1 Datawhale row was unlocked via user manual verification; 4 additional May 13 wide-run leads count as evidence upgrades on existing rows rather than new rows)** |

- **105 papers + 19 tools** searched across all 8 core dimensions plus D9/D10 follow-up checks
- **11,551 Google Scholar citations** (Apr 2026)
- **39.11M+ PyPI downloads** for PyOD
- **1,846 Semantic Scholar citations** for Diffusion Models survey
- **~285 Semantic Scholar citations** for TrustLLM
- **5+ books** with dedicated chapters on PyOD/COPOD/ECOD (Manning, Columbia, Apress, Routledge, IntechOpen)
- **2 podcasts** naming PyOD
- **5+ online courses/training pages** teaching PyOD (DataCamp, Udemy x2, O'Reilly video, Python Charmers / Datastat / RX-M / WUNU cluster)
- **8 enterprise integrations** (Databricks x2, Walmart, IQVIA, Apache Beam / Apache Software Foundation, PostHog, MLflow community flavor, Genentech/Roche Data Detective), 1 vendor whitepaper (Altair), 1 EU research project deliverable cluster (SEDIMARK Horizon Europe D3.1 p.18, D5.2), plus finance/audit workflow evidence from Discover Data and Syntora; PyOD GitHub Dependents aggregate snapshot 2026-05-07 = 5,493 repos + 139 packages
- **11 patents** citing PyOD/COPOD/ECOD/LSCP (WIPO x2, EU x2, US x4, China x3)
- **1 Nature Scientific Data publication** using PyOD (ESA OPS-SAT)

---

## Topic Validation (NOT Direct Coverage)

For grant narratives only. These do not name your work.

**AI agent security:** Tom's Hardware (non-DoxBench articles), TechCrunch, WinBuzzer, TechRadar, TechSpot, CyberNews, AI Commission, Bellingcat (DoxBench topic); Hacker News x2, Dark Reading, ReversingLabs, Sangfor, Reco.ai, Penligent.ai, DEV Community (gstack/aegis comparison -- different Aegis), Blink.new (OpenClaw crisis); NIST CAISI RFI (Jan 2026), NIST AI Agent Standards Initiative (Feb 2026), Bessemer VP, Cisco, Microsoft Agent Governance Toolkit, Palo Alto Networks OWASP blog; CSO Online "Runtime: The New Frontier of AI Agent Security"; HiddenLayer agentic runtime security (Mar 2026); IBM agentic AI runtime security; Grantex "State of AI Agent Security 2026" (93% rely on unscoped API keys); Gravitee "State of AI Agent Security 2026" (57.4% cite lack of audit trails); VentureBeat Nvidia agentic AI stack (GTC 2026); RSAC 2026 "Everyone trying to secure AI agents"; Help Net Security Sage open-source agent security layer (Mar 2026); Help Net Security Asqav open-source SDK for AI agent governance (Apr 2026); May 2026 topic-only additions from VentureBeat (agent identity/governance), The New Stack (security inside AI-agent tool handlers), CSO Online (MCP server exposure and zero trust), Forbes (agent authority risk), TechCrunch press release (agent trust protocol), Fortune (agent kill-switch framing). These do not name FORTIS work.

**Consulting/think tanks:** McKinsey x4 ("State of AI trust in 2026": 80% encountered risky agent behavior; "Agentic AI governance for autonomous systems"; "Agentic AI security: Risks & governance"; "Rethinking enterprise architecture for the agentic era"); Deloitte x5 ("Agentic AI in audit"; "Internal Audit Hot Topics 2026"; "Agentic AI Orchestration, Governance" -- only 21% mature governance; compliance leaders; Omnia platform); PwC x4 ("The end of traditional internal audit"; "Responsible adoption of AI agents"; "Validating multi-agent AI systems"; "Responsible AI and internal audit"); EY x2 (enterprise agentic AI audit launch -- 130K professionals, Apr 2026; "Unlocking the potential of agentic AI"); KPMG x4 ("AI governance for the agentic AI era" -- 75% prioritize auditability; "Critical Agenda Issues for Boards" -- 86% top priority; Q1 2026 pulse -- 63% require human validation; Canada audit committee); Accenture x3 (responsible AI governance; AI agent security identity; PE 2026); Oliver Wyman ("Agentic AI Transforming Compliance" -- automate 70% compliance, Feb 2026); WEF x3 ("AI Agents in Action" -- 82% plan adoption, Nov 2025; "Governance is key for AI agents" Mar 2026; public sector trust Jan 2026); OECD x2 (heightened security risks May 2025; Hong Kong privacy commissioner Mar 2026); CSA "AI Agent Governance Gap" (Apr 2026); CSET x3 ("Through the Chat Window"; "AI Control"; "Autonomous Cyber Defense"); Brookings ("The train has left the station"); RAND (measuring biological capabilities of AI agents); Partnership on AI ("Six AI Governance Priorities for 2026"); Sequoia

**ChatGPT geolocation (DoxBench topic, paper not cited):** Tom's Hardware, Cloudwards, Cybernews, TechRadar, TechSpot, WinBuzzer, AI Commission, Dataconomy, OECD.AI Incident Monitor.

**Government (topic, tools not cited):** GAO AI Accountability Framework, GAO Fraud/Improper Payments, Congress 119th hearing, Nextgov x2, OWASP Top 10 Agentic, OWASP AISVS, OWASP Agentic Skills Top 10, ENISA AI/Cybersecurity, UK Gov marketplace, OWASP Agentic AI Solutions Landscape Q2 2026 (no universities or academic tools listed); FTC AI Policy Statement ($53K/violation fines starting 2027, Mar 2026); SEC 2026 exam priorities targeting AI audit trails; FINRA 2026 Regulatory Oversight Report (multi-step agent reasoning auditability); Federal Register NIST RFI docket NIST-2025-0035 (Jan 2026); NIST ITL webinar "Building Measurement Probes into Agentic AI Ecosystems" (Apr 2026); White House National AI Policy Framework (Mar 2026); FDA deploys agentic AI platform for regulatory operations (2026); Singapore IMDA Model AI Governance Framework for Agentic AI (Jan 2026); EU AI Act enforcement (Aug 2, 2026) -- requires record-keeping, traceability, audit trails; EC Digital Strategy "Agentic AI: Leveraging European AI Talent" (Jan 2026); IEEE-USA NIST RFI Response mapping SP 800-53 audit controls to agent systems (Mar 2026); IETF Internet-Draft "Agent Audit Trail" standard -- JSON-based, tamper-evident hash chaining, maps to EU AI Act/SOC 2/ISO 42001 (Mar 2026)

**Auditable agents (topic, tools not cited):** ISACA "The Growing Challenge of Auditing Agentic AI" (2025); ISACA Advanced in AI Audit (AAIA) Certification launch (2025); ISACA Future Ready IT Audit Framework Update (2026); ISACA "Responsible AI: From Emerging Technology to Executive Governance Imperative" (2026); Fortune "Intelligence may be scalable, but accountability is not" -- Accenture/Wharton report (Mar 2026); Fortune "AI agents are getting more capable, but reliability is lagging" (Mar 2026); Fortune "Protect your agentic AI before you wreck your agentic AI" (Jan 2026); HBR "To Scale AI Agents Successfully, Think of Them Like Team Members" -- calls for audit trails (Mar 2026); HBR "AI Agents Act a Lot Like Malware" -- executive liability (Mar 2026); HBR "Create an Onboarding Plan for AI Agents" (Mar 2026); Bloomberg -- auditability "non-negotiable" in regulated environments; Gartner multiagent systems (audit trails); Forrester AEGIS Framework (39 controls, name collision -- their AEGIS, not ours); Forrester Predictions 2026 (half of ERP vendors will launch autonomous governance with audit trails); Forrester Agent Control Plane market evaluation; Mayer Brown legal guidance on agentic AI governance (Feb 2026); SafePaaS/Security Boulevard "2026 SOX Compliance: Why Every AI Agent is a Financial Risk" (Feb 2026); Accountancy Age "EY's agentic AI pivot -- A watershed moment for audit quality?" (Apr 2026); Medium (Ian Loe) "Your AI Agent Needs an Audit Trail, Not Just a Guardrail" (Mar 2026); Squirro "Autonomy without auditability is just a liability"; MarkTechPost "How to Build Transparent AI Agents: Traceable Decision-Making with Audit Trails" (Feb 2026); ACM "Creating Characteristically Auditable Agentic AI Systems" (FAIR 2025); Frontiers in AI "Audit-as-code" framework for continuous AI assurance (2026); IBM/e& enterprise agentic AI for governance and compliance (Jan 2026)

**LLM election prediction (topic, papers not cited):** Science (AAAS) "How AIs responded to the 2024 US presidential election -- in real time" (covers MIT CSAIL study, not USC papers); MIT Technology Review "AI's impact on elections is being overblown" (Sep 2024); Nature x2 ("Performance and biases of LLMs in public opinion simulation"; "Persuading voters using human-AI dialogues"); Newsweek x2 (AI election predictions); Semafor x2 (Aaru AI polling startup); Benzinga (Aaru); Brookings x2 ("How AI will transform the 2024 elections"; "Impact of generative AI in a global election year"); Pew Research (public concern over AI in elections); Harvard Ash Center "Using AI for Political Polling"; BYU (GPT-3 voter simulation); Chinese media: The Paper/澎湃新闻 x2 (AI election prediction, LLM voter simulation), Tencent News/南方周末 (Fudan agent-based election prediction), 36kr (Aaru), CSDN (ElectionSim Fudan), Al Jazeera Chinese; International: Carnegie Endowment "AI and Democracy" (Jan 2026); East Asia Forum (Korea elections); IDEA French "L'IA au service de la gestion electorale"; Korean academic journal (US election prediction models)

**Compute inequality in AI research (topic, paper not cited):** HPCwire "The Compute Divide in AI-Driven Science" (75% of AI supercomputing US-based, Nov 2025); VentureBeat "AI research finds a compute divide" (covers Ahmed & Wahed "De-democratization of AI"); Stanford HAI AI Index 2025 (academics 1-8 GPUs vs industry thousands, 90% of notable models from industry); TIME "US Just Made a Crucial Step Toward Democratizing AI Access" (NAIRR pilot); Brookings "How the NAIRR can pilot inclusive AI"; MIT Technology Review "AI is making inequality worse"; Nature x2 ("AI can supercharge inequality"; "AI scientists are changing research"); CFR "How 2026 Could Decide the Future of AI"; Digital Economy Trends 2026 "The AI Divide"; BAAI Community (AI large model training cost surge)

---

## Changes from Previous Audit

**May 13 (later) Claude independent wide 8-lane parallel Phase A + Phase B (+8 net new rows on top of the earlier Codex draft; 0 unique Ledger 2 + 8 Ledger 3, plus 4 Ledger 2 evidence upgrades after Codex Round 1 dedupe):**
- **Ledger 2 (+0 new rows; 4 evidence upgrades to existing rows after Codex Round 1 deduplication):** Wide-run Phase A initially proposed Microsoft Research TrustLLM page, thepaper.cn TrustLLM feature, aiproductivity.ai Aegis article, and jiqizhixin TrustLLM feature as four new Ledger 2 rows. Codex Round 1 caught all 4 as exact-URL duplicates of existing rows #7, #5, #21, #34b respectively (the Lane skip list did not enumerate these specific URLs). The four candidates were dropped from the Ledger 2 table; the May 13 verification work for each becomes an evidence upgrade on the corresponding existing row: #7 Microsoft Research TrustLLM now has stronger author-affiliation evidence for Yue Zhao at USC affiliation index 26; #5 The Paper (澎湃新闻) now has confirmed arXiv link and project URL; #21 AI:PRODUCTIVITY Aegis now has user-verified USC AEGIS-specific metrics despite the original WebFetch 403; #34b Jiqizhixin (机器之心) now has user-verified TrustLLM arXiv evidence.
- **Ledger 3 (+8):** TrustLLM 2026 mainstream-venue academic citation cluster across ACS Env Sci Tech, Springer Requirements Engineering, ACM/IEEE HRI 2026, Wiley TIBR, Springer CCIS, and Springer Frontiers of CS, plus ACM Computing Surveys "Towards Trustworthy AI" review folded in via user manual verification (#66do, OpenAlex citation graph + manual ACM verification); Justin0504/Aegis third-party implementation citing arXiv 2603.12621 (#66dp); first Russian-language Habr corporate-blog cluster across Otus, Garda, Rosatom (#66dq); Japanese developer-blog expansion across codemajin, tam5917 Hatena KDE extension, Qiita amber27182818 PyOD tutorial (#66dr); Juejin Chinese tutorial with direct repo clone and CMU SUOD PDF link (#66ds); mala-lab Awesome AD Foundation Models curated list citing PyOD 2 (#66dt); aggregator paper-page cluster across HuggingFace Papers (TrustLLM USC affiliation #26 verified), HuggingFace DoxBench dataset (Yue Zhao link points to USC homepage), alphaxiv x3, and papers.cool x2 (#66du, kept at Tier 5 as weak platform-tail evidence; aggregator pages are capped at Tier 3 by `disclaimer-patterns.md` and we hold the conservative T5 floor); Datawhale WeChat public-account lecture writeup by Yue Zhao (then CMU), unlocked via user manual verification of the WeChat verification gate (#66dv).
- **Phase B held leads, resolved via user manual verification 2026-05-13:**
  - **Unlocked (4 leads, 1 new row + 3 evidence upgrades):** aiproductivity.ai Aegis article verified by user (page names the USC AEGIS work with the paper-specific metrics) but exact URL = existing #21, so the unlock becomes an evidence upgrade on #21 rather than a new row; jiqizhixin.com TrustLLM feature verified by user but exact URL = existing #34b, evidence upgrade on #34b; ACM Computing Surveys "Towards Trustworthy AI" review verified by user (USC ACM subscription) and folded into Ledger 3 #66do cluster; Datawhale WeChat lecture by Yue Zhao (then CMU) verified by user, added as Ledger 3 #66dv.
  - **Dropped to verified-negative (1):** Stanford HAI 2026 AI Index Responsible AI chapter. The WebSearch snippet "the indicator measures a model's overall trustworthiness using the TrustLLM benchmark, a comprehensive framework spanning six dimensions" was a search-engine summarizer synthesis, not verbatim PDF text. The actual report does not name TrustLLM. Cautionary precedent recorded in `news-search-candidates.jsonl`; same failure mode as the 2026-05-07 GAO-26-108695 case. Lesson: never count a snippet-only Tier 0 / Tier 1 candidate without PDF or direct-fetch confirmation, even when the snippet reads as a verbatim quote.
- **Verified-negative buckets (recorded in JSONL, ~80 outlets across 8 lanes):** U.S./intl gov PDFs (NIST AI 800-series, GAO, CRS, White House, FTC, SEC, FINRA, CISA, DoD, DOE, EU AI Office, ENISA, UK AISI, OECD AI Incidents Monitor, IMDA, Canada, UNESCO/UN, ISO, IEEE-USA, FDA, NASA, CDC); foundation-model companies (OpenAI GPT-5.x / o3 / o4-mini / Deep Research / gpt-oss / Codex-Max / ChatGPT Agent system cards plus Preparedness Framework v2 and Model Spec; Anthropic Claude Mythos / Opus 4.6 / Sonnet 4.6 plus RSP 1.0-3.1 and alignment-auditing Petri/Bloom/A3; DeepMind Gemini 3.1 / Flash family; Meta Llama 4/5; Mistral; xAI Grok; Cohere; DeepSeek R1; IBM Granite; AWS Titan / Q; NVIDIA; Character.AI; Perplexity; Alibaba Qwen); Tier 1 mainstream press (Wired, MIT Tech Review, IEEE Spectrum, Forbes, Bloomberg, Reuters, WSJ, TechCrunch, VentureBeat, Ars Technica, The Register, Fortune, Fast Company, Axios, The Information, The Batch, The Gradient); security / AI-safety vendor blogs (DarkReading, BleepingComputer, SecurityWeek, HelpNetSecurity, CSO Online, SCMagazine, CyberScoop, TheRecord, TheHackerNews, SANS, Adversa AI, ProtectAI, HiddenLayer, Promptfoo, Lakera, Snyk, METR, Robust.ai, Scale, Goodfire, Huntress, Darktrace, Vectra, Exabeam, Apiiro, Ravelin, Reblaze); consulting / analyst firms (McKinsey, Deloitte, PwC, EY, KPMG, BCG, Bain, Accenture, Capgemini, Cognizant, Wipro, Slalom, Oliver Wyman, Gartner, Forrester, IDC, GigaOm, 451 Research); think tanks (RAND, Brookings, CSET-Georgetown, CSIS, CNAS, CIGI, ITIF, Data Innovation, Bipartisan Policy, safe.ai, Partnership on AI, CAISI, European AI Safety Institute); vendor whitepapers (Snowflake, Datadog, New Relic, H2O.ai, DataRobot, Dataiku, Domino.ai); additional non-English outlets (Heise, Golem, t3n, Spiegel, Le Monde Informatique, ZDNet FR, Numerama, Xataka, El Pais, Repubblica, Corriere, Le Figaro, ITmedia, AISmiley, AINow, dev.classmethod, ZDNet KR, ETNews, Bloter, IT World KR, Brunch, Modulabs, SAIGE); five major LLM/agent-security awesome lists (corca-ai, ucsb-mlsec, wearetyomsmnv, LLMSecurity, CryptoAILab); two awesome-ai-agents-2026 lists (caramaschiHG, Zijian-Ni); Glama MCP Aegis listings (all name-collisions).
- **New name-collision entries (added to disambiguation registry):** AegisAI (email security startup, Cy Khormaee / Ryan Luo ex-Google); Forrester AEGIS Framework; RedHat aegis-ai (CVE-focused GenAI agent); Adversa AEGIS (AI security catalog); SANS Fortisec (Foster Nethercott offensive AI consultancy, name-similar to FORTIS Lab); NVIDIA "Yue Zhao" NV Grad Fellow (UT Austin Krähenbühl group video foundation models); Amazon Science "Yue Zhao" (Applied Scientist, operations research); Google VideoPrism "Yue Zhao" (ICML 2024, video foundation models); Alibaba PyODPS (MaxCompute Python SDK, not PyOD); EU CORDIS TrustLLM project 101135671 (Linköping-led EU LLM initiative, not arXiv 2401.05561); Pyodide (Python in browser, not PyOD); TrustPid (not TrustLLM); Lingxiao Zhao CMU 2024 dissertation (not Yue Zhao).

**May 13 Codex Phase A wide sweep + Claude Phase B verification (+7 net new rows; 5 in Ledger 3 after one Ledger 2 to Ledger 3 demotion):**
- **Ledger 2 (+2 verified):** PyShine external developer blog covers `agent-style`, names Yue Zhao, and links the repo (Rule 1+2+6 met); The Fintech Mag names PyOD as a fintech fraud-detection alternative with a verbatim "go-to toolkit for fraud analytics" quote (Rule 1 met; templated 152-tool listicle pattern flagged but no AI disclaimer found).
- **Ledger 3 (+5 verified, including +1 demoted from Codex Ledger 2 Phase A draft):** Oracle FCCM product `pyod` license subpage names the BSD `Copyright (c) 2018, Yue Zhao` notice (Codex's Oracle IoT URL claim returned 404 on verification and was dropped from the row); RedTeams AI "Major Safety Benchmarks" table names TrustLLM in an editorial article; PySAD documentation and PyPI explicitly state batch detectors from PyOD can be used in streaming settings; non-English platform cluster #66dm narrowed to Volcengine + GitCode + Sohu after Inferri returned 403 Forbidden and the Qiita entry was identified as a translation of the Databricks Kakapo blog already counted as #42; Growth Japan CDCR-SFT moved to Ledger 3 #66dn from Codex's original Ledger 2 draft after the source page was found to carry a verbatim AI-generated disclaimer (per `disclaimer-patterns.md`, `ai_generated` is capped at Tier 3).
- **Candidate-only / topic-only:** AI News CX, ResearchTrend, Gist.Science, and Papers.cool direct paper pages for Agent Audit, Auditable Agents, and Aegis remain platform-tail unless promoted; VentureBeat, The New Stack, CSO Online, Forbes, TechCrunch, Fortune, and OECD.AI are topic validation only because no direct FORTIS citation surfaced.

**May 7 weekly parallel sweep + Codex Round 1+2 review promotions (+34):**
- **Ledger 1 (+3):** MITRE LILAC v1 technical report cites TrustLLM; Google DeepMind / Google Research TxGemma report and Google Developers pages use TDC for training/evaluation; OpenAI Careers Technical Intelligence Analyst listing names PyOD as an Intelligence & Investigations tool.
- **Ledger 2 (+6):** The Autonomy Review covers The Autonomy Tax; Fora Soft covers PyOD/ADBench; The Weather Report compares Aegis; Rubik's Code covers SUOD; EthicAI/JOBIRUN/WebProNews explain FLI/TrustLLM; Samsung SDS Insights Korean editorial names TrustLLM as flagship LLM trustworthiness evaluation framework.
- **Ledger 3 (+24):** Microsoft Research / CMU Tepper / Adobe Research coauthor-institution listings moved here from initial Ledger 2 placement; LangSkills reference; four new patent rows; Discover Data / Morningstar finance research; Syntora audit workflow; TrustLLM academic-citation cluster; DoxBench follow-on/AI-assisted-news cluster; SecTools Autonomy Tax AI-generated page; ACS PyOD 2 proteomics uptake; PyOD education cluster; TDC education/platform cluster; 2025-2026 paper-platform tail; gatodo (CDCR-SFT) external newsletter; **enterprise code-adoption rows:** Apache Beam (Apache Software Foundation, 8.5K stars, first-class PyOD ModelHandler), PostHog (34K stars, multi-detector production alerting subsystem), MLflow (25.8K stars, community-flavor docs), Genentech/Roche Data Detective (pharma drug-discovery validators); PyOD GitHub dependents aggregate snapshot (5,493 repos + 139 packages, 2026-05-07).
- **Ledger 5 (+1):** Wikipedia (en) "Anomaly detection" — Software section names PyOD; reference list cites Zhao/Nasrullah/Li 2019 JMLR.
- **Candidate-only / held:** OpenAI Quantitative Threat Forecasting Analyst — held until a first-party OpenAI/Ashby rendered snapshot is committed (Cloudflare returned 6.3KB JS shell on 2026-05-07; would promote to Ledger 1 #8h with #8g-pattern evidence on capture). Wells Fargo Principal Platform Engineer R-512394 — held until a rendered Wells Fargo page, Wayback copy, or browser snapshot is committed (returned 403 on 2026-05-07; would promote to Ledger 3 enterprise operational adoption on capture). Nature Scientific Reports x3 ADBench scientific-uptake cluster — demoted back to candidate pool in Codex Round 2 because the row rested on WebSearch-snippet confirmation only; full-text fetch was Nature-IDP gated. Re-promote after direct article fetch records reference-list evidence per the "snippet alone is not verified evidence" rule. MITRE CWE-1039 / CommanderSong kept out of count because the paper is not in `data/publications.json` and the Yue Zhao identity/inventory decision is pending.
- **Confirmed negatives:** OpenAI/Anthropic/DeepMind/Meta/Mistral/xAI/Cohere system-card searches, major tech/security/business press, OWASP/MITRE ATLAS/CSA/MLCommons, analyst/consulting sources, GAO/CRS accessible pages, and EU CORDIS had no new direct target hit beyond rows recorded above.
- **Skill upgrades (Round 1 + 2):** `skills/news-search/scripts/pdf_term_scan.py` rewritten to load every paper title and tool name from `data/publications.json` + `data/open-source.json` plus arXiv IDs (215 terms versus 38 hard-coded) so the full-audit-mode contract is met. `skills/news-search/SKILL.md` adds an explicit Tier 0(b) FM-co-careers exception (first-party FM-co JD naming a tool as operational tooling counts as Tier 0(b) only with a durable local or public snapshot, referencing #8g precedent); non-FM-co careers pages classify under Ledger 3 (ecosystem adoption) per Codex Round 2. `skills/news-search/references/candidate-schema.md` now documents the extended Phase A/B fields and the `status` lifecycle (`candidate` / `candidate-promote` / `counted` / `dropped` / `dropped_name_collision` / `verified-negative` / `paywall_or_blocked`) used by the active JSONL. `skills/news-search/references/disambiguation-registry.md` carries cumulative collision rules and verified-negative leads from this round. `.gitattributes` extended with binary declarations for PDF / DOCX / image types so `git diff --check` no longer treats binary assets as text.

**New items added this pass:**
- #4: Tom's Hardware -- REMOVED (DoxBench citation could not be verified; moved to Topic Validation)
- #5: The Paper (澎湃新闻) -- TrustLLM (Tier 1 Chinese news, D7)
- #10: MarkTechPost -- TrustLLM deep dive (D3)
- #16: Amazon Science paper -- BOND/PyGOD (D3)
- #22: SitePoint -- agent-audit (D4)
- #23: LLMoGuy.com -- StealthRank (D5)
- #32: Cake.ai -- PyOD guide (D2)
- #33: Milvus/Zilliz -- PyOD reference (D2)
- #34: Prompting Guide -- TrustLLM (D7)
- #45: Altair AI Studio -- PyOD whitepaper (D8)
- #47: ESA OPS-SAT upgraded -- Nature Scientific Data 2025
- #48-51: Courses (DataCamp, Udemy x2, O'Reilly video)
- #55-60: Non-English platforms (Zhihu x2, Tencent Cloud, aidoczh, Qiita, ClassCat)
- #61-62: HuggingFace (DoxBench, TDC)
- #64-65: Academic papers using COPOD/ECOD
- D8 regulated verticals searched (all negative)
- Metrics updated: 39.11M downloads, 9,770+ stars, 1,846 diffusion survey citations

- #18b-d: USC Viterbi conference roundups (ICLR 2025, ICML 2024, faculty announcement 2023)
- D3a mainstream press confirmed all negative

- **U.S. DoD CDAO** — TrustLLM listed in Generative AI Responsible AI Toolkit (Tier 0, found by Codex)
- #18e-f: USC ISI NeurIPS roundup, FSU TyphoFormer PR (found by Codex)
- #66a-b: Manning liveProject, GeeksforGeeks tutorial (found by Codex)
- Codex audit merged and deleted

**Apr 9 deep patch (+13):**
- #34b-f: Chinese media (机器之心, 腾讯新闻, 新浪财经, 懂AI, 搜狐)
- #66c-j: Ecosystem (tutorials, 2 books, Springer chapter, IQVIA enterprise, Text-ADBench, Tencent Cloud TrustLLM)
- BIS WP 1188 removed from D8 candidates (verified: does not cite PyOD)
- Citation affiliation audit refreshed (no change: 44 papers, 24 T0, 150 T1)

- External reports merged: 5 new media, 5 new patents, Ericsson research paper, 14 non-English sources (Korean x3, Japanese x4, German x5, Spanish x2), corrected negative results

**Previous total: 64 items. New total (Apr 9): 130 items (+66).**

**Apr 10 targeted search (+13):**
- **Tier 0 (Ledger 1):** International AI Safety Report 2026 — TrustLLM citation #881 (Yoshua Bengio, 30+ countries, Feb 2026). Privacy International "Nowhere to Hide?" — DoxBench cited p.28, footnote 56 (Feb 2026).
- **Ledger 2:** TDS "Boosting Your Anomaly Detection With LLMs" (PyOD 2, Sep 2025); Brian D. Colwell "Big List of AI Jailbreaking" (JailDAM); Number Analytics (PyOD); bioengineer.org DrugAgent syndication (Feb 2026).
- **Ledger 3:** 7 new Tier 5 platform entries (Liner x2, Moonlight x3, aimodels.fyi x2, Paper Digest ICLR 2026, alphaXiv, Bohrium, paperreading.club).
- DrugAgent/Nature Biotech (#12) verification flag removed (confirmed names DrugAgent).
- OWASP D8 candidate cleared (manually checked: no academic tools listed).
- Topic Validation: added OWASP Landscape Q2 2026 (negative), ISACA auditing article.

**New total: 143 items (+13 from Apr 9).**

**Apr 10 targeted search — agent/LLM/VLM last-author works (+10):**
- **Ledger 2:** #36k FaceLock — So Essentially (Substack) by Dhruv Diddi, covers FaceLock algorithm, names USC (Nov 2024, D5).
- **Ledger 3 (Tier 5 platforms):** 9 new entries — DyFlow (66ad: Moonlight, ChatPaper, alphaXiv); FaceLock (66ae: Liner, Moonlight); CoAct (66af: Moonlight, aimodels.fyi, Bytez); Agent Banana (66ag: Moonlight); StealthRank (66ah: Moonlight); Defenses Against Prompt Attacks (66ai: alphaXiv); Can MLLMs do TSAD (66aj: Emergent Mind, Moonlight, aimodels.fyi — extends 66ac); Multimodal GEO (66ak: Emergent Mind); agent-audit (66al: Hacker News Show HN).
- **Topic Validation (major expansion):** Auditable agents concept now covered by Fortune x3, HBR x3, Bloomberg, all Big Four (EY, Deloitte, PwC, KPMG), McKinsey x4, Forrester x3, Gartner, WEF x3, OECD x2, CSET x3, CSA, Partnership on AI. Government/regulatory: FTC ($53K/violation fines 2027), SEC exam priorities, FINRA, Singapore IMDA framework (Jan 2026), EU AI Act enforcement (Aug 2026), IETF Internet-Draft "Agent Audit Trail" standard (Mar 2026), NIST ITL webinar, White House AI Policy Framework, IEEE-USA response. Agent security: CSO Online, HiddenLayer, IBM, Grantex, Gravitee (57.4% lack audit trails), VentureBeat, RSAC 2026. ISACA expanded to 4 items including AAIA certification.
- **Aegis:** No new coverage. Name extremely crowded (10+ competing products named "Aegis").
- **agent-audit:** No new third-party editorial coverage. OpenClaw crisis covered heavily but cites Koi Security/Snyk/Trend Micro, not agent-audit.
- **Auditable Agents (arXiv:2604.05485):** No direct citations (paper too recent). Topic validation is the strongest of any work — the exact concept is the dominant theme of 2026 enterprise AI governance.

**New total: 153 items (+10 from 143).**

**Apr 10 targeted search #2 — DPU, Political-LLM, Treble, ADBench, Computing Resources (+17):**
- **Ledger 2:** #36l-m ADBench — BAAI Community (智源社区) x2: dedicated Chinese-language articles, one provocatively titled "Can We Really Trust Progress in Anomaly Detection Over the Past 20 Years?" (Sep 2022, D7).
- **Ledger 3:** 15 new entries:
  - ADBench (66am-as): Zhihu x2, CSDN x2, Emergent Mind topic page, Kaggle notebook, alphaXiv.
  - DPU (66at): GitHub Awesome-OOD-Detection curated list.
  - Treble (66au-av): Moonlight + alphaXiv; 2 GitHub Awesome Hallucination lists.
  - Political-LLM (66aw-ax): alphaXiv + aimodels.fyi; SSRN Top Download Paper for Decision Science.
  - Computing Resources (66ay-az): Hugging Face Papers page; CVPR 2026 Compute Reporting Form policy ecosystem (official pilot + LinkedIn posts from program chair Pavlovic, Sasha Luccioni, Jon Barron).
- **Topic Validation:** LLM election prediction — Science (AAAS), MIT Tech Review, Nature x2, Newsweek x2, Semafor x2, Brookings x2, Pew, Harvard, Chinese media (The Paper x2, Tencent News, 36kr, CSDN), Carnegie Endowment, Korean journal. Compute inequality — HPCwire, VentureBeat, Stanford HAI AI Index 2025, TIME (NAIRR), Brookings, MIT Tech Review, Nature x2, CFR.
- **Political-LLM:** No direct editorial coverage despite "Will Trump win?" media hook. MIT CSAIL study and Aaru startup captured the media attention. Topic validation very strong.
- **DPU:** No editorial coverage beyond platform listings. 2 Zhihu CVPR 2025 roundups inaccessible (403).
- **Treble:** No editorial coverage. EMNLP 2025 Findings. Listed in 2 GitHub Awesome Hallucination reading lists.
- **Computing Resources:** No new editorial coverage. CVPR 2026 Compute Reporting Form is the strongest downstream policy impact.

**New total: 170 items (+17 from 153).**

**Apr 11 targeted search #3 — under-searched high-star tools (+17):**
- **Ledger 2 (+6):** PyGOD TDS tutorial by Tomonori Masui (Oct 2022); PyGOD/BOND BAAI Community article (Nov 2022); Anomaly-Detection-Resources featured on paulvanderlaken.com (Dec 2019) + R-bloggers syndication; CS-Paper-Checklist featured in HelloGitHub Monthly Vol. 110 (May 2025) + Efficient Coder article (May 2025).
- **Ledger 3 (+11):** PyGOD (66ba-bb: Zhihu x3, CSDN x5); TODS (66bc-be: Zhihu x3, Tencent Cloud, CSDN x2, DongAI, GitCode, Explinks, Showapi); combo (66bf-bh: Zhihu, Tencent Cloud/Datawhale, CSDN x2); Anomaly-Detection-Resources (66bi-bj: Zhihu, CSDN x2); CS-Paper-Checklist (66bk-bl: CSDN, Scholar's Corner).
- Chinese-language coverage is the dominant discovery: PyGOD has 9 Chinese items, TODS has 10, combo has 4, Anomaly-Detection-Resources has 3. English-language coverage for these tools is sparse beyond the initial PyOD ecosystem articles.
- Anomaly-Detection-Resources (9,239 stars) has surprisingly little dedicated coverage — visibility flows through PyOD rather than the resources repo itself.

**New total: 187 items (+17 from 170).**

**Apr 16 delta check (5-day window since Apr 11, no new verified items):**
- Ran targeted Dim 1/3/4/5 queries: "Yue Zhao" + USC recent news; Auditable Agents (arXiv:2604.05485); agent-audit/Aegis April 2026; TrustLLM system cards; USC Viterbi ICLR 2026; DoxBench/FigEdit/TrustGen pre-conference; Chinese media TrustLLM 2026; FLI Spring 2026 (none released); Hacker News April 2026; Stanford AI Index 2026 overview pages; International AI Safety Report 2026 extended summary.
- **No new confirmed citations.** Auditable Agents (posted Apr 7) still too recent for external coverage. USC Viterbi "USC at ICLR 2026" roundup not yet published (conference is Apr 24-28). FLI AI Safety Index Spring 2026 not yet released.
- **D8 candidates deferred to next PDF pass:**
  - **Stanford AI Index 2026** (released Apr 15, 2026, 400+ page PDF at hai.stanford.edu/assets/files/ai_index_report_2026.pdf) — chapter overview pages show no mention of TrustLLM/PyOD/USC tools, but the full PDF could not be retrieved via WebFetch (size cap). Re-check via local PDF extraction in next full audit.
  - **Fast Company "AI's most important benchmark in 2026? Trust"** (fastcompany.com/91462096/ai-trust-benchmark-2026-openai-anthropic) — fetch returned 403; article title directly matches TrustLLM's framing. Retry with alternate method.
  - **eWeek "Stanford AI Index 2026: The Trust Gap Hits Critical Levels"** — fetch returned 403. Retry.
- **Name-collision clarifications (not coverage):**
  - **agentlayer.medium.com "Aegis + TrustLLM" smart contract auditing** — VERIFIED as different projects. Their "TrustLLM" is arXiv:2403.16073 (Solidity auditing, two-stage fine-tuning), not Yue Zhao's TrustLLM (arXiv:2401.05561). Their "Aegis" is AgentLayer's web3 auditor, not FORTIS's Aegis (arXiv:2603.12621). Add to negative-results to prevent re-investigation.
  - **"TRUST" decentralized framework** (arXiv:2510.20188) — different project from TrustLLM; name similarity only.
- **Upcoming opportunities reconfirmed:** ICLR 2026 in Rio Apr 24-28 (DoxBench, FigEdit, DecAlign, TrustGen); 机器之心 ICLR 2026 Paper Sharing in Beijing Apr 18; expect USC Viterbi "USC at ICLR 2026" roundup late Apr / early May.

**Apr 22 targeted search — KnowFM workshop acceptances, Cat-DPO preprint, agent-style, anywhere-agents (no new verified items):**

- **Scope (5 items):** Auditable Agents (ACL 2026 KnowFM acceptance, non-archival; paper itself on arXiv since Apr 7), Multimodal Generative Engine Optimization / MGEO (ACL 2026 KnowFM, archival; arXiv:2601.12263), Cat-DPO (new preprint arXiv:2604.17299, posted Apr 19), agent-style (PyPI release, 157 GitHub stars), anywhere-agents (PyPI/npm release).
- **Dimensions run:** 3 (outlet sweep), 4 (topic proximity), 5 (smart keywords), plus targeted `site:` queries on Hacker News, Reddit r/MachineLearning, DEV Community, MarkTechPost.
- **Findings:** No third-party editorial coverage for any of the 5 items. All results trace back to first-party sources (arXiv abstract/HTML/PDF, GitHub repos, ResearchGate auto-mirror, Yue Zhao USC homepage, LinkedIn profile) or unrelated topic-only articles.
  - Cat-DPO (3 days old) is expectedly too fresh for coverage.
  - MGEO workshop acceptance not yet propagated beyond the OpenReview submission (Apr 21).
  - Auditable Agents remains in the same position as Apr 11: strong topic-validation footprint, no direct coverage.
  - agent-style/anywhere-agents: no third-party blog review, no Show HN thread, no Hacker News item, no DEV Community writeup found. Repo exists, README content is the only surface visible to search engines.
- **Topic-only matches (Topic Validation, not coverage):** DeployHQ "How to Configure Every AI Coding Assistant" (covers AGENTS.md/CLAUDE.md/Cursor Rules — does not name agent-style or anywhere-agents). Several DEV Community AGENTS.md articles ("What is AGENTS.md and Why Should You Care?", "Agents.md — A New Standard for Coding Agents", "Steering AI Agents in Monorepos with AGENTS.md") cover the AGENTS.md concept without naming these tools.
- **Name-collision hazards noted for future runs:**
  - "Multimodal Generative Engine Optimization" ambiguates heavily with the marketing concept "Generative Engine Optimization" (GEO / LLM-SEO). Use "MGEO" + "vision-language model" + "rank manipulation" disambiguators.
  - "AGENTS.md" queries return crowded results on a generic spec used by 20K+ projects; always pair with `yzhao062` or `"Yue Zhao"` or one of the 21-rule distinctive phrases.
  - "Cat-DPO" has no known name-collision yet (unique enough).
- **Upcoming opportunities:**
  - Expected 1-2 week window for MarkTechPost / Synced / AI newsletters to pick up Auditable Agents given subject fit.
  - ACL 2026 KnowFM workshop proceedings go live closer to the August conference — post-workshop coverage window opens then.
  - Chinese AI press (机器之心, BAAI Community, Zhihu) historically covers AI-auditing and VLM-attack topics thoroughly; re-sweep in ~3-4 weeks.
  - Watch arxiv.org/abs/2604.17299 listing pages (alphaXiv, Moonlight, aimodels.fyi, Emergent Mind) for Cat-DPO — these aggregators index within days.

**New total: 187 items (unchanged from Apr 16; no new verified coverage this pass).**

**Apr 22 full-range parallel audit (5 agents, all dimensions across 120+ items):**

Dispatched 5 parallel research agents covering (A) tools+workshop delta since Apr 16, (B) Dim 8 PDF deep search with bypass of the 10 MB WebFetch cap, (C) Dim 3 outlet sweep across tech/security/newsletter press for 30 days, (D) Dim 7 non-English coverage 30/90-day window, (E) deep-dive media check on the two newly-launched tools. All 5 agents ran Dim 1/3/4/5/7/8 queries within their scopes.

**Verified new coverage: 0 items.** The previously recorded 187 items are unchanged.

Notable confirmed negatives worth logging (searched at full-text level, no matches for any FORTIS target term or arXiv ID):
- **Stanford AI Index 2026** (`hai.stanford.edu/assets/files/ai_index_report_2026.pdf`, 423 pp, 38.7 MB): 138 unique arXiv IDs in bibliography, none match. **Confirmed negative** — prevents re-search.
- **Anthropic Claude Opus 4.7 System Card** (232 pp, 14.2 MB): no TrustLLM, PyOD, DoxBench, or related citations.
- **Google DeepMind Gemini 3 Pro Model Card** (9 pp) and **Frontier Safety Framework** (26 pp): none.
- **OpenAI GPT-5 System Card** (60 pp) and **GPT-5.1-Codex-Max System Card** (27 pp): none.
- **OWASP GenAI Q2 2026 Solutions Landscape** (Agentic + LLM/GenAI Apps + AI Red Teaming, ~48 pp total): none.
- **NIST AI 800-3** (Feb 2026, 64 pp) and **NIST AI 800-2 Initial Public Draft** (39 pp): none.

Deferred D8 candidates:
- ~~**Fast Company "AI trust benchmark 2026"**~~ — mirror at fastcompany.co.za retrieved; no target terms. Cleared.
- **eWeek "Stanford AI Index 2026: Trust Gap Hits Critical Levels"** — 403 on fetch; three adjacent AI-Index coverage articles (IEEE Spectrum, ArtificialIntelligence-News, The-Decoder) fetched cleanly and all returned NONE. Deferring eWeek to next pass.
- **FLI AI Safety Index Spring 2026** — not released (current editions are Summer 2025 and Winter 2025). Re-check after next FLI release.
- **NIST AI RMF Profile on Trustworthy AI in Critical Infrastructure** (announced Apr 7) — concept note only; no PDF URL resolved. Check in 2-4 weeks.

Dim 3 outlet sweep (30-day window, 2026-03-22 to 2026-04-21):
- Zero verified hits across venturebeat, technologyreview, spectrum.ieee.org, infoq, thenewstack, techcrunch, wired, arstechnica, theverge, darkreading, thehackernews, securityweek, bleepingcomputer, csoonline, therecord.media, deeplearning.ai, marktechpost, syncedreview, thegradient, importai.net, kdnuggets, towardsdatascience, analyticsvidhya, dev.to, aiacceleratorinstitute, aiproductivity, sitepoint.
- Topic-only matches (not coverage): MarkTechPost "Enterprise AI Governance" (Mar 15 — uses "auditable agent execution" as generic concept), Stack Overflow Blog "Coding guidelines for AI agents" (Mar 26 — parallels agent-style concept but does not name it), DEV.to AI weekly roundups, Medium agentic-coding post.

Dim 7 non-English (30/90-day window):
- Zero verified hits in Chinese (jiqizhixin, BAAI, Zhihu, CSDN, Sohu, Tencent News, Sina, 36Kr, InfoQ.cn, dongaigc, thepaper.cn), Japanese (Qiita, Zenn), Korean (Tistory, Velog), or European (heise.de, lemondeinformatique.fr, eluniversal.com).
- Chinese LLM-Safety digest posts on Zhihu for Jan-Mar 2026 cover TrustJudge (PKU/THU) and TrustBench, not Yue Zhao's TrustLLM — name collision, topic-only.
- No 机器之心 syndication chain triggered yet for any 2026 item.

Name-collision hazards logged (add to disambiguation list):
- **TrustLLM**: European `trustllm.eu` project; smart-contract auditor "TrustLLM" at arXiv:2403.16073 (different from arXiv:2401.05561); Zhihu's "TrustJudge"/"TrustBench" posts are unrelated Chinese projects.
- **Aegis**: extremely crowded — Red Hat `aegis-ai`, AgentLayer Aegis (smart-contract), `automorphic-ai/aegis`, `antropos17/Aegis`, three unrelated 2026 arXiv papers titled AEGIS. FORTIS Aegis requires "pre-execution firewall" + `Justin0504` or paper authors.
- **MGEO**: collides with marketing "Generative Engine Optimization / GEO" (LLM-SEO); require "vision-language" or "rank manipulation" disambiguators.
- **FORTIS**: video-game company "Fortis" (Las Vegas Sands / Steve Chiang) dominates VentureBeat index.
- **Yue Zhao**: many homonyms (Salesforce Ventures principal, Yixue Zhao at USC ICT). Pair with USC, PyOD, FORTIS lab, or arXiv ID.
- **agent-style**: ambiguates with style-guide articles that discuss "agent style". Disambiguate with `yzhao062` or "21 writing rules" or "Claude Code Codex".

New tool launches (agent-style, anywhere-agents) — ecosystem signals only, no third-party coverage:
- **agent-style**: GitHub 214 stars (up ~36% since 2026-04-21), 8 forks; PyPI 725 weekly downloads (v0.3.1). No Show HN thread, no DEV writeup, no podcast, no aggregator listing. Explicitly not listed in VoltAgent/awesome-agent-skills (1100+ entries) or awesomeclaude.ai/awesomeskills.dev.
- **anywhere-agents**: GitHub 124 stars, 12 forks; PyPI 1,338 weekly downloads (v0.2.0 Apache-2.0); npm package exists. No third-party coverage found anywhere. HN Algolia API confirms no submission exists.
- Both are still in the first-party-signal phase. Star and download growth is healthy; external editorial coverage has not yet triggered.

New PDF candidates added to query bank for next audit:
1. **NIST AI 800-3** (`nvlpubs.nist.gov/nistpubs/ai/NIST.AI.800-3.pdf`) — NIST's first benchmark-evaluation statistical framework; track for updates.
2. **NIST AI 800-2 IPD** (`nvlpubs.nist.gov/nistpubs/ai/NIST.AI.800-2.ipd.pdf`) — automated benchmark best practices; track finalized version.
3. **OWASP GenAI Q2 2026 landscape trio** (IDs 53437 / 53440 / 53629 at `genai.owasp.org/download/<id>/`).
4. **McKinsey "State of AI trust in 2026: Shifting to the agentic era"** — retry as PDF export.
5. **Stanford AI Index 2026 public dataset** (CSV bibliography extraction complements PDF grep).
6. **Gemini 3.1 Pro Model Card** (`deepmind.google/models/model-cards/gemini-3-1-pro/`).
7. **International AI Safety Report — Extended Summary for Policymakers** (separate PDF from full report).
8. **CETaS / Alan Turing Institute Intl AI Safety Report page** (cetas.turing.ac.uk).

**Apr 24 parallel full sweep (+19 verified items):**
- **Ledger 1 (+1):** LLNL/DOE SafeAI report cites TrustLLM.
- **Ledger 2 (+2):** Vector Institute ICLR 2026 roundup names TrustGen and Yue Zhao; Adobe Research page names FigEdit/Charts Are Not Images and Yue Zhao.
- **Ledger 3 (+16):** New platform and ecosystem rows added for Cat-DPO, Topology Matters, Auditable Agents, Aegis, DoxBench, TrustGen, PyOD/PyOD 3, agent-audit, agent-style/anywhere-agents, PersonaConvBench, Defenses Against Prompt Attacks, Mitigating Hallucinations, AD-LLM/NLP-ADBench, Secure On-Device Video OOD/SocialMaze/MGEO, long-tail tool listings, and Deloitte Germany AIxAML citing ADBench as consulting/industry evidence.
- **Confirmed negatives:** No new direct hits in the requested major outlet set (USC Viterbi, MarkTechPost, Synced, Jiqizhixin, The Paper, VentureBeat, TechCrunch, Wired, MIT Tech Review, IEEE Spectrum, InfoQ, The New Stack, Dark Reading, The Hacker News, SecurityWeek, BleepingComputer, CSO, The Record, KDnuggets, TDS, Analytics Vidhya). NIST AI 800-3, NIST AI 800-2 IPD, Stanford AI Index 2026 full PDF/dataset, International AI Safety Report extended summary, OWASP GenAI Q2 2026, major system-card candidates, and FLI Spring 2026 remained negative or unreleased.

**Apr 29 parallel news-search skill deep sweep (+12 verified items, ledger placement refined the same day after manual PDF + web verification):**
- **Ledger 1 (+1):** DoD CDAO Responsible AI Toolkit (Dec 2024) names PyOD as a Production / High-maturity OOD-detection tool with a dedicated entry on p.49 and an embedded workflow link at Stage 3 Assessment §3.1.10. URLs include `github.com/yzhao062/pyod`, which names the author by GitHub username.
- **Ledger 2 (+3):** Sina / 机器之心Pro DoxBench syndication (#36w); Awesome Agents editorial section on Auditable Agents (#36y; names co-authors Yi Nian and Aojie Yuan, not Yue Zhao directly); Promptfoo + RAXE + SecTools.tw + Gist.Science DE + Fugu-MT cluster for No Attacker Needed (#36aa; mixed editorial / templated DB / AI-generated / aggregator, kept as a single row under the cluster convention).
- **Ledger 3 (+8):** SEDIMARK D3.1 p.18 names PyOD and TODS in the outlier-detection module (#66cc); Actimize US20230267468A1 patent names PyOD (#66cd; brings PyOD/COPOD/ECOD patent count to 7); PyOD tutorial / integration cluster (#66ce; HiveMQ Edge-to-Cloud production pipeline confirmed by code); CS-Paper-Checklist education / blog cluster (#66cf; Sayed Mohsin Reza credits Dr. Yue Zhao); The Autonomy Tax / Sovereign-OS platform cluster (#66cg); IET / Fairness or Fluency? / Someone Hid It platform cluster (#66ch); SecTools.tw 713 AI-generated coverage of Auditable Agents (#66ci; downgraded from initial Ledger 2 #36x placement after the page's "本文由 AI 產生、整理與撰寫" disclaimer was found); SecTools.tw 854 AI-generated coverage of Agent Audit (#66cj; same downgrade from initial #36z).
- **Ledger 4 (+0):** USC Viterbi "USC at ICLR 2026" institutional PR was initially placed in Ledger 2 as #36v, then evaluated for Ledger 4 institutional, then dropped from the count entirely — USC institutional PR for conference papers is treated as out of scope going forward (legacy USC PR rows #17, #18, #18b-e in Ledger 2 are kept in place pending a future cleanup pass).
- **Existing clusters expanded without count changes:** AD-AGENT, CoAct, agent-style/anywhere-agents, Defenses Against Prompt Attacks, AD-LLM/NLP-ADBench, and tool long-tail rows.
- **Candidate excluded:** DeFinity Markets whitepaper was not counted because the direct PyOD/reference hit could not be reproduced from PDF text or web search.
- **Confirmed negatives:** No new direct hits in MarkTechPost, Synced, The Batch, The Gradient, VentureBeat, TechCrunch, Wired, MIT Tech Review, IEEE Spectrum, InfoQ, The New Stack, Dark Reading, The Hacker News, SecurityWeek, BleepingComputer, CSO, The Record, Forbes, Fortune, Bloomberg, Reuters, WSJ, or FT. No new direct citations found in OpenAI, Anthropic, DeepMind, Meta, xAI, OWASP, NIST, GAO, CRS, EU, OECD, UNESCO, RAND, Brookings, CSET, or Stanford HAI sources beyond the rows already recorded. FLI Spring 2026 was still not released/found.

**Running total: 267 verified items (252 prior + 7 May 13 Codex Phase A draft rows verified by Claude + 8 May 13 Claude independent wide-run rows verified by Claude, of which 2 unlocked via user manual verification: Datawhale WeChat lecture (added as #66dv) and ACM Computing Surveys "Towards Trustworthy AI" review (folded into the #66do cluster). An additional 4 May 13 wide-run leads (Microsoft Research TrustLLM, thepaper.cn TrustLLM, aiproductivity.ai Aegis, jiqizhixin TrustLLM) hit exact-URL duplicates of existing rows #7, #5, #21, #34b and are not counted as new rows; their May 13 verification work is recorded as evidence upgrades on those existing rows. The duplicate catch came from Codex Round 1 review of the wide-run draft.** Phase B verified-negative on manual check 2026-05-13: Stanford HAI 2026 AI Index Responsible AI chapter. The WebSearch snippet "uses the TrustLLM benchmark, a comprehensive framework spanning six dimensions" turned out to be a search-engine summarizer synthesis, not verbatim PDF text; the actual report does not name TrustLLM. Recorded in `news-search-candidates.jsonl` as a cautionary precedent. Lesson reinforced: never count a snippet-only Tier 0 / Tier 1 candidate without PDF or direct-fetch confirmation, even when the snippet reads as verbatim; this is the same failure mode as the 2026-05-07 GAO-26-108695 case. (The lesson belongs in `skills/news-search/references/search-strategy.md` as a named search-engine-summarizer-synthesis example; pending a separate commit to skill specs.) Next scheduled pass: 2-4 weeks. Watch for MarkTechPost/Synced coverage of Auditable Agents or Cat-DPO, follow-up Adobe/ACL/ACM roundups, and the next FLI AI Safety Index release.

---

**May 19 parallel news-search Full audit (8-lane parallel Phase A + 4-batch parallel Phase B + citation-audit hook integration):**

This round ran the complete `/news-search` Full audit pipeline for the first time as a single orchestrated workflow: 8 parallel Phase A agents fanned across Dimensions 1-8 (D9 is now the standalone [[citation-audit]] skill), aggregated to 166 unique candidate URLs, then 4 parallel Phase B verification agents fetched and applied the citation-verification rule. Net: **+21 verified ledger rows** plus citation-audit hook integration.

**Running total after May 19: 288 verified items (267 prior, per the coverage-matrix total, + 21 May 19 verified ledger rows).**

- **Ledger 1 (+0):** No new Tier 0 hits in the 6-day delta window. D8 PDF deep search scanned 22 fresh PDFs (Anthropic Opus 4.7, Mythos Preview, RSP v3.0/v3.1, OpenAI Sora 2, xAI Grok 4.1 + Frontier Framework, NIST AI 800-3 / GCR 26-069 / CSWP 50 / IR 8259r1, NIST NCCoE AI Agent ID/Authz, AISI Frontier Trends + Alignment Eval, FMF briefs, Five Eyes Careful Adoption Agentic AI Services, MITRE ATLAS OpenClaw, FINRA 2026 Annual Report, WEF Global Risks 2026, NBER w33998, OECD AI Papers No. 56, AuditBench, Anthropic Risk Report Feb 2026) — all 0 FORTIS term hits. Re-validated TrustLLM citation #881 in International AI Safety Report 2026 (already #8b). OWASP Gen AI Q2 2026 Solutions Landscape PDF was the highest-promise D4 lead but fetched 4.3 MB image-heavy PDF returned 0 FORTIS hits — track next quarterly OWASP refresh.

- **Ledger 2 (+0):** Mainstream press and institutional features dry in this window. USC Viterbi 'USC at ICLR 2026' institutional PR (`viterbischool.usc.edu/news/2026/04/usc-at-iclr-2026/`) does name DoxBench, Charts Are Not Images, and DecAlign with Yue Zhao credit — but per the Apr 29 audit rule USC institutional PR for conference papers is out of scope; not counted. The aiproductivity.ai best-agent-platforms blog (`aiproductivity.ai/blog/best-ai-agent-platforms/`) snippet claimed Aegis + agent-audit references but the page returned HTTP 403 to WebFetch; flagged for manual logged-in re-fetch (see Manual Verification Backlog below).

- **Ledger 3 (+7):** Ecosystem adoption and dedicated platform/tutorial rows:
  - **L3.1** (D5) [Doxing via the Lens: Revealing Location-related Privacy Leakage on Multi-modal L](https://liner.com/review/doxing-via-the-lens-revealing-locationrelated-privacy-leakage-on-multimodal). Verified via WebFetch: Names DoxBench dataset and lists 'Weidi Luo, Tianyu Lu and 9 others' as authors (Yue Zhao would be among 9 others but not explicitly quoted). Page carries explicit AI-generation disclaimer 'This...
  - **L3.2** (D5) [[Literature Review] AD-AGENT: A Multi-agent Framework for End-to-end Anomaly Det](https://www.themoonlight.io/en/review/ad-agent-a-multi-agent-framework-for-end-to-end-anomaly-detection). Verified via WebFetch: paper title cited (rule 1 hit). No author/institution attribution. Moonlight is an aggregator with implicit AI-generation framing ('Moonlight, your AI research colleague'). Caps Tier 3. Ledger 3...
  - **L3.3** (D5) [[Literature Review] DrugAgent: Automating AI-aided Drug Discovery Programming th](https://www.themoonlight.io/en/review/drugagent-automating-ai-aided-drug-discovery-programming-through-llm-multi-agent-collaboration). Verified via WebFetch: paper title cited; no author/institution attribution. Same aggregator pattern as AD-AGENT/Moonlight. Caps Tier 3. Ledger 3 ecosystem.
  - **L3.4** (D5) [[Multi-Agent Framework] DrugAgent: Automating AI-Driven Drug Discovery Programmi](https://readqvick.medium.com/multi-agent-framework-drugagent-automating-ai-driven-drug-discovery-programming-with-4ad68122dcbf). Verified via WebFetch (after 302 redirect to medium.com/advancedai/...): Medium AdvancedAI publication post by QvickRead summarizing DrugAgent. Direct arXiv link (rule 6) and paper title citation. Tier 3 dedicated blo...
  - **L3.5** (D5) [[Literature Review] StealthRank: LLM Ranking Manipulation via Stealthy Prompt Op](https://www.themoonlight.io/en/review/stealthrank-llm-ranking-manipulation-via-stealthy-prompt-optimization). Verified via WebFetch: paper title cited. No author/institution. Aggregator pattern. Caps Tier 3. Ledger 3.
  - **L3.6** (D5) [Chapter 3: Empirical Cumulative Distribution-based Outlier Detection (ECOD)](https://www.linkedin.com/pulse/handbook-anomaly-detection-python-outlier-3-ecod-kuo-ph-d-cpcu). VERIFIED via WebFetch: LinkedIn Pulse handbook chapter dedicated to ECOD by Chris Kuo, PhD (CPCU), published Jan 28 2023. Direct verbatim TKDE 2022 citation naming Yue Zhao as co-author + extensive use of PyOD library...
  - **L3.7** (D6) [Moonlight literature review — MacrOData](https://www.themoonlight.io/en/review/macrodata-new-benchmarks-of-thousands-of-datasets-for-tabular-outlier-detection). Moonlight.io is an ai-aggregator domain class (hard cap at Tier 3). The review names ADBench by tool name (rule 1 met) but does not name Han et al. or Yue Zhao. Suggest add to existing Ledger 3 platform cluster — poss...

- **Ledger 4 (+13):** First-party / academic community rows:
  - **L4.1** (D5) [Paper page - Doxing via the Lens: Revealing Privacy Leakage in Image Geolocation](https://huggingface.co/papers/2504.19373). Verified via WebFetch: HF paper page lists Yue Zhao (USC) as co-author. First-party paper page; route to Ledger 4 (first-party/community).
  - **L4.2** (D5) [GEO-Detective: Unveiling Location Privacy Risks in Images with LLM Agents](https://arxiv.org/html/2511.22441). Verified via WebFetch: downstream paper cites DoxBench with abbreviated reference key [LZLLZXX25] (which decodes to Luo-Lu-Liu-Liu-Zhang-Hu-Xiang-Xiao-25, FORTIS co-authors). Academic downstream citation; route to Led...
  - **L4.3** (D5) [AD-AGENT: A Multi-agent Framework for End-to-end Anomaly Detection - ACL Antholo](https://aclanthology.org/2025.findings-ijcnlp.11/). Verified via WebFetch: canonical academic publication page (Findings IJCNLP-AACL 2025, pages 191-205, DOI 10.18653/v1/2025.findings-ijcnlp.11). Yue Zhao co-author confirmed. Ledger 4 (first-party/community) / first-pa...
  - **L4.4** (D5) [Chasing Compute - Foundation Model Research](https://mit-calc.csail.mit.edu/). Verified via WebFetch: MIT CSAIL Chasing Compute project home page lists Yue Zhao as co-author with affiliation 'School of Advanced Computing, USC' AND the full paper title 'Chasing Compute: The Role of Computing Reso...
  - **L4.5** (D5) [Defenses Against Prompt Attacks Learn Surface Heuristics / alphaXiv](https://www.alphaxiv.org/overview/2601.07185). Verified via WebFetch: alphaXiv overview page for arXiv 2601.07185. Title matches; alphaXiv is academic-community surface (other alphaXiv pages already in baseline at Ledger 4). Ledger 4 (first-party/community).
  - **L4.6** (D5) [Agent Banana: High-Fidelity Image Editing with Agentic Thinking and Tooling / al](https://www.alphaxiv.org/abs/2602.09084). Verified via WebFetch: alphaXiv overview page for arXiv 2602.09084. Title matches. Ledger 4 (first-party/community).
  - **L4.7** (D5) [Paper page - Agent Banana: High-Fidelity Image Editing with Agentic Thinking and](https://huggingface.co/papers/2602.09084). Verified via WebFetch: full HF paper page. Yue Zhao (USC) as co-author 9 of 13. First-party paper page; Ledger 4 (first-party/community).
  - **L4.8** (D5) [SkillSieve: A Hierarchical Triage Framework for Detecting Malicious AI Agent Ski](https://arxiv.org/pdf/2604.06550). VERIFIED via pdf_term_scan.py: SkillSieve cites FORTIS Agent Audit (Zhang, Nian, Zhao 2026) as reference [25]. Ledger 4 (first-party/community) downstream citation; route to Ledger 4 first-party/community OR D6 citati...
  - **L4.9** (D5) [ECOD: Unsupervised Outlier Detection Using Empirical Cumulative Distribution Fun](https://publications.pik-potsdam.de/pubman/faces/ViewItemFullPage.jsp;jsessionid=6mmJz7UditS93d-Lm2hwFDbtnkulHLbLNJ1DtvCR.se97?itemId=item_26927_1&view=EXPORT). Verified via WebFetch: PIK Potsdam publications repository entry for ECOD. Two PIK authors (Nicola Botta, Cezar Ionescu) are co-authors on the paper, so this is a coauthor-institution publication listing (not external...
  - **L4.10** (D6) [MacrOData: New Benchmarks of Thousands of Datasets for Tabular Outlier Detection](https://arxiv.org/abs/2602.09329). Direct follow-up paper by Akoglu lab (CMU) extending ADBench. Verified citation of ADBench Han et al. 2022 in arXiv HTML body and references. New downstream academic citation; complements 66cs / 66ca tool-long-tail cl...
  - **L4.11** (D6) [Awesome-Anomaly-Detection-with-Large-Language-Model (mala-lab)](https://github.com/mala-lab/Awesome-Anomaly-Detection-with-Large-Language-Model). NEW mala-lab curated list (sister to baseline foundation-models repo). Names PyOD 2 (with yzhao062 code link) and AD-LLM (FORTIS work). Suggest add to Ledger 3 platform cluster row alongside existing mala-lab tracking...
  - **L4.12** (D6) [Awesome-Deep-Graph-Anomaly-Detection (mala-lab, TKDE 2025 survey companion)](https://github.com/mala-lab/Awesome-Deep-Graph-Anomaly-Detection). NEW mala-lab curated list, TKDE 2025 survey companion (Qiao, Tong, An, King, Aggarwal, Pang, "Deep Graph Anomaly Detection: A Survey and New Perspectives"). Names PyOD 2 (yzhao062 code link) and BOND benchmark. The TK...
  - **L4.13** (D7) [【世界初】OOD検出 ≅ NEITHER ≅ 龍樹の空 — 機械学習と中観仏教の構造的同型 (PyOD 20アルゴリズム実証) #異常検知](https://qiita.com/fc0web/items/5193208c7403b871126b). language=ja; verified Phase B 2026-05-19 via WebFetch. Article cites PyOD JMLR 2019 with author Zhao Y. (rule 1+2 met). Apr 8-9 2026 publication. Novel framing (Buddhist Madhyamaka philosophy + PyOD empirical run on 2...

- **Ledger 5 (+1):** Awards and recognitions:
  - **L5.1** (D1) [Award Recipients - ACM SIGSPATIAL](https://www.sigspatial.org/people/award-recipients/). Direct mention confirmed: official ACM SIGSPATIAL award index naming Yue Zhao (USC) as co-author of Best Short Paper (TyphoFormer). Canonical first-party award page. Ledger 5 (awards/recognitions). Complements existin...

- **Citation-affiliation hook (from /citation-audit; this is the formerly D9 dimension, now its own skill at `skills/citation-audit/`):** Embedded full Tier 0 and Tier 1 tables from `citation-affiliation-audit.md` (regenerated 2026-05-19 with the OpenAlex + Dimensions Analytics two-source combined audit after two real-data bug fixes: arXiv ID Dimensions DSL field requires the `arXiv:` prefix, and the default search type is `full_data` not `title_only` — both bugs caught by running the audit, not by static review). Headline numbers: 102 non-survey papers, OpenAlex found 43 with citations (1,624 unique citing papers), Dimensions found 30 (1,176 unique citing papers), 7 cross-source confirmed. **Tier 0 institutions citing FORTIS work: 39 entries** (notable: NIH × 3, Brookhaven × 3, Sandia × 2, LANL × 2, PNNL × 1, Argonne × 1, JPL × 1, DLR × 1, DESY × 1, Bundesbank × 3, CDC × 1, Meta Platforms × 5, OpenAI × 2, Google DeepMind × 1, RAND × 1). **Tier 1 institutions: 207 entries** (Microsoft Research 9, Tencent 8, AstraZeneca 7+5, IBM Research Zurich 7, Amazon 6+3, IBM Watson 6, Microsoft Research Asia 7, Adobe 5+2, Huawei 5+3, Alibaba 5, Merck 5+4, BlackRock 3+2, Visa 2+1, Robert Bosch 3+1, etc.). The embedded tables follow this round summary.

- **Topic Validation (+56):** D4 topic-proximity sweep produced 56 topic-only rows (broad agent-security, anomaly-detection landscape, ChatGPT geolocation phenomenon coverage) recorded as context for grant narratives but not counted as direct coverage. Not enumerated individually — see `skills/news-search/scratch/phase-b-verified-B_paper.jsonl` and `phase-b-verified-A_news.jsonl` (`tier_guess: topic-validation`).

- **Verified-negative recorded (+33):** Major FM-co system cards (Anthropic Opus 4.7, Mythos Preview, RSP v3.0/v3.1, Risk Report Feb 2026; OpenAI Sora 2; xAI Grok 4.1, Frontier Framework), NIST series (AI 800-3, GCR 26-069, CSWP 50, IR 8259r1, NCCoE AI Agent ID/Authz Concept Paper), AISI (Frontier Trends, Alignment Eval arXiv:2604.00788), FMF (3 issue briefs), Five Eyes Careful Adoption Agentic AI Services guide, MITRE ATLAS OpenClaw Investigation MTR-26-00176-1, FINRA 2026 Annual Regulatory Oversight Report, WEF Global Risks Report 2026, NBER w33998 'AI and the Fed', OECD AI Papers No. 56 (Feb 2026), AuditBench (arXiv:2602.22755), OWASP Gen AI Q2 2026 Solutions Landscape, CVPR 2026 ComputeReporting policy page + CRF PDF (does NOT name the Hao/Zhao/Ghassemi paper that motivated the policy), npj AI s44387-026-00076-4 (paywall held — see manual verification backlog), ACM CSUR Jun 2026 diffusion survey (10.1145/3783986, verified via arXiv preprint 2404.18886v3 — does NOT cite the Yang/.../Zhao 2023 CSUR diffusion survey).

- **Disambiguation registry recommendations (add to `skills/news-search/references/disambiguation-registry.md`):**
  - **Hangbo Zhao** — USC AME/BME assistant professor, junior research award recipient 2026. Surfaced as false positive on the USC Viterbi 'People Behind the Work 2026 Awards' page under Yue Zhao searches.
  - **Wei Zhao (SiriuS)** — *Zhao, W. et al. (2025), SiriuS: Self-improving multi-agent systems via bootstrapped reasoning, arXiv:2502.04780*. Surfaced as 'Zhao et al., 2025[49]' in OECD AI Papers No. 56 (Feb 2026, p.20).
  - **AuditLuma** — CSDN-hosted AI code-audit project. Recurring collision target for `agent-audit` queries; not related to FORTIS agent-audit.
  - **Moonshot AI Kiwi-do** — different from Moonlight.io paper-aggregator outlet (the 'Moonlight' name collision).
  - **Hangbo Zhao + Wei Zhao + AuditLuma + Moonshot Kiwi-do**: 4 new collision targets logged this round.

- **Domain registry harvest (add to `skills/news-search/references/domain-registry.md`):**
  - `mit-calc.csail.mit.edu` (class: `university` / coauthor-institution project page)
  - `publications.pik-potsdam.de` (class: `university` / coauthor-institution publications repository)
  - `medium.com/advancedai` (class: `tech-blog` / Medium publication)

- **Manual verification backlog (URLs that returned 403 / 404 / paywall and need a logged-in browser re-fetch):**
  - `aiproductivity.ai/blog/best-ai-agent-platforms/` — snippet claimed Aegis + agent-audit references; verify direct mention or set verified-negative.
  - `tomshardware.com/.../chatgpt-becomes-a-formidable-geo-guesser` — phenomenon-discovery piece; verify whether DoxBench is named or only the underlying ChatGPT capability.
  - `www.nature.com/articles/s44387-026-00076-4` — npj AI healthcare review (Mar 2026); 303 → idp.nature.com auth. May overlap with existing #66cr TrustLLM npj cluster.
  - `sciencedirect.com/.../S1566253525005895` — Elsevier Information Fusion AD foundation-models survey; 403.
  - `securityboulevard.com/2026/02/openclaw-...` — 403 (cross-post of NSFOCUS analysis; NSFOCUS original was verified-negative for FORTIS).
  - `aimodels.fyi/papers/arxiv/jaildam-...` — 403 (likely aggregator; tier cap 3 if reachable).
  - `researchgate.net/publication/402481760_Sovereign-OS` — 403 (ResearchGate routinely blocks WebFetch).
  - `forum.cspaper.org/topic/170/...` — 301 → article removed.
  - `github.com/openclaw/openclaw/discussions/36663` — 410 'Discussions disabled' (phantom from search-engine cache).
  - `paperswithcode.com/paper/stealthrank-...` — 302 → 404.
  - GAO 26-107859 + GAO 25-107197 + fdd.org Mar 2026 + federalnewsnetwork May 2026 — all 403 to WebFetch.

- **D10 External Deep Research:** Out of scope for this automated audit pass. The user runs this manually in ChatGPT Deep Research / Gemini Deep Research / claude.ai with a self-contained prompt; output goes to `external-research/{source}-2026-05.md`. Prompt template generated in this audit cycle is at `external-research/PROMPT-2026-05-19.md` (see file). Run quarterly.

- **Codex Phase B review (skipped):** Codex review of Phase B output was skipped this round because the implementation-review cycle for the citation-audit skill split was already in flight earlier in the same session. The Phase A/B agents themselves apply the citation-verification rule with verbatim quotes; Codex review can be added in a follow-up pass if any of the 21 candidate-promote rows are questioned.

Lessons reinforced this round:
- **Static review does not catch API semantics.** Three /implement-review rounds + a smoke test all passed for the citation-audit Dimensions integration before this Full audit caught two real bugs (arxiv_id prefix, default search-type) only when actually running against the publication inventory. The fail-loud `_query_dimensions` wrapper from Round 1 of that review cycle paid off here.
- **Highest-promise topic-proximity lead was wrong.** OWASP Gen AI Q2 2026 Solutions Landscape PDF was flagged `phase_b_priority` by the D4 agent and was the single highest-promise D8-style PDF this round — fetched 4.3 MB, 0 hits. Worth retrying when the next OWASP edition lands.
- **PDF term scan beats LLM summarization for citation extraction.** B_paper Phase B caught a SkillSieve (arXiv:2604.06550) citation of agent-audit only via `pdf_term_scan.py`; the WebFetch summarizer missed it. Continue routing all candidate PDFs through the term scanner.

## Citation Affiliation Evidence (integrated from /citation-audit skill, 2026-05-19)

*The following section is integrated verbatim from `citation-affiliation-audit.md` per the news-search cross-skill citation-audit hook. Canonical copy lives in that separate file; this embed makes the unified report self-contained for tenure / promotion / grant readers. Re-run the standalone audit with `/citation-audit --source both` to refresh.*


*Generated: 2026-05-19 via OpenAlex + Dimensions*

**What this is:** Papers that cite your work, where at least one author is affiliated with a notable institution.
This means "researchers AT [institution] cited your tool" -- not "[institution] officially endorses your tool."

Per-source coverage of the 102 non-survey papers:
- **OpenAlex**: 43 papers with citations; 1624 unique citing papers analyzed.
- **Dimensions**: 30 papers with citations; 1176 unique citing papers analyzed.

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

**207 entries**

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
| Big Tech | Huawei Technologies (United States) | US | TODS: An Automated Time Series Outl | TAB: Unified Benchmarking of Time Series Anomaly Detection M | 2025 | openalex |
| Big Tech | Huawei Technologies (China) | CN | TODS: An Automated Time Series Outl | TAB: Unified Benchmarking of Time Series Anomaly Detection M | 2025 | openalex |
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
| Pharma | Eli Lilly and Co Ltd | United Kingdom | Therapeutics Data Commons: Machine  | Machine Learning for Toxicity Prediction Using Chemical Stru | 2025 | dimensions |
| Pharma | AstraZeneca AB | Sweden | Therapeutics Data Commons: Machine  | Machine Learning for Toxicity Prediction Using Chemical Stru | 2025 | dimensions |
| Pharma | Pfizer GmbH | Germany | Therapeutics Data Commons: Machine  | Machine Learning for Toxicity Prediction Using Chemical Stru | 2025 | dimensions |
| Pharma | Merck & Co Inc | United States | Therapeutics Data Commons: Machine  | Machine Learning for Toxicity Prediction Using Chemical Stru | 2025 | dimensions |
| Pharma | F Hoffmann La Roche AG | Switzerland | Artificial Intelligence Foundation  | Combinatorial prediction of therapeutic perturbations using  | 2025 | dimensions |
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
| Pharma | F Hoffmann La Roche AG | Switzerland | Artificial Intelligence Foundation  | Combinatorial prediction of therapeutic perturbations using  | 2024 | dimensions |
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
| Amazon (United States) | Big Tech | 6 |
| IBM Research - Thomas J. Watson Research Center | Big Tech | 6 |
| Adobe Systems (United States) | Big Tech | 5 |
| Huawei Technologies (China) | Big Tech | 5 |
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
| F Hoffmann La Roche AG | Pharma | 2 |
| Mayo Clinic in Florida | Healthcare | 1 |
| Amazon (Germany) | Big Tech | 1 |
| Jet Propulsion Laboratory | Space Agency | 1 |
| Siemens (China) | Industrial | 1 |
| Deutsches Zentrum für Luft- und Raumfahrt e. V. (DLR) | Space Agency | 1 |
| Intel (United Kingdom) | Big Tech | 1 |
| Microsoft (United States) | Big Tech | 1 |
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
| Eli Lilly and Co Ltd | Pharma | 1 |
| Pfizer GmbH | Pharma | 1 |
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

**Indexed but 0 citations (69):** Can Multimodal LLMs Perform Time Series , Charts Are Not Images: On the Challenges, CoAct: Co-Active LLM Preference Learning, Defenses Against Prompt Attacks Learn Su, Mitigating Hallucinations in Large Langu, "Someone Hid It": Query-Agnostic Black-B, Topology Matters: Measuring Memory Leaka, TrustGen: A Platform of Dynamic Benchmar, A Personalized Conversational Benchmark:, AD-AGENT: A Multi-agent Framework for En, DyFlow: Dynamic Workflow Framework for A, Edit Away and My Face Will Not Stay: Per, Few-Shot Graph Out-of-Distribution Detec, JailDAM: Jailbreak Detection with Adapti, LLM-Empowered Patient-Provider Communica, Learning from the Storm: A Multivariate , MetaOOD: Automatic Selection of OOD Dete, NLP-ADBench: NLP Anomaly Detection Bench, Navigating Between Explainability and Ex, Retrieval-Reasoning Large Language Model, ... and 49 more

**Not found (3):** AutoDavis: Automatic and Dynamic Evaluat, Automatic Unsupervised Outlier Model Sel, Revisiting Time Series Outlier Detection

*OpenAlex coverage improves over time. Re-run in 3-6 months to capture newly indexed papers; Dimensions has better CS coverage and complements OpenAlex on per-paper citation graphs.*

*Cross-source dedup uses exact (institution, citing_title, cited_work) matching. Variants like 'Google' vs 'Google LLC' or punctuation-variant titles may produce near-duplicate rows that span sources.*
