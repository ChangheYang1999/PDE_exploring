#!/bin/bash
# D6FP 2026-10-29T02:45Z: run release-battery gate cases one after another on ONE core after a given process exits (so that no core idles and
# at most four busy computations run). Usage: validation/core_chain.sh <core> <wait_pid or 0> <case1> [case2 ...]
# Each case runs as its own gates.py process with tag cpu_v1_<case> (own JSON and logs), one thread, on the cpu_v1 snapshot (SNAPSHOT=0).
# Also waits until DONE appears in the CPU timing log (the four-thread phase needs idle cores). Log: validation/logs/core_chain_<core>.log
ROOT=$(cd "$(dirname "$0")/.." && pwd); cd "$ROOT"; CORE=$1; WAITPID=$2; shift 2; LOG=validation/logs/core_chain_${CORE}.log
echo "$(date -u +%FT%TZ) chain on core $CORE: wait pid $WAITPID, cases $*" >> $LOG
while ! grep -q "^DONE" validation/logs/cpu_profile_S01.log 2>/dev/null && kill -0 739083 2>/dev/null; do sleep 20; done
while [ "$WAITPID" != "0" ] && kill -0 $WAITPID 2>/dev/null; do sleep 20; done
echo "$(date -u +%FT%TZ) core $CORE free (pid $WAITPID gone, timing done)" >> $LOG
for CASE in "$@"; do
  if [ -f validation/STOP_CHAINS ]; then echo "$(date -u +%FT%TZ) STOP_CHAINS present: not starting $CASE" >> $LOG; exit 0; fi
  echo "$(date -u +%FT%TZ) start gates cpu_v1_${CASE} ${CASE} on core $CORE" >> $LOG
  CORES=$CORE SNAPSHOT=0 bash scripts/run_cpu_battery.sh cpu_v1_${CASE} ${CASE} 1 >> $LOG 2>&1
  echo "$(date -u +%FT%TZ) finished gates cpu_v1_${CASE}" >> $LOG
done
echo "$(date -u +%FT%TZ) chain on core $CORE complete" >> $LOG
