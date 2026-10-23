#!/bin/bash
# One-command launch / RESUME of the supervised runner (detached, survives the agent session).
P=$(cd "$(dirname "$0")/.." && pwd)
cd "$P"
if [ -f runner.pid ] && kill -0 "$(cat runner.pid)" 2>/dev/null; then echo "runner already running (pid $(cat runner.pid))"; exit 0; fi
rm -f STOP
setsid nohup nice -n 19 python3 "$P/runner.py" >> "$P/runner.out" 2>&1 < /dev/null &
sleep 1
echo "runner launched pid $(cat runner.pid 2>/dev/null) ; status: $P/bin/status.sh ; stop: $P/bin/stop.sh"
