#!/usr/bin/env python3
"""Apply Layer 1 (cron + flock) and Layer 2 (Healthchecks.io ping) to USC deploy server.

Run once after registering a Healthchecks.io check. Idempotent.

Usage:
    python scripts/apply_robustness_layer12.py https://hc-ping.com/<UUID>

Reads DEPLOY_HOST / DEPLOY_USER from .env. DEPLOY_PASS is optional; when
empty, the helper falls back to SSH key auth via paramiko's allow_agent +
look_for_keys (run scripts/setup_usc_deploy_key.sh first to install the key).
Backs up ~/deploy_site.sh on the server before modifying it (keeps the latest
BACKUP_KEEP backups). Only writes user-level state (~/deploy_site.sh,
~/.deploy.env, the user's crontab).
"""

from __future__ import annotations

import os
import sys
import time
from pathlib import Path

import paramiko
from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parents[1]

WIRING_BEGIN = "# >>> apply_robustness_layer12.py managed wiring (do not edit between markers)"
WIRING_END = "# <<< apply_robustness_layer12.py managed wiring"

_WIRING_BODY = """\
[ -f "$HOME/.deploy.env" ] && source "$HOME/.deploy.env"
ping_hc() {
  [ -n "${HEALTHCHECK_URL:-}" ] || return 0
  curl -fsS -m 10 --retry 2 -o /dev/null "${HEALTHCHECK_URL}${1:-}" || true
}
finalize() {
  local rc=$?
  if [ $rc -eq 0 ]; then ping_hc; else ping_hc "/fail"; fi
}
trap finalize EXIT
ping_hc "/start"
"""

WIRING = WIRING_BEGIN + "\n" + _WIRING_BODY + WIRING_END + "\n"

CRON_MARKER = "# managed-by yzhao062.github.io apply_robustness_layer12.py"
CRON_LINE = (
    "*/30 * * * * /usr/bin/flock -n $HOME/.deploy_site.lock "
    "$HOME/deploy_site.sh >/dev/null 2>&1 "
    f"{CRON_MARKER}"
)
BACKUP_KEEP = 5


def run(client: paramiko.SSHClient, cmd: str, *, check: bool = True) -> tuple[int, str, str]:
    stdin, stdout, stderr = client.exec_command(cmd, timeout=60)
    out = stdout.read().decode(errors="replace")
    err = stderr.read().decode(errors="replace")
    rc = stdout.channel.recv_exit_status()
    if check and rc != 0:
        raise RuntimeError(
            f"remote command failed (rc={rc}): {cmd}\nstdout:\n{out}\nstderr:\n{err}"
        )
    return rc, out, err


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: apply_robustness_layer12.py <healthcheck-url>", file=sys.stderr)
        return 2
    hc_url = argv[1].strip()
    if not hc_url.startswith("https://hc-ping.com/"):
        print("ERROR: URL must start with https://hc-ping.com/", file=sys.stderr)
        return 2

    load_dotenv(REPO_ROOT / ".env", override=True)
    host = os.environ.get("DEPLOY_HOST", "").strip()
    user = os.environ.get("DEPLOY_USER", "").strip()
    password = os.environ.get("DEPLOY_PASS", "").strip()
    if not (host and user):
        print("ERROR: DEPLOY_HOST / DEPLOY_USER must be set in .env", file=sys.stderr)
        return 1

    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    connect_kwargs: dict = dict(
        hostname=host,
        username=user,
        timeout=20,
        auth_timeout=20,
        allow_agent=True,
        look_for_keys=True,
    )
    if password:
        connect_kwargs["password"] = password
    client.connect(**connect_kwargs)

    try:
        sftp = client.open_sftp()
        try:
            home = sftp.normalize(".")
            deploy_path = f"{home}/deploy_site.sh"
            env_path = f"{home}/.deploy.env"

            print(f"[1/6] Reading {deploy_path}")
            with sftp.open(deploy_path, "r") as f:
                original = f.read().decode()

            backup_path = f"{deploy_path}.bak.{int(time.time())}"
            print(f"[2/6] Backing up -> {backup_path}")
            run(client, f"cp -p '{deploy_path}' '{backup_path}'")
            run(
                client,
                f"ls -1t '{deploy_path}.bak.'* 2>/dev/null "
                f"| tail -n +{BACKUP_KEEP + 1} | xargs -r rm -f --",
                check=False,
            )

            print("[3/6] Patching deploy_site.sh")
            if WIRING_BEGIN in original and WIRING_END in original:
                pre, _, rest = original.partition(WIRING_BEGIN)
                _, _, post = rest.partition(WIRING_END + "\n")
                new_content = pre + WIRING + post
                print("      (managed wiring re-applied via markers)")
            elif "ping_hc" in original:
                raise RuntimeError(
                    "deploy_site.sh contains Healthchecks-style wiring (ping_hc) "
                    "but no managed markers. This usually means the script was "
                    "patched by an earlier version of apply_robustness_layer12.py "
                    "or by hand. To migrate, on the server restore the most recent "
                    f"{deploy_path}.bak.<unix> and re-run this script."
                )
            else:
                marker = "set -euo pipefail\n"
                if marker not in original:
                    raise RuntimeError(
                        "could not find 'set -euo pipefail' anchor in deploy_site.sh; "
                        "review the file manually"
                    )
                new_content = original.replace(marker, marker + "\n" + WIRING, 1)
                print("      (wiring inserted)")

            if new_content != original:
                with sftp.open(deploy_path, "w") as f:
                    f.write(new_content)
                sftp.chmod(deploy_path, 0o755)

            run(client, f"bash -n '{deploy_path}'")  # syntax-check the result

            print(f"[4/6] Writing {env_path}")
            with sftp.open(env_path, "w") as f:
                f.write(f"HEALTHCHECK_URL={hc_url}\n")
            sftp.chmod(env_path, 0o600)
        finally:
            sftp.close()

        print("[5/6] Installing crontab entry")
        _, out, _ = run(client, "crontab -l 2>/dev/null || true", check=False)
        existing_lines = out.splitlines()
        kept_lines = [
            line for line in existing_lines
            if "deploy_site.sh" not in line and CRON_MARKER not in line
        ]
        desired_lines = kept_lines + [CRON_LINE]
        if existing_lines == desired_lines:
            print("      (managed deploy cron already current)")
        else:
            new_crontab = "\n".join(desired_lines) + "\n"
            stdin, stdout, stderr = client.exec_command("crontab -", timeout=30)
            stdin.write(new_crontab)
            stdin.flush()
            stdin.channel.shutdown_write()
            crc = stdout.channel.recv_exit_status()
            if crc != 0:
                err = stderr.read().decode(errors="replace")
                raise RuntimeError(f"crontab install failed (rc={crc}): {err}")
            print("      (installed managed deploy cron)")

        print("[6/6] Cleaning up any leftover tmux deploy_loop")
        run(client, "tmux kill-session -t deploy_loop 2>/dev/null || true", check=False)

        print("\n=== final state ===")
        for cmd in (
            "crontab -l",
            "ls -la ~/.deploy.env",
            "echo '---'; head -20 ~/deploy_site.sh",
        ):
            _, out, err = run(client, cmd, check=False)
            print(f"\n$ {cmd}")
            print(out.rstrip())
            if err.strip():
                print(f"(stderr) {err.rstrip()}")
    finally:
        client.close()

    print("\nDone. Verify with:")
    print("  1. python scripts/server_ssh.py 'bash ~/deploy_site.sh'   # manual deploy + ping")
    print("  2. Check Healthchecks.io dashboard for the start+success ping pair")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
