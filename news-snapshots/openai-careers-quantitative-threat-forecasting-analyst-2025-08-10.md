# OpenAI Careers — Quantitative Threat Forecasting Analyst

Local snapshot for the Ledger 1 #8h citation in `news-coverage-audit.md`. This is the **second** OpenAI
careers posting that names PyOD, distinct from the Technical Intelligence Analyst posting recorded as #8g.

## Source

- **Canonical URL:** https://openai.com/careers/quantitative-threat-forecasting-analyst/ (now HTTP 403 to
  every automated client; the role is absent from OpenAI's live Ashby feed, checked against 750 live postings
  on 2026-08-09)
- **Wayback archive URLs (both HTTP 200, canonical first-party URL):**
    - http://web.archive.org/web/20250719151710/https://openai.com/careers/quantitative-threat-forecasting-analyst/ (36,623 bytes)
    - http://web.archive.org/web/20250810151707/https://openai.com/careers/quantitative-threat-forecasting-analyst/ (37,730 bytes)
- **Committed sidecar:** `openai-careers-quantitative-threat-forecasting-analyst-2025-08-10.html`, the
  2025-08-10 Wayback capture retrieved 2026-08-09 (218,278 bytes as served, including the Wayback toolbar
  wrapper). Two literal `PyOD` occurrences.
- **Verification:** Retrieved and text-extracted 2026-08-09 during the Phase B verification pass of the
  2026-08-09 news-search run.

## Verified excerpt

Verbatim, from the qualifications block:

> Expertise with modern toolchains—NumPyro, TensorFlow Probability, PyMC, Darts, GluonTS/Chronos, sktime,
> **PyOD 2.0**, River, scikit‑survival—and readiness to evaluate emerging libraries as the field evolves.

Surrounding context (same block):

> ... Deep fluency in statistical inference, forecasting, uncertainty quantification, and decision modeling
> —especially under sparse or adversarial data conditions. Demonstrated impact: you've shipped models that
> directly informed capital allocation, fraud prevention, incident response, or safety interventions.
> **Expertise with modern toolchains—NumPyro, TensorFlow Probability, PyMC, Darts, GluonTS/Chronos, sktime,
> PyOD 2.0, River, scikit‑survival**—and readiness to evaluate emerging libraries as the field evolves.
> Strong coding skills (Python/JAX/PyTorch or R) and data‑engineering fundamentals (SQL, Spark, data
> warehousing). ...

The mention names a **pinned major version** (PyOD 2.0) inside a named toolchain list, alongside NumPyro,
PyMC, sktime, and River. That is a stronger adoption signal than #8g's "anomaly detection tools, such as
PyOD": it places PyOD among the libraries an OpenAI threat-forecasting hire is expected to already know.

## Why this snapshot exists, and what it corrects

The 2026-05-07 snapshot note for #8g states that OpenAI's Cloudflare configuration blocks the Internet
Archive crawler, so "the URL cannot be archived to web.archive.org from any client." **That claim is too
strong and is corrected here.** OpenAI careers pages were archivable in mid-2025: this URL has two clean
HTTP 200 captures from July and August 2025. The block is either newer than those captures or applied
unevenly across postings. The operational lesson stands unchanged — commit a local sidecar — but the CDX
index should be checked before concluding that no archive exists.

This row also resolves a hold recorded in the audit's Negative Results table: "Earlier third-party mirrors
of the Quantitative Threat Forecasting Analyst role naming PyOD 2.0 remain candidate-only unless an official
OpenAI URL resurfaces." The Wayback captures are of the canonical `openai.com` URL, not a third-party job
aggregator, so the hold condition is met.
