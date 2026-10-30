#!/bin/bash
# Run detached from this lane. Every Python stage uses one assigned CPU.
set -euo pipefail
cd RUN_ROOT/numerics_audit_N4
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
PY=python3
finish() {
  result=$?
  date -u '+%Y-%m-%dT%H:%M:%SZ' > logs/queue_006_005_end.txt
  echo "$result" > logs/queue_006_005_exit.txt
}
trap finish EXIT
date -u '+%Y-%m-%dT%H:%M:%SZ' > logs/queue_006_005_start.txt
"$PY" -B research/candidate_audits/code/audit.py C1-N1-006-8branch-e2 > logs/candidate006_audit.log 2>&1
"$PY" -B research/candidate_audits/code/points.py C1-N1-006-8branch-e2 3/7 1/4 > logs/candidate006_point.log 2>&1
"$PY" -B research/projected_residual/code/build.py C1-N1-006-8branch-e2 > logs/candidate006_projected.log 2>&1
"$PY" -B research/projected_residual/code/probe.py C1-N1-006-8branch-e2 > logs/candidate006_probe.log 2>&1
"$PY" -B research/whole_plane_norms/code/pipeline.py C1-N1-005-d2w-j7-x3 assemble --bits 2048 --packing tight > logs/candidate005_assemble_tight.log 2>&1
"$PY" -B research/whole_plane_norms/code/norm_ball.py C1-N1-005-d2w-j7-x3 G0 > logs/candidate005_G0.log 2>&1
"$PY" -B research/whole_plane_norms/code/norm_ball.py C1-N1-005-d2w-j7-x3 rF_proxy > logs/candidate005_rF.log 2>&1
"$PY" -B research/exact_negative_norm/code/negative_ball.py C1-N1-005-d2w-j7-x3 2048 > logs/candidate005_H.log 2>&1
"$PY" -B research/whole_plane_norms/code/norm_ball.py C1-N1-005-d2w-j7-x3 G1 > logs/candidate005_G1.log 2>&1
"$PY" -B research/whole_plane_norms/code/norm_ball.py C1-N1-005-d2w-j7-x3 P2 > logs/candidate005_P2.log 2>&1
"$PY" -B research/rounding_realization/code/check.py C1-N1-005-d2w-j7-x3 > logs/candidate005_rounding.log 2>&1
