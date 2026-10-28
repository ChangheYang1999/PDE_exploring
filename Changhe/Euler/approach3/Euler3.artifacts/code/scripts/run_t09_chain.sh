#!/bin/bash
# T09 holdout aliasing on the three gate states (GPU given as $1)
ROOT=$(cd "$(dirname "$0")/.." && pwd); cd $ROOT
export CUDA_VISIBLE_DEVICES=${1:-5} OMP_NUM_THREADS=1
for s in d6t_L8_cl0.45_om+0.3_fixed:start_000.pt d6w3_L6_cl0.45_om+0.3_fixed:start_000.pt nest2_L2_cl0.45_om+0.3:start_034.pt; do
  j=${s%%:*}; st=${s##*:}; echo "=== $j $(date -u +%FT%TZ)"
  timeout 1800 .venv/bin/python scripts/t09_aliasing.py runs/$j/starts/$st --device cuda:0 --json reports/T09_holdout_aliasing_$j.json
done
echo "=== done $(date -u +%FT%TZ)"
