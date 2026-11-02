#!/bin/bash
# Cycle-9 queue, chain A, twentieth version (written 2026-10-31T13:29Z; one computation slot). Replaces queue_c9a19.sh (stopped
# while its gm2 tournament, PID 3770625, kept running) to add P5TN and P5TNR (v26, passive_turret=false): in gm2 P5T
# loses to guarded_maze with a splash in round 3 and a bait. Waits for gm2, then
#   gq1  P5TN and P5TNR on GUARDED_MAZE (72 settings, both seats; pair with gm2);
#   c9n  f5t for P5TF and P5TN (pair with c9i, V18FT 70-6-0);
#   c9o  f5t for P5T (ablation of fail_limit).
# P5T = v24 passive_until=5&poke_reactive="turret_only"; P5TF = P5T&fail_limit=2;
# P5TN = v26 passive_until=5&poke_reactive="turret_only"&fail_limit=2&passive_turret=false; P5TNR = P5TN&passive_ratio=0.5.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 3770625 2>/dev/null; do sleep 15; done
echo "gm2 done (seen by c9a20) $(date -u +%FT%TZ)"
P5T="bot_research.experiments.lead.v24:@make?passive_until=5&poke_reactive=\"turret_only\""
P5TF="$P5T&fail_limit=2"
P5TN="bot_research.experiments.lead.v26:@make?passive_until=5&poke_reactive=\"turret_only\"&fail_limit=2&passive_turret=false"
P5TNR="$P5TN&passive_ratio=0.5"
bot_research/experiments/lead/run_pool.sh guarded_maze gq1 "'$P5TN' '$P5TNR'" --keep-logs losses > bot_research/runs/lead/gq1.out 2>&1
echo "gq1 done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh f5t c9n "'$P5TF' '$P5TN'" --keep-logs losses > bot_research/runs/lead/c9n.out 2>&1
echo "c9n done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh f5t c9o "'$P5T'" --keep-logs losses > bot_research/runs/lead/c9o.out 2>&1
echo "== queue_c9a20 done $(date -u +%FT%TZ)"
