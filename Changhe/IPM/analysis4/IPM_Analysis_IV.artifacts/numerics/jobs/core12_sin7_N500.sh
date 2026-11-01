#!/bin/bash
# Stability of the sin7 at 4/5 growth law beyond 300: fresh run to N 500 (the program has no resume), then its evaluation.
cd "$(dirname "$0")/.."
taskset -c 12 nice -n 19 python3 -u code/tuned_general.py --tag single_sin7_45_p1024_N500 --a 4 --b 5 --f1-single 7 --prec 1024 --N 500 --ckpt-every 50 > logs/single_sin7_45_p1024_N500.out 2>&1
