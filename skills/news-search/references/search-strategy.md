# Search Strategy: How to Find Things and Not Give Up

This document codifies the search techniques that actually work for academic work coverage. The key problem: most papers never appear in news by their exact title. You need indirect strategies.

---

## Core Principle: Search the Echo, Not the Source

Academic work rarely gets direct press coverage. What gets covered is the **downstream effect**: the viral trend, the industry crisis, the policy debate, the enterprise deployment. Your job is to find the echo and trace it back.

| Source (your work) | Echo (what gets covered) | How to find it |
|---|---|---|
| DoxBench paper | "ChatGPT can guess your location from a selfie" trend | Search the trend, check if paper is cited |
| agent-audit tool | OpenClaw security crisis | Search the crisis, check if tool is mentioned |
| PyOD library | Walmart pricing anomaly detection system | Search the deployment, check if PyOD is cited |
| TrustLLM benchmark | FLI AI Safety Index evaluation | Search the index, check if TrustLLM is used |

---

## Technique 1: Topic Proximity Search

**Do not search for the paper title.** Search for the topic the paper addresses and see if your work appears in the results.

Bad: `"Doxing via the Lens: Revealing Location-related Privacy Leakage"`
Good: `ChatGPT geolocation doxing privacy selfie location news`

Bad: `"AEGIS: No Tool Call Left Unchecked"`
Good: `AI agent firewall pre-execution security open source 2026`

**Why this works:** Journalists write about trends, not papers. If your paper is relevant to a trend that got covered, the coverage exists under the trend's keywords.

## Technique 2: Smart Keyword Extraction

For each paper, extract the **most distinctive claim or result** and search for that instead of the title.

| Paper | Distinctive claim to search |
|---|---|
| CDCR-SFT | "surpassed human performance" "95.33%" CLADDER causal |
| Autonomy Tax | "defense training breaks" LLM agents "47-77%" benign task failure |
| DoxBench | "street-level accuracy" "60%" ChatGPT geolocation |
| agent-audit | "18,899 skills" "13,947 vulnerabilities" ClawHub scan |

## Technique 3: Reverse Citation Search

Instead of searching forward (paper → news), search backward (news → does it cite our work?).

1. Find a major news article about a topic your paper addresses
2. Check if the article links to your arXiv paper, GitHub repo, or project page
3. Search for your arXiv ID (e.g., `2504.19373`) or repo URL within news sites

## Technique 4: Outlet Sweep with `site:` Filters

Do not rely on general web search to surface results from specific outlets. Use `site:` filters to force the search into each outlet.

```
site:darkreading.com "agent security" 2026
site:thehackernews.com ClawHub OR OpenClaw 2026
site:venturebeat.com "anomaly detection" PyOD
```

**Run one query per outlet category**, not one query for all outlets. The `OR` combinator across `site:` filters often fails silently.

## Technique 5: Adoption Chain Search

For tools with wide adoption, search for the adopter, not the tool.

```
Walmart anomaly detection pricing real-time (→ finds Walmart's KDD paper citing PyOD)
NASA spacecraft monitoring anomaly detection Python (→ finds NASA use cases)
"Future of Life" "AI Safety Index" benchmark evaluation (→ finds TrustLLM in the index)
```

## Technique 6: Institutional & Co-Author Search

Coverage often attributes work to the institution or a co-author rather than the PI. Search for:

- **Institutional attribution**: "researchers from USC" + topic, "University of Southern California" + tool/paper topic, "Carnegie Mellon" + anomaly detection (for older work)
- **Co-author names**: For each paper, the first author or most prominent co-author may be named instead. Search for first-author name + paper topic when direct searches fail.
- **Lab-affiliated terms**: "FORTIS lab", "USC Viterbi" + research topic
- **Collaboration partners**: "Adobe Research" + FigEdit, "Harvard" + TDC, "Lehigh" + TrustLLM, "Microsoft Research" + TrustGen

This is especially important for:
- Papers with industry co-authors (Adobe, Microsoft) where the company blog may only name their own researchers
- Multi-institution collaborations where press releases come from the lead institution
- Student-led papers where the student's name may appear in news but not the advisor's

### Common patterns that miss the PI name

| Article says | Actually covers | How to find |
|---|---|---|
| "Researchers from USC Viterbi..." | Your paper | Search: USC Viterbi + paper topic keywords |
| "A team led by [first author]..." | Your paper (you are corresponding/senior author) | Search: first author name + paper topic |
| "Adobe Research presents..." | FigEdit (your collaboration) | Search: Adobe Research + chart editing |
| "Microsoft researchers developed..." | TrustGen (your collaboration) | Search: Microsoft Research + TrustGen |
| "[Student name] receives award for..." | Your mentee's work on your project | Search: student name + research topic |

## Technique 7: Name Disambiguation

"Yue Zhao" is a common name. Always add disambiguators:
- `"Yue Zhao" USC` or `"Yue Zhao" "University of Southern California"`
- `"Yue Zhao" anomaly detection` or `"Yue Zhao" "AI auditing"`
- `"Yue Zhao" PyOD` or `yzhao062`

Similarly, "Aegis" is extremely crowded (Forrester AEGIS, Red Hat aegis-ai, multiple HN projects). Search with:
- `Aegis "Justin0504"` or `Aegis "Aojie Yuan"`
- `Aegis "pre-execution firewall" "AI agent"`
- `"No Tool Call Left Unchecked"`

---

## When to Persist vs. When to Stop

### Persist when:
- The **topic** got coverage but your **paper** has not been traced yet (keep searching with different keyword combinations)
- A new outlet type has not been checked yet (run the outlet sweep)
- The paper has a **distinctive claim** that has not been searched with smart keywords
- An **enterprise deployment** or **policy citation** might exist but has not been searched for

### Stop when:
- You have searched all 10 dimensions (D1-D10) for a given paper/tool, treating D9 and D10 as corpus-level passes that may have already been run for the round
- The same 10 results keep appearing across different queries
- The paper is too recent (< 2 weeks since arXiv posting) for news to have appeared
- The paper is on a niche topic with no trending connection

### How many queries per item:
- **High-star tools** (PyOD, ADBench, TrustLLM): 10+ queries across all dimensions
- **Recent preprints with trending topics** (DoxBench, Autonomy Tax): 6-8 queries, heavy on Dim 4
- **Standard conference papers**: 3-4 queries (title, smart keywords, topic proximity)
- **Older papers** (pre-2023): 1-2 queries unless there is reason to believe new coverage exists

---

## The PDF Blind Spot (Most Important Lesson)

Web search does NOT index text inside PDFs. This means the highest-impact citations are systematically invisible:

- A **U.S. Senate committee report** citing TrustLLM (footnote 119 in HSGAC "Hedge Fund Use of AI" report, Jun 2024) — not findable via any web search query
- **OpenAI/Anthropic/DeepMind system cards** referencing academic benchmarks — often published as PDFs or long pages with embedded references
- **McKinsey/Gartner/Forrester reports** — paywalled PDFs that cite academic tools
- **NIST special publications** — cite academic work in footnotes

These are **Tier 0** — the most valuable citations for tenure, grants, and impact narrative. They are only discoverable by:
1. Identifying candidate documents by topic (Dimension 8 queries)
2. Fetching the PDF
3. Extracting text and searching for your tool/paper names inside

Never assume web search has found everything. The most important citations are the ones buried in PDFs.

### The Domain Blind Spot (Second Most Important Lesson)

`site:`-scoped searches are only as good as the domain list. High-impact reports increasingly live on **dedicated domains** that do not match any known government, think tank, or outlet URL pattern. Examples:

- The **International AI Safety Report 2026** (Yoshua Bengio, 30+ countries) lives on `internationalaisafetyreport.org` — not on `gov.uk`, `oecd.ai`, or any summit domain. A `site:gov.uk TrustLLM` query will never find it.
- **Privacy International** reports live on `privacyinternational.org` — an NGO that falls between "think tank" and "government" categories. No outlet sweep query targeted it.

These documents are Tier 0-1 material. They are invisible to outlet sweeps because the domain is not in the registry.

**How to avoid this blind spot:**

1. **Run name-first queries without `site:` filters.** After the outlet sweep, run queries like `"International AI Safety Report" TrustLLM` or `"Privacy International" DoxBench` — searching for the *report name* or *organization name* paired with your tool name. These succeed regardless of hosting domain.
2. **Run topic-proximity queries without `site:` filters.** A search like `AI geolocation privacy policy report DoxBench 2026` will surface documents on any domain, including unexpected ones.
3. **When a new major report is announced in the news, add its domain to the registry immediately.** Do not wait for the next full audit to discover it lives on a new domain.
4. **Periodically check "landmark reports" lists.** Major AI governance documents are tracked by FLI, OECD, Stanford HAI, and others. Scan those trackers for new report URLs, then search inside them.

The rule: **outlet sweeps find known sources; name-first and topic-proximity searches find unknown sources.** Always run both.

### How to execute Dimension 8

1. **Build the full term list** — extract every tool name, paper acronym, distinctive phrase, and author name from `data/publications.json` and `data/open-source.json`. Include at least 50+ terms.
2. **Download candidate PDFs** — use the query bank to find report URLs, then download them. See "Bypassing Cloudflare / SSR shells / 403 reverse-proxies" below for fetch tactics when scripted requests are blocked.
3. **Extract text and search** — run `python skills/news-search/scripts/pdf_term_scan.py <pdf_path>`. The scanner uses PyMuPDF (`fitz`), runs the FORTIS term list with word-boundary regex for short uppercase tools, and filters known false positives (ECOD inside decoder / BOND inside bonded / MAMA inside mammal / SUOD inside pseudo). Update its `TERMS` and `FALSE_POSITIVE_CTX` constants when the inventory or new collisions appear.
4. **Filter additional false positives at audit time** — common false positives the scanner's lexical filter cannot catch:
   - "Yue Zhao" matching a different person with the same name (Yuchen Zhao, Siyan Zhao, Qingyue Zhao, W. Zhao WildChat, D. Zhao Swiss Cheese) — filter by checking if the context relates to anomaly detection / AI safety / USC / yzhao062. See `references/disambiguation-registry.md`.
   - "Aegis" matching NVIDIA's Aegis dataset, Forrester AEGIS framework, RedHat aegis-ai, aegis-protocol, MIT CSAIL Aegis hardware — filter by requiring "pre-execution firewall" or "tool call" context.
   - "TrustLLM" matching the EU Horizon `trustllm.eu` multilingual LLM project — filter by requiring arXiv:2401.05561 or Lichao Sun.
5. **Search ALL terms in ALL PDFs** — do not search only for TrustLLM. Search for every single one of your 104 papers and 17 tools. A book chapter on COPOD or a patent citing PyOD is just as valuable as a system card citing TrustLLM.

### Bypassing Cloudflare / SSR shells / 403 reverse-proxies

Many high-value sources (gao.gov, docs.house.gov, media.defense.gov, openai.com, web.archive.org/save) refuse default scripted fetches with 403 / 520 / Cloudflare interstitial. The fix is a real Chrome User-Agent plus the document-fetch headers a browser would send. Confirmed working on the 2026-05-07 round for 8/8 previously-blocked PDFs at gov / defense / EU / FM-co domains.

PowerShell template (works on Windows; equivalent `curl -H` works on POSIX):

```powershell
$headers = @{
    "User-Agent"      = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    "Accept"          = "application/pdf,*/*;q=0.8"
    "Accept-Language" = "en-US,en;q=0.9"
    "Sec-Fetch-Dest"  = "document"
    "Sec-Fetch-Mode"  = "navigate"
    "Sec-Fetch-Site"  = "none"
    "Sec-Fetch-User"  = "?1"
    "Upgrade-Insecure-Requests" = "1"
}
Invoke-WebRequest -Uri $url -Headers $headers -OutFile $out -MaximumRedirection 5 -TimeoutSec 60
```

Diagnostic flags that the page is **not** real content even though HTTP 200 came back:

- Raw HTML shorter than ~5 KB while the URL is a multi-section document.
- Body contains `_cf_chl_opt`, `cf-challenge`, `__cf_chl_tk`, or `Enable JavaScript and cookies to continue` — Cloudflare interstitial.
- Body contains only a JSON shell or a `<script>` tag that fetches the real content client-side — modern SSR shell (Wells Fargo R-512394 careers page is the round-3 example).

When a scripted fetch returns a shell, fall back to: (a) Google's cached snippet (often has the rendered DOM at indexing time), (b) Wayback Machine via `https://web.archive.org/web/<url>` — the *retrieval* path is rarely blocked even when `web.archive.org/save/<url>` is, (c) an aggregator mirror (Greenhouse / Lever / Ashby / DFJ Growth / Glassdoor / LinkedIn / Indeed / Hiring Our Heroes for JDs), or (d) ask the user to capture a logged-in browser snapshot into `news-snapshots/`. Never claim absence on a 403 / shell — that's a fetch failure, not a verification.

When `web.archive.org/save/<url>` itself returns "Sorry, Job failed" (OpenAI Careers `technical-intelligence-analyst` had this on 2026-05-07), the source has blocked the Internet Archive crawler. Do not retry — record as "Wayback unavailable, source-side block" and rely on local browser-captured `.html` / `.pdf` sidecars in `news-snapshots/`.

---

## Citation Verification (Critical Step)

**Before adding any result to the audit file, verify that the article actually names or cites your work.** This is the most important quality gate in the skill. Without it, the audit fills with "topic validation" items that look impressive but cannot be used as news on the website.

### How to verify

1. Read the article snippet in the search result. Does it mention a specific tool name (PyOD, TrustLLM, Aegis, agent-audit), a paper title, the PI name ("Yue Zhao"), or the lab ("FORTIS")?
2. If the snippet is ambiguous, fetch the URL and search for the name within the page.
3. If the article only discusses the same topic (e.g., "AI agent security is the challenge of 2026") without naming your work, it goes in the **Topic Validation appendix**, not in the tier structure.

### Snippet-only evidence is not verified evidence

WebSearch snippets are paraphrased / summarized by the search engine and can carry hallucinated content that does not appear in the source. The 2026-05-07 round caught one example: GAO-26-108695 was claimed by the WebSearch summary to name TrustLLM as a "representative system for AI auditing"; manual PDF download + PyMuPDF text extraction confirmed the PDF says nothing of the sort. The snippet was a model synthesis, not a source quote.

Hard rule: **a candidate that would land in Tier 0 (government / foundation-model official document / standards / analyst report) or Tier 1 (mainstream press / national lab / high-impact policy) cannot be promoted on snippet evidence alone.** Phase B must re-fetch the source with `pdf_term_scan.py` (PDFs) or a real-UA HTTP fetch (web pages) and confirm the verbatim quote, before counting. If the source is gated and cannot be re-fetched, set `tier_guess: phase_b_priority` and leave it as a candidate; do not count.

Tier 2 / Tier 3 candidates can be entered on snippet evidence if the snippet contains the verbatim tool-name token (no paraphrase risk on a literal substring) — but the audit row should record the snippet text, not a paraphrase, so the next reviewer can spot synthesis.

### Pre-tier filter: first-party / already-tracked drops

Before assigning a tier, check these drop conditions. They were each stepped into during the 2026-05-07 round:

- **First-party hosting**: pages on the PI's current or prior institution that are about the PI's own work (e.g., `cs.usc.edu/~yzhao010/...`, the PI's CMU PhD-era profile at `heinz.cmu.edu/faculty-research/profiles/zhao-yue`, an NSF PAR record of the PI's own grant output at `par.nsf.gov/servlets/purl/<id>`, or a journal mirror of the PI's own paper at `jmlr.csail.mit.edu/papers/v20/19-011.html`). These are not external coverage. Drop with `tier_guess: first_party`.
- **Already-tracked award URL**: the canonical landing page for an award already recorded in Ledger 5 (e.g., Amazon Research Awards recipient profile, AAAI New Faculty Highlights program page). The award itself is the news; the URL is the citation, not a separate news row. Drop with `tier_guess: already_tracked`.
- **Coauthor-institution publication listing**: a research-listing page on a coauthor institution's site (Microsoft Research, Adobe Research, CMU Tepper, Lehigh Engineering Resolve) that is a bare publication entry, not editorial. Per the audit's Ledger 2 inclusion rule, demote to Ledger 3 (institutional research listing).

### Common false positives

| Search found | Looks like coverage of | Actually is |
|---|---|---|
| TechCrunch article on ChatGPT geolocation | DoxBench | Topic only — paper not cited |
| Dark Reading on OpenClaw crisis | agent-audit | Topic only — tool not named |
| McKinsey on agentic AI security | Aegis / agent-audit | Topic only — tools not named |
| NIST RFI on AI agent security | Your research area | Area validation — tools not cited |

These are still useful for grant narratives but are **not website news items**.

## Output Tracking

All results go into `news-coverage-audit.md`. Each entry must include:

```markdown
- [Outlet Name](URL) — "Headline" (Date) — names: {paper/tool/person named} — verified: {yes/no}
```

Tag each entry with the dimension that found it (D1-D10) so future audits know which strategies produced results.

Items that fail verification go in the **Topic Validation** appendix with this format:

```markdown
- [Outlet Name](URL) — "Headline" (Date) — topic: {related topic} — does NOT name your work
```

At the end of each audit, update the Negative Results table to record which outlet types returned nothing. This prevents wasting time re-searching dead-end outlets.
