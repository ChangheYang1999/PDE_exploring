#!/bin/bash
# Cycle-9 queue c9b31 (written 2026-10-31T15:10Z; one computation slot). The queues c9a24/c9a25/c9b30 were stopped (their running
# tournaments g9c and tm2 kept running) because tm2 shows the passive window losing to tier1 strikes in rounds 3-4
# (P4TNUB -30/-50, V18FT draws) and g9c shows P4TNUB losing growers (-660). New candidates: v30 with passive_mid_from
# 2 (M2) and 3 (M3), i.e. tier1-tier3 insurance in all or most passive rounds. Waits for tm2, then tm3.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
PAR="poke_reactive=\"turret_only\"&fail_limit=2&passive_turret=false&robust_k=null&behind_mode=\"current\""
M2="bot_research.experiments.lead.v30:@make?passive_until=5&$PAR&passive_mid_from=2"
M3="bot_research.experiments.lead.v30:@make?passive_until=5&$PAR&passive_mid_from=3"
while kill -0 688358 2>/dev/null; do sleep 10; done
echo "tm2 done (seen by queue_c9b31) $(date -u +%FT%TZ)"
bot_research/experiments/lead/run_pool.sh timing2 tm3 "'$M2' '$M3'" --keep-logs losses > bot_research/runs/lead/tm3.out 2>&1
echo "== queue_c9b31 done $(date -u +%FT%TZ)"
