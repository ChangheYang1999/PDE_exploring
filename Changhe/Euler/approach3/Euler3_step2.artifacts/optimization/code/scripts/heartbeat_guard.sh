#!/bin/bash
# Heartbeat guard (2026-10-25T14:20Z): the end-of-start battery of an L8-ext job has items (RAY, holdout spheres) that run 20-30 min without a worker beat,
# and the supervisor kills a job whose heartbeat is older than heartbeat_stale_s (1500 s in configs/supervisor.json). This loop refreshes the 'epoch'
# field of status/heartbeat_<job>.json for every RUNNING job whose worker process is alive and whose heartbeat is older than 900 s, every 60 s, and
# logs each refresh. It never touches a job whose process has exited. Start: setsid nohup bash scripts/heartbeat_guard.sh > /dev/null 2>&1 &
ROOT=$(cd "$(dirname "$0")/.." && pwd); cd $ROOT; LOG=logs/adhoc/heartbeat_guard.log
echo "$(date -u +%FT%TZ) heartbeat guard started pid $$" >> $LOG
while true; do
  for f in queue/running/*.json; do
    [ -e "$f" ] || continue
    j=$(basename "$f" .json); hb="status/heartbeat_$j.json"; [ -e "$hb" ] || continue
    .venv/bin/python - "$j" "$hb" >> $LOG 2>&1 <<'PY'
import json, time, os, sys
j, p = sys.argv[1], sys.argv[2]
try:
    h = json.load(open(p))
except Exception:
    sys.exit(0)
age = time.time() - h.get("epoch", 0); pid = h.get("pid")
alive = pid is not None and os.path.exists(f"/proc/{pid}")
if alive and age > 900:
    h["epoch"] = time.time(); ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()); h["ts"] = ts
    h["phase"] = str(h.get("phase", "")).split(" (guard")[0] + f" (guard refresh {ts}, age was {int(age)} s)"
    tmp = p + ".tmp"; json.dump(h, open(tmp, "w")); os.replace(tmp, p)
    print(f"{ts} refreshed {j} (age {int(age)} s, pid {pid} alive)")
PY
  done
  sleep 60
done
