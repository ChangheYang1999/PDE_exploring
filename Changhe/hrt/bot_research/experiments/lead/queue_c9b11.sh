#!/bin/bash
# Cycle-9 queue, chain B, eleventh version (written 2026-10-31T11:17Z; one computation slot). Runs after queue_c9b10.sh (PID
# 847729, t8g). The best_v9c candidate is V20T = v20 P&fortress_guns=true&catch_up=true&mid_joint=0.75&mid_level=true
# &foreign_target="econ20" (t8g V20L 22-22-2 on 46 of 48 TARGETED2 conditions against V18F 22-20-4; fx1c/fx1d: econ20
# the best foreign-map target). The foreign target never acts on the standard start.
#   c9h  f5t for V20T (V17 68-4-4 in c8m);
#   c9i  f5t for V18FT = v19 P&fortress_guns=true&catch_up=true&foreign_target="econ20" (ablation of mid_joint).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 847729 2>/dev/null; do sleep 15; done
echo "t8g done (seen by c9b11) $(date -u +%FT%TZ)"
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V20T="bot_research.experiments.lead.v20:@make?$P&fortress_guns=true&catch_up=true&mid_joint=0.75&mid_level=true&foreign_target=\"econ20\""
V18FT="bot_research.experiments.lead.v19:@make?$P&fortress_guns=true&catch_up=true&foreign_target=\"econ20\""
bot_research/experiments/lead/run_pool.sh f5t c9h "'$V20T'" --keep-logs losses > bot_research/runs/lead/c9h.out 2>&1
echo "c9h done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh f5t c9i "'$V18FT'" --keep-logs losses > bot_research/runs/lead/c9i.out 2>&1
echo "== queue_c9b11 done $(date -u +%FT%TZ)"
