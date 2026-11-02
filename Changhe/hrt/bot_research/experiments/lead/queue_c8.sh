#!/bin/bash
# Cycle-8 queue (written 08:13Z; replaces queue_c7f.sh, stopped while t7 ran). Waits for t7, then:
#   chk  v16 (V4 + foreign_policy=econ17) against econ17 on mirror:1:2, both seats (one process, error check);
#   sc1  scenario robustness on SCEN + econ17 ("scenx") under mirror:1:2, asym:3:2, mirror:22:3, asym:23:2 for
#        v16, V4 and best_v9a (on the standard start v16 plays exactly as V4: the switch needs a building
#        the bot never asked for);
#   c8a  FRONTIER5: V4 = A15 + fortress_n=4 + immune_attack, VB = A15 + big_splash + immune_attack (V2 dropped: t6);
#   s14  stateful forecaster screen of V4 (MODEL=v15 GRID=full COUNTER=stateful);
#   rr1, rr2: fortress v22 and econ17 against TARGETED and LATEST (complementary-strengths table).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
while pgrep -f 'tournament --name t[7] ' >/dev/null; do sleep 30; done
A15='bot_research.experiments.lead.v15:@make?big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"'
V4="$A15&fortress_n=4&immune_attack=true"
VB="$A15&big_splash=true&immune_attack=true"
V16='bot_research.experiments.lead.v16:@make?big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"'
BEST='bot_research.bots.best:decide'
E17='bot_research.bots.economy.frozen.v17.econ17:@make?free_fallback="zero"&foreign_attack_from=11'
PYTHONPATH=. taskset -c 20,21 nice -n 19 .venv/bin/python -B bot_research/tmp/qscen.py bot_research/tmp/qs/chk "$V16" "$E17" mirror:1:2 > bot_research/tmp/qs_v16chk.out 2>&1
bot_research/experiments/lead/run_pool.sh scenx sc1 "'$V16' '$V4' '$BEST'" --scenarios mirror:1:2 asym:3:2 mirror:22:3 asym:23:2 --keep-logs losses > bot_research/runs/lead/sc1.out 2>&1
bot_research/experiments/lead/run_pool.sh frontier5 c8a "'$V4' '$VB'" --keep-logs losses > bot_research/runs/lead/c8a.out 2>&1
P='"big_threat":100,"attack_mode":"adaptive","gun_cap":120,"poke_until":3,"poke_reactive":"turret","big_partial":true,"r1_poke":3,"immune_attack":true'
MODEL=v15 GRID=full COUNTER=stateful bot_research/experiments/lead/run_screens.sh s14 "{$P,\"fortress_n\":4}" > bot_research/runs/lead/s14.out 2>&1
W="'bot_research.bots.defense.frozen.v22.fortress:@make' '$E17'"
bot_research/experiments/lead/run_pool.sh targeted rr1 "$W" --keep-logs losses > bot_research/runs/lead/rr1.out 2>&1
bot_research/experiments/lead/run_pool.sh latest rr2 "$W" --keep-logs losses > bot_research/runs/lead/rr2.out 2>&1
echo "== queue done $(date -u +%FT%TZ)"
