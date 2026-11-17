---
name: scholar-citation-recovery
description: Audit, and repair only where the owner has explicitly authorized it, the article records on any researcher's Google Scholar profile through the visible browser UI. The goal is that each verified version the audit finds is either merged into the owner's main entry or kept separate by the owner's choice. Use for split citation counts, versions missing from the profile, duplicate rows, wrong merges, and unmerge requests. Works for any computer-use agent, vision-based or accessibility-tree, with no scraping, API calls, or scripts. Besides authorized profile edits, its only side effect is a local checkpoint note, kept when the agent can write one.
---

# Scholar Citation Recovery

Reference: Google Scholar Profiles help, https://scholar.google.com/intl/en/scholar/citations.html

## Operating Rules

- Act only through the visible Scholar UI, as a signed-in person would. Do not scrape, call APIs, run scripts, or build URLs to step through pages. You may open a link that the page displays.
- Find each control by its role and its accessible name or visible label: Edit, Merge, Save, Cited by N, All N versions, and the + add button. Never use stored coordinates. If a label is missing or worded differently, match it by function only when the match is unambiguous. Otherwise stop and report.
- Observe the page after every action, through a screenshot or the accessibility tree, and confirm the expected change before taking the next action.
- Titles repeat. Scope every read and every click to one row, detail block, or dialog, identified by the available title, byline, source and component link. Zero-citation and single-version records may have neither link. Never act on the first matching text on the page.

## Modes

- Audit only is the default: read, classify, and report, with no changes to the Scholar profile.
- Follow the owner's requested scope. An instruction to merge confirmed versions covers adding a verified missing component and retaining the owner's existing primary record.
- The owner's keep-separate list overrides every other rule here. Pin each exception to its component link or full cluster id before editing. Ask which version the owner means if the description fits several. If a listed item is already merged, report it and unmerge it only when authorized.

## Procedure

1. Before starting, record the owner's name forms (initials, middle names, former names, transliterations), the keep-separate list, the requested scope, and the mode. Start at the requested row and work down the citation ranking within that scope. If the owner supplies a bibliography, use it to search for papers absent from the profile entirely.

   Keep one cumulative checkpoint for the whole audit and update it after each edit and each batch. Store it where it survives a timeout or restart, such as a note or file outside the conversation; if the agent cannot write one, end each batch report with the full checkpoint, and the latest copy replaces earlier ones. Record what was actually done and found: the owner and coauthor profile links used; for each title, the coauthor profiles compared or marked not compared, the queries searched, whether the duplicate check in step 5 ran, each component's ids, the verification evidence, and the disposition. Also record the items still unknown or ambiguous, and the last finished and next titles with their year and identifying links.
2. Inspect the owner's entry. Open the article detail page and read its Scholar articles section, where indexed components may have Cited by or All versions links. Two kinds of id appear, and only one can be compared. A profile-row id, typically the id in the address of a row's own detail page, belongs to one author's row and differs on every profile, so never use it to match records across profiles. A cluster id identifies one indexed component and is the same on every profile that holds it. Read it from each link's destination, after `cites=` or `cluster=`. A merged entry can list several comma-separated ids after `cites=`, and one paper may have several cluster ids. Use the displayed link destination or the browser's Copy link address when hover text is truncated. A component with no readable cluster id, which is common for zero-citation records and Add articles results, cannot be matched by cluster id. Match it in step 6 by primary-source metadata (title, byline, venue, year, and arXiv id or DOI), and flag its identity as unresolved only if that also leaves it open.
3. For each title, open it on the profile of at least one of its own coauthors who lists it, preferring coauthors from different collaborator groups, and record the cluster ids of its components. Any cluster id that a coauthor has and the owner's entry lacks is a candidate. No audit needs every coauthor's profile. If a useful coauthor turns up late, mark the finished titles they share as not compared with them; reopen such a title only when new evidence points to a missed component or the owner asks. If none of the paper's coauthors with a profile lists it, record that and rely on step 4.
4. Search on your own for each title in scope, even when the cluster sets match. The comparison in step 3 cannot surface a component that no inspected entry contains, which is common for records with a malformed title or author field. Use + > Add articles and its individual article search; do not use Add article groups. Choose queries that fit the title, such as:
   - the exact title;
   - a distinctive title fragment with an author surname;
   - the arXiv id or DOI;
   - a variant damaged by a bad BibTeX import, such as a truncated title, run-together words, missing accents, or the wrong first author.

   No fixed set of queries suits every title. Add queries when a title is generic, was renamed, or shows signs of a damaged import, and record the ones that ran. Use the search only to read results unless adding is authorized.
5. Check the owner's own rows for duplicates as well. Two rows already on the profile can be versions of one work, and a check for missing components passes over them. Once per audit, sort by the Title column, load the whole profile list using Show more as needed, and note adjacent rows with the same or nearly the same title, and any row whose Cited by count is crossed out, which Scholar shows when it treats the row as a duplicate. Then restore the citation sort and confirm that the full list is loaded, expanding it again as needed after sorting or reloading. For each title in scope, also look on the loaded list, for example with the browser's find-in-page, for rows that share a distinctive title fragment or an arXiv id shown in the source line. Open detail pages only for hits.
6. Compare each candidate and each suspected duplicate row with the primary source (the publisher page, arXiv abstract page, or PDF) on title, byline, and identifiers.
   - Treat follow-up papers, software or dataset releases, extended journal versions, workshop versions, and theses as separate works unless the source establishes that both records describe the same publication, or the owner confirms it. A record for a dataset or software landing page does not become a version of the paper because it shares the title or collects the paper's citations.
   - A matching name does not by itself make the owner an author, because an initial and surname, or a common full name, can belong to several people. Before attributing a record to the owner, expand any initial against the primary-source byline and the owner's name forms, and check that at least one other signal agrees: an identifier or title shared with the owner's paper, a known coauthor, the affiliation, an ORCID or email, or the owner's bibliography. Leave the record unknown if none does. A paper by a namesake belongs outside the profile. Flag it for the owner rather than splitting it into an owner row.
   - Versions of one work need not carry identical author lists, and a Scholar title or author field may be truncated or damaged. Accept such a record as a version when other strong evidence agrees, such as a matching arXiv id or DOI, and the paper at that identifier is the same publication as the record rather than an extended or follow-up paper that replaced it in a later revision.
   - Records with conflicting identifiers of the same kind, such as two arXiv ids, two other preprint ids, or two publisher DOIs, stay separate until a primary source states that both describe the same publication, or the owner explicitly confirms that they are one work. A preprint id paired with a publisher DOI is not such a conflict. Overlapping content, or a statement that one extends the other, does not establish identity. An owner's confirmation settles identity; editing still needs the requested scope.
   - For a suspected wrong merge, apply the same checks to the components already inside the owner's entry. Report the exact conflicting component and evidence.
7. Put each verified version into one class:
   - already merged: its cluster id is in the owner entry's set or, for a component without one, the entry lists a component whose primary-source metadata matches it;
   - independently listed: it is a separate row on the owner's profile. When merging is authorized, merge confirmed duplicates unless the owner excepted them;
   - absent: it is missing from both the main entry and the rest of the owner's profile. Do not infer absence from a profile list that has not finished loading, or from the lack of an In profile mark in Add articles alone; confirm it on the fully loaded list and in the main entry's components. If you cannot locate it in Add articles, record it as found but unavailable to add. Do not create a manual entry to stand in for an indexed record.

   For each class, mark the owner's requested disposition, including keep separate. Leave a candidate whose identity is still open as unknown rather than forcing it into a class. In audit mode, report verified candidates and proposed actions without submitting changes.

## Authorized Edits

- **Add.** Add each verified absent record once. Return to the profile, locate the added row and verify its component link or, where missing, the source identifier and byline against the candidate. After an error, a timeout, or a partial result, reload the profile and check whether the row already exists before retrying. When merging is also authorized and the profile has a main entry for that work, merge the added row into it unless the owner kept it separate.
- **Merge.** In the profile list, select exactly two confirmed rows and choose Merge. In the dialog, select the owner's existing primary record. When both rows were already on the profile and the owner named neither, select the citation for the final published version and report the choice; if neither row is clearly that version, pause the pair. If the requested metadata and the available choices conflict, pause that pair before confirming. If the choices share a title, tell them apart by venue, year, and authors. Confirm with Save or Merge. Then reopen the surviving detail page and verify its metadata and the presence of the exact merged-in component, by cluster id or else by source metadata, alongside the original components. The merged count is the union of unique citing papers, so overlapping citing papers can make the gain zero. A zero gain is not a failure.
- **Unmerge.** Open the article and choose Edit. Under Scholar articles, find the exact block by its component link or unambiguous source metadata and choose "Unmerge this article and add it to my profile as a separate entry", then Save. Verify that a separate row now exists and that the main entry no longer lists that component.
- Counts can take time to refresh. Record the value you observe and check again later. Do not repeat an action because a count has not changed yet.

## Examples

These optional illustrations come from past audits of one profile; the rules above govern.

- A diffusion survey component had 48 citations. Its indexed title ended in 2022, its source line said 2025, and its arXiv id matched the survey. The owner asked to list that exact component separately, and the agent split it out. Scholar displayed 48 on the new row and 4,014 on the main entry, down from 4,048, an observed drop of 34.
- GLIP-OOD appeared as two owner rows, with 15 and 6 citations, that carried the same arXiv id, 2504.21186. After a title and author check against arXiv, the authorized merge showed 21 observed citations. A check for missing components alone would have passed over this pair.
- The owner confirmed that arXiv 2411.03321 and 2412.15291, two election preprints with different ids, are versions of one work. That confirmation settled identity; editing still followed the requested scope.
- On a coauthor's profile, "Y Zhao" may be Yuying Zhao rather than the owner, Yue Zhao, which is why initials are expanded against the byline.

## Pacing and Stops

- Work serially in small batches, for example 5 to 10 rows, and make one edit at a time.
- Pause between searches and between batches. Searches are the most likely trigger for an unusual traffic page, so spread a large profile across sessions.
- Keep each call short enough to finish within the tool's timeout. After a timeout or crash, read the checkpoint and re-observe the profile before retrying any add, merge, or unmerge.
- Stop immediately if any of these appear: an unusual traffic page, a captcha, a sign-in or verification challenge, or an unexpected dialog. Do not try to solve it. Hand control to a person and report the checkpoint.

## Report

After each batch, report what that batch did and found, without repeating earlier batches:

- each action taken (add, merge, or unmerge), with its title and any available cluster ids;
- the observed counts before and after, and the observed change if both are available;
- for each title, the coauthor profiles compared, the queries searched, whether the duplicate check ran, and what they found. A title with no new candidate means only that those checks found none;
- proposed actions in audit mode, and flags: namesake rows, suspected wrong merges with their evidence, and the owner's separate works found during search but missing from the profile;
- the candidates that remain unknown or ambiguous, and each blocked item, with the reason; and
- the last finished and next titles, with their year and identifying links.

When the checkpoint falls back to the report (step 1), the full checkpoint replaces the per-title and unknown items above. Leave out account details, personal information, and anything specific to the local environment.
