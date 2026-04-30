---
name: dual-update
description: Add or update content that must appear on both the website and the LaTeX CV. Use when the user mentions adding a new paper, award, grant, service role, teaching course, PhD student, open-source project, or any other content that overlaps between the website and CV.
---

# Dual Update — Website + CV

When the user adds or updates content that exists in both the website and the CV, **always update both sides in the same pass**. Never update one and forget the other.

## Content Type → File Mapping

| Content type | Website file(s) | CV file(s) | Notes |
|---|---|---|---|
| **Publication** (peer-reviewed) | `data/publications.json` | `cv/cv-full.tex` (Publications section) | Website JSON uses structured fields; CV uses `\item` in `benumerate`. Match venue, year, authors, title format. Also check `data/lab-members.json` for co-authors. |
| **Preprint / under submission** | `data/publications.json` (section `"preprint"`) | `cv/cv-full.tex` (Preprints section) | Add to both. Website preprints render on `publications.html` via the JSON `section: "preprint"` entries. |
| **Award / Grant** | `index.html` (Awards section) | `cv/cv-full.tex` (Awards section) | Both use chronological order, newest first. |
| **Service role** (reviewer, AC, editor, organizer) | `services.html` | `cv/cv-full.tex` (Services section) | Match the sub-category (organizing, editorial, AC/reviewer, journal reviewer). |
| **Teaching course** | `teaching.html` | `cv/cv-full.tex` (Teaching section) | Include semester, course number, title, enrollment if known. |
| **PhD student** | `data/lab-current-phd.json` | `cv/cv-full.tex` (PhD Students section) | JSON has structured fields; CV uses inline LaTeX. |
| **Open-source project** | `data/open-source.json` | `cv/open-source.tex` (**auto-generated**) | Edit JSON only, then run `python scripts/generate_cv_open_source.py`. Do NOT edit `cv/open-source.tex` directly. |
| **Research direction / keywords** | `index.html` (Research section) | `cv/cv-full.tex` (Research Summary section) | Keep the three-pillar structure consistent. |
| **News item** | `index.html` (News section) | — | Website only. |
| **Lab member** (non-PhD) | `data/lab-members.json` | — | Website only. When adding a new member, check `data/publications.json` for their published papers and populate the `publications` field. |
| **Talks** | — | `cv/cv-full.tex` (Talks section) | CV only (not on website currently). |
| **Student committee** | — | `cv/cv-full.tex` (Student Committee section) | CV only. |

## Workflow

1. **Ask what changed** if the user hasn't specified clearly. Get: content type, the specific details (title, venue, year, authors, etc.).
2. **Read both target files** before editing. Understand existing format and ordering.
3. **Verify external facts with a web search** before writing them. Use the agent's available web-search/browser tool for any fact you cannot read out of the repo: real conference dates (for `sort_date`), conference location, official venue acronym/abbreviation, arXiv ID, GitHub URL, project page, co-author homepage. Do not invent dates or URLs. If a search cannot confirm a fact, leave it out (omit the link, omit the `sort_date`) and state in the response that it was omitted because it was unverified.
4. **Make both edits** in the same response. For the website side, match the existing HTML/JSON structure. For the CV side, match the existing LaTeX formatting.
5. **For open-source changes**: edit `data/open-source.json`, then run the generation script. Do not hand-edit `cv/open-source.tex`.
6. **Verify consistency**: after editing, briefly confirm both sides have the same content.

### Recommended searches for publication updates

When adding or moving a peer-reviewed paper, run these searches before writing:

- `<VENUE> <YEAR> conference dates location` — get real start/end dates for `sort_date` (the website sorts by descending `sort_date`, so accuracy here decides display order). Set `sort_date` to the conference start date in `YYYY-MM-DD` form. If two same-year venues collide on the regex-inferred default (the script in `publications.html` hardcodes month-by-venue, e.g., ACL→Aug, ICML→Jul, which can be wrong year-to-year), an explicit `sort_date` overrides it.
- `<paper title> arxiv` — confirm the arXiv ID is correct.
- `<paper title> github` or check what the user pasted — only link a GitHub URL that the user provides or that you have confirmed exists.
- For news items mentioning a co-author, do **not** auto-link a homepage you have not verified. Use plain text instead.

## Format Guidelines

### Publications (website JSON)
```json
{
  "id": "conference-short-slug",
  "section": "conference",
  "title": "Paper Title",
  "paper_url": "https://arxiv.org/abs/...",
  "authors": "Author1, Author2, ..., and AuthorN",
  "venue": "VENUE, YEAR",
  "year": 2026,
  "links": [
    {"type": "github", "url": "https://github.com/..."}
  ],
  "abstract": "..."
}
```
Use `"section": "conference"` for conference papers, `"section": "workshop"` for workshop papers, and `"section": "journal"` for journal papers. The website groups conference and workshop entries in the same rendered section, but the JSON distinguishes them. The `links` array can include entries with `type` set to `"github"` or `"project"`. Mark equal contribution with `†` and corresponding author with `♠` in the `authors` string.

### Preprints (website JSON)
```json
{
  "id": "preprint-short-slug",
  "section": "preprint",
  "title": "Paper Title",
  "paper_url": "https://arxiv.org/abs/XXXX.XXXXX",
  "authors": "Author1, Author2, ..., and AuthorN",
  "venue": "arXiv preprint",
  "year": 2026,
  "links": [],
  "abstract": "..."
}
```
Preprints render on `publications.html` under "Preprints & Working Papers", sorted by arXiv ID (newest first).

### Publications (CV LaTeX)
Papers in the CV use `benumerate` with reverse numbering. Match the existing style:
```latex
\item AUTHOR\_LIST. ``TITLE.'' \textit{VENUE}, YEAR. \href{URL}{[PDF]}
```
- Mark equal contribution with `\equalcontrib` and corresponding author with `\corrauthor`.
- The CV contains papers not on the website (older work, preprints). This is expected.

### Awards (website HTML in index.html)
```html
<li>AWARD_NAME (YEAR)</li>
```

### Awards (CV LaTeX)
```latex
AWARD_NAME & TYPE & DATE \\
```

## Important Reminders

- The CV is a **superset** of the website for publications — it includes older papers and preprints that may not be on the website.
- When adding a new peer-reviewed paper, add to **both** unless the user says otherwise.
- When adding a preprint, add to **both** `data/publications.json` (with `section: "preprint"`) and `cv/cv-full.tex`.
- Always preserve reverse chronological ordering in both places.
- Run `python scripts/generate_cv_open_source.py` after any change to `data/open-source.json`.
- **Publication ↔ lab-members sync**: When adding a new published paper to `data/publications.json`, check if any non-PhD lab member (in `data/lab-members.json`) is a co-author. If so, add the paper to their `publications` array. Note that author names may differ between the two files (e.g., display name vs legal name), so match carefully. Only list published papers with a venue, not arXiv-only preprints.

## News Item Trigger (index.html)

Some dual-update events also warrant a news item in the News section of `index.html` (top of the list, newest first). Add a news item — in addition to the dual update — when any of the following happens:

- A paper is **newly accepted** to a venue (including moves from preprint → conference/workshop/journal). Mention the title, venue, and lead author.
- A paper wins a **best paper / spotlight / oral** award.
- A new **grant or award** is received (PI or co-PI).
- A **PhD student passes their qualifying exam** or other major milestone.
- A new **open-source release** that is significant enough to flag publicly.

Match the tone and length of nearby items. For paper acceptance, a one-sentence congratulations with the venue in italics and an arXiv link is enough. Do not invent a homepage URL for a co-author you cannot verify; just write the name in plain text.

If the user already has a relevant news item drafted or asks you to skip the news, do not add one.

## CV Paper Count Check

**After every publication change**, verify that the `benumerate` start numbers in `cv/cv-full.tex` are correct. The CV uses three `benumerate` sections with reverse numbering:

- `benumerate{N1}` for Preprints (numbers N1 down to N2+1)
- `benumerate{N2}` for Journals (numbers N2 down to N3+1)
- `benumerate{N3}` for Conference/Workshop (numbers N3 down to 1)

The rule: **N1 = total papers**, **N2 = journals + conference/workshop**, **N3 = conference/workshop only**. When you add a paper to any section, increment the start numbers of that section and all sections above it.

Run `python scripts/check_cv_paper_count.py` to verify. If it reports a mismatch, fix the `benumerate` start numbers before compiling.
