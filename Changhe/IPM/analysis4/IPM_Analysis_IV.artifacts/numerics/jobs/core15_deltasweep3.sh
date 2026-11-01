#!/bin/bash
cd .
while kill -0 2971550 2>/dev/null; do sleep 20; done
for CL in 18001/10000 18201/10000 17501/10000 19001/10000 20001/10000; do
  T=$(echo $CL | tr '/' '_')
  python3 -u code/run_recursion.py --tag dsw3_sin1_cl${T}_p512 --ring arb --prec 512 --cl $CL --f1 sin1 --N 300 --ckpt-every 50
done
