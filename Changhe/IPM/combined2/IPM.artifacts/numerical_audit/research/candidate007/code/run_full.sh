#!/bin/sh
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
exec taskset -c 50 nice -n 19 python3 research/candidate007/code/full_residual.py --bits 2048
