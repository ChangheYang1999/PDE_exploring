#!/bin/bash
# Cycle-7 follow-up queue (written 07:27Z): waits for queue_c7d.sh, then rr1 = the newest recommended worker artifacts
# (hrt-w1's fortress v22, hrt-w2's econ17) against pool TARGETED and each other (pool LATEST), for the
# complementary-strengths table of the report (the lead settings against LATEST are run t6).
cd "$(dirname "$0")/../../.." || exit 1
while pgrep -f 'queue_c7[d]' >/dev/null; do sleep 60; done
W="'bot_research.bots.defense.frozen.v22.fortress:@make' 'bot_research.bots.economy.frozen.v17.econ17:@make?free_fallback=\"zero\"&foreign_attack_from=11'"
bot_research/experiments/lead/run_pool.sh targeted rr1 "$W" --keep-logs losses > bot_research/runs/lead/rr1.out 2>&1
bot_research/experiments/lead/run_pool.sh latest rr2 "$W" --keep-logs losses > bot_research/runs/lead/rr2.out 2>&1
echo "== queue done $(date -u +%FT%TZ)"
