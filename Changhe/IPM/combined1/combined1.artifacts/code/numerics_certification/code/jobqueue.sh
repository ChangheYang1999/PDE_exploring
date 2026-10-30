#!/bin/bash
# File-based job queue for one core. Usage: jobqueue.sh <core> <jobfile>
# Every non-empty, non-comment line of <jobfile> is one shell command (run from the lane root, low priority, pinned to <core>).
# The first line is popped before it runs, so the file can be edited while the queue runs. A line "EXIT" stops the queue.
# A line "WAITPID <pid>" blocks until that pid has exited.
CORE=$1; JOBS=$2
LANE=RUN_ROOT/numerics_N3; cd $LANE
export PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
PY=python3; export PY
LOG=logs/jobqueue_core$CORE.out
echo "[$(date -u +%FT%TZ)] queue start core $CORE jobfile $JOBS" >> $LOG
while true; do
  LINE=""
  if [ -s "$JOBS" ]; then
    LINE=$(grep -v -m1 -E '^\s*(#|$)' "$JOBS")
    if [ -n "$LINE" ]; then
      # pop the first non-comment, non-empty line
      awk -v done=0 'done==0 && $0 !~ /^[[:space:]]*(#|$)/ {done=1; next} {print}' "$JOBS" > "$JOBS.tmp" && mv "$JOBS.tmp" "$JOBS"
    fi
  fi
  if [ -z "$LINE" ]; then sleep 60; continue; fi
  if [ "$LINE" = "EXIT" ]; then echo "[$(date -u +%FT%TZ)] EXIT" >> $LOG; break; fi
  case "$LINE" in
    WAITPID\ *) P=${LINE#WAITPID }; echo "[$(date -u +%FT%TZ)] waiting for pid $P" >> $LOG
                while kill -0 $P 2>/dev/null; do sleep 20; done; echo "[$(date -u +%FT%TZ)] pid $P gone" >> $LOG; continue;;
  esac
  echo "[$(date -u +%FT%TZ)] START: $LINE" >> $LOG
  taskset -c $CORE nice -n 10 bash -c "$LINE"; RC=$?
  echo "[$(date -u +%FT%TZ)] END rc=$RC: $LINE" >> $LOG
done
