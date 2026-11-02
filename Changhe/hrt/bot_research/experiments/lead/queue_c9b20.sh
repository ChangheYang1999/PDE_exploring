#!/bin/bash
# Cycle-9 queue, chain B, twentieth version (written 2026-10-31T13:08Z; one computation slot). Replaces queue_c9b19.sh (stopped
# after it had started q25, whose tournament, PID 3651271, keeps running) to add the checks of the promoted best.py
# (best_v9e installed 13:07:59Z). Waits for q25, then
#   promote  sha256 of bots/best.py, tests/test_best.py, the smoke command (runs/lead/promote_v9e/);
#   b9b  P5 and R5 on BLUFFCOV (pair with b9a);
#   t8h  P5 and R5 on TARGETED2 (pair with t8f);
#   t9i  P5 on TARGETED3_P5 (TEAMMATES3, GuardedForecast with an exact model of P5, fortress v32).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 3651271 2>/dev/null; do sleep 15; done
echo "q25 done (seen by c9b20) $(date -u +%FT%TZ)"
OUT=bot_research/runs/lead/promote_v9e
mkdir -p $OUT
sha256sum bot_research/bots/best.py bot_research/experiments/lead/frozen/best_v9e.py > $OUT/sha256.out 2>&1
echo "sha256 exit $? $(date -u +%FT%TZ)"
.venv/bin/python -B -m unittest bot_research.tests.test_best > $OUT/tests.out 2>&1
echo "tests exit $? $(date -u +%FT%TZ)"
.venv/bin/python -B -m td_game.runner --balanced --bot-a bot_research.bots.best:decide --bot-b td_bots.protocol:idle \
  --output bot_research/runs/best-vs-idle-000001.jsonl > $OUT/smoke.out 2>&1
echo "smoke exit $? $(date -u +%FT%TZ)"
P5="bot_research.experiments.lead.v24:@make?passive_until=5"
R5="bot_research.experiments.lead.v25:@make?passive_until=5&passive_ratio=0.5"
bot_research/experiments/lead/run_pool.sh bluffcov b9b "'$P5' '$R5'" --keep-logs losses > bot_research/runs/lead/b9b.out 2>&1
echo "b9b done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted2 t8h "'$P5' '$R5'" --keep-logs losses > bot_research/runs/lead/t8h.out 2>&1
echo "t8h done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted3_p5 t9i "'$P5'" --keep-logs losses > bot_research/runs/lead/t9i.out 2>&1
echo "== queue_c9b20 done $(date -u +%FT%TZ)"
