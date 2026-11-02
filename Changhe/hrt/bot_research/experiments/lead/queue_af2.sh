#!/bin/bash
# Slot A (2026-10-31T18:42Z): rest of the f5t ablation ladder of the installed best_v9f: without the passive rule, immune_attack,
# the round-2..5 mid insurance, the round-1 poke and poke insurance (af2, af4-af7). f5t without the round-5 mid step
# (af3) is run xm_f (V33M). Waits for the PID in $1.
cd "$(dirname "$0")/../../.." || exit 1
while [ -n "$1" ] && kill -0 "$1" 2>/dev/null; do sleep 20; done
B='bot_research.experiments.lead.frozen.best_v9f:@make'
for job in "f5t af2 $B?passive_until=null" "f5t af4 $B?immune_attack=false" "f5t af5 $B?mid_until=null" \
           "f5t af6 $B?r1_poke=0" "f5t af7 $B?poke_insurance=false"; do
  set -- $job
  echo "start $2 ($1) $3 $(date -u +%FT%TZ)"
  bot_research/experiments/lead/run_pool.sh $1 $2 "'$3'" --keep-logs losses > bot_research/runs/lead/$2.out 2>&1
  echo "end $2 exit $? $(date -u +%FT%TZ)"
done
echo "== queue_af2 done $(date -u +%FT%TZ)"
