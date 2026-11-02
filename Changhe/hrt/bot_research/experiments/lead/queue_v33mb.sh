#!/bin/bash
# Gate of V33M = frozen best_v9f with passive_mid_from=null (rule in NOTES_FOR_TEAM 2026-10-31T18:29Z), slot B.
# Stage 1 pools first in slot A; reference rows are the x33* runs of V33C. Waits for the PID in $1.
cd "$(dirname "$0")/../../.." || exit 1
while [ -n "$1" ] && kill -0 "$1" 2>/dev/null; do sleep 20; done
S='bot_research.experiments.lead.frozen.best_v9f:@make?passive_mid_from=null'
for job in "guarded_maze xm_gm" "screened xm_sg" "timing xm_tm" "strike1 xm_s1"; do
  set -- $job
  echo "start $2 ($1) $S $(date -u +%FT%TZ)"
  bot_research/experiments/lead/run_pool.sh $1 $2 "'$S'" --keep-logs losses > bot_research/runs/lead/$2.out 2>&1
  echo "end $2 exit $? $(date -u +%FT%TZ)"
done
echo "== queue_v33mb done $(date -u +%FT%TZ)"
