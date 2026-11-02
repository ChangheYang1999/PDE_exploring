#!/bin/bash
# Cycle-9 queue, chain B, tenth version (written 2026-10-31T10:44Z; one computation slot). Runs after queue_c9b9.sh's
# t8f tournament (PID 837365). experiments/lead/v20.py gates mid_joint on our HP being at least the opponent's:
#   t8g  TARGETED2 for V20L = v20 P&fortress_guns=true&catch_up=true&mid_joint=0.75&mid_level=true.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 837365 2>/dev/null; do sleep 15; done
echo "t8f done (seen by c9b10) $(date -u +%FT%TZ)"
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V20L="bot_research.experiments.lead.v20:@make?$P&fortress_guns=true&catch_up=true&mid_joint=0.75&mid_level=true"
bot_research/experiments/lead/run_pool.sh targeted2 t8g "'$V20L'" --keep-logs losses > bot_research/runs/lead/t8g.out 2>&1
echo "== queue_c9b10 done $(date -u +%FT%TZ)"
