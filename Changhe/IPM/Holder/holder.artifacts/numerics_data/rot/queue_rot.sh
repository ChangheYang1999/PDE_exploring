#!/bin/bash
# waits for the n14_a34_c30_ff parent (pid 3111510) to exit, then runs the rotated-family float scan (single process)
cd ..
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
PY=python3
while kill -0 3111510 2>/dev/null; do sleep 15; done
echo "start $(date -u +%FT%TZ)" >> runs/rot/queue.log
nice -n 10 $PY -u code/rotated_float.py 0.5 0.75 -0.15 1000/1021 0 0 > runs/rot/test_phi0.log 2>&1
nice -n 10 $PY -u code/rotated_float.py 0.5 0.75 -0.15 1000/1021 0,0.3,0.6,0.9 m3 > runs/rot/scan_m3.log 2>&1
nice -n 10 $PY -u code/rotated_float.py 0.5 0.75 -0.15 1000/1021 0.3,0.6,0.9 p3 > runs/rot/scan_p3.log 2>&1
nice -n 10 $PY -u code/rotated_float.py 0.5 0.75 -0.15 1000/1021 0.3,0.6,0.9 0 > runs/rot/scan_d0.log 2>&1
echo "end $(date -u +%FT%TZ)" >> runs/rot/queue.log
