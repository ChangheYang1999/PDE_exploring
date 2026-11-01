#!/bin/bash
cd .
python3 -u code/logff.py --tag log_sin1_c9_5_p512 --ring arb --prec 512 --A 4 --B 9 --f1 sin1 --N 300 --ckpt-every 10
python3 -u code/logff.py --tag log_sin1_c2_p512 --ring arb --prec 512 --A 1 --B 2 --f1 sin1 --N 200 --ckpt-every 10
python3 -u code/logff.py --tag log_sin1_c5_3_p512 --ring arb --prec 512 --A 2 --B 5 --f1 sin1 --N 200 --ckpt-every 10
python3 -u code/logff.py --tag log_c007f1_c9_5_p512 --ring arb --prec 512 --A 4 --B 9 --f1 cand007 --N 70 --ckpt-every 5
python3 -u code/logff.py --tag log_sin1_c20_11_p512 --ring arb --prec 512 --A 9 --B 20 --f1 sin1 --N 200 --ckpt-every 10
python3 -u code/logff.py --tag log_sin1_c3_p512 --ring arb --prec 512 --A 2 --B 3 --f1 sin1 --N 200 --ckpt-every 10
