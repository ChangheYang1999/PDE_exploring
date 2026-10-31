#!/bin/bash
# wait for the D1 v2b chain to finish, then the LM cost comparison on GPU 5
cd RUN_ROOT/numerics/degree6_free_parameters_48h
while pgrep -f "run_d1_v2b_chain.sh" > /dev/null; do sleep 20; done
PY=python3
export CUDA_VISIBLE_DEVICES=5 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
echo "$(date -u +%FT%TZ) lm_cost_compare start" >> validation/logs/wait_cost.log
nice -n 10 taskset -c 31-34 $PY -u validation/lm_cost_compare.py > validation/logs/lm_cost_compare.log 2>&1
echo "$(date -u +%FT%TZ) lm_cost_compare done" >> validation/logs/wait_cost.log
