#!/bin/bash
# Written 2026-10-31T21:49Z. Adds hrt-w1's final recommendation v46 (from 21:45Z) to the final round robins frr1 and
# frr2, which hold v41: frr3 plays v46 against the ten frr1 finalists on the standard start, frr4 against the
# six frr2 finalists on mirror:1:2 and asym:23:2. Both seats. Starts after queue_h16 B (PID 1589710) exits.
# Descriptive only; best.py is not changed.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
L=bot_research/runs/lead
. bot_research/experiments/lead/rr_specs.sh
while kill -0 1589710 2>/dev/null; do sleep 10; done
echo "start frr3 $(date -u +%FT%TZ)"
taskset -c 20,21 nice -n 19 .venv/bin/python -B -m bot_research.harness.tournament --name frr3 \
  --candidates "$V46" --opponents "$BEST_V9E" "$BEST_V9F" "$AF2G" "$P5TNUBM" "$V41" "$V29" "$G1" "$GUARD00" "$TDEF" "$AS1C" \
  --jobs 1 --keep-logs all > $L/frr3.out 2>&1
echo "end frr3 exit $? $(date -u +%FT%TZ)"
echo "start frr4 $(date -u +%FT%TZ)"
taskset -c 20,21 nice -n 19 .venv/bin/python -B -m bot_research.harness.tournament --name frr4 \
  --candidates "$V46" --opponents "$BEST_V9E" "$BEST_V9F" "$V41" "$V29" "$G1" "$AS1C" --scenarios mirror:1:2 asym:23:2 \
  --jobs 1 --keep-logs all > $L/frr4.out 2>&1
echo "end frr4 exit $? $(date -u +%FT%TZ)"
echo "== queue_h17 done $(date -u +%FT%TZ)"
