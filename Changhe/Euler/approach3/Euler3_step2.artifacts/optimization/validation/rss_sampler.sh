#!/bin/bash
# D6FP: sample VmRSS and VmHWM of a PID every N seconds (default 10) to validation/logs/rss_<pid>.log until the process exits. Usage: rss_sampler.sh <pid> [interval]
PID=$1; INT=${2:-10}; cd "$(dirname "$0")/.."; OUT=validation/logs/rss_${PID}.log
while kill -0 $PID 2>/dev/null; do echo "$(date -u +%FT%TZ) $(grep -E 'VmRSS|VmHWM' /proc/$PID/status 2>/dev/null | awk '{printf "%s %.2f GB ", $1, $2/1e6}')" >> $OUT; sleep $INT; done
echo "$(date -u +%FT%TZ) process $PID exited" >> $OUT
