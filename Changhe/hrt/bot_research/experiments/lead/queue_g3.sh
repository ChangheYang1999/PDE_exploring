#!/bin/bash
# 2026-10-31T19:08Z: which of the four option values that separate af2g from best_v9e carries the GROWERS gain
# (af2g 128-0-14 against best_v9e 66-0-76; section 5.14). best_v9e with one option at a time, GROWERS (142 games,
# both seats). Descriptive ablation, no selection rule depends on it. Waits for the PID in $1 (queue_g1, slot A).
cd "$(dirname "$0")/../../.." || exit 1
while [ -n "$1" ] && kill -0 "$1" 2>/dev/null; do sleep 20; done
B='bot_research.experiments.lead.frozen.best_v9e:@make'
for job in "growers gx1 $B?poke_reactive=\"turret_only\"" "growers gx2 $B?fail_limit=2" "growers gx3 $B?robust_k=null" \
           "growers gx4 $B?behind_mode=\"current\""; do
  set -- $job
  echo "start $2 ($1) $3 $(date -u +%FT%TZ)"
  bot_research/experiments/lead/run_pool.sh $1 $2 "'$3'" --keep-logs losses > bot_research/runs/lead/$2.out 2>&1
  echo "end $2 exit $? $(date -u +%FT%TZ)"
done
echo "== queue_g3 done $(date -u +%FT%TZ)"
