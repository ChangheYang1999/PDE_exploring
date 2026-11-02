#!/bin/bash
# Written 2026-10-31T22:33Z. Runs the last three f5t ablations of best_v9e that queue_h15.sh dropped (ab4
# big_partial=false, ab5 fortress_n=null, ab12 big_threat=null) in the slot that queue_h16 A freed at 22:32:46Z, one
# at a time, next to queue_h17 (frr3, frr4). Descriptive only; base ab1 (f5t 70-6-0); best.py is not changed.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
L=bot_research/runs/lead
. bot_research/experiments/lead/rr_specs.sh
B="$BEST_V9E"
pool() { echo "start $2 ($1) $3 $(date -u +%FT%TZ)"; bot_research/experiments/lead/run_pool.sh $1 $2 "'$3'" --keep-logs losses > $L/$2.out 2>&1; echo "end $2 exit $? $(date -u +%FT%TZ)"; }
pool f5t ab4 "$B?big_partial=false"; pool f5t ab5 "$B?fortress_n=null"; pool f5t ab12 "$B?big_threat=null"
echo "== queue_h18 done $(date -u +%FT%TZ)"
