#!/bin/bash
# waits for the sin13/sin11 hh_tune queue (PID 590955); then the modular first-compatibility scans, the delta=4/7
# two-mode certificate, and hh_tune sin15 (one busy computation at a time)
while kill -0 590955 2>/dev/null; do sleep 30; done
PY=python3
cd ../modscan
OMP_NUM_THREADS=1 nice -n 19 $PY mod_scan.py cand007 120 2/5 1/2 scan_cand007_Q120.jsonl > scan_cand007_Q120.out 2>&1
OMP_NUM_THREADS=1 nice -n 19 $PY mod_scan.py sin1 120 0 1 scan_sin1_Q120.jsonl > scan_sin1_Q120.out 2>&1
cd ../tuned
OMP_NUM_THREADS=1 nice -n 19 $PY tq_certh.py 7 2 > tq_certh_Q7h2.log 2>&1
OMP_NUM_THREADS=1 nice -n 19 $PY hh_tune.py 9 2 15 4 > hh_tune_Q9h2_sin15.out 2>&1
