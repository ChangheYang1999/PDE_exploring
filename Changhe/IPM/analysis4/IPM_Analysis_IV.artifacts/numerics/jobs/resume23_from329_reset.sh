#!/bin/bash
cd .
PY=python3
# the live log of this tag starts from the verifier-archived 329 checkpoint (identical bytes to my 09:29Z state), radii reset at 329
$PY -u code/logff.py --tag log_sin1_c3_from329 --ring arb --prec 512 --A 2 --B 3 --f1 sin1 --N 350 --ckpt-every 5 --resume --reset-radii --workers 4 --stop-rel-rad 1e9 > logs/log_sin1_c3_from329.out 2>&1
