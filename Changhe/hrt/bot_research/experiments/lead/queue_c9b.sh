#!/bin/bash
# Cycle-9 queue, chain B (written 2026-10-31T09:26Z; one computation slot). Waits for the c8a tournament
# (started by queue_c8.sh, whose remaining steps s14, rr1 and rr2 were dropped at 09:26Z), then:
#   t8b  TARGETED2 for V18 = V17 + mid_joint=1.0 (experiments/lead/v18.py);
#   c9f  f5t (FRONTIER5 + TARGETED) for V18, the regression set on which V17 scored 68-4-4 (c8m).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while pgrep -f 'tournament --name c8[a] ' >/dev/null; do sleep 30; done
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V18="bot_research.experiments.lead.v18:@make?$P&mid_joint=1.0"
echo "start $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted2 t8b "'$V18'" --keep-logs losses > bot_research/runs/lead/t8b.out 2>&1
echo "t8b done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh f5t c9f "'$V18'" --keep-logs losses > bot_research/runs/lead/c9f.out 2>&1
echo "== queue_c9b done $(date -u +%FT%TZ)"
