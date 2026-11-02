#!/bin/bash
# Slot A (written 2026-10-31T17:46Z): replaces queue_frz.sh, whose call of freeze_v9f.sh failed with exit 126 (the script is not
# executable; it is now run with bash) and which was stopped by process group during af2 (partial af2 moved to
# tmp/aborted/af2_1745Z). x9fs1 had completed. Runs the freeze checks, then af2-af7 as planned.
cd "$(dirname "$0")/../../.." || exit 1
echo "start freeze_v9f V33C $(date -u +%FT%TZ)"
bash bot_research/experiments/lead/freeze_v9f.sh V33C > bot_research/runs/lead/freeze_v9f.log 2>&1
echo "end freeze_v9f exit $? $(date -u +%FT%TZ)"
B='bot_research.experiments.lead.frozen.best_v9f:@make'
for job in "f5t af2 $B?passive_until=null" "f5t af3 $B?passive_mid_from=null" \
           "f5t af4 $B?immune_attack=false" "f5t af5 $B?mid_until=null" "f5t af6 $B?r1_poke=0" \
           "f5t af7 $B?poke_insurance=false"; do
  set -- $job
  echo "start $2 ($1) $3 $(date -u +%FT%TZ)"
  bot_research/experiments/lead/run_pool.sh $1 $2 "'$3'" --keep-logs losses > bot_research/runs/lead/$2.out 2>&1
  echo "end $2 exit $? $(date -u +%FT%TZ)"
done
echo "== queue_frz2 done $(date -u +%FT%TZ)"
