#!/bin/bash
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
for R in 20 30 50 100 300; do nice -n 5 "${PYTHON:-python3}" code/farfield_F_sharp.py data/state088_exact.json 10 $R 1e9 0.02; done > runs/farfield_F_sharp_all.log 2>&1
