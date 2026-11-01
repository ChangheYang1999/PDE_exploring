#!/bin/bash
cd .
PY=python3
$PY -u code/logff.py --tag log23_edge30_p256 --ring arb --prec 256 --A 2 --B 3 --f1 sin1 --N 320 --ckpt-every 20 --edge 30 --stop-rel-rad 1e9 > logs/log23_edge30_p256.out 2>&1
