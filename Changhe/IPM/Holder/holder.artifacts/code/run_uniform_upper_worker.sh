#!/bin/bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
worker="$1"
for start in $(seq "$((128 + 32 * worker))" 64 383); do
  stop="$((start + 32))"
  output="09_uniform_comparison/lead_certificate/verification/recomputed/upper_r${start}_${stop}"
  if test -s "${output}.json"; then continue; fi
  date -u
  timeout 540 python3 code/reproduce_uniform_upper_chunks.py --start "$start" --stop "$stop" > "${output}.log" 2>&1
  date -u
done
