#!/bin/bash
cd .
while kill -0 2886911 2>/dev/null; do sleep 30; done
python3 -u code/evaluate_series.py ckpt/sqrt5_sin1_p1024.pkl --N 10,20,40,80,160,320 --R 0.25,0.5,1,2,4 --out notes/eval_sqrt5_sin1_p1024.json > logs/eval_sqrt5_sin1_p1024.out 2>&1
