#!/bin/bash
# Checks of the best_v9f freeze (written 2026-10-31T13:21Z; one process at a time): full-trajectory identity of the frozen copy
# experiments/lead/frozen/best_v9f.py with its development twin on the standard start and after scripted openings, the
# bot tests on the frozen copy (bot_research/tmp/test_best_v9f_$CAND.py with BEST_MODULE set), and a smoke game.
# Usage: freeze_v9f.sh P5T|P5TF|P5TN|P5TNR|P5TFU|P5TNU|P5TNUB|P4TNUB|P5TNUBM|M3|M2|V33C (case V33C, the tier2 round-4 striker and fortress v32 added 16:50Z; cases M3, M2 and the round-3 tier1 striker added 15:28Z; cases P4TNUB, P5TNUBM and the two round-5 strikers added 14:55Z; case P5TNUB and the handoff opponent added 14:06Z; cases P5TFU, P5TNU and the screened opponent added 13:39Z; P5TN, P5TNR 13:34Z; the chosen candidate; frozen/best_v9f.py must be tmp/drafts/best_v9f_$CAND.py).
cd "$(dirname "$0")/../../.."
export PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 TMPDIR="$PWD/bot_research/tmp"
PY="taskset -c 20,21 nice -n 19 .venv/bin/python -B"
CAND=$1
case $CAND in
  P5T) TWIN='bot_research.experiments.lead.v24:@make?passive_until=5&poke_reactive="turret_only"' ;;
  P5TF) TWIN='bot_research.experiments.lead.v24:@make?passive_until=5&poke_reactive="turret_only"&fail_limit=2' ;;
  P5TN) TWIN='bot_research.experiments.lead.v26:@make?passive_until=5&poke_reactive="turret_only"&fail_limit=2&passive_turret=false' ;;
  P5TNR) TWIN='bot_research.experiments.lead.v26:@make?passive_until=5&poke_reactive="turret_only"&fail_limit=2&passive_turret=false&passive_ratio=0.5' ;;
  P5TFU) TWIN='bot_research.experiments.lead.v27:@make?passive_until=5&poke_reactive="turret_only"&fail_limit=2&robust_k=null' ;;
  P5TNU) TWIN='bot_research.experiments.lead.v27:@make?passive_until=5&poke_reactive="turret_only"&fail_limit=2&passive_turret=false&robust_k=null' ;;
  P5TNUB) TWIN='bot_research.experiments.lead.v28:@make?passive_until=5&poke_reactive="turret_only"&fail_limit=2&passive_turret=false&robust_k=null&behind_mode="current"' ;;
  P4TNUB) TWIN='bot_research.experiments.lead.v28:@make?poke_reactive="turret_only"&fail_limit=2&passive_turret=false&robust_k=null&behind_mode="current"&passive_until=4' ;;
  P5TNUBM) TWIN='bot_research.experiments.lead.v30:@make?passive_until=5&poke_reactive="turret_only"&fail_limit=2&passive_turret=false&robust_k=null&behind_mode="current"&passive_mid_from=5' ;;
  M3) TWIN='bot_research.experiments.lead.v30:@make?passive_until=5&poke_reactive="turret_only"&fail_limit=2&passive_turret=false&robust_k=null&behind_mode="current"&passive_mid_from=3' ;;
  M2) TWIN='bot_research.experiments.lead.v30:@make?passive_until=5&poke_reactive="turret_only"&fail_limit=2&passive_turret=false&robust_k=null&behind_mode="current"&passive_mid_from=2' ;;
  V33C) TWIN='bot_research.experiments.lead.v33:@make?passive_until=5&poke_reactive="turret_only"&fail_limit=2&passive_turret=false&robust_k=null&behind_mode="current"&passive_mid_from=5&passive_cheap_from=3' ;;
  *) echo "usage: freeze_v9f.sh P5T|P5TF|P5TN|P5TNR|P5TFU|P5TNU|P5TNUB|P4TNUB|P5TNUBM|M3|M2|V33C"; exit 2 ;;
esac
cmp bot_research/experiments/lead/frozen/best_v9f.py bot_research/tmp/drafts/best_v9f_$CAND.py || exit 3
BEST='bot_research.experiments.lead.frozen.best_v9f:@make'
OUT=bot_research/runs/lead/freeze_v9f
mkdir -p $OUT
echo "start $(date -u +%FT%TZ)"
(cd bot_research/experiments/lead/frozen && sha256sum -c SHA256SUMS) > $OUT/sha256.out 2>&1
echo "sha256 exit $? $(date -u +%FT%TZ)"
$PY -m bot_research.experiments.lead.same_actions "$BEST" "$TWIN" \
  'bot_research.bots.economy.frozen.v13.econ13:@make' \
  'bot_research.bots.counters.feature_bluff:@make?turret_round=2' \
  'bot_research.bots.counters.feature_bluff:@make?turret_round=0' \
  'bot_research.bots.counters.feature_bluff:@make?turret_round=1' \
  'bot_research.bots.counters.feature_bluff:@make?turret_round=1&turret_x=0&turret_y=2' \
  'bot_research.bots.counters.guard_geometry:@make?roster=["tier1"]&x=9&y=1&parameters={"foreign_attack_from":null}' \
  'bot_research.bots.counters.adaptive_continuation:@make?attack_weight=4' \
  'bot_research.bots.counters.guarded_schedule:@make?schedule=[[1,"tier1",1],[5,"tier4",200]]' \
  'bot_research.harness.baselines:@threat_defender' \
  'bot_research.bots.counters.forecast_timing:@make?attack_round=8&tier=tier5&attack_share=1.0&model_lam=1.0' \
  'bot_research.bots.economy.frozen.v4.econ:@make?late_round=6&phi=0.0' \
  'bot_research.bots.counters.budget_timing:@make?tier="tier3"&attack_round=3&budget_fraction=0.5' \
  'bot_research.bots.counters.guard_geometry:@make?roster=["tier1"]' \
  'bot_research.bots.counters.guard_geometry:@make?roster=["tier1","tier1"]' \
  'bot_research.bots.counters.guard_roster:@make?roster=[]' \
  'bot_research.bots.economy.frozen.v17.econ17:@make?free_fallback="zero"&foreign_attack_from=11' \
  'bot_research.bots.counters.maze_grower:@make?layout="lead_opening"&growth_rounds=6&bait=["tier1"]&bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000' \
  'bot_research.bots.counters.roster_bait:@make?turret_x=0&turret_y=2&tier="tier5"&factory_cap=2000&purchase_cap=1000&bait_round=2&turret_round=0&growth_rounds=5&bait=["tier1","tier1","tier1"]' \
  'bot_research.bots.counters.staged_guard_maze:@make?layout="empty"&growth_rounds=6&bait=[]&bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000&guard_rounds=[4,6]' \
  'bot_research.bots.counters.guarded_maze:@make?layout="empty"&growth_rounds=4&guard_round=3&bait=["tier1"]&bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000' \
  'bot_research.bots.counters.screened_guard_maze:@make?layout="empty"&growth_rounds=6&bait=[]&bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000&upgrade_round=9' \
  'bot_research.bots.counters.guard_handoff:@make?layout="empty"&growth_rounds=6&bait=[]&bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000&handoff_round=12&replan_iters=5000' \
  'bot_research.bots.economy.timing:@make' \
  'bot_research.bots.counters.budget_timing:@make?tier="tier3"&attack_round=5&budget_fraction=0.5' \
  'bot_research.bots.counters.budget_timing:@make?tier="tier1"&attack_round=3&budget_fraction=0.5' \
  'bot_research.bots.counters.budget_timing:@make?tier="tier2"&attack_round=4&budget_fraction=0.5' \
  'bot_research.bots.defense.frozen.v32.fortress:@make' \
  'bot_research.bots.counters.heavy_drip:@make' > $OUT/same_actions_std.out 2>&1
echo "same_actions exit $? $(date -u +%FT%TZ)"
$PY -m bot_research.experiments.lead.same_actions_scen "$BEST" "$TWIN" $OUT/scen \
  --opponents 'bot_research.bots.economy.frozen.v17.econ17:@make?free_fallback="zero"&foreign_attack_from=11' \
  'bot_research.bots.defense.frozen.v25.fortress:@make' \
  'bot_research.bots.economy.frozen.v19.econ19:@make?free_fallback="zero"&foreign_attack_from=11&doom="next"&fac_cap=400&sat_reach=true' \
  --scenarios mirror:1:2 asym:23:2 none > $OUT/same_actions_scen.out 2>&1
echo "same_actions_scen exit $? $(date -u +%FT%TZ)"
BEST_MODULE=bot_research.experiments.lead.frozen.best_v9f PYTHONPATH=. $PY bot_research/tmp/test_best_v9f_$CAND.py > $OUT/tests.out 2>&1
echo "tests exit $? $(date -u +%FT%TZ)"
$PY -m unittest bot_research.tests.test_harness bot_research.tests.test_gamekit > $OUT/tests_harness.out 2>&1
echo "harness tests exit $? $(date -u +%FT%TZ)"
$PY -m td_game.runner --balanced --bot-a bot_research.experiments.lead.frozen.best_v9f:decide --bot-b td_bots.protocol:idle \
  --output bot_research/runs/best-vs-idle-v9f-000001.jsonl > $OUT/smoke.out 2>&1
echo "smoke exit $? $(date -u +%FT%TZ)"
