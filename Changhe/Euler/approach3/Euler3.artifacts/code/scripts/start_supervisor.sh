#!/bin/bash
# Start (or restart) the campaign supervisor as a detached process. Safe to re-run: refuses if one is alive.
ROOT=$(cd "$(dirname "$0")/.." && pwd)
HB=$ROOT/status/supervisor_heartbeat.json
if [ -f "$HB" ]; then
  pid=$(python3 -c "import json;print(json.load(open('$HB'))['pid'])" 2>/dev/null)
  if [ -n "$pid" ] && kill -0 "$pid" 2>/dev/null && ps -o cmd= -p "$pid" | grep -q supervisor.py; then
    echo "supervisor already running (pid $pid)"; exit 0
  fi
fi
rm -f "$ROOT/status/STOP_SUPERVISOR"
cd "$ROOT" && setsid nohup env OMP_NUM_THREADS=1 "$ROOT/.venv/bin/python" "$ROOT/scripts/supervisor.py" >> "$ROOT/logs/supervisor.out" 2>&1 < /dev/null &
sleep 2
echo "supervisor started; log: $ROOT/logs/supervisor.log"
