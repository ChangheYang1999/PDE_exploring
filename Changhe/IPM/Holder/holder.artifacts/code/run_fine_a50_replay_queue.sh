#!/bin/bash
set -u
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
out=05_team_audit/note14_certificate/replay_fine_a50
for attempt in $(seq 1 10); do
  date -u '+ATTEMPT %Y-%m-%dT%H:%M:%SZ'
  timeout 540 env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B -u code/replay_note14_refined_sequential.py --alpha 1/2 --b 3/4 --c=-3/20 --lam 1000/1021 --delta .005 --rho-min 1e-8 --rho-m .01 --rho-max 1e8 --depth 3 --prec 80 --out "$out"
  status=$?
  date -u "+RETURN $status %Y-%m-%dT%H:%M:%SZ"
  if [ "$status" -eq 0 ]; then exit 0; fi
  if [ "$status" -ne 124 ]; then exit "$status"; fi
done
exit 124
