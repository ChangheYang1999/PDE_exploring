#!/bin/bash
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
P="${PYTHON:-python3}"
for f in state131_T1_exact n12_m4_exact n12_m5_exact n12_m7_exact; do
  nice -n 5 $P code/n12_norms.py data/$f.json -6.9 9.21 240 24 -2,-1,0,0.3 data/${f}_routeU.json > runs/routeU_$f.log 2>&1
done
echo "done $(date -u +%FT%TZ)" >> runs/routeU_norms.done
