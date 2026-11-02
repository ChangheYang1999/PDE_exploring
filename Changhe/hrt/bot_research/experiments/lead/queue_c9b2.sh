#!/bin/bash
# Cycle-9 queue, chain B, second version (written 2026-10-31T09:41Z; one computation slot). Replaces queue_c9b.sh
# (stopped while waiting). Quick games of 09:37Z-09:41Z: mid_joint=1.0 turns budget_timing tier3 r3 0.5 from
# -26 into a draw, fortress_guns turns forecast_timing r8 tier5 from -125 into +15, so both options are combined.
# Waits for the c8a tournament, then:
#   t8b  TARGETED2 for V18c = V17 + mid_joint=1.0 + fortress_guns=true (experiments/lead/v18.py);
#   c9f  f5t (FRONTIER5 + TARGETED) for V18c, the regression set on which V17 scored 68-4-4 (c8m).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while pgrep -f 'tournament --name c8[a] ' >/dev/null; do sleep 30; done
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V18C="bot_research.experiments.lead.v18:@make?$P&mid_joint=1.0&fortress_guns=true"
echo "start $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted2 t8b "'$V18C'" --keep-logs losses > bot_research/runs/lead/t8b.out 2>&1
echo "t8b done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh f5t c9f "'$V18C'" --keep-logs losses > bot_research/runs/lead/c9f.out 2>&1
echo "== queue_c9b2 done $(date -u +%FT%TZ)"
