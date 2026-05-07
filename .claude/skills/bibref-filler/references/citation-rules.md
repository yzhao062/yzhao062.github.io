# Citation Rules

Use this reference only when you need placement guidance, a clear density rule,
or storage conventions for machine-added bibliography entries.

## Density Modes

- `sparse`: cite only the highest-value non-obvious claims, the most relevant
  prior outputs, and one or two essential external anchors per local topic
- `moderate`: support each major paragraph or technical move with one exact
  citation cluster when strong evidence exists
- `heavy`: use only for related-work-heavy sections or when the user explicitly
  asks for dense grounding; do not add approximate or weakly related citations

If the user does not specify a mode, default to `sparse`.

## Source Priority

Use evidence in this order:

1. cite keys already present in active local `.bib` files near the task
2. cite keys already used in neighboring active source files
3. externally verified papers from canonical sources when exact support is
   missing locally
4. exact matches already present in shared or template `.bib` files, but only
   after confirming they are the exact intended paper
5. exact matches from archived or example `.bib` files, again only after exact
   confirmation

For the author's own work, the default expectation is that needed entries
already exist locally. If they do not, do not improvise.

This priority order is for exact entry reuse, not for deciding whether a
self-citation is the right rhetorical support. For broad framing claims,
external literature usually outranks the author's own papers.

The main use case of this skill is safe external addition. Local `.bib` files
are checked first to avoid duplication and catch already-available exact keys,
not because local reuse is the main product.

## Storage Rules

- Keep existing human-maintained bibliography files as they are.
- Put new machine-added entries into a dedicated working bibliography in the
  same directory as the active main bib files; `working.bib` is the default
  name.
- If no machine-managed bibliography exists, create one next to the active bibs
  or stop and ask when the repo has a stricter convention.
- Never mix machine-added entries into the curated main bib files.
- Do not duplicate an entry into the working bibliography if the exact cite key
  already exists in a curated local bib file.
- If a machine-added entry needs later human cleanup, leave it in the working
  bibliography until a human explicitly consolidates it.

## Existence Guardrail

- A citation may be inserted only after its entry exists in either a curated
  local bib file or the dedicated working bib.
- If canonical metadata cannot be confirmed, do not create the entry and do not
  cite the paper.
- "Probably the right paper" is a failure case, not a usable citation.
- Full text is not required to establish existence. Exact metadata from a
  canonical source is sufficient.
- If only metadata is available, stay conservative about claim support. Use the
  title, abstract, venue context, and canonical summary page when available;
  otherwise leave a visible unresolved note.

## Placement By Rhetorical Function

### Summary, Abstract, Or Executive Overview

- Keep citations minimal unless the user explicitly asks for more.
- Cite only when a sentence makes a non-obvious technical, empirical, or
  community claim that will look unsupported without a source.
- Avoid turning the summary into a literature review.

### Intro Or Problem Framing

- Cite the problem landscape, prior infrastructure, scientific setting, or
  gap-defining prior work.
- Prefer a small number of representative citations over long laundry lists.
- Default to external surveys, standards, community infrastructure papers, or
  representative prior work as the main anchors.
- Do not make the author's own papers the primary support for broad field,
  community, or infrastructure claims.
- Use the author's own papers here only when the sentence explicitly references
  a prior system, dataset, or method that the current work directly builds on.

### Prior Capability Or Track Record

- Cite the author's own papers, systems, software, or datasets when the prose
  claims prior capability or concrete track record.
- Do not over-cite biography-like facts unless the section uses publication
  evidence to prove fit.
- If a specific prior output is mentioned by name, use the exact local entry or
  leave a visible unresolved note.

### Method, Aim, Or Technical Body

- Cite directly adjacent methods, data models, workflows, or prior community
  systems.
- Use citations to sharpen the gap, not to inflate the paragraph.
- When the section names a component that builds on the author's own prior
  work, prefer those local citations first.
- In motivation, background, or overview paragraphs inside a technical section,
  start with external anchors for the field-wide problem and then add
  self-citations only when they document a concrete technical foundation
  carried into the current work.

### Evaluation, Reproducibility, Translation, Or Infrastructure

- Cite benchmarks, standards, reproducibility practices, shared platforms, or
  community workflows only when they are directly relevant to the promised
  measures or artifacts.
- Avoid vague "best practice" citations that do not materially support the
  metric or release plan.

### Related Work Or Background

- Use denser citation coverage only when the section is actually performing a
  literature function.
- Prefer representative, exact support over exhaustive name-dropping.
- Group citations by the claim they support, not by convenience.

## External Verification Rules

When an exact local entry is missing and the user allows external additions:

- prefer DOI or publisher pages, official arXiv pages, DBLP, OpenReview, ACL
  Anthology, IEEE, ACM, Springer, Nature, or equivalent canonical sources
- verify title, author list, venue, year, and DOI or canonical URL
- add the entry to the active working bibliography before using the cite key
- if the current agent cannot actually access reliable external search or
  lookup tools, do not pretend to verify; leave a visible unresolved note
- a successful lookup means the agent can return exact metadata from a
  canonical source, not just say that it "seems online"

Leave a visible unresolved note instead of adding a citation when:

- preprint and published versions disagree and you cannot confirm the intended
  version
- multiple papers fit the description but the sentence does not disambiguate
- the exact local cite key for the author's own work cannot be located
- the candidate source supports only the general topic, not the specific claim

## What Not To Do

- Do not invent cite keys.
- Do not guess titles, authors, venues, years, or DOIs.
- Do not cite a paper just because it is nearby in topic.
- Do not copy a key from templates or examples without confirming that the
  entry is the exact intended paper.
- Do not add dense citation clusters just to make a paragraph look scholarly.
