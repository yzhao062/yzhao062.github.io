---
name: post-to-linkedin
description: Use when announcing a release, paper, grant, talk, award, or project update on LinkedIn from this repo. Covers drafting, OAuth setup, token refresh, and posting via scripts/post_to_linkedin.py.
---

# Post to LinkedIn

Compose and post announcements to LinkedIn from this repo via `scripts/post_to_linkedin.py`. LinkedIn API posts are free (no per-post charge, unlike X Premium). Max commentary length is 3,000 chars.

The draft format, hashtag sets, and writing rules are shared with the `post-to-x` skill (same `scripts/drafts/` directory, same `references/draft-patterns.md`, same `references/hashtag-sets.md` at `skills/post-to-x/references/`).

## When to use

- User asks to post, share, or announce something on LinkedIn
- Cross-post: the same release/paper/grant that went to X, adapted for LinkedIn tone
- Longer-form academic/professional framing where the 25,000-char X Premium post would feel out of place

Do not use for: generic networking DMs, connection requests, group posts to a Company Page feed (this skill posts to the authenticated user's personal feed only).

## Prerequisites

Two gates.

**Gate 1: drafting / previewing**
- `~/miniforge3/envs/py312/python.exe` has `requests` and `python-dotenv` installed (`pip install -r scripts/requirements-post.txt`).
- Source data available: `data/open-source.json`, `data/publications.json`, or user-provided text.

**Gate 2: real post**
- `.env` at repo root contains `LINKEDIN_CLIENT_ID` + `LINKEDIN_CLIENT_SECRET`.
- LinkedIn app has products **Share on LinkedIn** (Default Tier, gives `w_member_social`) and **Sign In with LinkedIn using OpenID Connect** (Standard Tier, gives `openid profile email`) approved. Both are self-serve; approval is typically instant.
- `.env` also contains `LINKEDIN_ACCESS_TOKEN`, `LINKEDIN_TOKEN_EXPIRES_AT`, `LINKEDIN_USER_URN`, written by `--auth` on first run. `LINKEDIN_REFRESH_TOKEN` is written when LinkedIn returns one; on default self-serve apps it may be empty, in which case re-run `--auth` after the access token expires (60 days).
- User has reviewed and approved the dry-run preview for this specific post.

If Gate 2 fails, stop and report before posting. Drafting and previewing may continue.

## One-time OAuth setup

Before the first post, user must:

1. Create a LinkedIn Developer app at https://developer.linkedin.com (requires a Company Page, not a personal profile; a 2-minute free Company Page creation is fine).
2. Add Products: **Share on LinkedIn** + **Sign In with LinkedIn using OpenID Connect**. Both auto-approve.
3. In the app's **Auth** tab, add `http://localhost:8765/callback` to Authorized redirect URLs.
4. Copy Client ID + Client Secret into `.env` (see `.env.example`).
5. Run:
   ```
   python scripts/post_to_linkedin.py --auth
   ```
   This opens a browser, user authorizes, tokens + user URN are written back to `.env`. Takes about 10 seconds.

Access tokens last 60 days. The script auto-refreshes when a refresh token is available, but LinkedIn's default self-serve tier typically does not return a refresh token (observed 2026-04-22). In that case, re-run `--auth` when the access token expires; the re-auth flow is unchanged, takes ~10 seconds.

## Workflow

```
1. Identify source   →  open-source.json / publications.json / user-provided
2. Draft to file     →  scripts/drafts/<slug>.md  (same directory as X drafts)
                        Can reuse an X draft directly, or tweak for LinkedIn tone.
                        For LinkedIn the draft can be longer (up to 3,000 chars)
                        and more narrative; hashtag volume can be higher (~5 to 10
                        is normal on LinkedIn without penalty).
3. Preview dry-run   →  python scripts/post_to_linkedin.py --dry-run --draft <path>
4. Iterate           →  show preview, accept user edits, re-preview
5. Post              →  python scripts/post_to_linkedin.py --yes --draft <path>
                        Attach images with --media <path> (repeatable, up to 20).
6. Report URL        →  return https://www.linkedin.com/feed/update/<URN>/
```

Always run step 3 before step 5. No exceptions. `--yes` skips the interactive prompt; never use `--yes` without a prior successful `--dry-run` that the user approved.

## Hard rules

- **Lead with the one-line value prop**, same as X posts. LinkedIn readers scan the first sentence; if it does not answer "what is different now?", they scroll past.
- **LinkedIn tone is slightly more professional than X.** Fewer bullet lists, more connective prose. Emojis are accepted but not required.
- **Hashtags**: 3 to 10 tags is fine on LinkedIn (higher ceiling than X). Pick from `skills/post-to-x/references/hashtag-sets.md`.
- **Apply CLAUDE.md writing rules**:
  - No em dashes (Unicode U+2014) or en dashes (Unicode U+2013) as casual punctuation.
  - No banned AI-tell words.
  - Prefer full forms (`it is`) over contractions.
  - No Unicode `U+202F`.
- **Verify every factual claim**. Star counts, download counts, venue names, coauthor names must match `data/open-source.json`, `data/publications.json`, or user-stated facts.
- **Cost**: zero. LinkedIn does not charge per-post via the API.

## Post type differences from X

| Aspect | X (Premium) | LinkedIn |
|---|---|---|
| Char limit | 25,000 | 3,000 |
| Per-post cost | $0.20 with URL, $0.015 without | free |
| URL length counting | t.co shortens to 23 chars | full literal length |
| Hashtags | 3 to 5 | 3 to 10 |
| Tone | direct, punchy, dev-adjacent | professional, narrative, network-adjacent |
| Thread support | native reply-chain (X side only) | not used; single post is canonical on LinkedIn |
| Image limit per post | 4 | 20 |

## Common mistakes (draft from post-to-x + observed)

| Mistake | Fix |
|---|---|
| Reusing an X draft verbatim without adjusting tone | LinkedIn readers expect more context; add 1-2 sentences of positioning before the bullets |
| Dumping too many hashtags (over 10) | LinkedIn allows more than X but the algorithm still penalizes stuffing; stay at 5 to 8 |
| Posting without running `--dry-run` | Contract: dry-run is mandatory. Check cost, char count, media attachments |
| Posting with expired token + no refresh_token | Re-run `--auth` to get a fresh refresh_token |
| Posting an X draft that uses t.co-shortened URL math | LinkedIn counts URLs literally; re-check char count on the preview |

## Quick reference

- Script source: `scripts/post_to_linkedin.py`
- Flags: `python scripts/post_to_linkedin.py --help`
- Env vars: see `.env.example` for LINKEDIN_* keys
- Shared draft patterns: `skills/post-to-x/references/draft-patterns.md`
- Shared hashtag sets: `skills/post-to-x/references/hashtag-sets.md`
- First live post: TBD (set once first LinkedIn post goes out)
