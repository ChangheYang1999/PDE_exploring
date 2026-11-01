#!/bin/bash
cd .
while kill -0 3265064 2>/dev/null; do sleep 20; done
# Candidate 007 profile with its sin3 (index 1) or sin5 (index 2) coefficient rescaled: perturbations of its Fourier coefficients
for S in 1/2 3/4 5/4 3/2; do
  T=$(echo $S | tr '/' '_')
  python3 -u code/run_recursion.py --tag pert007_a1x${T}_p512 --ring arb --prec 512 --cl cand007 --f1 json:notes/c007_pert_a1x${T}.json --N 200 --ckpt-every 50
done
for S in 1/2 3/2; do
  T=$(echo $S | tr '/' '_')
  python3 -u code/run_recursion.py --tag pert007_a2x${T}_p512 --ring arb --prec 512 --cl cand007 --f1 json:notes/c007_pert_a2x${T}.json --N 200 --ckpt-every 50
done
