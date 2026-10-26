#!/bin/bash
# Resolve the working layout relative to this script, without a campaign-host path.
IPM_ARTIFACT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
while [ ! -d "$IPM_ARTIFACT_ROOT/work/research860" ] || [ ! -d "$IPM_ARTIFACT_ROOT/outputs" ]; do
    [ "$IPM_ARTIFACT_ROOT" != / ] || { echo "artifact root not found" >&2; exit 1; }
    IPM_ARTIFACT_ROOT="${IPM_ARTIFACT_ROOT%/*}"
    [ -n "$IPM_ARTIFACT_ROOT" ] || IPM_ARTIFACT_ROOT=/
done
export IPM_ARTIFACT_ROOT
# Watchdog for the fork-pool exit deadlock of the campaign driver (outputs/diag/pilot_hang_20261025T0050Z.md); lead order 2026-10-25T00:59Z.
# Every INTERVAL s (<= 60): if the campaign860 worker of <root> waits in wait4 (wchan do_wait) and has exactly one non-zombie child while the
# others are zombies, run bin/pool_unblock_once.sh, which verifies the four conditions (parent py-spy stack in _terminate_pool join; child is a
# pool child of the worker whose py-spy stack contains pool.py worker AND synchronize.py SemLock __enter__; zero CPU ticks over 6 s; every other
# pool worker exited) and ONLY then SIGKILLs that idle child, writing a numbered intervention record plus stack files and logging whether the
# record write succeeded. Nothing else is ever signalled. Log: outputs/diag/pool_watchdog.log. Stop: touch outputs/diag/pool_watchdog.STOP.
# Usage: setsid nohup bin/pool_hang_watchdog.sh <campaign-root> [interval-s=45] > /dev/null 2>&1 < /dev/null &
set -u
ROOT=$1; INTERVAL=${2:-45}; LANE=$IPM_ARTIFACT_ROOT; LOG=$LANE/outputs/diag/pool_watchdog.log
stamp() { date -u +%FT%TZ; }
echo "$(stamp) watchdog start pid $$ root $ROOT interval $INTERVAL" >> $LOG; echo $$ > $LANE/outputs/diag/pool_watchdog.pid
while true; do
  [ -e $LANE/outputs/diag/pool_watchdog.STOP ] && { echo "$(stamp) STOP file present; watchdog exits" >> $LOG; exit 0; }
  for W in $(pgrep -f "campaign860.py --root $ROOT"); do
    [ "$(cat /proc/$W/wchan 2>/dev/null)" = "do_wait" ] || continue
    live=0; zomb=0; for k in $(pgrep -P $W); do st=$(awk '{print $3}' /proc/$k/stat 2>/dev/null); if [ "$st" = "Z" ]; then zomb=$((zomb+1)); else live=$((live+1)); fi; done
    if [ "$live" = "1" ] && [ "$zomb" -ge 1 ]; then
      echo "$(stamp) candidate: worker $W in do_wait, $live live child, $zomb zombies; running the four-condition check" >> $LOG
      bash $LANE/bin/pool_unblock_once.sh $W $ROOT >> $LOG 2>&1
    fi
  done
  sleep $INTERVAL
done
