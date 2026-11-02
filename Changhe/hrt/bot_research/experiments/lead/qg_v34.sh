#!/bin/bash
# Quick seat-0 development games (written 2026-10-31T16:55Z; one slot) of v34 = v33 (3, 60) plus passive_cheap2_from=4 (tier1-tier3
# rosters, cap 120 or 90 gold, in round 4): the budget_timing tier3 round-4 strike that v33 loses (x33tm2 log 00025), the
# conditions of qg_v33.sh and hrt-w2's round-4 all-in economy.timing striker.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1 PYTHONPATH="$PWD"
PAR="poke_reactive=\"turret_only\"&fail_limit=2&passive_turret=false&robust_k=null&behind_mode=\"current\""
K=bot_research.bots.counters.
G='bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000'
EH="${K}early_heavy_handoff:@make?layout=\"empty\"&growth_rounds=6&bait=[]&bait_round=2&tier=\"tier5\"&factory_cap=2000&purchase_cap=1000&upgrade_round=9&forecast=true&strike_round=5&strike_tier=\"tier4\"&strike_count=1"
MPP='{"poke_reactive":"turret_only","fail_limit":2,"passive_turret":false,"robust_k":null,"behind_mode":"current","passive_until":5,"passive_mid_from":5}'
for V in "4 120" "4 90"; do
  set -- $V
  C="bot_research.experiments.lead.v34:@make?passive_until=5&$PAR&passive_mid_from=5&passive_cheap_from=3&passive_cheap2_from=$1&passive_cheap2_cap=$2"
  MP=$(printf '{"poke_reactive":"turret_only","fail_limit":2,"passive_turret":false,"robust_k":null,"behind_mode":"current","passive_until":5,"passive_mid_from":5,"passive_cheap_from":3,"passive_cheap2_from":%s,"passive_cheap2_cap":%s}' $1 $2)
  echo "== passive_cheap2_from=$1 cap2=$2 $(date -u +%FT%TZ)"
  .venv/bin/python -B -m bot_research.experiments.lead.quick_games "$C" \
    "bot_research.bots.defense.frozen.v32.fortress:@make" \
    "bot_research.bots.economy.timing:@make" \
    "bot_research.bots.economy.timing:@make?attack_round=4&attack_frac=1.0&repeat=false" \
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
    "$EH&deadline=6&model_spec=\"bot_research.experiments.lead.v34:@make\"&model_parameters=$MP" \
    "$EH&deadline=6&model_spec=\"bot_research.experiments.lead.v30:@make\"&model_parameters=$MPP"
done
echo "== done $(date -u +%FT%TZ)"
