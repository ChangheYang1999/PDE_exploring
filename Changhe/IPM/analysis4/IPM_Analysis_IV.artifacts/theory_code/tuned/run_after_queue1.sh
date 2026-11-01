#!/bin/bash
while kill -0 590955 2>/dev/null; do sleep 20; done
PY=python3
OMP_NUM_THREADS=1 nice -n 19 $PY hh_tune.py 9 2 15 4 > hh_tune_Q9h2_sin15.out 2>&1
