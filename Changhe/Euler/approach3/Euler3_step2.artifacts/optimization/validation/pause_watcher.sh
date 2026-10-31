#!/bin/bash
# D6FP lead 01:43Z rule: when validation/logs/cpu_profile_S01.log shows the "threads 1:" line (four-thread phase of the CPU timing begins),
# SIGSTOP every PID listed in validation/logs/pause_pids.txt; when it shows DONE, SIGCONT them. Times appended to validation/logs/pause_watcher.log
# and to WORKLOG.md. The PID list may be extended while the watcher runs (one PID per line).
ROOT=$(cd "$(dirname "$0")/.." && pwd); cd "$ROOT"
LOG=validation/logs/cpu_profile_S01.log; PIDS=validation/logs/pause_pids.txt; OUT=validation/logs/pause_watcher.log; WL=../WORKLOG.md
PROFILE_PID=${PROFILE_PID:-739083}
echo "$(date -u +%FT%TZ) watcher start (profile pid $PROFILE_PID)" >> $OUT
paused=0
while true; do
  if ! kill -0 $PROFILE_PID 2>/dev/null; then
    echo "$(date -u +%FT%TZ) profile process $PROFILE_PID gone" >> $OUT
    if [ $paused = 1 ]; then for p in $(cat $PIDS); do kill -CONT $p 2>/dev/null && echo "$(date -u +%FT%TZ) CONT $p (profile gone)" >> $OUT; done; fi
    exit 0
  fi
  if [ $paused = 0 ] && grep -q "^threads 1:" $LOG 2>/dev/null; then
    for p in $(cat $PIDS 2>/dev/null); do kill -STOP $p 2>/dev/null && echo "$(date -u +%FT%TZ) STOP $p (four-thread phase of the CPU timing began)" >> $OUT; done
    paused=1; T=$(date -u +%FT%TZ)
    echo "- $T pause watcher: 'threads 1:' line seen in cpu_profile_S01.log; kill -STOP sent to PIDs $(cat $PIDS | tr '\n' ' ') for the four-thread timing phase (lead 01:43Z)." >> $WL
  fi
  if [ $paused = 1 ] && grep -q "^DONE" $LOG 2>/dev/null; then
    for p in $(cat $PIDS 2>/dev/null); do kill -CONT $p 2>/dev/null && echo "$(date -u +%FT%TZ) CONT $p (timing DONE)" >> $OUT; done
    T=$(date -u +%FT%TZ)
    echo "- $T pause watcher: DONE seen in cpu_profile_S01.log; kill -CONT sent to PIDs $(cat $PIDS | tr '\n' ' ')." >> $WL
    exit 0
  fi
  sleep 15
done
