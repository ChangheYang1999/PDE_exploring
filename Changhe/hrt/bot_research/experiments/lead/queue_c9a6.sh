#!/bin/bash
# Cycle-9 queue, chain A, sixth version (written 2026-10-31T10:25Z; one computation slot). Replaces queue_c9a5.sh,
# whose s16 screen was stopped after 3 minutes (its partial output removed) because fx1a showed V17 (best_v9b's
# twin, foreign policy econ17) at 4-0-20 against the new foreign opponents. Order:
#   fx1b  V18B with foreign_target fortress26 and econ19 on new_foreign (fortress v25, v26, econ19), 4 scenarios;
#   fx1c  the same two candidates on old_foreign (the six older foreign-map opponents);
#   s16   stateful forecaster screen of V18E (MODEL=v18 GRID=full COUNTER=stateful).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V18B="bot_research.experiments.lead.v18:@make?$P"
SC="--scenarios mirror:1:2 asym:3:2 mirror:22:3 asym:23:2"
bot_research/experiments/lead/run_pool.sh new_foreign fx1b "'$V18B&foreign_target=\"fortress26\"' '$V18B&foreign_target=\"econ19\"'" $SC --keep-logs losses > bot_research/runs/lead/fx1b.out 2>&1
echo "fx1b done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh old_foreign fx1c "'$V18B&foreign_target=\"fortress26\"' '$V18B&foreign_target=\"econ19\"'" $SC --keep-logs losses > bot_research/runs/lead/fx1c.out 2>&1
echo "fx1c done $(date -u +%FT%TZ)"
Q='"big_threat":100,"gun_cap":120,"poke_until":3,"big_partial":true,"r1_poke":3,"attack_mode":"adaptive","poke_reactive":"turret","fortress_n":4,"immune_attack":true,"foreign_policy":"econ17","mid_until":5'
MODEL=v18 GRID=full COUNTER=stateful bot_research/experiments/lead/run_screens.sh s16 "{$Q,\"mid_joint\":0.75,\"fortress_guns\":true,\"catch_up\":true}" > bot_research/runs/lead/s16.out 2>&1
echo "== queue_c9a6 done $(date -u +%FT%TZ)"
