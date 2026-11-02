#!/bin/bash
# Usage (from anywhere): run_tourn.sh NAME OPPFILE "SCENARIOS" CAND_SPEC [CAND_SPEC...]
# Runs the lead's tournament on cores 25-27 at low priority, output in runs/economy/NAME.
set -e
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"  # project root (this file is bot_research/experiments/economy/)
cd "$ROOT"
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$ROOT/bot_research/tmp" OMP_NUM_THREADS=1
NAME=$1; OPPF=$2; SCEN=$3; shift 3
mapfile -t OPPS < <(grep -v '^#' "$OPPF" | grep -v '^$')
SCARGS=()
if [ -n "$SCEN" ]; then SCARGS=(--scenarios $SCEN); fi
exec taskset -c 25-27 nice -n 19 .venv/bin/python -B -m bot_research.harness.tournament \
  --name "$NAME" --out-dir "bot_research/runs/economy/$NAME" --candidates "$@" \
  --opponents "${OPPS[@]}" "${SCARGS[@]}" --jobs "${JOBS:-3}" --keep-logs "${KEEP:-losses}"
