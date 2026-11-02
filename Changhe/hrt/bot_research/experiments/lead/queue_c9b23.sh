#!/bin/bash
# Cycle-9 queue, chain B, twenty-third version (written 2026-10-31T13:21Z; one computation slot). Replaces queue_c9b22.sh (stopped while it waited; its smoke output name was taken by freeze_v9e.sh), which replaced queue_c9b21.sh (stopped
# while its st1 tournament, PID 3791184, kept running): the promotion smoke of c9b21 failed with exit 2 because the
# runner does not overwrite runs/best-vs-idle-000001.jsonl (written 02:26Z); this queue repeats it with a unique
# output name. The promotion unit tests passed (12 tests OK, runs/lead/promote_v9e/tests.out). Waits for st1, then
#   smoke  the smoke command with --output bot_research/runs/best-vs-idle-bestpy-v9e-000001.jsonl;
#   b9b  P5T and P5TF on BLUFFCOV (pair with b9a);
#   t8h  P5T and P5TF on TARGETED2 (pair with t8f);
#   t9i  P5T and P5TF on TARGETED3_P5TF (TEAMMATES3, GuardedForecast with an exact model of P5TF, fortress v32).
# P5T = v24 passive_until=5&poke_reactive="turret_only"; P5TF = P5T&fail_limit=2.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 3791184 2>/dev/null; do sleep 15; done
echo "st1 done (seen by c9b23) $(date -u +%FT%TZ)"
OUT=bot_research/runs/lead/promote_v9e
.venv/bin/python -B -m td_game.runner --balanced --bot-a bot_research.bots.best:decide --bot-b td_bots.protocol:idle \
  --output bot_research/runs/best-vs-idle-bestpy-v9e-000001.jsonl > $OUT/smoke2.out 2>&1
echo "smoke exit $? $(date -u +%FT%TZ)"
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V18FT="bot_research.experiments.lead.v19:@make?$P&fortress_guns=true&catch_up=true&foreign_target=\"econ20\""
P5T="bot_research.experiments.lead.v24:@make?passive_until=5&poke_reactive=\"turret_only\""
P5TF="$P5T&fail_limit=2"
bot_research/experiments/lead/run_pool.sh bluffcov b9b "'$P5T' '$P5TF'" --keep-logs losses > bot_research/runs/lead/b9b.out 2>&1
echo "b9b done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted2 t8h "'$P5T' '$P5TF'" --keep-logs losses > bot_research/runs/lead/t8h.out 2>&1
echo "t8h done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted3_p5tf t9i "'$P5T' '$P5TF'" --keep-logs losses > bot_research/runs/lead/t9i.out 2>&1
echo "== queue_c9b23 done $(date -u +%FT%TZ)"
