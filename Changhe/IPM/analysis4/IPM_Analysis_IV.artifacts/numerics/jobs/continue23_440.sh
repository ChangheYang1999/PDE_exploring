#!/bin/bash
# continue the 2/3 midpoint continuation (relative to the certified 329 midpoints, V364 scope) from 400 to 440 on cores 13-16 (about 9 min/order: 440 about 00:30Z)
cd .
PY=python3
$PY -u code/logff.py --tag log_sin1_c3_from329 --ring arb --prec 512 --A 2 --B 3 --f1 sin1 --N 440 --ckpt-every 5 --resume --workers 4 --stop-rel-rad 1e9 >> logs/log_sin1_c3_from329.out 2>&1
