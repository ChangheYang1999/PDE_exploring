#!/bin/bash
# Cycle-9 queue, chain B, twenty-first version (written 2026-10-31T13:16Z; one computation slot). Replaces queue_c9b20.sh (stopped
# after q25 and the sha256 check, while its unit-test child, PID 3777882, kept running) to test P5T and P5TF instead of P5 and R5
# (g9a: P5T 142-0-0, P5 138-0-4; hrt-w3 13:14Z: fail_limit=2 repairs P5's staged-guard loss). Waits for that
# test run (output runs/lead/promote_v9e/tests.out), then
#   smoke  the official smoke command (runs/lead/promote_v9e/smoke.out);
#   st1  V18FT, P5T and P5TF on pools.py STAGED (70 settings, both seats);
#   b9b  P5T and P5TF on BLUFFCOV (pair with b9a);
#   t8h  P5T and P5TF on TARGETED2 (pair with t8f);
#   t9i  P5T and P5TF on TARGETED3_P5TF (TEAMMATES3, GuardedForecast with an exact model of P5TF, fortress v32).
# P5T = v24 passive_until=5&poke_reactive="turret_only"; P5TF = P5T&fail_limit=2.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 3777882 2>/dev/null; do sleep 15; done
echo "tests done (seen by c9b21) $(date -u +%FT%TZ): $(tail -1 bot_research/runs/lead/promote_v9e/tests.out)"
OUT=bot_research/runs/lead/promote_v9e
.venv/bin/python -B -m td_game.runner --balanced --bot-a bot_research.bots.best:decide --bot-b td_bots.protocol:idle \
  --output bot_research/runs/best-vs-idle-000001.jsonl > $OUT/smoke.out 2>&1
echo "smoke exit $? $(date -u +%FT%TZ)"
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V18FT="bot_research.experiments.lead.v19:@make?$P&fortress_guns=true&catch_up=true&foreign_target=\"econ20\""
P5T="bot_research.experiments.lead.v24:@make?passive_until=5&poke_reactive=\"turret_only\""
P5TF="$P5T&fail_limit=2"
bot_research/experiments/lead/run_pool.sh staged st1 "'$V18FT' '$P5T' '$P5TF'" --keep-logs losses > bot_research/runs/lead/st1.out 2>&1
echo "st1 done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh bluffcov b9b "'$P5T' '$P5TF'" --keep-logs losses > bot_research/runs/lead/b9b.out 2>&1
echo "b9b done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted2 t8h "'$P5T' '$P5TF'" --keep-logs losses > bot_research/runs/lead/t8h.out 2>&1
echo "t8h done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted3_p5tf t9i "'$P5T' '$P5TF'" --keep-logs losses > bot_research/runs/lead/t9i.out 2>&1
echo "== queue_c9b21 done $(date -u +%FT%TZ)"
