#!/bin/bash
# Cycle-9 queue, chain A, fifteenth version (written 2026-10-31T12:44Z; one computation slot). queue_c9a14.sh and its fx3
# tournament were stopped at 12:35Z (fx3 partial, 40 of 72 games) to free the slot for hrt-w3's grower counters
# (notes/validation.md 12:00Z-12:22Z: V18FT 20W-52L on their maze grid). Waits for the quick screen qrun1
# (PID 3260418), then
#   g9a  V17, V18FT, P5 (v24 passive_until=5) and P5T (P5 + poke_reactive="turret_only") on pools.py GROWERS
#        (35 roster_bait + 36 maze_grower settings, both seats);
#   c9n  f5t for P5 (pair with c9i, V18FT 70-6-0).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while kill -0 3260418 2>/dev/null; do sleep 15; done
echo "qrun1 done (seen by c9a15) $(date -u +%FT%TZ)"
P='big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5'
V17="bot_research.experiments.lead.v17:@make?$P"
V18FT="bot_research.experiments.lead.v19:@make?$P&fortress_guns=true&catch_up=true&foreign_target=\"econ20\""
P5="bot_research.experiments.lead.v24:@make?passive_until=5"
P5T="bot_research.experiments.lead.v24:@make?passive_until=5&poke_reactive=\"turret_only\""
bot_research/experiments/lead/run_pool.sh growers g9a "'$V17' '$V18FT' '$P5' '$P5T'" --keep-logs losses > bot_research/runs/lead/g9a.out 2>&1
echo "g9a done $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh f5t c9n "'$P5'" --keep-logs losses > bot_research/runs/lead/c9n.out 2>&1
echo "== queue_c9a15 done $(date -u +%FT%TZ)"
