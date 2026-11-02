#!/bin/bash
# Cycle-9 queue, chain A, fifth version (written 2026-10-31T10:17Z; one computation slot). Replaces queue_c9a4.sh
# while its fx1a tournament runs (PID 277641, left running). The candidate changed to V18E (queue_c9b6.sh), so
# after fx1a:
#   s16  stateful forecaster screen of V18E (MODEL=v18 GRID=full COUNTER=stateful);
#   s15  the same screen of V17 (the baseline);
# fx1b (foreign targets) is decided after fx1a has been read.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 277641 2>/dev/null; do sleep 15; done
echo "fx1a done (seen by c9a5) $(date -u +%FT%TZ)"
Q='"big_threat":100,"gun_cap":120,"poke_until":3,"big_partial":true,"r1_poke":3,"attack_mode":"adaptive","poke_reactive":"turret","fortress_n":4,"immune_attack":true,"foreign_policy":"econ17","mid_until":5'
MODEL=v18 GRID=full COUNTER=stateful bot_research/experiments/lead/run_screens.sh s16 "{$Q,\"mid_joint\":0.75,\"fortress_guns\":true,\"catch_up\":true}" > bot_research/runs/lead/s16.out 2>&1
echo "s16 done $(date -u +%FT%TZ)"
MODEL=v17 GRID=full COUNTER=stateful bot_research/experiments/lead/run_screens.sh s15 "{$Q}" > bot_research/runs/lead/s15.out 2>&1
echo "== queue_c9a5 done $(date -u +%FT%TZ)"
