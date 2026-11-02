#!/bin/bash
# Cycle-9 queue, chain A, tenth version (written 2026-10-31T11:24Z; one computation slot). Replaces queue_c9a9.sh after its
# first step started: waits for freeze_v9c.sh (PID 1809292), then
#   t9a  V20T on pools.py TARGETED3 (hrt-w1 fortress v27-v29, hrt-w2 econ21, hrt-w3's adaptive-continuation and
#        guard counters, GuardedForecast with an exact model of frozen best_v9c), both seats;
#   s17  stateful forecaster screen of V20T (MODEL=v20, GRID=full).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 1809292 2>/dev/null; do sleep 15; done
echo "freeze checks done (seen by c9a10) $(date -u +%FT%TZ)"
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V20T="bot_research.experiments.lead.v20:@make?$P&fortress_guns=true&catch_up=true&mid_joint=0.75&mid_level=true&foreign_target=\"econ20\""
bot_research/experiments/lead/run_pool.sh targeted3 t9a "'$V20T'" --keep-logs losses > bot_research/runs/lead/t9a.out 2>&1
echo "t9a done $(date -u +%FT%TZ)"
Q='"big_threat":100,"gun_cap":120,"poke_until":3,"big_partial":true,"r1_poke":3,"attack_mode":"adaptive","poke_reactive":"turret","fortress_n":4,"immune_attack":true,"foreign_policy":"econ17","mid_until":5'
MODEL=v20 GRID=full COUNTER=stateful bot_research/experiments/lead/run_screens.sh s17 "{$Q,\"fortress_guns\":true,\"catch_up\":true,\"mid_joint\":0.75,\"mid_level\":true,\"foreign_target\":\"econ20\"}" > bot_research/runs/lead/s17.out 2>&1
echo "== queue_c9a10 done $(date -u +%FT%TZ)"
