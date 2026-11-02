#!/bin/bash
# Cycle-9 queue, chain B, twenty-sixth version (written 2026-10-31T14:04Z; one computation slot). Replaces queue_c9b25.sh (stopped
# while its st2 tournament, PID 43459, kept running): P5TNUB (v28, behind_mode="current") replaces P5TF. Waits for st2, then
#   g9b  GROWERS: P5TNU, P5TNUB (pair with g9a);
#   b9b  BLUFFCOV: P5TNU, P5TNUB (pair with b9a);
#   t8h  TARGETED2: P5TNU, P5TNUB (pair with t8f);
#   t9i  TARGETED3_P5TF (TEAMMATES3, GuardedForecast with an exact model of P5TF, fortress v32): P5TNU, P5TNUB;
#   st3  STAGED: P5TNUB (pair with st1, st2);
#   sg2  SCREENED: P5TNUB (pair with sg1).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 43459 2>/dev/null; do sleep 15; done
echo "st2 done (seen by c9b26) $(date -u +%FT%TZ)"
PAR="passive_until=5&poke_reactive=\"turret_only\"&fail_limit=2&passive_turret=false&robust_k=null"
P5TNU="bot_research.experiments.lead.v27:@make?$PAR"
P5TNUB="bot_research.experiments.lead.v28:@make?$PAR&behind_mode=\"current\""
bot_research/experiments/lead/run_pool.sh growers g9b "'$P5TNU' '$P5TNUB'" --keep-logs losses > bot_research/runs/lead/g9b.out 2>&1
echo "g9b done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh bluffcov b9b "'$P5TNU' '$P5TNUB'" --keep-logs losses > bot_research/runs/lead/b9b.out 2>&1
echo "b9b done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted2 t8h "'$P5TNU' '$P5TNUB'" --keep-logs losses > bot_research/runs/lead/t8h.out 2>&1
echo "t8h done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted3_p5tf t9i "'$P5TNU' '$P5TNUB'" --keep-logs losses > bot_research/runs/lead/t9i.out 2>&1
echo "t9i done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh staged st3 "'$P5TNUB'" --keep-logs losses > bot_research/runs/lead/st3.out 2>&1
echo "st3 done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh screened sg2 "'$P5TNUB'" --keep-logs losses > bot_research/runs/lead/sg2.out 2>&1
echo "== queue_c9b26 done $(date -u +%FT%TZ)"
