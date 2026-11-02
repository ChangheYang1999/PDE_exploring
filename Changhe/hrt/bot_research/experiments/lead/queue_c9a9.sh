#!/bin/bash
# Cycle-9 queue, chain A, ninth version (written 2026-10-31T11:19Z; one computation slot). Replaces queue_c9a8.sh, whose s16
# screen of V18F was stopped after 8 of 54 games (partial output moved to bot_research/tmp/stale/): the candidate
# is now V20T (queue_c9b11.sh). Steps:
#   freeze  experiments/lead/freeze_v9c.sh (frozen/best_v9c.py against its twin V20T; tests; smoke);
#   s17     stateful forecaster screen of V20T (MODEL=v20, GRID=full).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
bash bot_research/experiments/lead/freeze_v9c.sh > bot_research/runs/lead/freeze_v9c.log 2>&1
echo "freeze checks done $(date -u +%FT%TZ)"
Q='"big_threat":100,"gun_cap":120,"poke_until":3,"big_partial":true,"r1_poke":3,"attack_mode":"adaptive","poke_reactive":"turret","fortress_n":4,"immune_attack":true,"foreign_policy":"econ17","mid_until":5'
MODEL=v20 GRID=full COUNTER=stateful bot_research/experiments/lead/run_screens.sh s17 "{$Q,\"fortress_guns\":true,\"catch_up\":true,\"mid_joint\":0.75,\"mid_level\":true,\"foreign_target\":\"econ20\"}" > bot_research/runs/lead/s17.out 2>&1
echo "== queue_c9a9 done $(date -u +%FT%TZ)"
