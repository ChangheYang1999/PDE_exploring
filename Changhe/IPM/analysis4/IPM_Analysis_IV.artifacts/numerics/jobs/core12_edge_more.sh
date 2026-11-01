#!/bin/bash
cd .
PY=python3
while kill -0 2585385 2>/dev/null; do sleep 20; done
$PY -u code/logff.py --tag log23_edge10_float --ring float --A 2 --B 3 --f1 sin1 --N 300 --ckpt-every 50 --edge 10 --stop-rel-rad 1e9 > logs/log23_edge10_float.out 2>&1
$PY -u code/logff.py --tag log23_edge30_float --ring float --A 2 --B 3 --f1 sin1 --N 300 --ckpt-every 50 --edge 30 --stop-rel-rad 1e9 > logs/log23_edge30_float.out 2>&1
