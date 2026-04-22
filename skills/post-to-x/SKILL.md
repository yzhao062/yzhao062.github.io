---
name: post-to-x
description: Use when announcing a release, paper, grant, talk, award, or project update on X (Twitter) from this repo. Covers drafting, style compliance, cost preview, and posting via scripts/post_to_x.py.
---

# Post to X

Compose and post announcement tweets from this repo via `scripts/post_to_x.py`. The account holder has X Premium, so single long posts (up to 25,000 chars) are the default; threads are opt-in.

## When to use

- User asks to post, tweet, or announce something on X/Twitter
- New open-source release, paper, grant, award, talk, hiring, student news
- Follow-ups to previous announcements

Do **not** use for: drafting LinkedIn posts, email newsletters, or non-public announcements.

## Prerequisites

Two gates. Drafting and previewing require less than posting; do not block the user on posting-only items when they just want to draft.

**Gate 1: drafting and previewing** (steps 1 to 4 of the workflow)
- `~/miniforge3/envs/py312/python.exe` has `tweepy` and `python-dotenv` installed (`pip install -r scripts/requirements-post.txt`). `tweepy` is imported at module load even for `--dry-run`, so it must be present.
- Source data available: `data/open-source.json`, `data/publications.json`, or user-provided text.

If Gate 1 fails, stop and report.

**Gate 2: real post** (step 5)
- `.env` at repo root contains `X_API_KEY`, `X_API_KEY_SECRET`, `X_ACCESS_TOKEN`, `X_ACCESS_TOKEN_SECRET`. Do not ask the user to paste them into chat; they are gitignored by design.
- X Developer account has API credit balance (check at `console.x.com` → Billing).
- User has reviewed and approved the dry-run preview for this specific post.

If Gate 2 fails, stop and report **before posting**. Drafting and previewing may continue.

## Workflow

```
1. Identify source   →  open-source.json / publications.json / user-provided
2. Draft to file     →  scripts/drafts/<slug>.md  (use references/draft-patterns.md)
                        For data/open-source.json entries, seed with:
                        python scripts/post_to_x.py --project <name>
                        That writes scripts/drafts/<slug>.md with TODO markers and exits.
3. Preview dry-run   →  python scripts/post_to_x.py --dry-run --draft <path>
4. Iterate           →  show preview, accept user edits, re-preview
5. Post              →  python scripts/post_to_x.py --yes --draft <path>
                        Attach images with --media <path> (repeatable, up to 4).
                        In thread mode, media attaches to the first tweet only.
6. Report URL        →  return https://x.com/i/web/status/<id>
```

Always run step 3 before step 5. No exceptions. `--project` seeds a draft but never posts directly; the script refuses to post any draft that still contains `<!-- TODO` markers.

## Hard rules

- **Lead with the one-line value prop** that answers "what is different now?" For a release, that is the single biggest change, not a list of features. If the user says the core is X, do not bury X under other points.
- **End with 3 to 5 hashtags** selected from `references/hashtag-sets.md`. Never more than 5; algorithm penalizes stuffing.
- **Single long post is the default** (Premium). Only split into a thread when the user explicitly asks, or when content has 3+ distinct beats that read awkwardly as one paragraph.
- **Apply CLAUDE.md writing rules**:
  - No em dashes (`—`) or en dashes (`–`) as casual sentence punctuation. Use commas, colons, semicolons, or parentheses instead.
  - No banned words from `AGENTS.md` / `CLAUDE.md` Writing Defaults.
  - Prefer full forms (`it is`) over contractions where natural.
  - Avoid Unicode `U+202F`.
- **Verify every factual claim** against the source JSON or the user. Star counts, download counts, version numbers, coauthor names, venue dates: do not fabricate or round up.
- **Cost awareness**: each post with a URL is $0.20, without URL is $0.015. Show total in dry-run output. Warn the user if a thread pushes above $1 for a single announcement.

## Cost reference

| Scenario | Cost |
|---|---|
| Single long post, no URL | $0.015 |
| Single long post, with URL | $0.20 |
| 3-part thread, all with URLs | $0.60 |
| 5-part thread, all with URLs | $1.00 |

## Common mistakes (from observed failures)

| Mistake | Fix |
|---|---|
| Leading with a side feature (e.g., "multi-modal") when the core change is elsewhere (e.g., "agentic") | Ask the user what the core change is before drafting, do not infer from JSON alone |
| Drafting without hashtags | Always append 3 to 5 from `references/hashtag-sets.md` |
| Em dash slips into draft (`—`) | Replace with `:` or `,` before preview; the guard hook will block Writes with banned style anyway |
| Defaulting to thread mode | Premium user gets single long post by default; `--thread` only on explicit request |
| Posting without dry-run confirmation | Always run `--dry-run` first, get user yes/no, then run with `--yes` |
| Fabricated social proof ("300+ companies") | Only cite numbers from `data/open-source.json`, `data/publications.json`, or user-stated facts |

## Quick reference

- Draft patterns (release, paper, grant, talk): `skills/post-to-x/references/draft-patterns.md`
- Hashtag sets by topic and announcement type: `skills/post-to-x/references/hashtag-sets.md`
- Known-good example posted 2026-04-17: `scripts/drafts/pyod-3.0.md` (PyOD 3 release)
- Script source: `scripts/post_to_x.py`
- Script flags: run with `--help`
