#!/bin/bash
# Cycle-7 queue, v15 form (written 07:43Z; replaces queue_c7d.sh and queue_c7e.sh, stopped while t5 ran).
# v15 = v14 + immune_attack (current-rule attacks once our own S >= 1500). Seat-0 games: A15 + fortress_n=2/4 +
# immune_attack beat guarded tier4 r5 (+1038 / +1267; A13 + fortress_n: 0 / -35), guarded tier4 r8 (+1062 / +1092)
# and the round-2 bluff (+640).
# Waits for t5 (A14 + big_splash, + fortress_n=4 on TARGETED; started by queue_c7d.sh) and t6 (LATEST: frozen
# best_v9a, V2, V4; started by hand with one job), then with two jobs:
#   t7  TARGETED: V2 = A15 + fortress_n=2 + immune_attack, V4 = A15 + fortress_n=4 + immune_attack,
#       A15 + immune_attack (no fortress), VB = A15 + big_splash + immune_attack;
#   c8a FRONTIER5: V2, V4, VB;
#   s13, s14 forecaster screens (GRID=full, COUNTER=stateful) of V2 and V4;
#   rr1, rr2: fortress v22 and econ17 against TARGETED and LATEST (complementary-strengths table).
cd "$(dirname "$0")/../../.." || exit 1
while pgrep -f 'tournament --name t[56] ' >/dev/null; do sleep 30; done
rm -f bot_research/experiments/lead/JOBS1
A15='bot_research.experiments.lead.v15:@make?big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"'
V2="$A15&fortress_n=2&immune_attack=true"
V4="$A15&fortress_n=4&immune_attack=true"
VB="$A15&big_splash=true&immune_attack=true"
bot_research/experiments/lead/run_pool.sh targeted t7 "'$V2' '$V4' '$A15&immune_attack=true' '$VB'" --keep-logs losses > bot_research/runs/lead/t7.out 2>&1
bot_research/experiments/lead/run_pool.sh frontier5 c8a "'$V2' '$V4' '$VB'" --keep-logs losses > bot_research/runs/lead/c8a.out 2>&1
P='"big_threat":100,"attack_mode":"adaptive","gun_cap":120,"poke_until":3,"poke_reactive":"turret","big_partial":true,"r1_poke":3,"immune_attack":true'
MODEL=v15 GRID=full COUNTER=stateful bot_research/experiments/lead/run_screens.sh s13 "{$P,\"fortress_n\":2}" > bot_research/runs/lead/s13.out 2>&1
MODEL=v15 GRID=full COUNTER=stateful bot_research/experiments/lead/run_screens.sh s14 "{$P,\"fortress_n\":4}" > bot_research/runs/lead/s14.out 2>&1
W="'bot_research.bots.defense.frozen.v22.fortress:@make' 'bot_research.bots.economy.frozen.v17.econ17:@make?free_fallback=\"zero\"&foreign_attack_from=11'"
bot_research/experiments/lead/run_pool.sh targeted rr1 "$W" --keep-logs losses > bot_research/runs/lead/rr1.out 2>&1
bot_research/experiments/lead/run_pool.sh latest rr2 "$W" --keep-logs losses > bot_research/runs/lead/rr2.out 2>&1
echo "== queue done $(date -u +%FT%TZ)"
