---
name: bibref-filler
description: Add new external bibliography citations in existing prose without inventing support. Use when Codex needs to find real papers from canonical sources, verify exact metadata before citation, add machine-generated entries into a separate working bibliography next to the active main bib files, avoid polluting curated bibs, and leave visible TODOs instead of guessing. Useful for proposals, papers, slides, rebuttals, and other technical writing where the prose mostly exists and the main task is safe external citation support.
---

# Bibref Filler

## Overview

Use this skill when the prose mostly exists and the job is to add new external
citations, tighten weak support, or audit citation integrity without rewriting
the argument.

This skill works best in repos that use local `.bib` files and cite-key based
markup such as LaTeX. When the writing format is different, keep the same
evidence discipline but adapt the mechanics instead of forcing BibTeX-specific
steps.

This skill is for safe external citation filling, not for full section
rewrites:

- keep the section's argument intact
- add citations only where they materially support a claim
- default to conservative coverage unless the user asks for denser support

This skill has two non-negotiable rules:

- never insert a citation to a paper unless the paper is real and the entry is
  already present in a local `.bib` file or has just been verified from a
  canonical source
- put every machine-added bibliography entry into a separate working bib placed
  next to the active main bib files; do not mix machine-added entries into the
  curated main bib files

For this skill, proving that a paper exists does not require full-text access.
Accurate canonical metadata is enough: title, author list, venue, year, and a
stable identifier or canonical landing page.

The main value of this skill is adding new external support safely. Reusing an
already-correct local cite key is fine, but that is a secondary convenience,
not the main reason to invoke this skill.

For broad framing claims, do not let the author's own papers become the main
support when better external anchors exist. Use self-citations mainly for prior
capability, concrete artifacts, or direct technical foundations.

Read [references/citation-rules.md](references/citation-rules.md) only when
you need placement patterns, density guidance, or storage conventions.

If the repo does not already have a dedicated working bib, copy
`assets/working.bib` next to the active main bib files and use it for all
machine-added entries.

Use this helper when the repo uses local `.bib` files and cite-key based source
files:

- cite-key validation after patching:
  `scripts/check_cite_keys.py`

## Workflow

### 1. Confirm External Lookup Capability And Scope

Before doing anything else, confirm whether the current agent can actually look
up external papers from canonical sources.

- If the environment has real web or literature lookup capability, continue.
- If the environment does not have reliable external lookup capability, do not
  fabricate new citations. Switch to audit-only or TODO-only mode and say so.

Use a concrete self-check rather than a vague claim about connectivity. The
agent should be able to resolve at least one canonical source and extract exact
metadata from it:

- title
- author list
- year
- venue or publisher when available
- DOI, arXiv id, DBLP record, OpenReview URL, or another canonical identifier

If the agent cannot do that reliably in the current environment, it does not
have the capability this skill needs for external additions.

Then identify:

- the target file or file set
- whether the user wants `sparse`, `moderate`, or `heavy` citation density
- whether the user allows externally verified additions or wants local-only
  citations
- which local `.bib` files are the active curated bibs for this task
- which working bib will hold machine-added entries; default to `working.bib`
  in the same directory as the active curated bibs

If the user does not specify density, default to `sparse`: fill only the
claims that most obviously need support.

If there are multiple plausible active bib directories, stop and ask instead of
guessing where the working bib should live.

### 2. Gather Only The Inputs Needed

Read the smallest useful set of files:

- the target source file or files
- neighboring sections only when needed for citation style, cite-key reuse, or
  local rhetorical context
- active bibliography files near the target files
- the dedicated working bib next to those active bibliography files
- shared or template bibliography files only when the active bib lacks a known
  exact entry

Do not scan the entire repo unless the user asks for a broad pass.

### 3. Check Local Bibliography To Avoid Duplicates

Before adding anything external, check whether the exact paper is already
present locally. Use local evidence in this order:

1. workspace-local `.bib` files adjacent to the task
2. cite keys already used in nearby active files
3. shared or template `.bib` files in the repo
4. archived or example `.bib` files in the repo

For the author's own work, prefer exact local cite keys when they exist. If
the prose names a paper, system, or dataset and no exact local entry is
available, do not invent a key. Leave a visible TODO or stop and ask for the
missing entry.

Do not move or rewrite human-maintained entries just to normalize them. Keep
existing curated bibliography files intact and add new machine-verified entries
only to a dedicated working bibliography. If the repo does not already have
one, create `working.bib` next to the active curated bibs unless the repo has a
stricter convention. Prefer copying `assets/working.bib` as the initializer.

This local-first rule is about exact-key reuse, not about preferring
self-citations. If a paragraph makes a field-wide or community-wide claim and
the local matches are mostly the author's own papers, treat that as
insufficient support and look for externally verified anchors instead.

### 4. Search External Canonical Sources For Missing Support

When exact support is not already local and the environment can do external
lookup, search for a real paper using canonical sources.

- prefer DOI or publisher pages, official arXiv pages, DBLP, OpenReview, ACL
  Anthology, IEEE, ACM, Springer, Nature, or an equivalent venue source
- use local examples or template bibs only as candidate hints, not as proof
- stop if you cannot establish that the paper is real and exactly identified

The goal is not to find "something on the same topic." The goal is to find the
exact paper that supports the sentence.

### 5. Verify Every Candidate Before Inserting It

Insert a cite key only if all of these are true:

- the key already exists in a local `.bib`, or you have just added it to the
  dedicated working bib from an exact verified source
- the title and authors match the claim you are supporting
- the venue and year are not materially ambiguous
- the paper is a conservative fit for the sentence, using metadata and abstract
  information when available; do not overclaim support that you cannot justify

Do not use "close enough" matches. A nearby topic match is not enough.
Full text is not required for existence verification, but exact metadata is.
If support is still unclear after inspecting the available metadata, abstract,
or canonical summary page, leave a visible TODO instead of pretending certainty.

### 6. Add New External Entries To The Working Bib

When a new paper passes verification:

- add the BibTeX entry to the dedicated working bib before citing it in prose
- never write a machine-added entry into the curated main bib files
- keep the working bib next to the active curated bibs so the user can inspect
  new additions separately
- record only metadata you actually verified from a canonical source

If any key metadata remains uncertain, do not add the entry. Leave a visible
TODO instead.

### 7. Place Citations Conservatively

Follow [references/citation-rules.md](references/citation-rules.md) when you
need placement guidance.

Default rules:

- cite non-obvious technical or empirical claims
- cite concrete prior outputs when claiming prior capability
- prefer one strong citation cluster over many weak ones
- avoid turning every sentence into a citation dump
- keep executive-summary style sections especially sparse unless the user
  explicitly wants more
- for broad framing, motivation, or overview paragraphs, prefer externally
  verified anchors over self-citation-heavy clusters

### 8. Validate Cite Keys After Patching

After editing:

- run `scripts/check_cite_keys.py` on the touched source files when the repo
  uses local `.bib` files and cite-key based markup
- fix any unresolved keys before finishing
- if the edit added new external entries, confirm they were added to the
  dedicated working bib rather than mixed into curated files
- confirm the working bib sits next to the active main bib files so the user
  can inspect machine-added entries separately

If the document is compile-sensitive or the user asks for it, also recompile
the relevant target.

### 9. Leave Visible TODOs For Anything Uncertain

Use visible unresolved notes for:

- missing exact cite keys
- external papers whose metadata is not yet confirmed
- claims that need a source but have only a vague candidate
- places where the user requested higher citation density but the available
  evidence is not strong enough

Never hide uncertainty in comments and never silently insert fabricated
bibrefs.

## Output Style

When using this skill, prefer one of these outcomes:

- a patch that adds verified citations plus new entries in the dedicated
  working bib only
- a patch plus one or two visible unresolved notes where accuracy blocked
  insertion
- a citation audit summary before patching when the user asks for planning
  first
