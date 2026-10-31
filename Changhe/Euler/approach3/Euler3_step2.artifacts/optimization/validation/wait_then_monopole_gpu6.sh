#!/bin/bash
# after g8_tables finishes on GPU 6: rerun the exterior-monopole regression (corrected anchor mask) and the cache regression
cd "$(dirname "$0")/.."; PY=python3
export CUDA_VISIBLE_DEVICES=6 OMP_NUM_THREADS=1
while pgrep -f 'validation/g8_tables' > /dev/null; do sleep 15; done
echo "$(date -u +%FT%TZ) exterior monopole regression start"; nice -n 10 $PY -u validation/exterior_monopole_regression.py > validation/logs/misc_exterior_monopole_regression.log 2>&1; echo "$(date -u +%FT%TZ) done exit $?"
echo "$(date -u +%FT%TZ) cache regression start"; nice -n 10 $PY -u validation/cache_regression.py > validation/logs/misc_cache_regression.log 2>&1; echo "$(date -u +%FT%TZ) done exit $?"
