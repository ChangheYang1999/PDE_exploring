#!/bin/bash
# Regularized refit files for the F6 points (lead 22:41:03Z item 3 (d), (e); after the control passed and the verifier checked it): on one GPU through l_launch_v3:
# point 1 (S09, (0.42179, 0.808573)) -> starts/F6_S09_k1_refit_v2.pt, then point 0 (S01, (0.459677, 1.338884)) -> starts/F6_S01_k0_refit_v2.pt; each with its
# .json record; a target that fails the tool's guards is marked .UNUSABLE and gets no pilot. Pilots are enqueued separately (release_queue f2refit) on the lead's word.
# Usage: bash scripts/refit_v2_points.sh <gpu>
set -u; cd RUN_ROOT/numerics/degree6_free_parameters_48h; D=$(pwd); PY=python3; GPU=$1; LOG=validation/logs/l_slot_chain.log
fit() { T0=$(date -u +%FT%TZ); bash validation/l_launch_v6.sh cmd "cd $D && CUDA_VISIBLE_DEVICES=$GPU OMP_NUM_THREADS=1 nice -n 10 taskset -c 31-34 $PY scripts/refit_start_v2.py $1 $2 $3 $4 --device cuda:0 > validation/logs/refit_v2_$(basename $4 .pt).out 2>&1"; T1=$(date -u +%FT%TZ)
  $PY - "$T0" "$T1" "$GPU" "$4" <<'PYEOF'
import json, sys, datetime as dt
t0, t1, gpu, out = sys.argv[1:5]; f = lambda s: dt.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")
open("status/gpu_hours_manual.jsonl", "a").write(json.dumps(dict(kind="gpu_use", what=f"refit_start_v2.py {out}", label="VALIDATION", gpu=int(gpu), start=t0, end=t1, hours=round((f(t1) - f(t0)).total_seconds() / 3600, 4), note="regularized offline refit (lead 22:41:03Z item 3)")) + "\n")
PYEOF
  tail -2 validation/logs/refit_v2_$(basename $4 .pt).out | cut -c1-300; echo "$(date -u +%FT%TZ) refit v2 file $4: $( [ -f $4 ] && echo sha256 $(sha256sum $4 | cut -c1-16) || echo MISSING ) $( [ -f $4.UNUSABLE ] && echo UNUSABLE )" | tee -a $LOG; }
echo "$(date -u +%FT%TZ) refit v2 point fits on GPU $GPU: tool $(sha256sum scripts/refit_start_v2.py | cut -c1-16)" | tee -a $LOG
fit starts/S09_d6w_cl0.45_om0.3_R1.pt 0.42179 0.808573 starts/F6_S09_k1_refit_v2.pt
fit starts/S01_nest6_cl0.45_om1.0_p0.pt 0.459677 1.338884 starts/F6_S01_k0_refit_v2.pt
echo "$(date -u +%FT%TZ) refit v2 point fits done (pilots on the lead's word: bash scripts/release_queue.sh f2refit S09_k1|S01_k0 <gpu> 1)" | tee -a $LOG
