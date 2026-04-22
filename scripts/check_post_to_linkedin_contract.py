#!/usr/bin/env python3
"""Contract checks for scripts/post_to_linkedin.py.

Guards against silent drift in five surfaces:
  1. Flags referenced in skills/post-to-linkedin/SKILL.md must still exist in argparse.
  2. LINKEDIN_VERSION must be <= 12 months old (LinkedIn sunsets versions ~12mo
     after release; stale values will return HTTP errors at post time).
  3. TODO-marker gate must block a real `--yes` post before token loading.
  4. escape_little_text must backslash LinkedIn's reserved characters. `#` is
     preserved unescaped so bare `#tag` renders as a hashtag; `@` IS escaped
     because a bare `@user` is not a valid mention (mentions require explicit
     `@[Name](URN)` syntax, which this script does not construct).
  5. `--dry-run` on plain text must exit 0 without requiring any LINKEDIN_* env.

Exits 0 on success, nonzero on mismatch. Wired into CI via site-checks.yml.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "post_to_linkedin.py"
SKILL = REPO / "skills" / "post-to-linkedin" / "SKILL.md"
REQUIRED_FLAGS = {"--auth", "--draft", "--dry-run", "--yes", "--media"}


def flags_in(text: str) -> set[str]:
    return set(re.findall(r"--[a-z][a-z0-9-]*", text))


def check_flags() -> list[str]:
    help_out = subprocess.run(
        [sys.executable, str(SCRIPT), "--help"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    help_flags = flags_in(help_out)
    skill_flags = flags_in(SKILL.read_text(encoding="utf-8"))
    missing = sorted((REQUIRED_FLAGS | skill_flags) - help_flags)
    if missing:
        return [f"flags in SKILL.md/REQUIRED missing from --help: {missing}"]
    return []


def check_linkedin_version() -> list[str]:
    scripts_dir = str(REPO / "scripts")
    if scripts_dir not in sys.path:
        sys.path.insert(0, scripts_dir)
    from post_to_linkedin import LINKEDIN_VERSION

    if not re.fullmatch(r"\d{6}", LINKEDIN_VERSION):
        return [
            f"LINKEDIN_VERSION format invalid: {LINKEDIN_VERSION} "
            "(expected YYYYMM, e.g. 202604)"
        ]
    year = int(LINKEDIN_VERSION[:4])
    month = int(LINKEDIN_VERSION[4:])
    try:
        version_date = date(year, month, 1)
    except ValueError:
        return [f"LINKEDIN_VERSION {LINKEDIN_VERSION} is not a valid year-month"]
    age_days = (date.today() - version_date).days
    if age_days > 365:
        return [
            f"LINKEDIN_VERSION {LINKEDIN_VERSION} is >12 months old ({age_days} days). "
            "LinkedIn deprecates versions ~12 months after release; bump to the current one "
            "(see https://learn.microsoft.com/en-us/linkedin/marketing/versioning)."
        ]
    return []


def check_todo_gate() -> list[str]:
    """A real `--yes` post whose text contains <!-- TODO --> must exit nonzero."""
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "--yes", "hello <!-- TODO: fill me in -->"],
        capture_output=True,
        text=True,
    )
    if proc.returncode == 0:
        return ["TODO-marker gate did not block a --yes post"]
    combined = proc.stdout + proc.stderr
    if "Draft still contains" not in combined:
        return [
            f"TODO-marker gate exited {proc.returncode} without the expected message. "
            f"output={combined!r}"
        ]
    return []


def check_escape_little_text() -> list[str]:
    scripts_dir = str(REPO / "scripts")
    if scripts_dir not in sys.path:
        sys.path.insert(0, scripts_dir)
    from post_to_linkedin import escape_little_text

    cases = [
        ("plain text", "plain text", "passthrough"),
        ("(a)", r"\(a\)", "parentheses escaped"),
        ("[x]", r"\[x\]", "brackets escaped"),
        ("{y}", r"\{y\}", "braces escaped"),
        ("a|b", r"a\|b", "pipe escaped"),
        ("a*b", r"a\*b", "star escaped"),
        ("a_b", r"a\_b", "underscore escaped"),
        ("a~b", r"a\~b", "tilde escaped"),
        ("<x>", r"\<x\>", "angle brackets escaped"),
        ("#AIAgents", "#AIAgents", "hashtag preserved"),
        ("@user", r"\@user", "at-sign escaped (bare @ is not a valid mention)"),
        ("a@b.com", r"a\@b.com", "at-sign in email escaped"),
        ("a\\b", r"a\\b", "backslash escaped"),
    ]
    failures: list[str] = []
    for input_text, want, label in cases:
        got = escape_little_text(input_text)
        if got != want:
            failures.append(
                f"[{label}] escape_little_text({input_text!r}): want {want!r}, got {got!r}"
            )
    return failures


def check_dry_run_no_tokens() -> list[str]:
    """--dry-run for plain text must exit 0 even with all LINKEDIN_* env vars unset."""
    env = {k: v for k, v in os.environ.items() if not k.startswith("LINKEDIN_")}
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "--dry-run", "plain text preview"],
        capture_output=True,
        text=True,
        env=env,
    )
    if proc.returncode != 0:
        return [
            f"--dry-run with no LINKEDIN_* env vars failed: exit {proc.returncode}. "
            f"stderr={proc.stderr!r}"
        ]
    return []


def check_create_post_body() -> list[str]:
    """Mock requests.post and verify /rest/posts body shapes for 0/1/N media."""
    scripts_dir = str(REPO / "scripts")
    if scripts_dir not in sys.path:
        sys.path.insert(0, scripts_dir)
    import post_to_linkedin as mod

    recorded: dict = {}

    class _Resp:
        status_code = 201
        headers = {"x-restli-id": "urn:li:share:FAKE"}

    def fake_post(url, headers=None, json=None, timeout=None, **kw):  # noqa: ANN001
        recorded["url"] = url
        recorded["headers"] = headers or {}
        recorded["json"] = json
        return _Resp()

    failures: list[str] = []
    original = mod.requests.post
    mod.requests.post = fake_post
    try:
        # Case 1: text only, escape_little_text applied, no content field
        mod.create_post("tkn", "urn:li:person:ABC", "hello (world) #tag", [])
        b = recorded["json"]
        if b.get("author") != "urn:li:person:ABC":
            failures.append(f"text-only: author wrong: {b.get('author')!r}")
        if b.get("commentary") != r"hello \(world\) #tag":
            failures.append(
                f"text-only: commentary not escaped correctly: {b.get('commentary')!r}"
            )
        if "content" in b:
            failures.append(f"text-only: unexpected content field: {b.get('content')!r}")
        for k in ("lifecycleState", "distribution", "visibility"):
            if k not in b:
                failures.append(f"text-only: body missing {k}")
        h = recorded["headers"]
        if h.get("LinkedIn-Version") != mod.LINKEDIN_VERSION:
            failures.append(
                f"text-only: LinkedIn-Version header wrong: {h.get('LinkedIn-Version')!r}"
            )
        if not h.get("Authorization", "").startswith("Bearer "):
            failures.append(f"text-only: Authorization header wrong: {h.get('Authorization')!r}")

        # Case 2: one image -> content.media.id
        recorded.clear()
        mod.create_post("tkn", "urn:li:person:ABC", "x", ["urn:li:image:1"])
        b = recorded["json"]
        media = b.get("content", {}).get("media", {})
        if media.get("id") != "urn:li:image:1":
            failures.append(f"single-image: content.media.id wrong: {b.get('content')!r}")

        # Case 3: multi-image -> content.multiImage.images
        recorded.clear()
        mod.create_post(
            "tkn", "urn:li:person:ABC", "x", ["urn:li:image:1", "urn:li:image:2"]
        )
        b = recorded["json"]
        images = b.get("content", {}).get("multiImage", {}).get("images", [])
        if len(images) != 2 or images[0].get("id") != "urn:li:image:1" or images[1].get("id") != "urn:li:image:2":
            failures.append(
                f"multi-image: content.multiImage.images wrong: {b.get('content')!r}"
            )
    finally:
        mod.requests.post = original
    return failures


def check_upload_media_contract() -> list[str]:
    """Mock initializeUpload + PUT and verify body + required headers."""
    scripts_dir = str(REPO / "scripts")
    if scripts_dir not in sys.path:
        sys.path.insert(0, scripts_dir)
    import post_to_linkedin as mod
    import tempfile

    recorded: dict = {"post_calls": [], "put_calls": []}

    class _InitResp:
        status_code = 200

        @staticmethod
        def json():
            return {
                "value": {
                    "uploadUrl": "https://pre-signed.linkedin.example/upload/abc",
                    "image": "urn:li:image:FAKE",
                }
            }

    class _PutResp:
        status_code = 201

    def fake_post(url, headers=None, json=None, timeout=None, **kw):  # noqa: ANN001
        recorded["post_calls"].append({"url": url, "headers": headers or {}, "json": json})
        return _InitResp()

    def fake_put(url, data=None, headers=None, timeout=None, **kw):  # noqa: ANN001
        # Drain data without fully reading, just to avoid pickling issues.
        if hasattr(data, "read"):
            data.read()
        recorded["put_calls"].append({"url": url, "headers": headers or {}})
        return _PutResp()

    failures: list[str] = []
    original_post = mod.requests.post
    original_put = mod.requests.put
    mod.requests.post = fake_post
    mod.requests.put = fake_put
    try:
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
            tmp.write(b"\x89PNG\r\n\x1a\n" + b"0" * 32)
            tmp_path = Path(tmp.name)
        try:
            urns = mod.upload_media("tkn", "urn:li:person:ABC", [tmp_path])
        finally:
            tmp_path.unlink(missing_ok=True)

        if urns != ["urn:li:image:FAKE"]:
            failures.append(f"upload_media: returned urns wrong: {urns!r}")

        if not recorded["post_calls"]:
            failures.append("upload_media: no initializeUpload call recorded")
        else:
            init = recorded["post_calls"][0]
            want_body = {"initializeUploadRequest": {"owner": "urn:li:person:ABC"}}
            if init["json"] != want_body:
                failures.append(f"upload_media: init body wrong: {init['json']!r}")
            h = init["headers"]
            for k in ("Authorization", "LinkedIn-Version", "X-Restli-Protocol-Version", "Content-Type"):
                if k not in h:
                    failures.append(f"upload_media: init missing header {k}")

        if not recorded["put_calls"]:
            failures.append("upload_media: no PUT upload call recorded")
        else:
            put = recorded["put_calls"][0]
            if put["url"] != "https://pre-signed.linkedin.example/upload/abc":
                failures.append(f"upload_media: PUT url wrong: {put['url']!r}")
            if not put["headers"].get("Authorization", "").startswith("Bearer "):
                failures.append(
                    f"upload_media: PUT missing Authorization header: {put['headers']!r}"
                )
    finally:
        mod.requests.post = original_post
        mod.requests.put = original_put
    return failures


def main() -> int:
    failures = (
        check_flags()
        + check_linkedin_version()
        + check_todo_gate()
        + check_escape_little_text()
        + check_dry_run_no_tokens()
        + check_create_post_body()
        + check_upload_media_contract()
    )
    if failures:
        for f in failures:
            print(f"FAIL: {f}", file=sys.stderr)
        return 1
    print("OK: post_to_linkedin contract checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
