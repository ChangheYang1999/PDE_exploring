#!/bin/bash
# Cycle-9 queue, chain B, twenty-seventh version (written 2026-10-31T14:29Z; one computation slot). Replaces queue_c9b26.sh (stopped
# while its t8h tournament, PID 364471, kept running). Adds hd2, a development run of v29 (strike_until) on HANDOFF.
# Waits for t8h, then
#   hd2  HANDOFF: P5TNUB + strike_until=6, P5TNUB + strike_until=7 (v29; pair with hd1);
#   t9i  TARGETED3_P5TF: P5TNU, P5TNUB;
#   st3  STAGED: P5TNUB (pair with st1, st2);
#   sg2  SCREENED: P5TNUB (pair with sg1).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 364471 2>/dev/null; do sleep 15; done
echo "t8h done (seen by c9b27) $(date -u +%FT%TZ)"
PAR="passive_until=5&poke_reactive=\"turret_only\"&fail_limit=2&passive_turret=false&robust_k=null"
P5TNU="bot_research.experiments.lead.v27:@make?$PAR"
P5TNUB="bot_research.experiments.lead.v28:@make?$PAR&behind_mode=\"current\""
S6="bot_research.experiments.lead.v29:@make?$PAR&behind_mode=\"current\"&strike_until=6"
S7="bot_research.experiments.lead.v29:@make?$PAR&behind_mode=\"current\"&strike_until=7"
bot_research/experiments/lead/run_pool.sh handoff hd2 "'$S6' '$S7'" --keep-logs losses > bot_research/runs/lead/hd2.out 2>&1
echo "hd2 done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted3_p5tf t9i "'$P5TNU' '$P5TNUB'" --keep-logs losses > bot_research/runs/lead/t9i.out 2>&1
echo "t9i done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh staged st3 "'$P5TNUB'" --keep-logs losses > bot_research/runs/lead/st3.out 2>&1
echo "st3 done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh screened sg2 "'$P5TNUB'" --keep-logs losses > bot_research/runs/lead/sg2.out 2>&1
echo "== queue_c9b27 done $(date -u +%FT%TZ)"
