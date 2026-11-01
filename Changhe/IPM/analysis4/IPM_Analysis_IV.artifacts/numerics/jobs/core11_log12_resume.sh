#!/bin/bash
cd .
PY=python3
$PY -u code/logff.py --tag log_sin1_c2_p512 --ring arb --prec 512 --A 1 --B 2 --f1 sin1 --N 300 --ckpt-every 10 --resume > logs/log_sin1_c2_p512_resume2.out 2>&1
