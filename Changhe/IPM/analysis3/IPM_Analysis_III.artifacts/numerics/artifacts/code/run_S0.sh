#!/bin/bash
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
cd numerics/artifacts/code
date -u
python3 -u run_section.py S0_M4_s60_o12 exact 4 60 12 30 2 256
date -u; echo DONE
