#!/bin/bash
# Remainder of the Theorem 3.5 family at alpha=0 with the group-0 plans (about one minute, single-threaded).
# The alpha=1/200 rows are recomputed in the same runs and compared with the stored node certificates.
cd "$(dirname "$0")/.."
export OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
python3 code/refl_nodes_a0.py --cells 384 --alphas 0,1/200 --out data/refl_a0.json > results/refl_a0.log 2>&1
python3 code/far_nodes_a0.py --angles 512 --radial 128 --alphas 0,1/200 --ref 1/20 --out data/far_a0.json > results/far_a0.log 2>&1
python3 code/combine_alpha0.py
