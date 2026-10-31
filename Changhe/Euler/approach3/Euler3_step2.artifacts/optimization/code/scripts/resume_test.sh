#!/bin/bash
# Interruption-and-resume test on a disposable job: start worker, kill -9 it after 120 s, restart, verify RESUME in log.
ROOT=$(cd "$(dirname "$0")/.." && pwd); cd $ROOT
RD=runs/resume_test; rm -rf $RD/starts $RD/checkpoint.pt $RD/worker.log $RD/results.jsonl status/heartbeat_resume_test.json
export CUDA_VISIBLE_DEVICES=${1:-5} OMP_NUM_THREADS=1 PYTHONUNBUFFERED=1
.venv/bin/python scripts/worker.py $RD/job.json $RD > $RD/stdout1.log 2>&1 &
P=$!; echo "worker pid $P started $(date -u +%T)"; sleep 120
kill -9 $P; sleep 2; echo "killed -9 at $(date -u +%T); checkpoint: $(ls -la $RD/checkpoint.pt 2>/dev/null)"
python3 -c "import torch;s=torch.load('$RD/checkpoint.pt',map_location='cpu',weights_only=False);print('checkpoint state: completed',len(s['completed']),'current', None if s['current'] is None else dict(idx=s['current']['idx'],it=s['current']['it']))"
.venv/bin/python scripts/worker.py $RD/job.json $RD > $RD/stdout2.log 2>&1
echo "second run exit $?"; grep -E "RESUME|resuming|start [01] done|JOB" $RD/worker.log
