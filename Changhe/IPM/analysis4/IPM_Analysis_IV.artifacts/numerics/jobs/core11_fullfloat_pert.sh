#!/bin/bash
cd .
PY=python3
$PY -u code/logff.py --tag log23_full_float_pert --ring float --A 2 --B 3 --f1 coeffs:1.0000000001 --N 400 --ckpt-every 50 --stop-rel-rad 1e9 > logs/log23_full_float_pert.out 2>&1
