#!/bin/bash
cd .
python3 -u code/run_recursion.py --tag nearres_eps1e-3_p512 --ring arb --prec 512 --cl 1000/599 --f1 sin1 --N 120 --ckpt-every 20
python3 -u code/run_recursion.py --tag nearres_eps1e-6_p512 --ring arb --prec 512 --cl 1000000/599999 --f1 sin1 --N 120 --ckpt-every 20
python3 -u code/run_recursion.py --tag nearres_eps1e-9_p512 --ring arb --prec 512 --cl 1000000000/599999999 --f1 sin1 --N 120 --ckpt-every 20
python3 -u code/run_recursion.py --tag nearres_eps0_cl5_3_p512 --ring arb --prec 512 --cl 5/3 --f1 sin1 --N 120 --ckpt-every 20
python3 -u code/run_recursion.py --tag sin1_c007_p2048 --ring arb --prec 2048 --cl cand007 --f1 sin1 --N 1000 --ckpt-every 25
