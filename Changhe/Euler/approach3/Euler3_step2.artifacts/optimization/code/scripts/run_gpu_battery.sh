#!/bin/bash
# D6FP GPU battery (GPUs 4,5,6 restored to this lane at 2026-10-29T02:51:04Z, GPU_UPDATE.md): gates.py on the given cases on ONE GPU.
# Usage: scripts/run_gpu_battery.sh <gpu index> <core> <tag> <cases,comma,separated> [sections]   (snapshot cpu_v1 code; records state device cuda)
cd RUN_ROOT/numerics/degree6_free_parameters_48h
PY=python3
GPU=$1; CORE=$2; TAG=$3; CASES=$4; SEC=$5
[ -z "$GPU" ] || [ -z "$TAG" ] || [ -z "$CASES" ] && { echo "usage: run_gpu_battery.sh <gpu> <core> <tag> <cases> [sections]"; exit 1; }
export CUDA_VISIBLE_DEVICES=$GPU OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
echo "$(date -u +%FT%TZ) GPU battery $TAG cases $CASES on GPU $GPU core $CORE ${SEC:+sections $SEC}; snapshot: the current source state (see status/RELEASE_SNAPSHOT_gpu_v1*.md; the record stores the code hashes)" | tee -a validation/logs/gpu_battery_${TAG}.log
nice -n 10 taskset -c ${CORE} $PY -u validation/gates.py --tag ${TAG} --cases ${CASES} --device cuda:0 ${SEC:+--sections $SEC} > validation/logs/gates_${TAG}.log 2>&1
echo "$(date -u +%FT%TZ) gates done exit $?" >> validation/logs/gpu_battery_${TAG}.log
