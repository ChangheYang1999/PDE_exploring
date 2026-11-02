#!/bin/bash
# Usage: strong.sh NAME "CANDIDATE SPECS..." [extra tournament args]
# Candidates against the lead "strong" pool (frozen lead versions and worker/counter bots).
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
NAME=$1; shift
CANDS=$1; shift
eval "CAND=($CANDS)"
OPP=(bot_research.experiments.lead.frozen.best_v1:@make
     'bot_research.experiments.lead.frozen.best_v1:@make?kappa=8'
     bot_research.experiments.lead.frozen.best_v2:@make
     bot_research.bots.economy.econ:@make
     bot_research.bots.counters.posterior_response:@make
     bot_research.bots.counters.switching:@make
     bot_research.bots.counters.maze_pressure:@make
     'bot_research.bots.counters.forecast_lock:@make?opening_units=2&reserve=180&saturate_round=20')
exec taskset -c 20,21 nice -n 19 .venv/bin/python -B -m bot_research.harness.tournament --name "$NAME" \
    --candidates "${CAND[@]}" --opponents "${OPP[@]}" --jobs 2 "$@"
