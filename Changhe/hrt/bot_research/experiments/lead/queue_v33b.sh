#!/bin/bash
# Gating of v33 (written 2026-10-31T16:37Z; one computation slot; chain b of 2). Quick seat-0 games (runs/lead/qg_v33.out):
# passive_cheap_from=3 with cap 60 draws the four tier1/tier2 round-3/4 strikes P5TNUBM loses, wins fortress v32 +5,
# economy.timing +15 and all five growers; it still loses budget_timing tier3 r4 (-26). Cap 30 plays as P5TNUBM.
# Gate (stated 14:49Z): no new loss against V18FT on f5t, PUNISH, BLUFFCOV, TARGETED2 and TARGETED3; the broad pools
# follow. Waits for the PID given as $1 (the previous job in this slot) to exit.
cd "$(dirname "$0")/../../.." || exit 1
while [ -n "$1" ] && kill -0 "$1" 2>/dev/null; do sleep 20; done
PAR="poke_reactive=\"turret_only\"&fail_limit=2&passive_turret=false&robust_k=null&behind_mode=\"current\""
V33="bot_research.experiments.lead.v33:@make?passive_until=5&$PAR&passive_mid_from=5&passive_cheap_from=3&passive_cheap_cap=60"
for job in "timing2 x33tm2" "targeted2 x33t2" "punish x33pu" "guarded_maze x33gm" "screened x33sg" "handoff x33hd"; do
  set -- $job
  echo "start $2 ($1) $(date -u +%FT%TZ)"
  bot_research/experiments/lead/run_pool.sh $1 $2 "'$V33'" --keep-logs losses > bot_research/runs/lead/$2.out 2>&1
  echo "end $2 exit $? $(date -u +%FT%TZ)"
done
echo "== queue_v33b done $(date -u +%FT%TZ)"
