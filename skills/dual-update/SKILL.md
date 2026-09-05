---
name: dual-update
description: Add or update content that must appear across the website, the LaTeX CV, and the GitHub profile README. Use when the user mentions a new paper, award, grant, service role, teaching course, PhD student, open-source project, research direction, or headline metric. Use it for any other content that overlaps those surfaces.
---

# Dual Update: Website, CV, and GitHub Profile

When the user adds or updates content that exists on more than one surface, **update every affected surface in the same pass**. Never update one and forget another.

There are three surfaces. The first two live in this repository. Because the third is a separate repository, it is the one most easily forgotten:

| Surface | Location | Kind |
|---|---|---|
| Website | this repo | HTML and JSON |
| CV | `cv/` in this repo | LaTeX, compiled to a distributed PDF |
| GitHub profile README | `../yzhao062/README.md`, repo `yzhao062/yzhao062` | Markdown, rendered at <https://github.com/yzhao062> |

Not every change touches all three. The table below maps the first two; the **GitHub Profile README** section after it says when the third is in scope.

## Content Type → File Mapping

| Content type | Website file(s) | CV file(s) | Notes |
|---|---|---|---|
| **Publication** (peer-reviewed) | `data/publications.json`, `files/yue-zhao.bib` | `cv/cv-full.tex` (Publications section) | Website JSON uses structured fields; CV uses `\item` in `benumerate`. Match venue, year, authors, and title format. Also sync the public BibTeX `files/yue-zhao.bib` (linked from `publications.html`, fetched by `bib-viewer.html`): use the accepted venue's BibTeX type and venue field, for example `@inproceedings` with `booktitle` for conference or workshop papers and `@article` with `journal` for journal papers. Also check `data/lab-members.json` for co-authors. |
| **Preprint / under submission** | `data/publications.json` (section `"preprint"`), `files/yue-zhao.bib` | `cv/cv-full.tex` (Preprints section) | Add to all three. Website preprints render on `publications.html` via the JSON `section: "preprint"` entries. In `files/yue-zhao.bib` a preprint is an `@article` with `journal={arXiv preprint arXiv:...}`; on acceptance, switch that entry to the accepted venue's BibTeX type and venue field, year, and final venue text. |
| **Award / Grant** | `index.html` (Awards section) | `cv/cv-full.tex` (Awards section) | Both use chronological order, newest first. |
| **Service role** (reviewer, AC, editor, organizer) | `services.html` | `cv/cv-full.tex` (Services section) | Match the sub-category (organizing, editorial, AC/reviewer, journal reviewer). |
| **Institutional leadership appointment** (institute/center director, associate director, or similar named USC role) | `services.html` (Institutional Leadership); optionally `files/bio.txt` as a current-profile surface | `cv/cv-full.tex` (Services → Institutional Leadership) | Use the exact title from the offer letter, and a finite term (`2026-2027` in HTML, `2026--2027` in LaTeX). Never write `Present` and never infer months the letter does not state. The dated CV and services records stay accurate after the term. If `files/bio.txt` says the appointee currently serves in the role, revise or remove that clause after the term. Keep it out of Professional Experience, which holds employment and external advisory roles. Link the institute's home page, not its leadership page, which may not list the appointee yet. |
| **Teaching course** | `teaching.html` | `cv/cv-full.tex` (Teaching section) | Include semester, course number, title, enrollment if known. |
| **PhD student** | `data/lab-current-phd.json` | `cv/cv-full.tex` (PhD Students section) | JSON has structured fields; CV uses inline LaTeX. |
| **Open-source project** | `data/open-source.json` | `cv/open-source.tex` (**auto-generated**) | Edit JSON only, then run `python scripts/generate_cv_open_source.py`. Do NOT edit `cv/open-source.tex` directly. |
| **Research direction / keywords** | `index.html` (Research section), `files/bio.txt` | `cv/cv-full.tex` (Research Summary section) | Keep the same four audit questions across these sources and `../yzhao062/README.md`. Translate the wording to fit each surface without changing the count or scope. |
| **News item** | `index.html` (News section) | — | Website only. |
| **Lab member** (non-PhD) | `data/lab-members.json` | — | Website only. When adding a new member, check `data/publications.json` for their published papers and populate the `publications` field. |
| **Talks** | — | `cv/cv-full.tex` (Talks section) | CV only (not on website currently). |
| **Student committee** | — | `cv/cv-full.tex` (Student Committee section) | CV only. |


## GitHub Profile README

The profile README renders at <https://github.com/yzhao062> and is the first thing a
recruiter, collaborator, or investor sees. It lives in a **separate repository**,
`yzhao062/yzhao062`, cloned at `../yzhao062` beside this one. Because it is a different
repo, it survives every `git status` run here, which is exactly why it goes stale.

### The README follows the website

**The website is the source of truth and the README is downstream of it.** The README's
GitHub and Pepy badges update from their source services. The Google Scholar
badge and every figure in prose are hardcoded, so they go stale silently. On any change to
the facts below, open both files and copy the site's version across. Do not restate a
figure from memory, and do not treat a README number that disagrees with the site as the
newer one.

Work the table field by field rather than reading the README and deciding what looks
out of date. Reading it is how the headline blocks get missed, because they are the parts
that read fluently while being wrong.

| README element | Authoritative source | Notes |
|---|---|---|
| Subtitle under the name | `index.html` Research box | Must name the same pillars the site names, in the same count. |
| `> [!NOTE]` summary block | `files/bio.txt` | The single densest cluster of stale numbers. Check every figure in it against the bio, one at a time. |
| Aggregate stars and downloads | `files/bio.txt`, the sentence beginning "His open-source projects, including" | It gives the figure, the scope, and the example project list. Copy all three; a different example list makes the same total look like a different claim. |
| PyOD's own download figure | `data/open-source.json` | **Not the same number as the aggregate.** The site says PyOD alone has 55M+ downloads and all projects together exceed 60 million. Mixing them misstates both. |
| PyOD adopters | `files/bio.txt` | The bio distinguishes **named by** OpenAI from **used by** the others. Preserve that split. Collapsing it into one verb claims endorsements nobody gave. |
| Per-project star counts | `data/open-source.json` | Prefer a shields.io badge, which stays current on its own. |
| Research taxonomy and its count | the four collapsible headings in `index.html` | Use the site's names verbatim. Presentation order may differ, and here it is deliberately inverted so the agent work leads. |
| Venture and advisory roles | `index.html` About, the Current Focus card | Copy the site's description of each role, and give it the same weight the site gives it. |
| Paper count, appointments, policy citations | `files/bio.txt` | |
| Open-source table rows | `data/open-source.json` | |

A figure that appears in the README with **no counterpart anywhere on the site** is neither
confirmed nor refuted by this repository. The Google Scholar citation count is the current
example. Ask the user for the current value rather than guessing, and say plainly that the
repository cannot check it. Never refresh it by inference, and never delete it just because
the site is silent.

The Scholar badge stays **static on purpose**, and the question of making it live has been
settled once. Google Scholar publishes no API. It answers an automated request with a `200`
carrying a bot-block page rather than the profile, verified from a residential address in
August 2026. A datacenter address, such as a GitHub Actions runner, fares worse. Such a
scraping workflow therefore fails, and it fails in the worst available way, by continuing
to serve the last number it captured. That looks live while being stale, so nobody thinks
to check it. Semantic Scholar does publish an API, but it rate-limits anonymous callers and
counts differently. A badge built on it has to be labelled Semantic Scholar and will show a
different number. Refresh the badge and the prose together when the user supplies a figure.

### Match the Site's Facts and Emphasis

Two surfaces can agree on every fact and still disagree, because a topic given one sentence
on the site can occupy a callout box at the top of the README. Prominence is a claim about
importance, so a mismatch in prominence is a mismatch in substance.

After the facts line up, compare weight. For each topic, ask how much room and how high a
position the site gives it, then give it comparable room and position in the README:

| Site treatment | README treatment |
|---|---|
| The site hero or opening About summary | The single top-level `> [!NOTE]` summary |
| A heading with its own section | A `##` section |
| One card among peers, or one clause in the bio | One sentence inside the existing `> [!NOTE]` block; never a standalone alert |
| A line in a table or list | A row or bullet |
| Absent | Absent |

Use a standalone `> [!IMPORTANT]` only when the same topic appears in the site hero or
another top-of-page lead. Otherwise follow the table above, and move any contact action to
`## Contact`. This has already gone wrong once. The venture held its own `> [!IMPORTANT]`
block while the site had reduced it to one sentence in one of three equal cards. As a
result, the README read as a company page with a professor attached.

Emphasis drifts silently, because nothing about a stale callout looks wrong when you read
it. Check emphasis on every pass, including passes where the underlying facts stay the
same.

Publications, awards, grants, service roles, teaching, PhD students, and news items do
**not** appear in the README. Do not add sections for them.

### Rules

1. **Refresh before editing.** Run `git -C ../yzhao062 status --short --branch` first.
   If the worktree is dirty, stop and ask how to preserve those changes. If it is clean,
   run `git -C ../yzhao062 pull --ff-only`, and stop rather than merging or rebasing if
   Git reports divergence. A bare `git pull` is wrong here: this machine has
   `pull.rebase=false`, so a divergent history produces a merge commit, which is a commit
   nobody approved. The repo is edited through the GitHub web UI as well, so the local
   clone is often behind, and editing a stale copy silently reverts what was changed there.
2. **Diff the facts before you finish, do not eyeball them.** Pull every figure and every
   named list out of both files and compare them as sets, so a divergence is reported
   rather than noticed. The cheap version:

   ```bash
   grep -ohE "[0-9][0-9,.]*[KkMm]?\+? (million )?(GitHub stars|downloads|peer-reviewed papers)" \
     files/bio.txt ../yzhao062/README.md | sort -u
   grep -ohE "named by[^.]*\.|used by[^.]*\." files/bio.txt ../yzhao062/README.md | sort -u
   ```

   Each command should print one line per distinct claim. Two lines that say the same
   thing differently is the signal to reconcile them against `files/bio.txt`.
3. **Match the value, not the typography.** `30,000` in the bio and `30k+` in the README
   are the same claim, and each suits its own surface. What must never differ is the
   number itself or its precision. Do not turn `over 80` into `83`, or `55M+` into
   `54.8M`, and do not carry the aggregate figure into a sentence about one project.
4. **The README is a separate commit and a separate push,** and both need explicit
   approval like any other. Say plainly that two repositories are being changed.
5. **If `../yzhao062` is missing,** clone it with
   `git clone https://github.com/yzhao062/yzhao062.git ../yzhao062` rather than editing
   through the web UI, so the change goes through the same review as everything else.

## Workflow

1. **Ask what changed** if the user hasn't specified clearly. Get: content type, the specific details (title, venue, year, authors, etc.).
2. **Read every target file** before editing, including `../yzhao062/README.md` when the change is in scope for it. Understand existing format and ordering.
3. **Verify external facts with a web search** before writing them. Use the agent's available web-search/browser tool for any fact you cannot read out of the repo: real conference dates (for `sort_date`), conference location, official venue acronym/abbreviation, arXiv ID, GitHub URL, project page, co-author homepage. Do not invent dates or URLs. If a search cannot confirm a fact, leave it out (omit the link, omit the `sort_date`) and state in the response that it was omitted because it was unverified.
4. **Make every edit** in the same response. For the website side, match the existing HTML/JSON structure. For the CV side, match the existing LaTeX formatting. For the profile README, match the existing Markdown. Preserve badge syntax while updating hardcoded values. Keep an alert block only while it satisfies the emphasis mapping above; otherwise merge, move, or remove it.
5. **For open-source changes**: edit `data/open-source.json`, then run the generation script. Do not hand-edit `cv/open-source.tex`.
6. **Verify consistency**: after editing, briefly confirm every touched surface agrees. For numbers, grep each figure across all three so no copy is left behind.

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

- **Three publication surfaces, not two**: every publication add, move, or remove must touch `data/publications.json`, `cv/cv-full.tex`, AND `files/yue-zhao.bib`. The BibTeX file is a public copy-paste surface linked from `publications.html`; `scripts/ci_check_site.py` only checks that each JSON title has some BibTeX match, so it does not catch a stale venue or a leftover removed entry. `files/yue-zhao.bib` is hand-maintained, not generated.
- The CV is a **superset** of the website for publications — it includes older papers and preprints that may not be on the website.
- When adding a new peer-reviewed paper, add to **both** unless the user says otherwise.
- When adding a preprint, add to **both** `data/publications.json` (with `section: "preprint"`) and `cv/cv-full.tex`.
- Always preserve reverse chronological ordering in both places.
- Run `python scripts/generate_cv_open_source.py` after any change to `data/open-source.json`.
- **Publication ↔ lab-members sync**: When adding a new published paper to `data/publications.json`, check if any non-PhD lab member (in `data/lab-members.json`) is a co-author. If so, add the paper to their `publications` array. Note that author names may differ between the two files (e.g., display name vs legal name), so match carefully. Only list published papers with a venue, not arXiv-only preprints.

## News Item Trigger (index.html)

Some dual-update events also warrant a news item in the News section of `index.html` (top of the list, newest first). Add a news item — in addition to the dual update — when any of the following happens:

- A paper is **newly accepted** to a venue, including a move from preprint → conference, workshop, or journal, **when Yue-led credit framing applies**. This framing applies when Yue is last or co-last author, or a Yue-advised student is first author. Mention the title, venue, and lead author. When only neutral framing applies (Yue is a middle author and no Yue-advised student is first author), **skip the news item by default**: do the three-surface publication update and stop. A Yue-advised co-author in a middle slot does not by itself earn a news item. Add one anyway only if Yue asks, or if the result is unusually notable (best paper, oral, or spotlight; see the next trigger). (Confirmed by Yue 2026-07-17 on the COLM 2026 FlexRouter update.)
- A paper wins a **best paper / spotlight / oral** award.
- A new **grant or award** is received (PI or co-PI).
- A **PhD student passes their qualifying exam** or other major milestone.
- A new **open-source release** that is significant enough to flag publicly.
- A named **institutional leadership appointment** (institute or center director, associate director, or similar) is accepted. Name the institute, the term, and the people the role reports to or works with when the offer letter states them.

Match the tone and length of nearby items. For paper acceptance, a one-sentence congratulations with the venue in italics and an arXiv link is enough. Do not invent a homepage URL for a co-author you cannot verify; just write the name in plain text.

**Credit framing.** Check author positions before writing. When Yue is last (or co-last) author, or when a Yue-advised student is first author, use possessive framing ("Our paper", "Our group's work", "led by [student first author]"). When Yue is a middle author and no Yue-advised student is first author, the work is led by another lab; use neutral framing such as "Co-authored", "Collaborative paper at ...", or "Two papers Yue co-authored" instead of "Our paper", and do not introduce external first authors as "lead author" in a way that implies Yue is the senior advisor. The goal is to acknowledge the contribution without overclaiming credit from the leading lab.

If the user already has a relevant news item drafted or asks you to skip the news, do not add one.

### Rolling Three-Month News Window (Do This Every Time a News Item Is Added)

The News section in `index.html` keeps **only the current month and the two before it** visible. Everything older lives inside the collapsed `<details class="smart-details">` block whose summary reads "Show more news". Whenever you add a news item, fold anything that has fallen outside the window in the same edit, so the window maintains itself instead of drifting. (Confirmed by Yue 2026-08-01, when the visible list had grown to five months.)

Worked example: adding an item in August 2026 leaves August, July, and June visible, and pushes May and everything older into the collapsed block.

**How to fold, and what not to do.** The visible items sit directly above the `<details>` opener and the collapsed ones directly below its `<summary>`. To fold, **move the `<details>` and `<summary>` lines upward** so the now-outdated paragraphs fall inside the block. Do not cut and re-paste the paragraph text, and do not rewrite any wording. A correct fold produces a diff of two added lines and two removed lines, touching no news prose. If the diff is larger than that, something was rewritten and should be redone.

Newly folded items land immediately after the `<summary>`, which puts them ahead of the items already collapsed and preserves reverse-chronological order throughout.

**Verify after folding.** Count the news paragraphs before and after; the total must be unchanged, because folding hides items and never deletes them. Confirm the visible set covers exactly the intended three months, and confirm the `<details>` and `<p>` tags are still balanced inside the News section. A quick check:

```python
import re, collections, pathlib
t = pathlib.Path("index.html").read_text()
news = t.split('<h2 id="news">')[1].split('<h2 id="awards">')[0]
head, tail = news.split("Show more news")
print("visible:", dict(collections.Counter(re.findall(r"\[([A-Za-z]{3}) \d{4}\]", head))))
print("folded :", dict(collections.Counter(re.findall(r"\[([A-Za-z]{3}) \d{4}\]", tail))))
print("details balanced:", news.count("<details") == news.count("</details>"))
```

The window is about display only. Never delete a news item to satisfy it, and never reorder items to make the boundary land more neatly.

## CV Paper Count Check

**After every publication change**, verify that the `benumerate` start numbers in `cv/cv-full.tex` are correct. The CV uses three `benumerate` sections with reverse numbering:

- `benumerate{N1}` for Preprints (numbers N1 down to N2+1)
- `benumerate{N2}` for Journals (numbers N2 down to N3+1)
- `benumerate{N3}` for Conference/Workshop (numbers N3 down to 1)

The rule: **N1 = total papers**, **N2 = journals + conference/workshop**, **N3 = conference/workshop only**. When you add a paper to any section, increment the start numbers of that section and all sections above it.

Run `python scripts/check_cv_paper_count.py` to verify. If it reports a mismatch, fix the `benumerate` start numbers before compiling.
