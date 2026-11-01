#!/bin/bash
# Sensitivity diagnostic (verifier V364): continuation of the canonical 2/3 log series from the archived 329 state with every ball displaced to a
# random boundary point (mid +/- rad, seed 20261031), 512 bits, 2 workers on cores 11-12, to N 350. Starts when both tuned chains have ended and
# pauses c007_p2048 (pid 3465211; checkpoint at about order 450, resume later with run_recursion.py --resume).
cd .
PY=python3
while kill -0 1741202 2>/dev/null || kill -0 3921779 2>/dev/null; do sleep 30; done
kill 3465211 2>/dev/null; sleep 5
echo "$(date -u +%FT%TZ) chains ended; c007_p2048 paused (pid 3465211 killed, resume from ckpt/c007_p2048.pkl)" >> logs/launch_pert329.out
setsid nohup taskset -c 11,12 nice -n 19 $PY -u code/logff.py --tag log_sin1_c3_pert329 --ring arb --prec 512 --A 2 --B 3 --f1 sin1 --N 350 --ckpt-every 5 --resume --perturb-radii 20261031 --workers 2 --stop-rel-rad 1e9 > logs/log_sin1_c3_pert329.out 2>&1 &
echo "$(date -u +%FT%TZ) launched pert329 pid $!" >> logs/launch_pert329.out
