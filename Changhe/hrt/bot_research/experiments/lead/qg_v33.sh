#!/bin/bash
# Quick seat-0 development games (written 2026-10-31T16:22Z; one slot) of v33 (P5TNUBM plus a capped tier1-tier2 plan in passive rounds from round 3 or 4; section 5.11): the
# round-4 tier2 strike of hrt-w1's fortress v32 that P5TNUBM loses (t9j), the TIMING2 strikes, economy.timing, the
# growers with the smallest margins and hrt-w3's early_heavy_handoff (model retargeted, and the P5TNUBM model).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1 PYTHONPATH="$PWD"
PAR="poke_reactive=\"turret_only\"&fail_limit=2&passive_turret=false&robust_k=null&behind_mode=\"current\""
K=bot_research.bots.counters.
G='bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000'
EH="${K}early_heavy_handoff:@make?layout=\"empty\"&growth_rounds=6&bait=[]&bait_round=2&tier=\"tier5\"&factory_cap=2000&purchase_cap=1000&upgrade_round=9&forecast=true&strike_round=5&strike_tier=\"tier4\"&strike_count=1"
MPP='{"poke_reactive":"turret_only","fail_limit":2,"passive_turret":false,"robust_k":null,"behind_mode":"current","passive_until":5,"passive_mid_from":5}'
for V in "3 60" "4 60" "3 30"; do
  set -- $V
  C="bot_research.experiments.lead.v33:@make?passive_until=5&$PAR&passive_mid_from=5&passive_cheap_from=$1&passive_cheap_cap=$2"
  MP=$(printf '{"poke_reactive":"turret_only","fail_limit":2,"passive_turret":false,"robust_k":null,"behind_mode":"current","passive_until":5,"passive_mid_from":5,"passive_cheap_from":%s,"passive_cheap_cap":%s}' $1 $2)
  echo "== passive_cheap_from=$1 cap=$2 $(date -u +%FT%TZ)"
  .venv/bin/python -B -m bot_research.experiments.lead.quick_games "$C" \
    "bot_research.bots.defense.frozen.v32.fortress:@make" \
    "bot_research.bots.economy.timing:@make" \
    "${K}budget_timing:@make?tier=\"tier1\"&attack_round=3&budget_fraction=0.5" \
    "${K}budget_timing:@make?tier=\"tier1\"&attack_round=4&budget_fraction=0.5" \
    "${K}budget_timing:@make?tier=\"tier2\"&attack_round=3&budget_fraction=0.5" \
    "${K}budget_timing:@make?tier=\"tier2\"&attack_round=4&budget_fraction=0.5" \
    "${K}budget_timing:@make?tier=\"tier3\"&attack_round=4&budget_fraction=0.5" \
    "${K}budget_timing:@make?tier=\"tier3\"&attack_round=5&budget_fraction=0.5" \
    "${K}maze_grower:@make?layout=\"lead_opening\"&growth_rounds=6&bait=[\"tier1\"]&$G" \
    "${K}maze_grower:@make?layout=\"lead_opening\"&growth_rounds=6&bait=[\"tier2\"]&$G" \
    "${K}guarded_maze:@make?layout=\"lead_opening\"&growth_rounds=5&guard_round=5&bait=[\"tier2\"]&$G" \
    "${K}guarded_maze:@make?layout=\"empty\"&growth_rounds=4&guard_round=3&bait=[\"tier1\"]&$G" \
    "${K}guard_ladder:@make?growth_rounds=7&bait=[]&$G&upgrades=[[4,1],[6,2],[9,5]]" \
    "$EH&deadline=6&model_spec=\"bot_research.experiments.lead.v33:@make\"&model_parameters=$MP" \
    "$EH&deadline=6&model_spec=\"bot_research.experiments.lead.v30:@make\"&model_parameters=$MPP"
done
echo "== done $(date -u +%FT%TZ)"
