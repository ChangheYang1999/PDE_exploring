#!/bin/bash
# Cycle-9 queue, chain A, seventeenth version (written 2026-10-31T13:04Z; one computation slot). Replaces queue_c9a16.sh (stopped
# while it waited) to add R5 = v25 passive_until=5&passive_ratio=0.5 (P5 lost to the three-tier1 bait in g9a). Waits
# for g9a (PID 3414226), then
#   gm1  V18FT, P5 and R5 on pools.py GUARDED_MAZE (72 settings, both seats);
#   c9n  f5t for P5 and R5 (pair with c9i, V18FT 70-6-0).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 3414226 2>/dev/null; do sleep 15; done
echo "g9a done (seen by c9a17) $(date -u +%FT%TZ)"
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V18FT="bot_research.experiments.lead.v19:@make?$P&fortress_guns=true&catch_up=true&foreign_target=\"econ20\""
P5="bot_research.experiments.lead.v24:@make?passive_until=5"
R5="bot_research.experiments.lead.v25:@make?passive_until=5&passive_ratio=0.5"
bot_research/experiments/lead/run_pool.sh guarded_maze gm1 "'$V18FT' '$P5' '$R5'" --keep-logs losses > bot_research/runs/lead/gm1.out 2>&1
echo "gm1 done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh f5t c9n "'$P5' '$R5'" --keep-logs losses > bot_research/runs/lead/c9n.out 2>&1
echo "== queue_c9a17 done $(date -u +%FT%TZ)"
