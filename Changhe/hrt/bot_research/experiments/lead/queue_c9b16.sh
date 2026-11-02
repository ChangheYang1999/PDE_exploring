#!/bin/bash
# Cycle-9 queue, chain B, sixteenth version (written 2026-10-31T11:56Z; one computation slot). Replaces queue_c9b15.sh: c9j showed
# that r1_gun loses the economy race (V22G 38-4-34 on f5t: -1125 against eco6_t5, -130 against five fortress and
# economy bots), so c9l and t9i (V24G) were stopped. Runs
#   d9e  checks of experiments/lead/best_v9e_draft.py (V20T's frozen file without the joint plan): same_actions with
#        its twin V18FT on six opponents and tmp/test_best_v9e.py with BEST_MODULE set to the draft;
#   t9h  V18FT on pools.py TARGETED3_V18FT (TEAMMATES3, GuardedForecast modelling V18FT with six rosters, fortress v32);
#   s19  stateful forecaster screen of V18FT (MODEL=v19, GRID=full).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
PY="taskset -c 20,21 nice -n 19 .venv/bin/python -B"
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V18FT="bot_research.experiments.lead.v19:@make?$P&fortress_guns=true&catch_up=true&foreign_target=\"econ20\""
OUT=bot_research/runs/lead/d9e
mkdir -p $OUT
echo "d9e start $(date -u +%FT%TZ)"
$PY -m bot_research.experiments.lead.same_actions 'bot_research.experiments.lead.best_v9e_draft:@make' "$V18FT" \
  'bot_research.bots.counters.feature_bluff:@make?turret_round=1&turret_x=0&turret_y=2' \
  'bot_research.bots.counters.budget_timing:@make?tier="tier3"&attack_round=3&budget_fraction=0.5' \
  'bot_research.bots.counters.guard_geometry:@make?roster=["tier1"]' \
  'bot_research.bots.counters.forecast_timing:@make?attack_round=8&tier=tier5&attack_share=1.0&model_lam=1.0' \
  'bot_research.bots.counters.adaptive_continuation:@make?attack_weight=4' \
  'bot_research.bots.economy.frozen.v13.econ13:@make' > $OUT/same_actions_std.out 2>&1
echo "d9e same_actions exit $? $(date -u +%FT%TZ)"
BEST_MODULE=bot_research.experiments.lead.best_v9e_draft PYTHONPATH=. $PY bot_research/tmp/test_best_v9e.py > $OUT/tests.out 2>&1
echo "d9e tests exit $? $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted3_v18ft t9h "'$V18FT'" --keep-logs losses > bot_research/runs/lead/t9h.out 2>&1
echo "t9h done $(date -u +%FT%TZ)"
Q='"big_threat":100,"gun_cap":120,"poke_until":3,"big_partial":true,"r1_poke":3,"attack_mode":"adaptive","poke_reactive":"turret","fortress_n":4,"immune_attack":true,"foreign_policy":"econ17","mid_until":5'
MODEL=v19 GRID=full COUNTER=stateful bot_research/experiments/lead/run_screens.sh s19 "{$Q,\"fortress_guns\":true,\"catch_up\":true,\"foreign_target\":\"econ20\"}" > bot_research/runs/lead/s19.out 2>&1
echo "== queue_c9b16 done $(date -u +%FT%TZ)"
