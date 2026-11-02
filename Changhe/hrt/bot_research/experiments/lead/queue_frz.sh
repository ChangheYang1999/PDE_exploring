#!/bin/bash
# Slot A after queue_v33a (written 2026-10-31T17:35Z; replaces queue_v34q.sh, stopped before it started any job, because V33C passed
# the 14:49Z gate and is frozen as experiments/lead/frozen/best_v9f.py). Runs the freeze checks (freeze_v9f.sh V33C,
# log runs/lead/freeze_v9f.log), the frozen file on hrt-w2's strike1 set (x9fs1), then the first half of its
# ablation ladder on f5t (af2-af7). Waits for the PID in $1.
cd "$(dirname "$0")/../../.." || exit 1
while [ -n "$1" ] && kill -0 "$1" 2>/dev/null; do sleep 20; done
echo "start freeze_v9f V33C $(date -u +%FT%TZ)"
bot_research/experiments/lead/freeze_v9f.sh V33C > bot_research/runs/lead/freeze_v9f.log 2>&1
echo "end freeze_v9f exit $? $(date -u +%FT%TZ)"
B='bot_research.experiments.lead.frozen.best_v9f:@make'
for job in "strike1 x9fs1 $B" "f5t af2 $B?passive_until=null" "f5t af3 $B?passive_mid_from=null" \
           "f5t af4 $B?immune_attack=false" "f5t af5 $B?mid_until=null" "f5t af6 $B?r1_poke=0" \
           "f5t af7 $B?poke_insurance=false"; do
  set -- $job
  echo "start $2 ($1) $3 $(date -u +%FT%TZ)"
  bot_research/experiments/lead/run_pool.sh $1 $2 "'$3'" --keep-logs losses > bot_research/runs/lead/$2.out 2>&1
  echo "end $2 exit $? $(date -u +%FT%TZ)"
done
echo "== queue_frz done $(date -u +%FT%TZ)"
