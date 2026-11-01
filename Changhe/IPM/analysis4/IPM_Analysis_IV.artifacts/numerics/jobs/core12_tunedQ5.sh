#!/bin/bash
cd .
PY=python3
while kill -0 1144903 2>/dev/null; do sleep 20; done
$PY -u code/tuned_cQ.py --tag tunedQ5_r6_p1024 --Q 5 --root-guess 0.559981053471976903 --prec 1024 --N 300 --ckpt-every 30 > logs/tunedQ5_r6_p1024.out 2>&1
$PY -u code/tuned_cQ.py --tag tunedQ5_r5_p1024 --Q 5 --root-guess 0.315276594987968648 --prec 1024 --N 300 --ckpt-every 30 > logs/tunedQ5_r5_p1024.out 2>&1
$PY -u code/tuned_cQ.py --tag tunedQ5_r4_p1024 --Q 5 --root-guess 0.212092130879632768 --prec 1024 --N 300 --ckpt-every 30 > logs/tunedQ5_r4_p1024.out 2>&1
$PY -u code/tuned_cQ.py --tag tunedQ5_r3_p1024 --Q 5 --root-guess 0.125333778821311281 --prec 1024 --N 300 --ckpt-every 30 > logs/tunedQ5_r3_p1024.out 2>&1
$PY -u code/tuned_cQ.py --tag tunedQ5_r2_p1024 --Q 5 --root-guess 0.048998666175014319 --prec 1024 --N 300 --ckpt-every 30 > logs/tunedQ5_r2_p1024.out 2>&1
$PY -u code/tuned_cQ.py --tag tunedQ5_r1_p1024 --Q 5 --root-guess -0.48975799134877350 --prec 1024 --N 300 --ckpt-every 30 > logs/tunedQ5_r1_p1024.out 2>&1
