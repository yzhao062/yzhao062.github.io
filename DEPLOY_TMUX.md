# Server Deploy Runbook

Deploys go to USC `viterbi-scf01.vlab.usc.edu`, served from `~/public_html` via Apache.
The mechanism is **cron + flock + Healthchecks.io ping**, not tmux. The filename is
kept for backwards compatibility; see "Migration History" at the bottom.

## Architecture

```
laptop (this repo)
  │  scripts/server_ssh.py            (daily ops)
  │  scripts/apply_robustness_layer12.py  (one-time / re-apply / new machine)
  ▼
viterbi-scf01.vlab.usc.edu (behind USC VPN)
  │
  ├── crond runs */30 minute → /usr/bin/flock -n ~/.deploy_site.lock ~/deploy_site.sh
  │     └── git fetch + reset --hard origin/main on ~/site_repo
  │     └── rsync --delete ~/site_repo → ~/public_html (excluding .git, .github)
  │     └── /start ping at begin, success ping at clean exit, /fail ping on error
  │
  └── ~/.deploy.env (chmod 600) holds HEALTHCHECK_URL
```

Local credentials live in `.env` (gitignored): `DEPLOY_HOST`, `DEPLOY_USER`, and
optional `DEPLOY_PASS`. The Python helpers connect via `paramiko`; they use
`DEPLOY_PASS` when set and otherwise fall back to SSH key auth after
`scripts/setup_usc_deploy_key.sh` has installed your key.

## Daily Check

From the laptop, check both sides at once:

```bash
python scripts/server_ssh.py 'crontab -l; echo ---; tail -10 ~/deploy_logs/deploy_$(date +%F).log'
```

Or visit <https://healthchecks.io>. The check **USC viterbi-scf01 site deploy** should
be green; "Last Duration" tells you how long the most recent deploy took (typically a
few seconds in steady state, larger when many files changed).

## Alerts

Healthchecks.io sends email to your registered address when:

- No successful ping arrives within 40 minutes (Period 30m + Grace 10m), OR
- The deploy script exits non-zero (the `trap finalize EXIT` sends `/fail` immediately,
  so you do not wait the full 40 minutes for known failures).

If alerts stop arriving, check that the bell icon on the Healthchecks.io row is not
"Snoozed", and that Email is enabled both at the account level and on the specific
check (per-check integration is independent of the global toggle).

## Manual Operations

Force a deploy now (does not affect cron schedule):

```bash
python scripts/server_ssh.py 'bash ~/deploy_site.sh && tail -5 ~/deploy_logs/deploy_$(date +%F).log'
```

Read the current crontab:

```bash
python scripts/server_ssh.py 'crontab -l'
```

Inspect today's log:

```bash
python scripts/server_ssh.py 'cat ~/deploy_logs/deploy_$(date +%F).log'
```

## Recovery and Fresh-Machine Setup

If the deploy server changes, your account is reset, or any of the wiring is lost,
re-apply Layer 1 + Layer 2 in one shot. The script is idempotent:

```bash
# 1. Make sure DEPLOY_HOST / DEPLOY_USER are set in .env; set DEPLOY_PASS only if not using key auth
# 2. Re-apply (replace the URL with your healthchecks.io ping URL):
python scripts/apply_robustness_layer12.py 'https://hc-ping.com/<your-uuid>'
```

Optional, eliminates the password from `.env` permanently:

```bash
bash scripts/setup_usc_deploy_key.sh
```

`setup_usc_deploy_key.sh` pushes `~/.ssh/id_ed25519.pub` to the server's
`authorized_keys` and adds an `usc-deploy` entry to `~/.ssh/config`. The Python
helpers (`server_ssh.py`, `apply_robustness_layer12.py`) connect with
`look_for_keys=True` and treat an empty `DEPLOY_PASS` as "use the SSH key in
`~/.ssh/`", so after the bootstrap you can clear `DEPLOY_PASS=` in `.env` and
rely on the key.

## Backup and Rollback

`apply_robustness_layer12.py` backs up `~/deploy_site.sh` to
`~/deploy_site.sh.bak.<unix-timestamp>` before each patch. To roll back:

```bash
# 1. Find the most recent backup
python scripts/server_ssh.py 'ls -t ~/deploy_site.sh.bak.* | head -3'

# 2. Restore (substitute the timestamp you want)
python scripts/server_ssh.py 'cp -p ~/deploy_site.sh.bak.<TS> ~/deploy_site.sh'

# 3. Remove the cron entry
python scripts/server_ssh.py "crontab -l | grep -v deploy_site.sh | crontab -"
```

If healthchecks.io itself is the problem (false alerts, account issues), comment
out the `[ -f "$HOME/.deploy.env" ]` source line in `~/deploy_site.sh` to disable
pings without removing the wiring.

## Migration History

Earlier versions of this file described a tmux session running
`while true; do ~/deploy_site.sh; sleep 30m; done` inside a session named
`deploy_loop`. That model had four silent failure modes:

1. logout killed the session
2. server reboot did not restart it
3. accidental `kill` left no trace
4. `deploy_site.sh` exit codes were ignored, so a broken deploy looked identical
   to a healthy one until the site went stale

The cron + Healthchecks.io approach above addresses all four. The tmux flow is
preserved in git history before the commit that introduced this rewrite; check
`git log -- DEPLOY_TMUX.md` if you ever want it back for debugging.
