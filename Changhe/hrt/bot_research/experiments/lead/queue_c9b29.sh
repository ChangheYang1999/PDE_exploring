#!/bin/bash
# Cycle-9 queue, chain B, twenty-ninth version (written 2026-10-31T14:52Z; one computation slot). Replaces queue_c9b28.sh (stopped
# while its gm3 tournament, PID 619518, kept running). hd2 (v29 strike_until) dropped: hrt-w3's early-guard campaign
# (notes/validation.md 14:47:58Z) refutes strike_until 6 and 7 on H10. Waits for gm3, then the gating pools for the
# two repair candidates P4TNUB and P5TNUBM: c9p f5t (pair with c9i V18FT), t8i TARGETED2, pu2 PUNISH, b9c BLUFFCOV.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
PAR="poke_reactive=\"turret_only\"&fail_limit=2&passive_turret=false&robust_k=null&behind_mode=\"current\""
P4TNUB="bot_research.experiments.lead.v28:@make?$PAR&passive_until=4"
P5TNUBM="bot_research.experiments.lead.v30:@make?passive_until=5&$PAR&passive_mid_from=5"
while kill -0 619518 2>/dev/null; do sleep 15; done
echo "gm3 done (seen by queue_c9b29) $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh f5t c9p "'$P4TNUB' '$P5TNUBM'" --keep-logs losses > bot_research/runs/lead/c9p.out 2>&1
echo "c9p done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted2 t8i "'$P4TNUB' '$P5TNUBM'" --keep-logs losses > bot_research/runs/lead/t8i.out 2>&1
echo "t8i done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh punish pu2 "'$P4TNUB' '$P5TNUBM'" --keep-logs losses > bot_research/runs/lead/pu2.out 2>&1
echo "pu2 done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh bluffcov b9c "'$P4TNUB' '$P5TNUBM'" --keep-logs losses > bot_research/runs/lead/b9c.out 2>&1
echo "== queue_c9b29 done $(date -u +%FT%TZ)"
