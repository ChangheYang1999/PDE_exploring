#!/bin/bash
# Usage: run_pool.sh POOL NAME "CANDIDATE SPECS..." [extra tournament args]
# POOL is tuning, strong, all, frontier, frontier2, frontier3, frontier4, frontier5, scen, targeted, latest or everything
# (experiments/lead/pools.py). Cores 20,21, nice 19, 2 jobs (1 if the file experiments/lead/JOBS1 exists, which leaves
# one of the lane's two computation slots for development games).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
POOL=$1; shift
NAME=$1; shift
CANDS=$1; shift
eval "OPP=($(.venv/bin/python -B -m bot_research.experiments.lead.pools "$POOL"))"
eval "CAND=($CANDS)"
exec taskset -c 20,21 nice -n 19 .venv/bin/python -B -m bot_research.harness.tournament --name "$NAME" \
    --candidates "${CAND[@]}" --opponents "${OPP[@]}" --jobs "$([ -e bot_research/experiments/lead/JOBS1 ] && echo 1 || echo 2)" "$@"
