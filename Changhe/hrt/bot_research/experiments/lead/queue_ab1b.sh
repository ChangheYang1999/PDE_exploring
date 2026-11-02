#!/bin/bash
# Replaces queue_ab1.sh after its ab1 run (written 2026-10-31T16:23Z): waits for the ab1 tournament (PID $1) to exit, runs the
# quick v33 games (qg_v33.sh, runs/lead/qg_v33.out), then the rest of the chain-1 ablations ab2-ab6 unchanged.
cd "$(dirname "$0")/../../.." || exit 1
while [ -n "$1" ] && kill -0 "$1" 2>/dev/null; do sleep 20; done
echo "ab1 tournament exited $(date -u +%FT%TZ)"
echo "start qg_v33 $(date -u +%FT%TZ)"
bot_research/experiments/lead/qg_v33.sh > bot_research/runs/lead/qg_v33.out 2>&1
echo "end qg_v33 exit $? $(date -u +%FT%TZ)"
B='bot_research.experiments.lead.frozen.best_v9e:@make'
for job in "f5t ab2 $B?r1_poke=0" "f5t ab3 $B?spec_share=0&big_threat=null&poke_insurance=false&mid_until=null" \
           "f5t ab4 $B?big_partial=false" "f5t ab5 $B?fortress_n=null" "f5t ab6 $B?attack_mode=\"current\""; do
  set -- $job
  echo "start $2 ($1) $3 $(date -u +%FT%TZ)"
  bot_research/experiments/lead/run_pool.sh $1 $2 "'$3'" --keep-logs losses > bot_research/runs/lead/$2.out 2>&1
  echo "end $2 exit $? $(date -u +%FT%TZ)"
done
echo "== queue_ab1b done $(date -u +%FT%TZ)"
