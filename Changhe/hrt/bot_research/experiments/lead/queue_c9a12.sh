#!/bin/bash
# Cycle-9 queue, chain A, twelfth version (written 2026-10-31T11:35Z; one computation slot). Replaces queue_c9a11.sh while it
# waited: waits for freeze_v9c.sh (PID 1809292), then
#   d9a  V23R = v23 V20T&mid_relevant=true on pools.py MIDJOINT (feature bluffs, budget_timing tier3 r3 0.5, guards);
#   c9k  V23R on f5t (pair with c9h V20T and c8m V17);
#   t9a  V20T and V23R on TARGETED3 (newest teammate bots, hrt-w3 counters, GuardedForecast modelling best_v9c);
#   t9c  V22G = V20T on v22 with r1_gun=[4,1] on TARGETED2 (t8g pair);
#   t9e  V22G on TARGETED3_V22G;
#   s17  stateful forecaster screen of V20T (MODEL=v20, GRID=full).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 1809292 2>/dev/null; do sleep 15; done
echo "freeze checks done (seen by c9a12) $(date -u +%FT%TZ)"
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V20T="bot_research.experiments.lead.v20:@make?$P&fortress_guns=true&catch_up=true&mid_joint=0.75&mid_level=true&foreign_target=\"econ20\""
V23R="bot_research.experiments.lead.v23:@make?$P&fortress_guns=true&catch_up=true&mid_joint=0.75&mid_level=true&foreign_target=\"econ20\"&mid_relevant=true"
V22G="bot_research.experiments.lead.v22:@make?$P&fortress_guns=true&catch_up=true&mid_joint=0.75&mid_level=true&foreign_target=\"econ20\"&r1_gun=[4,1]"
bot_research/experiments/lead/run_pool.sh midjoint d9a "'$V23R'" --keep-logs losses > bot_research/runs/lead/d9a.out 2>&1
echo "d9a done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh f5t c9k "'$V23R'" --keep-logs losses > bot_research/runs/lead/c9k.out 2>&1
echo "c9k done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted3 t9a "'$V20T' '$V23R'" --keep-logs losses > bot_research/runs/lead/t9a.out 2>&1
echo "t9a done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted2 t9c "'$V22G'" --keep-logs losses > bot_research/runs/lead/t9c.out 2>&1
echo "t9c done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted3_v22g t9e "'$V22G'" --keep-logs losses > bot_research/runs/lead/t9e.out 2>&1
echo "t9e done $(date -u +%FT%TZ)"
Q='"big_threat":100,"gun_cap":120,"poke_until":3,"big_partial":true,"r1_poke":3,"attack_mode":"adaptive","poke_reactive":"turret","fortress_n":4,"immune_attack":true,"foreign_policy":"econ17","mid_until":5'
MODEL=v20 GRID=full COUNTER=stateful bot_research/experiments/lead/run_screens.sh s17 "{$Q,\"fortress_guns\":true,\"catch_up\":true,\"mid_joint\":0.75,\"mid_level\":true,\"foreign_target\":\"econ20\"}" > bot_research/runs/lead/s17.out 2>&1
echo "== queue_c9a12 done $(date -u +%FT%TZ)"
