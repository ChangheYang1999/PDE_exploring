#!/bin/bash
# Ablation ladder of the installed bot (written 2026-10-31T16:14Z), chain 2 of 2: further single-component switches of the frozen
# best_v9e on f5t, then the insurance switches and the base on GROWERS (hrt-w3's passive growers, 142 games).
cd "$(dirname "$0")/../../.." || exit 1
while [ -n "$1" ] && kill -0 "$1" 2>/dev/null; do sleep 20; done
B='bot_research.experiments.lead.frozen.best_v9e:@make'
for job in "f5t ab7 $B?immune_attack=false" "f5t ab8 $B?mid_until=null" "f5t ab9 $B?poke_insurance=false" \
           "f5t ab10 $B?catch_up=false" "f5t ab11 $B?fortress_guns=false" "f5t ab12 $B?big_threat=null" \
           "growers ab13 $B" "growers ab14 $B?spec_share=0&big_threat=null&poke_insurance=false&mid_until=null" \
           "growers ab15 $B?big_threat=null" "growers ab16 $B?poke_insurance=false" "growers ab17 $B?mid_until=null"; do
  set -- $job
  echo "start $2 ($1) $3 $(date -u +%FT%TZ)"
  bot_research/experiments/lead/run_pool.sh $1 $2 "'$3'" --keep-logs losses > bot_research/runs/lead/$2.out 2>&1
  echo "end $2 exit $? $(date -u +%FT%TZ)"
done
echo "== queue_ab2 done $(date -u +%FT%TZ)"
