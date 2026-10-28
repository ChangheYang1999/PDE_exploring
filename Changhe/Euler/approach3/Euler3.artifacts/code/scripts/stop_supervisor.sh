#!/bin/bash
# Ask the supervisor to stop: it SIGTERMs workers (they checkpoint) and exits. Jobs stay in the queue and resume on restart.
ROOT=$(cd "$(dirname "$0")/.." && pwd)
touch "$ROOT/status/STOP_SUPERVISOR"
echo "stop requested; watch $ROOT/logs/supervisor.log"
