#!/usr/bin/env python3
"""Post announcements to X (Twitter) from the command line.

Usage
-----
  python scripts/post_to_x.py "Just shipped PyOD v3.0: https://github.com/yzhao062/pyod"
  python scripts/post_to_x.py --draft scripts/drafts/pyod-3.0.md
  python scripts/post_to_x.py --project pyod          # seeds scripts/drafts/pyod.md and exits
  python scripts/post_to_x.py --thread "para 1\\n\\npara 2\\n\\npara 3"
  python scripts/post_to_x.py --dry-run "preview only"

Setup
-----
  pip install -r scripts/requirements-post.txt
  Fill in X_API_KEY, X_API_KEY_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET in .env
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

import tweepy
from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parent.parent
OPEN_SOURCE_JSON = REPO_ROOT / "data" / "open-source.json"
ENV_FILE = REPO_ROOT / ".env"
DRAFTS_DIR = REPO_ROOT / "scripts" / "drafts"

URL_RE = re.compile(r"https?://\S+")
PREMIUM_MAX_CHARS = 25_000
URL_EFFECTIVE_LEN = 23
COST_WITH_URL = 0.20
COST_NO_URL = 0.015

_TRAILING_PUNCT = ".,;:!?)]}'\">"
_TODO_MARKER = "<!-- TODO"


def _find_urls(text: str) -> list[tuple[int, int]]:
    """Return (start, end) spans of URLs with trailing punctuation trimmed.

    X shortens URLs via t.co and treats adjacent punctuation (`.`, `)`, `,`)
    as surrounding text, not part of the link. This helper mirrors that so
    the effective character count matches what X actually renders.

    Limitations (documented, locked by scripts/check_post_to_x_contract.py):
    - Bare domains without a scheme (e.g. `pyod.readthedocs.io`) are not
      detected. Always include `http://` or `https://` for accurate counting.
    - Trailing `)`, `]`, `}` are always trimmed, even when balanced inside the
      URL (e.g. `https://example.com/a(b)` overcounts by 1). Percent-encode
      the closing bracket (`%29`, `%5D`, `%7D`) for exact counting if needed.
    """
    spans: list[tuple[int, int]] = []
    for m in URL_RE.finditer(text):
        start, end = m.start(), m.end()
        while end > start and text[end - 1] in _TRAILING_PUNCT:
            end -= 1
        if end > start:
            spans.append((start, end))
    return spans


def effective_char_count(text: str) -> int:
    """Character count as X sees it. Each URL counts as 23 chars (t.co)."""
    spans = _find_urls(text)
    if not spans:
        return len(text)
    total = 0
    cursor = 0
    for start, end in spans:
        total += start - cursor + URL_EFFECTIVE_LEN
        cursor = end
    total += len(text) - cursor
    return total


def cost_for(text: str) -> tuple[float, bool]:
    has_url = bool(_find_urls(text))
    return (COST_WITH_URL if has_url else COST_NO_URL, has_url)


def split_into_thread(text: str) -> list[str]:
    """Split on blank lines. Prefix with (i/N) when more than one part."""
    parts = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    if len(parts) <= 1:
        return parts or [text.strip()]
    total = len(parts)
    return [f"({i + 1}/{total}) {p}" for i, p in enumerate(parts)]


def load_project_template(project_key: str) -> str:
    """Build a seed draft from an open-source.json entry.

    The result is intentionally incomplete: it leaves TODO markers so the
    user is forced to edit before posting. Callers should write it to
    scripts/drafts/<slug>.md, not post it directly.
    """
    if not OPEN_SOURCE_JSON.exists():
        sys.exit(f"Not found: {OPEN_SOURCE_JSON}")
    data = json.loads(OPEN_SOURCE_JSON.read_text(encoding="utf-8"))
    key_lower = project_key.lower()
    match = next(
        (entry for entry in data if entry.get("name", "").lower() == key_lower),
        None,
    )
    if match is None:
        names = ", ".join(sorted(entry.get("name", "?") for entry in data))
        sys.exit(f"Project '{project_key}' not in open-source.json. Available: {names}")
    name = match.get("name", "")
    desc = match.get("description", "").strip()
    repo = match.get("repo_url", "").strip()
    docs = match.get("docs_url", "").strip()
    stars = match.get("stars")
    star_line = f"{stars:,}+ GitHub stars" if isinstance(stars, int) else ""

    lines = [
        f"🚀 {name}: {desc}",
        "",
        f"{_TODO_MARKER}: rewrite the lead so it answers 'what changed' in one sentence. -->",
        f"{_TODO_MARKER}: add 2 to 3 bullets on what is new. -->",
        "",
    ]
    if star_line:
        lines.append(f"{star_line}.")
    if docs:
        lines.append(f"Docs: {docs}")
    if repo:
        lines.append(f"Repo: {repo}")
    lines.append("")
    lines.append(
        f"{_TODO_MARKER}: pick 3 to 5 hashtags from "
        "skills/post-to-x/references/hashtag-sets.md -->"
    )
    return "\n".join(lines)


def seed_project_draft(project_key: str) -> Path:
    """Write a project seed to scripts/drafts/<slug>.md and return the path.

    Refuses to overwrite an existing draft. The user must edit the file and
    then use `--draft <path>` to actually post.
    """
    text = load_project_template(project_key)
    slug = re.sub(r"[^a-z0-9]+", "-", project_key.lower()).strip("-")
    if not slug:
        sys.exit(f"Could not derive a filename from '{project_key}'.")
    DRAFTS_DIR.mkdir(parents=True, exist_ok=True)
    path = DRAFTS_DIR / f"{slug}.md"
    if path.exists():
        sys.exit(
            f"Draft already exists: {path}\n"
            f"Open it, edit, then:\n"
            f"  python scripts/post_to_x.py --dry-run --draft "
            f"{path.relative_to(REPO_ROOT).as_posix()}"
        )
    path.write_text(text + "\n", encoding="utf-8")
    rel = path.relative_to(REPO_ROOT).as_posix()
    print(f"Seeded draft at: {rel}")
    print("Next steps:")
    print("  1. Edit the draft. Remove all <!-- TODO --> markers.")
    print(f"  2. Preview: python scripts/post_to_x.py --dry-run --draft {rel}")
    print(f"  3. Post:    python scripts/post_to_x.py --draft {rel}")
    return path


def preview(posts: list[str]) -> float:
    total = 0.0
    print("=" * 64)
    print(f"{len(posts)} post(s) queued:")
    for i, post in enumerate(posts, 1):
        cents, has_url = cost_for(post)
        total += cents
        chars = effective_char_count(post)
        flag = " [URL]" if has_url else ""
        print(f"\n--- Post {i}/{len(posts)}  ({chars} chars, ${cents:.3f}{flag}) ---")
        print(post)
    print("\n" + "=" * 64)
    print(f"Estimated cost: ${total:.3f}")
    return total


def confirm(prompt: str = "Post now? (y/n): ") -> bool:
    try:
        return input(prompt).strip().lower() in {"y", "yes"}
    except (EOFError, KeyboardInterrupt):
        return False


class ThreadError(Exception):
    """A thread post failed partway through. Carries already-posted tweet IDs."""

    def __init__(self, message: str, posted_ids: list[str]) -> None:
        super().__init__(message)
        self.posted_ids = posted_ids


def _remediation_for(exc: BaseException | None) -> str:
    """Return a one-line remediation hint for a known Tweepy exception."""
    if isinstance(exc, tweepy.Unauthorized):
        return (
            "Unauthorized (401). Check X_API_KEY, X_API_KEY_SECRET, "
            "X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET in .env."
        )
    if isinstance(exc, tweepy.Forbidden):
        return (
            "Forbidden (403). Confirm the app's permissions include Read and "
            "Write, and that Access Token was regenerated after changing "
            "permissions."
        )
    if isinstance(exc, tweepy.TooManyRequests):
        return (
            "Rate limited (429). Wait and retry. If this persists, check API "
            "credit balance at console.x.com."
        )
    return ""


def post_single(
    client: tweepy.Client, text: str, media_ids: list[str] | None = None
) -> str:
    kwargs: dict[str, object] = {"text": text}
    if media_ids:
        kwargs["media_ids"] = media_ids
    resp = client.create_tweet(**kwargs)
    return resp.data["id"]


def post_thread(
    client: tweepy.Client,
    parts: list[str],
    media_ids: list[str] | None = None,
) -> list[str]:
    ids: list[str] = []
    reply_to: str | None = None
    for i, part in enumerate(parts, 1):
        kwargs: dict[str, object] = {"text": part}
        if reply_to is not None:
            kwargs["in_reply_to_tweet_id"] = reply_to
        if i == 1 and media_ids:
            kwargs["media_ids"] = media_ids
        try:
            resp = client.create_tweet(**kwargs)
        except tweepy.TweepyException as e:
            raise ThreadError(
                f"Thread failed at part {i}/{len(parts)}: {e}", ids
            ) from e
        ids.append(resp.data["id"])
        reply_to = ids[-1]
    return ids


def upload_media(creds: dict[str, str], paths: list[Path]) -> list[str]:
    """Upload media files via v1.1 API and return media_id strings.

    v2 create_tweet accepts media_ids but v2 has no upload endpoint yet,
    so we must authenticate v1.1 alongside to call media_upload().
    """
    if not paths:
        return []
    auth = tweepy.OAuth1UserHandler(
        creds["X_API_KEY"],
        creds["X_API_KEY_SECRET"],
        creds["X_ACCESS_TOKEN"],
        creds["X_ACCESS_TOKEN_SECRET"],
    )
    api_v1 = tweepy.API(auth)
    ids: list[str] = []
    for path in paths:
        media = api_v1.media_upload(filename=str(path))
        ids.append(media.media_id_string)
    return ids


def resolve_content(args: argparse.Namespace) -> str:
    if args.text is not None:
        return args.text
    if args.draft is not None:
        if not args.draft.exists():
            sys.exit(f"Draft not found: {args.draft}")
        return args.draft.read_text(encoding="utf-8").strip()
    sys.exit("Provide inline text or --draft.")


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Post to X from the command line.")
    ap.add_argument("text", nargs="?", help="Inline post text")
    ap.add_argument("--draft", type=Path, help="Path to a text or markdown file to post")
    ap.add_argument(
        "--project",
        help=(
            "Seed a draft from data/open-source.json into scripts/drafts/<slug>.md "
            "and exit. Does not post."
        ),
    )
    ap.add_argument(
        "--thread",
        action="store_true",
        help="Split on blank lines into a reply chain (default: single long post)",
    )
    ap.add_argument("--dry-run", action="store_true", help="Preview only, do not post")
    ap.add_argument("--yes", action="store_true", help="Skip confirmation prompt")
    ap.add_argument(
        "--media",
        type=Path,
        action="append",
        default=[],
        help=(
            "Attach image/video (repeatable; up to 4 images per post). "
            "In thread mode, media attaches to the first tweet only."
        ),
    )
    return ap.parse_args()


def main() -> int:
    args = parse_args()

    sources = sum(x is not None for x in (args.text, args.draft, args.project))
    if sources != 1:
        sys.exit("Provide exactly one of: inline text, --draft, or --project.")

    if args.project is not None:
        seed_project_draft(args.project)
        return 0

    content = resolve_content(args)
    posts = split_into_thread(content) if args.thread else [content.strip()]

    for i, post in enumerate(posts, 1):
        chars = effective_char_count(post)
        if chars > PREMIUM_MAX_CHARS:
            sys.exit(
                f"Post {i} is {chars} chars, exceeds {PREMIUM_MAX_CHARS:,} limit. "
                f"Add --thread to split, or shorten."
            )

    media_paths: list[Path] = list(args.media)
    if len(media_paths) > 4:
        sys.exit(f"--media: {len(media_paths)} files given; X allows at most 4 per post.")
    for path in media_paths:
        if not path.exists():
            sys.exit(f"Media file not found: {path}")

    preview(posts)
    if media_paths:
        target = "first tweet" if len(posts) > 1 else "post"
        print(f"Media attachments ({len(media_paths)}, attached to {target}):")
        for path in media_paths:
            size_kb = path.stat().st_size / 1024
            print(f"  - {path} ({size_kb:,.1f} KB)")

    has_todo = any(_TODO_MARKER in p for p in posts)
    if has_todo and not args.dry_run:
        sys.exit(
            f"Draft still contains '{_TODO_MARKER}' markers. Edit the draft and "
            f"remove them before posting."
        )
    if has_todo and args.dry_run:
        print(
            f"WARNING: draft contains '{_TODO_MARKER}' markers. Remove them before "
            f"a real post."
        )

    if args.dry_run:
        print("Dry run. Nothing posted.")
        return 0

    if not args.yes and not confirm():
        print("Cancelled.")
        return 0

    creds = load_credentials()
    client = build_client(creds)
    media_ids = upload_media(creds, media_paths) if media_paths else []

    try:
        if len(posts) == 1:
            tid = post_single(client, posts[0], media_ids or None)
            print(f"Posted: https://x.com/i/web/status/{tid}")
        else:
            ids = post_thread(client, posts, media_ids or None)
            print(f"Thread posted ({len(ids)} tweets).")
            print(f"First:  https://x.com/i/web/status/{ids[0]}")
            print(f"Last:   https://x.com/i/web/status/{ids[-1]}")
    except ThreadError as e:
        print(str(e), file=sys.stderr)
        hint = _remediation_for(e.__cause__)
        if hint:
            print(hint, file=sys.stderr)
        if e.posted_ids:
            print("Already posted (edit or delete these on X):", file=sys.stderr)
            for tid in e.posted_ids:
                print(f"  https://x.com/i/web/status/{tid}", file=sys.stderr)
        return 1
    except (tweepy.Unauthorized, tweepy.Forbidden, tweepy.TooManyRequests) as e:
        sys.exit(f"{_remediation_for(e)} Details: {e}")
    except tweepy.TweepyException as e:
        sys.exit(f"X API error: {e}")
    return 0


def load_credentials() -> dict[str, str]:
    load_dotenv(ENV_FILE)
    required = [
        "X_API_KEY",
        "X_API_KEY_SECRET",
        "X_ACCESS_TOKEN",
        "X_ACCESS_TOKEN_SECRET",
    ]
    missing = [k for k in required if not os.environ.get(k)]
    if missing:
        sys.exit(
            f"Missing env vars in {ENV_FILE}: {', '.join(missing)}\n"
            f"Fill them in (see .env.example)."
        )
    return {k: os.environ[k] for k in required}


def build_client(creds: dict[str, str]) -> tweepy.Client:
    return tweepy.Client(
        consumer_key=creds["X_API_KEY"],
        consumer_secret=creds["X_API_KEY_SECRET"],
        access_token=creds["X_ACCESS_TOKEN"],
        access_token_secret=creds["X_ACCESS_TOKEN_SECRET"],
    )


if __name__ == "__main__":
    raise SystemExit(main())
