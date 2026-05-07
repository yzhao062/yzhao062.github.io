<!-- Round 1 -->

# Review

**Verification notes**

- `python -m pytest pyod/test/test_regen_skill.py pyod/test/test_skill_kb_consistency.py -q` passed.
- `python -m pytest pyod/test/test_cli.py -q` failed only at `pyod/test/test_cli.py:352`.
- `docutils.core.publish_doctree(...)` on `docs/skill_maintenance.rst` succeeded.

**File / Diff Scope**

`git diff --cached` over the 10 staged Phase 1 files for the v3.2.0 od-expert deep-skill work: installer/package-data changes, `scripts/regen_skill.py`, the new KB-consistency and regen tests, the methodology doc, the research/backlog docs, and the docs toctree update.

**Review Lens**

`code` with an Additional focus on Phase 1 versus Phase 2 coupling: design, functionality, error handling, test strength, and consistency between `docs/skill_maintenance.rst` and the actual generator/test implementation. I also spot-checked RST parsing for the new methodology doc.

**New**

1. **High -- Phase 1 stages a knowingly failing test, so the diff is not green on its own.** `pyod/test/test_cli.py:352` now asserts that `pyod install skill` copies `references/workflow.md`, but the packaged skill tree does not contain any `references/` directory yet. I verified the current Phase 1 state: `pyod/test/test_regen_skill.py` and `pyod/test/test_skill_kb_consistency.py` both pass, while `pytest pyod/test/test_cli.py -q` fails only at this new test. That makes the Phase 1 commit red until Phase 2 content lands.

   Recommended change: either move this test into the Phase 2 content commit, or mark it `skip`/`xfail` until `pyod/skills/od_expert/references/` exists, or ship placeholder reference files in the same phase. The tree-aware installer change in `pyod/skills/__init__.py:133` can stay; only the Phase 2 expectation needs deferral.

   Exact rewrite for `pyod/test/test_cli.py:351` (insert immediately above the current function definition on line 352):

   ```python
   @pytest.mark.xfail(reason="Phase 1 does not ship references/workflow.md yet; remove this xfail when Phase 2 content lands")
   ```

2. **Medium -- KB-consistency allowlist exempts real detector names, weakening the rename/staleness guard.** In `_BACKTICK_ALLOWLIST` at `pyod/test/test_skill_kb_consistency.py:29`, `EmbeddingOD`, `MultiModalOD`, `PCA`, and `TimeSeriesOD` are all allowlisted even though they are live keys in `ADEngine().kb.algorithms`. If any of those detectors are renamed or removed later, stale backtick references to them will keep passing the safety-net test.

   Recommended change: remove any allowlist entry that is also a live KB detector key, and add a small regression assertion that `_BACKTICK_ALLOWLIST` has empty intersection with `ADEngine().kb.algorithms`.

3. **Medium -- `_render_detector_list()` does not normalize KB metadata before formatting, so generated markdown will contain raw Python dict reprs.** `scripts/regen_skill.py:64` reads `complexity` and `scripts/regen_skill.py:68` reads `paper`, but those fields are dicts in the live KB, so the current output becomes strings like `complexity: {'time': ...}` and `paper: {'id': ..., 'short': ...}`. That does not match the methodology doc's promise of clean "complexity" and "paper reference" bullets in `docs/skill_maintenance.rst:56`.

   Recommended change: add explicit formatter helpers for structured KB fields before concatenating them into markdown. For example, render complexity as a compact `time / space` string and render paper from a stable human-facing field such as `paper["short"]` with optional id handling if needed.

4. **Medium -- Generator turns raw KB `requires` tokens into `pyod[...]` extras verbatim, producing at least one wrong install hint.** `scripts/regen_skill.py:67` and `scripts/regen_skill.py:75` assume every KB requirement name is also a PyOD extra. That is not true for graph detectors: the KB reports `requires=['torch_geometric']`, while `pyproject.toml:58` exposes the supported extra as `pyod[graph]`. The methodology doc currently promises `pyod[extra]` install hints in `docs/skill_maintenance.rst:58`, so this will generate incorrect guidance as soon as the graph reference file lands.

   Recommended change: introduce an explicit mapping layer from KB dependency tokens to user-facing install hints, for example `torch_geometric -> pyod[graph]`, instead of interpolating the raw token directly.

5. **Medium -- Combined `text-image-detector-list` renderer will duplicate multimodal detectors.** `_SECTION_RENDERERS` at `scripts/regen_skill.py:118` builds that section by concatenating the text list and the image list, but the live KB already includes `EmbeddingOD` and `MultiModalOD` in both modalities. The generated section will therefore repeat those detectors twice.

   Recommended change: build the text/image combined section from a deduplicated ordered collection keyed by detector name, then render once per unique detector. Add a regression test that `EmbeddingOD` and `MultiModalOD` appear exactly once in `text-image-detector-list`.

**Previously raised**

None. This is Round 1.
