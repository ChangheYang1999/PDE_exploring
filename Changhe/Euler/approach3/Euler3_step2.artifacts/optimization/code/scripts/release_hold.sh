#!/bin/bash
# Return every held job file to queue/pending (inverse of hold_exclusive.sh).
ROOT=$(cd "$(dirname "$0")/.." && pwd); cd $ROOT
n=$(ls queue/hold/*.json 2>/dev/null | wc -l)
[ "$n" -gt 0 ] && mv queue/hold/*.json queue/pending/
echo "$(date -u +%FT%TZ) released $n held jobs to queue/pending" | tee -a status/hold.log
