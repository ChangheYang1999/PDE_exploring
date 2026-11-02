#!/bin/bash
# Cycle-7 queue, third form (written 07:24Z). queue_c7b.sh was stopped after it had started t4 (TARGETED: A13 +
# splash_insurance, + fortress_n=4, + fortress_n=2), which keeps running; its c7a, s10 and s11 are rescheduled here.
# v14 = v13 plus big_splash (splash-only plans in the big-threat branch only).
#   t5  TARGETED: A14 + big_splash, A14 + big_splash + fortress_n=4;
#   c7a FRONTIER5: A13 + fortress_n=4, A14 + big_splash;
#   s10, s11, s12 forecaster screens (GRID=full, COUNTER=stateful) of A (v10), A13 + fortress_n=4, A14 + big_splash.
cd "$(dirname "$0")/../../.." || exit 1
while pgrep -f 'tournament --name t[4] ' >/dev/null; do sleep 30; done
A13='bot_research.experiments.lead.v13:@make?big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"'
A14='bot_research.experiments.lead.v14:@make?big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"'
bot_research/experiments/lead/run_pool.sh targeted t5 "'$A14&big_splash=true' '$A14&big_splash=true&fortress_n=4'" --keep-logs losses > bot_research/runs/lead/t5.out 2>&1
bot_research/experiments/lead/run_pool.sh frontier5 c7a "'$A13&fortress_n=4' '$A14&big_splash=true'" --keep-logs losses > bot_research/runs/lead/c7a.out 2>&1
P='"big_threat":100,"attack_mode":"adaptive","gun_cap":120,"poke_until":3,"poke_reactive":"turret","big_partial":true,"r1_poke":3'
MODEL=v10 GRID=full COUNTER=stateful bot_research/experiments/lead/run_screens.sh s10 "{$P}" > bot_research/runs/lead/s10.out 2>&1
MODEL=v13 GRID=full COUNTER=stateful bot_research/experiments/lead/run_screens.sh s11 "{$P,\"fortress_n\":4}" > bot_research/runs/lead/s11.out 2>&1
MODEL=v14 GRID=full COUNTER=stateful bot_research/experiments/lead/run_screens.sh s12 "{$P,\"big_splash\":true}" > bot_research/runs/lead/s12.out 2>&1
echo "== queue done $(date -u +%FT%TZ)"
