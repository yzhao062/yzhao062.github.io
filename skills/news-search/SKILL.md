---
name: news-search
description: Systematic web search for news, media, policy, and industry coverage of FORTIS Lab publications, tools, and research. Use when the user asks for a news audit, media coverage check, broader impact evidence, or visibility search for their work.
---

# News & Media Coverage Search

Systematically search for external coverage of Yue Zhao / FORTIS Lab work across all outlet types: tech press, security press, business press, government/policy, industry analysts, science press, AI newsletters, and universities.

## When to Use

- Periodic audit of media coverage (quarterly recommended)
- Before tenure/promotion materials
- Before grant applications requiring "broader impact" evidence
- After major paper acceptances or tool releases
- When updating the website news section

## Inputs

Read these files before starting:

1. `data/publications.json` — all papers (titles, venues, years, links)
2. `data/open-source.json` — all tools/libraries (names, stars, URLs)
3. `news-coverage-audit.md` — previous audit results (skip known items, update stale entries)

## Execution Model

If parallel workers and web search are available, run dimensions in parallel; otherwise process dimensions sequentially. Batch queries conservatively to stay within tool rate limits. Read all three reference files before starting:

1. `references/search-queries.md` — query bank (not exhaustive; see triage rules below)
2. `references/outlet-registry.md` — outlet classification and `site:` domain lists
3. `references/search-strategy.md` — techniques for finding indirect coverage, when to persist vs. stop, name disambiguation

After all searches complete, merge results into `news-coverage-audit.md` using the tier structure in the Output section. If `news-coverage-audit.md` does not yet exist, create it with the full tier structure and negative-results table as a fresh audit.

### Query Bank Triage Rules

The query bank in `references/search-queries.md` is curated, not exhaustive. It covers high-adoption tools and papers with known media hooks.

**Full audit mode: search EVERY paper and tool.** Read `data/publications.json` and `data/open-source.json` and generate at least one smart-keyword search (Dimension 5) for every single entry. Do not skip any paper or tool. Use distinctive claims or method names, not exact titles. This is critical because coverage can appear for any paper, not just high-profile ones (e.g., COPOD has a dedicated book chapter, GLIP-OOD has a tech blog feature, the computing resources paper influenced CVPR policy).

For items not in the query bank, generate queries at runtime:

- **Tools with 500+ GitHub stars**: add dedicated Dimension 2 queries
- **All papers at top venues from the current or prior year**: add Dimension 5 smart-keyword entries
- **Older papers and low-star tools**: still search with at least one Dimension 5 smart-keyword query each
- **Preprints**: search with distinctive claim keywords

---

## Dimension 1: Person & Lab

Find coverage that names the PI or lab, regardless of which paper or tool.

Search for: name + university + research area + various contexts (news, interview, podcast, keynote, expert quote, award, fellowship, grant). Also search for lab name and industry partner names (Amazon, NVIDIA, Google, Meta, Anthropic, NSF).

See `references/search-queries.md` § Dimension 1 for the full query list.

## Dimension 2: Tools in Non-Academic Contexts

Major tools (PyOD, TrustLLM, agent-audit, Aegis, ADBench) may appear in industry deployments, government reports, textbooks, or enterprise case studies without naming the PI.

Search for: each tool name + context keywords (enterprise, deployment, production, fraud detection, cybersecurity, government, NIST, federal, textbook, course, patent, Walmart, NASA, Tesla).

See `references/search-queries.md` § Dimension 2 for the full query list.

## Dimension 3: Outlet Sweep

Systematically check each outlet category using `site:` filters. This is the most important dimension for finding coverage the other dimensions miss.

**Categories:** security press, business press, top tech press, AI newsletters, science press, government/policy, industry analysts, university/institutional press, developer community.

**Generation rule:** `references/search-queries.md` § Dimension 3 provides base queries for the highest-priority outlets. For any outlet domain listed in `references/outlet-registry.md` that does not have an explicit query in the query bank, generate one at runtime using this template: `site:{domain} "anomaly detection" OR "AI auditing" OR "AI agent security" OR PyOD OR TrustLLM`. This ensures every registered outlet is checked without requiring the query bank to enumerate all 70+ domains.

## Dimension 4: Topic Proximity

Search for the broader trending topic and check if the work appears within coverage. This catches indirect coverage where the paper is relevant but not cited by name.

Examples: ChatGPT geolocation trend (connects to DoxBench), OpenClaw security crisis (connects to agent-audit), OWASP agentic AI landscape (connects to agent-audit/Aegis), anomaly detection open-source landscape (connects to PyOD).

See `references/search-queries.md` § Dimension 4 for the full query list.

## Dimension 5: Smart Paper Search

For papers where exact title search fails (most papers), use distinctive result keywords or striking claims from the paper instead.

Examples: "surpassed human performance 95.33% CLADDER" for the causal reasoning paper, "defense training breaks LLM agents 47-77% benign task failure" for The Autonomy Tax.

See `references/search-queries.md` § Dimension 5 for the full mapping table.

## Dimension 6: Citation & Downstream Impact

Track high-level citation metrics, appearances in high-impact journals (Nature, Science), enterprise adoption evidence, and downstream tools built on the work.

See `references/search-queries.md` § Dimension 6 for the full query list.

## Dimension 7: Education, Ecosystem & Global

Search the surfaces where widely-adopted tools spread beyond academic papers and news: education platforms, code ecosystems, non-English press, and developer communities.

**Education & courses:** Kaggle notebooks, Google Colab examples, Coursera/edX/Udemy course materials, university syllabi, YouTube/Bilibili tutorials, O'Reilly/Manning learning paths
**Code ecosystem:** GitHub code dependents (repos that import PyOD), PyPI/conda-forge download stats pages, Papers with Code tool listings, Hugging Face Spaces built on your tools
**Dissertations & theses:** ProQuest, Google Scholar thesis search, university repository searches
**Non-English coverage:** Chinese tech press (InfoQ CN, CSDN, Zhihu, WeChat public accounts), Japanese (Qiita, Zenn), Korean (Tistory, Velog), European (Heise, Le Monde Informatique, etc.)

See `references/search-queries.md` § Dimension 7 Education/Ecosystem for queries.

## Dimension 8: PDF Deep Search (Government, Think Tank, Industry Reports)

**This is critical and cannot be skipped.** Web search does not index the text inside PDFs from government reports, congressional testimony, think tank whitepapers, and industry reports. Citations of your work inside these documents are the highest-impact coverage (Tier 0) and are routinely missed by Dimensions 1-6.

### Strategy

1. **Identify candidate PDFs** — search for government/think tank reports on topics your work addresses (AI agent security, anomaly detection, LLM trustworthiness, AI auditing). Collect the PDF URLs.
2. **Fetch and search inside each PDF** — download or fetch the PDF, extract text (via PyMuPDF, pdftotext, or the WebFetch tool), and search for: tool names (PyOD, TrustLLM, Aegis, agent-audit, etc.), paper titles, author names ("Yue Zhao", "Zhao et al."), arXiv IDs, and repo URLs.
3. **Verify and classify** — if found, note the exact page, footnote number, and surrounding context.

### High-priority PDF sources to search

**U.S. Government (highest priority):**
- **U.S. Senate committee reports** — HSGAC, Commerce, Judiciary, Armed Services (AI-related)
- **U.S. House committee reports** — Science, Homeland Security, Financial Services
- **NIST special publications** — AI RMF updates, AI agent security, AI 100-series
- **GAO reports** — AI technology assessments, Science & Tech Spotlight series
- **CRS reports** — Congressional Research Service AI analyses
- **Federal agency AI strategies** — DOD (JAIC/CDAO), DOE national labs, HHS, Treasury/OCC, SEC, CFTC, Federal Reserve
- **White House** — AI executive orders, OMB memoranda, OSTP reports, CEA reports
- **NSF** — program solicitations, dear colleague letters mentioning anomaly detection or AI safety

**International Government (high priority):**
- **EU** — AI Act impact assessments, ENISA reports, EU AI Office publications
- **UK** — AI Safety Institute reports, DSIT AI regulation papers, Alan Turing Institute policy briefs
- **Canada** — ISED AI strategy, Canadian Centre for Cyber Security
- **Australia** — Department of Industry AI reports, eSafety Commissioner
- **Singapore** — IMDA Model AI Governance Framework
- **OECD** — AI Policy Observatory reports, OECD AI Principles implementation documents
- **UN** — UNESCO AI ethics recommendations, ITU AI reports
- **G7/G20** — Hiroshima AI Process documents, AI governance communiques

**Think tanks & policy institutes:**
- Brookings, RAND, CSET Georgetown, Stanford HAI, FLI, CAIS, Partnership on AI
- Center for Data Innovation, Information Technology and Innovation Foundation (ITIF)
- Centre for International Governance Innovation (CIGI)

**Foundation model companies (Tier 0 if they cite your work):**
- **OpenAI** — system cards (GPT-4, GPT-5, o1, o3), safety reports, preparedness framework documents, red teaming reports
- **Anthropic** — model cards, responsible scaling policy documents, safety research reports
- **Google DeepMind** — technical reports, Gemini system cards, safety evaluations
- **Meta AI** — Llama model cards, system cards, responsible use guides
- **Mistral** — model documentation, technical reports
- **xAI** — Grok system cards and technical reports
- **Cohere** — model cards, safety documentation
- **Microsoft** — Phi model cards, responsible AI reports, Azure AI safety documentation
- **Amazon** — Titan model documentation, AWS AI safety reports

These companies publish system cards and safety evaluations as PDFs or long-form web pages that reference academic benchmarks (TrustLLM, HELM, etc.) and tools. They also publish blog posts with embedded citations. Search both the HTML pages and any linked PDFs.

**Standards bodies:**
- ISO/IEC (AI standards series), IEEE SA, OWASP (agentic AI PDFs)
- MITRE ATLAS documentation

**Industry whitepapers & analyst reports (Tier 0 if they cite your work by name):**
- McKinsey, Deloitte, PwC, Accenture, EY, KPMG, BCG, Bain
- Gartner, Forrester, IDC research reports

### Known citations found via this dimension

- **U.S. Senate HSGAC** — "Hedge Fund Use of Artificial Intelligence" (Jun 2024), footnote 119 cites TrustLLM on page 25
- **FLI AI Safety Index** — Winter 2025 PDF uses TrustLLM as an official benchmark

### Why web search misses these

Government PDFs are hosted as static files (e.g., `.senate.gov/wp-content/uploads/...pdf`). Web search engines index the hosting page but not the text inside the PDF. A search for `site:senate.gov TrustLLM` returns nothing because the word "TrustLLM" only appears inside the PDF, not on any HTML page. The only way to find these is to identify candidate documents by topic, then search inside the PDFs directly.

---

## Output

Write all results to `news-coverage-audit.md` at the project root.

### Citation Verification Rule

**An item only counts as coverage if the article names or cites at least one of:**

1. A specific paper title or tool name (PyOD, TrustLLM, Aegis, agent-audit, etc.)
2. The PI by name ("Yue Zhao")
3. The lab ("FORTIS")
4. A co-author by name in the context of the specific paper/tool
5. An institutional attribution ("researchers from USC", "a USC team") in the context of the specific paper/tool
6. A direct link to the project URL, repo, or arXiv paper

**Read the article or its snippet to verify before including it.** Items attributed to co-authors or institutions should note this in the entry (e.g., "names: first author X, USC affiliation — Yue Zhao is co-author").

Items that only cover the same **topic** your work addresses (e.g., "AI agent security is important" without naming your tools) are **not coverage**. These may be useful as context for grant narratives but must be placed in a separate **"Topic Validation (Not Direct Coverage)"** appendix, clearly marked as not naming your work.

### Tier Structure

All tiers below require the citation verification rule above. If a result does not name or cite your work, it does not belong in any tier.

| Tier | Definition | Examples |
|------|-----------|----------|
| **Tier 0** | (a) Government reports (U.S. or international: legislative, executive, federal/national agency), international body reports (OECD, UN, EU), or official standards documents; (b) Technical reports, system cards, safety reports, or model cards from major foundation model companies (OpenAI, Anthropic, Google DeepMind, Meta AI, Mistral, xAI, Cohere, etc.); (c) Major consulting/analyst firm reports (McKinsey, Gartner, Forrester, Deloitte, etc.) — all that cite your work by name | U.S. Senate report citing TrustLLM, OpenAI system card citing TrustLLM, Anthropic safety report citing anomaly detection benchmark, Gartner report citing PyOD |
| **Tier 1** | Mainstream tech/business/security press, major research institutions (national labs, Hoover, Microsoft Research), or high-impact policy reports that name your work | FLI AI Safety Index using TrustLLM, LLNL article naming TrustLLM, Nature Biotechnology citing DrugAgent |
| **Tier 2** | Industry press, institutional PR, or dedicated features that name your work | "DrugAgent" in MarkTechPost, "Yue Zhao" in USC Viterbi News, Databricks blog naming PyOD |
| **Tier 3** | Dedicated blog posts, tutorials, or platform integrations naming your tool | KDnuggets PyOD tutorial, Databricks Kakapo built on PyOD, DEV Community Aegis post |
| **Tier 4** | Awards, recognitions, encyclopedia entries | Amazon RA, NVIDIA Grant, Grokipedia entry |
| **Tier 5** | Academic community only (Hugging Face, alphaXiv, etc.) | Paper pages, GitHub stars, Moonlight reviews |

Separate appendix (not a tier):
- **Topic Validation** — articles covering the same topic area without naming your work. Useful for grant narratives ("our research addresses concerns raised in McKinsey's 2026 report on agentic AI security") but not website news items.

### Required Sections in Output File

1. **Coverage ledgers** (separate counts for each):
   - **Government/Policy citations** — Tier 0: government reports, foundation model system cards, standards documents, analyst reports that cite your work by name
   - **External media** — Tier 1-2: third-party press, institutional features, dedicated blog posts by external authors
   - **Ecosystem adoption** — Tier 3: books, podcasts, enterprise integrations, patents, tutorials, platform integrations by external parties
   - **First-party/community** — self-authored blog posts, GitHub discussions, dataset hosting (not external coverage)
   - **Awards & recognitions** — Tier 4: awards, fellowships, encyclopedia entries
2. **Topic Validation appendix** — articles that cover the same topic but do not name your work
3. **Negative Results table** — outlet types searched with no results (prevents re-searching)
4. **Upcoming Opportunities** — imminent conferences, journalist contacts from prior coverage
5. **Summary Statistics** — separate counts per ledger, not a single aggregate. Report: government/policy total, external media total, ecosystem total, awards total.
6. **Coverage matrix** — per-item appendix or CSV with one row per paper/tool, dimensions searched (D1-D8), and outcome (coverage/topic-only/none). This makes the audit auditable.

### Incremental Updates

When running a targeted search (not full audit), append new findings to the existing file. Do not overwrite previous results. Mark the date of each search pass.

---

## Run Modes

| Mode | When | Dimensions to run |
|------|------|-------------------|
| **Full audit** | Once per semester, before portfolio updates | All 8 dimensions |
| **Targeted** | After a specific paper acceptance or tool release | Dims 1, 3, 4, 5 scoped to that item |
| **Quick check** | Before grant submissions | Dims 1, 6, 8 (citations, impact, government PDFs) |
| **Topic monitor** | When a trending topic connects to your work | Dim 4 only, focused on that topic |
| **Ecosystem check** | Before broader-impact statements | Dim 7 (education, code ecosystem, global) |
| **PDF deep search** | Before tenure materials or when a specific gov report is suspected | Dim 8 only, with candidate PDF list |
| **Affiliation audit** | Before tenure/promotion, after major citation milestones | Dim 9 (citation affiliation analysis) |

---

## Dimension 9: Citation Affiliation Analysis

**Purpose:** Find citing papers where at least one author is affiliated with a notable institution (government agencies, space agencies, national labs, defense contractors, foundation model companies, Fortune 500, pharma, financial institutions). This surfaces adoption evidence that web search and PDF search miss entirely.

**Important framing:** This finds "researchers AT [institution] cited your tool" -- not "[institution] officially endorses your tool." The distinction matters for how results are presented in grant narratives and tenure materials.

### How it works

Run `scripts/citation_affiliation_audit.py`, which uses the OpenAlex API to:
1. **Load ALL papers** from `data/publications.json` (not a hand-picked subset). The script reads the full inventory and only excludes surveys.
2. Find each paper on OpenAlex by arXiv ID, DOI, or title search. Title matching uses a two-pass strategy: exact normalized-title match first, then prefix-anchor (pre-colon acronym like "PyOD:", "TrustGen:") plus high word overlap (50%+ with prefix, 70%+ without). This prevents false positives from ambiguous or short titles.
3. **Query citing papers per work** using OpenAlex's `filter=cites:{work_id}` syntax. Per-work queries preserve the mapping from each citing paper back to which of your works it cites, which is critical for the output table. This is slower than batching but produces accurate attribution.
4. Extract author institution affiliations from every citing paper.
5. Pattern-match institutions against Tier 0 targets (government, space, national labs, defense, foundation model companies) and Tier 1 targets (Big Tech, finance, pharma, healthcare, industrial).
6. Deduplicate and write results to `citation-affiliation-audit.md`.

### Comprehensiveness rule

**Search every paper, not just the high-profile ones.** You do not know where the gold lies. The ESA OPS-SAT citation came from PyOD (obvious), but NASA JPL cited a less obvious paper. The CDC cited ECOD, not PyOD. Deutsche Bundesbank cited ECOD. Morgan Stanley cited XGBOD. Coverage can come from any paper. The script must read `data/publications.json` and search ALL non-survey entries. Do not skip papers because they have low citation counts or seem unlikely to have notable adopters.

### What to exclude

- **Survey papers** (e.g., Diffusion Models survey): OpenAlex conflates papers with similar titles, producing massive false positive rates. Only include tools, benchmarks, and methods papers. The script filters these automatically using title keywords like "comprehensive survey", "a survey on", "a survey of".
- **Papers with ambiguous short names** (e.g., "BOND"): The script uses title-word overlap verification (>30%) to confirm the right paper was found. If OpenAlex returns biology papers for a graph anomaly detection tool, the match is rejected.
- **Grant-funded affiliations vs. employment:** NIH appears as an affiliation on many papers, but most are university researchers with NIH grants, not NIH intramural staff. The output uses the framing "researchers AT [institution]" to avoid overclaiming. NIH Clinical Center and NIH intramural programs are stronger signals than generic "National Institutes of Health".

### Known Limitations

- **OpenAlex coverage gaps:** OpenAlex has incomplete coverage for papers published before ~2022 and its citation index lags behind Google Scholar significantly (e.g., PyOD shows ~24 citations on OpenAlex vs. 1,000+ on Scholar). This means the audit systematically undercounts. Run it as a lower-bound estimate, not an exhaustive census.
- **Google Scholar has no API.** Scholar has the most complete citation data but cannot be queried programmatically. For high-priority papers where OpenAlex returns few results, consider manual Scholar spot-checks.
- **Semantic Scholar** has better coverage than OpenAlex for CS papers but its affiliation data is mostly empty. It is not useful for this audit.
- **Re-run periodically.** OpenAlex backfills citation data over time. A paper that shows 0 citations today may show 50 in six months. Re-run at least once per semester. Very recent preprints (2026) will only appear in future runs.
- **The script tries arXiv ID lookup first** (from `paper_url` in `publications.json`), then falls back to title search. arXiv lookup is more reliable for CS papers but still requires OpenAlex to have ingested the paper.

### Improving Coverage

OpenAlex covers ~50% of papers as of Apr 2026. To close the gap:
- **Semantic Scholar API** (`api.semanticscholar.org/graph/v1/paper/{id}/citations`): better CS coverage than OpenAlex, but affiliation data is mostly empty. Useful as a second pass to find citing papers that OpenAlex missed, then cross-reference those citing paper titles back to OpenAlex for institution data.
- **Web of Science / Scopus APIs**: best affiliation data but require USC library credentials. Use for manual verification of Tier 0 claims.
- **Re-running the script** every 3-6 months is the simplest way to improve coverage, since OpenAlex backfills continuously.

### Output

Results go to `citation-affiliation-audit.md` at the project root, separate from the news coverage audit. The file includes:
- Tier 0 table (government, space, national labs, defense, foundation model companies)
- Tier 1 table (Big Tech, finance, pharma, healthcare, industrial)
- Summary by institution (counts)
- Methodology note about framing (affiliated researchers, not institutional endorsement)
