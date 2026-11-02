#!/bin/bash
# Cycle-9 queue, chain B, thirteenth version (written 2026-10-31T11:25Z; one computation slot). Replaces queue_c9b12.sh while it
# waited: waits for c9h (PID 1779553), then
#   t9b  V17 (the best_v9b twin) on pools.py TEAMMATES3, the paired baseline for t9a;
#   fx2  V21E = v21 P&fortress_guns=true&catch_up=true&mid_joint=0.75&mid_level=true&foreign_target="econ21" on
#        the nine foreign-map opponents under the four sc1 openings (paired with the econ20 rows of fx1c and fx1d);
#   c9i  f5t for V18FT = v19 P&fortress_guns=true&catch_up=true&foreign_target="econ20" (ablation of mid_joint).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 1779553 2>/dev/null; do sleep 15; done
echo "c9h done (seen by c9b13) $(date -u +%FT%TZ)"
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V17="bot_research.experiments.lead.v17:@make?$P"
V21E="bot_research.experiments.lead.v21:@make?$P&fortress_guns=true&catch_up=true&mid_joint=0.75&mid_level=true&foreign_target=\"econ21\""
V18FT="bot_research.experiments.lead.v19:@make?$P&fortress_guns=true&catch_up=true&foreign_target=\"econ20\""
SC="--scenarios mirror:1:2 asym:3:2 mirror:22:3 asym:23:2"
bot_research/experiments/lead/run_pool.sh teammates3 t9b "'$V17'" --keep-logs losses > bot_research/runs/lead/t9b.out 2>&1
echo "t9b done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh foreign fx2 "'$V21E'" $SC --keep-logs losses > bot_research/runs/lead/fx2.out 2>&1
echo "fx2 done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh f5t c9i "'$V18FT'" --keep-logs losses > bot_research/runs/lead/c9i.out 2>&1
echo "== queue_c9b13 done $(date -u +%FT%TZ)"
