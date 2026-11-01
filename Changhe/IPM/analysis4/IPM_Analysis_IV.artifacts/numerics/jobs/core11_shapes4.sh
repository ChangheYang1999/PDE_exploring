#!/bin/bash
cd .
while kill -0 3185672 2>/dev/null; do sleep 20; done
# three-mode family sin + a sin3 + b sin5 around 007's ratios (a = 0.113, b = 0.034), unit leading amplitude
for A in 2/25 11/100 7/50; do for B in -3/100 0 3/100 3/50; do
  TA=$(echo $A | tr '/' '_'); TB=$(echo $B | tr '/' '_' | tr '-' 'm')
  python3 -u code/run_recursion.py --tag shape4_a${TA}_b${TB}_p512 --ring arb --prec 512 --cl cand007 --f1 "coeffs:1,$A,$B" --N 200 --ckpt-every 50
done; done
