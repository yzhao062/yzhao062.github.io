# Base Query Bank

Curated base queries for the news-search skill. This bank covers high-priority outlets and tools but is not exhaustive. For triage rules on when to add queries at runtime, see the "Query Bank Triage Rules" section in `SKILL.md`. For Dimension 3, any outlet in `outlet-registry.md` without a query here should be searched at runtime using the generation rule in `SKILL.md`.

Replace `{YEAR}` with the current year and `{YEAR-1}` with the previous year. Queries are grouped by dimension.

---

## § Dimension 1: Person & Lab

```
"Yue Zhao" USC "AI auditing" news {YEAR-1} {YEAR}
"Yue Zhao" USC interview podcast keynote speaker {YEAR-1} {YEAR}
"Yue Zhao" USC quoted expert AI safety security agent news article {YEAR-1} {YEAR}
"FORTIS lab" USC news award {YEAR}
"Yue Zhao" USC award fellowship grant recognition {YEAR-1} {YEAR}
"Yue Zhao" Anthropic OR Amazon OR NVIDIA OR Google OR Meta award {YEAR}
"Yue Zhao" USC anomaly detection NASA Tesla "Morgan Stanley" government
"Yue Zhao" USC VentureBeat OR TechCrunch OR Wired OR "MIT Technology Review" OR "IEEE Spectrum"
"Yue Zhao" "Carnegie Mellon" OR USC award fellowship recognition honor {YEAR-1} {YEAR}
"Yue Zhao" cited quoted expert AI safety security agent news article {YEAR-1} {YEAR}
```

## § Dimension 2: Tools in Non-Academic Contexts

### PyOD (highest adoption — run all queries)

```
PyOD anomaly detection enterprise deployment production industry
PyOD fraud detection cybersecurity industry report {YEAR-1} {YEAR}
PyOD anomaly detection NIST government federal report
PyOD cited textbook course university education
PyOD Walmart OR NASA OR Tesla OR "Morgan Stanley" OR "U.S. Senate"
PyOD patent cited enterprise
PyOD outlier detection Gartner Forrester McKinsey enterprise report
PyOD anomaly detection KDnuggets "Towards Data Science" featured {YEAR-1} {YEAR}
"anomaly detection" "open source" landscape comparison PyOD scikit-learn {YEAR-1} {YEAR} report
PyOD library fraud detection cybersecurity industry report {YEAR-1} {YEAR}
```

### TrustLLM

```
TrustLLM benchmark LLM trustworthiness news {YEAR-1} {YEAR}
TrustLLM AI safety policy government regulation benchmark cited
"AI Safety Index" "Future of Life" TrustLLM benchmark cited evaluated {YEAR}
TrustLLM cited enterprise safety evaluation deployed
```

### agent-audit

```
agent-audit OWASP agentic security scan vulnerabilities {YEAR}
"agent-audit" "Yue Zhao" ClawHub scan vulnerabilities {YEAR}
agent-audit ClawHub vulnerabilities news coverage {YEAR}
OpenClaw agent-audit security scanner OWASP agentic 18899 skills
```

### Aegis

```
Aegis "AI agent firewall" open source tool call security {YEAR}
"No Tool Call Left Unchecked" Aegis firewall pre-execution news blog
Aegis AI agent security "Justin0504" "Aojie Yuan" blog post news
```

### anywhere-agents

```
anywhere-agents "portable AI agent config" Claude Code Codex {YEAR}
anywhere-agents "AGENTS.md" "PreToolUse guard" destructive git block news blog
"anywhere-agents" "Yue Zhao" writing routing skills agent config post
site:pypi.org anywhere-agents OR "Yue Zhao"
site:readthedocs.io "anywhere-agents" documentation adoption
```

### agent-style

```
agent-style "AI writing rules" Claude Code Codex Copilot AGENTS.md {YEAR}
"agent-style" "Yue Zhao" style rules LLM prose generation news blog
agent-style PyPI "drop-in rules package" LLM writing guide tutorial
site:pypi.org/project/agent-style downloads adoption
"AGENTS.md" style-review "agent-style" skill invocation {YEAR}
```

### Other tools (run selectively — include any tool with 500+ stars or known media hooks)

```
ADBench anomaly detection benchmark NeurIPS news coverage
PyGOD graph outlier detection library JMLR news
SUOD outlier detection acceleration MLSys news
"Therapeutics Data Commons" TDC drug discovery news {YEAR-1} {YEAR}
TrustEval-toolkit trustworthiness generative foundation models benchmark
NLP-ADBench anomaly detection NLP benchmark EMNLP
AD-LLM benchmarking large language models anomaly detection
TODS time-series outlier detection system AutoML
combo machine learning model combination ensemble library
LangSkills evidence-backed skill library AI agents
CS-Paper-Checklist research paper quality checklist
Anomaly-Detection-Resources curated resource hub
```

## § Dimension 3: Outlet Sweep

Run one query per outlet or outlet family. Do NOT combine `site:` filters with OR — per search-strategy.md, this fails silently.

### Security press

```
site:darkreading.com "anomaly detection" OR "AI auditing" OR "agent security" OR PyOD
site:securityweek.com "anomaly detection" OR "AI auditing" OR "agent security" OR PyOD
site:scmagazine.com "anomaly detection" OR "AI auditing" OR "agent security"
site:bleepingcomputer.com AI agent security firewall audit {YEAR}
site:therecord.media AI agent security audit {YEAR}
site:krebsonsecurity.com AI agent security {YEAR}
site:thehackernews.com AI agent security ClawHub OpenClaw {YEAR}
site:csoonline.com AI agent security auditing {YEAR}
```

### Business press

```
site:forbes.com "anomaly detection" OR "AI auditing" OR PyOD
site:fortune.com "anomaly detection" OR "AI auditing" OR PyOD
site:bloomberg.com "anomaly detection" OR "AI auditing" OR "outlier detection"
site:wsj.com AI agent security auditing {YEAR}
site:reuters.com AI agent security auditing {YEAR}
```

### Top tech press

```
site:venturebeat.com PyOD OR "anomaly detection" OR "AI agent security" OR TrustLLM
site:thenewstack.io "anomaly detection" OR "AI agent security" OR PyOD
site:infoq.com "anomaly detection" OR "AI agent security" OR TrustLLM
site:techcrunch.com "anomaly detection" OR "AI auditing" OR PyOD
site:wired.com "anomaly detection" OR "AI auditing" OR PyOD
site:technologyreview.com "anomaly detection" OR "AI auditing"
site:spectrum.ieee.org anomaly detection OR AI auditing OR agent security
```

### AI newsletters & blogs

```
site:deeplearning.ai PyOD OR TrustLLM OR "anomaly detection"
site:marktechpost.com "Yue Zhao" OR PyOD OR TrustLLM OR "anomaly detection"
site:syncedreview.com PyOD OR TrustLLM OR "AI auditing" OR "Yue Zhao"
site:thegradient.pub "anomaly detection" OR "AI auditing" OR "Yue Zhao"
```

### Science press

```
site:nature.com "Yue Zhao" anomaly detection OR "AI auditing"
site:science.org "Yue Zhao" anomaly detection OR "AI auditing"
site:scientificamerican.com anomaly detection AI agent security
site:newscientist.com anomaly detection AI agent security
```

### Government & policy

```
NSF award "Yue Zhao" OR "FORTIS lab" anomaly detection AI auditing
NIST AI agent security considerations RFI {YEAR}
"AI Safety Index" "Future of Life" TrustLLM benchmark cited
Federal Register AI agent security {YEAR}
site:gao.gov artificial intelligence anomaly detection audit
site:crs.gov artificial intelligence anomaly detection audit
OWASP agentic AI security solutions landscape Q2 {YEAR} agent-audit
site:congress.gov PyOD OR "anomaly detection" OR "AI agent" OR "AI auditing"
site:whitehouse.gov "anomaly detection" OR "AI agent security" OR "AI auditing"
site:osti.gov PyOD OR "anomaly detection" OR "Yue Zhao"
site:nsf.gov "Yue Zhao" OR "FORTIS" anomaly detection
site:nextgov.com "anomaly detection" OR "AI agent security" {YEAR}
```

### International government & policy

```
site:digital-strategy.ec.europa.eu TrustLLM OR PyOD OR "anomaly detection" OR "AI auditing"
site:enisa.europa.eu "anomaly detection" OR "AI agent security" OR TrustLLM
site:gov.uk "anomaly detection" OR "AI auditing" OR "AI agent security" OR TrustLLM
site:oecd-ilibrary.org PyOD OR TrustLLM OR "anomaly detection" OR "Yue Zhao"
site:unesco.org "anomaly detection" OR "AI auditing" OR TrustLLM
site:internationalaisafetyreport.org TrustLLM OR PyOD OR "anomaly detection" OR "Yue Zhao"
site:privacyinternational.org "anomaly detection" OR "geolocation" OR DoxBench OR "AI privacy" OR "Yue Zhao"
"International AI Safety Report" TrustLLM OR PyOD OR "anomaly detection" OR DoxBench cited {YEAR}
"Privacy International" DoxBench OR "geolocation" OR "doxing" OR "Yue Zhao" cited {YEAR}
"EU AI Act" TrustLLM OR PyOD OR "anomaly detection benchmark" cited
"UK AI Safety Institute" TrustLLM OR PyOD OR "anomaly detection" cited report
"Hiroshima AI Process" OR "G7" OR "G20" TrustLLM OR "anomaly detection" cited
```

### Foundation model company reports & system cards

```
site:openai.com TrustLLM OR PyOD OR "Yue Zhao" OR "anomaly detection"
site:openai.com "system card" OR "safety report" trustworthiness benchmark evaluation
site:anthropic.com TrustLLM OR PyOD OR "Yue Zhao" OR "anomaly detection"
site:anthropic.com "model card" OR "responsible scaling" OR "safety" benchmark cited
site:deepmind.google TrustLLM OR PyOD OR "Yue Zhao" OR "anomaly detection"
site:ai.meta.com TrustLLM OR PyOD OR "anomaly detection" OR "Yue Zhao"
site:ai.meta.com "system card" OR "model card" trustworthiness benchmark
site:mistral.ai TrustLLM OR PyOD OR "anomaly detection"
site:docs.cohere.com TrustLLM OR PyOD OR "anomaly detection"
site:azure.microsoft.com "responsible AI" TrustLLM OR PyOD
OpenAI "system card" TrustLLM OR "trustworthiness" benchmark cited {YEAR}
Anthropic "model card" TrustLLM OR "safety benchmark" cited {YEAR}
Google DeepMind "technical report" TrustLLM OR "trustworthiness" benchmark {YEAR}
Meta "Llama" "system card" TrustLLM OR "safety benchmark" cited {YEAR}
```

### Consulting & analyst firm reports (search for name citations inside PDFs)

```
McKinsey "Global Institute" OR "report" PyOD OR TrustLLM OR "Yue Zhao" filetype:pdf
Deloitte "AI" "report" PyOD OR TrustLLM OR "anomaly detection" benchmark cited filetype:pdf
Gartner "Magic Quadrant" OR "Hype Cycle" anomaly detection PyOD OR "outlier detection" {YEAR}
Forrester "Wave" OR "report" anomaly detection OR "AI agent security" PyOD {YEAR}
```

## § Dimension 7: Education, Ecosystem & Global

### Education & courses

```
site:kaggle.com PyOD anomaly detection outlier notebook
site:kaggle.com ADBench OR "anomaly detection benchmark"
Coursera OR edX OR Udemy PyOD "anomaly detection" course
YouTube PyOD anomaly detection tutorial
Bilibili PyOD 异常检测 教程
university syllabus PyOD "anomaly detection" course materials
```

### Code ecosystem & package dependents

```
site:paperswithcode.com PyOD OR ADBench OR "anomaly detection"
site:paperswithcode.com TrustLLM OR TrustGen OR DoxBench
GitHub "import pyod" OR "from pyod" language:python stars:>10
site:libraries.io PyOD dependents downstream
PyPI PyOD dependents downstream packages
conda-forge PyOD downloads stats
site:hub.docker.com PyOD anomaly detection
site:colab.research.google.com PyOD anomaly detection
Google Colab notebook PyOD "anomaly detection" tutorial
site:huggingface.co/spaces PyOD anomaly detection outlier
```

### Professional visibility (tutorials, webinars, meetups)

```
site:speakerdeck.com PyOD OR "anomaly detection" OR "Yue Zhao"
site:slideshare.net PyOD OR "anomaly detection" OR "Yue Zhao"
site:meetup.com PyOD OR "anomaly detection" workshop tutorial
PyOD webinar tutorial workshop invited talk recording 2024 2025
"Yue Zhao" invited talk tutorial workshop anomaly detection
WeChat 公众号 PyOD 异常检测
```

### Dissertations & theses

```
site:proquest.com PyOD OR "anomaly detection" dissertation thesis
Google Scholar PyOD "anomaly detection" thesis OR dissertation filetype:pdf
"PyOD" OR "ADBench" thesis defense university 2024 2025
```

### Non-English coverage

```
site:csdn.net PyOD 异常检测
site:zhihu.com PyOD 异常检测 离群点检测
site:zenn.dev PyOD 異常検知
site:qiita.com PyOD anomaly detection
site:tistory.com PyOD 이상 탐지
InfoQ中文 PyOD 异常检测 OR TrustLLM
site:heise.de "anomaly detection" OR PyOD OR TrustLLM
```

---

### Dimension 8: PDF candidate identification — Governance & Model Reports

Use these to find government/think tank/model PDFs, then fetch and search inside them:

```
site:hsgac.senate.gov AI OR "artificial intelligence" OR "machine learning" filetype:pdf
site:commerce.senate.gov AI OR "artificial intelligence" filetype:pdf
site:judiciary.senate.gov AI OR "artificial intelligence" filetype:pdf
site:gao.gov "artificial intelligence" OR "machine learning" report filetype:pdf {YEAR-1} {YEAR}
site:nist.gov "artificial intelligence" "risk management" OR "agent" filetype:pdf {YEAR}
site:whitehouse.gov "artificial intelligence" OR "AI" memorandum OR "executive order" filetype:pdf {YEAR}
site:rand.org "artificial intelligence" "anomaly detection" OR "agent security" OR "trustworthiness" filetype:pdf
site:brookings.edu "artificial intelligence" "anomaly detection" OR "agent security" filetype:pdf
OECD AI report "anomaly detection" OR "trustworthiness benchmark" filetype:pdf {YEAR}
"EU AI Office" report "trustworthiness" OR "anomaly detection" filetype:pdf {YEAR}
"UK AI Safety Institute" report evaluation benchmark filetype:pdf {YEAR}
```

### Dimension 8: PDF candidate identification — Regulated Verticals (where PyOD/ADBench are most likely cited)

These are the sectors where anomaly detection tools are deployed in production. Search for reports from sector regulators and industry bodies.

```
site:occ.gov "anomaly detection" OR "outlier detection" OR "machine learning" fraud report filetype:pdf
site:fdic.gov "anomaly detection" OR "machine learning" OR "AI" risk report filetype:pdf
site:finra.org "anomaly detection" OR "machine learning" OR "AI" surveillance report filetype:pdf
site:sec.gov "anomaly detection" OR "machine learning" OR "AI" market surveillance filetype:pdf
site:cftc.gov "anomaly detection" OR "machine learning" risk filetype:pdf
FINRA OR OCC OR FDIC "anomaly detection" "machine learning" report {YEAR-1} {YEAR}
SEC "anomaly detection" OR "outlier detection" market surveillance AI report filetype:pdf
site:fda.gov "anomaly detection" OR "machine learning" medical device AI filetype:pdf
FDA "artificial intelligence" "machine learning" "anomaly detection" device surveillance {YEAR}
site:nasa.gov "anomaly detection" OR "outlier detection" "machine learning" spacecraft monitoring filetype:pdf
NASA JPL "anomaly detection" "machine learning" Python report filetype:pdf
site:faa.gov "anomaly detection" OR "machine learning" OR "AI" safety report filetype:pdf
site:cisa.gov "anomaly detection" OR "AI" cybersecurity ICS critical infrastructure filetype:pdf
CISA ICS-CERT "anomaly detection" "machine learning" report guidance filetype:pdf
DOE "anomaly detection" "machine learning" national laboratory report filetype:pdf
```

### Dimension 8: PDF candidate identification — Defense, Telecom, Insurance

```
DARPA "anomaly detection" "machine learning" program report filetype:pdf
MITRE "anomaly detection" "machine learning" report filetype:pdf {YEAR-1} {YEAR}
"anomaly detection" "machine learning" telecom fraud network monitoring report filetype:pdf {YEAR}
"anomaly detection" insurance claims fraud "machine learning" report filetype:pdf
Splunk OR Elastic OR Datadog "anomaly detection" PyOD OR "outlier detection" integration filetype:pdf
CrowdStrike OR Palo Alto OR Fortinet "anomaly detection" "machine learning" whitepaper filetype:pdf
```

### Books & patents

```
site:books.google.com PyOD "anomaly detection" OR "outlier detection"
site:books.google.com TrustLLM "trustworthiness" OR "large language models"
site:books.google.com "Yue Zhao" "anomaly detection" OR "outlier detection"
site:patents.google.com PyOD "anomaly detection"
site:patents.google.com "Yue Zhao" anomaly detection
```

### Industry analysts & VC

```
site:gartner.com PyOD OR "anomaly detection" OR "AI agent security"
site:forrester.com "anomaly detection" OR "AI agent security" {YEAR}
site:idc.com "anomaly detection" OR "AI agent security" {YEAR}
site:bvp.com "AI agent security" {YEAR}
site:a16z.com "AI agent security" {YEAR}
```

### Think tanks, research institutes & policy orgs

```
site:hai.stanford.edu "anomaly detection" OR "AI auditing" OR "AI agent security" OR PyOD OR TrustLLM
site:cset.georgetown.edu "anomaly detection" OR "AI agent security" OR "AI auditing"
site:brookings.edu "anomaly detection" OR "AI agent security" OR "AI auditing"
site:rand.org "anomaly detection" OR "AI agent security" OR "AI auditing"
site:safe.ai TrustLLM OR "anomaly detection" OR "AI auditing"
site:partnershiponai.org "anomaly detection" OR "AI agent security"
site:weforum.org "anomaly detection" OR "AI agent security" OR "AI auditing"
site:oecd.ai "anomaly detection" OR "AI agent security" OR "AI auditing"
site:turing.ac.uk "anomaly detection" OR "AI agent security" OR PyOD
```

### Consulting firm reports

```
site:mckinsey.com PyOD OR "Yue Zhao" OR TrustLLM
site:deloitte.com PyOD OR "Yue Zhao" OR TrustLLM
site:pwc.com PyOD OR "Yue Zhao" OR TrustLLM
site:accenture.com PyOD OR "Yue Zhao" OR TrustLLM
site:ey.com "anomaly detection" OR "AI agent security" OR "AI auditing" {YEAR}
site:kpmg.com "anomaly detection" OR "AI agent security" OR "AI auditing" {YEAR}
site:bcg.com "anomaly detection" OR "AI agent security" {YEAR}
site:bain.com "anomaly detection" OR "AI agent security" {YEAR}
```

### Standards bodies & threat frameworks

```
site:atlas.mitre.org "anomaly detection" OR PyOD
site:cloudsecurityalliance.org "anomaly detection" OR "AI agent security" OR "AI auditing"
site:mlcommons.org "anomaly detection" OR PyOD OR "outlier detection"
site:standards.ieee.org "anomaly detection" OR "AI agent" OR "AI auditing"
MITRE ATLAS adversarial ML anomaly detection PyOD {YEAR}
```

### Industry research blogs (verified citation required)

```
site:research.ibm.com "anomaly detection" OR PyOD OR TrustLLM
site:deepmind.google "anomaly detection" OR "AI auditing" OR "AI agent security"
site:microsoft.com/en-us/research PyOD OR "Yue Zhao" OR "anomaly detection"
```

### University / institutional

```
site:viterbischool.usc.edu "Yue Zhao"
site:cs.usc.edu "Yue Zhao"
site:cmu.edu "Yue Zhao" anomaly detection
USC Viterbi news "computer science" AI security safety {YEAR-1} {YEAR}
```

### Developer community

```
site:news.ycombinator.com PyOD anomaly detection
site:news.ycombinator.com "agent-audit" OR "Aegis" AI agent security
site:reddit.com/r/MachineLearning PyOD OR TrustLLM "Yue Zhao"
site:stackoverflow.com PyOD anomaly detection
```

## § Dimension 4: Topic Proximity

Each query searches the broader trending topic. The arrow indicates which of your works it connects to.

```
ChatGPT geolocation doxing privacy risk news {YEAR-1} {YEAR}                      → DoxBench
ChatGPT o3 geolocation doxing privacy news media Wired Verge                       → DoxBench
OpenClaw agent security crisis ClawHub vulnerabilities {YEAR}                       → agent-audit
"anomaly detection" "open source" landscape comparison {YEAR-1} {YEAR}              → PyOD
"LLM trustworthiness" benchmark evaluation safety {YEAR}                            → TrustLLM
"AI agent firewall" "pre-execution" security tool {YEAR}                            → Aegis
"drug discovery" AI multi-agent automation LLM {YEAR}                               → DrugAgent, TDC
OWASP agentic AI top 10 security solutions landscape {YEAR}                         → agent-audit
"diffusion models" survey highly cited ACM {YEAR-1} {YEAR}                          → diffusion survey
typhoon forecasting AI LLM weather {YEAR}                                           → TyphoFormer
"multimodal out-of-distribution" detection benchmark NeurIPS                        → MultiOOD, DPU
"AI auditing" "agent security" OWASP agentic top 10 USC research cited {YEAR}       → agent-audit, Aegis
"jailbreak detection" vision language model adaptive memory                         → JailDAM
"prompt injection defense" shortcut heuristic surface pattern                       → Defenses Against Prompt Attacks
"AI agent config" portable skills AGENTS.md Claude Code Codex {YEAR}                → anywhere-agents
"AI writing style" LLM prose rules AGENTS.md style-review {YEAR}                    → agent-style
```

## § Dimension 5: Smart Paper Keywords

When exact title search fails, use these distinctive keywords or striking claims.

| Paper | Smart search query |
|-------|--------------------|
| DoxBench / Doxing via the Lens | ChatGPT o3 geolocation doxing privacy 60% street-level accuracy |
| The Autonomy Tax | defense training breaks LLM agents 47-77% benign task failure |
| Sovereign-OS | charter-governed AI agent operating system fiscal discipline verifiable |
| FigEdit / Charts Are Not Images | scientific chart editing benchmark 30000 structured transformation ICLR |
| CDCR-SFT | causal DAG LLM hallucination surpass human performance CLADDER 95.33 |
| MAMA / Topology Matters | network topology memory leakage multi-agent PII extraction |
| Implicit Execution Tracing | provenance attribution multi-agent "final text survives" watermark |
| Cross-user contamination | shared-state LLM agent privacy unintentional leakage cross-user |
| Multimodal GEO | rank manipulation vision-language model rankers adversarial multimodal |
| StealthRank | LLM ranking manipulation stealthy prompt optimization energy-based |
| Agent Banana | high-fidelity image editing agentic thinking tooling context folding |
| Auditable Agents | auditable agents AI agent audit trail preprint {YEAR} |
| Fairness or Fluency | language bias pairwise LLM-as-a-Judge fairness fluency |
| Tracing Moral Foundations | moral foundations large language models mechanistic interpretability |
| ClimateLLM | weather forecasting frequency-aware large language models climate |
| Political-LLM | large language models political science simulation decision-making |
| DPU | dynamic prototype updating multimodal out-of-distribution detection CVPR highlight |
| FaceLock | biometric defense generative editing personal protection CVPR |
| JailDAM | jailbreak detection adaptive memory vision language model COLM |
| DyFlow | dynamic workflow agentic reasoning framework NeurIPS |
| DrugAgent | multi-agent drug discovery programming LLM automation |
| AD-AGENT | multi-agent anomaly detection end-to-end platform natural language |
| Don't Let It Hallucinate | premise verification retrieval-augmented logical reasoning TMLR |

## § Dimension 6: Citation & Downstream Impact

```
PyOD citations achievements (→ check pyod.readthedocs.io/en/latest/pubs.html)
"Yue Zhao" Google Scholar highly cited anomaly detection outlier {YEAR-1} {YEAR}
"diffusion models comprehensive survey" ACM Computing Surveys most cited downloaded
DrugAgent cited Nature Biotechnology OR Nature OR Science
TDC "Therapeutics Data Commons" cited drug discovery industry
TrustLLM cited AI safety regulation policy government
"anomaly detection" benchmark review citing PyOD {YEAR-1} {YEAR}
```
