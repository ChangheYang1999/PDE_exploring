#!/bin/bash
# Checks of the best_v9d freeze (written 2026-10-31T11:47Z; one process at a time): full-trajectory identity of the frozen copy
# experiments/lead/frozen/best_v9d.py with its development twin V23R on the standard start and after scripted openings,
# the bot tests on the frozen copy (bot_research/tmp/test_best_v9d.py with BEST_MODULE set), and a smoke game.
cd "$(dirname "$0")/../../.."
export PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 TMPDIR="$PWD/bot_research/tmp"
PY="taskset -c 20,21 nice -n 19 .venv/bin/python -B"
TWIN='bot_research.experiments.lead.v23:@make?big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5&fortress_guns=true&catch_up=true&mid_joint=0.75&mid_level=true&foreign_target="econ20"&mid_relevant=true'
BEST='bot_research.experiments.lead.frozen.best_v9d:@make'
OUT=bot_research/runs/lead/freeze_v9d
mkdir -p $OUT
echo "start $(date -u +%FT%TZ)"
(cd bot_research/experiments/lead/frozen && sha256sum -c SHA256SUMS) > $OUT/sha256.out 2>&1
echo "sha256 exit $? $(date -u +%FT%TZ)"
$PY -m bot_research.experiments.lead.same_actions "$BEST" "$TWIN" \
  'bot_research.bots.economy.frozen.v13.econ13:@make' \
  'bot_research.bots.counters.feature_bluff:@make?turret_round=2' \
  'bot_research.bots.counters.feature_bluff:@make?turret_round=0' \
  'bot_research.bots.counters.feature_bluff:@make?turret_round=1' \
  'bot_research.bots.counters.adaptive_continuation:@make?attack_weight=4' \
  'bot_research.bots.counters.guarded_schedule:@make?schedule=[[1,"tier1",1],[5,"tier4",200]]' \
  'bot_research.harness.baselines:@threat_defender' \
  'bot_research.bots.counters.forecast_timing:@make?attack_round=8&tier=tier5&attack_share=1.0&model_lam=1.0' \
  'bot_research.bots.economy.frozen.v4.econ:@make?late_round=6&phi=0.0' \
  'bot_research.bots.counters.budget_timing:@make?tier="tier3"&attack_round=3&budget_fraction=0.5' \
  'bot_research.bots.counters.guard_geometry:@make?roster=["tier1"]' \
  'bot_research.bots.counters.guard_geometry:@make?roster=["tier1","tier1"]' \
  'bot_research.bots.counters.guard_roster:@make?roster=[]' \
  'bot_research.bots.economy.frozen.v17.econ17:@make?free_fallback="zero"&foreign_attack_from=11' > $OUT/same_actions_std.out 2>&1
echo "same_actions exit $? $(date -u +%FT%TZ)"
$PY -m bot_research.experiments.lead.same_actions_scen "$BEST" "$TWIN" $OUT/scen \
  --opponents 'bot_research.bots.economy.frozen.v17.econ17:@make?free_fallback="zero"&foreign_attack_from=11' \
  'bot_research.bots.defense.frozen.v25.fortress:@make' \
  'bot_research.bots.economy.frozen.v19.econ19:@make?free_fallback="zero"&foreign_attack_from=11&doom="next"&fac_cap=400&sat_reach=true' \
  --scenarios mirror:1:2 asym:23:2 none > $OUT/same_actions_scen.out 2>&1
echo "same_actions_scen exit $? $(date -u +%FT%TZ)"
BEST_MODULE=bot_research.experiments.lead.frozen.best_v9d PYTHONPATH=. $PY bot_research/tmp/test_best_v9d.py > $OUT/tests.out 2>&1
echo "tests exit $? $(date -u +%FT%TZ)"
$PY -m unittest bot_research.tests.test_harness bot_research.tests.test_gamekit > $OUT/tests_harness.out 2>&1
echo "harness tests exit $? $(date -u +%FT%TZ)"
$PY -m td_game.runner --balanced --bot-a bot_research.experiments.lead.frozen.best_v9d:decide --bot-b td_bots.protocol:idle \
  --output bot_research/runs/best-vs-idle-v9d-000001.jsonl > $OUT/smoke.out 2>&1
echo "smoke exit $? $(date -u +%FT%TZ)"
