#!/bin/bash
# Cycle-9 queue, chain B, nineteenth version (written 2026-10-31T13:04Z; one computation slot). Replaces queue_c9b18.sh (stopped
# while it waited). Waits for the orphaned freeze_v9e.sh (PID 3003975), then
#   q25  v25 variants on pools.py ROSTER_BAIT (35 settings, both seats): R5 = passive_until=5&passive_ratio=0.5,
#        R5D = R5&passive_defend=false, B100 = passive_until=5&passive_bait=100;
#   b9b  P5 and R5 on BLUFFCOV (pair with b9a);
#   t8h  P5 and R5 on TARGETED2 (pair with t8f);
#   t9i  P5 on TARGETED3_P5 (TEAMMATES3, GuardedForecast with an exact model of P5, fortress v32).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 3003975 2>/dev/null; do sleep 15; done
echo "freeze_v9e done (seen by c9b19) $(date -u +%FT%TZ)"
P5="bot_research.experiments.lead.v24:@make?passive_until=5"
R5="bot_research.experiments.lead.v25:@make?passive_until=5&passive_ratio=0.5"
R5D="bot_research.experiments.lead.v25:@make?passive_until=5&passive_ratio=0.5&passive_defend=false"
B100="bot_research.experiments.lead.v25:@make?passive_until=5&passive_bait=100"
bot_research/experiments/lead/run_pool.sh roster_bait q25 "'$R5' '$R5D' '$B100'" --keep-logs losses > bot_research/runs/lead/q25.out 2>&1
echo "q25 done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh bluffcov b9b "'$P5' '$R5'" --keep-logs losses > bot_research/runs/lead/b9b.out 2>&1
echo "b9b done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted2 t8h "'$P5' '$R5'" --keep-logs losses > bot_research/runs/lead/t8h.out 2>&1
echo "t8h done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted3_p5 t9i "'$P5'" --keep-logs losses > bot_research/runs/lead/t9i.out 2>&1
echo "== queue_c9b19 done $(date -u +%FT%TZ)"
