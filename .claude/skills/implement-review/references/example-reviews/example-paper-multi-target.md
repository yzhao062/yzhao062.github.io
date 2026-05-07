<!-- Round 4 -->

# Review

Verification notes: I read the staged files, compiled `arxiv-main.tex` (it builds to 4 pages), spot-compiled `main.tex`, and checked the cited primary papers for AutoGluon, PyOD 2, and AD-Agent to verify the taxonomy. I did not treat the intentional `\todo{}` placeholders or the two red figure-placeholder blocks as findings. Per-target history: the long-paper deep rewrite is on round 4; the arxiv short version is on round 1.

File/diff scope: staged changes covering `FIGURES.md`, `arxiv-main.tex`, `build-arxiv.sh`, `build-arxiv.bat`, and the long-paper section files `sections/{intro,background,architecture,adengine,deployment,discussion,related-work,conclusion}.tex`.

Review lens: `paper/content` -- soundness, novelty, significance, clarity, related-work positioning.

Overall assessment: the deep rewrite mostly works. The four-shift vocabulary now ties together the introduction, novelty delta, ADEngine section, discussion, and related work much more tightly than in earlier rounds. The remaining problems are concentrated in three places: the shift taxonomy is still not fully fair to prior systems, the Discussion section presents internal design/usage observations as if they were evidence, and both versions reintroduce conclusion-level scope claims that outrun the support on the page.

## (A) New findings on the long version's deep rewrite

### 1. High -- The related-work taxonomy still overstates AutoGluon's similarity to the proposed pattern, and AD-AGENT is still described inaccurately (`sections/related-work.tex:23,37-41`, `sections/background.tex:21-23`).

Under the paper's own definition, Shift 2 is not generic automation; it is expertise made available as auditable routing evidence, specifically benchmark-backed rules. AutoGluon's paper presents a one-line `fit()` API with internal preprocessing, validation, model fitting, and stacking, plus a predefined model order and adaptive ensembling, not benchmark-backed routing or an exposed workflow state (AutoGluon-Tabular, arXiv:2003.06505, esp. Sections 2.1-2.3). Giving it a checkmark on S2 and a tilde on S1 makes the table look like a family-resemblance chart rather than a principled rubric. By contrast, the current tilde for PyOD 2 on S2 still looks fair: PyOD 2 does automate model choice, but through symbolic metadata plus LLM reasoning rather than benchmark-backed routing (PyOD 2, arXiv:2412.12154 Section 2.2).

Separately, the background delta table still calls AD-AGENT a "fixed 4-agent pipeline," but the cited paper describes Processor, Selector, Info Miner, Generator, Reviewer, Evaluator, and Optimizer agents with optional feedback loops (AD-Agent, arXiv:2505.12594 Sections 2.1-2.2). The partial-S1 classification is defensible; the "4-agent" wording is not.

Suggested row rewrite for `tab:related-shifts`:

```tex
\textsc{AutoGluon}~\cite{erickson2020autogluon} & $\times$ & $\sim$ & $\sim$ & $\times$ \\
```

Suggested text rewrite for the AutoGluon paragraph:

```tex
\textsc{AutoGluon}~\cite{erickson2020autogluon} is the KDD ADS precedent \pyodthree\ follows structurally: a widely deployed open-source library that operationalizes expert supervised-learning practice behind a simple \texttt{fit()} interface. We therefore treat it as a structural analogue rather than as a partial workflow substrate under our four-shift definition.
```

Suggested wording fix for the AD-AGENT row in `tab:method-deltas`:

```tex
Model selection & LLM-powered, single model & LLM-driven, multi-agent pipeline with optional feedback loops & Benchmark-backed top-$k$ consensus \\
```

### 2. Medium -- Section 6 turns undocumented design history and usage impressions into paper-level evidence (`sections/discussion.tex:6-13`).

The discussion is at its best when it extracts design lessons from the artifact. It weakens when it states unevidenced facts about the artifact's history or usage, for example "the six-phase session state machine ... is the third iteration of the design," "the one-shot convenience method dominates in practice," and "users in early testing also reached for the natural-language path." None of these observations is supported elsewhere in the paper, and the section does not mark them as anecdotal author experience. That is exactly the kind of sentence a reviewer will push on because it sounds empirical while carrying no method behind it.

Suggested replacement for the first three discussion paragraphs:

```tex
\paragraph{Choosing the phase granularity mattered.}
Designing Shift~1 was mainly a question of phase granularity. Too fine, and the agent drowns in transitions and the one-shot path becomes awkward; too coarse, and iteration loses the handles it needs. The design lesson is that exposing a state machine is not enough; the state partition has to match how the workflow is revisited.
```

### 3. Medium -- The new framing reintroduces broad scope claims that the paper cannot currently defend (`sections/intro.tex:27`, `sections/related-work.tex:44`, `sections/conclusion.tex:15-16`).

The strongest remaining overclaiming is no longer about OD quality; it is about scope. Three sentences are doing too much work:

- `sections/intro.tex:27` moves from a real installed base to "already how a significant fraction of the world's AD code will meet the agentic era."
- `sections/related-work.tex:44` claims "the first open-source Python scientific library in any domain" to name and implement the pattern.
- `sections/conclusion.tex:15-16` says the conditions that make the pattern work "hold" for causal inference, drug target identification, and financial factor research.

Each sentence is plausible as ambition, but none is supported as a result of the present paper.

Suggested rewrite for the introduction sentence:

```tex
\pyodthree\ is the first anomaly-detection library built as a workflow substrate, implementing all four shifts in \adengine, its Layer-2 Python API (\S\ref{sec:adengine}). It ships as the third generation of a widely deployed Python AD library, with 39M+ PyPI downloads and documented production deployments, so the substrate is presented in a library with genuine production reach rather than in a demonstration artifact.
```

Suggested rewrite for the beyond-OD future-directions paragraph:

```tex
\textit{(i) Beyond anomaly detection.}
The workflow-substrate pattern may extend to domains such as causal inference, drug target identification, and financial factor research, where expert workflows and evaluation ecosystems already exist, but that is a hypothesis rather than a result of the present paper.
```

## (B) Previously raised items from Rounds 1-3

- `R1 #1: intro stiffness` -- Fixed. The stakes-first opener survives the rewrite.
- `R1 #5: residual overclaims in intro/deployment/conclusion` -- Reopened. The earlier overclaim wording stayed fixed, but the deep rewrite introduces fresh scope claims. See A3.
- `R2 #1: image modality overclaim` -- Fixed. Long table and closing sentence still state image inputs share the interface without a dedicated routing benchmark.
- `R3 #1: AD-LLM mischaracterization` -- Fixed. Related-work now treats AD-LLM as a benchmark study rather than as a workflow system.

## (C) New findings on the arxiv short version

Stand-alone assessment: the short version is close to a citable preprint. The build lands at 4 pages, the cardiotocography walkthrough still keeps the essential Turn-4 disagreement check, and `tab:related-shifts-arxiv` does not drift from the long table. The remaining issues are about claim calibration, not narrative completeness.

### 1. High -- The short version still states the empirical thesis as achieved while explicitly deferring the validating evidence (`arxiv-main.tex:100-102`).

The preprint does a good job telling the reader that oracle comparisons, the PyOD 2 pairing, calibration, overhead, and case studies are deferred. But the sentence immediately before that still says `\pyodthree` "gives agents enough structure to run competent anomaly detection workflows with less OD expertise." In the 4-page version, that sentence reads as the earned result, not as the design target.

Suggested rewrite:

```tex
The claim is narrower than expert-level automation: \pyodthree\ is designed to give agents the structure needed for more competent anomaly-detection workflows with less OD expertise. This preprint motivates that design claim and shows a worked example.
```

### 2. Medium -- The compressed conclusion keeps the same two biggest scope jumps from the long version (`arxiv-main.tex:193,197`).

There is no classification drift between the long and short related-work tables; the symbols match. The problem is that the short version inherits the same overreach in an even more exposed form.

## Cross-variant drift

The long and short versions' related-work shift tables agree (no drift). The overclaiming in intro and conclusion also appears in both versions in parallel form, so fixing one side without the other would introduce new drift. Coordinate the fixes for A3 (long) with C1 and C2 (short) to keep the two variants aligned.
