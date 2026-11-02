#!/bin/bash
# Cycle-9 queue, chain B continuation (written 2026-10-31T09:46Z; one computation slot). Waits until queue_c9b2.sh has
# finished, then:
#   fx1c  V17 against the six older foreign-map opponents (pools.py OLD_FOREIGN) under the four sc1 openings, so
#         that V17 (fx1a + fx1c) and the two foreign targets (fx1b) are compared on the same 72 conditions;
#   s16   the stateful forecaster screen (hrt-w3's stateful_public timing counter with a persistent private model
#         of the candidate, full grid, both seats) of V18c = V17 + mid_joint=1.0 + fortress_guns=true; compare
#         with s15 (V17, chain A) and with hrt-w3's lead-seventeen-mid5-standard campaign (counter 16-8-2).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
until grep -q "queue_c9b2 done" bot_research/runs/lead/queue_c9b2.out 2>/dev/null; do sleep 30; done
echo "start $(date -u +%FT%TZ)"
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V17="bot_research.experiments.lead.v17:@make?$P"
SC="--scenarios mirror:1:2 asym:3:2 mirror:22:3 asym:23:2"
bot_research/experiments/lead/run_pool.sh old_foreign fx1c "'$V17'" $SC --keep-logs losses > bot_research/runs/lead/fx1c.out 2>&1
echo "fx1c done $(date -u +%FT%TZ)"
Q='"big_threat":100,"gun_cap":120,"poke_until":3,"big_partial":true,"r1_poke":3,"attack_mode":"adaptive","poke_reactive":"turret","fortress_n":4,"immune_attack":true,"foreign_policy":"econ17","mid_until":5,"mid_joint":1.0,"fortress_guns":true'
MODEL=v18 GRID=full COUNTER=stateful bot_research/experiments/lead/run_screens.sh s16 "{$Q}" > bot_research/runs/lead/s16.out 2>&1
echo "== queue_c9b3 done $(date -u +%FT%TZ)"
