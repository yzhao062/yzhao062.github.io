---
name: post-to-x
description: Use when announcing a release, paper, grant, talk, award, or project update on X (Twitter) from this repo. Covers drafting, style compliance, cost preview, and posting via scripts/post_to_x.py.
---

# Post to X

Compose and post announcement tweets from this repo via `scripts/post_to_x.py`. The default is one brief, natural post that explains what the thing is and why it is useful. The account holder has X Premium, which allows single posts up to 25,000 characters; that is capacity for the rare post that needs it, not a length target. Threads are opt-in.

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

The `--project` seed is a legacy long-form scaffold: its TODO prompts ask for bullets, star and docs lines, and 3 to 5 hashtags. Rewrite the seed into the short release shape in `references/draft-patterns.md`; do not fill each prompt mechanically.

## Hard rules

- **Lead with the one-line value prop** that answers "what is different now?" For a release, that is the single biggest change, not a list of features. If the user says the core is X, do not bury X under other points.
- **Keep it brief by default.** A few sentences on use and value, one link, a few hashtags. Do not pad to fill space or add bullets, feature lists, questions, research-program framing, or calls to action by habit, and do not add a caveat paragraph by habit. A limit that keeps a claim honest is required at any length. Write a long post only when the user asks or the content cannot be understood briefly. See `references/example-prefixsim.md` for one short example (a reference, not a template).
- **Repost or quote captions add one useful angle** (who should use it, where it fits, a concrete takeaway). Do not restate the original post. `post_to_x.py` has no native quote or repost option, so a caption posted through the script must include the original post's URL and read as standalone commentary; otherwise the user makes the native quote manually.
- **Hashtags: a few relevant ones**, usually two to four and never more than five, each naming something the post is about. Use `references/hashtag-sets.md` as vocabulary, and do not make claims about how X ranks tagged posts.
- **One post is the default.** Only split into a thread when the user explicitly asks, or when content has 3+ distinct beats that read awkwardly as one post.
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
| Padding a short announcement into a long post, or adding bullets, a question, or a call to action by habit | Cut to the sentences that explain use and value; go long only on request or real need |
| Repost caption that restates the original | Add one angle the original does not state |
| Hashtags that do not match the body, or more than five | Keep a few relevant tags; justify each by the post content |
| Em dash slips into draft (`—`) | Replace with `:` or `,` before preview; the guard hook will block Writes with banned style anyway |
| Defaulting to thread mode | One post by default; `--thread` only on explicit request |
| Posting without dry-run confirmation | Always run `--dry-run` first, get user yes/no, then run with `--yes` |
| Fabricated social proof ("300+ companies") | Only cite numbers from `data/open-source.json`, `data/publications.json`, or user-stated facts |

## Quick reference

- Draft patterns (release, paper, repost, grant, talk): `skills/post-to-x/references/draft-patterns.md`
- Short release example (PrefixSim, editorial reference only): `skills/post-to-x/references/example-prefixsim.md`
- Hashtag sets by topic and announcement type: `skills/post-to-x/references/hashtag-sets.md`
- Earlier posted example, 2026-04-17: `scripts/drafts/pyod-3.0.md` (PyOD 3 release; its bullet list is not the default shape)
- Script source: `scripts/post_to_x.py`
- Script flags: run with `--help`
