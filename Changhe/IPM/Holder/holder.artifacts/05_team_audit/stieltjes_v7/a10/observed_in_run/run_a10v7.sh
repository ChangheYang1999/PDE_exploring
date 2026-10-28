#!/bin/bash
cd "$(dirname "$0")"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
taskset -c 62 nice -n 5 python3 run_queue7.py plans/a10v7.json >> run_a10v7.log 2>&1
echo EXIT $? >> run_a10v7.log
