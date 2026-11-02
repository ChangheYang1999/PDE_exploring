#!/bin/bash
# Cycle-9 queue, chain A, twenty-fourth version (written 2026-10-31T14:44Z; one computation slot). Replaces queue_c9a23.sh (stopped
# while its c9n tournament, PID 371840, kept running; gq1 and pu2 dropped for now). Round-5 striker repair candidates:
#   P4TNUB  = v28 P5TNUB parameters with passive_until=4 (insurance again from round 5);
#   P5TNUBM = v30 P5TNUB parameters + passive_mid_from=5 (tier1-tier3 insurance in passive round 5).
# Waits for c9n, then tm1 TIMING (P4TNUB, P5TNUBM), g9c GROWERS (P4TNUB, P5TNUBM).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
PAR="poke_reactive=\"turret_only\"&fail_limit=2&passive_turret=false&robust_k=null&behind_mode=\"current\""
P4TNUB="bot_research.experiments.lead.v28:@make?$PAR&passive_until=4"
P5TNUBM="bot_research.experiments.lead.v30:@make?passive_until=5&$PAR&passive_mid_from=5"
S6="bot_research.experiments.lead.v29:@make?passive_until=5&$PAR&strike_until=6"
S7="bot_research.experiments.lead.v29:@make?passive_until=5&$PAR&strike_until=7"
while kill -0 371840 2>/dev/null; do sleep 15; done
echo "c9n done (seen by queue_c9a24) $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh timing tm1 "'$P4TNUB' '$P5TNUBM'" --keep-logs losses > bot_research/runs/lead/tm1.out 2>&1
echo "tm1 done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh growers g9c "'$P4TNUB' '$P5TNUBM'" --keep-logs losses > bot_research/runs/lead/g9c.out 2>&1
echo "== queue_c9a24 done $(date -u +%FT%TZ)"
