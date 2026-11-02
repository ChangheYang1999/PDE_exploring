#!/bin/bash
# Cycle-9 queue, chain A, thirteenth version (written 2026-10-31T11:47Z; one computation slot). Replaces queue_c9a12.sh after d9a
# (V23R repaired feature_bluff turret_round=1 and kept budget_timing tier3 r3 0.5 at 0); waits for the orphaned c9k
# tournament (PID 2404531, V23R on f5t), then
#   freeze_v9d.sh  checks of the frozen copy best_v9d (twin V23R);
#   t9a  V23R on pools.py TARGETED3_V9D (newest teammate bots, hrt-w3 counters, GuardedForecast modelling best_v9d, v32);
#   t9c  V22G (v22 r1_gun=[4,1]) on TARGETED2 (t8g pair);
#   t9e  V22G on TARGETED3_V22G + v32;
#   s18  stateful forecaster screen of V23R (MODEL=v23, GRID=full).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 2404531 2>/dev/null; do sleep 15; done
echo "c9k done (seen by c9a13) $(date -u +%FT%TZ)"
bot_research/experiments/lead/freeze_v9d.sh > bot_research/runs/lead/freeze_v9d.log 2>&1
echo "freeze_v9d done $(date -u +%FT%TZ)"
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V23R="bot_research.experiments.lead.v23:@make?$P&fortress_guns=true&catch_up=true&mid_joint=0.75&mid_level=true&foreign_target=\"econ20\"&mid_relevant=true"
V22G="bot_research.experiments.lead.v22:@make?$P&fortress_guns=true&catch_up=true&mid_joint=0.75&mid_level=true&foreign_target=\"econ20\"&r1_gun=[4,1]"
bot_research/experiments/lead/run_pool.sh targeted3_v9d t9a "'$V23R'" --keep-logs losses > bot_research/runs/lead/t9a.out 2>&1
echo "t9a done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted2 t9c "'$V22G'" --keep-logs losses > bot_research/runs/lead/t9c.out 2>&1
echo "t9c done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted3_v22g t9e "'$V22G'" --keep-logs losses > bot_research/runs/lead/t9e.out 2>&1
echo "t9e done $(date -u +%FT%TZ)"
Q='"big_threat":100,"gun_cap":120,"poke_until":3,"big_partial":true,"r1_poke":3,"attack_mode":"adaptive","poke_reactive":"turret","fortress_n":4,"immune_attack":true,"foreign_policy":"econ17","mid_until":5'
MODEL=v23 GRID=full COUNTER=stateful bot_research/experiments/lead/run_screens.sh s18 "{$Q,\"fortress_guns\":true,\"catch_up\":true,\"mid_joint\":0.75,\"mid_level\":true,\"foreign_target\":\"econ20\",\"mid_relevant\":true}" > bot_research/runs/lead/s18.out 2>&1
echo "== queue_c9a13 done $(date -u +%FT%TZ)"
