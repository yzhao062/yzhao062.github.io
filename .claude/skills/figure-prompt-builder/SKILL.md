---
name: figure-prompt-builder
description: Build copy-ready prompts for explanatory figures such as overviews, architectures, mechanisms, workflows, timelines, and conceptual illustrations from source text, figure ideas, reference figures, or rough drafts. Use when Codex needs to decide whether a section needs an explanatory figure, distill the figure's core message and required visual elements, select a small number of structural or style donors from a reference bank, draft a model-neutral prompt pack for image-generation models, adapt prompts to a requested tool, or recommend limited cleanup after external generation.
---

# Figure Prompt Builder

## Overview

Use this skill when the user wants help with nontrivial figures beyond a simple
placeholder.

This skill is not limited to NSF proposals. Treat the surrounding task context
as the constraint:

- proposals
- papers
- slides
- posters
- reports
- technical docs
- websites or demos when the figure is the main artifact

This skill is mainly for explanatory figures rather than publication result
plots. Its strongest cases are:

- system or project overviews
- workflow and task pipelines
- local mechanism or subsystem diagrams
- method composites and scientific schematics
- timelines or work plans
- conceptual illustrations or theory cues

This skill is for prompt-building workflow, not for high-level writing framing:

- adjacent writing skills can decide whether a section needs a figure
- `figure-prompt-builder` turns that need into a concise figure brief,
  downstream prompt pack, and limited follow-up guidance

Use it when the user asks for work such as:

- what figure should support this intro or thrust
- create a figure brief, caption, and downstream prompt pack
- generate a model-neutral prompt for Gemini, Claude, ChatGPT image tools,
  Sora, Midjourney, Flux, or another outside tool
- adapt one prompt to a specific downstream model
- compare prompt strategies for different rendering models
- decide whether an outside model output needs reprompting, light cleanup, or
  can be accepted as final

Read these references only as needed:

- figure archetypes and example anchors: `references/figure-archetypes.md`
- bundled portable reference bank with structure and style donors:
  `references/reference-bank.md`
- larger repo-level figure archive when available locally:
  `../../figure-references/index.md`
- format and tool choice: `references/tool-selection.md`
- outside-tool prompt packs and import flow: `references/external-handoff.md`
- cross-model prompt design for image generation: `references/prompt-design.md`

In a multi-project repo, use `<work-dir>` to mean the concrete workspace for
the figure task, such as one proposal folder, one paper folder, or one slide
deck directory.

Use `scripts/init_figure_spec.py` when the user wants a concrete local figure
brief scaffold before writing the final prompt pack.

## Workflow

### 1. Read Only The Figure Context You Need

Read the smallest set of files needed to understand the figure's job:

- the target source file for the section, slide, or page the figure supports
- neighboring text only when needed to understand scope or terminology
- existing figures only if the user wants a refresh rather than a fresh figure
- one to three references from `references/reference-bank.md` when the user
  wants grounding in an existing visual language
- use `../../figure-references/index.md` only as an extra local archive when it
  actually exists in the current repo

Do not read the whole repo just to draft one figure.

### 2. Decide Whether The Figure Is Worth Making

Add or refresh a figure only when it compresses logic better than prose.

Typical cases:

- intro or overview figure for the end-to-end project or system logic
- thrust or aim figure for a pipeline, mechanism, or layered method
- timeline or work plan figure for evaluation and coordination
- ecosystem or adoption figure for capability-building efforts
- evidence or impact figure when adoption or prior-system footprint matters

If the figure would only restate nearby sentences without clarifying structure,
say so and avoid unnecessary figure bloat.

### 3. Pick A Figure Archetype Before Writing The Prompt

Reduce the request to one archetype first:

1. `overview-architecture`
2. `local-mechanism-or-subsystem`
3. `workflow-or-method-pipeline`
4. `method-composite`
5. `concept-illustration`
6. `timeline-or-work-plan`

Then choose the downstream generation path using
`references/tool-selection.md`.

When helpful, also choose:

- one structural donor from `references/reference-bank.md`
- at most one or two style donors from the same bank

Do not average many references into one prompt.

### 4. Distill A Figure Brief Before Writing The Prompt

Before drafting the final prompt, distill a figure brief with:

- figure goal
- one-sentence reviewer takeaway
- target section and file
- required boxes, actors, or stages
- required arrows or dependencies
- suggested layout
- short in-figure text
- caption draft
- recommended downstream generation path
- recommended file or asset destinations

This brief is the local source of truth. The prompt pack is the primary
deliverable for downstream models.

Do not let the figure collapse into a plain box-only wireframe unless the user
explicitly asks for a minimal placeholder. When the figure is proposal-facing,
use a light visual language such as icon badges, grouped regions, or
restrained illustrative cues when those cues improve readability.

### 5. Choose The Downstream Generation Path Before Writing The Prompt

Do not over-prioritize format purity. First choose the prompt and tool path
most likely to yield a strong final figure within the user's time, tooling,
and revision constraints.

Common paths:

1. direct LLM generation as the final deliverable
2. LLM-generated first draft plus local cleanup
3. fully local diagramming or code-generated figure
4. hybrid pipeline with multiple tools

Direct model output is acceptable when:

- the user mainly wants a visually strong figure fast
- future edits are likely to be minor
- the model can already deliver good typography and composition for the task
- exact local editability is less important than final appearance

Prefer editable local sources when:

- many collaborators will revise the figure repeatedly
- labels or layout will change often with the text
- the figure encodes precise graph, chart, or workflow logic that benefits from
  deterministic updates

Once the path is clear, produce one copy-ready prompt pack for that path.

### 6. Format One Prompt The Model Can Actually Use

When the downstream path uses an outside image model, do not dump the entire
figure brief into the model. Produce:

1. a short local source-of-truth note for the repo
2. one model-neutral prompt meant to be copied into the outside tool

That prompt should be self-contained and visually directive, but not overloaded
with internal reasoning, review rubrics, or repo-specific workflow notes.

Use the cross-model guidance in `references/prompt-design.md`. The prompt
should usually contain these layers in this order:

- figure type and core message
- reviewer takeaway
- required layout and semantic elements
- required arrows or dependencies
- visual-quality layer
- output-quality layer

Prefer prompts that tell the rendering model:

- what kind of scientific figure this is
- what the central semantic blocks are
- how directionality should read
- how color should map to functional role
- what aesthetics to avoid

Do not ask the rendering model to optimize for the repo's internal workflow.
That part belongs in the local brief, not in the copied prompt.

Never ask an outside image model to produce code-based formats such as TikZ,
SVG, Graphviz, or Mermaid. These formats severely limit visual quality. When a
code-based source is needed, the agent should write it directly.

### 7. Support Third-Party Tools Without Depending On Them

When the user wants to use Gemini, Sora, Midjourney, Flux, or similar tools:

1. convert the figure brief into a clean prompt pack
2. tell the user whether the expected output is:
   - a reference draft
   - a near-final candidate
   - an acceptable final deliverable
3. if the returned asset should stay in the repo, place it under
   `<work-dir>/figure-src/reference/` or another agreed local folder
4. treat those assets as inspiration, a draft, or a final candidate depending
   on the task
5. if the first output is close but not right, reprompt with delta feedback
   before escalating to cleanup or rebuild
6. rebuild or clean up locally only when the figure quality or editability
   still falls short

When reprompting a close-but-not-right draft:

- explicitly keep the parts that already work
- describe only the deltas that must change
- change one to three dimensions at a time unless the concept is fundamentally
  wrong
- restart from the original brief when repeated delta prompts are drifting or
  contradicting each other

Useful delta instructions include:

- keep the current layered layout but enlarge all labels by 20%
- preserve the left-to-right flow and simplify the icon set
- keep the composition and color roles, but make the causal arrows explicit
- keep the overall structure and replace decorative art with cleaner schematics

Do not force a rebuild just because the output is raster or not locally
editable. Rebuild only when the figure still fails the user's actual quality or
maintenance needs.

### 8. Treat Editability As A Decision Variable, Not A Hard Rule

Editable local sources are sometimes helpful, but they are secondary here.
Recommend them only when they materially improve iteration or reuse.
Otherwise, optimize for a strong prompt and final figure quality.

Possible outputs include:

- direct image-model output
- Figma or PowerPoint source
- draw.io or SVG
- Graphviz or Mermaid source
- matplotlib or another plotting script
- TikZ when LaTeX-native generation helps
- hybrid source plus exported PDF or PNG

For complex figures, it is still acceptable to produce:

- a strong figure brief
- a prompt pack for outside generation
- a local cleanup plan
- a skeletal editable source when fully polished auto-generation is unrealistic

When drafting local skeletons or cleanup plans:

- avoid crude box farms unless structure is the only goal
- route arrows deliberately; avoid diagonals that create visual confusion
- prefer grouped regions, icon badges, and 1-2 accent shapes over decorative
  clutter
- keep in-figure text short enough that later style polishing remains easy

### 9. Write Outputs Into Stable Locations When The Workspace Has Them

Use these repo locations:

- `<work-dir>/figure-spec/` for figure briefs and prompt packs
- `<work-dir>/figure-src/` for editable local sources or intermediate assets
- `<work-dir>/figure/` for final exported assets
- `<work-dir>/figure-src/reference/` for external reference images or drafts

When the workspace does not already use these folders, create only the folders
that materially help organization. Do not force repo-specific directories onto
a task that only needs one prompt file or one final image.

When the user explicitly wants an outside-model prompt, save a dedicated prompt
file under `<work-dir>/figure-spec/` with a stable name such as
`<figure-name>-universal-prompt.md`. Keep the file easy to copy:

- short title
- optional one-line note
- one fenced `text` block containing the actual prompt

## Output Style

When using this skill, prefer one of these outcomes:

- a figure recommendation with rationale and no new file
- a figure brief and caption draft
- a figure brief plus a prompt pack for outside tools
- a prompt-only file meant to be pasted into an external image model
- a prompt pack plus generation-path recommendation and filenames
- a prompt pack plus follow-up guidance for improving an outside draft

Keep the output practical. The main value is reducing manual figure-design work
while making it easier to get to a strong downstream prompt and a strong final
figure.
