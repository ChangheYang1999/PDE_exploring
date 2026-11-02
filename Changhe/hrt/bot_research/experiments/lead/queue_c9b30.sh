#!/bin/bash
# Cycle-9 queue, chain B, thirtieth version (written 2026-10-31T14:57Z; one computation slot). Replaces queue_c9b29.sh (stopped
# while waiting for gm3, PID 619518; nothing of it had started). Adds tm2 first: TIMING2 (pools.py "timing2":
# budget_timing tier1-tier4 striking in rounds 2-6) for V18FT, P4TNUB and P5TNUBM, because a strike inside the passive
# window is the obvious counter to both repairs. Then c9p f5t, t8i TARGETED2, pu2 PUNISH, b9c BLUFFCOV (P4TNUB, P5TNUBM).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
PAR="poke_reactive=\"turret_only\"&fail_limit=2&passive_turret=false&robust_k=null&behind_mode=\"current\""
P4TNUB="bot_research.experiments.lead.v28:@make?$PAR&passive_until=4"
P5TNUBM="bot_research.experiments.lead.v30:@make?passive_until=5&$PAR&passive_mid_from=5"
V18FT="bot_research.experiments.lead.v19:@make?big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode=\"adaptive\"&poke_reactive=\"turret\"&fortress_n=4&immune_attack=true&foreign_policy=\"econ17\"&mid_until=5&fortress_guns=true&catch_up=true&foreign_target=\"econ20\""
while kill -0 619518 2>/dev/null; do sleep 15; done
echo "gm3 done (seen by queue_c9b30) $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh timing2 tm2 "'$V18FT' '$P4TNUB' '$P5TNUBM'" --keep-logs losses > bot_research/runs/lead/tm2.out 2>&1
echo "tm2 done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh f5t c9p "'$P4TNUB' '$P5TNUBM'" --keep-logs losses > bot_research/runs/lead/c9p.out 2>&1
echo "c9p done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh targeted2 t8i "'$P4TNUB' '$P5TNUBM'" --keep-logs losses > bot_research/runs/lead/t8i.out 2>&1
echo "t8i done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh punish pu2 "'$P4TNUB' '$P5TNUBM'" --keep-logs losses > bot_research/runs/lead/pu2.out 2>&1
echo "pu2 done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh bluffcov b9c "'$P4TNUB' '$P5TNUBM'" --keep-logs losses > bot_research/runs/lead/b9c.out 2>&1
echo "== queue_c9b30 done $(date -u +%FT%TZ)"
