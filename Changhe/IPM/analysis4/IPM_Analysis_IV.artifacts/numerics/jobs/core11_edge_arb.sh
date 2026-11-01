#!/bin/bash
cd .
PY=python3
$PY -u code/logff.py --tag log23_edge1_p1024 --ring arb --prec 1024 --A 2 --B 3 --f1 sin1 --N 300 --ckpt-every 50 --edge 1 --stop-rel-rad 1e9 > logs/log23_edge1_p1024.out 2>&1
$PY -u code/logff.py --tag log23_edge3_p1024 --ring arb --prec 1024 --A 2 --B 3 --f1 sin1 --N 300 --ckpt-every 50 --edge 3 --stop-rel-rad 1e9 > logs/log23_edge3_p1024.out 2>&1
