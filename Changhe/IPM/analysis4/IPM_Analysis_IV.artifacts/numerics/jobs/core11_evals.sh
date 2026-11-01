#!/bin/bash
cd .
PY=python3
$PY -u code/evaluate_series.py ckpt/tuned49_r5_p1024.pkl --N 10,20,40,80 --R 32,64,128,256,512,1024 --out notes/eval_tuned49_r5.json > logs/eval_tuned49_r5.out 2>&1
$PY -u code/evaluate_series.py ckpt/tuned13_r6_p1024.pkl --N 10,20,40,80 --R 16,32,64,128,256,512 --out notes/eval_tuned13_r6.json > logs/eval_tuned13_r6.out 2>&1
$PY -u code/evaluate_series.py ckpt/tuned13_r1_p1024.pkl --N 10,20,40,80 --R 64,128,256,512,1024,2048 --out notes/eval_tuned13_r1.json > logs/eval_tuned13_r1.out 2>&1
