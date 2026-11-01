#!/bin/bash
cd .
while kill -0 3039394 2>/dev/null; do sleep 20; done
# quasi-irrational delta = d + 0.01234567 (exact rationals with denominator 10^8; first resonance n >= 10^8)
for D in 31234567 36234567 41234567 46234567 51234567 56234567 61234567 66234567 71234567 26234567; do
  python3 -u code/run_recursion.py --tag dsw4_sin1_d${D}_p512 --ring arb --prec 512 --cl 100000000/$((100000000-D)) --f1 sin1 --N 300 --ckpt-every 50
done
