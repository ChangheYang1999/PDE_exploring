#!/bin/bash
# Cycle-9 queue, chain A, fourth version (written 2026-10-31T10:02Z; one computation slot). Replaces queue_c9a3.sh (whose quick catch-up games moved to queue_c9b4.sh), which replaced queue_c9a2.sh
# while its t8a tournament runs (PID 4102554, left running). Waits for t8a, then:
#   fx1a, fx1b, s15 as in queue_c9a2.sh.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
PY="taskset -c 20,21 nice -n 19 .venv/bin/python -B"
while kill -0 4102554 2>/dev/null; do sleep 15; done
echo "t8a done (seen by c9a4) $(date -u +%FT%TZ)"
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V17="bot_research.experiments.lead.v17:@make?$P"
V18B="bot_research.experiments.lead.v18:@make?$P"
V18D="bot_research.experiments.lead.v18:@make?$P&mid_joint=1.0&fortress_guns=true&catch_up=true"
OUT=bot_research/runs/lead/c9
K=bot_research.bots.counters
SC="--scenarios mirror:1:2 asym:3:2 mirror:22:3 asym:23:2"
bot_research/experiments/lead/run_pool.sh new_foreign fx1a "'$V17'" $SC --keep-logs losses > bot_research/runs/lead/fx1a.out 2>&1
echo "fx1a done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh foreign fx1b "'$V18B&foreign_target=\"fortress26\"' '$V18B&foreign_target=\"econ19\"'" $SC --keep-logs losses > bot_research/runs/lead/fx1b.out 2>&1
echo "fx1b done $(date -u +%FT%TZ)"
Q='"big_threat":100,"gun_cap":120,"poke_until":3,"big_partial":true,"r1_poke":3,"attack_mode":"adaptive","poke_reactive":"turret","fortress_n":4,"immune_attack":true,"foreign_policy":"econ17","mid_until":5'
MODEL=v17 GRID=full COUNTER=stateful bot_research/experiments/lead/run_screens.sh s15 "{$Q}" > bot_research/runs/lead/s15.out 2>&1
echo "== queue_c9a4 done $(date -u +%FT%TZ)"
