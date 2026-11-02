#!/bin/bash
# 2026-10-31T18:46Z: ablation ladder of the reinstalled final bot best_v9e (frozen file, defaults otherwise), the runs left
# undone at 16:30Z (specs as in queue_ab1.sh and queue_ab2.sh; ab1, ab7, ab8 done; ab13 = GROWERS of the twin V18FT,
# runs g9a-g9d). Waits for the PID in $1.
cd "$(dirname "$0")/../../.." || exit 1
while [ -n "$1" ] && kill -0 "$1" 2>/dev/null; do sleep 20; done
B='bot_research.experiments.lead.frozen.best_v9e:@make'
for job in "f5t ab2 $B?r1_poke=0" "f5t ab3 $B?spec_share=0&big_threat=null&poke_insurance=false&mid_until=null" "f5t ab4 $B?big_partial=false" "f5t ab5 $B?fortress_n=null" "f5t ab6 $B?attack_mode=\"current\"" "growers ab14 $B?spec_share=0&big_threat=null&poke_insurance=false&mid_until=null" "growers ab15 $B?big_threat=null"; do
  set -- $job
  echo "start $2 ($1) $3 $(date -u +%FT%TZ)"
  bot_research/experiments/lead/run_pool.sh $1 $2 "'$3'" --keep-logs losses > bot_research/runs/lead/$2.out 2>&1
  echo "end $2 exit $? $(date -u +%FT%TZ)"
done
echo "== queue_ab3 done $(date -u +%FT%TZ)"
