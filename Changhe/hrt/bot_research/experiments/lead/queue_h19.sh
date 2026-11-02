#!/bin/bash
# Written 2026-10-31T22:45Z. hrt-w1 revised its final recommendation to frozen v48 at 22:39Z (notes/defense.md). Plays
# v48 against the same bots as v46 in queue_h17.sh: frr5 against the ten frr1 bots on the standard start, frr6 against
# the six frr2 bots on mirror:1:2 and asym:23:2. Both seats. Starts after queue_h17 (PID 1734913) exits.
# Descriptive only; best.py is not changed.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
L=bot_research/runs/lead
. bot_research/experiments/lead/rr_specs.sh
while kill -0 1734913 2>/dev/null; do sleep 10; done
echo "start frr5 $(date -u +%FT%TZ)"
taskset -c 20,21 nice -n 19 .venv/bin/python -B -m bot_research.harness.tournament --name frr5 \
  --candidates "$V48" --opponents "$BEST_V9E" "$BEST_V9F" "$AF2G" "$P5TNUBM" "$V41" "$V29" "$G1" "$GUARD00" "$TDEF" "$AS1C" \
  --jobs 1 --keep-logs all > $L/frr5.out 2>&1
echo "end frr5 exit $? $(date -u +%FT%TZ)"
echo "start frr6 $(date -u +%FT%TZ)"
taskset -c 20,21 nice -n 19 .venv/bin/python -B -m bot_research.harness.tournament --name frr6 \
  --candidates "$V48" --opponents "$BEST_V9E" "$BEST_V9F" "$V41" "$V29" "$G1" "$AS1C" --scenarios mirror:1:2 asym:23:2 \
  --jobs 1 --keep-logs all > $L/frr6.out 2>&1
echo "end frr6 exit $? $(date -u +%FT%TZ)"
echo "== queue_h19 done $(date -u +%FT%TZ)"
