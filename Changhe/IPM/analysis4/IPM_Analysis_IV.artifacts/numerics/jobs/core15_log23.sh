#!/bin/bash
cd .
while kill -0 3185671 2>/dev/null; do sleep 20; done
python3 -u code/logff.py --tag log_sin1_c3_p512b --ring arb --prec 512 --A 2 --B 3 --f1 sin1 --N 300 --ckpt-every 10
python3 -u code/logff.py --tag log_sin1_c2_p512b --ring arb --prec 512 --A 1 --B 2 --f1 sin1 --N 300 --ckpt-every 10
