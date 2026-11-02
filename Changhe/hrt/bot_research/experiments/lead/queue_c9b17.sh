#!/bin/bash
# Cycle-9 queue, chain B, seventeenth version (written 2026-10-31T12:02Z; one computation slot). Replaces queue_c9b16.sh (d9e done,
# both checks passed) while t9h ran: waits for the orphaned t9h tournament (PID 2576007, V18FT on TARGETED3_V18FT), then
#   freeze_v9e.sh  checks of the frozen file experiments/lead/frozen/best_v9e.py (twin V18FT);
#   s19            stateful forecaster screen of V18FT (MODEL=v19, GRID=full).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 2576007 2>/dev/null; do sleep 15; done
echo "t9h done (seen by c9b17) $(date -u +%FT%TZ)"
bash bot_research/experiments/lead/freeze_v9e.sh > bot_research/runs/lead/freeze_v9e.log 2>&1
echo "freeze_v9e done $(date -u +%FT%TZ)"
Q='"big_threat":100,"gun_cap":120,"poke_until":3,"big_partial":true,"r1_poke":3,"attack_mode":"adaptive","poke_reactive":"turret","fortress_n":4,"immune_attack":true,"foreign_policy":"econ17","mid_until":5'
MODEL=v19 GRID=full COUNTER=stateful bot_research/experiments/lead/run_screens.sh s19 "{$Q,\"fortress_guns\":true,\"catch_up\":true,\"foreign_target\":\"econ20\"}" > bot_research/runs/lead/s19.out 2>&1
echo "== queue_c9b17 done $(date -u +%FT%TZ)"
