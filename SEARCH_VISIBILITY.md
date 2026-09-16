# Search visibility maintenance

The canonical site is `https://viterbi-web.usc.edu/~yzhao010/`. The GitHub Pages mirror continues to declare USC URLs as canonical. Do not switch this identity independently in page metadata, sitemap URLs, profile schema, or Search Console.

## Existing setup

The USC URL-prefix property and its sitemap were confirmed in the maintainer's existing Google Search Console account on September 16, 2026. No second property or new verification record is needed. Keep account identifiers, private analytics exports, and verification credentials outside this public repository.

Use the USC property for indexing and search performance. The current sitemap is `https://viterbi-web.usc.edu/~yzhao010/sitemap.xml`. Submitted URLs, discovered URLs, indexed pages, and search clicks are different measurements. An alternate page with the intended canonical is not necessarily an error. Inspect actual examples before changing URLs or requesting validation, especially for BibTeX query URLs and auxiliary files.

USC hosts this site under a user directory. A robots.txt file at `/~yzhao010/robots.txt` does not control crawlers for the host; the relevant location is `https://viterbi-web.usc.edu/robots.txt`. That root URL returned 404 during the September 16 check, which is not a robots-based disallow. This repository's robots.txt operates at the root of the GitHub Pages mirror. Submit the USC sitemap through Search Console rather than relying on a subdirectory robots file. Do not change university-wide crawler policy.

## Content and identity

The homepage uses ProfilePage with Yue Zhao as its Person main entity. The visible headshot is also the profile image. The WebSite publisher, laboratory member, and publications-page author share the canonical `#person` identifier. This helps consumers relate records; it does not guarantee a knowledge panel, ranking, or generated-answer citation.

Google's inspected homepage record flagged the date-only ProfilePage `dateModified` as an invalid datetime on September 16, 2026. The optional field is omitted rather than supplying an invented time. If it is reintroduced, use an actual profile modification timestamp with its timezone. The sitemap's date-only `lastmod` follows a separate format and remains valid. The Search Console warning can only be checked again after deployment and recrawling.

The homepage, publications page, and lab page ship navigation and sidebar HTML directly, generated from `includes/`. Readers and retrieval tools can access these without executing JavaScript. The JavaScript loader retains enhancement and supports other pages. Publication lists and the biography remain generated from their existing data sources. Preserve actual titles, authors, venues, publication status, primary-source links, and disclosures. Update research claims through the existing content workflow rather than adding keyword repetitions or hidden search copy.

## Checks and publication

Run:

```bash
python scripts/prerender_pages.py
python scripts/ci_check_site.py
```

The CI job regenerates the three core pages and fails if their committed HTML is stale. Search checks cover all sitemap HTML routes: distinct titles/descriptions, USC canonical and Open Graph URLs, parseable JSON-LD, and accidental indexing/snippet blocks. The core pages also check static include freshness and Person identity references.

Sitemap dates come from per-page Git history. They should not be changed to today's date merely to appear fresh. Regeneration can pick up genuine older changes whose sitemap date lagged a commit. See the CI job's lastmod notice for this known sequencing behavior.

After an authorized push, confirm both GitHub Pages and the USC mirror have the new source. USC uses its separate scheduled deployment described in [the deployment runbook](DEPLOY_TMUX.md); GitHub CI success alone does not prove USC deployed. Verify live canonical URLs, page content, the sitemap, and real HTTP 404 behavior before marking the rollout complete.

## Measurement routine

Compare complete 28-day periods, allowing for reporting delay. Separate branded queries such as Yue Zhao and FORTIS Lab from research-topic queries, and compare by landing page. Check impressions, clicks, CTR, and average position together; low-volume changes can be noisy. Prioritize the homepage, publications, lab, and relevant project pages over indexing every auxiliary file. Record dated baselines outside the public repository. Check Google-selected versus declared canonical on key URLs and inspect causes before resubmitting. No recurring automation is installed by this document.

Search visibility and accurate AI citations depend on useful, accessible content and clear evidence. There is no universal registration for every LLM, and no special file or schema guarantees retrieval. Existing crawlable HTML, stable identity, source links, and maintained research pages are the foundation.

References: [Google ProfilePage guidance](https://developers.google.com/search/docs/appearance/structured-data/profile-page), [robots.txt placement](https://developers.google.com/search/docs/crawling-indexing/robots/create-robots-txt), [Google AI features guidance](https://developers.google.com/search/docs/appearance/ai-features).
