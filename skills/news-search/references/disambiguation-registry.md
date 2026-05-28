# Disambiguation Registry

Cumulative list of name collisions, false-positive patterns, and verified-negative leads that recur across audit rounds. New rounds should consult this list before counting any borderline match. Add entries when a new collision is discovered; do not remove entries — even after a collision is "common knowledge" it still needs to be recorded so future agents know to apply the disambiguator.

This file complements `search-strategy.md` ("Common false positives" table) by carrying the longer-form context, the resolution rule, and any specific URLs that have repeatedly surfaced as false positives.

## Tool-Name Collisions

### Aegis

**Real match**: USC `AEGIS: No Tool Call Left Unchecked, A Pre-Execution Firewall and Audit Layer for AI Agents` (arXiv:2603.12621). Authors: Justin Li (Justin0504), Aojie Yuan, ..., Yue Zhao.

**Required disambiguator**: at least one of "pre-execution firewall", "tool call", "Justin0504", "Aojie Yuan", arXiv:2603.12621.

**Known collisions** (do NOT count):

- **Forrester AEGIS Framework** (`forrester.com/technology/aegis-framework/`) — Forrester's enterprise framework, full name "Agentic AI Enterprise Guardrails For Information Security". Same acronym, different system, published 2026.
- **NVIDIA Aegis dataset** — generic security dataset, unrelated.
- **RedHat aegis-ai** (`github.com/RedHatProductSecurity/aegis-ai`) — CVE-analysis genAI agent.
- **aegis-protocol** (onchain accountability layer, e.g. JoelEmmanuelCloud's repo) — blockchain project.
- **aegisplatform.ai** — commercial "Aegis Agent Control Plane" product page; no link to USC paper.
- **MIT CSAIL Aegis (secure processor)** — Trusted Computing Group hardware project, predates LLMs.
- **AegisAI email-security startup** — surfaced under SecurityWeek search.
- **Help Net Security Asqav / Sage / Praetor** — competitor agent-firewall projects that mention AEGIS by USC as prior art *but do not always cite by full name*. Treat as topic-adjacent unless the paper title or arXiv ID is named.
- **TechFides AEGIS** (`techfides.com`, "AEGIS: Governing the Agentic Enterprise"): commercial six-layer enterprise AI-governance product ($15K-$400K+); no USC disambiguators present across two fetches. Verified 2026-05-28.
- **CloudMatos "Aegis" / "Aegis Gateway"** (`cloudmatos.ai`): the vendor's own Istio+OPA-for-agents runtime policy/observability gateway (full blog series plus a dedicated product page at `cloudmatos.ai/solution/aegis-gateway/`). The product and blog pages were fetchable on 2026-05-28 and confirm a CloudMatos commercial product, not a FORTIS AEGIS hit; some automated fetchers receive a catch-all 404 shell for non-JS clients. Verified 2026-05-28.
- **Authensor "Aegis" scanner** (`authensor.com`, npm `@authensor/aegis`): commercial prompt-injection / memory-poisoning detector. Verified 2026-05-28.
- **Beam AI "AEGIS framework"** (`beam.ai`): a generic threat-modeling framework paired with MAESTRO, not the FORTIS paper. Verified 2026-05-28.

### TrustLLM

**Real match**: Sun et al., "Position: TrustLLM: Trustworthiness in Large Language Models" (ICML 2024 / arXiv:2401.05561). Authors: Lichao Sun, Yue Zhao, plus ~40 others.

**Required disambiguator**: arXiv:2401.05561, ICML 2024, Lichao Sun, or the project page `trustllmbenchmark.github.io`.

**Known collisions** (do NOT count):

- **`trustllm.eu`** — EU Horizon multilingual LLM project. Different team, different paper, different institution mix.
- Other "trust LLM" projects spelled with a space — usually generic policy terminology, not the benchmark.

### TDC (Therapeutics Data Commons)

**Real match**: Huang et al., "Therapeutics Data Commons" (Yue Zhao, Marinka Zitnik, et al.). The full name "Therapeutics Data Commons" is the disambiguator; the bare 3-letter acronym is too short.

**Required disambiguator**: full name "Therapeutics Data Commons", or `tdcommons.ai`, or `tdc-team` GitHub org, or context naming Marinka Zitnik (Harvard).

**Known collisions** (do NOT count):

- **TDCJ** — Texas Department of Criminal Justice.
- **TDC Group Limited** — Caribbean telecom.
- **Travere Therapeutics (ticker TVTX)** — biopharma, not TDC.
- **J&J "Therapeutics Discovery (TD)"** — internal Johnson & Johnson R&D org. Surfaced repeatedly in Built In Boston listings (e.g. "Principal Data Scientist - R&D DSDH - Therapeutics Discovery (TD)"). Verified by full-page fetch on 2026-05-07.

### BOND (PyGOD benchmark)

**Real match**: Liu, Tang, Zhao et al., BOND graph anomaly-detection benchmark. Always paired with PyGOD.

**Required disambiguator**: PyGOD context, or "graph anomaly detection", or "node-level outlier".

**Known collisions** (do NOT count):

- "bonds", "bonded", "bonding" — English words. Scanner already filters via `FALSE_POSITIVE_CTX["BOND"]`.
- Biology / chemistry papers about molecular bonds.

### ECOD

**Real match**: Li et al., "ECOD: Unsupervised Outlier Detection Using Empirical Cumulative Distribution Functions" (TKDE 2022). Yue Zhao is corresponding author.

**Required disambiguator**: word boundary regex (the scanner enforces this for short uppercase tools); plus context naming "outlier detection" / "anomaly detection" / cumulative distribution.

**Known collisions** (do NOT count):

- "decoder", "encoder", "decoding", "encoding" substrings. Scanner filters via `FALSE_POSITIVE_CTX["ECOD"]`.
- "LiveCodeBench" — substring `code` adjacent. Scanner filters this; D8 saw the false positive in Gemini 2.5 Flash Model Card (2026-05-07 round).
- Generic "code" / "codebase" mentions.

### MAMA (Topology Matters)

**Real match**: Liu et al., "Topology Matters: Measuring Memory Leakage in Multi-Agent Systems" (arXiv 2026). Sometimes referenced as MAMA in derivative work.

**Required disambiguator**: "Topology Matters" full title or arXiv ID.

**Known collisions** (do NOT count):

- "mammal", "Obama", "Mahama" (Ghanaian president John Mahama). Scanner filters via `FALSE_POSITIVE_CTX["MAMA"]`.

### SUOD

**Real match**: Zhao et al., "SUOD: Toward Scalable Unsupervised Outlier Detection" (MLSys 2021).

**Known collisions** (do NOT count):

- "pseudo" substring. Scanner filters via `FALSE_POSITIVE_CTX["SUOD"]`.

### agent-style

**Real match**: Yue Zhao's `yzhao062/agent-style` GitHub repo (writing rule pack for AI agents).

**Required disambiguator**: explicit GitHub URL, "yzhao062", or context naming the writing rule pack.

**Known collisions** (do NOT count):

- "agent-style workflows" as an English compound adjective ("workflows in the style of agents") — surfaced in OpenAI Security Engineer Detection & Response JD on 2026-05-07. Verified rejection.
- Any generic "X-style agent" phrasing without explicit repo/author reference.

### import pyod

**Real match**: `from pyod...` or `import pyod` Python imports.

**Required disambiguator**: actual `pyod.X` module reference; verify `from pyod` not `from pyodbc` / `from pyodide`.

**Known collisions** (do NOT count):

- **pyodbc** — Python ODBC driver. Frequent false positive in Apache Airflow / Apache Arrow / Apache Ignite-3 / aws/aws-sdk-pandas docs (2026-05-07 round).
- **Pyodide** — CPython on WebAssembly. Surfaced in The New Stack / VentureBeat searches.

## Person-Name Collisions: "Yue Zhao"

"Yue Zhao" is a common Chinese name. Always disambiguate before counting an author hit.

**Real match**: Yue Zhao, USC FORTIS Lab, `yzhao062` on GitHub, anomaly detection / AI auditing / AI agent security.

**Required disambiguator**: at least one of: USC, University of Southern California, FORTIS, yzhao062, PyOD, anomaly detection, AI auditing.

**Known same-name-different-person hits** (do NOT count without disambiguator):

| Person | Affiliation / context | Where surfaced |
|---|---|---|
| Yuchen Zhao | Patent inventor, US10445311B1 / EP3075102B1 | Google Patents, 2026-05-07 D10 |
| Siyan Zhao | Patent inventor (different US patent) | Google Patents, 2026-05-07 D10 |
| Qingyue Zhao | Stanford CRFM Foundation Model Transparency Index 2025 author (chain-of-thought transparency) | Stanford CRFM FMTI 2025 PDF, 2026-05-07 D8 |
| W. Zhao | WildChat dataset (1M ChatGPT logs) | NIST AI 800-4 ref [91], 2026-05-07 D8 |
| D. Zhao | Swiss Cheese Model AI safety paper | NIST AI 800-4, 2026-05-07 D8 |
| Yue Zhao (Carnegie Mellon HCII / different Yue Zhao) | HCI researcher, distinct from FORTIS PI | Multiple D1 sweeps |

When in doubt, mark `tier_guess: dropped_name_collision` and record the disambiguation evidence in `notes`.

## Verified-Negative Leads

Leads that repeatedly surface like positives but are confirmed not to name FORTIS work. Future rounds should skip these without re-checking.

| Source | Verified date | Why it surfaces / what it really covers |
|---|---|---|
| Pinterest Engineering — "Bring Your Own Algorithm to Anomaly Detection" (Wu / Tallam / Bajaj, Medium) | 2026-05-07 D7 | Cites EGADs (Yahoo) and Prophet (Meta), not PyOD. |
| Anthropic Threat Intelligence Engineer JD | 2026-05-07 D2-careers | Lists YARA / Sigma / Snort / Suricata / Passive DNS / Netflow / SIEM-native queries. No PyOD or any FORTIS tool. The closest peer to OpenAI #8g but does not replicate the pattern. |
| Anthropic Detection & Response Security Engineer JD | 2026-05-07 D2-careers | Lists EDR / SIEM / SOAR / Kubernetes / LLMs. No FORTIS tool. The "agent-style workflows" phrase here is generic English, not a `agent-style` repo reference. Re-checked 2026-05-28: the current Greenhouse title is "Security Software Engineer, Detection & Response Platform" (same role, renamed); still no FORTIS tool. |
| Anthropic Petri v1 / Petri v2 alignment posts | 2026-05-07 D3c | Parallel agent-auditing work; cites UK AISI Inspect / Palisade / ProntoQA / NLTK / LMSYS / Souly et al. Does NOT cite TrustLLM / Aegis / agent-audit / Auditable Agents. |
| MarkTechPost "Navigating the Complexity of Trustworthiness in LLMs" (Jan 2024) | 2026-05-07 D3a | Article about TRUST LLM but does NOT name Yue Zhao, Lichao Sun, Xiangliang Zhang, or any author/institution. Topic-only despite tier-2 outlet appearance. (Existing audit Ledger 2 #10 may be optimistic; flagged for review.) |
| ISACA — "The Growing Challenge of Auditing Agentic AI" (2025) | 2026-05-07 D5 | Strong topic match for Auditable Agents framework; does NOT name the paper, arXiv:2604.05485, or co-authors. Topic-validation only. |
| Stanford HAI 2026 AI Index (full report, ~400pp) | 2026-05-07 D8 | Kept HELM as canonical safety benchmark; no TrustLLM in benchmark tables or footnotes. |
| Stanford CRFM Foundation Model Transparency Index 2025 | 2026-05-07 D8 | "Qingyue Zhao" substring is a different person; no FORTIS hits. |
| OpenAI / Anthropic / Google DeepMind / Meta / Mistral / xAI / Cohere 2025-2026 system cards (Opus 4.5/4.6, GPT-5/5.2/5.3-Codex, Gemini 3 Pro Card + FSF, Gemini 2.5 Flash) | 2026-05-07 D8 | All PyMuPDF-extracted; 0 FORTIS term hits. |
| NIST AI 700-1 / 600-1 / 800-1 ipd2 / 800-4 / IR 8596 | 2026-05-07 D8 | All extracted; 0 FORTIS hits. |
| IMDA Singapore Model AI Governance Framework for Agentic AI (PDF) | 2026-05-07 D4 + D8 | 0 hits in PDF. Re-check on next IMDA revision. |
| BIS othp90 / othp98 / othp100 | 2026-05-07 D8 | All extracted; 0 hits. |
| ESMA AI Adoption in Securities Markets (Feb 2026) | 2026-05-07 D8 | 0 hits. |
| OWASP Top 10 LLM Applications v2025 / Agentic Apps 2026 / AIVSS v0.5 | 2026-05-07 D8 | All extracted; 0 hits. |
| CSA MythosReady v95 (Apr 2026 — also v92 D3c flagged) | 2026-05-07 D8 | 0 hits in v95. v92 likely also negative. |
| MITRE ATLAS NIST CSRC Sept 2025 deck | 2026-05-07 D8 | 0 hits. |
| FBI IC3 Principles for Secure AI Integration (Dec 2025) | 2026-05-07 D8 | 0 hits. |
| WO2023057798A1 (Isolation Forest Edge Patent) | 2026-05-07 D2 | Verified does NOT cite PyOD or Zhao et al. |
| OpenAI Careers, Data Science Manager, Integrity JD | 2026-05-28 D2-careers | Live OpenAI page fetchable on 2026-05-28. Lists "anomaly detection" as a generic data-science technique and does NOT name PyOD or any FORTIS tool. Distinct from #8g (Technical Intelligence Analyst, which names PyOD verbatim). |
| Anthropic ML/Research Engineer, Safeguards JD | 2026-05-28 D2-careers | Names only generic "anomaly detection systems" and "classifiers"; no PyOD or FORTIS tool. Peer of the existing Anthropic Threat-Intelligence and Detection-and-Response JD negatives. |
| Agent-governance vendor/consulting blogs (EY, Microsoft Agent Governance Toolkit, Databricks Unity AI Gateway, Acceldata, Beam AI, Sysdig, Kai Waehner/Confluent, GovTech, Ariel Softwares, Indext Data Lab, Waxell, LoginRadius) | 2026-05-28 D4/D5 | Agent-auditing/governance topic coverage; none names a FORTIS work on direct fetch. Beam AI "AEGIS framework" is a generic threat-modeling framework, not FORTIS Aegis. |

## How to Use This File

1. **Before counting a Tier 0/1 candidate**: search this file for the source name or tool name. If it appears under "Verified-Negative Leads", do not re-search; the negative is already recorded.
2. **Before counting a name match**: search for the matched name under "Tool-Name Collisions" or "Person-Name Collisions". Apply the required disambiguator before assigning a tier.
3. **When discovering a new collision**: add an entry under the appropriate section with the round date and the resolution rule. The file grows monotonically.

This is the disambiguation-side equivalent of `domain-registry.md`'s recall-floor harvest step.
