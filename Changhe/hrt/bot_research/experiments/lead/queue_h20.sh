#!/bin/bash
# Written 2026-10-31T23:15Z. Runs frr6 (v48 against the six frr2 bots on mirror:1:2 and asym:23:2, both seats) now, in the slot
# that queue_h18.sh freed at 23:11:28Z, next to frr5. The bash of queue_h19.sh was stopped before it reached frr6
# (its frr5 tournament process keeps running and writing frr5.out). Same command as in queue_h19.sh.
# Descriptive only; best.py is not changed.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
L=bot_research/runs/lead
. bot_research/experiments/lead/rr_specs.sh
echo "start frr6 $(date -u +%FT%TZ)"
taskset -c 20,21 nice -n 19 .venv/bin/python -B -m bot_research.harness.tournament --name frr6 \
  --candidates "$V48" --opponents "$BEST_V9E" "$BEST_V9F" "$V41" "$V29" "$G1" "$AS1C" --scenarios mirror:1:2 asym:23:2 \
  --jobs 1 --keep-logs all > $L/frr6.out 2>&1
echo "end frr6 exit $? $(date -u +%FT%TZ)"
echo "== queue_h20 done $(date -u +%FT%TZ)"
