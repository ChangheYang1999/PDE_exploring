#!/bin/bash
# Cycle-9 queue, chain A, twenty-third version (written 2026-10-31T14:04Z; one computation slot). Replaces queue_c9a22.sh (stopped
# while its pu1 tournament, PID 4185897, kept running) to test v28 behind_mode first. Waits for pu1, then
#   hd1  HANDOFF (pools.py "handoff": hrt-w3's guard_handoff, growth 5-7, handoff round 10-14 and 16): P5TNU, P5TNUB;
#   c9n  f5t: P5TNU, P5TNUB (pair with c9i, V18FT 70-6-0);
#   gq1  GUARDED_MAZE: P5TNU, P5TNUB (pair with gm2);
#   pu2  PUNISH: P5TNUB (pair with pu1).
# P5TNUB = P5TNU on v28 with behind_mode="current"; other spec names as in queue_c9a22.sh.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 4185897 2>/dev/null; do sleep 15; done
echo "pu1 done (seen by c9a23) $(date -u +%FT%TZ)"
PAR="passive_until=5&poke_reactive=\"turret_only\"&fail_limit=2&passive_turret=false&robust_k=null"
P5TNU="bot_research.experiments.lead.v27:@make?$PAR"
P5TNUB="bot_research.experiments.lead.v28:@make?$PAR&behind_mode=\"current\""
bot_research/experiments/lead/run_pool.sh handoff hd1 "'$P5TNU' '$P5TNUB'" --keep-logs losses > bot_research/runs/lead/hd1.out 2>&1
echo "hd1 done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh f5t c9n "'$P5TNU' '$P5TNUB'" --keep-logs losses > bot_research/runs/lead/c9n.out 2>&1
echo "c9n done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh guarded_maze gq1 "'$P5TNU' '$P5TNUB'" --keep-logs losses > bot_research/runs/lead/gq1.out 2>&1
echo "gq1 done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh punish pu2 "'$P5TNUB'" --keep-logs losses > bot_research/runs/lead/pu2.out 2>&1
echo "== queue_c9a23 done $(date -u +%FT%TZ)"
