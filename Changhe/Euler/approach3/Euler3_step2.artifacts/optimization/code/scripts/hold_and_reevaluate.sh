#!/bin/bash
# Hold the pending exclusive jobs, wait until the exclusive job on the given GPU has left queue/running, re-evaluate the heavy states
# (status/reeval_heavy.txt) on that GPU one after another, regenerate the shortlist, release the hold. Usage: hold_and_reevaluate.sh <gpu> <running job id to wait for>
ROOT=$(cd "$(dirname "$0")/.." && pwd); cd $ROOT
GPU=$1; WAITJOB=$2; LOG=logs/adhoc/hold_reeval_$(date -u +%Y%m%dT%H%M%SZ).log
echo "$(date -u +%FT%TZ) hold_and_reevaluate: gpu $GPU wait for $WAITJOB" >> $LOG
bash scripts/hold_exclusive.sh >> $LOG 2>&1
n=0
while [ -e "queue/running/$WAITJOB.json" ] && [ $n -lt 720 ]; do sleep 20; n=$((n+1)); done
echo "$(date -u +%FT%TZ) $WAITJOB left queue/running (waited $((n*20)) s); starting re-evaluations" >> $LOG
export CUDA_VISIBLE_DEVICES=$GPU OMP_NUM_THREADS=1 PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
for f in $(cat status/reeval_heavy.txt); do
  [ -e "$f" ] || { echo "missing $f" >> $LOG; continue; }
  echo "$(date -u +%FT%TZ) re-evaluating $f" >> $LOG
  timeout 3000 .venv/bin/python scripts/reevaluate_holdout.py --device cuda:0 $f >> $LOG 2>&1
done
.venv/bin/python scripts/shortlist.py all >> $LOG 2>&1
bash scripts/release_hold.sh >> $LOG 2>&1
echo "$(date -u +%FT%TZ) hold_and_reevaluate done" >> $LOG
