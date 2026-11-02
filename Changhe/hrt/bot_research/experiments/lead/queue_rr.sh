#!/bin/bash
# Final round robins of the team's finalists (descriptive; no selection depends on them; bots/best.py is final since
# 18:44:53Z). Usage: queue_rr.sh A|B.
# A (after queue_g3b): 9 finalists, standard start, every pair, both seats (72 games): frr1.
# B (after queue_tm): 5 finalists, scripted starts mirror:1:2 and asym:23:2 (hrt-w1's x182/x201 starts), both seats (40 games): frr2.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
L=bot_research/runs/lead
. bot_research/experiments/lead/rr_specs.sh
if [ "$1" = A ]; then
  until grep -q "^== queue_g3b done" $L/queue_g3b.log; do sleep 30; done
  echo "start frr1 $(date -u +%FT%TZ)"
  taskset -c 20,21 nice -n 19 .venv/bin/python -B -m bot_research.harness.tournament --name frr1 \
    --round-robin "$BEST_V9E" "$BEST_V9F" "$AF2G" "$P5TNUBM" "$V41" "$V29" "$G1" "$GUARD00" "$TDEF" \
    --jobs 1 --keep-logs all > $L/frr1.out 2>&1
  echo "end frr1 exit $? $(date -u +%FT%TZ)"
elif [ "$1" = B ]; then
  until grep -q "^== queue_tm done" $L/queue_tm.log; do sleep 30; done
  echo "start frr2 $(date -u +%FT%TZ)"
  taskset -c 20,21 nice -n 19 .venv/bin/python -B -m bot_research.harness.tournament --name frr2 \
    --round-robin "$BEST_V9E" "$BEST_V9F" "$V41" "$V29" "$G1" --scenarios mirror:1:2 asym:23:2 \
    --jobs 1 --keep-logs all > $L/frr2.out 2>&1
  echo "end frr2 exit $? $(date -u +%FT%TZ)"
fi
echo "== queue_rr $1 done $(date -u +%FT%TZ)"
