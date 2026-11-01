#!/bin/bash
cd .
python3 -u code/logff.py --tag log_sin1_c3_p512 --ring arb --prec 512 --A 2 --B 3 --f1 sin1 --N 240 --ckpt-every 10 --resume
python3 -u code/logff.py --tag log_sin1_c2_p512 --ring arb --prec 512 --A 1 --B 2 --f1 sin1 --N 300 --ckpt-every 10 --resume
