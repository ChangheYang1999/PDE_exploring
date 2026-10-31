#!/bin/bash
# D6FP: run one SMOKE/VALIDATION job directly with the worker (no supervisor), keeping its job file OUTSIDE the queue.
# Usage: [CORES=34] scripts/run_smoke_job.sh <gpu or cpu> <tag> [enqueue_d6.py options...]  (CORES: taskset core list, default 31-34; added 2026-10-29T02:36Z)   e.g. scripts/run_smoke_job.sh 5 smk1 --start starts/S01_nest6_cl0.45_om1.0_p0.pt --max_iter 12
ROOT=$(cd "$(dirname "$0")/.." && pwd); GPU=$1; TAG=$2; shift 2
PY=python3
cd "$ROOT"
$PY scripts/enqueue_d6.py --label SMOKE --tag $TAG --priority 0 "$@" > /dev/null || exit 1
JOBQ=$(ls queue/pending/${TAG}_*.json | head -1); JID=$(basename $JOBQ .json); RUN=runs/$JID; mkdir -p $RUN
JOB=$RUN/job.json; mv $JOBQ $JOB
echo "$(date -u +%FT%TZ) smoke job $JID on GPU $GPU (job file $JOB)"
CUDA_VISIBLE_DEVICES=$([ "$GPU" = "cpu" ] && echo "" || echo "$GPU") OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 setsid nohup nice -n 10 taskset -c ${CORES:-31-34} $PY scripts/worker_d6.py $JOB $RUN > $RUN/stdout.log 2>&1 < /dev/null &
echo "pid $! log $RUN/worker.log"
