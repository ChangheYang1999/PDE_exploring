#!/bin/bash
# Cycle-9 queue, chain B, seventh version (written 2026-10-31T10:33Z; one computation slot). Replaces queue_c9b6.sh
# while its t8e tournament runs (PID 449403, left running). t8e so far: V18E still loses guard_roster
# [tier1,tier1] -5 (log 00029: round-1 exchange -5, no catch-up attack in rounds 2-5 because half of the factory
# gold, about 65, buys no tier3, and tier1/tier2 die to the two gun1). After t8e:
#   quick  seat-0 games of V18E&catch_up_share=1.0 against the guard counters, econ13/15/17 and budget_timing;
#   c9h    f5t for V18E (V17 68-4-4 in c8m).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
PY="taskset -c 20,21 nice -n 19 .venv/bin/python -B"
while kill -0 449403 2>/dev/null; do sleep 15; done
echo "t8e done (seen by c9b7) $(date -u +%FT%TZ)"
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V18E="bot_research.experiments.lead.v18:@make?$P&mid_joint=0.75&fortress_guns=true&catch_up=true"
K=bot_research.bots.counters
E=bot_research.bots.economy.frozen
$PY bot_research/tmp/quick.py "$V18E&catch_up_share=1.0" \
    "$K.guard_roster:@make?roster=[\"tier1\",\"tier1\"]" "$K.guard_roster:@make?roster=[\"tier2\"]" \
    "$K.guard_geometry:@make?roster=[\"tier1\",\"tier1\"]" "$K.guard_geometry:@make?roster=[\"tier2\"]" \
    "$K.guard_geometry:@make?roster=[\"tier1\"]" "$K.guard_geometry:@make?roster=[]" \
    "$E.v17.econ17:@make?free_fallback=\"zero\"&foreign_attack_from=11" "$E.v13.econ13:@make" \
    "$E.v15.econ15:@make?free_fallback=\"leak\"" \
    "$K.budget_timing:@make?tier=\"tier3\"&attack_round=3&budget_fraction=0.5" \
    "$K.budget_timing:@make?tier=\"tier3\"&attack_round=5&budget_fraction=0.25" > bot_research/runs/lead/c9/quick_cu1.out 2>&1
echo "quick_cu1 done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh f5t c9h "'$V18E'" --keep-logs losses > bot_research/runs/lead/c9h.out 2>&1
echo "== queue_c9b7 done $(date -u +%FT%TZ)"
