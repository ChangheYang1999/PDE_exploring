#!/bin/bash
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
P="${PYTHON:-python3}"
FT=data/state131_formal_tail.json
for R in 16 64 128; do OMP_NUM_THREADS=1 nice -n 5 $P code/splice2.py data/n12_m10_exact.json $FT $R 300 160 32 > runs/splice2_m10_R$R.log 2>&1; done
echo "chain done $(date -u +%FT%TZ)" >> runs/splice2_chain.done
