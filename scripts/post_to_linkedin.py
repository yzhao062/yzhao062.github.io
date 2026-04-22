#!/usr/bin/env python3
"""Post announcements to LinkedIn from the command line.

Usage
-----
  python scripts/post_to_linkedin.py --auth                         # one-time OAuth
  python scripts/post_to_linkedin.py --dry-run --draft <path>
  python scripts/post_to_linkedin.py --yes --draft <path>
  python scripts/post_to_linkedin.py --yes --draft <path> --media img1.png --media img2.png

Setup
-----
  pip install -r scripts/requirements-post.txt
  Add to .env: LINKEDIN_CLIENT_ID=..., LINKEDIN_CLIENT_SECRET=...
  Run --auth once; tokens and user URN are written back to .env automatically.
  Requires the LinkedIn app to have 'Share on LinkedIn' and
  'Sign In with LinkedIn using OpenID Connect' products approved.
"""

from __future__ import annotations

import argparse
import http.server
import os
import secrets
import socketserver
import sys
import threading
import time
import urllib.parse
import webbrowser
from pathlib import Path

import requests
from dotenv import load_dotenv, set_key

REPO_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = REPO_ROOT / ".env"

POST_CHAR_LIMIT = 3000
TODO_MARKER = "<!-- TODO"
OAUTH_REDIRECT_HOST = "localhost"
OAUTH_REDIRECT_PORT = 8765
OAUTH_REDIRECT_URL = f"http://{OAUTH_REDIRECT_HOST}:{OAUTH_REDIRECT_PORT}/callback"
OAUTH_SCOPES = "openid profile email w_member_social"

LINKEDIN_AUTH_URL = "https://www.linkedin.com/oauth/v2/authorization"
LINKEDIN_TOKEN_URL = "https://www.linkedin.com/oauth/v2/accessToken"
LINKEDIN_USERINFO_URL = "https://api.linkedin.com/v2/userinfo"
LINKEDIN_POSTS_URL = "https://api.linkedin.com/rest/posts"
LINKEDIN_IMAGES_INIT_URL = (
    "https://api.linkedin.com/rest/images?action=initializeUpload"
)
LINKEDIN_VERSION = "202604"


# LinkedIn "little" text format reserved characters. Backslash-escape these in
# `commentary` to keep them as literal text. `#` is left unescaped because a
# bare `#tag` is the valid hashtag form. `@` IS escaped because a bare `@user`
# is not a valid mention on its own; real mentions use `@[Name](urn:li:person:id)`
# syntax, which this script does not construct. If real mention support is
# added later, it must bypass escape_little_text for the mention span.
_LITTLE_RESERVED = set("\\|{}[]()<>*_~@")


def escape_little_text(text: str) -> str:
    """Escape LinkedIn Little-format reserved characters. `#` is preserved."""
    out: list[str] = []
    for ch in text:
        if ch in _LITTLE_RESERVED:
            out.append("\\" + ch)
        else:
            out.append(ch)
    return "".join(out)


def _env_get(key: str) -> str:
    return os.environ.get(key, "").strip()


def _env_set(key: str, value: str) -> None:
    """Write key=value back to .env and refresh os.environ."""
    ENV_FILE.touch(exist_ok=True)
    set_key(str(ENV_FILE), key, value)
    os.environ[key] = value


class _OAuthHandler(http.server.BaseHTTPRequestHandler):
    code_holder: dict[str, str] = {}

    def do_GET(self):  # noqa: N802
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path != "/callback":
            self.send_response(404)
            self.end_headers()
            return
        params = urllib.parse.parse_qs(parsed.query)
        if "error" in params:
            msg = (
                f"{params.get('error', [''])[0]}: "
                f"{params.get('error_description', [''])[0]}"
            )
            _OAuthHandler.code_holder["error"] = msg
            self._respond(f"<h1>Authorization failed</h1><p>{msg}</p>")
            return
        _OAuthHandler.code_holder["code"] = params.get("code", [""])[0]
        _OAuthHandler.code_holder["state"] = params.get("state", [""])[0]
        self._respond(
            "<h1>Authorized.</h1><p>You can close this tab and return to the "
            "terminal.</p>"
        )

    def _respond(self, html: str) -> None:
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def log_message(self, format, *args):  # noqa: A002
        pass


def run_oauth_flow() -> None:
    """Interactive OAuth 2.0 3-legged flow. Writes tokens + user URN to .env."""
    load_dotenv(ENV_FILE)
    client_id = _env_get("LINKEDIN_CLIENT_ID")
    client_secret = _env_get("LINKEDIN_CLIENT_SECRET")
    if not client_id or not client_secret:
        sys.exit(
            "Set LINKEDIN_CLIENT_ID and LINKEDIN_CLIENT_SECRET in .env first.\n"
            "Get these from https://developer.linkedin.com -> your app -> Auth."
        )

    state = secrets.token_urlsafe(24)
    auth_url = f"{LINKEDIN_AUTH_URL}?" + urllib.parse.urlencode(
        {
            "response_type": "code",
            "client_id": client_id,
            "redirect_uri": OAUTH_REDIRECT_URL,
            "state": state,
            "scope": OAUTH_SCOPES,
        }
    )

    _OAuthHandler.code_holder = {}
    try:
        server = socketserver.TCPServer(
            (OAUTH_REDIRECT_HOST, OAUTH_REDIRECT_PORT), _OAuthHandler
        )
    except OSError as exc:
        sys.exit(
            f"Could not bind to port {OAUTH_REDIRECT_PORT}: {exc}. "
            "Close whatever is using that port, or change OAUTH_REDIRECT_PORT "
            "in the script and in the LinkedIn app Authorized redirect URLs."
        )

    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    print("Opening browser for LinkedIn authorization...")
    print(f"If it does not open, visit: {auth_url}")
    try:
        webbrowser.open(auth_url)
    except Exception:  # noqa: BLE001
        pass

    deadline = time.time() + 300  # 5 min
    while time.time() < deadline:
        if _OAuthHandler.code_holder:
            break
        time.sleep(0.2)

    server.shutdown()
    server.server_close()

    if "error" in _OAuthHandler.code_holder:
        sys.exit(f"LinkedIn OAuth error: {_OAuthHandler.code_holder['error']}")
    code = _OAuthHandler.code_holder.get("code", "")
    if not code:
        sys.exit("Timed out waiting for LinkedIn redirect.")
    if _OAuthHandler.code_holder.get("state") != state:
        sys.exit("State mismatch in OAuth callback; aborting (possible CSRF).")

    resp = requests.post(
        LINKEDIN_TOKEN_URL,
        data={
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": OAUTH_REDIRECT_URL,
            "client_id": client_id,
            "client_secret": client_secret,
        },
        timeout=30,
    )
    if resp.status_code != 200:
        sys.exit(f"Token exchange failed ({resp.status_code}): {resp.text}")
    td = resp.json()
    access_token = td["access_token"]
    refresh_token = td.get("refresh_token", "")
    expires_in = int(td.get("expires_in", 5184000))
    expires_at = int(time.time()) + expires_in

    userinfo_resp = requests.get(
        LINKEDIN_USERINFO_URL,
        headers={"Authorization": f"Bearer {access_token}"},
        timeout=30,
    )
    if userinfo_resp.status_code != 200:
        sys.exit(
            f"userinfo call failed ({userinfo_resp.status_code}): {userinfo_resp.text}"
        )
    userinfo = userinfo_resp.json()
    user_urn = f"urn:li:person:{userinfo['sub']}"

    _env_set("LINKEDIN_ACCESS_TOKEN", access_token)
    _env_set("LINKEDIN_REFRESH_TOKEN", refresh_token)
    _env_set("LINKEDIN_TOKEN_EXPIRES_AT", str(expires_at))
    _env_set("LINKEDIN_USER_URN", user_urn)

    print(
        f"Auth complete. Logged in as {userinfo.get('name', '?')} "
        f"({user_urn})."
    )
    print(
        "Access token expires at "
        f"{time.strftime('%Y-%m-%d %H:%M', time.localtime(expires_at))}."
    )
    if refresh_token:
        print("Refresh token stored; auto-refresh on next post.")
    else:
        print("No refresh token returned; re-run --auth when token expires.")


def ensure_fresh_token() -> str:
    """Return a valid access token, refreshing via refresh_token if close to expiry."""
    load_dotenv(ENV_FILE)
    access_token = _env_get("LINKEDIN_ACCESS_TOKEN")
    if not access_token:
        sys.exit(
            "No LINKEDIN_ACCESS_TOKEN in .env. "
            "Run: python scripts/post_to_linkedin.py --auth"
        )

    expires_at_str = _env_get("LINKEDIN_TOKEN_EXPIRES_AT")
    expires_at = int(expires_at_str) if expires_at_str.isdigit() else 0
    if expires_at and int(time.time()) < expires_at - 3600:
        return access_token

    refresh_token = _env_get("LINKEDIN_REFRESH_TOKEN")
    if not refresh_token:
        sys.exit(
            "Access token expired and no LINKEDIN_REFRESH_TOKEN in .env. "
            "Re-run: python scripts/post_to_linkedin.py --auth"
        )

    client_id = _env_get("LINKEDIN_CLIENT_ID")
    client_secret = _env_get("LINKEDIN_CLIENT_SECRET")
    resp = requests.post(
        LINKEDIN_TOKEN_URL,
        data={
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": client_id,
            "client_secret": client_secret,
        },
        timeout=30,
    )
    if resp.status_code != 200:
        sys.exit(
            f"Refresh failed ({resp.status_code}): {resp.text}. "
            "Re-auth with --auth."
        )
    td = resp.json()
    access_token = td["access_token"]
    new_refresh = td.get("refresh_token", refresh_token)
    expires_in = int(td.get("expires_in", 5184000))
    expires_at = int(time.time()) + expires_in

    _env_set("LINKEDIN_ACCESS_TOKEN", access_token)
    _env_set("LINKEDIN_REFRESH_TOKEN", new_refresh)
    _env_set("LINKEDIN_TOKEN_EXPIRES_AT", str(expires_at))
    print(
        "Token refreshed. Expires at "
        f"{time.strftime('%Y-%m-%d %H:%M', time.localtime(expires_at))}."
    )
    return access_token


def upload_media(access_token: str, user_urn: str, paths: list[Path]) -> list[str]:
    """Upload media files via the 3-step flow. Returns image URNs."""
    urns: list[str] = []
    headers_json = {
        "Authorization": f"Bearer {access_token}",
        "LinkedIn-Version": LINKEDIN_VERSION,
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json",
    }
    for path in paths:
        init_resp = requests.post(
            LINKEDIN_IMAGES_INIT_URL,
            headers=headers_json,
            json={"initializeUploadRequest": {"owner": user_urn}},
            timeout=30,
        )
        if init_resp.status_code not in (200, 201):
            sys.exit(
                f"Media init failed ({init_resp.status_code}): {init_resp.text}"
            )
        value = init_resp.json()["value"]
        upload_url = value["uploadUrl"]
        image_urn = value["image"]

        with open(path, "rb") as f:
            put_resp = requests.put(
                upload_url,
                data=f,
                headers={"Authorization": f"Bearer {access_token}"},
                timeout=120,
            )
        if put_resp.status_code not in (200, 201):
            sys.exit(
                f"Media PUT failed for {path} ({put_resp.status_code}): "
                f"{put_resp.text}"
            )
        urns.append(image_urn)
        print(f"Uploaded: {path.name} -> {image_urn}")
    return urns


def create_post(
    access_token: str,
    user_urn: str,
    text: str,
    media_urns: list[str],
) -> str:
    """POST /rest/posts. Returns the post URN (urn:li:share:... or urn:li:ugcPost:...)."""
    body: dict[str, object] = {
        "author": user_urn,
        "commentary": escape_little_text(text),
        "visibility": "PUBLIC",
        "distribution": {
            "feedDistribution": "MAIN_FEED",
            "targetEntities": [],
            "thirdPartyDistributionChannels": [],
        },
        "lifecycleState": "PUBLISHED",
        "isReshareDisabledByAuthor": False,
    }
    if len(media_urns) == 1:
        body["content"] = {"media": {"id": media_urns[0], "altText": ""}}
    elif len(media_urns) > 1:
        body["content"] = {
            "multiImage": {
                "images": [{"id": urn, "altText": ""} for urn in media_urns]
            }
        }

    resp = requests.post(
        LINKEDIN_POSTS_URL,
        headers={
            "Authorization": f"Bearer {access_token}",
            "LinkedIn-Version": LINKEDIN_VERSION,
            "X-Restli-Protocol-Version": "2.0.0",
            "Content-Type": "application/json",
        },
        json=body,
        timeout=30,
    )
    if resp.status_code not in (200, 201):
        sys.exit(f"Post failed ({resp.status_code}): {resp.text}")
    return resp.headers.get("x-restli-id", "")


def preview(text: str, media_paths: list[Path]) -> None:
    print("=" * 64)
    print(f"Post preview ({len(text)} chars, limit {POST_CHAR_LIMIT:,}):")
    print()
    print(text)
    print()
    print("=" * 64)
    if media_paths:
        print(f"Media attachments ({len(media_paths)}):")
        for p in media_paths:
            kb = p.stat().st_size / 1024
            print(f"  - {p} ({kb:,.1f} KB)")
    print("LinkedIn API posts are free (no per-post charge).")


def resolve_content(args: argparse.Namespace) -> str:
    if args.text is not None:
        return args.text.strip()
    if args.draft is not None:
        if not args.draft.exists():
            sys.exit(f"Draft not found: {args.draft}")
        return args.draft.read_text(encoding="utf-8").strip()
    sys.exit("Provide inline text or --draft.")


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Post to LinkedIn from the command line.")
    ap.add_argument("text", nargs="?", help="Inline post text")
    ap.add_argument("--draft", type=Path, help="Path to a text or markdown file to post")
    ap.add_argument(
        "--auth",
        action="store_true",
        help="Run the interactive OAuth flow to get access + refresh tokens",
    )
    ap.add_argument("--dry-run", action="store_true", help="Preview only, do not post")
    ap.add_argument("--yes", action="store_true", help="Skip confirmation prompt")
    ap.add_argument(
        "--media",
        type=Path,
        action="append",
        default=[],
        help="Attach image (repeatable; up to 20 per post on LinkedIn)",
    )
    return ap.parse_args()


def confirm(prompt: str = "Post now? (y/n): ") -> bool:
    try:
        return input(prompt).strip().lower() in {"y", "yes"}
    except (EOFError, KeyboardInterrupt):
        return False


def main() -> int:
    args = parse_args()

    if args.auth:
        run_oauth_flow()
        return 0

    sources = sum(x is not None for x in (args.text, args.draft))
    if sources != 1:
        sys.exit("Provide exactly one of: inline text or --draft.")

    text = resolve_content(args)
    if len(text) > POST_CHAR_LIMIT:
        sys.exit(f"Post is {len(text)} chars, exceeds {POST_CHAR_LIMIT:,} limit.")

    media_paths: list[Path] = list(args.media)
    if len(media_paths) > 20:
        sys.exit(
            f"--media: {len(media_paths)} files; LinkedIn allows at most 20 per post."
        )
    for p in media_paths:
        if not p.exists():
            sys.exit(f"Media file not found: {p}")

    has_todo = TODO_MARKER in text
    preview(text, media_paths)
    if has_todo and not args.dry_run:
        sys.exit(
            f"Draft still contains '{TODO_MARKER}' markers. Remove them before posting."
        )
    if has_todo and args.dry_run:
        print(
            f"WARNING: draft contains '{TODO_MARKER}' markers. "
            "Remove them before a real post."
        )

    if args.dry_run:
        print("Dry run. Nothing posted.")
        return 0

    if not args.yes and not confirm():
        print("Cancelled.")
        return 0

    access_token = ensure_fresh_token()
    user_urn = _env_get("LINKEDIN_USER_URN")
    if not user_urn:
        sys.exit("LINKEDIN_USER_URN missing from .env; run --auth first.")

    media_urns = upload_media(access_token, user_urn, media_paths) if media_paths else []
    post_urn = create_post(access_token, user_urn, text, media_urns)

    if post_urn:
        print(f"Posted. URN: {post_urn}")
        print(f"View: https://www.linkedin.com/feed/update/{post_urn}/")
    else:
        print("Posted, but no URN returned. Check your LinkedIn feed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
