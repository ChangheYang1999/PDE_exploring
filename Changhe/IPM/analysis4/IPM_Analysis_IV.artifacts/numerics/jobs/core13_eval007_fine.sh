#!/bin/bash
cd .
while kill -0 3293743 2>/dev/null; do sleep 30; done
python3 -u code/evaluate_series.py ckpt/c007_arb512.pkl --N 50,100 --R 14,16,18,20,22,24,26,28 --out notes/eval_c007_fineR.json > logs/eval_c007_fineR.out 2>&1
