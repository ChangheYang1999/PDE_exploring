#!/bin/bash
set -euo pipefail
cd RUN_ROOT/numerics_audit_N4
TASK_PY=python3
"$TASK_PY" -B research/projected_residual/code/probe.py Mpen2 > logs/Mpen2_projected_probe.log 2>&1
for TASK_ID in C1-N1-002-7branch-frf C1-N1-003-8branch-frf C1-N1-004-4branch-l2fw; do
    "$TASK_PY" -B research/projected_residual/code/build.py "$TASK_ID" > "logs/${TASK_ID}_projected_build.log" 2>&1
    "$TASK_PY" -B research/projected_residual/code/probe.py "$TASK_ID" > "logs/${TASK_ID}_projected_probe.log" 2>&1
done
