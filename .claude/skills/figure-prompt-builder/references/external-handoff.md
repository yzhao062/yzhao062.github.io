# External Handoff

Use this file when the user wants to involve an outside tool such as Gemini,
Claude, ChatGPT image tools, Sora, Midjourney, Flux, or another image model to reduce manual drawing
work.

## Goal

Use outside tools for whichever role actually helps:

- ideation
- first draft generation
- near-final production
- final production

Do not assume an outside-model output must be rebuilt locally. Rebuild only
when the output still misses the quality, readability, or editability bar the
user actually needs.

## Cross-Model Prompt Strategy

When the user wants a prompt for an outside image model, the default deliverable
should be a single model-neutral prompt that can be pasted directly into the
tool. Keep it clean enough that the model can follow it without seeing the
entire local figure workflow.

Structure that prompt in this order:

1. figure type and scientific context
2. core message
3. reviewer takeaway
4. required layout
5. required semantic elements
6. required arrows or dependencies
7. visual-quality requirements
8. output-quality requirements

Do not include repo-only instructions such as:

- local folder names
- local brief details
- review rubrics
- file naming conventions
- notes to future collaborators

Do not ask the outside model to produce code-based output formats such as TikZ,
SVG, Graphviz, or Mermaid. These formats severely limit the visual richness that
image models can deliver. When the agent needs a code-based figure, it should
write the code itself rather than prompting an external model for it.

## Visual-Quality Layer

When the user wants the figure to look polished, the prompt should say some
version of the following:

- infer the correct figure type from the scientific context
- prioritize semantically central elements only
- make causal or structural directionality explicit
- use consistent visual encoding across the full figure
- assign color by functional role, not arbitrarily
- use a colorblind-friendly palette
- benchmark against high-end scientific schematics and polished research
  figures
- keep a white or soft off-white background
- keep the figure legible at the intended output size
- keep the layout clean enough for optional later cleanup

It is acceptable to use a soft prestige anchor such as
`Nature/Cell-family scientific schematics` if the user clearly wants that level
of polish, but translate that into general figure qualities rather than domain-
specific biological styling.

## Minimal Universal Prompt Template

```text
Create a publication-quality scientific figure.

Core message:
[one paragraph]

Reviewer takeaway:
[one short paragraph]

Figure archetype:
[overview architecture / thrust mechanism / workflow pipeline / timeline]

Required layout:
[left-to-right / layered / hub-and-spoke / stacked]

Required elements:
- ...
- ...

Required arrows or dependencies:
- ...

Visual quality requirements:
- infer the correct scientific figure type from the context
- prioritize only semantically central elements
- make causal directionality explicit
- use consistent visual encoding across the figure
- assign color by functional role with a colorblind-friendly palette
- benchmark against high-end scientific schematics and polished research figures
- use a white or soft off-white background
- keep the figure clean enough for optional later cleanup

Output quality requirements:
- large readable labels
- minimal decorative clutter
- avoid photorealism
- avoid dense tiny text
- keep the image clear at the intended final size
```

## Import Back Into This Repo Or Workspace

When the user gets a returned image or draft:

1. if it should stay in the repo, place it under
   `<work-dir>/figure-src/reference/` or another agreed local folder
2. compare it with the original figure brief
3. decide whether the output is:
   - inspiration only
   - a draft to clean up
   - already acceptable as final
4. if the draft is close but not right, reprompt with delta feedback before
   escalating to cleanup or rebuild
5. rebuild or clean up locally only if needed
6. place the final deliverable in `<work-dir>/figure/` or another agreed final
   asset location when the workspace uses one

## Iterative Reprompting

When the first generation is directionally correct but still wrong in detail:

- keep what already works explicitly
- describe the required deltas instead of rewriting the whole prompt
- change one to three things per round when possible
- if layout, semantics, and style are all wrong at once, restart from the
  original brief rather than stacking contradictory revision prompts

Good delta feedback looks like:

- keep the current hub-and-spoke layout, but enlarge labels and remove the
  background texture
- preserve the current color roles, but reduce decorative icons and clarify
  the directional arrows
- keep the overall composition, but replace the center artwork with a cleaner
  workflow schematic
- keep the top-level structure, but shorten all in-figure text to noun phrases

## Acceptable Uses Of Outside Outputs

- layout inspiration
- icon placement inspiration
- grouping and flow inspiration
- general color and spacing inspiration
- strong first draft
- acceptable final figure when the user is satisfied

## When To Escalate To Cleanup Or Rebuild

- tiny unreadable fixed text
- incorrect structure or missing semantic elements
- weak visual hierarchy
- artifacts that will obviously break under expected revisions
- output that looks like a generic dashboard, startup infographic, or marketing
  poster rather than a technical figure
