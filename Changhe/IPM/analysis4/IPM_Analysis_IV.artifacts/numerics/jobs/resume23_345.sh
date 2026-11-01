#!/bin/bash
cd .
PY=python3
$PY -u code/logff.py --tag log_sin1_c3_p512 --ring arb --prec 512 --A 2 --B 3 --f1 sin1 --N 350 --ckpt-every 5 --resume --workers 4 --stop-rel-rad 1e9 > logs/log_sin1_c3_p512_resume345.out 2>&1
