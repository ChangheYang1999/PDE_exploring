#!/bin/bash
cd .
PY=python3
$PY -u code/logff.py --tag log23_edge60_float --ring float --A 2 --B 3 --f1 sin1 --N 400 --ckpt-every 100 --edge 60 --stop-rel-rad 1e9 > logs/log23_edge60_float.out 2>&1
