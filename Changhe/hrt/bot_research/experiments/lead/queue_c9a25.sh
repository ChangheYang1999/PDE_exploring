#!/bin/bash
# Cycle-9 queue, chain A follow-up (written 2026-10-31T14:52Z; one computation slot). Waits for the queue_c9a24.sh bash (PID 572103:
# c9n, tm1, g9c), then the remaining broad pools for P4TNUB and P5TNUBM: st3 STAGED, sg2 SCREENED, hd2 HANDOFF,
# t9j TARGETED3_P5TF (pair with t9h).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
PAR="poke_reactive=\"turret_only\"&fail_limit=2&passive_turret=false&robust_k=null&behind_mode=\"current\""
P4TNUB="bot_research.experiments.lead.v28:@make?$PAR&passive_until=4"
P5TNUBM="bot_research.experiments.lead.v30:@make?passive_until=5&$PAR&passive_mid_from=5"
while kill -0 572103 2>/dev/null; do sleep 15; done
echo "queue_c9a24 done (seen by queue_c9a25) $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh staged st3 "'$P4TNUB' '$P5TNUBM'" --keep-logs losses > bot_research/runs/lead/st3.out 2>&1
echo "st3 done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh screened sg2 "'$P4TNUB' '$P5TNUBM'" --keep-logs losses > bot_research/runs/lead/sg2.out 2>&1
echo "sg2 done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh handoff hd2 "'$P4TNUB' '$P5TNUBM'" --keep-logs losses > bot_research/runs/lead/hd2.out 2>&1
echo "hd2 done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted3_p5tf t9j "'$P4TNUB' '$P5TNUBM'" --keep-logs losses > bot_research/runs/lead/t9j.out 2>&1
echo "== queue_c9a25 done $(date -u +%FT%TZ)"
