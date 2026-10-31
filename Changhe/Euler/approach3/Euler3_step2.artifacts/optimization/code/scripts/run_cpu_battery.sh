#!/bin/bash
# D6FP CPU battery after the GPU revocation (2026-10-29T00:57:59Z): gates.py on the given cases, one process, N torch threads.
# Usage: [CORES=33] [SNAPSHOT=0] scripts/run_cpu_battery.sh <tag> <cases,comma,separated> <threads> [quick]
#   CORES: taskset core list (default 31-34); SNAPSHOT=0 skips writing status/RELEASE_SNAPSHOT_<tag>_<ts>.md (when the snapshot was already written
#   for this tag by another process). Progressive saving: validation/gates_<tag>.json after every gate section. (v2 2026-10-29T02:41Z)
cd RUN_ROOT/numerics/degree6_free_parameters_48h
PY=python3
TAG=$1; CASES=$2; NTH=${3:-1}; QUICK=$4
[ -z "$TAG" ] || [ -z "$CASES" ] && { echo "usage: run_cpu_battery.sh <tag> <cases> <threads> [quick]"; exit 1; }
export CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=$NTH MKL_NUM_THREADS=$NTH OPENBLAS_NUM_THREADS=$NTH PYTHONDONTWRITEBYTECODE=1
TS=$(date -u +%Y%m%dT%H%M%SZ)
if [ "${SNAPSHOT:-1}" != "0" ]; then $PY scripts/source_state.py > status/RELEASE_SNAPSHOT_${TAG}_${TS}.md 2>&1; fi
echo "$(date -u +%FT%TZ) CPU battery $TAG cases $CASES threads $NTH cores ${CORES:-31-34}; source state status/RELEASE_SNAPSHOT_${TAG}_*.md" | tee -a validation/logs/cpu_battery_${TAG}.log
nice -n 10 taskset -c ${CORES:-31-34} $PY -u validation/gates.py --tag ${TAG} --cases ${CASES} --device cpu ${QUICK:+--quick} > validation/logs/gates_${TAG}.log 2>&1
echo "$(date -u +%FT%TZ) gates done exit $?" >> validation/logs/cpu_battery_${TAG}.log
