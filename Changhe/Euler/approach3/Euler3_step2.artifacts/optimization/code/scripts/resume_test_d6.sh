#!/bin/bash
# D6FP G7: disposable free-parameter smoke job (label SMOKE, 8 iterations, checkpoint every 30 s), killed with SIGKILL after a checkpoint, then
# relaunched; the resumed run must continue from the checkpoint with the same X (bitwise), lam, iteration counter, generator state and layout,
# and the ledger must show the interruption. Usage: [MAX_ITER=3 TIME_LIMIT=14400 CKPT=60 CORES=33 WAIT_CKPTS=2] scripts/resume_test_d6.sh <gpu or cpu>
# (CPU variant 2026-10-29T02:46Z: at about 41 min per accepted iteration on one core, MAX_ITER 3 and a 14400 s time limit; the first run is killed after
# WAIT_CKPTS checkpoints (polling up to 4 h), the resumed run finishes the remaining iterations and the cheap battery.)
ROOT=$(cd "$(dirname "$0")/.." && pwd); GPU=${1:-5}
PY=python3
TAG=resume_test_$(date -u +%H%M%S)
cd "$ROOT"
$PY scripts/enqueue_d6.py --start starts/S01_nest6_cl0.45_om1.0_p0.pt --label SMOKE --tag $TAG --max_iter ${MAX_ITER:-8} --time_limit ${TIME_LIMIT:-1500} --ckpt_interval ${CKPT:-30} --no_linearization --lin_every 0 --priority 0 --note "G7 resume test (disposable)" > /dev/null
JOBQ=$(ls queue/pending/${TAG}_*.json); JID=$(basename $JOBQ .json); RUN=runs/$JID
mkdir -p $RUN logs
JOB=$RUN/job.json; mv $JOBQ $JOB            # the job file lives OUTSIDE the queue: the supervisor must never pick it up
echo "$(date -u +%FT%TZ) G7: job $JID on GPU $GPU" | tee -a logs/resume_test.log
CUDA_VISIBLE_DEVICES=$([ "$GPU" = "cpu" ] && echo "" || echo "$GPU") OMP_NUM_THREADS=1 setsid nohup nice -n 10 taskset -c ${CORES:-31-34} $PY scripts/worker_d6.py $JOB $RUN > $RUN/stdout_run1.log 2>&1 < /dev/null &
PID=$!
# wait for the second checkpoint line, then SIGKILL
for i in $(seq 1 2880); do sleep 5; n=$(grep -c "checkpoint at start" $RUN/worker.log 2>/dev/null); n=${n:-0}; n=${n//[^0-9]/}; [ -z "$n" ] && n=0; if [ "$n" -ge ${WAIT_CKPTS:-2} ]; then break; fi; if ! kill -0 $PID 2>/dev/null; then echo "worker exited early"; break; fi; done
sleep 3
echo "$(date -u +%FT%TZ) G7: SIGKILL pid $PID after $n checkpoints" | tee -a logs/resume_test.log
kill -9 $PID; sleep 2
cp $RUN/checkpoint.pt $RUN/checkpoint_at_kill.pt
grep 'LM it' $RUN/worker.log | tail -3 | tee -a logs/resume_test.log
echo "$(date -u +%FT%TZ) G7: relaunch" | tee -a logs/resume_test.log
CUDA_VISIBLE_DEVICES=$([ "$GPU" = "cpu" ] && echo "" || echo "$GPU") OMP_NUM_THREADS=1 nice -n 10 taskset -c ${CORES:-31-34} $PY scripts/worker_d6.py $JOB $RUN > $RUN/stdout_run2.log 2>&1 < /dev/null
echo "$(date -u +%FT%TZ) G7: resumed run exit $?" | tee -a logs/resume_test.log
$PY - "$RUN" <<'PYEOF' | tee -a logs/resume_test.log
import sys, torch, json, os
run = sys.argv[1]
ck = torch.load(os.path.join(run, "checkpoint_at_kill.pt"), map_location="cpu", weights_only=False)
cur = ck["current"]; print("checkpoint at kill: it", cur["it"], "lam", cur["lam"], "geometry", cur["geometry_base"], "z_opt sha", __import__("hashlib").sha256(cur["z_opt"].numpy().tobytes()).hexdigest()[:16])
log = open(os.path.join(run, "worker.log")).read().splitlines()
res = [l for l in log if "RESUME from checkpoint" in l]; print(res[-1] if res else "NO RESUME LINE")
st = [l for l in log if "resuming at iteration" in l]; print(st[-1] if st else "NO RESUMING LINE")
# the resumed run's first history record must continue from the checkpoint iterate: compare the z hash of the record at it0-1 with the checkpoint
fin = torch.load(sorted(__import__("glob").glob(os.path.join(run, "starts", "start_000*.pt")))[-1], map_location="cpu", weights_only=False)
hist = fin.get("history") or fin.get("d6fp", {}).get("trajectory")
print("final file:", "iterations", fin.get("iterations"), "status", fin.get("status"))
h = fin.get("history")
if h:
    pre = [r for r in h if r["it"] == cur["it"] - 1]
    print("record at the checkpoint iterate:", {k: pre[0][k] for k in ("it", "cost", "lam", "z_sha256_12")} if pre else "missing")
    print("checkpoint z_opt sha12:", __import__("hashlib").sha256(cur["z_opt"].numpy().tobytes()).hexdigest()[:12], "(must equal the record's z_sha256_12)")
    print("costs:", [f"{r['cost']:.9e}" for r in h])
PYEOF
echo "$(date -u +%FT%TZ) G7 done; ledger rows:"; grep "$JID" status/ledger.jsonl | cut -c1-200 | tail -8
