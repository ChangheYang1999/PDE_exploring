#!/bin/bash
# Lead request 18:03Z, second part of the chain: wait for the sin7 at 4/5 run (pid $1), evaluate its section-13 residuals, then run sin9 at 4/7 and evaluate it too.
cd "$(dirname "$0")/.."
PY=python3
while kill -0 "$1" 2>/dev/null; do sleep 20; done
taskset -c 12 nice -n 19 $PY -u code/evaluate_series.py ckpt/single_sin7_45_p1024.pkl --N 10,20,40,80 --R 0.125,0.25,0.5,1,2,4 --out notes/eval_single_sin7_45.json > logs/eval_single_sin7_45.out 2>&1
taskset -c 12 nice -n 19 $PY -u code/tuned_general.py --tag single_sin9_47_p1024 --a 4 --b 7 --f1-single 9 --prec 1024 --N 300 --ckpt-every 30 > logs/single_sin9_47_p1024.out 2>&1
taskset -c 12 nice -n 19 $PY -u code/evaluate_series.py ckpt/single_sin9_47_p1024.pkl --N 10,20,40,80 --R 0.0625,0.125,0.25,0.5,1,2,4,8 --out notes/eval_single_sin9_47.json > logs/eval_single_sin9_47.out 2>&1
