#!/bin/bash
# Cycle-9 queue, chain B, fifth version (written 2026-10-31T10:07Z; one computation slot). queue_c9b4.sh was stopped
# after its first quick games: V18D (mid_joint=1.0, fortress_guns, catch_up) lost -1120 (round 12) to
# guard_geometry roster [] and -973 to roster [tier1], where best_v9b drew 0 and lost -5, and -270 to econ17
# (best_v9b -10). Attribution, seat 0 only (qscen QSEATS=0; seat pairs were identical in every quick game so far):
#   c9/quick_attr.out  V17C (catch_up only), V18 (mid_joint=1.0 only), V18G (fortress_guns only), V18M75
#                      (mid_joint=0.75) against corner rosters [] and [tier1], econ17, budget_timing tier3 r3 0.5.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1 QSEATS=0
PY="taskset -c 20,21 nice -n 19 .venv/bin/python -B"
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V="bot_research.experiments.lead.v18:@make?$P"
OUT=bot_research/runs/lead/c9
K=bot_research.bots.counters
echo "start $(date -u +%FT%TZ)"
for c in "$V&catch_up=true" "$V&mid_joint=1.0" "$V&fortress_guns=true" "$V&mid_joint=0.75"; do
  for o in "$K.guard_geometry:@make?roster=[]" "$K.guard_geometry:@make?roster=[\"tier1\"]" \
           'bot_research.bots.economy.frozen.v17.econ17:@make?free_fallback="zero"&foreign_attack_from=11' \
           "$K.budget_timing:@make?tier=\"tier3\"&attack_round=3&budget_fraction=0.5"; do
    echo "== ${c##*mid_until=5&} | $o" >> $OUT/quick_attr.out
    PYTHONPATH=. $PY bot_research/tmp/qscen.py $OUT/quicka "$c" "$o" none >> $OUT/quick_attr.out 2>&1
  done
done
echo "== queue_c9b5 done $(date -u +%FT%TZ)"
