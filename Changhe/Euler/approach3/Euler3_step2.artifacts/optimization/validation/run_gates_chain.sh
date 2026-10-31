#!/bin/bash
# G8 controls then the full gate battery (all cases of SPEC 3.1) on one GPU, detached. Usage: run_gates_chain.sh <gpu> <tag> <cases>
cd "$(dirname "$0")/.."; PY=python3
GPU=$1; TAG=$2; CASES=$3
export CUDA_VISIBLE_DEVICES=$GPU OMP_NUM_THREADS=1
echo "$(date -u +%FT%TZ) G8 start" 
nice -n 10 $PY -u validation/g8_controls.py > validation/logs/g8_controls_$TAG.log 2>&1
echo "$(date -u +%FT%TZ) G8 done exit $?; gates start cases $CASES"
nice -n 10 $PY -u validation/gates.py --tag $TAG --cases $CASES > validation/logs/gates_$TAG.log 2>&1
echo "$(date -u +%FT%TZ) gates done exit $?"
