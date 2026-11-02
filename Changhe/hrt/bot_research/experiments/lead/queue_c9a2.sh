#!/bin/bash
# Cycle-9 queue, chain A, second version (written 2026-10-31T09:39Z; one computation slot). Replaces queue_c9a.sh
# after its same_v18j0 step (8/8 same), its V18 games and its first V18g pairing (forecast_timing r8 tier5, left
# running). Waits for that pairing, then:
#   c9/quick_v18g.out  V18g (fortress_guns=true) against the other three fortress-sensitive opponents, both seats;
#   c9/same_v18j0_scen.out  v18 (mid_joint=0.0, foreign_target unset) against V17 under mirror:1:2 and asym:23:2
#                      (checks v18's foreign-switch wrapper);
#   t8a  TARGETED2 for V17 (standard start; the foreign target plays no role there);
#   fx1  V17 against the new foreign-map opponents and V18 with foreign_target fortress26 and econ19 against the
#        foreign pool, all under the four scripted openings of sc1;
#   s15  stateful forecaster screen of V17 (MODEL=v17 GRID=full COUNTER=stateful).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
PY="taskset -c 20,21 nice -n 19 .venv/bin/python -B"
while pgrep -f 'tmp/qscen[.]py' >/dev/null; do sleep 15; done
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V17="bot_research.experiments.lead.v17:@make?$P"
V18J0="bot_research.experiments.lead.v18:@make?$P&mid_joint=0.0"
V18="bot_research.experiments.lead.v18:@make?$P&mid_joint=1.0"
V18G="bot_research.experiments.lead.v18:@make?$P&fortress_guns=true"
V18B="bot_research.experiments.lead.v18:@make?$P"
BT='bot_research.bots.counters.budget_timing:@make?tier="tier3"&attack_round=3'
OUT=bot_research/runs/lead/c9
echo "start $(date -u +%FT%TZ)"
for o in 'bot_research.bots.counters.feature_bluff:@make?turret_round=2' 'bot_research.bots.defense.frozen.v22.fortress:@make' \
         'bot_research.bots.counters.guarded_schedule:@make?schedule=[[1,"tier1",1],[8,"tier4",200]]'; do
  echo "== $o" >> $OUT/quick_v18g.out
  PYTHONPATH=. $PY bot_research/tmp/qscen.py $OUT/quickg "$V18G" "$o" none >> $OUT/quick_v18g.out 2>&1
done
echo "quick done $(date -u +%FT%TZ)"
$PY -m bot_research.experiments.lead.same_actions_scen "$V18J0" "$V17" $OUT/same_scen \
  --opponents 'bot_research.bots.economy.frozen.v17.econ17:@make?free_fallback="zero"&foreign_attack_from=11' \
  --scenarios mirror:1:2 asym:23:2 > $OUT/same_v18j0_scen.out 2>&1
echo "same_v18j0_scen exit $? $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted2 t8a "'$V17'" --keep-logs losses > bot_research/runs/lead/t8a.out 2>&1
echo "t8a done $(date -u +%FT%TZ)"
SC="--scenarios mirror:1:2 asym:3:2 mirror:22:3 asym:23:2"
bot_research/experiments/lead/run_pool.sh new_foreign fx1a "'$V17'" $SC --keep-logs losses > bot_research/runs/lead/fx1a.out 2>&1
echo "fx1a done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh foreign fx1b "'$V18B&foreign_target=\"fortress26\"' '$V18B&foreign_target=\"econ19\"'" $SC --keep-logs losses > bot_research/runs/lead/fx1b.out 2>&1
echo "fx1b done $(date -u +%FT%TZ)"
Q='"big_threat":100,"gun_cap":120,"poke_until":3,"big_partial":true,"r1_poke":3,"attack_mode":"adaptive","poke_reactive":"turret","fortress_n":4,"immune_attack":true,"foreign_policy":"econ17","mid_until":5'
MODEL=v17 GRID=full COUNTER=stateful bot_research/experiments/lead/run_screens.sh s15 "{$Q}" > bot_research/runs/lead/s15.out 2>&1
echo "== queue_c9a2 done $(date -u +%FT%TZ)"
