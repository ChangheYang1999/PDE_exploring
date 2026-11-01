#!/bin/bash
cd .
while kill -0 1048599 2>/dev/null; do sleep 30; done
python3 -u code/run_recursion.py --tag sin1_c007_p2048 --ring arb --prec 2048 --cl cand007 --f1 sin1 --N 1000 --ckpt-every 25 --resume
