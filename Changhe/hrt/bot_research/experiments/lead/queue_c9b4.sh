#!/bin/bash
# Cycle-9 queue, chain B, fourth version (written 2026-10-31T10:02Z; one computation slot). Replaces queue_c9b2.sh
# (its t8b run of V18c was stopped after one minute) and queue_c9b3.sh (waiting). c8a finished at 10:01Z.
# New option catch_up (v18, 10:00Z) against hrt-w3's model-free corner-gun counters, so the candidate becomes
# V18D = V18c + catch_up=true if the quick games support it:
#   c9/quick_catch.out  V18D (catch_up_share default and 1.0) against hrt-w3's model-free counters
#                       (guard_geometry corner rosters, direct econ17, budget_timing tier3 r3 0.5), both seats;
#   t8d   TARGETED2 for V18D (V17 in t8a);
#   c9g   f5t for V18D (V17 68-4-4 in c8m);
#   fx1c  V17 against OLD_FOREIGN under the four sc1 openings (as planned in queue_c9b3.sh);
#   s16   stateful forecaster screen of V18D (MODEL=v18 GRID=full COUNTER=stateful).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
PY="taskset -c 20,21 nice -n 19 .venv/bin/python -B"
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V17="bot_research.experiments.lead.v17:@make?$P"
V18D="bot_research.experiments.lead.v18:@make?$P&mid_joint=1.0&fortress_guns=true&catch_up=true"
OUT=bot_research/runs/lead/c9
K=bot_research.bots.counters
echo "start $(date -u +%FT%TZ)"
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
bot_research/experiments/lead/run_pool.sh targeted2 t8d "'$V18D'" --keep-logs losses > bot_research/runs/lead/t8d.out 2>&1
echo "t8d done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh f5t c9g "'$V18D'" --keep-logs losses > bot_research/runs/lead/c9g.out 2>&1
echo "c9g done $(date -u +%FT%TZ)"
SC="--scenarios mirror:1:2 asym:3:2 mirror:22:3 asym:23:2"
bot_research/experiments/lead/run_pool.sh old_foreign fx1c "'$V17'" $SC --keep-logs losses > bot_research/runs/lead/fx1c.out 2>&1
echo "fx1c done $(date -u +%FT%TZ)"
Q='"big_threat":100,"gun_cap":120,"poke_until":3,"big_partial":true,"r1_poke":3,"attack_mode":"adaptive","poke_reactive":"turret","fortress_n":4,"immune_attack":true,"foreign_policy":"econ17","mid_until":5,"mid_joint":1.0,"fortress_guns":true,"catch_up":true'
MODEL=v18 GRID=full COUNTER=stateful bot_research/experiments/lead/run_screens.sh s16 "{$Q}" > bot_research/runs/lead/s16.out 2>&1
echo "== queue_c9b4 done $(date -u +%FT%TZ)"
