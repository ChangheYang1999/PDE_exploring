#!/bin/bash
# Cycle-9 queue c9a27 (written 2026-10-31T15:26Z; one computation slot). M2 (v30, passive_mid_from=2: tier1-tier3 insurance by
# rule 3a in every passive round) keeps GROWERS 142-0-0 (g9d), so it gets the gating pools now. Waits for the v31
# quick games (qg_v31.sh, PID 1177279), then c9p f5t, t8i TARGETED2, pu2 PUNISH, b9c BLUFFCOV, t9j TARGETED3_P5TF,
# gm4 GUARDED_MAZE, tm4 TIMING.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
PAR="poke_reactive=\"turret_only\"&fail_limit=2&passive_turret=false&robust_k=null&behind_mode=\"current\""
M2="bot_research.experiments.lead.v30:@make?passive_until=5&$PAR&passive_mid_from=2"
while kill -0 1177279 2>/dev/null; do sleep 10; done
echo "qg_v31 done (seen by queue_c9a27) $(date -u +%FT%TZ)"
for job in "f5t c9p" "targeted2 t8i" "punish pu2" "bluffcov b9c" "targeted3_p5tf t9j" "guarded_maze gm4" "timing tm4"; do
  set -- $job
  echo "start $2 ($1) $(date -u +%FT%TZ)"
  bot_research/experiments/lead/run_pool.sh $1 $2 "'$M2'" --keep-logs losses > bot_research/runs/lead/$2.out 2>&1
  echo "end $2 exit $? $(date -u +%FT%TZ)"
done
echo "== queue_c9a27 done $(date -u +%FT%TZ)"
