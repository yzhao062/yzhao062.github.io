# Figure Archetypes

Use this file to map a research or technical communication need to one of a
small number of reusable
figure patterns.

Representative anchors should come first from the bundled donor bank described
in `reference-bank.md`. That bundled bank keeps this skill portable across
bootstrapped repos.

If the current repo also has a larger local `figure-references/` archive, use
it only as an optional overflow source after checking the bundled bank.

## 1. Overview Architecture

Use when the introduction, opening slide, landing page, or summary section
needs a single visual summary of the whole project.

Typical content:

- problem setting or input context
- 3-4 major technical or capability layers
- outputs, testbeds, or broader impacts

Representative bundled donors:

- `../assets/reference-bank/system-overviews-and-architectures/overview-2.pdf`
- `../assets/reference-bank/system-overviews-and-architectures/intro-illustration.png`

## 2. Local Mechanism Or Subsystem

Use when one method unit, section, subsystem, or capability needs one picture
that clarifies the local mechanism.

Typical content:

- 2-4 subtasks or stages
- core data objects or signals
- one or two key transitions
- optionally one explicit output artifact

Representative bundled donors:

- `../assets/reference-bank/workflows-and-local-pipelines/task-2-1.pdf`
- `../assets/reference-bank/method-composites-and-schematics/immunostruct-schematic.png`

## 3. Workflow Or Method Pipeline

Use when the task needs a concrete process flow, algorithm pipeline, or
data-processing path.

Typical content:

- inputs
- transforms
- intermediate artifacts
- outputs or metrics

Representative bundled donors:

- `../assets/reference-bank/workflows-and-local-pipelines/development-process-final.pdf`
- `../assets/reference-bank/workflows-and-local-pipelines/task-2-1.pdf`

## 4. Method Composite

Use when the figure needs to combine mechanism, motivation, and linked
scientific modules into one coherent schematic.

Typical content:

- core method blocks
- one or two scientific concepts
- causal or informational dependencies
- optional supporting inset or evaluation cue

Representative bundled donors:

- `../assets/reference-bank/method-composites-and-schematics/dispersion-observation-distillation.png`
- `../assets/reference-bank/method-composites-and-schematics/immunostruct-schematic.png`

## 5. Concept Illustration

Use when the figure's main job is to give intuition, a geometric picture, or a
theory cue rather than a full pipeline.

Typical content:

- one abstract idea
- a minimal semantic legend
- spatial metaphor or topology cue
- low to medium text density

Representative bundled donors:

- `../assets/reference-bank/concept-motifs-and-illustrations/manifold.png`
- `../assets/reference-bank/concept-motifs-and-illustrations/idea.png`

## 6. Timeline Or Work Plan

Use for sequencing, milestones, rollout logic, and collaboration logic.

Typical content:

- years or semesters
- work packages or ownership
- deliverables
- evaluation milestones

Representative bundled donors:

- `../assets/reference-bank/timelines-and-workplans/gantt-chart.pdf`
- `../assets/reference-bank/timelines-and-workplans/timeline-extended-maine.pdf`

## Quick Heuristic

- if the whole project needs one memorable picture, choose
  `overview-architecture`
- if one subsystem or unit is still hard to explain, choose
  `local-mechanism-or-subsystem`
- if the logic is a process, choose `workflow-or-method-pipeline`
- if the task needs one schematic that combines multiple method layers, choose
  `method-composite`
- if the task needs intuition or a scientific cartoon, choose
  `concept-illustration`
- if the question is sequencing or milestones, choose `timeline-or-work-plan`
