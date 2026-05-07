# Tool Selection

Use this file after the figure archetype is clear.

## Default Rule

Choose the path most likely to yield the best final figure under the user's
time, revision, and collaboration constraints.

Do not optimize for a specific file format by default. Optimize for:

- visual quality
- clarity
- speed to a strong result
- fit to the target medium
- enough editability for the actual revision pattern

## Common Paths

### Direct LLM Generation

Best for:

- polished conceptual overviews
- visually rich schematics
- situations where speed and appearance matter more than long-term editability
- first drafts that may already be good enough as finals

Good choices include image tools from OpenAI, Gemini, Claude, Midjourney,
Flux, Sora, and similar systems.

Use when:

- the model can plausibly handle the figure's visual complexity
- the user is comfortable with prompt-driven iteration
- the figure does not require strict deterministic layout control

### Hybrid LLM Draft Plus Cleanup

Best for:

- high-polish figures with some exact text or layout constraints
- cases where the model is strong on composition but weak on final labeling
- workflows where a fast strong draft is more valuable than building from
  scratch

Cleanup tools can include Figma, PowerPoint, Illustrator, draw.io, or any
other editor the user already uses.

### Figma / PowerPoint / Illustrator / draw.io

Best for:

- collaborator-facing diagrams
- architecture and ecosystem figures
- layered boxes, arrows, actors, and swimlanes
- cases where medium-term editability matters

Useful styling guidance in these tools:

- use grouped background regions rather than only isolated boxes
- use small icon badges or pictograms when they clarify semantics
- route arrows orthogonally or with smooth deliberate curves
- avoid the look of a raw slide wireframe unless the user asked for a
  placeholder

### Graphviz / Mermaid

Best for:

- typed graphs
- dependency diagrams
- asset-linking or relation-heavy figures
- cases where automatic layout matters more than bespoke visual polish

Why:

- good for automatic layout
- easier than hand-placing complex graphs

Avoid for:

- polished ecosystem art with many custom visual groupings

### matplotlib Or Other Plotting Code

Best for:

- charts
- simple timelines
- benchmark or evidence plots

Why:

- deterministic
- easy PDF output
- good for data-backed visuals

### TikZ

Best for:

- LaTeX-native diagrams or timelines
- relatively regular technical diagrams
- cases where reproducible, code-side updates matter more than easy GUI editing

Use cautiously:

- avoid for highly detailed artistic diagrams
- avoid when many collaborators need quick manual edits

### SVG / PDF / PNG / Other Export Formats

These are output containers, not primary workflow decisions.

- vector export is useful when later editing or crisp scaling matters
- raster export is acceptable when the figure already looks right and the user
  does not need heavy downstream editing
- do not force a vector rebuild just because vector sounds cleaner in theory

## Quick Decision Guide

- user wants the fastest path to a beautiful figure:
  start with direct LLM generation
- model can generate most of the composition, but exact wording will change:
  choose hybrid draft plus cleanup
- many collaborators will repeatedly tweak labels and arrows:
  choose Figma, PowerPoint, Illustrator, or draw.io
- graph structure matters most:
  choose Graphviz or Mermaid
- chart or timeline is data-driven:
  choose matplotlib or another plotting library
- LaTeX-native and moderately structured:
  choose TikZ
