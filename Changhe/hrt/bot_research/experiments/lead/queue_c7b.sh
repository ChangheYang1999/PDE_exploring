#!/bin/bash
# Cycle-7 queue, second form (07:14Z; queue_c7.sh stopped before starting any job), after t3 (started by queue_c6e.sh, whose remaining steps s10 and c6e were dropped:
# t3 showed open_attack_from 2/3 losing to all four bluffs). v13 = v12 plus splash-only insurance options.
# Quick seat-0 games: A + splash_insurance, A + fortress_n=4, A + fortress_n=2 beat all four bluffs
# (+560 to +640 against turret_round=2, where A loses -1065).
#   t4  TARGETED: the three v13 variants;
#   c7a FRONTIER5: the three v13 variants;
#   s10 forecaster screen of A (v10), s11 the same for A + fortress_n=4 (v13); GRID=full, COUNTER=stateful
#   (hrt-w3 07:06Z: the public counter is not exact against the stateful adaptive attack).
cd "$(dirname "$0")/../../.." || exit 1
while pgrep -f 'tournament --name t[3] ' >/dev/null; do sleep 30; done
A='bot_research.experiments.lead.v13:@make?big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"'
VARS="'$A&splash_insurance=true' '$A&fortress_n=4' '$A&fortress_n=2'"
bot_research/experiments/lead/run_pool.sh targeted t4 "$VARS" --keep-logs losses > bot_research/runs/lead/t4.out 2>&1
bot_research/experiments/lead/run_pool.sh frontier5 c7a "$VARS" --keep-logs losses > bot_research/runs/lead/c7a.out 2>&1
MODEL=v10 GRID=full COUNTER=stateful bot_research/experiments/lead/run_screens.sh s10 \
    '{"big_threat":100,"attack_mode":"adaptive","gun_cap":120,"poke_until":3,"poke_reactive":"turret","big_partial":true,"r1_poke":3}'
MODEL=v13 GRID=full COUNTER=stateful bot_research/experiments/lead/run_screens.sh s11 \
    '{"big_threat":100,"attack_mode":"adaptive","gun_cap":120,"poke_until":3,"poke_reactive":"turret","big_partial":true,"r1_poke":3,"fortress_n":4}'
echo "== queue done $(date -u +%FT%TZ)"
