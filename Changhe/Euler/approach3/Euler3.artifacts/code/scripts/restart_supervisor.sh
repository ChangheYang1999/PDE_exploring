#!/bin/bash
# Plain supervisor restart: STOP (workers checkpoint on SIGTERM and exit, jobs stay pending), then start; jobs resume from checkpoints.
ROOT=$(cd "$(dirname "$0")/.." && pwd); cd $ROOT
echo "$(date -u +%FT%TZ) requesting stop"; touch status/STOP_SUPERVISOR
pid=$(python3 -c "import json;print(json.load(open('status/supervisor_heartbeat.json'))['pid'])")
for i in $(seq 1 100); do kill -0 $pid 2>/dev/null || break; sleep 6; done
kill -0 $pid 2>/dev/null && { echo "supervisor still alive; aborting"; exit 1; }
sleep 20; echo "$(date -u +%FT%TZ) supervisor exited; workers left: $(pgrep -f scripts/worker.py | wc -l)"
rm -f status/STOP_SUPERVISOR; scripts/start_supervisor.sh; echo "$(date -u +%FT%TZ) done"
