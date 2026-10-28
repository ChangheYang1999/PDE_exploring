#!/bin/bash
# pauses one worker of n14_a34_c30_ff (pid 3111533) while the single-process rotated-family float scan runs, then resumes it
cd ..
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
PY=python3
W=3111533
kill -STOP $W 2>/dev/null; echo "start $(date -u +%FT%TZ) (worker $W paused)" >> runs/rot/queue.log
nice -n 10 $PY -u code/rotated_float.py 0.5 0.75 -0.15 1000/1021 0 0 > runs/rot/test_phi0.log 2>&1
nice -n 10 $PY -u code/rotated_float.py 0.5 0.75 -0.15 1000/1021 0.3,0.6,0.9 m3 > runs/rot/scan_m3.log 2>&1
nice -n 10 $PY -u code/rotated_float.py 0.5 0.75 -0.15 1000/1021 0.3,0.6,0.9 p3 > runs/rot/scan_p3.log 2>&1
nice -n 10 $PY -u code/rotated_float.py 0.5 0.75 -0.15 1000/1021 0.3,0.6,0.9 0 > runs/rot/scan_d0.log 2>&1
kill -CONT $W 2>/dev/null; echo "end $(date -u +%FT%TZ) (worker $W resumed)" >> runs/rot/queue.log
