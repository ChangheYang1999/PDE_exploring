#!/bin/bash
# Lead request 18:03Z, third single-harmonic run moved to core 12 (free after sin9): sin11 at 4/9, then its section-13 evaluation.
cd "$(dirname "$0")/.."
PY=python3
taskset -c 12 nice -n 19 $PY -u code/tuned_general.py --tag single_sin11_49_p1024 --a 4 --b 9 --f1-single 11 --prec 1024 --N 300 --ckpt-every 30 > logs/single_sin11_49_p1024.out 2>&1
taskset -c 12 nice -n 19 $PY -u code/evaluate_series.py ckpt/single_sin11_49_p1024.pkl --N 10,20,40,80 --R 1,2,4,8,16,32,64,128 --out notes/eval_single_sin11_49.json > logs/eval_single_sin11_49.out 2>&1
