#!/bin/bash
cd .
PY=python3
while kill -0 3528858 2>/dev/null; do sleep 20; done
$PY -u code/logff.py --tag log23_full_float --ring float --A 2 --B 3 --f1 sin1 --N 400 --ckpt-every 50 --stop-rel-rad 1e9 > logs/log23_full_float.out 2>&1
