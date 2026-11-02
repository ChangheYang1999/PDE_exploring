#!/bin/bash
# Cycle-9 queue, chain B, sixth version (written 2026-10-31T10:17Z; one computation slot). Attribution games
# (c9/quick_attr.out, seat 0): catch_up alone turns guard_geometry [tier1] from -5 into +7 and keeps
# corner [] 0, econ17 +10, budget_timing tier3 r3 0.5 -26; mid_joint=1.0 alone loses -1120 to corner [] and
# -270 to econ17 (rejected); fortress_guns alone 0 / -5 / +10 / -26 (no change); mid_joint=0.75 0 / -5 / +10 / 0.
# Candidate V18E = V17 + catch_up + fortress_guns + mid_joint=0.75 (experiments/lead/v18.py):
#   t8e  TARGETED2 for V18E (V17 20-16-12 in t8a);
#   c9h  f5t for V18E (V17 68-4-4 in c8m).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V18E="bot_research.experiments.lead.v18:@make?$P&mid_joint=0.75&fortress_guns=true&catch_up=true"
echo "start $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted2 t8e "'$V18E'" --keep-logs losses > bot_research/runs/lead/t8e.out 2>&1
echo "t8e done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh f5t c9h "'$V18E'" --keep-logs losses > bot_research/runs/lead/c9h.out 2>&1
echo "== queue_c9b6 done $(date -u +%FT%TZ)"
