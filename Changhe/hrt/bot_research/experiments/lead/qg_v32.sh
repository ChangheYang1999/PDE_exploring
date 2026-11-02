#!/bin/bash
# Quick seat-0 development games of M2L = v32 M2 + passive_ladder=[70,20] (written 2026-10-31T15:31Z; one slot): the TIMING2
# strikes M2 loses or might lose, economy.timing, and the growers with the smallest margins for M2/P5TNUBM/P5TNU.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1 PYTHONPATH="$PWD"
PAR="poke_reactive=\"turret_only\"&fail_limit=2&passive_turret=false&robust_k=null&behind_mode=\"current\""
C="bot_research.experiments.lead.v32:@make?passive_until=5&$PAR&passive_mid_from=2&passive_ladder=[70,20]"
K=bot_research.bots.counters.
G='bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000'
echo "== M2L $(date -u +%FT%TZ)"
.venv/bin/python -B -m bot_research.experiments.lead.quick_games "$C" \
  "${K}budget_timing:@make?tier=\"tier1\"&attack_round=3&budget_fraction=0.5" \
  "${K}budget_timing:@make?tier=\"tier1\"&attack_round=4&budget_fraction=0.5" \
  "${K}budget_timing:@make?tier=\"tier2\"&attack_round=3&budget_fraction=0.5" \
  "${K}budget_timing:@make?tier=\"tier2\"&attack_round=4&budget_fraction=0.5" \
  "${K}budget_timing:@make?tier=\"tier3\"&attack_round=4&budget_fraction=0.5" \
  "${K}budget_timing:@make?tier=\"tier1\"&attack_round=2&budget_fraction=0.5" \
  "${K}budget_timing:@make?tier=\"tier3\"&attack_round=3&budget_fraction=0.5" \
  "bot_research.bots.economy.timing:@make" \
  "${K}maze_grower:@make?layout=\"lead_opening\"&growth_rounds=6&bait=[\"tier2\"]&$G" \
  "${K}maze_grower:@make?layout=\"lead_opening\"&growth_rounds=6&bait=[\"tier1\"]&$G" \
  "${K}guarded_maze:@make?layout=\"lead_opening\"&growth_rounds=5&guard_round=5&bait=[\"tier2\"]&$G" \
  "${K}guarded_maze:@make?layout=\"empty\"&growth_rounds=4&guard_round=3&bait=[\"tier1\"]&$G" \
  "${K}guard_ladder:@make?growth_rounds=7&bait=[]&$G&upgrades=[[4,1],[6,2],[9,5]]" \
  "${K}screened_guard_maze:@make?layout=\"empty\"&growth_rounds=7&bait=[]&$G&upgrade_round=9"
echo "== done $(date -u +%FT%TZ)"
