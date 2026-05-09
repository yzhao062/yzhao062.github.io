#!/usr/bin/env bash
# One-time bootstrap: install local SSH public key on viterbi-scf01.vlab.usc.edu
# and add a 'usc-deploy' alias to ~/.ssh/config.
#
# After this runs successfully you can use:
#   ssh usc-deploy 'crontab -l'
#   ssh usc-deploy 'tail -20 ~/deploy_logs/deploy_$(date +%F).log'
# without ever entering the USC password again. The Python helpers
# (scripts/server_ssh.py, scripts/apply_robustness_layer12.py) also pick up
# the installed key when DEPLOY_PASS is empty in .env.
#
# Usage:
#   bash scripts/setup_usc_deploy_key.sh
#
# You will be prompted for your USC password ONCE (when the script pushes the
# public key to the server). The password is never stored on disk.

set -euo pipefail

HOST="viterbi-scf01.vlab.usc.edu"
USER_NAME="yzhao010"
ALIAS="usc-deploy"
KEY="$HOME/.ssh/id_ed25519"
PUB_KEY="$KEY.pub"
CONFIG="$HOME/.ssh/config"

if [[ ! -f "$PUB_KEY" ]]; then
  echo "ERROR: public key $PUB_KEY not found." >&2
  echo "       Generate one first with: ssh-keygen -t ed25519" >&2
  exit 1
fi

# Skip the password step entirely if the key is already authorized.
if ssh -o BatchMode=yes -o ConnectTimeout=10 -i "$KEY" "$USER_NAME@$HOST" \
       'echo authorized' 2>/dev/null | grep -q '^authorized$'; then
  echo "[1/3] Public key already authorized on $HOST -- skipping password step."
else
  echo "[1/3] Pushing public key to $USER_NAME@$HOST"
  echo "      You will be prompted for your USC password ONCE."
  cat "$PUB_KEY" | ssh -o StrictHostKeyChecking=accept-new "$USER_NAME@$HOST" '
    set -e
    mkdir -p ~/.ssh && chmod 700 ~/.ssh
    touch ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys
    while IFS= read -r line; do
      [ -z "$line" ] && continue
      if grep -qxF "$line" ~/.ssh/authorized_keys; then
        echo "      (key already in authorized_keys)"
      else
        printf "%s\n" "$line" >> ~/.ssh/authorized_keys
        echo "      (key appended to authorized_keys)"
      fi
    done
  '
fi

echo
echo "[2/3] Ensuring '$ALIAS' alias in $CONFIG"
mkdir -p "$(dirname "$CONFIG")"
touch "$CONFIG"
chmod 600 "$CONFIG"
if grep -Eq "^[[:space:]]*Host[[:space:]]+$ALIAS([[:space:]]|$)" "$CONFIG"; then
  echo "      ('$ALIAS' already in config; leaving as-is)"
else
  cat >> "$CONFIG" <<EOF

Host $ALIAS
    HostName $HOST
    User $USER_NAME
    IdentityFile $KEY
    IdentitiesOnly yes
    StrictHostKeyChecking accept-new
    UserKnownHostsFile ~/.ssh/known_hosts
    ServerAliveInterval 60
    ServerAliveCountMax 3
EOF
  echo "      ('$ALIAS' appended)"
fi

echo
echo "[3/3] Verifying passwordless login via '$ALIAS'"
if ssh -o BatchMode=yes -o ConnectTimeout=10 "$ALIAS" \
       'echo "      OK from $(hostname) as $(whoami)"'; then
  echo
  echo "Setup complete. Try:"
  echo "    ssh $ALIAS 'crontab -l'"
else
  echo
  echo "Passwordless login still failing. Run 'ssh -v $ALIAS' to debug." >&2
  exit 1
fi
