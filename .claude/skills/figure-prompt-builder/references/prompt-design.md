# Prompt Design

Use this file when the user wants a model-neutral prompt that can be pasted
into an outside image model.

## Principle

The copied prompt should control the image model's visual output, not explain
the repo's internal workflow.

Keep internal planning separate from the pasted prompt.

## Format Restriction For External Prompts

Never ask an outside image model to produce code-based output formats such as
TikZ, SVG, Graphviz, or Mermaid. These formats drastically limit the visual
quality and richness the model can deliver. External image models should always
produce raster or rendered visual output. When a code-based editable source is
needed, the agent should write it directly rather than prompting an external
model for it.

## What A Good Cross-Model Prompt Should Do

A strong prompt for a research or technical figure should:

- identify the correct figure archetype from the scientific context
- state the core message and reviewer takeaway
- specify the main semantic regions and required directionality
- describe color as functional-role logic
- constrain the aesthetic family
- state readability and output constraints

## Recommended Prompt Layers

Write prompts in this order:

1. `figure type`
2. `core message`
3. `reviewer takeaway`
4. `layout`
5. `required elements`
6. `required arrows or dependencies`
7. `visual quality requirements`
8. `output quality requirements`

## Visual Requirements To Reuse

These are strong default requirements for polished scientific figures:

- publication-quality scientific figure
- infer the correct figure type from the scientific context
- prioritize semantically central elements only
- avoid unsupported or speculative decorative elements
- make causal or structural directionality explicit
- use consistent visual encoding across the full figure
- assign color by functional role, not arbitrarily
- use a colorblind-friendly palette
- benchmark against high-end scientific schematics and polished research
  figures
- use a white or soft off-white background
- preserve clean professional typography and clear spatial organization
- keep the composition clean enough for optional later editing

## Output Requirements To Reuse

- readable at the intended final display size
- large readable labels
- no tiny dense paragraph text
- minimal decorative clutter
- no glossy 3D effects
- no marketing infographic tone
- no dashboard styling
- no startup pitch-deck aesthetics
- no cartoonish icons or robot imagery unless explicitly required

## Text Density Rule

Outside image models are weak at dense typography. Default to:

- short block titles
- at most one short supporting line per major block
- concise labels instead of paragraph text

If the user prioritizes beauty over exact wording, tell the model to preserve
clean label regions that can be refined later if needed.

## Prestige Anchors

If the user wants very polished output, it is acceptable to say:

- benchmark against high-end scientific schematics
- benchmark against polished research overview figures
- benchmark against Nature/Cell-family figure clarity

Translate those anchors into visual properties:

- clarity
- hierarchy
- color discipline
- white background
- crisp modular composition

Do not let the prompt drift into biology-specific conventions unless the figure
itself is biological.
