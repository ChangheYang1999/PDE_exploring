#!/bin/bash
# Wait (up to 4 h) until the job is launched, read its GPU from logs/supervisor.log, then run gpu_mem_sampler.sh for it.
# Usage: setsid nohup bash scripts/gpu_mem_sampler_wait.sh <job id> > /dev/null 2>&1 &
ROOT=$(cd "$(dirname "$0")/.." && pwd); cd $ROOT; JOB=$1; n=0
while [ ! -e "queue/running/$JOB.json" ] && [ $n -lt 720 ]; do sleep 20; n=$((n+1)); done
[ -e "queue/running/$JOB.json" ] || { echo "$(date -u +%FT%TZ) $JOB not launched within 4 h" >> logs/adhoc/gpumem_${JOB}.log; exit 0; }
GPU=$(grep "launched $JOB on GPU" logs/supervisor.log | tail -n 1 | sed 's/.*on GPU \([0-9]*\).*/\1/')
[ -n "$GPU" ] || GPU=0
exec bash scripts/gpu_mem_sampler.sh $GPU $JOB
