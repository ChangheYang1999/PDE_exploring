#!/bin/bash
# Cycle-9 queue, chain A, fourteenth version (written 2026-10-31T11:53Z; one computation slot). Replaces queue_c9a13.sh while it
# waited for c9k: hrt-w3 (notes/validation.md 11:45Z) confirmed that V23R's relevance filter is bypassed by a gun1 at
# (0,2) or (9,11), so best_v9d is not promoted and the joint plan (mid_joint) is ablated instead. Waits for the
# orphaned c9k tournament (PID 2404531, V23R on f5t), then
#   b9a  V17, V18FT, V23R and V24G on pools.py BLUFFCOV (eight feature_bluff settings, both seats, all logs);
#   c9i  f5t for V18FT (V20T without mid_joint and mid_level; pair with c9h and c8m);
#   fx3  V18FT on the nine foreign-map opponents under the four sc1 openings (pair with fx1c/fx1d).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 2404531 2>/dev/null; do sleep 15; done
echo "c9k done (seen by c9a14) $(date -u +%FT%TZ)"
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V17="bot_research.experiments.lead.v17:@make?$P"
V18FT="bot_research.experiments.lead.v19:@make?$P&fortress_guns=true&catch_up=true&foreign_target=\"econ20\""
V23R="bot_research.experiments.lead.v23:@make?$P&fortress_guns=true&catch_up=true&mid_joint=0.75&mid_level=true&foreign_target=\"econ20\"&mid_relevant=true"
V24G="bot_research.experiments.lead.v22:@make?$P&fortress_guns=true&catch_up=true&foreign_target=\"econ20\"&r1_gun=[4,1]"
SC="--scenarios mirror:1:2 asym:3:2 mirror:22:3 asym:23:2"
bot_research/experiments/lead/run_pool.sh bluffcov b9a "'$V17' '$V18FT' '$V23R' '$V24G'" --keep-logs all > bot_research/runs/lead/b9a.out 2>&1
echo "b9a done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh f5t c9i "'$V18FT'" --keep-logs losses > bot_research/runs/lead/c9i.out 2>&1
echo "c9i done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh foreign fx3 "'$V18FT'" $SC --keep-logs losses > bot_research/runs/lead/fx3.out 2>&1
echo "== queue_c9a14 done $(date -u +%FT%TZ)"
