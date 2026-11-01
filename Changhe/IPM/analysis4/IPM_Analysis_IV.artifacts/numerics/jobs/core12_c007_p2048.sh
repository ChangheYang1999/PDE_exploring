#!/bin/bash
cd .
while kill -0 2960468 2>/dev/null; do sleep 20; done
python3 -u code/run_recursion.py --tag c007_p2048 --ring arb --prec 2048 --cl cand007 --f1 cand007 --N 500 --ckpt-every 10
