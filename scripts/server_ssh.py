#!/usr/bin/env python3
"""Run a shell command on the USC deploy server (viterbi-scf01) over SSH.

Reads DEPLOY_HOST / DEPLOY_USER from the repo-local .env file. DEPLOY_PASS is
optional; when empty, paramiko's allow_agent + look_for_keys fall back to the
SSH key in ~/.ssh/ (run scripts/setup_usc_deploy_key.sh first to install it).
Connects with paramiko, executes the given command, and streams stdout/stderr.

Usage:
    python scripts/server_ssh.py 'crontab -l'
    python scripts/server_ssh.py 'tail -20 ~/deploy_logs/deploy_$(date +%F).log'
    python scripts/server_ssh.py 'bash ~/deploy_site.sh'

Exit code mirrors the remote command's exit code. The password is never
written to disk by this script and is not echoed.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import paramiko
from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = REPO_ROOT / ".env"


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: server_ssh.py <remote-command>", file=sys.stderr)
        return 2

    remote_cmd = " ".join(argv[1:])

    if not ENV_PATH.exists():
        print(f"ERROR: {ENV_PATH} not found", file=sys.stderr)
        return 1
    load_dotenv(ENV_PATH, override=True)

    host = os.environ.get("DEPLOY_HOST", "").strip()
    user = os.environ.get("DEPLOY_USER", "").strip()
    password = os.environ.get("DEPLOY_PASS", "").strip()
    if not (host and user):
        print("ERROR: DEPLOY_HOST / DEPLOY_USER must be set in .env",
              file=sys.stderr)
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

    try:
        client.connect(**connect_kwargs)
    except paramiko.AuthenticationException as exc:
        print(f"AUTH FAILED: {exc}", file=sys.stderr)
        return 3
    except Exception as exc:
        print(f"CONNECT FAILED: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 4

    try:
        stdin, stdout, stderr = client.exec_command(remote_cmd, timeout=60)
        stdin.close()
        out = stdout.read().decode(errors="replace")
        err = stderr.read().decode(errors="replace")
        rc = stdout.channel.recv_exit_status()
        if out:
            sys.stdout.write(out)
            if not out.endswith("\n"):
                sys.stdout.write("\n")
        if err:
            sys.stderr.write(err)
            if not err.endswith("\n"):
                sys.stderr.write("\n")
        return rc
    finally:
        client.close()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
