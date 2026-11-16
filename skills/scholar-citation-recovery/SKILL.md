---
name: scholar-citation-recovery
description: Audit, and repair only where the owner has explicitly authorized it, the article records on a Google Scholar profile through the visible browser UI. The goal is that every version of a paper is either merged into the owner's main entry or kept separate by the owner's choice. Use for split citation counts, versions missing from the profile, wrong merges, and unmerge requests. Works for vision-based and accessibility-tree computer-use agents, with no scraping, API calls, or scripts.
---

# Scholar Citation Recovery

Reference: Google Scholar Profiles help, https://scholar.google.com/intl/en/scholar/citations.html

## Operating Rules

- Act only through the visible Scholar UI, as a signed-in person would. Do not scrape, call APIs, run scripts, or build URLs to step through pages. You may open a link that the page displays.
- Find each control by its role and its accessible name or visible label: Edit, Merge, Save, Cited by N, All N versions, and the + add button. Never use stored coordinates. If a label is missing or worded differently, match it by function only when the match is unambiguous. Otherwise stop and report.
- Observe the page after every action, through a screenshot or the accessibility tree, and confirm the expected change before taking the next action.
- Titles repeat. Scope every read and every click to one row, detail block, or dialog, identified by the available title, byline, source and component link. Zero-citation and single-version records may have neither link. Never act on the first matching text on the page.

## Modes

- Audit only is the default: read, classify, and report, with no changes.
- Follow the owner's requested scope. An instruction to merge confirmed versions covers adding a verified missing component and retaining the owner's existing primary record.
- The owner's keep-separate list overrides every other rule here. Pin each exception to its component link or full cluster id before editing. Ask which version the owner means if the description fits several. If a listed item is already merged, report it and unmerge it only when authorized.

## Procedure

1. Start at the requested row and work down the citation ranking within the requested scope. If the owner supplies a bibliography, use it to search for papers absent from the profile entirely. Keep a checkpoint that records the last finished and next titles with their year and identifying links.
2. Inspect the owner's entry. Open the article detail page and read its Scholar articles section, where indexed components may have Cited by or All versions links. From each link's destination, record the ids after `cites=` and `cluster=`. A merged entry can list several comma-separated ids after `cites=`. Use the displayed link destination or the browser's Copy link address when hover text is truncated. If an identifier is unavailable, keep the source evidence and flag unresolved identity. A cluster id identifies one indexed component across profiles. One paper may have several cluster ids. Profile item ids are different for each author and cannot be compared.
3. Open the same paper on one or more coauthor profiles and record the cluster ids of its components. Any cluster id that a coauthor has and the owner's entry lacks is a candidate.
4. Search on your own as well. Use + > Add articles and its individual article search; do not use Add article groups. Search by:
   - the exact title;
   - distinctive title fragments with an author surname;
   - the arXiv id or DOI;
   - fragments damaged by bad BibTeX imports, such as truncated titles, run-together words, missing accents, or the wrong first author.

   Use the search only to read results unless adding is authorized.
5. Compare each candidate with the primary source (the publisher page, arXiv abstract page, or PDF) on title, byline, and identifiers. Treat follow-up papers, software or dataset releases, extended journal versions, workshop versions, and theses as separate works unless the source establishes that both records describe the same publication. For a suspected wrong merge, apply the same comparison to the components already inside the owner's entry. Report the exact conflicting component and evidence. A paper by a namesake belongs outside the profile. Flag it for the owner rather than splitting it into an owner row.
6. Put each verified version into one class:
   - already merged: its cluster id is in the owner entry's set;
   - independently listed: it is a separate row on the owner's profile;
   - absent: the cluster is missing from both the main entry and the rest of the owner's profile. If you cannot locate it in Add articles, record it as found but unavailable to add. Do not create a manual entry to stand in for an indexed record.

   For each class, mark the owner's requested disposition, including keep separate. In audit mode, report verified candidates and proposed actions without submitting changes.

## Authorized Edits

- **Add.** Add each verified absent record once. Return to the profile, locate the added row and verify its component link or, where missing, the source identifier and byline against the candidate. After an error, a timeout, or a partial result, reload the profile and check whether the row already exists before retrying.
- **Merge.** In the profile list, select exactly two confirmed rows and choose Merge. In the dialog, select the owner's existing primary record. If the requested metadata and the available choices conflict, pause that pair before confirming. If the choices share a title, tell them apart by venue, year, and authors. Confirm with Save or Merge. Then reopen the surviving detail page and verify its metadata and the presence of the exact added cluster alongside the original clusters. The merged count is the union of unique citing papers, so overlapping citing papers can make the gain zero. A zero gain is not a failure.
- **Unmerge.** Open the article and choose Edit. Under Scholar articles, find the exact block by its component link or unambiguous source metadata and choose "Unmerge this article and add it to my profile as a separate entry", then Save. Verify that a separate row now exists and that the main entry no longer lists that component.
- Counts can take time to refresh. Record the value you observe and check again later. Do not repeat an action because a count has not changed yet.

## Example

In one audit, a diffusion survey component had 48 citations. Its indexed title ended in 2022, its source line said 2025, and its arXiv id matched the survey. The owner wanted this particular component listed separately. On the owner's request, the agent split out that exact component. Scholar displayed 48 on the separate row and 4,014 on the main entry, down from 4,048. The observed drop was 34.

## Pacing and Stops

- Work serially in small batches, for example 5 to 10 rows, and make one edit at a time.
- Stop immediately if any of these appear: an unusual traffic page, a captcha, a sign-in or verification challenge, or an unexpected dialog. Do not try to solve it. Hand control to a person and report the checkpoint.

## Report

After each batch, report:

- each action taken (add, merge, or unmerge), with its title and any available cluster ids;
- the observed counts before and after, and the observed change if both are available;
- which titles yielded no additional candidate, and which candidates remain ambiguous;
- each blocked item, with the reason; and
- the checkpoint: the last finished and next titles with their year and identifying links.

Leave out account details, personal information, and anything specific to the local environment.
