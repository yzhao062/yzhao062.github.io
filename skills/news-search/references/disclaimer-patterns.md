# Disclaimer and Aggregator Detection Patterns

Phase B fetches each candidate page and runs the patterns below. Matches set entries in the candidate's `flags[]` field (see `references/candidate-schema.md`). Phase B uses the flags as hard caps when assigning a tier.

## Why This Exists

Three rounds in a row, AI-generated security catalogs (sectools.tw 713, 793, 854) and auto-aggregator newsletters (Cool Papers, GoatStack, ChatPaper) were initially classified as Tier 2 third-party media because the disclaimer at the bottom of the page was not read. Phase B's regex sweep makes the classification mechanical instead of judgment-based. Hand-curated GitHub awesome-lists are a separate failure mode that this regex layer does not catch. After direct-mention verification, classify them during tier assignment as ecosystem-list evidence (Tier 3 by default), unless an independent editorial outlet has covered the same row.

## Flags and Patterns

Each flag has one or more regex patterns. A page can have multiple flags.

### `ai_generated`

Set when the page declares itself AI-generated. Hard cap at Tier 3.

```regex
本文由\s*AI\s*(產生|生成|整理|撰寫|撰写)
AI[-_\s]?generated\b
[Gg]enerated\s+by\s+(GPT|Claude|Gemini|LLM|AI)
This\s+article\s+was\s+(written|generated)\s+by\s+(AI|GPT|Claude|an?\s+LLM)
```

### `machine_translated`

Set when the page declares itself machine-translated (no editorial pass). Hard cap at Tier 3 unless `editorial_translation` is also set.

```regex
[Mm]achine[-_\s]translated
[Aa]uto[-_\s]translated
machine\s+translation\s+(of|from)
本文为机器翻译
```

### `editorial_translation`

Set when a Chinese-language or other-language page is an editorial translation (journalist or editor pass) of an English source. Compatible with Tier 2 if the editorial review is genuine.

Heuristics: page is on a known editorial outlet (jiqizhixin.com, 36kr.com, infoq.cn, paperweekly.site) AND links to or quotes the English original arXiv paper or blog. Run this check after `machine_translated` to override the cap when both signals appear.

```regex
(?:翻译\s*整理|编辑|译者|翻译\s*校对)
(?:Editor's\s+note|译者注|编者按)
```

### `aggregator`

Set when the page is part of a known auto-aggregator (paper digesters, AI newsletters that auto-curate from arXiv). Hard cap at Tier 3.

Two ways to set:
1. The page's domain is in the `ai-aggregator` class of `references/domain-registry.md`.
2. The page contains an aggregator footer or "powered by" attribution:

```regex
[Pp]owered\s+by\s+(Cool\s*Papers|ChatPaper|GoatStack|alphaXiv)
[Vv]ia\s+(Cool\s*Papers|ChatPaper|GoatStack)
[Aa]uto[-_\s]curated\s+from
[Cc]urated\s+with\s+(GPT|Claude|AI)
```

### `templated_db`

Set when the page is a templated catalog entry (security tool catalog, dataset card, leaderboard row). Useful for Phase B to recognize but not a hard tier cap, since templated databases can still be high-value if maintained editorially.

Heuristics: page has uniform layout (cardinality of unique items per page = 1) and the entry is one of many on the same domain. Less mechanical to detect than the others; check by looking at sibling URLs (e.g., sectools.tw/tools/{id} for many ids).

### `paywall_or_blocked`

Set when WebFetch returns a 403, paywall stub, or content less than 500 characters. Phase B should not classify these from snippet alone; either retry with a different fetcher or ask the user to verify manually.

```regex
(?:Subscribe\s+to\s+continue|Sign\s+in\s+to\s+read|Access\s+denied|403\s+Forbidden)
```

## How Phase B Uses the Flags

| Flag set | Tier cap |
|---|---|
| `ai_generated` | <= Tier 3 |
| `aggregator` | <= Tier 3 |
| `machine_translated` (without `editorial_translation`) | <= Tier 3 |
| `templated_db` | no cap; review case by case |
| `paywall_or_blocked` | hold for manual verification |

A candidate can have multiple flags; the lowest cap wins.

## Adding New Patterns

When a round encounters a new disclaimer or aggregator footer not covered above:

1. Add the pattern to the appropriate section.
2. Commit with the audit so the next round picks it up.

This is the disclaimer-side equivalent of the domain-registry harvest step.
