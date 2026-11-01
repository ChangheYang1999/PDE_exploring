#!/bin/bash
cd .
while kill -0 3062148 2>/dev/null; do sleep 20; done
for A in 3/50 2/25 1/10 3/25 7/50 4/25 9/50; do
  T=$(echo $A | tr '/' '_')
  python3 -u code/run_recursion.py --tag shape3_sin1_a${T}_p512 --ring arb --prec 512 --cl cand007 --f1 "coeffs:1,$A" --N 320 --ckpt-every 40
done
