#!/bin/bash
cd .
PY=python3
$PY -u code/tuned_c3.py --tag tuned_b1_p1024 --root 1 --prec 1024 --N 400 --ckpt-every 30 > logs/tuned_b1_p1024.out 2>&1
$PY -u code/tuned_c3.py --tag tuned_b2_p1024 --root 2 --prec 1024 --N 300 --ckpt-every 30 > logs/tuned_b2_p1024.out 2>&1
