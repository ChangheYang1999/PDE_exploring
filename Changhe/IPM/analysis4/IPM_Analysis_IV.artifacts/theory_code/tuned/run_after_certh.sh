#!/bin/bash
# queued after tq_certh.py 10 3 (one busy computation at a time)
while kill -0 524872 2>/dev/null; do sleep 20; done
PY=python3
OMP_NUM_THREADS=1 nice -n 19 $PY hh_tune.py 9 2 13 3 > hh_tune_Q9h2_sin13.out 2>&1
OMP_NUM_THREADS=1 nice -n 19 $PY hh_tune.py 9 2 11 3 > hh_tune_Q9h2_sin11.out 2>&1
