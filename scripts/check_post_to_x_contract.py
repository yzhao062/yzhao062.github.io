#!/usr/bin/env python3
"""Contract checks for scripts/post_to_x.py.

Guards against silent drift in four surfaces:
  1. Flags referenced in skills/post-to-x/SKILL.md must still exist in argparse.
  2. URL-aware character count on known edge cases.
  3. TODO-marker gate must block a real `--yes` post before credential loading.
  4. ThreadError must carry already-posted tweet IDs and preserve the cause.

Exits 0 on success, nonzero on mismatch. Wired into CI via site-checks.yml.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "post_to_x.py"
SKILL = REPO / "skills" / "post-to-x" / "SKILL.md"
REQUIRED_FLAGS = {"--draft", "--project", "--dry-run", "--thread", "--yes"}


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
        return [f"flags in SKILL.md / REQUIRED missing from --help: {missing}"]
    return []


def check_char_count() -> list[str]:
    sys.path.insert(0, str(REPO / "scripts"))
    from post_to_x import effective_char_count, cost_for, COST_WITH_URL, COST_NO_URL

    cases = [
        # (text, expected_chars, expected_has_url, label)
        ("hello", 5, False, "plain text, no URL"),
        ("https://github.com/yzhao062/pyod", 23, True, "bare URL counts as 23"),
        ("see https://example.com/path.", len("see ") + 23 + 1, True,
         "trailing period stays outside URL"),
        ("(https://example.com)", 1 + 23 + 1, True,
         "trailing paren stays outside URL"),
        ("foo bar", 7, False, "space not counted as URL"),
        ("https://a.com and https://b.com", 23 + 5 + 23, True,
         "two URLs both replaced"),
        ("https://example.com/a(b)", 24, True,
         "balanced paren trimmed (documented; percent-encode for exact count)"),
    ]
    failures: list[str] = []
    for text, want_chars, want_url, label in cases:
        got_chars = effective_char_count(text)
        got_cost, got_has_url = cost_for(text)
        want_cost = COST_WITH_URL if want_url else COST_NO_URL
        if got_chars != want_chars:
            failures.append(
                f"[{label}] chars: want {want_chars}, got {got_chars} "
                f"for text={text!r}"
            )
        if got_has_url != want_url or abs(got_cost - want_cost) > 1e-9:
            failures.append(
                f"[{label}] url/cost: want ({want_url}, {want_cost}), "
                f"got ({got_has_url}, {got_cost}) for text={text!r}"
            )
    return failures


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
        return [f"TODO-marker gate exited {proc.returncode} but without the expected message. output={combined!r}"]
    return []


def check_thread_error() -> list[str]:
    """post_thread must raise ThreadError carrying posted IDs, preserving cause."""
    scripts_dir = str(REPO / "scripts")
    if scripts_dir not in sys.path:
        sys.path.insert(0, scripts_dir)
    from post_to_x import post_thread, ThreadError
    import tweepy

    class _FakeClient:
        calls = 0

        def create_tweet(self, **kwargs):
            _FakeClient.calls += 1
            if _FakeClient.calls == 1:
                class _Resp:
                    data = {"id": "11111"}
                return _Resp()
            raise tweepy.TweepyException("fake failure on part 2")

    try:
        post_thread(_FakeClient(), ["first", "second"])
    except ThreadError as e:
        failures: list[str] = []
        if e.posted_ids != ["11111"]:
            failures.append(f"ThreadError.posted_ids wrong: {e.posted_ids!r}")
        if not isinstance(e.__cause__, tweepy.TweepyException):
            failures.append(
                f"ThreadError did not preserve cause: {type(e.__cause__).__name__}"
            )
        return failures
    return ["ThreadError was not raised when fake client failed on part 2"]


def main() -> int:
    failures = (
        check_flags()
        + check_char_count()
        + check_todo_gate()
        + check_thread_error()
    )
    if failures:
        for f in failures:
            print(f"FAIL: {f}", file=sys.stderr)
        return 1
    print("OK: post_to_x contract checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
