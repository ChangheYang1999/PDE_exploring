#!/bin/bash
# Cycle-9 queue, chain A, third version (written 2026-10-31T10:00Z; one computation slot). Replaces queue_c9a2.sh
# while its t8a tournament runs (PID 4102554, left running). Waits for t8a, then:
#   c9/quick_catch.out  V18c plus catch_up (catch_up_share default and 1.0) against hrt-w3's model-free
#                       counters (guard_geometry corner rosters, direct econ17, budget_timing tier3 r3 0.5),
#                       standard start, both seats;
#   fx1a, fx1b, s15 as in queue_c9a2.sh.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
PY="taskset -c 20,21 nice -n 19 .venv/bin/python -B"
while kill -0 4102554 2>/dev/null; do sleep 15; done
echo "t8a done (seen by c9a3) $(date -u +%FT%TZ)"
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V17="bot_research.experiments.lead.v17:@make?$P"
V18B="bot_research.experiments.lead.v18:@make?$P"
V18D="bot_research.experiments.lead.v18:@make?$P&mid_joint=1.0&fortress_guns=true&catch_up=true"
OUT=bot_research/runs/lead/c9
K=bot_research.bots.counters
for c in "$V18D" "$V18D&catch_up_share=1.0"; do
  for o in "$K.guard_geometry:@make?roster=[]" "$K.guard_geometry:@make?roster=[\"tier1\"]" \
           "$K.guard_geometry:@make?roster=[\"tier1\",\"tier1\"]" "$K.guard_geometry:@make?roster=[\"tier2\"]" \
           "$K.guard_geometry:@make?roster=[\"tier1\",\"tier1\",\"tier2\"]" \
           'bot_research.bots.economy.frozen.v17.econ17:@make?free_fallback="zero"&foreign_attack_from=11' \
           "$K.budget_timing:@make?tier=\"tier3\"&attack_round=3&budget_fraction=0.5"; do
    echo "== ${c##*mid_until=5&} | $o" >> $OUT/quick_catch.out
    PYTHONPATH=. $PY bot_research/tmp/qscen.py $OUT/quickc "$c" "$o" none >> $OUT/quick_catch.out 2>&1
  done
done
echo "quick_catch done $(date -u +%FT%TZ)"
SC="--scenarios mirror:1:2 asym:3:2 mirror:22:3 asym:23:2"
bot_research/experiments/lead/run_pool.sh new_foreign fx1a "'$V17'" $SC --keep-logs losses > bot_research/runs/lead/fx1a.out 2>&1
echo "fx1a done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh foreign fx1b "'$V18B&foreign_target=\"fortress26\"' '$V18B&foreign_target=\"econ19\"'" $SC --keep-logs losses > bot_research/runs/lead/fx1b.out 2>&1
echo "fx1b done $(date -u +%FT%TZ)"
Q='"big_threat":100,"gun_cap":120,"poke_until":3,"big_partial":true,"r1_poke":3,"attack_mode":"adaptive","poke_reactive":"turret","fortress_n":4,"immune_attack":true,"foreign_policy":"econ17","mid_until":5'
MODEL=v17 GRID=full COUNTER=stateful bot_research/experiments/lead/run_screens.sh s15 "{$Q}" > bot_research/runs/lead/s15.out 2>&1
echo "== queue_c9a3 done $(date -u +%FT%TZ)"
