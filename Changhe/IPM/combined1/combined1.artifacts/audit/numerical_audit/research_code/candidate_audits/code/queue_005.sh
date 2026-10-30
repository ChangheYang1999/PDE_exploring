#!/bin/bash
set -euo pipefail
cd RUN_ROOT/numerics_audit_N4
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
PY=python3
"$PY" -B research/candidate_audits/code/audit.py C1-N1-005-d2w-j7-x3 > logs/candidate005_audit.log 2>&1
"$PY" -B research/candidate_audits/code/points.py C1-N1-005-d2w-j7-x3 0 1/4 > logs/candidate005_point.log 2>&1
"$PY" -B research/projected_residual/code/build.py C1-N1-005-d2w-j7-x3 > logs/candidate005_projected.log 2>&1
"$PY" -B research/projected_residual/code/probe.py C1-N1-005-d2w-j7-x3 > logs/candidate005_probe.log 2>&1
