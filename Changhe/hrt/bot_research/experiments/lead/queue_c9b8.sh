#!/bin/bash
# Cycle-9 queue, chain B, eighth version (written 2026-10-31T10:38Z; one computation slot). queue_c9b7.sh failed
# in its quick step (tmp/quick.py run without PYTHONPATH) and started c9h; c9h was stopped after 3 minutes and its
# partial output removed. t8e is done. Now:
#   quick  seat-0 games (tmp/qscen.py, QSEATS=0) of V18E&catch_up_share=1.0 against the guard counters,
#          econ13/15/17 and budget_timing (out runs/lead/c9/quick_cu1.out);
#   c9h    f5t for V18E (V17 68-4-4 in c8m).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
PY="taskset -c 20,21 nice -n 19 .venv/bin/python -B"
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V18E="bot_research.experiments.lead.v18:@make?$P&mid_joint=0.75&fortress_guns=true&catch_up=true"
K=bot_research.bots.counters
E=bot_research.bots.economy.frozen
OUT=bot_research/runs/lead/c9
rm -f $OUT/quick_cu1.out
for o in "$K.guard_roster:@make?roster=[\"tier1\",\"tier1\"]" "$K.guard_roster:@make?roster=[\"tier2\"]" \
    "$K.guard_geometry:@make?roster=[\"tier1\",\"tier1\"]" "$K.guard_geometry:@make?roster=[\"tier2\"]" \
    "$K.guard_geometry:@make?roster=[\"tier1\"]" "$K.guard_geometry:@make?roster=[]" \
    "$E.v17.econ17:@make?free_fallback=\"zero\"&foreign_attack_from=11" "$E.v13.econ13:@make" \
    "$E.v15.econ15:@make?free_fallback=\"leak\"" \
    "$K.budget_timing:@make?tier=\"tier3\"&attack_round=3&budget_fraction=0.5" \
    "$K.budget_timing:@make?tier=\"tier3\"&attack_round=5&budget_fraction=0.25"; do
    echo "== $o" >> $OUT/quick_cu1.out
    QSEATS=0 PYTHONPATH=. $PY bot_research/tmp/qscen.py $OUT/quickcu1 "$V18E&catch_up_share=1.0" "$o" none >> $OUT/quick_cu1.out 2>&1
done
echo "quick_cu1 done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh f5t c9h "'$V18E'" --keep-logs losses > bot_research/runs/lead/c9h.out 2>&1
echo "== queue_c9b8 done $(date -u +%FT%TZ)"
