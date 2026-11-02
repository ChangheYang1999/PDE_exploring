#!/bin/bash
# Cycle-9 queue, chain B, fifteenth version (written 2026-10-31T11:53Z; one computation slot). Replaces queue_c9b14.sh (killed
# while c9j ran; fx2 of V21E dropped with the joint plan). Waits for the orphaned c9j tournament (PID 2318692, V22G on
# f5t), then
#   c9l  f5t for V24G (V18FT with r1_gun=[4,1]; pair with c9i);
#   t9h  V18FT on pools.py TARGETED3_V18FT (TEAMMATES3, GuardedForecast modelling V18FT with six rosters, fortress v32);
#   t9i  V24G on TARGETED3_V24G (the same with GuardedForecast modelling V24G).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 2318692 2>/dev/null; do sleep 15; done
echo "c9j done (seen by c9b15) $(date -u +%FT%TZ)"
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V18FT="bot_research.experiments.lead.v19:@make?$P&fortress_guns=true&catch_up=true&foreign_target=\"econ20\""
V24G="bot_research.experiments.lead.v22:@make?$P&fortress_guns=true&catch_up=true&foreign_target=\"econ20\"&r1_gun=[4,1]"
bot_research/experiments/lead/run_pool.sh f5t c9l "'$V24G'" --keep-logs losses > bot_research/runs/lead/c9l.out 2>&1
echo "c9l done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted3_v18ft t9h "'$V18FT'" --keep-logs losses > bot_research/runs/lead/t9h.out 2>&1
echo "t9h done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted3_v24g t9i "'$V24G'" --keep-logs losses > bot_research/runs/lead/t9i.out 2>&1
echo "== queue_c9b15 done $(date -u +%FT%TZ)"
