#!/bin/bash
cd .
PY=python3
while kill -0 894864 2>/dev/null; do sleep 20; done
$PY -u code/tuned_cQ.py --tag tunedQ4_r6_p1024 --Q 4 --root-guess 0.626787499078 --prec 1024 --N 300 --ckpt-every 30 > logs/tunedQ4_r6_p1024.out 2>&1
$PY -u code/tuned_cQ.py --tag tunedQ4_r5_p1024 --Q 4 --root-guess 0.351504417845 --prec 1024 --N 300 --ckpt-every 30 > logs/tunedQ4_r5_p1024.out 2>&1
$PY -u code/tuned_cQ.py --tag tunedQ4_r4_p1024 --Q 4 --root-guess 0.187763074126 --prec 1024 --N 300 --ckpt-every 30 > logs/tunedQ4_r4_p1024.out 2>&1
$PY -u code/tuned_cQ.py --tag tunedQ4_r1_p1024 --Q 4 --root-guess -0.279638830219 --prec 1024 --N 300 --ckpt-every 30 > logs/tunedQ4_r1_p1024.out 2>&1
$PY -u code/tuned_cQ.py --tag tunedQ4_r3_p1024 --Q 4 --root-guess 0.077146738755 --prec 1024 --N 300 --ckpt-every 30 > logs/tunedQ4_r3_p1024.out 2>&1
$PY -u code/tuned_cQ.py --tag tunedQ4_r2_p1024 --Q 4 --root-guess 0.039935695190 --prec 1024 --N 300 --ckpt-every 30 > logs/tunedQ4_r2_p1024.out 2>&1
