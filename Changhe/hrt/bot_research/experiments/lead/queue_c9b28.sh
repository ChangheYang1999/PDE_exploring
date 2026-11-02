#!/bin/bash
# Cycle-9 queue, chain B, twenty-eighth version (written 2026-10-31T14:44Z; one computation slot). Replaces queue_c9b27.sh (stopped
# while its t8h tournament, PID 364471, kept running; t9i, st3, sg2 dropped for now). Waits for t8h, then gm3
# GUARDED_MAZE (P4TNUB, P5TNUBM; see queue_c9a24.sh) and hd2 HANDOFF (v29 P5TNUB + strike_until=6 / =7).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
PAR="poke_reactive=\"turret_only\"&fail_limit=2&passive_turret=false&robust_k=null&behind_mode=\"current\""
P4TNUB="bot_research.experiments.lead.v28:@make?$PAR&passive_until=4"
P5TNUBM="bot_research.experiments.lead.v30:@make?passive_until=5&$PAR&passive_mid_from=5"
S6="bot_research.experiments.lead.v29:@make?passive_until=5&$PAR&strike_until=6"
S7="bot_research.experiments.lead.v29:@make?passive_until=5&$PAR&strike_until=7"
while kill -0 364471 2>/dev/null; do sleep 15; done
echo "t8h done (seen by queue_c9b28) $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh guarded_maze gm3 "'$P4TNUB' '$P5TNUBM'" --keep-logs losses > bot_research/runs/lead/gm3.out 2>&1
echo "gm3 done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh handoff hd2 "'$S6' '$S7'" --keep-logs losses > bot_research/runs/lead/hd2.out 2>&1
echo "== queue_c9b28 done $(date -u +%FT%TZ)"
