#!/bin/bash
# SPEC v1.15 3.6 (f)/(i) (lead 05:53Z item 4): segment 2 of a pair member continues the SAME run through the worker resume path: a new job whose config equals
# the segment-1 job's except max_iter = (cumulative iteration of the segment-1 end state) + 240 and time_limit_per_start = 7200 s, with cfg continue_from_run =
# the segment-1 run directory (the worker copies checkpoint_segment_end.pt and checks the configuration; ledger rows segment_continuation / continuation_refused).
# v2 2026-10-29T09:0xZ: the job is enqueued UNPLACED (gpus_allowed [], exclusive null, "placement": "governor", "target": {gpu, exclusive} = the segment-1 arrangement;
# lead 08:53Z item 2: segment 2 stays on its segment-1 GPUs); the slot governor grants the pair as a whole and writes gpus_allowed/exclusive from the target (V217: no
# pending job is ever eligible for the supervisor before its grant). Enqueue BOTH members of a pair in one command (complete pair before exposure, V216).
# Usage: scripts/enqueue_segment2.sh <segment-1 run dir> <new tag> <gpu> <exclusive 0|1> [iterations=240] [time_limit=7200]
cd "$(dirname "$0")/.."; PY=python3
RUN1=$1; TAG=$2; GPU=$3; EXCL=${4:-1}; INC=${5:-240}; TL=${6:-7200}
[ -d "$RUN1" ] && [ -f "$RUN1/checkpoint_segment_end.pt" ] || { echo "usage: enqueue_segment2.sh <segment-1 run dir with checkpoint_segment_end.pt> <tag> <gpu> <excl> [inc] [tl]"; exit 1; }
JID=$(basename "$RUN1"); JOBF=""
for cand in "$RUN1/job.json" "queue/done/$JID.json" "queue/running/$JID.json" "queue/failed/$JID.json"; do [ -f "$cand" ] && { JOBF=$cand; break; }; done   # v3: the supervisor keeps the job file in queue/<state>, not in the run dir
[ -n "$JOBF" ] || { echo "no job file for $JID in the run dir or queue/done|running|failed"; exit 1; }
$PY - "$RUN1" "$TAG" "$GPU" "$EXCL" "$INC" "$TL" "$JOBF" <<'PYEOF'
import json, sys, os, time, hashlib, torch
run1, tag, gpu, excl, inc, tl, jobf = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4] == "1", int(sys.argv[5]), float(sys.argv[6]), sys.argv[7]
job1 = json.load(open(jobf)); cfg = dict(job1["config"])
ck = torch.load(os.path.join(run1, "checkpoint_segment_end.pt"), map_location="cpu", weights_only=False); cur = ck["current"]
it_end = int(cur["it"]); cfg["max_iter"] = it_end + inc; cfg["time_limit_per_start"] = tl; cfg["continue_from_run"] = run1; cfg["segment"] = int(cfg.get("segment", 1)) + 1
job_id = f"{tag}_L6_cl{job1['config']['c_l']:.4f}_om{job1['config']['omega']:.4f}_{'free' if cfg.get('free_params') else 'fixed'}"
job = dict(job_id=job_id, label=job1["label"], type="d6fp", priority=job1.get("priority", 10), max_retries=job1.get("max_retries", 2), config=cfg, exclusive=None, placement="governor", target=dict(gpu=gpu, exclusive=excl),
           created=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), note=f"segment {cfg['segment']} continuation of {job1['job_id']} (run {run1}; end state it {it_end}, counters {cur.get('counters')}, lm_status {cur.get('lm_status')}); max_iter {cfg['max_iter']} = {it_end} + {inc}, time limit {tl:.0f} s (SPEC v1.15 3.6 (f)); target {'alone on GPU %d (exclusive)' % gpu if excl else 'together with its pair partner on GPU %d (non-exclusive)' % gpu} = the segment-1 arrangement, unplaced until the slot governor grants the pair; pre-verifier",
           start_sha256=job1.get("start_sha256"), objective=job1.get("objective"), gpus_allowed=[], segment_source=dict(run=run1, job_id=job1["job_id"], it_end=it_end, config_sha256_segment1=hashlib.sha256(json.dumps(job1["config"], sort_keys=True).encode()).hexdigest()))
path = os.path.join("queue", "pending", job_id + ".json")
assert not os.path.exists(path), path
json.dump(job, open(path, "w"), indent=1); print("enqueued", path, "max_iter", cfg["max_iter"], "time_limit", tl, "config_sha256", hashlib.sha256(json.dumps(cfg, sort_keys=True).encode()).hexdigest()[:16])
PYEOF
