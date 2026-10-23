#!/bin/bash
# Graceful STOP: workers checkpoint and exit, queue entries are kept, runner exits.
P=$(cd "$(dirname "$0")/.." && pwd)
touch "$P/STOP"
echo "STOP requested at $(date -u +%FT%TZ); waiting for runner to exit..."
for i in $(seq 1 120); do
  if [ -f "$P/runner.pid" ] && kill -0 "$(cat "$P/runner.pid")" 2>/dev/null; then sleep 5; else echo "runner stopped"; exit 0; fi
done
echo "runner still alive after 10 min; check $P/runner.log"
