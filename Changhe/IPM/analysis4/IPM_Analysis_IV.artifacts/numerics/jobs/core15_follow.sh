#!/bin/bash
cd .
while kill -0 128833 2>/dev/null; do sleep 30; done
python3 -u code/logff.py --tag log_sin1_c2_p512 --ring arb --prec 512 --A 1 --B 2 --f1 sin1 --N 300 --ckpt-every 10 --resume
