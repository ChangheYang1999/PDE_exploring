#!/bin/bash
set -u
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
for attempt in $(seq 1 10); do
  date -u '+ATTEMPT %Y-%m-%dT%H:%M:%SZ'
  timeout 540 env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B -u code/replay_middle_balanced_residuals.py
  status=$?
  date -u "+RETURN $status %Y-%m-%dT%H:%M:%SZ"
  if [ "$status" -eq 0 ]; then exit 0; fi
  if [ "$status" -ne 124 ]; then exit "$status"; fi
done
exit 124
