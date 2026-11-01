#!/bin/bash
cd .
while kill -0 2886915 2>/dev/null; do sleep 30; done
python3 -u code/prime_congruence_check.py 61 sin1 > logs/prime_congruence_sin1.out 2>&1
python3 -u code/prime_congruence_check.py 29 cand007 > logs/prime_congruence_cand007.out 2>&1
