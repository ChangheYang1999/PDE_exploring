#!/bin/bash
cd .
while pgrep -f "tag pert007_" > /dev/null; do sleep 30; done
for K in 2 3 5 9; do
  python3 -u code/run_recursion.py --tag shear_K${K}_c007_p512 --ring arb --prec 512 --cl cand007 --f1 json:notes/shear_family_K${K}.json --N 200 --ckpt-every 50
done
