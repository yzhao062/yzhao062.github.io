# Search behavior: documented versus folklore

Verified 2026-08-25 against Google Search Central only, at `developers.google.com/search`.
Re-verify before relying on any of it; this page records what was documented on that date.

Much advice in this area is folklore that has been repeated until it sounds like a rule.
The two columns below exist because a single run of this skill produced three confident
claims that turned out to be folklore. Two of the three came from the agent running it.

## Verified

| Claim | Official wording | Source |
|---|---|---|
| Google may rewrite the title link shown in results | Lists as a problem case that "the page title doesn't reflect the page content"; also names obsolete, inaccurate, and half-empty titles, and duplicate site names. Wording is "may" and "might" throughout, never a guarantee | `/docs/appearance/title-link` |
| Title-link generation draws on many inputs | The `<title>`, the main visual title, "Heading elements, such as `<h1>` elements", `og:title`, prominent on-page text, anchor text, and `WebSite` structured data | `/docs/appearance/title-link` |
| `<meta name="keywords">` does nothing | "The meta-keyword tag is not used by Google Search, and it has no effect on indexing and ranking at all" | `/docs/crawling-indexing/special-tags` |
| Heading order does not matter to Search | "from Google Search perspective, it doesn't matter if you're using them out of order"; no ideal number of headings | `/docs/fundamentals/seo-starter-guide` |
| `sameAs` disambiguates a person | "You can use the `sameAs` property as an alternative. Google can understand both `sameAs` and `url` when disambiguating authors" | `/docs/appearance/structured-data/article` |
| Screen-reader-only text is not by itself a violation | Permits "Text that's only accessible to screen readers and is intended to improve the experience for those using screen readers" | `/docs/essentials/spam-policies` |
| Off-screen text can be a violation | Lists "Using CSS to position text off-screen" as an abuse example | `/docs/essentials/spam-policies` |

## Not documented, treat as folklore

| Common claim | What is actually documented |
|---|---|
| A title should stay under about 60 characters, or about 600 pixels | "there's no limit on how long a `<title>` element can be". Truncation is described as fitting the device width. No character or pixel threshold appears. Any number is a community estimate |
| A `<title>` that differs from the H1 triggers a rewrite | Not documented as an independent trigger. What is documented is broader and narrower at once: a title that does not reflect page **content** is a listed problem case, and H1 is one of several possible title-link sources |
| A visually hidden H1 is free keyword space that only crawlers read | Nothing documents how a CSS-clipped H1 is weighted. The spam policy keys on **intent**: accessibility text is permitted, off-screen positioning is an abuse example. Hidden text placed for search engines sits on the wrong side of that line |
| A hidden H1 is ignored, or penalized, or weighted equally | All three are undocumented. The honest position is that the treatment is unknown |

## What follows for naming work

Two documented facts carry most of the practical weight.

**Meta keywords are inert to Google Search.** A term present only in a `keywords` list
gets no Google indexing or ranking benefit from that tag. To carry weight it has to appear
in visible text, in a documented title-link input, or in structured data. Other consumers of
the tag are outside what Google documents, so claim nothing about them.

**Disambiguation has a supported mechanism.** Google documents `url` and `sameAs` as
author-disambiguation inputs in Article markup. For a common personal name, point them at
pages that identify the person uniquely: an ORCID record, an institutional page, a
curated bibliography. Treat them as supported signals. Nothing documents that they resolve
a collision completely, and hidden keyword text is not an alternative.

**Check an identity link before asserting it.** A profile that merges two people makes the
`sameAs` claim partly false. In one run, a curated bibliography carried a visible
"ORCID ID conflict" banner and an auto-built profile held a paper from an unrelated field.
Read the record, not just the name on it.

## Method note

When checking a claim in this area, search the official domain for the specific phrasing
and report NOT-VERIFIED when the official pages are silent. NOT-VERIFIED means the check
cannot support the rule; it does not mean the rule is false. Keeping that distinction is
what stops a reference like this one from laundering folklore into fact.
