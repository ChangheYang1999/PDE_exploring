#!/bin/bash
# Cycle-9 queue, chain B, ninth version (written 2026-10-31T10:43Z; one computation slot). Replaces queue_c9b8.sh
# during its last quick game (qscen PID 829253, left running), before its c9h step. Reason: t8e (V18E on
# TARGETED2) is 22-20-6 against V17's 20-16-12 but loses guard_geometry [tier1] -973 in round 13 (V17 -5): mid_joint
# bought two gun1 in round 2 and a gun1 in round 3, catch_up a tier2 in round 4 (+12, so we led), and with 9
# factories at rounds 5-9 against the opponent's 24-89 the big-threat insurance took all our gold; the opponent,
# now behind, locked at round 10 and flooded with tier5 from round 11. quick_cu1 (V18E&catch_up_share=1.0): -961
# there. mid_joint is therefore dropped from the candidate. Now:
#   t8f  TARGETED2 for V18F = v18 P&fortress_guns=true&catch_up=true and V18F1 = V18F&catch_up_share=1.0.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 829253 2>/dev/null; do sleep 15; done
echo "quick_cu1 done (seen by c9b9) $(date -u +%FT%TZ)"
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V18F="bot_research.experiments.lead.v18:@make?$P&fortress_guns=true&catch_up=true"
bot_research/experiments/lead/run_pool.sh targeted2 t8f "'$V18F' '$V18F&catch_up_share=1.0'" --keep-logs losses > bot_research/runs/lead/t8f.out 2>&1
echo "== queue_c9b9 done $(date -u +%FT%TZ)"
