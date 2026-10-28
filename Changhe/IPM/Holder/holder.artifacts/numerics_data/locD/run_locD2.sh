#!/bin/bash
cd ../numerics_data/locD
export OMP_NUM_THREADS=1
PY=python3
nice -n 10 $PY -u ../../code/locD_lp.py 0.75 0,0.53996 64 1.5 1e-8 > locD_a075.log 2>&1
nice -n 10 $PY -u ../../code/locD_lp.py 0.3 0,0.53996 64 1.5 1e-8 > locD_a03.log 2>&1
echo "done $(date -u +%FT%TZ)" > locD2.done
