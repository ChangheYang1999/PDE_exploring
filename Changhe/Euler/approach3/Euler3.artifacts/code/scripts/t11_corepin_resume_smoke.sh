#!/bin/bash
# Resume path with 'auto' pins (worker fix 2026-10-25T23:22Z): run a disposable CPU job with core_pin auto, kill -9 after the first checkpoint, resume, and check
# that the restored pin equals the start state's pin (log lines 'S8 CORE PIN' and 'restored from the checkpoint meta').
ROOT=$(cd "$(dirname "$0")/.." && pwd); cd $ROOT
export CUDA_VISIBLE_DEVICES=-1 OMP_NUM_THREADS=1 PYTHONUNBUFFERED=1
D=runs/t11lit; rm -rf $D/P; mkdir -p $D/P; rm -f status/heartbeat_resume_test_t11lit_cpu_P_corepin.json
.venv/bin/python scripts/worker.py $D/job_P.json $D/P > $D/P/stdout1.log 2>&1 &
P=$!
for i in $(seq 1 300); do sleep 2; IT=$(python3 -c "import torch;s=torch.load('$D/P/checkpoint.pt',map_location='cpu',weights_only=False);c=s['current'];print(-1 if c is None else c['it'])" 2>/dev/null || echo -1); if [ "$IT" -ge 6 ] 2>/dev/null; then break; fi; if ! kill -0 $P 2>/dev/null; then break; fi; done
kill -9 $P 2>/dev/null; sleep 1; echo "$(date -u +%FT%TZ) killed at checkpoint iteration $IT"
.venv/bin/python scripts/worker.py $D/job_P.json $D/P > $D/P/stdout2.log 2>&1; echo "$(date -u +%FT%TZ) resumed run exit $?"
grep -E "S8 CORE PIN|restored|RESUME|resuming|PIN ROWS|JOB" $D/P/worker.log | cut -c1-220
