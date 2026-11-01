#!/bin/bash
cd .
python3 -u code/run_recursion.py --tag sqrt5_sin1_p1024 --ring arb --prec 1024 --cl sqrt5 --f1 sin1 --N 700 --ckpt-every 25
python3 -u code/run_recursion.py --tag sqrt5_sin1p3_p1024 --ring arb --prec 1024 --cl sqrt5 --f1 "coeffs:1,1/2" --N 400 --ckpt-every 25
python3 -u code/run_recursion.py --tag sqrt5_sin1m3_p1024 --ring arb --prec 1024 --cl sqrt5 --f1 "coeffs:1,-1/2" --N 400 --ckpt-every 25
python3 -u code/run_recursion.py --tag sqrt5_c007f1_p1024 --ring arb --prec 1024 --cl sqrt5 --f1 cand007 --N 300 --ckpt-every 25
