#!/bin/bash
# Slot B after queue_v33b (written 2026-10-31T17:23Z): the frozen best_v9e (= V18FT on the standard start) on the three broad
# development pools that have no V18FT rows (SCREENED, HANDOFF, TIMING; runs bse_sg, bse_hd, bse_tm), so that the
# second stage of the 14:49Z gate compares V33C with the installed bot on every broad pool. Waits for the PID in $1.
cd "$(dirname "$0")/../../.." || exit 1
while [ -n "$1" ] && kill -0 "$1" 2>/dev/null; do sleep 20; done
B='bot_research.experiments.lead.frozen.best_v9e:@make'
for job in "screened bse_sg" "handoff bse_hd" "timing bse_tm"; do
  set -- $job
  echo "start $2 ($1) $(date -u +%FT%TZ)"
  bot_research/experiments/lead/run_pool.sh $1 $2 "'$B'" --keep-logs losses > bot_research/runs/lead/$2.out 2>&1
  echo "end $2 exit $? $(date -u +%FT%TZ)"
done
echo "== queue_bse done $(date -u +%FT%TZ)"
