#!/bin/bash
cd .
for A in -2 -1 -1/2 -1/5 1/5 1/2 1 2; do
  T=$(echo $A | tr '/' '_' | tr '-' 'm')
  python3 -u code/run_recursion.py --tag shape_sin1_a${T}_p512 --ring arb --prec 512 --cl cand007 --f1 "coeffs:1,$A" --N 200 --ckpt-every 50
done
python3 -u code/run_recursion.py --tag shape_sin3_p512 --ring arb --prec 512 --cl cand007 --f1 "coeffs:0,1" --N 200 --ckpt-every 50
python3 -u code/run_recursion.py --tag shape_sin5_p512 --ring arb --prec 512 --cl cand007 --f1 "coeffs:0,0,1" --N 200 --ckpt-every 50
for K in 2 3 5; do
  python3 -u code/run_recursion.py --tag shape_c007trunc${K}_p512 --ring arb --prec 512 --cl cand007 --f1 json:notes/c007_f1_trunc${K}.json --N 200 --ckpt-every 50
done
