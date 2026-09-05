# REFERENCE-CHECK: data/publications.json (2026 cohort)
Date: 2026-08-22  
Source: `data/publications.json`, the 31 entries with year 2026 and no `links`  
Method: 4 of the skill's passes, adapted from `.bib` to JSON. Pass A ran as 5 parallel Codex units over arXiv, Papers-with-Code, and GitHub from a local residential IP.  
**Status: links applied; venues, titles, authors, and abstracts NOT modified. S2-degraded, no `S2_API_KEY` present, so Pass B did not run.**

## Scope rule in force
`venue` was excluded from verification entirely. Several of these papers are accepted but unpublished, so their venue is not discoverable online and the repository text is authoritative by definition. Workers were instructed not to flag venues. Titles and author lists are reported but were likewise left unmodified, for the same reason: a camera-ready can differ from its preprint.

## Summary

| Result | Count |
|---|---|
| Entries checked | 31 |
| Authors EXACT-MATCH | 25 |
| Authors NAME-DIFF | 3 |
| Authors UNVERIFIABLE | 2 |
| Authors MISSING-AUTHOR | 1 |
| Code/project links verified at HTTP 200 and applied | 17 |
| Links rejected | 1 (self-link to own site) |
| Entries site-wide still without links | 55 (was 71) |

## Applied links

| Paper | Type | URL |
|---|---|---|
| CoAct: Co-Active LLM Preference Learning with Human-AI Syn | github | <https://github.com/rux001/CoAct> |
| SpecAlign: Efficient Specification-Grounded Alignment of L | github | <https://github.com/Jackwwj619/SpecAlign> |
| GEO-Bench: Benchmarking Ranking Manipulation in Generative | github | <https://github.com/glad-lab/geobench> |
| Topology Matters: Measuring Memory Leakage in Multi-Agent  | github | <https://github.com/llll121/mama-eval> |
| FORTIS: Benchmarking Over-Privilege in Agent Skills | github | <https://github.com/lili0415/FORTIS-Benchmark> |
| Multimodal Generative Engine Optimization: Exploiting Cros | github | <https://github.com/glad-lab/MGEO> |
| MaskForge: Structure-Aware Adaptive Attacks for Jailbreaki | github | <https://github.com/SaFo-Lab/MaskForge> |
| MedExAgent: Training LLM Agents to Ask, Examine, and Diagn | github | <https://github.com/EndlessCG/medexagent> |
| AEGIS: No Tool Call Left Unchecked -- A Pre-Execution Fire | github | <https://github.com/Justin0504/Aegis> |
| MemoHarness: Agent Harnesses That Learn from Experience | github | <https://github.com/HowieHwong/MemoHarness> |
| Geometry over Density: Few-Shot Cross-Domain OOD Detection | github | <https://github.com/lili0415/UFCOD> |
| Agent Banana: High-Fidelity Image Editing with Agentic Thi | github | <https://github.com/taco-group/agent-banana> |
| Agent Banana: High-Fidelity Image Editing with Agentic Thi | project | <https://agent-banana.github.io/> |
| Tracing Moral Foundations in Large Language Models | github | <https://github.com/AiHeMaotai/MFT_LLMs> |
| WeClawArena: An Auditable Sandbox and Benchmark for Cross- | github | <https://github.com/kingofspace0wzz/WeClawArena> |
| Can Subgraph Explanations Be Weaponized to Steal Graph Neu | github | <https://github.com/LabRAI/XSTEAL/> |
| Benchmarking Knowledge-Extraction Attack and Defense on Re | github | <https://github.com/charlieqi02/RAG-Knowledge-Extraction-Attack-and-Defense-Benchmark> |

## Resolved (applied 2026-08-22)

The owner's rule: follow arXiv for author names and titles; leave OpenReview-only entries alone; venues remain authoritative as written.

### Cat-DPO author list completed
Three authors absent from the record were restored from arXiv 2604.17299: **Henry Peng Zou, Xiyang Hu, Yan Liu**. Its venue is `arXiv preprint`, so arXiv is the source of truth rather than an unpublished camera-ready.

### "Shawn Li" vs "Li Li" resolved per arXiv, across all 21 affected entries

The workers only saw the 2026 no-links cohort, so applying the rule properly meant querying arXiv for every entry carrying the name. All 18 with an arXiv URL were checked in one batch.

| Result | Count | Action |
|---|---|---|
| arXiv says `Li Li` | 5 | changed |
| arXiv says `Shawn Li` | 13 | kept |
| No arXiv URL (OpenReview, CVF) | 3 | left alone |

Changed: `A Personalized Conversational Benchmark`, `Auditable Agents`, `Agent Banana`, `TAG-AD`, `M3OOD`. The other 13 were confirmed correct as written, so the record was already right more often than not.

### MGEO title taken from arXiv
Record now reads *Multimodal Generative Engine Optimization: Rank Manipulation for Vision-Language Model Rankers*, matching arXiv 2601.12263 v1 and v2. `data/lab-members.json` carried the same title and was updated with it, so `lab.html` and `publications.html` agree.

**DOG-DPO was deliberately not changed.** arXiv renders `DOG-DPO:Dynamic` with no space after the colon; the record is correct and arXiv carries the typo.

### Two stale copies of the old MGEO title remain, by choice

- `cv/cv-full.tex` line 683. Hand-authored LaTeX; only its open-source section is generated. Left for the owner, since reconciling website against CV is a manual decision.
- `data/s2-metrics.json`. A generated cache carrying `generated_at` and `source`; it self-heals on the next `fetch_s2_metrics.py` run. (Superseded since this audit: both the cache and the script were removed, and `data/citations.json` now arrives from meta-finder's `update-citations` workflow.)


## Unverifiable, not errors

- **Modeling, Evaluating, and Enhancing Reasoning of Large Langu**: Repo: "Zixiang Xu, Yanbo Wang, Yue Huang, Haomin Zhuang, Yujun Zhou, Jiayi Ye, Sixian Li, Zirui Song, Lang Gao, Chenxi Wang, Zhaorun Chen, Wang Pan, Yue Zhao, Jieyu Zhao, Xiangliang Zhang, X
- **FinanceLLM: A Survey of Large Language Models in Finance**: No arXiv abstract record was found. The repository list is "Ojas Nimase, Zhengao Li, Xinyu Wei, Jinglin Hu, Luojia Liu, Kangyi Zhao, Yue Zhao, Yushun Dong". The paper_url is OpenReview; curl

OpenReview serves a browser challenge to automated fetches and returns HTTP 403 on its PDF and API endpoints, so entries whose `paper_url` is OpenReview cannot be checked this way. This is a tooling limit, not a defect in the records.

## No code found

Searched arXiv abstract text, arXiv comments and link panels, Papers-with-Code, and GitHub by title and by first author. Ten papers came back with no repository meeting the required title-match rule. They are Agent Safety Is Action Alignment, Cat-DPO, Implicit Execution Tracing, The Autonomy Tax, JigShape, Memory Retrieval for Changing Preferences, Premise Verification, DOG-DPO, FinanceLLM, and No Attacker Needed. A repository that merely discusses the topic was rejected rather than guessed.

## Re-run

```
python scripts/prerender_pages.py && python scripts/ci_check_site.py
```

Unit prompts and raw worker output are in the session scratchpad under `prun/`.
