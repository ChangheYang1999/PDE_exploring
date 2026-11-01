#!/bin/bash
cd .
for CL in 9/5 361/200 363/200 91/50; do
  T=$(echo $CL | tr '/' '_')
  python3 -u code/run_recursion.py --tag sin1_cl${T}_p1024 --ring arb --prec 1024 --cl $CL --f1 sin1 --N 500 --ckpt-every 25
done
for CL in 9/5 361/200 363/200 91/50; do
  T=$(echo $CL | tr '/' '_')
  python3 -u code/run_recursion.py --tag c007f1_cl${T}_p1024 --ring arb --prec 1024 --cl $CL --f1 cand007 --N 250 --ckpt-every 25
done
