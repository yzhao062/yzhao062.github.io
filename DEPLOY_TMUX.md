# Server Deploy with tmux (30 min)

This is the simplest deployment loop for the campus/VPN server setup.

## Start / Restart the Loop

```bash
tmux kill-session -t deploy_loop 2>/dev/null || true
tmux new -d -s deploy_loop 'while true; do ~/deploy_site.sh; sleep 30m; done'
tmux ls
```

Expected output contains:

```text
deploy_loop: 1 windows
```

## Check What Is Running

```bash
tmux ls
tmux list-panes -t deploy_loop -F '#S:#I.#P #{pane_current_command} | #{pane_start_command}'
```

To attach and inspect live output:

```bash
tmux attach -t deploy_loop
```

Detach without stopping:

- Press `Ctrl+b`, then `d`

## Confirm Recent Deploy

```bash
grep "Deploy started" ~/deploy_logs/deploy_$(date +'%Y-%m-%d').log | tail -n 3
```

## Stop the Loop

```bash
tmux kill-session -t deploy_loop
```

## One-line Recovery (if tmux is fully stopped)

```bash
tmux new -d -s deploy_loop 'while true; do ~/deploy_site.sh; sleep 30m; done'
```

