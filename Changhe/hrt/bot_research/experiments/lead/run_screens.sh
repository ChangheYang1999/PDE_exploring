#!/bin/bash
# Usage: run_screens.sh PREFIX 'JSON1' 'JSON2' ...  (sequential screen_known runs PREFIX-k0, PREFIX-k1, ...)
# Cores 20,21, nice 19, 2 jobs per screen. Set MODEL (default v5), GRID (default small) and COUNTER
# (known, public, mixed or schedule; default known) in the environment.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
PREFIX=$1; shift
i=0
for params in "$@"; do
    echo "== $PREFIX-k$i $params $(date -u +%FT%TZ)"
    taskset -c 20,21 nice -n 19 .venv/bin/python -B -m bot_research.experiments.lead.screen_known \
        "$PREFIX-k$i" "$params" --model "${MODEL:-v5}" --grid "${GRID:-small}" --counter "${COUNTER:-known}"
    i=$((i + 1))
done
echo "== done $(date -u +%FT%TZ)"
