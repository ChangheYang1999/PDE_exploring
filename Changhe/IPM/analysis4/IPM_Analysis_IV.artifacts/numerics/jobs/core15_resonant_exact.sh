#!/bin/bash
cd .
python3 -u code/run_recursion.py --tag res_sin1_cl5_3_exact --ring fmpq --cl 5/3 --f1 sin1 --N 32 --ckpt-every 4
python3 -u code/run_recursion.py --tag res_sin1_cl9_5_exact --ring fmpq --cl 9/5 --f1 sin1 --N 30 --ckpt-every 4
python3 -u code/run_recursion.py --tag res_sin1_cl20_11_exact --ring fmpq --cl 20/11 --f1 sin1 --N 45 --ckpt-every 4
python3 -u code/run_recursion.py --tag res_sin1p3_cl5_3_exact --ring fmpq --cl 5/3 --f1 "coeffs:1,1/2" --N 22 --ckpt-every 4
python3 -u code/run_recursion.py --tag res_c007f1_cl5_3_exact --ring fmpq --cl 5/3 --f1 cand007 --N 16 --ckpt-every 2
python3 -u code/run_recursion.py --tag res_c007f1_cl9_5_exact --ring fmpq --cl 9/5 --f1 cand007 --N 19 --ckpt-every 2
