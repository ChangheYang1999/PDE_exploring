#!/bin/bash
# Cycle-9 queue, chain A, twenty-second version (written 2026-10-31T13:40Z; one computation slot). Replaces queue_c9a21.sh (stopped
# while its sg1 tournament, PID 4023968, kept running) to add pu1. Waits for sg1 (SCREENED: P5TF, P5TFU, P5TNU), then
#   pu1  PUNISH (pools.py "punish": hrt-w1's counter_astra33 and counter_astra28, guarded_schedule with 200 copies of
#        tier3/4/5 from round 3-7; 17 settings, both seats): V18FT, P5TF, P5TN, P5TNU (risk of passive_turret=false);
#   gq1  GUARDED_MAZE (pair with gm2): P5TN, P5TNU;
#   c9n  f5t: P5TF, P5TNU (pair with c9i, V18FT 70-6-0);
#   c9o  f5t: P5T (ablation of fail_limit).
# Spec names as in queue_c9a21.sh; V18FT = best_v9e's twin.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 4023968 2>/dev/null; do sleep 15; done
echo "sg1 done (seen by c9a22) $(date -u +%FT%TZ)"
PAR="passive_until=5&poke_reactive=\"turret_only\""
V18FT='bot_research.experiments.lead.v19:@make?big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5&fortress_guns=true&catch_up=true&foreign_target="econ20"'
P5T="bot_research.experiments.lead.v24:@make?$PAR"
P5TF="$P5T&fail_limit=2"
P5TN="bot_research.experiments.lead.v26:@make?$PAR&fail_limit=2&passive_turret=false"
P5TNU="bot_research.experiments.lead.v27:@make?$PAR&fail_limit=2&passive_turret=false&robust_k=null"
bot_research/experiments/lead/run_pool.sh punish pu1 "'$V18FT' '$P5TF' '$P5TN' '$P5TNU'" --keep-logs losses > bot_research/runs/lead/pu1.out 2>&1
echo "pu1 done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh guarded_maze gq1 "'$P5TN' '$P5TNU'" --keep-logs losses > bot_research/runs/lead/gq1.out 2>&1
echo "gq1 done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh f5t c9n "'$P5TF' '$P5TNU'" --keep-logs losses > bot_research/runs/lead/c9n.out 2>&1
echo "c9n done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh f5t c9o "'$P5T'" --keep-logs losses > bot_research/runs/lead/c9o.out 2>&1
echo "== queue_c9a22 done $(date -u +%FT%TZ)"
