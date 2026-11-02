#!/bin/bash
# Cycle-9 queue, chain B, eighteenth version (written 2026-10-31T12:44Z; one computation slot). Replaces queue_c9b17.sh while its
# freeze_v9e.sh ran (s19 dropped for now). Waits for the orphaned freeze_v9e.sh (PID 3003975), then
#   t9i  P5 (v24 passive_until=5) on TARGETED3_P5 (TEAMMATES3, GuardedForecast with an exact model of P5, fortress v32);
#   b9b  P5 on BLUFFCOV (pair with b9a);
#   t8h  P5 on TARGETED2 (pair with t8f).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 3003975 2>/dev/null; do sleep 15; done
echo "freeze_v9e done (seen by c9b18) $(date -u +%FT%TZ)"
P5="bot_research.experiments.lead.v24:@make?passive_until=5"
bot_research/experiments/lead/run_pool.sh targeted3_p5 t9i "'$P5'" --keep-logs losses > bot_research/runs/lead/t9i.out 2>&1
echo "t9i done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh bluffcov b9b "'$P5'" --keep-logs losses > bot_research/runs/lead/b9b.out 2>&1
echo "b9b done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted2 t8h "'$P5'" --keep-logs losses > bot_research/runs/lead/t8h.out 2>&1
echo "== queue_c9b18 done $(date -u +%FT%TZ)"
