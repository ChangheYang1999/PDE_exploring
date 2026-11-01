#!/bin/bash
# waits for the 1/2 canonical log run (pid given as $1) to exit, then runs the sin11 at 4/9 single-harmonic tuned series on core 11
cd "$(dirname "$0")/.."
while kill -0 "$1" 2>/dev/null; do sleep 60; done
taskset -c 11 nice -n 19 python3 -u code/tuned_general.py --tag single_sin11_49_p1024 --a 4 --b 9 --f1-single 11 --prec 1024 --N 300 --ckpt-every 30 > logs/single_sin11_49_p1024.out 2>&1
