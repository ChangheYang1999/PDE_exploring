#!/bin/bash
# Sample the memory of one GPU every 20 s while a given job is in queue/running; log the running maximum (peak memory of smoke batteries).
# Usage: setsid nohup bash scripts/gpu_mem_sampler.sh <gpu index> <job id> > /dev/null 2>&1 &
ROOT=$(cd "$(dirname "$0")/.." && pwd); cd $ROOT; GPU=$1; JOB=$2; LOG=logs/adhoc/gpumem_${JOB}.log; PEAK=0
echo "$(date -u +%FT%TZ) sampler start gpu $GPU job $JOB" >> $LOG
while [ -e "queue/running/$JOB.json" ]; do
  M=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits -i $GPU 2>/dev/null | head -n 1 | tr -d ' ')
  if [ -n "$M" ] && [ "$M" -gt "$PEAK" ]; then PEAK=$M; echo "$(date -u +%FT%TZ) new peak $PEAK MiB" >> $LOG; fi
  sleep 20
done
echo "$(date -u +%FT%TZ) job left queue/running; peak $PEAK MiB" >> $LOG
