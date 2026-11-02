#!/bin/bash
# Ablation ladder of the installed bot (written 2026-10-31T16:14Z): the frozen best_v9e and single-component switches, on f5t
# (FRONTIER5 + hrt-w3's targeted counters, 38 opponents, both seats). Chain 1 of 2; one tournament job each.
# Waits for the PID given as $1 (the previous job in this slot) to exit.
cd "$(dirname "$0")/../../.." || exit 1
while [ -n "$1" ] && kill -0 "$1" 2>/dev/null; do sleep 20; done
B='bot_research.experiments.lead.frozen.best_v9e:@make'
for job in "f5t ab1 $B" "f5t ab2 $B?r1_poke=0" "f5t ab3 $B?spec_share=0&big_threat=null&poke_insurance=false&mid_until=null" \
           "f5t ab4 $B?big_partial=false" "f5t ab5 $B?fortress_n=null" "f5t ab6 $B?attack_mode=\"current\""; do
  set -- $job
  echo "start $2 ($1) $3 $(date -u +%FT%TZ)"
  bot_research/experiments/lead/run_pool.sh $1 $2 "'$3'" --keep-logs losses > bot_research/runs/lead/$2.out 2>&1
  echo "end $2 exit $? $(date -u +%FT%TZ)"
done
echo "== queue_ab1 done $(date -u +%FT%TZ)"
