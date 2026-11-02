#!/bin/bash
# Cycle-9 queue, chain A, nineteenth version (written 2026-10-31T13:15Z; one computation slot). Replaces queue_c9a18.sh (stopped
# with its gm1 tournament after 20 games, kept as runs/lead/gm1_stopped) after g9a (P5T 142-0-0, P5 138-0-4) and
# hrt-w3's 13:14Z sticky-attack ablation (P5 with fail_limit=2 wins the staged-guard grower R4/R6 that P5 loses).
#   gm2  V18FT, P5T and P5TF on pools.py GUARDED_MAZE (72 settings, both seats);
#   c9n  f5t for P5T and P5TF (pair with c9i, V18FT 70-6-0).
# P5T = v24 passive_until=5&poke_reactive="turret_only"; P5TF = P5T&fail_limit=2.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V18FT="bot_research.experiments.lead.v19:@make?$P&fortress_guns=true&catch_up=true&foreign_target=\"econ20\""
P5T="bot_research.experiments.lead.v24:@make?passive_until=5&poke_reactive=\"turret_only\""
P5TF="$P5T&fail_limit=2"
bot_research/experiments/lead/run_pool.sh guarded_maze gm2 "'$V18FT' '$P5T' '$P5TF'" --keep-logs losses > bot_research/runs/lead/gm2.out 2>&1
echo "gm2 done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh f5t c9n "'$P5T' '$P5TF'" --keep-logs losses > bot_research/runs/lead/c9n.out 2>&1
echo "== queue_c9a19 done $(date -u +%FT%TZ)"
