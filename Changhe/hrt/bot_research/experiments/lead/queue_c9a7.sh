#!/bin/bash
# Cycle-9 queue, chain A, seventh version (written 2026-10-31T10:27Z; one computation slot). Replaces queue_c9a6.sh
# while its fx1b tournament runs (PID 575276, left running), to add the two foreign targets of experiments/lead/v19.py
# (econ20 with the re-planner, fortress27). After fx1b:
#   fx1d  V19 with foreign_target econ20 and fortress27 on new_foreign, 4 scenarios;
#   fx1c  V18B foreign_target econ19 and V19 foreign_target econ20 on old_foreign (the deterministic targets);
#   s16   stateful forecaster screen of V18E.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 575276 2>/dev/null; do sleep 15; done
echo "fx1b done (seen by c9a7) $(date -u +%FT%TZ)"
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V18B="bot_research.experiments.lead.v18:@make?$P"
V19="bot_research.experiments.lead.v19:@make?$P"
SC="--scenarios mirror:1:2 asym:3:2 mirror:22:3 asym:23:2"
bot_research/experiments/lead/run_pool.sh new_foreign fx1d "'$V19&foreign_target=\"econ20\"' '$V19&foreign_target=\"fortress27\"'" $SC --keep-logs losses > bot_research/runs/lead/fx1d.out 2>&1
echo "fx1d done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh old_foreign fx1c "'$V18B&foreign_target=\"econ19\"' '$V19&foreign_target=\"econ20\"'" $SC --keep-logs losses > bot_research/runs/lead/fx1c.out 2>&1
echo "fx1c done $(date -u +%FT%TZ)"
Q='"big_threat":100,"gun_cap":120,"poke_until":3,"big_partial":true,"r1_poke":3,"attack_mode":"adaptive","poke_reactive":"turret","fortress_n":4,"immune_attack":true,"foreign_policy":"econ17","mid_until":5'
MODEL=v18 GRID=full COUNTER=stateful bot_research/experiments/lead/run_screens.sh s16 "{$Q,\"mid_joint\":0.75,\"fortress_guns\":true,\"catch_up\":true}" > bot_research/runs/lead/s16.out 2>&1
echo "== queue_c9a7 done $(date -u +%FT%TZ)"
