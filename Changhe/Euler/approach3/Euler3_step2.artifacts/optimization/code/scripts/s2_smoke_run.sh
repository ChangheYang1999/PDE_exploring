#!/bin/bash
# Strategy-2 smoke runs (lead 18:31:20Z item 4 (i), 20:22:14Z item 2 (a)): one at a time on an exclusive GPU through the busy guard; label SMOKE in the manual
# ledger (the prod reference run is labelled FREE by the worker's rule and accounted as SMOKE). Blocks until the run ends.
# Usage: bash scripts/s2_smoke_run.sh <Jc|hookoff|prod> <gpu>
set -u; cd RUN_ROOT/numerics/degree6_free_parameters_48h; D=$(pwd); PY=python3
W=$1; GPU=$2; JID=s2smoke_${W}_cont1s3; JOB=status/s2_smoke/$JID.json; [ -f $JOB ] || { echo "no job file $JOB"; exit 1; }
case $W in Jc|hookoff) WK=scripts/worker_d6_s2.py;; prod) WK=scripts/worker_d6.py;; *) echo "unknown smoke $W"; exit 1;; esac
mkdir -p runs/$JID; T0=$(date -u +%FT%TZ)
echo "$T0 s2 smoke $W: $WK ($(sha256sum $WK | cut -c1-16)) job $JOB ($(sha256sum $JOB | cut -c1-16)) on GPU $GPU (exclusive)" | tee -a validation/logs/l_slot_chain.log
bash validation/l_launch_v6.sh cmd "cd $D && CUDA_VISIBLE_DEVICES=$GPU OMP_NUM_THREADS=1 nice -n 10 taskset -c 31-34 $PY $WK $JOB runs/$JID > runs/$JID/stdout.log 2>&1"
T1=$(date -u +%FT%TZ); echo "$T1 s2 smoke $W ended (exit $?)" | tee -a validation/logs/l_slot_chain.log
$PY - "$T0" "$T1" "$GPU" "$JID" <<'PYEOF'
import json, sys, datetime as dt
t0, t1, gpu, jid = sys.argv[1:5]
f = lambda s: dt.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")
h = (f(t1) - f(t0)).total_seconds() / 3600.0
row = dict(kind="gpu_use", what=f"strategy-2 smoke {jid}", label="SMOKE", gpu=int(gpu), start=t0, end=t1, hours=round(h, 4), note="hand-launched smoke on an exclusive GPU (lead 18:31:20Z item 4 (i)); outside the 8.3 mix")
open("status/gpu_hours_manual.jsonl", "a").write(json.dumps(row) + "\n"); print("ledger row:", row)
PYEOF
grep -E "LM it|LM finished|JOB DONE|Traceback|Error" runs/$JID/worker.log runs/$JID/stdout.log 2>/dev/null | tail -6 | cut -c1-300
