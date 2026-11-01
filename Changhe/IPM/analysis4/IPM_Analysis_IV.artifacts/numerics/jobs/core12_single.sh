#!/bin/bash
# Lead request 18:03Z: single-harmonic tuned series in ball arithmetic (unit amplitude), sequential on core 12.
cd "$(dirname "$0")/.."
PY=python3
taskset -c 12 nice -n 19 $PY -u code/tuned_general.py --tag single_sin7_45_p1024 --a 4 --b 5 --f1-single 7 --prec 1024 --N 300 --ckpt-every 30 > logs/single_sin7_45_p1024.out 2>&1
taskset -c 12 nice -n 19 $PY -u code/tuned_general.py --tag single_sin9_47_p1024 --a 4 --b 7 --f1-single 9 --prec 1024 --N 300 --ckpt-every 30 > logs/single_sin9_47_p1024.out 2>&1
