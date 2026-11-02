#!/bin/bash
# Quick seat-0 development games of v31 candidates (written for cycle 9, one slot): M2H (passive_hp=560) and
# M2A (passive_hp=1500) against hrt-w3's early_heavy_handoff (round-5 tier4, then exact-model defence) with the model
# retargeted to the candidate and with the original P5TNUBM model, plus budget_timing tier4 strikes and a grower.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1 PYTHONPATH="$PWD"
PAR="poke_reactive=\"turret_only\"&fail_limit=2&passive_turret=false&robust_k=null&behind_mode=\"current\""
K=bot_research.bots.counters.
for H in 560 1500; do
  C="bot_research.experiments.lead.v31:@make?passive_until=5&$PAR&passive_mid_from=2&passive_hp=$H"
  MP=$(printf '{"poke_reactive":"turret_only","fail_limit":2,"passive_turret":false,"robust_k":null,"behind_mode":"current","passive_until":5,"passive_mid_from":2,"passive_hp":%s}' $H)
  MPP='{"poke_reactive":"turret_only","fail_limit":2,"passive_turret":false,"robust_k":null,"behind_mode":"current","passive_until":5,"passive_mid_from":5}'
  EH="${K}early_heavy_handoff:@make?layout=\"empty\"&growth_rounds=6&bait=[]&bait_round=2&tier=\"tier5\"&factory_cap=2000&purchase_cap=1000&upgrade_round=9&forecast=true&strike_round=5&strike_tier=\"tier4\"&strike_count=1"
  echo "== passive_hp=$H $(date -u +%FT%TZ)"
  .venv/bin/python -B -m bot_research.experiments.lead.quick_games "$C" \
    "$EH&deadline=6&model_spec=\"bot_research.experiments.lead.v31:@make\"&model_parameters=$MP" \
    "$EH&deadline=7&model_spec=\"bot_research.experiments.lead.v31:@make\"&model_parameters=$MP" \
    "$EH&deadline=6&model_spec=\"bot_research.experiments.lead.v30:@make\"&model_parameters=$MPP" \
    "${K}budget_timing:@make?tier=\"tier4\"&attack_round=5&budget_fraction=0.5" \
    "${K}budget_timing:@make?tier=\"tier4\"&attack_round=4&budget_fraction=0.5" \
    "${K}budget_timing:@make?tier=\"tier4\"&attack_round=5&budget_fraction=1.0" \
    "${K}budget_timing:@make?tier=\"tier3\"&attack_round=5&budget_fraction=0.5" \
    "bot_research.bots.economy.timing:@make"
done
echo "== done $(date -u +%FT%TZ)"
