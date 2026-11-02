#!/bin/bash
# Cycle-9 queue, chain B, twenty-fourth version (written 2026-10-31T13:29Z; one computation slot). Replaces queue_c9b23.sh (stopped
# while its st1 tournament, PID 3791184, kept running) to add P5TN (v26, passive_turret=false) and drop P5T after st1.
# Waits for st1, then
#   smoke  the smoke command with --output bot_research/runs/best-vs-idle-bestpy-v9e-000001.jsonl;
#   st2  P5TN on STAGED (pair with st1);
#   g9b  P5TF and P5TN on GROWERS (pair with g9a);
#   b9b  P5TF and P5TN on BLUFFCOV (pair with b9a);
#   t8h  P5TF and P5TN on TARGETED2 (pair with t8f);
#   t9i  P5TF and P5TN on TARGETED3_P5TF (TEAMMATES3, GuardedForecast with an exact model of P5TF, fortress v32).
# P5TF = v24 passive_until=5&poke_reactive="turret_only"&fail_limit=2; P5TN = v26 with P5TF's parameters and
# passive_turret=false.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 3791184 2>/dev/null; do sleep 15; done
echo "st1 done (seen by c9b24) $(date -u +%FT%TZ)"
OUT=bot_research/runs/lead/promote_v9e
.venv/bin/python -B -m td_game.runner --balanced --bot-a bot_research.bots.best:decide --bot-b td_bots.protocol:idle \
  --output bot_research/runs/best-vs-idle-bestpy-v9e-000001.jsonl > $OUT/smoke2.out 2>&1
echo "smoke exit $? $(date -u +%FT%TZ)"
P5TF="bot_research.experiments.lead.v24:@make?passive_until=5&poke_reactive=\"turret_only\"&fail_limit=2"
P5TN="bot_research.experiments.lead.v26:@make?passive_until=5&poke_reactive=\"turret_only\"&fail_limit=2&passive_turret=false"
bot_research/experiments/lead/run_pool.sh staged st2 "'$P5TN'" --keep-logs losses > bot_research/runs/lead/st2.out 2>&1
echo "st2 done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh growers g9b "'$P5TF' '$P5TN'" --keep-logs losses > bot_research/runs/lead/g9b.out 2>&1
echo "g9b done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh bluffcov b9b "'$P5TF' '$P5TN'" --keep-logs losses > bot_research/runs/lead/b9b.out 2>&1
echo "b9b done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted2 t8h "'$P5TF' '$P5TN'" --keep-logs losses > bot_research/runs/lead/t8h.out 2>&1
echo "t8h done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted3_p5tf t9i "'$P5TF' '$P5TN'" --keep-logs losses > bot_research/runs/lead/t9i.out 2>&1
echo "== queue_c9b24 done $(date -u +%FT%TZ)"
