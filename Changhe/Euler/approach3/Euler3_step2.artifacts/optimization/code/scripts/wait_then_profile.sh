#!/bin/bash
# wait for the smoke worker to exit, then run the profiling on GPU 5
cd "$(dirname "$0")/.."; PY=python3
while pgrep -f 'worker_d6.py runs/smk_scale' > /dev/null; do sleep 10; done
echo "$(date -u +%FT%TZ) smoke worker gone; profiling start"
CUDA_VISIBLE_DEVICES=5 OMP_NUM_THREADS=1 nice -n 10 $PY -u validation/profile_d6.py --start starts/S01_nest6_cl0.45_om1.0_p0.pt --out profiling/profile_S01.json --gpu_index 5 > profiling/profile_S01.log 2>&1
echo "$(date -u +%FT%TZ) profiling done exit $?"
