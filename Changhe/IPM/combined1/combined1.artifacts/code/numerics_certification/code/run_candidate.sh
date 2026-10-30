#!/bin/bash
# Usage: run_candidate.sh <source.json> <ID> <core> [kmax]
# Chains: e2norms (components) -> hminus1 (Hdot^-1 enclosure) -> audit_e2norms (second path). Low priority, one core.
set -u
SRC=$1; ID=$2; CORE=$3; KMAX=${4:-30}
LANE=RUN_ROOT/numerics_N3
PY=python3
export PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
cd $LANE
OUT=certification/results
taskset -c $CORE nice -n 10 $PY -B certification/e2norms.py $SRC $ID $OUT > logs/${ID}_e2norms.out 2>&1 || { echo "e2norms failed" >> logs/${ID}_e2norms.out; exit 1; }
taskset -c $CORE nice -n 10 $PY -B certification/hminus1.py $ID $SRC $OUT $KMAX 20 61 > logs/${ID}_hminus1.out 2>&1
taskset -c $CORE nice -n 10 $PY -B certification/audit_e2norms.py $ID $OUT $SRC > logs/${ID}_audit.out 2>&1
echo "CHAIN DONE $(date -u +%FT%TZ)" >> logs/${ID}_chain.out
