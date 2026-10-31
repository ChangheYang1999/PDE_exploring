#!/bin/bash
# Return the parked low-priority sweep jobs (queue/hold_lowprio) to queue/pending. They were parked at 2026-10-25T08:02Z so that the GPUs could
# drain and the exclusive nest8 / s1nk / s9b jobs could start (the supervisor places an exclusive job only on a fully free GPU, and a long queue of
# non-exclusive jobs otherwise keeps every GPU partly occupied).
ROOT=$(cd "$(dirname "$0")/.." && pwd); cd $ROOT
n=$(ls queue/hold_lowprio/*.json 2>/dev/null | wc -l)
[ "$n" -gt 0 ] && mv queue/hold_lowprio/*.json queue/pending/
echo "$(date -u +%FT%TZ) released $n low-priority jobs to queue/pending" | tee -a status/hold.log
