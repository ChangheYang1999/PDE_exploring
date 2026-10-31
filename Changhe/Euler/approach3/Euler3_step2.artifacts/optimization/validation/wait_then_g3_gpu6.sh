#!/bin/bash
# after the profiling on GPU 5 has finished (clean timings), run the G3 add-on and the far-noise split on GPU 6
cd "$(dirname "$0")/.."; PY=python3
while pgrep -f 'validation/profile_d6' > /dev/null; do sleep 15; done
echo "$(date -u +%FT%TZ) profiling finished; G3 add-on start on GPU 6"
CUDA_VISIBLE_DEVICES=6 OMP_NUM_THREADS=1 nice -n 10 $PY -u validation/g3_addon.py --tag A --cases S01_own,S05_own,manu_small_omega,manu_large_omega > validation/logs/g3_addon_A.log 2>&1
echo "$(date -u +%FT%TZ) G3 add-on done exit $?; far noise split start"
CUDA_VISIBLE_DEVICES=6 OMP_NUM_THREADS=1 nice -n 10 $PY -u validation/far_noise_split.py --tag A --cases S01_own,manu_a > validation/logs/far_noise_split_A.log 2>&1
echo "$(date -u +%FT%TZ) far noise split done exit $?"
