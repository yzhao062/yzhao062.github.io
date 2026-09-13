#!/usr/bin/env bash
# Dispatch news-search worker lanes, with the guards the 2026-08-30 round paid for.
#
#   dispatch_lanes.sh --prompts DIR --results DIR [--backend agy|codex] [--cap N] [--no-wait] UNIT ...
#
# Lanes go to Agy (Gemini through the Antigravity CLI) by default. Codex stays reachable
# behind --backend codex, because the prun skill reserves its higher-cost quota for the
# /vet gatekeeper role rather than for ordinary fan-out. This mirrors the backend switch in
# meta-finder's funding pass (FUNDING_LLM_BACKEND, agy default, codex retained).
#
# Reads <prompts>/<unit>.md, writes <results>/<unit>.md, logs to <results>/../state/<unit>.log.
# Every guard here exists because its absence lost lanes silently. See
# references/fan-out-reliability.md for what each one is standing in for.
#
#   1. Unit ids are stripped of a trailing CR. A list written by Python on Windows carries
#      CRLF, and the CR poisons every path built from the id.
#   2. Launch is verified by polling for dispatch-task's STATE-DIR line, never assumed.
#   3. Workers use nohup; setsid does not exist in Git Bash. Only --no-wait disowns them.
#      Wait mode keeps each worker in the job table, because that table is both the --cap
#      counter and what `wait` blocks on. Disowning unconditionally is exactly what made
#      --cap a no-op and let reconciliation run against workers that had barely started.
#   4. Every prompt is preflighted before any worker starts, so a missing one fails the run rather
#      than quietly shrinking the launch set to nothing and exiting 0 under --no-wait.
#   5. The run reconciles every dispatched unit against a *complete* result file and exits
#      non-zero when any is missing, empty, or a timeout FALLBACK. A reaped worker still leaves
#      a non-empty result behind, so size alone would grade a timeout as a success.
#   6. With --no-wait the script holds no supervising shell, so nothing long-lived can be
#      killed out from under the workers. Reconcile later with --reconcile-only. Note that
#      --cap has no effect in --no-wait mode: the cap counts entries in the shell job table,
#      and --no-wait disowns each worker as it launches. Launch every unit you pass, or run
#      without --no-wait when you need the cap enforced.
#   7. The FALLBACK test matches either dispatcher's header, anchored and case-sensitive.
#      The two write different text ("worker wrote no result file" for Codex, "Agy wrote no
#      final result" for Agy), so a literal match on one grades the other's failure as a
#      success. anywhere-agents 754833a fixed the same divergence in monitor.{sh,ps1}.
#   8. The wall clock is set through whichever knob the chosen backend reads. They are named
#      differently, so exporting only Codex's leaves an Agy lane with no hard deadline, and
#      guard 5 is only load-bearing while a lane can actually time out.
#
# NEVER edit this file while a wave is in flight. Bash reads a script lazily by byte offset,
# so an edit kills the running shell mid-loop. Copy it and edit the copy.
set -u

PROMPTS=""; RESULTS=""; CAP=4; WAIT=1; RECONCILE_ONLY=0
BACKEND=""
UNITS=""

while [ $# -gt 0 ]; do
  case "$1" in
    --prompts)        PROMPTS="$2"; shift 2 ;;
    --results)        RESULTS="$2"; shift 2 ;;
    --backend)        [ $# -ge 2 ] && [ -n "${2:-}" ] || {
                        echo "--backend requires a value: agy or codex" >&2; exit 2; }
                      BACKEND="$2"; shift 2 ;;
    --cap)            CAP="$2"; shift 2 ;;
    --no-wait)        WAIT=0; shift ;;
    --reconcile-only) RECONCILE_ONLY=1; shift ;;
                      # Print the whole header comment rather than a hardcoded line range. The
                      # range was '2,29p', then '2,37p', and drifted out of date both times the
                      # header grew, truncating guard 8 and hiding the never-edit-in-flight
                      # warning. Stop at the first line that is not a comment.
    -h|--help)        awk 'NR>1 && /^#/ {print; next} NR>1 {exit}' "$0"; exit 0 ;;
    *)                u="${1%$''}"
                      # An empty or whitespace-only argument used to leave UNITS as a lone space,
                      # which passes the non-empty test while every `for u in $UNITS` loop sees zero
                      # words: the run then reports RECONCILE-OK on 0 units and exits 0. That is the
                      # false success this script exists to prevent, so reject it at the argument.
                      # Match the alphabet both dispatchers enforce (dispatch-task.sh:128-133,
                      # dispatch-task-agy.py:384-385) rather than only rejecting whitespace.
                      # Their check happens after this launcher has already touched the
                      # filesystem: the retry branch moves a path built from $u, so an id like
                      # `../victim` relocated an unrelated file outside both directories before
                      # the dispatcher rejected the unit. Tightening here also keeps slashes and
                      # glob characters out of the mktemp template and out of the later unquoted
                      # `for u in $UNITS` expansion. Caught in review round 2.
                      case "$u" in ''|*[!A-Za-z0-9_-]*)
                        echo "unit id must contain only letters, digits, dashes, or underscores, got: '$1'" >&2
                        exit 2 ;;
                      esac
                      UNITS="$UNITS $u"; shift ;;
  esac
done

[ -n "$PROMPTS" ] && [ -n "$RESULTS" ] || { echo "need --prompts and --results" >&2; exit 2; }
[ -n "$UNITS" ] || { echo "no units given" >&2; exit 2; }
# --cap counts live entries in the shell job table, so a cap of 0 (or a non-number, which
# compares as 0 under -ge) makes the gate loop wait for a job count below zero. Nothing ever
# launches, and the run looks like a slow dispatch rather than a bad flag.
# Validate a decimal count that a later [ -ge ] / [ -gt ] will compare. Three things bite here.
# Digits alone are not enough: past the shell's integer width the comparison fails with "integer
# expression expected", which evaluates false, so an oversized bound silently becomes no bound while
# each launch prints an error. Leading zeros must be stripped before the width test, or "00" passes
# as non-zero and then compares as zero, hanging the launch gate forever. And the override is a
# documented control, so it needs the same treatment as the flag. Echoes the normalized value.
validate_count() {
  local label="$1" raw="$2" norm
  case "$raw" in ''|*[!0-9]*) echo "$label must be a positive integer, got: $raw" >&2; return 2 ;; esac
  norm="${raw#"${raw%%[!0]*}"}"          # strip leading zeros; "000" -> "" and "04" -> "4"
  [ -n "$norm" ] || { echo "$label must be a positive integer, got: $raw" >&2; return 2; }
  [ "${#norm}" -le 9 ] || { echo "$label is too large, got: $raw" >&2; return 2; }
  echo "$norm"
}

CAP_MAX="$(validate_count "DISPATCH_LANES_CAP_MAX" "${DISPATCH_LANES_CAP_MAX:-1000}")" || exit 2
CAP="$(validate_count "--cap" "$CAP")" || exit 2
# A documented round dispatches thirty to forty lanes, so the 1000 default is far above real use.
[ "$CAP" -le "$CAP_MAX" ] || {
  echo "--cap must be between 1 and $CAP_MAX, got: $CAP (raise DISPATCH_LANES_CAP_MAX if you mean it)" >&2
  exit 2
}

STATE="$RESULTS/../state"
mkdir -p "$RESULTS" "$STATE"

# Interpreter resolution, copied from the prun scripts' own resolve_python (report-state.sh,
# snapshot-tail.sh) so this launcher honours the same knobs. PRUN_PYTHON outranks
# ANYWHERE_AGENTS_PYTHON. A bare `command -v python` is not sufficient on Windows: it resolves
# to the Microsoft Store redirect stub under WindowsApps, which either fails or opens a GUI
# dialog, so candidates are rejected by path and then proven by actually running.
_python_usable() {
  case "$1" in
    *WindowsApps*|*windowsapps*) return 1 ;;
  esac
  "$1" -I -c 'import sys; sys.exit(0)' >/dev/null 2>&1
}

resolve_python() {
  local explicit="${PRUN_PYTHON:-${ANYWHERE_AGENTS_PYTHON:-}}"
  if [ -n "$explicit" ]; then
    if _python_usable "$explicit"; then printf '%s\n' "$explicit"; return 0; fi
    echo "dispatch_lanes: PRUN_PYTHON/ANYWHERE_AGENTS_PYTHON is not usable: $explicit" >&2
    return 1
  fi
  local candidate resolved
  for candidate in python3 python; do
    resolved="$(command -v "$candidate" 2>/dev/null || true)"
    [ -n "$resolved" ] || continue
    if _python_usable "$resolved"; then printf '%s\n' "$resolved"; return 0; fi
  done
  return 1
}

# Agy binary resolution, mirroring resolve_binary() in dispatch-task-agy.py. The installer
# updates the user PATH registry but cannot update an already-running shell, so the CLI is
# often present at %LOCALAPPDATA%\agy\bin\agy.exe while absent from this shell's PATH. Without
# this fallback the preflight would fail on a machine where the dispatcher itself would work.
resolve_agy() {
  local want resolved candidate
  want="${ANTIGRAVITY_BIN:-agy}"
  # The dispatcher reads os.environ.get("ANTIGRAVITY_BIN", "agy"), which returns the empty
  # string when the variable is SET but empty, so the Python default never applies and it
  # resolves nothing. The shell's ${...:-agy} would silently substitute "agy" here and pass
  # preflight, producing a clean preflight followed by FAILED-START on every lane. Normalize
  # the empty override the same way on both sides: treat it as unset and warn once.
  if [ -n "${ANTIGRAVITY_BIN+set}" ] && [ -z "${ANTIGRAVITY_BIN:-}" ]; then
    echo "ANTIGRAVITY_BIN is set but empty; unsetting it so the dispatcher resolves agy itself" >&2
    unset ANTIGRAVITY_BIN
    want="agy"
  fi
  resolved="$(command -v "$want" 2>/dev/null || true)"
  # The Windows fallback applies whenever the name being sought is the bare executable, which
  # includes an explicit ANTIGRAVITY_BIN=agy, because resolve_binary() in the dispatcher allows
  # either bare name there (dispatch-task-agy.py:108-113). Gating this on "unset" alone made
  # the launcher reject a configuration the dispatcher supports.
  case "$want" in
    agy|agy.exe)
      if [ -z "$resolved" ] && [ -n "${LOCALAPPDATA:-}" ]; then
        for candidate in "$LOCALAPPDATA/agy/bin/agy.exe"; do
          [ -f "$candidate" ] && { resolved="$candidate"; break; }
        done
      fi
      ;;
  esac
  [ -n "$resolved" ] || return 1
  printf '%s\n' "$resolved"
}

# Backend selection. Agy is the default because the prun skill reserves Codex for /vet.
# An unknown value fails closed rather than falling through to a default, so a typo in a
# round script cannot quietly send forty lanes to the expensive backend.
BACKEND="$(echo "${BACKEND:-${NEWS_SEARCH_LANE_BACKEND:-agy}}" | tr '[:upper:]' '[:lower:]')"
case "$BACKEND" in
  agy|codex) ;;
  *) echo "unknown --backend '$BACKEND'; expected one of agy, codex" >&2; exit 2 ;;
esac

# Resolve the chosen dispatcher through the documented skill lookup order, first hit wins.
# DISPATCH_CMD is an array because the Agy dispatcher is Python and needs an interpreter in
# front of it, while the Codex one is a shell script invoked directly.
if [ "$BACKEND" = "agy" ]; then
  DISPATCH_REL="scripts/dispatch-task-agy.py"
else
  DISPATCH_REL="scripts/dispatch-task.sh"
fi
DISPATCH=""
for c in "skills/prun/$DISPATCH_REL" \
         ".claude/skills/prun/$DISPATCH_REL" \
         ".agent-config/repo/skills/prun/$DISPATCH_REL"; do
  [ -f "$c" ] && { DISPATCH="$(cd "$(dirname "$c")" && pwd)/$(basename "$c")"; break; }
done
[ -n "$DISPATCH" ] || { echo "$(basename "$DISPATCH_REL") not found in the skill lookup order" >&2; exit 2; }

if [ "$BACKEND" = "agy" ]; then
  PY="$(resolve_python)" || {
    echo "no usable Python interpreter for the Agy dispatcher; set PRUN_PYTHON" >&2; exit 2; }
  DISPATCH_CMD=("$PY" "$DISPATCH")
  # Unset rather than merely decline to export. A research lane must never see the checkout:
  # the Agy dispatcher refuses a caller-supplied workspace without an explicit --mode, and
  # with accept-edits it can write whatever it is pointed at. Neither --mode plan nor the
  # sandbox stops a headless write (meta-finder a9c8573 established this), so the only real
  # boundary is that the lane has no workspace at all and its prompt names no repo path. The
  # lane's inventory therefore travels in the prompt body, not as a file path.
  #
  # Skipping the export is not enough, because an inherited value survives it. The Agy
  # dispatcher then exits 2 before printing STATE-DIR, this script polls the full launch
  # deadline, and every unit is reported FAILED-START. Caught in review round 1.
  unset PRUN_SCRATCH_CWD
  export ANTIGRAVITY_DISPATCH_MODEL="${ANTIGRAVITY_DISPATCH_MODEL:-gemini-3.8-flash-high}"
  export ANTIGRAVITY_DISPATCH_EFFORT="${ANTIGRAVITY_DISPATCH_EFFORT:-high}"
  # Guard 8: the Agy dispatcher reads its own timeout name, and this is the ONLY deadline an
  # Agy lane gets. It runs no idle check: its process.wait() has no independent timeout and it
  # delegates enforcement to the CLI's --print-timeout. PRUN_STALL_THRESHOLD is a Codex-only
  # knob and is deliberately not exported here.
  export ANTIGRAVITY_DISPATCH_TIMEOUT_SECONDS="${ANTIGRAVITY_DISPATCH_TIMEOUT_SECONDS:-7200}"
else
  DISPATCH_CMD=("$DISPATCH")
  export PRUN_SCRATCH_CWD="${PRUN_SCRATCH_CWD:-$(pwd)}"
  export PRUN_STALL_THRESHOLD="${PRUN_STALL_THRESHOLD:-1800}"
  export CODEX_DISPATCH_REASONING="${CODEX_DISPATCH_REASONING:-xhigh}"
  export CODEX_DISPATCH_SANDBOX="${CODEX_DISPATCH_SANDBOX:-danger-full-access}"
  # dispatch-task defaults CODEX_DISPATCH_TIMEOUT to 0, which disables its hard deadline and
  # leaves only the idle-tail check. A worker that never finishes but keeps appending output
  # resets that idle timer forever, holds a slot under --cap forever, and blocks the final
  # reconcile. Give wait mode a finite wall clock. Set CODEX_DISPATCH_TIMEOUT=0 explicitly to
  # opt back out when a lane is genuinely expected to run longer than this.
  export CODEX_DISPATCH_TIMEOUT="${CODEX_DISPATCH_TIMEOUT:-7200}"
fi

# A non-empty result is not the same as a finished one. When either dispatcher reaps a worker
# on hard-timeout or idle-stall it still writes a result, headed FALLBACK and beginning
# "Conclusion: INCOMPLETE", so the unit is never silently missing. Sizing the file alone would
# accept that as success, which is the silent lane-loss this launcher exists to prevent, and
# bare `wait` does not surface the child's 124 exit either.
#
# The two dispatchers word their header differently: Codex writes "(FALLBACK, worker wrote no
# result file)" and Agy writes "(FALLBACK, Agy wrote no final result)". A literal match on one
# reports the other's failure as a complete result. Match the shape instead, anchored at the
# line start and case-sensitive so a genuine result that merely discusses fallbacks in its
# prose is not misread as one. This is the same generalization anywhere-agents 754833a applied
# to monitor.{sh,ps1} after an Agy FALLBACK was reported done.
result_complete() {
  local result="$1"
  [ -s "$result" ] || return 1
  ! head -n 1 "$result" | grep -Eq '^# [A-Za-z0-9_-]+ result \(FALLBACK, '
}

reconcile() {
  local incomplete="" u
  for u in $UNITS; do
    result_complete "$RESULTS/$u.md" || incomplete="$incomplete $u"
  done
  if [ -n "$incomplete" ]; then
    echo "RECONCILE-FAIL missing, empty, or fallback results:$incomplete"
    return 3
  fi
  echo "RECONCILE-OK $(echo $UNITS | wc -w) units returned a complete result"
  return 0
}

if [ "$RECONCILE_ONLY" = "1" ]; then
  reconcile; exit $?
fi

# Name the backend in the run's own output. A round's write-up records which executor produced
# each lane (meta-finder stores backend and model on every pick for the same reason), and a
# reconcile-only rerun months later should not have to guess from the audit prose.
echo "BACKEND        $BACKEND"

# Preflight the Agy CLI before launching anything. `agy --version` and `agy models` are the
# two calls meta-finder a9c8573 settled on: the first proves the binary runs, the second that
# the account is authenticated and a model list is reachable. Without this, an expired login
# surfaces as N identical FAILED-START lines after the full launch deadline has elapsed.
# Set NEWS_SEARCH_AGY_PREFLIGHT=off to skip.
if [ "$BACKEND" = "agy" ] && [ "${NEWS_SEARCH_AGY_PREFLIGHT:-on}" != "off" ]; then
  AGY_BIN="$(resolve_agy)" || {
    echo "agy CLI not found: install the Antigravity CLI or set ANTIGRAVITY_BIN" >&2; exit 2; }
  # Do NOT export ANTIGRAVITY_BIN from what resolve_agy found. `command -v` under Git Bash
  # returns a POSIX path (/c/Users/...), and the Python dispatcher cannot execute that form on
  # Windows: exporting it turned a working lane into "no runnable Antigravity CLI found". The
  # dispatcher carries the same LOCALAPPDATA fallback, so it can always resolve the binary
  # whenever this preflight could. Leave its own resolution alone.
  #
  # Bound each call. An unbounded check blocks before any lane launches, and neither the worker
  # timeout nor the launch deadline covers this earlier step. Reuse the name the Agy
  # dispatcher's own preflight reads so one setting governs both.
  # Validate as a positive integer, matching positive_int_env() in the dispatcher, which rejects
  # zero and anything non-numeric. Accepting 0 here disabled the timeout entirely while the
  # dispatcher would refuse the same value later, so the two disagreed before dispatch began.
  AGY_PF_TIMEOUT="$(validate_count "ANTIGRAVITY_PREFLIGHT_TIMEOUT_SECONDS" \
    "${ANTIGRAVITY_PREFLIGHT_TIMEOUT_SECONDS:-60}")" || exit 2
  for a in --version models; do
    # --kill-after is what makes the bound real. Plain `timeout` sends TERM and then keeps
    # waiting, so a CLI that ignores TERM runs to completion and the wrapper only reports 124
    # afterwards: a 0.2s deadline still let a one-second fixture finish. Escalate to KILL.
    timeout --kill-after=5s "$AGY_PF_TIMEOUT" "$AGY_BIN" "$a" >/dev/null 2>&1 || {
      rc=$?
      case "$rc" in
        124) echo "agy preflight timed out after ${AGY_PF_TIMEOUT}s on \`$(basename "$AGY_BIN") $a\`" >&2 ;;
        137) echo "agy preflight ignored TERM and was killed after ${AGY_PF_TIMEOUT}s + 5s on \`$(basename "$AGY_BIN") $a\`" >&2 ;;
        125|126|127) echo "agy preflight could not run \`$(basename "$AGY_BIN") $a\` (timeout exit $rc)" >&2 ;;
        *) echo "agy preflight failed on \`$(basename "$AGY_BIN") $a\` (exit $rc); check the login before dispatching" >&2 ;;
      esac
      exit 2; }
  done
  echo "PREFLIGHT-OK   agy --version, agy models"
fi

running() { jobs -rp | wc -l; }

# Preflight every prompt before launching anything. Skipping a missing prompt and carrying on lets
# --no-wait finish with an empty launch set, print "workers running detached", and exit 0 having
# launched nothing, which is the exact exit-code-is-not-evidence failure this script exists to close.
# A later --reconcile-only would catch it, but a preflight failure known before any worker started
# should never be reported as a successful launch.
MISSING=""
for u in $UNITS; do
  [ -f "$PROMPTS/$u.md" ] || MISSING="$MISSING $u"
done
if [ -n "$MISSING" ]; then
  echo "MISSING-PROMPTS:$MISSING"
  echo "no workers launched; every requested unit needs a prompt at $PROMPTS/<unit>.md" >&2
  exit 3
fi

DISPATCHED=""
for u in $UNITS; do
  P="$PROMPTS/$u.md"; R="$RESULTS/$u.md"; L="$STATE/$u.log"
  if result_complete "$R"; then echo "ALREADY-DONE   $u"; continue; fi
  # The Agy dispatcher refuses ANY pre-existing result path (dispatch-task-agy.py:397-398),
  # so a retry of an incomplete lane could never start: it printed LAUNCHED, then FAILED-START
  # "result path already exists", and burned the launch deadline doing it. Retrying a fallback
  # is the normal case this launcher is built around, so move the incomplete artifact aside
  # under a unique name rather than deleting it. Checklist item 10 requires reading a FALLBACK
  # tail before re-dispatching, which needs that file to still exist. Caught in review round 1.
  if [ "$BACKEND" = "agy" ] && [ -e "$R" ]; then
    previous="$(mktemp "$STATE/$u.previous-result.XXXXXX")" || {
      echo "could not create a holding path for $u's previous result under $STATE" >&2; exit 3; }
    # Remove the empty file mktemp just created if the move fails, so a failed retry does not
    # accumulate zero-byte siblings next to the real salvaged tails, and say which unit failed.
    mv -- "$R" "$previous" || {
      rm -f -- "$previous"
      echo "could not move $u's previous result out of the way: $R -> $previous" >&2; exit 3; }
    echo "PREVIOUS-RESULT $u :: $previous"
  fi
  if [ "$WAIT" = "1" ]; then
    while [ "$(running)" -ge "$CAP" ]; do sleep 20; done
  fi
  : > "$L"
  nohup "${DISPATCH_CMD[@]}" --prompt-file "$P" --result-file "$R" --unit-id "$u" >>"$L" 2>&1 </dev/null &
  # Detach ONLY in --no-wait mode. disown removes the job from `jobs -rp`, which is both the
  # concurrency cap's counter and what `wait` blocks on. Disowning unconditionally made --cap
  # a no-op and made `wait` return instantly, so reconciliation ran against workers that had
  # barely started and reported them missing. Confirmed by review: after disown the job count
  # went 1 -> 0, `wait` returned in 0s, and the child was still alive.
  if [ "$WAIT" = "0" ]; then
    disown 2>/dev/null || true
  fi
  DISPATCHED="$DISPATCHED $u"
  echo "LAUNCHED       $u"
  sleep 3
done

# Verify the launch actually took, by polling rather than by one delayed sample. dispatch-task
# emits exactly one STATE-DIR line before it starts the model, so the thing being waited on is
# dispatcher startup, which antivirus, shell re-execution, or host load can delay well past any
# fixed grace period. A single sample would label a slow starter FAILED-START and leave it running.
LAUNCH_DEADLINE="${DISPATCH_LANES_LAUNCH_DEADLINE:-120}"
PENDING="$DISPATCHED"
FAILED=""
elapsed=0
while [ -n "$PENDING" ]; do
  STILL=""
  for u in $PENDING; do
    if grep -q '^STATE-DIR ' "$STATE/$u.log" 2>/dev/null; then
      echo "CONFIRMED      $u"
    elif result_complete "$RESULTS/$u.md"; then
      echo "ALREADY-DONE   $u"
    else
      STILL="$STILL $u"
    fi
  done
  PENDING="$STILL"
  # Sample first, then test the deadline. Testing the deadline at the top of the loop skipped
  # the final sample, so a unit that wrote STATE-DIR during the last sleep was reported
  # FAILED-START even though it had started. Every unit is now classified exactly once, and
  # a launch that lands on the boundary is accepted.
  [ -n "$PENDING" ] || break
  [ "$elapsed" -lt "$LAUNCH_DEADLINE" ] || break
  remaining=$((LAUNCH_DEADLINE - elapsed))
  step=5
  [ "$remaining" -lt "$step" ] && step="$remaining"
  sleep "$step"
  elapsed=$((elapsed + step))
done
for u in $PENDING; do
  FAILED="$FAILED $u"
  echo "FAILED-START   $u :: $(head -1 "$STATE/$u.log" 2>/dev/null)"
done
[ -n "$FAILED" ] && { echo "START-FAILURES:$FAILED"; exit 3; }

if [ "$WAIT" = "0" ]; then
  echo "workers running detached; reconcile later with --reconcile-only"
  exit 0
fi

wait
reconcile
