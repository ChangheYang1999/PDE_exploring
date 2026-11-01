#!/bin/bash
cd .
while kill -0 2898221 2>/dev/null; do sleep 30; done
for CL in 10/7 20/13 5/3 20/11 1.9 2 20/9 5/2 10/3 20/7; do
  T=$(echo $CL | tr '/' '_' | tr '.' 'p')
  python3 -u code/run_recursion.py --tag dsweep_sin1_cl${T}_p512 --ring arb --prec 512 --cl $CL --f1 sin1 --N 300 --ckpt-every 50
done
