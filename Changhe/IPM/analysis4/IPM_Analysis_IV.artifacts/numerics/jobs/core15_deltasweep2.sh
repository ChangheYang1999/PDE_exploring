#!/bin/bash
cd .
while kill -0 2898455 2>/dev/null; do sleep 20; done
# irrational-like delta = d + 1e-4 as rationals with denominator 10000 (first resonance at n >= 10000)
for D in 3001 3501 4001 4501 5001 5501 6001 6501 7001 2501 2001 1501; do
  python3 -u code/run_recursion.py --tag dsw2_sin1_d${D}_p512 --ring arb --prec 512 --cl 10000/$((10000-D)) --f1 sin1 --N 300 --ckpt-every 50
done
