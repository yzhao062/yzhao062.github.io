# OpenAI Careers — Technical Intelligence Analyst, San Francisco

Local snapshot for the Ledger 1 #8g citation in `news-coverage-audit.md`. Careers pages are pulled when roles are filled, so this file preserves the verified evidence text out-of-band from the live URL.

## Source

- **Live URL:** https://openai.com/careers/technical-intelligence-analyst-san-francisco/
- **Captured:** 2026-05-07. Both committed sidecars (HTML + PDF) were saved by the user from a logged-in Chrome browser session, since the workspace fetcher hit the Cloudflare bot-challenge.
- **Wayback archive URL:** _not available — Save Page Now returned "Sorry, Job failed" on 2026-05-07 even from a logged-in browser session, because OpenAI's Cloudflare configuration blocks the Internet Archive crawler at the source. This is not a workspace-side limit; the URL cannot be archived to web.archive.org from any client until OpenAI loosens the bot policy. The committed sidecars below are the canonical snapshot._
- **Browser-side captures (sidecars, committed alongside this file):**
    - `openai-careers-technical-intelligence-analyst-2026-05-07.html` — rendered DOM saved from a logged-in browser tab (`Ctrl+S` -> "Webpage, complete"). 268 KB. Verified to contain the full Qualifications block including the verbatim PyOD line.
    - `openai-careers-technical-intelligence-analyst-2026-05-07.pdf` — `Print` -> `Save as PDF`. 144 KB self-contained portable record. PyOD verified by `python skills/news-search/scripts/pdf_term_scan.py news-snapshots/openai-careers-technical-intelligence-analyst-2026-05-07.pdf` -> hit on page 2.
- **Verification:** Confirmed during the 2026-05-07 news-search Phase B sweep; recorded in `news-search-candidates.jsonl` row with `status: counted`.

## Verified excerpt

Verbatim text from the live job listing's Qualifications section, captured 2026-05-07:

> Have experience with anomaly detection tools, such as PyOD, and discovery processes for surfacing novel or low-prevalence patterns.

Surrounding context (same Qualifications block):

> ... integrity, trust and safety, operational risk, or a related quantitative risk domain. Are strong in SQL and Python, including querying, organizing, and transforming complex datasets. Have delivered zero-to-one analyses and turned them into reusable playbooks, workflows, or lightweight tools. **Have experience with anomaly detection tools, such as PyOD, and discovery processes for surfacing novel or low-prevalence patterns.** Learn new systems, processes, datasets, and team dynamics quickly. ...

The mention is on the live job description, not in a system card or safety report; it is treated as Tier 0(b)-equivalent foundation-model-company official content because OpenAI is the publisher and PyOD is named as expected operational tooling for the Intelligence & Investigations role, not as background literature.

## Why this snapshot exists

1. **The live URL will go stale.** OpenAI takes down filled roles. Without an out-of-band copy of the evidence, the Ledger 1 #8g citation becomes unverifiable as soon as the role is closed.
2. **Wayback Machine cannot archive this URL.** Both this workspace's automated `web.archive.org/save/...` call (520 from archive.org, Cloudflare challenge from openai.com) and a logged-in browser-side Save Page Now attempt on 2026-05-07 returned "Sorry, Job failed". OpenAI's bot policy blocks the Internet Archive crawler, so there is no public archive URL to point at. Browser-side `.html` and `.pdf` sidecars are the only durable record.
3. **The candidate file (`news-search-candidates.jsonl`) is `.git/info/exclude`-masked**, so its evidence note does not survive a fresh clone. This file is committable.

## How to keep this current

- Periodically re-attempt Wayback Save Page Now (every few months). If OpenAI ever loosens the bot policy and a snapshot lands, paste the archive URL into the **Source URLs** row of `news-coverage-audit.md` (Ledger 1 section) so the public-archive path becomes available.
- If OpenAI rotates the URL slug, update the Live URL here, capture fresh `.html` / `.pdf` sidecars from a logged-in browser session, and add a "Successor URL:" line so the audit history stays traceable.
- **Retain Ledger 1 #8g as long as the committed sidecars remain readable, even if the live URL goes 404.** The `.html` and `.pdf` are the canonical first-party-OpenAI evidence; the live URL is the live-discovery pointer, not the load-bearing citation. Add a "live URL stale" note to the Ledger 1 row when the live page disappears, but do not demote.
- Demote to Ledger 3 only if the sidecars are absent, corrupted, or shown not to be a first-party OpenAI capture (e.g., proven to be an aggregator mirror). Verify by re-running `pdf_term_scan.py` on the PDF and inspecting the HTML headers.
