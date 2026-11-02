#!/bin/bash
# Cycle-6 queue, part 5 (06:59Z), after t2 (started by an earlier queue). A = C2 with attack_mode "adaptive".
# t2 so far: A 12-4-6 on TARGETED, destroyed by the round-2 gun bluff; lead guard from round 4 rejected
# (-835 to -895 against the bluffs). New options in v12 (defaults = v11):
#   t3  TARGETED: A + open_attack_from=2, A + open_attack_from=3, A + poke_reactive "relevant", A + poke_reactive true;
#   s10 forecaster screen of A (GRID=full, COUNTER=public);
#   c6e FRONTIER5: the four t3 variants.
cd "$(dirname "$0")/../../.." || exit 1
while pgrep -f 'tournament --name t[2] ' >/dev/null; do sleep 30; done
A='bot_research.experiments.lead.v12:@make?big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"'
T='poke_reactive="turret"'
VARS="'$A&$T&open_attack_from=2' '$A&$T&open_attack_from=3' '$A&poke_reactive=\"relevant\"' '$A&poke_reactive=true'"
bot_research/experiments/lead/run_pool.sh targeted t3 "$VARS" --keep-logs losses > bot_research/runs/lead/t3.out 2>&1
MODEL=v10 GRID=full COUNTER=public bot_research/experiments/lead/run_screens.sh s10 \
    '{"big_threat":100,"attack_mode":"adaptive","gun_cap":120,"poke_until":3,"poke_reactive":"turret","big_partial":true,"r1_poke":3}'
bot_research/experiments/lead/run_pool.sh frontier5 c6e "$VARS" --keep-logs losses > bot_research/runs/lead/c6e.out 2>&1
echo "== queue done $(date -u +%FT%TZ)"
