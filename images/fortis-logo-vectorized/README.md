# FORTIS Logo Sources

The site uses the three SVG masters in `images/fortis/`. For an ordinary change, edit those and run `scripts/export_fortis_brand.py`. This directory records how the masters were made, plus the layouts that were not adopted.

Each script reads the previous one's output:

1. `trace_original.py` traces `fortis-original-raster.png` into `fortis-original-editable.svg`, which keeps the gradients. The raster is `images/lab-logo.png` as it was before commit `14e754f`.
2. `build_variants.py` writes the flat, clearspace and horizontal variants to `variants/`.
3. `build_arc.py` adds the USC upper-arc variant.
4. `build_brand_kit.py` writes `brand-kit/`, whose SVGs are identical to the masters in `images/fortis/`.

Rerunning step 1 replaces the editable master. Steps 2 to 4 reproduced the tracked SVGs byte for byte on 2026-10-17. PNG, PDF, zip and preview files are not tracked; rerun the scripts to get them.

Requirements: CairoSVG, Pillow and fontTools; step 1 also needs NumPy, SciPy and potracer.

`../fortis-logo-draft/` holds an earlier geometric redesign. Run `build.py` before `build_v2.py`, which reads its output.
