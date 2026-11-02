#!/bin/bash
# Slot A after queue_v33a (written 2026-10-31T16:55Z): quick v34 games (qg_v34.sh, runs/lead/qg_v34.out), then v33 (3, 60) on
# hrt-w2's strike1 set (STRIKE1, run x33s1; best_v9e, P4TNUB and P5TNUBM on it: runs/economy/strike1, strike1b).
# Waits for the PID given as $1.
cd "$(dirname "$0")/../../.." || exit 1
while [ -n "$1" ] && kill -0 "$1" 2>/dev/null; do sleep 20; done
echo "start qg_v34 $(date -u +%FT%TZ)"
bot_research/experiments/lead/qg_v34.sh > bot_research/runs/lead/qg_v34.out 2>&1
echo "end qg_v34 exit $? $(date -u +%FT%TZ)"
PAR="poke_reactive=\"turret_only\"&fail_limit=2&passive_turret=false&robust_k=null&behind_mode=\"current\""
V33="bot_research.experiments.lead.v33:@make?passive_until=5&$PAR&passive_mid_from=5&passive_cheap_from=3&passive_cheap_cap=60"
echo "start x33s1 (strike1) $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh strike1 x33s1 "'$V33'" --keep-logs losses > bot_research/runs/lead/x33s1.out 2>&1
echo "end x33s1 exit $? $(date -u +%FT%TZ)"
echo "== queue_v34q done $(date -u +%FT%TZ)"
