#!/bin/bash
# Usage: run_tourney.sh NAME "CANDIDATE SPECS..." [extra tournament args]
# Runs candidates against the lead TUNING pool on cores 20,21 at low priority.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
NAME=$1; shift
CANDS=$1; shift
eval "OPP=($(.venv/bin/python -B -m bot_research.experiments.lead.pools))"
eval "CAND=($CANDS)"
exec taskset -c 20,21 nice -n 19 .venv/bin/python -B -m bot_research.harness.tournament --name "$NAME" \
    --candidates "${CAND[@]}" --opponents "${OPP[@]}" --jobs 2 "$@"
