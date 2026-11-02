#!/bin/bash
# Cycle-9 queue c9a28 (written 2026-10-31T15:34Z; one computation slot). M2 is out (f5t c9p: loses economy.timing -37 in both seats,
# which V18FT does not lose), M2 + passive_ladder (v32) is out (quick games: economy.timing -37, two growers lost by
# more than 1000), so P5TNUBM (v30, passive_mid_from=5) is the remaining revision candidate. Gating and broad pools
# for P5TNUBM: c9q f5t, pu2 PUNISH, b9c BLUFFCOV, t9j TARGETED3_P5TF.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
PAR="poke_reactive=\"turret_only\"&fail_limit=2&passive_turret=false&robust_k=null&behind_mode=\"current\""
P5TNUBM="bot_research.experiments.lead.v30:@make?passive_until=5&$PAR&passive_mid_from=5"
for job in "f5t c9q" "punish pu2" "bluffcov b9c" "targeted3_p5tf t9j"; do
  set -- $job
  echo "start $2 ($1) $(date -u +%FT%TZ)"
  bot_research/experiments/lead/run_pool.sh $1 $2 "'$P5TNUBM'" --keep-logs losses > bot_research/runs/lead/$2.out 2>&1
  echo "end $2 exit $? $(date -u +%FT%TZ)"
done
echo "== queue_c9a28 done $(date -u +%FT%TZ)"
