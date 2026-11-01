#!/bin/bash
cd .
while kill -0 2991382 2>/dev/null; do sleep 20; done
python3 -u code/run_recursion.py --tag shape2_sin1_a2_p512 --ring arb --prec 512 --cl cand007 --f1 "coeffs:1,2" --N 200 --ckpt-every 50
python3 -u code/run_recursion.py --tag shape2_sin1_am2_p512 --ring arb --prec 512 --cl cand007 --f1 "coeffs:1,-2" --N 200 --ckpt-every 50
python3 -u code/run_recursion.py --tag shape2_sin7_p512 --ring arb --prec 512 --cl cand007 --f1 "coeffs:0,0,0,1" --N 200 --ckpt-every 50
python3 -u code/run_recursion.py --tag shape2_sin1_a1_10_p512 --ring arb --prec 512 --cl cand007 --f1 "coeffs:1,1/10" --N 200 --ckpt-every 50
python3 -u code/run_recursion.py --tag shape2_sin1_am1_10_p512 --ring arb --prec 512 --cl cand007 --f1 "coeffs:1,-1/10" --N 200 --ckpt-every 50
python3 -u code/run_recursion.py --tag shape2_sin1_a1_20_p512 --ring arb --prec 512 --cl cand007 --f1 "coeffs:1,1/20" --N 200 --ckpt-every 50
python3 -u code/run_recursion.py --tag shape2_sin1_a3_10_p512 --ring arb --prec 512 --cl cand007 --f1 "coeffs:1,3/10" --N 200 --ckpt-every 50
python3 -u code/run_recursion.py --tag shape2_c007_signflip_p512 --ring arb --prec 512 --cl cand007 --f1 "coeffs:18.56782229755,-2.107321631475,0.6247347944873" --N 200 --ckpt-every 50
