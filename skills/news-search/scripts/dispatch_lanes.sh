#!/usr/bin/env bash
# Dispatch news-search worker lanes to Codex, with the guards the 2026-08-30 round paid for.
#
#   dispatch_lanes.sh --prompts DIR --results DIR [--cap N] [--no-wait] UNIT [UNIT ...]
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
#
# NEVER edit this file while a wave is in flight. Bash reads a script lazily by byte offset,
# so an edit kills the running shell mid-loop. Copy it and edit the copy.
set -u

PROMPTS=""; RESULTS=""; CAP=4; WAIT=1; RECONCILE_ONLY=0
UNITS=""

while [ $# -gt 0 ]; do
  case "$1" in
    --prompts)        PROMPTS="$2"; shift 2 ;;
    --results)        RESULTS="$2"; shift 2 ;;
    --cap)            CAP="$2"; shift 2 ;;
    --no-wait)        WAIT=0; shift ;;
    --reconcile-only) RECONCILE_ONLY=1; shift ;;
    -h|--help)        sed -n '2,29p' "$0"; exit 0 ;;
    *)                u="${1%$''}"
                      # An empty or whitespace-only argument used to leave UNITS as a lone space,
                      # which passes the non-empty test while every `for u in $UNITS` loop sees zero
                      # words: the run then reports RECONCILE-OK on 0 units and exits 0. That is the
                      # false success this script exists to prevent, so reject it at the argument.
                      case "$u" in ''|*[[:space:]]*)
                        echo "unit id must be non-empty and contain no whitespace, got: '$1'" >&2; exit 2 ;;
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

# Resolve dispatch-task through the documented skill lookup order, first hit wins.
DISPATCH=""
for c in "skills/prun/scripts/dispatch-task.sh" \
         ".claude/skills/prun/scripts/dispatch-task.sh" \
         ".agent-config/repo/skills/prun/scripts/dispatch-task.sh"; do
  [ -f "$c" ] && { DISPATCH="$(cd "$(dirname "$c")" && pwd)/$(basename "$c")"; break; }
done
[ -n "$DISPATCH" ] || { echo "dispatch-task.sh not found in the skill lookup order" >&2; exit 2; }

export PRUN_SCRATCH_CWD="${PRUN_SCRATCH_CWD:-$(pwd)}"
export CODEX_DISPATCH_REASONING="${CODEX_DISPATCH_REASONING:-xhigh}"
export CODEX_DISPATCH_SANDBOX="${CODEX_DISPATCH_SANDBOX:-danger-full-access}"
export PRUN_STALL_THRESHOLD="${PRUN_STALL_THRESHOLD:-1800}"
# dispatch-task defaults CODEX_DISPATCH_TIMEOUT to 0, which disables its hard deadline and
# leaves only the idle-tail check. A worker that never finishes but keeps appending output
# resets that idle timer forever, holds a slot under --cap forever, and blocks the final
# reconcile. Give wait mode a finite wall clock. Set CODEX_DISPATCH_TIMEOUT=0 explicitly to
# opt back out when a lane is genuinely expected to run longer than this.
export CODEX_DISPATCH_TIMEOUT="${CODEX_DISPATCH_TIMEOUT:-7200}"

# A non-empty result is not the same as a finished one. When dispatch-task reaps a worker on
# hard-timeout or idle-stall it still writes a result, headed FALLBACK and beginning
# "Conclusion: INCOMPLETE", so the unit is never silently missing. Sizing the file alone would
# accept that as success, which is the silent lane-loss this launcher exists to prevent, and
# bare `wait` does not surface the child's 124 exit either.
result_complete() {
  local result="$1"
  [ -s "$result" ] || return 1
  ! head -n 1 "$result" | grep -Fq '(FALLBACK, worker wrote no result file)'
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
  if [ "$WAIT" = "1" ]; then
    while [ "$(running)" -ge "$CAP" ]; do sleep 20; done
  fi
  : > "$L"
  nohup "$DISPATCH" --prompt-file "$P" --result-file "$R" --unit-id "$u" >>"$L" 2>&1 </dev/null &
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
