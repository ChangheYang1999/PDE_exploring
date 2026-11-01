#!/bin/bash
cd .
while kill -0 1066905 2>/dev/null; do sleep 30; done
python3 -u code/kappa_scan_arb.py 67 199 5400 > logs/kappa_scan_arb.out 2>&1
