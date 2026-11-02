#!/bin/bash
# Cycle-9 queue, chain A, sixteenth version (written 2026-10-31T12:47Z; one computation slot). queue_c9a15.sh was stopped after it
# had started g9a (its tournament, PID 3414226, keeps running) to add hrt-w3's delayed-guard grower
# (notes/validation.md 12:32Z). Waits for g9a, then
#   gm1  V18FT, P5 and P5T on pools.py GUARDED_MAZE (72 settings, both seats);
#   c9n  f5t for P5 (pair with c9i, V18FT 70-6-0).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 3414226 2>/dev/null; do sleep 15; done
echo "g9a done (seen by c9a16) $(date -u +%FT%TZ)"
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V18FT="bot_research.experiments.lead.v19:@make?$P&fortress_guns=true&catch_up=true&foreign_target=\"econ20\""
P5="bot_research.experiments.lead.v24:@make?passive_until=5"
P5T="bot_research.experiments.lead.v24:@make?passive_until=5&poke_reactive=\"turret_only\""
bot_research/experiments/lead/run_pool.sh guarded_maze gm1 "'$V18FT' '$P5' '$P5T'" --keep-logs losses > bot_research/runs/lead/gm1.out 2>&1
echo "gm1 done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh f5t c9n "'$P5'" --keep-logs losses > bot_research/runs/lead/c9n.out 2>&1
echo "== queue_c9a16 done $(date -u +%FT%TZ)"
