#!/bin/bash
# D6FP 2026-10-29T08:4xZ: start production on GPUs 4,5,6 after the lead's PROVISIONAL RELEASE note (SPEC v1.18 3.6 (f), (h), (i)).
# Order: (1) the slot governor writes "gpus"/"max_running" of configs/supervisor_gpu456.json from the live process counts (hold while
# validation/gate_queue.txt still lists items; four busy host processes at most), (2) the governor loop runs detached, (3) the supervisor
# starts with that configuration (CUDA_VISIBLE_DEVICES=4,5,6; each worker gets its own GPU index from the supervisor).
# Pairs must already be enqueued: PLACE="4:1 5:1 6:0 6:0" scripts/enqueue_gpu_pairs.sh 120 3600 s1
# Stop: touch status/STOP_SUPERVISOR (workers checkpoint and exit) and status/STOP_SLOT_GOVERNOR.
ROOT=$(cd "$(dirname "$0")/.." && pwd); cd "$ROOT"
PY=python3
CFG=${D6_SUPERVISOR_CFG:-$ROOT/configs/supervisor_gpu456.json}; GPUS=${D6_GPUS:-4,5,6}
rm -f status/STOP_SLOT_GOVERNOR
gov_alive() { "$PY" - <<'PYEOF'
import psutil, sys
for p in psutil.process_iter(["pid", "name", "cmdline"]):
    c = p.info["cmdline"] or []
    if len(c) > 1 and c[1].endswith("scripts/slot_governor.py") and (p.info["name"] or "").startswith("python"):
        print(p.pid); sys.exit(0)
sys.exit(1)
PYEOF
}
if gov_alive > /dev/null; then echo "governor already running (pid $(gov_alive))"; else   # exact cmdline match (a pgrep pattern matched the calling shell's own command line at 09:09Z)
  CUDA_VISIBLE_DEVICES= "$PY" scripts/slot_governor.py --cfg "$CFG" --gpus "$GPUS" --once > /dev/null || { echo "governor --once failed"; exit 1; }
  setsid nohup env CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 nice -n 15 taskset -c 31-34 "$PY" scripts/slot_governor.py --cfg "$CFG" --gpus "$GPUS" >> logs/slot_governor.out 2>&1 < /dev/null &
  sleep 2; echo "governor started at $(date -u +%FT%TZ): $(tail -1 logs/slot_governor.log | cut -c1-200)"
fi
D6_SUPERVISOR_CFG="$CFG" D6_CVD="$GPUS" bash scripts/start_supervisor.sh
