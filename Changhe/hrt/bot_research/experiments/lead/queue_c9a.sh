#!/bin/bash
# Cycle-9 queue, chain A (written 2026-10-31T09:26Z; one computation slot). Waits for the best_v9b freeze checks
# (freeze_v9b.sh writes "smoke exit" last), then:
#   c9/same_v18j0.out  v18 with mid_joint=0.0 against V17 (= best_v9b's twin), full trajectories, 4 opponents;
#                      checks that v18's copy of the v15 decision method is faithful;
#   c9/quick_v18.out   V18 (mid_joint=1.0) against hrt-w3's budget_timing tier3 round 3 (0.5 and 0.25), both seats;
#   c9/quick_v18g.out  V18g (fortress_guns=true; rewritten 09:29Z) against the fortress-sensitive opponents, both seats;
#   t8a                TARGETED2 (hrt-w3's budget-timing and guard counters, fortress v24/v25) for V17;
#   s15                stateful forecaster screen of V17 (MODEL=v17 GRID=full COUNTER=stateful).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
PY="taskset -c 20,21 nice -n 19 .venv/bin/python -B"
until grep -q "smoke exit" bot_research/runs/lead/freeze_v9b.log 2>/dev/null; do sleep 30; done
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V17="bot_research.experiments.lead.v17:@make?$P"
V18J0="bot_research.experiments.lead.v18:@make?$P&mid_joint=0.0"
V18="bot_research.experiments.lead.v18:@make?$P&mid_joint=1.0"
BT='bot_research.bots.counters.budget_timing:@make?tier="tier3"&attack_round=3'
OUT=bot_research/runs/lead/c9
mkdir -p $OUT
echo "start $(date -u +%FT%TZ)"
$PY -m bot_research.experiments.lead.same_actions "$V18J0" "$V17" "$BT&budget_fraction=0.5" \
  'bot_research.bots.economy.frozen.v17.econ17:@make?free_fallback="zero"&foreign_attack_from=11' \
  'bot_research.bots.counters.feature_bluff:@make?turret_round=2' \
  'bot_research.bots.counters.forecast_timing:@make?attack_round=8&tier=tier5&attack_share=1.0&model_lam=1.0' \
  > $OUT/same_v18j0.out 2>&1
echo "same_v18j0 exit $? $(date -u +%FT%TZ)"
for f in 0.5 0.25; do
  echo "== budget_timing tier3 r3 $f" >> $OUT/quick_v18.out
  PYTHONPATH=. $PY bot_research/tmp/qscen.py $OUT/quick "$V18" "$BT&budget_fraction=$f" none >> $OUT/quick_v18.out 2>&1
done
V18G="bot_research.experiments.lead.v18:@make?$P&fortress_guns=true"
for o in 'bot_research.bots.counters.forecast_timing:@make?attack_round=8&tier=tier5&attack_share=1.0&model_lam=1.0' \
         'bot_research.bots.counters.feature_bluff:@make?turret_round=2' 'bot_research.bots.defense.frozen.v22.fortress:@make' \
         'bot_research.bots.counters.guarded_schedule:@make?schedule=[[1,"tier1",1],[8,"tier4",200]]'; do
  echo "== $o" >> $OUT/quick_v18g.out
  PYTHONPATH=. $PY bot_research/tmp/qscen.py $OUT/quickg "$V18G" "$o" none >> $OUT/quick_v18g.out 2>&1
done
echo "quick done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted2 t8a "'$V17'" --keep-logs losses > bot_research/runs/lead/t8a.out 2>&1
echo "t8a done $(date -u +%FT%TZ)"
Q='"big_threat":100,"gun_cap":120,"poke_until":3,"big_partial":true,"r1_poke":3,"attack_mode":"adaptive","poke_reactive":"turret","fortress_n":4,"immune_attack":true,"foreign_policy":"econ17","mid_until":5'
MODEL=v17 GRID=full COUNTER=stateful bot_research/experiments/lead/run_screens.sh s15 "{$Q}" > bot_research/runs/lead/s15.out 2>&1
echo "== queue_c9a done $(date -u +%FT%TZ)"
