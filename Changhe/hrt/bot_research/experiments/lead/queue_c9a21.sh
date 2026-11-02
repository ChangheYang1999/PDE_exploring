#!/bin/bash
# Cycle-9 queue, chain A, twenty-first version (written 2026-10-31T13:37Z; one computation slot). Replaces queue_c9a20.sh (stopped
# while its gm2 tournament, PID 3770625, kept running) to add v27's robust_k=null (hrt-w3 13:26Z-13:32Z: the robust
# rule evaluates only the best two tiers; screened_guard_maze beats P5TF 520:755). Waits for gm2, then
#   sg1  SCREENED (30 screened_guard_maze settings, both seats): P5TF, P5TFU, P5TNU;
#   gq1  GUARDED_MAZE (72 settings, both seats; pair with gm2): P5TN, P5TNU;
#   c9n  f5t: P5TF, P5TNU (pair with c9i, V18FT 70-6-0);
#   c9o  f5t: P5T (ablation of fail_limit).
# P5T = v24 passive_until=5&poke_reactive="turret_only"; P5TF = P5T&fail_limit=2;
# P5TN = v26 with P5TF's parameters and passive_turret=false; P5TFU = v27 with P5TF's parameters and robust_k=null;
# P5TNU = v27 with P5TN's parameters and robust_k=null.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 3770625 2>/dev/null; do sleep 15; done
echo "gm2 done (seen by c9a21) $(date -u +%FT%TZ)"
PAR="passive_until=5&poke_reactive=\"turret_only\""
P5T="bot_research.experiments.lead.v24:@make?$PAR"
P5TF="$P5T&fail_limit=2"
P5TN="bot_research.experiments.lead.v26:@make?$PAR&fail_limit=2&passive_turret=false"
P5TFU="bot_research.experiments.lead.v27:@make?$PAR&fail_limit=2&robust_k=null"
P5TNU="bot_research.experiments.lead.v27:@make?$PAR&fail_limit=2&passive_turret=false&robust_k=null"
bot_research/experiments/lead/run_pool.sh screened sg1 "'$P5TF' '$P5TFU' '$P5TNU'" --keep-logs losses > bot_research/runs/lead/sg1.out 2>&1
echo "sg1 done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh guarded_maze gq1 "'$P5TN' '$P5TNU'" --keep-logs losses > bot_research/runs/lead/gq1.out 2>&1
echo "gq1 done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh f5t c9n "'$P5TF' '$P5TNU'" --keep-logs losses > bot_research/runs/lead/c9n.out 2>&1
echo "c9n done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh f5t c9o "'$P5T'" --keep-logs losses > bot_research/runs/lead/c9o.out 2>&1
echo "== queue_c9a21 done $(date -u +%FT%TZ)"
