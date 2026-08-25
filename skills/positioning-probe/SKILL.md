---
name: positioning-probe
description: Decide or validate a research-program name, site headline, lab tagline, or talk framing by measuring where the person actually surfaces, instead of arguing about which phrase sounds better. Use when choosing an umbrella term, renaming a program, or judging whether a phrase is dated or contested. Also use it to check who already owns a phrase, and to re-audit on a schedule whether a public self-description still matches the work.
---

# Positioning Probe

## Overview

A naming decision is usually argued. It can be measured instead. This skill measures two
things that are easy to confuse, then applies a set of gates that a measured answer cannot
supply on its own.

The output is a decision with the evidence behind it.

## When to Use

- Choosing or changing the umbrella term for a research program.
- Judging whether a term reads as dated, or as owned by another community.
- Deciding what belongs in a site `<title>`, an H1, a bio first line, or a talk title.
- Checking prior art before adopting a phrase.
- Diagnosing why a person does not surface for the work they actually do.
- Re-checking an existing description on a schedule. It catches a name that has drifted
  from the work, a stale claim, or a phrase a new claimant has taken.

Skip when the phrasing is local and reversible, such as one section heading. It is also
unnecessary when an external body fixes the name and the task is only to describe it well.

## The One Idea That Matters

**Two mechanisms answer naming questions, they disagree, and confusing them wastes a day.**

| | Parametric | Retrieval |
|---|---|---|
| What it is | What a model says with no web access | What a search engine returns now |
| Source | Training data | The live web |
| Lag | Provider- and version-specific. Record the published cutoff, or "unknown" | Query-, client-, locale-, and engine-specific |
| Responds to a site edit | Only after a provider update | After discovery and recrawling, on each engine's own schedule |
| Good for | Associations the tested models returned on the test date | Results returned under the recorded retrieval conditions |

A researcher appointed in the last few years is often absent from parametric memory under
every candidate term. The same person can rank first in retrieval for the terms their own
site and repositories carry. Both facts are real and they point to different actions.

Low parametric recall is evidence about the model versions tested, on the date tested. It
says the site text is a lever worth pulling. Before concluding it is the only one, inventory
the other indexed surfaces: institutional pages, repositories, citation records, profiles,
and coauthors' pages. Google documents several inputs to the title link it generates and
publishes no ranking-weight ordering among them. Treat the `<title>` as a documented input
rather than a measured maximum.

## Pipeline

### Probe A, forward: does the person surface for a term?

Ask for a ranked list of people working on term X, then look for the subject.

**Query wording decides the answer.** "Leading international researchers in X" returns a
media-salience list, heavy on well-known public figures, whatever X is. Ask instead for
"university professors, tenure-track or tenured, whose group publishes on X at NeurIPS,
ICML, ICLR, KDD, ACL, or IEEE and ACM journals". That returns the working field.

### Probe B, reverse: what terms attach to the person?

Give the name and ask what they are known for. This is the more informative half. It reveals:

- which phrase already carries equity;
- whether the models have the right person at all.

Run it in variants that add one qualifier at a time: bare name, name plus institution, name
plus a flagship artifact, name plus lab. Comparing the variants tells you which qualifier
fixes what. In one measured run, the institution fixed identity while the flagship artifact
fixed the topic but attached it to the wrong institution.

### Probe C, prior art: who already owns the phrase?

Before adopting a phrase, find its existing claimants and classify each as academic,
standards body, government, consulting or accounting, security vendor, or unclaimed. A
phrase owned by a standards body is not merely crowded; its meaning has already been set,
and a homepage cannot reset it.

## Mandatory Controls

**Every run needs a control term the subject definitionally owns.** If the control fails,
the probe is broken and its zeros mean nothing. Pick something like the person's own
flagship library or most-cited artifact.

**Every scraped search result needs a known-answer sanity check.** Issue one query whose
correct top result you already know, and confirm it appears. An engine that returns HTTP
200 without it is degraded, not working.

Engine verdicts are perishable. Two runs three hours apart on one machine disagreed
completely about which engines worked, because the client differed. Never carry a verdict
forward from an earlier run. See `references/engines.md`.

## Gates a Measurement Cannot Supply

A term can win every probe and still be wrong. Check these before proposing anything.

1. **One topic.** The headline names a single thing. Never conjoin a current direction with
   a legacy one to widen keyword coverage. An asset that already ranks on its own name does
   not need headline space.
2. **Expected durability.** Name the event that would make each candidate stale, and give
   the evidence that the event is likely. A term tied to a current system architecture
   usually dates when that architecture is superseded, while a term naming a lasting
   property usually does not. "Testable software" outlived decades of architecture churn.
   Treat this as one factor with stated evidence, not as a fixed lifespan per category.
3. **Reads as a field name.** Show the candidate beside real lab names and ask which look
   like fields. A keyword list fails this even when every keyword ranks.
4. **Pronunciation.** A phrase that makes a reader pause is out, whatever it scores.
5. **Parallelism.** In `X and Y`, both sides take the same grammatical form. Mixed forms are
   disqualified.
6. **No parent and child in one conjunction.** If a standards body defines Y as a
   sub-process of X, then `X and Y` reads as a category beside its own member. Layering is
   the repair: put the child under the parent instead of beside it.
7. **The title must reflect the page.** Google documents "the page title doesn't reflect
   the page content" as a reason it might replace the title shown in results, which would
   defeat the change. Note the hedge: might, not will. Do not extend this into the stricter
   folk rule that a title differing textually from the H1 triggers a rewrite, which is
   undocumented. See `references/seo-facts.md` before asserting any rule in this area.

## Re-running Later, on an Existing Description

The first run picks a name. Later runs ask a different question: **does what this page says
about this person still hold?** Two things drift, and they drift for unrelated reasons.

**The evidence decays.** Everything dated in `references/` expires. Prior-art claimants
accumulate, so a phrase that was open becomes crowded. Engine verdicts expire in hours, not
months. Search-engine documentation changes. Re-verify rather than reading the stored tables
as current, and re-date the file when you do.

**Save a dated baseline, or later runs are anecdotes.** Before comparing anything, record the deployed
wording, the source commit, and the exact queries. Add the control and its verdict, the returned
URLs and positions, and the model identifiers with their raw outputs. Keep the evidence
behind each factual claim.

| Item | Record and compare | Refresh |
|---|---|---|
| Work fit | Current output over a review window chosen before inspection, and the window itself | Every audit |
| Factual claims | Source URL, date checked, role end dates, how any count was taken, what a superlative ranges over | Before publishing, and every audit |
| Prior use | Exact phrase and variants, claimant, type of use, primary URL, access date | Every audit |
| Retrieval | Query, locale, client, engine, timestamp, control verdict, result URLs and ranks | Same session as the decision |
| Parametric probe | Provider, exact model identifier, prompt, sample count, raw output | New baseline after any model or prompt change |
| Surfaces | Tracked source, rendered pages, structured data, generated files, institutional profiles, crawler summaries | Every audit |

Compare retrieval only when the control passes. A change in provider, model, prompt, client,
or query makes a new baseline rather than a finding. Fix stale factual claims straight away.
Reopen the name only when work-fit drift, or retrieval evidence that replicates under the
recorded controls, survives.

**The description drifts from the work.** This half needs no probe at all and is usually the
larger finding. Read the live description against the record and check each claim:

| Check | How |
|---|---|
| Does the headline still name the current work? | Compare it against a review window chosen before inspection and recorded. Twelve months suits a fast-publishing field; a book, a trial, or an instrument needs longer |
| Has a subpoint gone empty? | A named area with nothing recent behind it is now a claim, not a description |
| Is a superlative still true? | Counts, rankings, and "first" claims age silently and are the most quotable things on the page |
| Do the roles still hold? | Appointments, advisory positions, and company status carry end dates the page rarely records |
| Does every page still agree? | A rename usually reaches the obvious pages and misses generated files, shared includes, and machine-readable summaries |

That last row is where a real run failed. A full-site rename covering nine files missed a
shared sidebar rendered on every page by a script, and a crawler-facing site summary that
defined the old term as the umbrella. Neither is an HTML page in the site root, so a scan
written as "look through the pages" cannot see them.

**Enumerate surfaces before scanning, not while scanning.** List every place the name can
appear. Page source, shared includes, and JavaScript-injected fragments. Generated regions
and the source files behind them. Structured data, machine-readable summaries such as
`llms.txt`, plain-text deliverables, and anything a CV pipeline emits. Then grep the whole
tracked tree by content, rather than a glob of one extension.

## Reporting

State the mechanism beside every number, because a reader who does not know which one
produced it will draw the wrong action from it. Report the control outcome first: without a
passing control, report the run as unmeasurable rather than as a set of zeros.

Withhold rather than guess. A unit that reports "no engine passed the control, so this is
unmeasurable" is worth more than one that reports five confident zeros.

## Files

- `scripts/probe.py` runs Probes A and B across several model families through an
  OpenAI-compatible gateway and AWS Bedrock. Everything about the subject comes from a JSON
  config, so the script carries no personal paths, endpoints, or terms. It requires the key
  path and gateway URL in the environment, refuses a plaintext HTTP gateway for a non-local
  host, and never prints the key. `scripts/config.example.json` is the template.
- `references/pitfalls.md` is the failure catalogue. Read it before designing a run.
- `references/engines.md` gives the control-query method and one dated sample matrix.
- `references/seo-facts.md` separates documented search behavior from folklore.
- `references/phrase-landscape.md` records dated public use of five audit-adjacent phrases,
  with source links. It does not establish ownership or future ranking difficulty.
