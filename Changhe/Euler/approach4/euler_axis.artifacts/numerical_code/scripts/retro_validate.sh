#!/bin/bash
cd "$(dirname "$0")/.."
export OMP_NUM_THREADS=1
for d in runs/p1_* runs/crit1_* runs/s1pin1_*; do
  [ -f "$d/result.json" ] || continue; [ -f "$d/validation.json" ] && continue
  nice -n 19 "${PYTHON:-python3}" scripts/validate_candidate.py "$d" >> logs/retro_validate.log 2>&1
done
