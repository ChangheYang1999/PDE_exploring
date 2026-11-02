#!/bin/bash
# Written 2026-10-31T21:41Z. Restores three of the f5t ablations of best_v9e that queue_h15.sh dropped and that
# best_v9f's af8-af10 do not cover: ab6 attack_mode="current", ab10 catch_up=false (slot A, after queue_h15 A, PID
# 844574, exits) and ab11 fortress_guns=false (slot B, after queue_h15 B, PID 844575). Descriptive only: the
# selection is final and nothing here changes bots/best.py. Usage: queue_h16.sh A|B.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
L=bot_research/runs/lead
. bot_research/experiments/lead/rr_specs.sh
B="$BEST_V9E"
pool() {  # POOL NAME SPEC
  echo "start $2 ($1) $3 $(date -u +%FT%TZ)"
  bot_research/experiments/lead/run_pool.sh $1 $2 "'$3'" --keep-logs losses > $L/$2.out 2>&1
  echo "end $2 exit $? $(date -u +%FT%TZ)"
}
if [ "$1" = A ]; then
  while kill -0 844574 2>/dev/null; do sleep 10; done
  pool f5t ab6 "$B?attack_mode=\"current\""
  pool f5t ab10 "$B?catch_up=false"
elif [ "$1" = B ]; then
  while kill -0 844575 2>/dev/null; do sleep 10; done
  pool f5t ab11 "$B?fortress_guns=false"
fi
echo "== queue_h16 $1 done $(date -u +%FT%TZ)"
