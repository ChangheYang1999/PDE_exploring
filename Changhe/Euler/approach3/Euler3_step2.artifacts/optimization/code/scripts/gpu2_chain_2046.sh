#!/bin/bash
# GPU 2 slot after the third smoke run (20:4xZ): smoke comparison (CPU, ~3 min, counted by the busy guard), then the P2 v10 admission pair (record_63a v10 start + --full end, wrapper).
cd RUN_ROOT/numerics/degree6_free_parameters_48h; PY=python3
bash validation/l_launch.sh cmd "cd RUN_ROOT/numerics/degree6_free_parameters_48h && CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=4 MKL_NUM_THREADS=4 nice -n 10 taskset -c 31-34 $PY validation/s2_smoke_compare.py > validation/logs/s2_smoke_compare.out 2>&1"
echo "$(date -u +%FT%TZ) smoke comparison done (exit $?)"
bash scripts/v10_pair_chain.sh 2 P2
