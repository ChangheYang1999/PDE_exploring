#!/bin/bash
# Strategy-2 END CHAIN (lead 06:58:09Z item 2 (b)-(c); V674): (1) zero-step resume of the s2 worker on the same run directory with max_iter = 630 (the periodic checkpoint's cumulative
# iteration) so that it writes checkpoint_segment_end.pt (= the it-630 state) and runs the END BATTERY without any LM step; (2) J_c EVAL; (3) 6.3 (a) --full end record against
# P1_start_v10 with segment start cont1_s4_S01_end_v10; (4) the admitted wrapper; a manual ledger row (FREE: the end battery belongs to the production job) for the resume's wall.
# Every step through the busy guard, one GPU. Written as a NEW script (the v2 instance of s2_prod_run.sh died after an in-place edit: KNOWN_ISSUES). Usage: bash scripts/s2_end_chain.sh <gpu>
set -u; cd RUN_ROOT/numerics/degree6_free_parameters_48h; D=$(pwd); PY=python3; LOG=validation/logs/l_slot_chain.log
GPU=$1; JID=s2_P1s4_Jc_L6_cl0.4500_om1.0000_free; JOB=status/s2_prod/$JID.endbattery.json; WK=scripts/worker_d6_s2.py
echo "$(date -u +%FT%TZ) s2_end_chain: zero-step resume for the end battery: $WK ($(sha256sum $WK | cut -c1-16)) job $JOB ($(sha256sum $JOB | cut -c1-16)) on GPU $GPU" | tee -a $LOG
T0=$(date -u +%FT%TZ)
bash validation/l_launch_v6.sh cmd "cd $D && CUDA_VISIBLE_DEVICES=$GPU OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 10 taskset -c 31-34 $PY $WK $JOB runs/$JID >> runs/$JID/stdout.log 2>&1"
RC=$?; T1=$(date -u +%FT%TZ); echo "$T1 s2_end_chain: resume/battery ended (exit $RC)" | tee -a $LOG
TS0=$(grep "START job" runs/$JID/worker.log | tail -1 | cut -c1-20); [ -n "$TS0" ] || TS0=$T0
$PY - "$TS0" "$T1" "$GPU" "$JID" <<'PYEOF'
import json, sys, datetime as dt
t0, t1, gpu, jid = sys.argv[1:5]; f = lambda s: dt.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")
row = dict(kind="gpu_use", what=f"strategy-2 end battery by zero-step resume {jid} (lead 06:58:09Z item 2 (b)-(c); max_iter 630 = the periodic checkpoint's iteration; no LM step)", label="FREE", gpu=int(gpu), start=t0, end=t1, hours=round((f(t1) - f(t0)).total_seconds() / 3600.0, 4), shared_jobs_on_gpu=1, note="end battery of the hand-launched FREE production run (counted FREE like the worker's own battery)", job_id=jid)
open("status/gpu_hours_manual.jsonl", "a").write(json.dumps(row) + "\n"); print("ledger row:", row)
PYEOF
grep -E "LM finished|JOB DONE|resuming" runs/$JID/worker.log | tail -3 | cut -c1-300
[ -f runs/$JID/checkpoint_segment_end.pt ] || { echo "$(date -u +%FT%TZ) s2_end_chain: NO checkpoint_segment_end.pt after the resume; stopping" | tee -a $LOG; exit 1; }
NAME=jceval_v5_s2_P1s4_Jc_$(date -u +%H%M%S); bash validation/l_launch_v6.sh frozen $NAME $GPU jc_eval_state.py $D/runs/$JID cuda:0 256
if [ -d runs_l/$NAME/validation/jc_eval/$JID ]; then mkdir -p validation/jc_eval/$JID; cp -n runs_l/$NAME/validation/jc_eval/$JID/* validation/jc_eval/$JID/; echo "$(date -u +%FT%TZ) J_c EVAL of $JID copied" | tee -a $LOG; fi
bash scripts/r63a_run.sh $GPU s2_P1s4_Jc_end end $D/runs/$JID --full --start-ref $D/validation/records_63a/P1_start_v10.json --segment-start $D/validation/records_63a/cont1_s4_S01_end_v10.json
DEC=$($PY scripts/r63a_decide.py --end s2_P1s4_Jc_end --ref P1_start_v10); echo "$(date -u +%FT%TZ) wrapper r63a_decide: --end s2_P1s4_Jc_end --ref P1_start_v10" > validation/records_63a/s2_P1s4_Jc_end.decision.txt; echo "$DEC" >> validation/records_63a/s2_P1s4_Jc_end.decision.txt
echo "$(date -u +%FT%TZ) 6.3 (a) decision for s2_P1s4_Jc_end vs P1_start_v10: $DEC" | tee -a $LOG
echo "$(date -u +%FT%TZ) s2_end_chain done" | tee -a $LOG
