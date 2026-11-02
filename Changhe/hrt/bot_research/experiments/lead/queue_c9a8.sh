#!/bin/bash
# Cycle-9 queue, chain A, eighth version (written 2026-10-31T11:08Z; one computation slot). Replaces queue_c9a7.sh while its fx1c
# tournament runs (PID 1435751, left running): V18E was rejected (t8e), so the stateful screen s16 is run for V18F
# (v18 P&fortress_guns=true&catch_up=true; t8f 24-20-4 on TARGETED2 against V17 20-16-12).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 1435751 2>/dev/null; do sleep 15; done
echo "fx1c done (seen by c9a8) $(date -u +%FT%TZ)"
Q='"big_threat":100,"gun_cap":120,"poke_until":3,"big_partial":true,"r1_poke":3,"attack_mode":"adaptive","poke_reactive":"turret","fortress_n":4,"immune_attack":true,"foreign_policy":"econ17","mid_until":5'
MODEL=v18 GRID=full COUNTER=stateful bot_research/experiments/lead/run_screens.sh s16 "{$Q,\"fortress_guns\":true,\"catch_up\":true}" > bot_research/runs/lead/s16.out 2>&1
echo "== queue_c9a8 done $(date -u +%FT%TZ)"
