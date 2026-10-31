#!/bin/bash
# v3 (00:0xZ): the enqueue runs under the launcher lock until the new worker is visible (scripts/enqueue_under_lock.sh; 23:54Z race).
# v2 (23:2xZ): waits for a host slot (scripts/wait_slot.sh) before enqueuing the pilot (the supervisor launches granted jobs without a host-slot check; incident 23:20:44Z).
# F3 offline chain (lead 22:55:42Z item 2; V505): on one GPU through l_launch_v3: generate starts/F3_S01_<size>_s<seed>.pt with scripts/perturb_start_free.py
# (S01 at its own parameters; no parameter perturbation), then enqueue the pilot (release_queue f3off) if the file is usable. Usage: bash scripts/f3_chain.sh <gpu> <1e-3|1e-1> <seed>
set -u; cd RUN_ROOT/numerics/degree6_free_parameters_48h; D=$(pwd); PY=python3; GPU=$1; SZ=$2; SD=$3; LOG=validation/logs/l_slot_chain.log
OUT=starts/F3_S01_${SZ}_s${SD}.pt
echo "$(date -u +%FT%TZ) F3 chain on GPU $GPU: perturb_start_free.py $(sha256sum scripts/perturb_start_free.py | cut -c1-16) size $SZ seed $SD -> $OUT" | tee -a $LOG
T0=$(date -u +%FT%TZ)
bash validation/l_launch_v6.sh cmd "cd $D && CUDA_VISIBLE_DEVICES=$GPU OMP_NUM_THREADS=1 nice -n 10 taskset -c 31-34 $PY scripts/perturb_start_free.py starts/S01_nest6_cl0.45_om1.0_p0.pt $OUT --size $SZ --seed $SD --device cuda:0 > validation/logs/perturb_$(basename $OUT .pt).out 2>&1"
T1=$(date -u +%FT%TZ)
$PY - "$T0" "$T1" "$GPU" "$OUT" <<'PYEOF'
import json, sys, datetime as dt
t0, t1, gpu, out = sys.argv[1:5]; f = lambda s: dt.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")
open("status/gpu_hours_manual.jsonl", "a").write(json.dumps(dict(kind="gpu_use", what=f"perturb_start_free.py {out}", label="VALIDATION", gpu=int(gpu), start=t0, end=t1, hours=round((f(t1) - f(t0)).total_seconds() / 3600, 4), note="offline F3 perturbed start (lead 22:55:42Z item 2)")) + "\n")
PYEOF
tail -3 validation/logs/perturb_$(basename $OUT .pt).out | cut -c1-300
if [ -f "$OUT" ] && [ ! -f "$OUT.UNUSABLE" ]; then echo "$(date -u +%FT%TZ) F3 file $OUT sha256 $(sha256sum $OUT | cut -c1-16): usable; waiting for a host slot, then enqueue pilot f3off $SZ on GPU $GPU" | tee -a $LOG; bash scripts/enqueue_under_lock.sh f3off_S01_${SZ}_s${SD} bash scripts/release_queue.sh f3off $SZ $GPU 1 2>&1 | tee -a $LOG; else echo "$(date -u +%FT%TZ) F3 file $OUT missing or UNUSABLE: no pilot" | tee -a $LOG; fi
echo "$(date -u +%FT%TZ) F3 chain done" | tee -a $LOG
