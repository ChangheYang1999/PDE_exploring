#!/bin/bash
cd .
python3 -u code/resonance_scan.py sin1 60 > logs/resonance_scan_sin1.out 2>&1
python3 -u code/resonance_scan.py cand007 17 > logs/resonance_scan_cand007.out 2>&1
python3 -u code/run_recursion.py --tag sin1_c007_p2048 --ring arb --prec 2048 --cl cand007 --f1 sin1 --N 1000 --ckpt-every 25 --resume
