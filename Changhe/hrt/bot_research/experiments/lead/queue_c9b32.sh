#!/bin/bash
# Cycle-9 queue c9b32 (written 2026-10-31T15:26Z; one computation slot). Waits for queue_c9b31 (PID 831497: tm2, then tm3 TIMING2
# with M2 and M3), then the broad pools for M2: st3 STAGED, sg2 SCREENED, hd2 HANDOFF.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
PAR="poke_reactive=\"turret_only\"&fail_limit=2&passive_turret=false&robust_k=null&behind_mode=\"current\""
M2="bot_research.experiments.lead.v30:@make?passive_until=5&$PAR&passive_mid_from=2"
while kill -0 831497 2>/dev/null; do sleep 10; done
echo "queue_c9b31 done (seen by queue_c9b32) $(date -u +%FT%TZ)"
for job in "staged st3" "screened sg2" "handoff hd2"; do
  set -- $job
  echo "start $2 ($1) $(date -u +%FT%TZ)"
  bot_research/experiments/lead/run_pool.sh $1 $2 "'$M2'" --keep-logs losses > bot_research/runs/lead/$2.out 2>&1
  echo "end $2 exit $? $(date -u +%FT%TZ)"
done
echo "== queue_c9b32 done $(date -u +%FT%TZ)"
