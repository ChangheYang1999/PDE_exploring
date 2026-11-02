#!/bin/bash
# Written 2026-10-31T23:20Z. hrt-w2's af5 (V29 + attack_from=5) is the candidate of its 18.22 rule (notes/economy.md 18.26, 18.29);
# its run afrr plays af5 against the ten frr1 bots on the standard start only. frr7 plays af5 against the six frr2
# bots and v48 on mirror:1:2 and asym:23:2 (28 games); frr8 plays af5 against v48 on the standard start (2 games).
# Both seats. Uses the slot that frr5 freed at 23:18:15Z, next to queue_h20.sh (frr6). Descriptive only; best.py is
# not changed.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
L=bot_research/runs/lead
. bot_research/experiments/lead/rr_specs.sh
echo "start frr7 $(date -u +%FT%TZ)"
taskset -c 20,21 nice -n 19 .venv/bin/python -B -m bot_research.harness.tournament --name frr7 \
  --candidates "$AF5" --opponents "$BEST_V9E" "$BEST_V9F" "$V41" "$V29" "$G1" "$AS1C" "$V48" --scenarios mirror:1:2 asym:23:2 \
  --jobs 1 --keep-logs all > $L/frr7.out 2>&1
echo "end frr7 exit $? $(date -u +%FT%TZ)"
echo "start frr8 $(date -u +%FT%TZ)"
taskset -c 20,21 nice -n 19 .venv/bin/python -B -m bot_research.harness.tournament --name frr8 \
  --candidates "$AF5" --opponents "$V48" --jobs 1 --keep-logs all > $L/frr8.out 2>&1
echo "end frr8 exit $? $(date -u +%FT%TZ)"
echo "== queue_h21 done $(date -u +%FT%TZ)"
