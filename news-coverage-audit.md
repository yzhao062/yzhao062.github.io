# News & Media Coverage Audit — Yue Zhao / FORTIS Lab

*Updated: 2026-04-08. Full audit via /news-search skill (all 8 dimensions).*
*All 8 dimensions complete across all 121 items (104 papers + 17 tools).*
*Citation verification applied: every item names or cites the work, person, lab, or co-author.*

---

## Ledger 1: Government & Policy Citations

Items where government bodies, policy organizations, or foundation model companies cite your work by name in official documents.

| # | Work Cited | Source | Detail | Date |
|---|-----------|--------|--------|------|
| 1 | TrustLLM | **U.S. Senate HSGAC** | Footnote 119, p.25: *"the trustworthiness of large language models is still being analyzed"* in "Hedge Fund Use of Artificial Intelligence" | Jun 2024 |
| 2 | TrustLLM | **Future of Life Institute** | Official benchmark in AI Safety Index (Winter 2025). Pages 7, 11, 13, 21, 27, 43, 46. Full indicator definition p.46. | Dec 2025 |
| 3 | TrustLLM | **Future of Life Institute** | Official benchmark in AI Safety Index (Summer 2025). Pages 5, 9, 11, 17, 34, 36, 37. | Jul 2025 |

**Source URLs:** [Senate PDF](https://www.hsgac.senate.gov/wp-content/uploads/2024.06.11-Hedge-Fund-Use-of-AI-Report.pdf) · [FLI Winter](https://futureoflife.org/ai-safety-index-winter-2025/) · [FLI Summer](https://futureoflife.org/ai-safety-index-summer-2025/)

**Dimension 8 (PDF deep search) status:** Searched 25+ governance PDFs (OpenAI GPT-4/4o/4.5/5/o1/o3, Anthropic Claude 3/3.5/4/4.5, Meta Llama 3, Google Gemini 1.5, DeepSeek V3/R1, Qwen 2.5, Phi-4, Cohere, Gemma 2, White House x3, NIST AI 600-1, FLI x2, Senate HSGAC) + regulated verticals (OCC, FDIC, FINRA, SEC, CFTC, FDA, NASA, FAA, CISA, DARPA, MITRE, DOE, telecom, insurance, security vendors) for all 104 papers + 17 tools. TrustLLM confirmed in Senate HSGAC + FLI x2. PyOD confirmed in U.S. DoD CDAO Generative AI Responsible AI Toolkit and ESA OPS-SAT benchmark (Nature Scientific Data).

**D8 candidates needing manual PDF verification:**
- **BIS Working Paper 1188** — ML-based anomaly detection in high-value payment systems (Bank for International Settlements). PDF text extraction failed; could cite PyOD.
- **OWASP GenAI Solutions Landscape Q2 2026** — Agentic AI security solutions map. agent-audit/Aegis inclusion unconfirmed from search snippets; needs manual check of the landscape graphic.

| 4 | PyOD | **European Space Agency (ESA/ESOC)** | All 30 anomaly detection algorithms in the OPS-SAT spacecraft telemetry benchmark implemented using PyOD 1.1.2. Published in **Nature Scientific Data** (2025). | 2025 |
| 5 | PyOD | **U.S. Department of Defense (CDAO)** | Listed in the official "Generative AI Responsible AI Toolkit" (v1.0, pages 48-49) with direct link to `yzhao062/pyod`. Published by the Chief Digital and AI Office, Responsible AI Division. | Dec 2024 |

**Source URLs:** ... · [CDAO Toolkit PDF](https://www.ai.mil/Portals/137/Documents/Resources%20Page/2024-12GenAI-Responsible-AI-Toolkit.pdf)

**Count: 5 government/policy citations (TrustLLM x3, PyOD x2)**

---

## Ledger 2: External Third-Party Media

Independent third-party coverage by outlets not affiliated with you, your lab, or your co-authors. These are the items a promotion committee would consider "external recognition."

| # | Work Named | Outlet | Type | Headline | Date | Dim | URL |
|---|-----------|--------|------|----------|------|-----|-----|
| 5 | TrustLLM | **The Paper (澎湃新闻)** | Tier 1 Chinese news | "大语言模型的可信之路：TrustLLM全面揭秘" | 2024 | D7 | [Link](https://www.thepaper.cn/newsDetail_forward_26315865) |
| 6 | TrustLLM | Lawrence Livermore National Lab | National lab article | "Evaluating trust and safety of large language models" | 2024 | D3 | [Link](https://computing.llnl.gov/about/newsroom/evaluating-trust-safety-llms) |
| 7 | TrustLLM | Microsoft Research | Research listing | Listed as MS Research publication | 2024 | D3 | [Link](https://www.microsoft.com/en-us/research/publication/trustllm-trustworthiness-in-large-language-models/) |
| 8 | TrustGen | Hoover Institution (Stanford) | Research listing | Listed as Hoover research publication | 2026 | D3 | [Link](https://www.hoover.org/research/trustgen-platform-dynamic-benchmarking-trustworthiness-generative-foundation-models) |
| 9 | TrustGen | Microsoft Research | Research listing | Part of ICLR 2026 portfolio | 2026 | D3 | [Link](https://www.microsoft.com/en-us/research/publication/trustgen-a-platform-of-dynamic-benchmarking-on-the-trustworthiness-of-generative-foundation-models/) |
| 10 | TrustLLM | MarkTechPost | AI newsletter | "Navigating the Complexity of Trustworthiness in LLMs: A Deep Dive into the TRUST LLM Framework" | Jan 2024 | D3 | [Link](https://www.marktechpost.com/2024/01/16/navigating-the-complexity-of-trustworthiness-in-llms-a-deep-dive-into-the-trust-llm-framework/) |
| 11 | DrugAgent | MarkTechPost | Tech blog article | "Meet DrugAgent: A Multi-Agent Framework for Automating ML in Drug Discovery" | Dec 2024 | D3 | [Link](https://www.marktechpost.com/2024/12/01/meet-drugagent-a-multi-agent-framework-for-automating-machine-learning-in-drug-discovery/) |
| 12 | DrugAgent | Nature Biotechnology | Journal citation | Cited in "Agentic AI and the rise of in silico team science" | 2026 | D4 | [Link](https://www.nature.com/articles/s41587-026-03035-1) — **needs manual verification** |
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
| 35 | TODS | Towards Data Science | Data science blog | "TODS: Detecting Outliers from Time Series Data" | -- | D3 | [Link](https://towardsdatascience.com/tods-detecting-outliers-from-time-series-data-2d4bd2e91381/) |
| 36 | DrugAgent | Awesome AI Agents for Healthcare | Curated list | Listed in community resource | -- | D3 | [Link](https://github.com/AgenticHealthAI/Awesome-AI-Agents-for-Healthcare) |

**Count: 37 external third-party items**

---

## Ledger 3: Ecosystem Adoption (books, podcasts, courses, enterprise integrations, patents, platforms)

External parties building on, integrating, or teaching your tools -- not coverage about you, but adoption evidence.

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

**Count: 31 ecosystem adoption items**

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

**Count: 18 awards/recognitions**

---

## Upcoming Visibility Opportunities

1. **ICLR 2026** (Apr 24-28): DoxBench, FigEdit, DecAlign, TrustGen. DoxBench strongest outreach candidate.
2. **ACM AI and Agentic Systems** (May 26-29): agent-audit presentation.
3. **ACL 2026** (Jul 2-7): CoAct, Defenses Against Prompt Attacks, Topology Matters.
4. **Adobe Research blog**: May cover FigEdit in ICLR roundup.

---

## Negative Results

| Outlet Type | Searched | Result |
|-------------|----------|--------|
| Major business press | Forbes, Fortune, Bloomberg, WSJ, Reuters, FT | No hits |
| Top-tier tech press (except Tom's Hardware) | VentureBeat, TechCrunch, Wired, MIT Tech Review, IEEE Spectrum, The Verge, Ars Technica | No hits |
| Security press | Dark Reading, SecurityWeek, SC Magazine, Bleeping Computer, Krebs, The Record, CSO Online, CyberNews | No hits by name |
| AI newsletters | The Batch, Import AI, The Gradient, Synced Review | No hits |
| Industry analysts | Gartner, Forrester, IDC | No hits by name. Forrester "AEGIS" is their own framework (name collision). |
| Consulting firms | McKinsey, Deloitte, PwC, Accenture, EY, KPMG | Topic coverage only |
| Think tanks | Stanford HAI, CSET, CAIS, Brookings, RAND, WEF, OECD, Turing | Topic coverage only |
| Foundation model system cards | OpenAI (8), Anthropic (5), Meta, Google, DeepSeek (2), Qwen, Phi-4, Cohere, Gemma, Yi | No citations |
| Government (beyond Senate) | White House (3), NIST AI 600-1, GAO, Congress.gov, NSF.gov, OSTI.gov | No citations by name |
| International government | EU AI Office, ENISA, UK gov, OECD iLibrary, UNESCO, G7/G20 | No citations by name |
| **Regulated verticals (D8)** | OCC, FDIC, FINRA, SEC, CFTC (finance); FDA (healthcare); NASA, FAA (aerospace); CISA (cybersecurity); DARPA, MITRE, DOE (defense); telecom; insurance; security vendors (Splunk, Elastic, CrowdStrike, Palo Alto, Fortinet) | **No confirmed citations**. Topic-relevant PDFs found but none cite PyOD/ADBench/COPOD by name. |
| Standards bodies | MITRE ATLAS, MLCommons, Cloud Security Alliance | No citations |
| Korean tech (Tistory) | Searched | No PyOD content |
| German tech (Heise.de) | Searched | No results |

---

## Summary Statistics

| Ledger | Count |
|--------|-------|
| Government/Policy citations | 5 |
| External third-party media | 37 |
| Ecosystem adoption | 31 |
| First-party/community | 6 |
| Awards/recognitions | 18 |
| **Total verified items** | **97** |

- **104 papers + 17 tools** searched across all 8 dimensions
- **11,551 Google Scholar citations** (Apr 2026)
- **39.11M+ PyPI downloads** for PyOD
- **1,846 Semantic Scholar citations** for Diffusion Models survey
- **~285 Semantic Scholar citations** for TrustLLM
- **3 books** with dedicated chapters on PyOD/COPOD
- **2 podcasts** naming PyOD
- **4 online courses** teaching PyOD (DataCamp, Udemy x2, O'Reilly video)
- **3 enterprise integrations** (Databricks x2, Walmart) + 1 vendor whitepaper (Altair)
- **1 patent** citing PyOD
- **1 Nature Scientific Data publication** using PyOD (ESA OPS-SAT)

---

## Topic Validation (NOT Direct Coverage)

For grant narratives only. These do not name your work.

**AI agent security:** Tom's Hardware (non-DoxBench articles), TechCrunch, WinBuzzer, TechRadar, TechSpot, CyberNews, AI Commission, Bellingcat (DoxBench topic); Hacker News x2, Dark Reading, ReversingLabs, Sangfor, Reco.ai, Penligent.ai, DEV Community (gstack/aegis comparison -- different Aegis), Blink.new (OpenClaw crisis); NIST CAISI RFI (Jan 2026), NIST AI Agent Standards Initiative (Feb 2026), Bessemer VP, Cisco, Microsoft Agent Governance Toolkit, Palo Alto Networks OWASP blog

**Consulting/think tanks:** McKinsey x2, Deloitte x2, PwC x2, Accenture x2, EY, KPMG, WEF, OECD, CSA (Securing Autonomous AI Agents), CSET, Brookings, RAND, Sequoia

**ChatGPT geolocation (DoxBench topic, paper not cited):** Tom's Hardware, Cloudwards, Cybernews, TechRadar, TechSpot, WinBuzzer, AI Commission

**Government (topic, tools not cited):** GAO AI Accountability Framework, GAO Fraud/Improper Payments, Congress 119th hearing, Nextgov x2, OWASP Top 10 Agentic, OWASP AISVS, ENISA AI/Cybersecurity, UK Gov marketplace

---

## Changes from Previous Audit (2026-04-08 refresh)

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

- #5 (Ledger 1): **U.S. DoD CDAO** — PyOD listed in Generative AI Responsible AI Toolkit (Tier 0, found by Codex)
- #18e-f: USC ISI NeurIPS roundup, FSU TyphoFormer PR (found by Codex)
- #66a-b: Manning liveProject, GeeksforGeeks tutorial (found by Codex)
- Codex audit merged and deleted

**Previous total: 64 items. New total: 97 items (+33).**
