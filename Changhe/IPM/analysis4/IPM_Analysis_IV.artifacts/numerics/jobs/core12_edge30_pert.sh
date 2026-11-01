#!/bin/bash
cd .
PY=python3
$PY -u code/logff.py --tag log23_edge30_float_pert --ring float --A 2 --B 3 --f1 coeffs:1.0000000001 --N 300 --ckpt-every 100 --edge 30 --stop-rel-rad 1e9 > logs/log23_edge30_float_pert.out 2>&1
