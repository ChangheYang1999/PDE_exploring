#!/bin/bash
# P1 STRATEGY-2 production comparison (lead 04:15:58Z item 2 (2); plan item 3; 21:39:31Z item 3): scripts/worker_d6_s2.py with cfg step_jacobian 'J_c' (the complete Jacobian
# as the LM step model) from the P1 segment-4 segment-end checkpoint by the same resume path as P1 segment 5 (continue_from_run, max_iter 827 = 587 + 240, 7200 s), label FREE,
# configuration otherwise identical to P1 segment 5 (its job json is the template). The supervisor's worker is fixed (scripts/worker_d6.py), so this run is HAND-LAUNCHED on an
# exclusive GPU through the busy guard (validation/l_launch_v6.sh cmd), like the strategy-2 smokes; the GPU is reserved for it (no governor target uses it); a manual ledger
# row (FREE) is written at its end; then the end chain of a FREE segment: J_c EVAL, 6.3 (a) --full end record against P1_start_v10 with segment start cont1_s4_S01_end_v10,
# wrapper (information). v2 (04:4xZ; V627): an OPEN hand-launched row (status/gpu_hours_open_hand.jsonl: label FREE, gpu, start, end running) is written at the launch and removed when the closed manual row is appended, so the ledger counts the active interval and never double counts.
# v3 (V632): open row at the worker's START line. Usage: bash scripts/s2_prod_run.sh <gpu>
set -u; cd RUN_ROOT/numerics/degree6_free_parameters_48h; D=$(pwd); PY=python3; LOG=validation/logs/l_slot_chain.log
GPU=$1; JID=s2_P1s4_Jc_L6_cl0.4500_om1.0000_free; JOB=status/s2_prod/$JID.json; TEMPLATE=queue/done/cont1_s5_S01_L6_cl0.4500_om1.0000_free.json
[ -d runs/$JID ] && { echo "REFUSED: runs/$JID exists"; exit 2; }
$PY - "$TEMPLATE" "$JOB" "$JID" "$GPU" <<'PYEOF'
import json, sys, time, hashlib
t, out, jid, gpu = sys.argv[1:5]; j = json.load(open(t)); c = dict(j["config"])
assert c["continue_from_run"].endswith("runs/cont1_s4_S01_L6_cl0.4500_om1.0000_free") and c["max_iter"] == 827 and c["time_limit_per_start"] == 7200.0
c["step_jacobian"] = "J_c"
j2 = dict(job_id=jid, label="FREE", type="d6fp", priority=0, max_retries=0, config=c, exclusive=True, created=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), objective="O1", hand_launched=True, strategy2=True,
          gpus_allowed=[int(gpu)], target=dict(gpu=int(gpu), exclusive=True), start_sha256=j.get("start_sha256"), segment_source=j.get("segment_source"),
          spec_version_job="v1.25", spec_sha256_job="acd5406d92973592c2b45e7c5f3a484e5e80234ba8d2f4e271b509076c941e64", record_label_job="full release under the post-result timing rule 3.6 (m)", g1_label_job="G1 under post-result rules 3.6 (j), (k), (l), (n)",
          lineage_history="P1 (S01, (0.45, 1.0)) segments 1 to 4 (segments 1 to 3 before the full release of 2026-10-29T16:40:13Z, segment 4 under it); this run is the STRATEGY-2 comparison (lead 04:15:58Z item 2 (2); plan item 3): the same resume path, budget and configuration as P1 segment 5 (cont1_s5_S01), with the complete Jacobian J_c as the LM step model (scripts/worker_d6_s2.py, cfg step_jacobian 'J_c'); hand-launched on an exclusive GPU (the supervisor's worker is fixed); its reference is P1 segment 5",
          note=f"strategy-2 production comparison from the P1 s4 end (lead 04:15:58Z item 2 (2)): template {t} (P1 s5 job), config identical except step_jacobian 'J_c'; worker scripts/worker_d6_s2.py; FREE; one GPU alone (GPU {gpu}); comparison with P1 s5 at equal wall time and equal accepted iterations (O1, 6.4 diagnostics, accepted/rejected counts, parameter path, holdout rho_u^max); the two ran at different times on exclusive GPUs")
json.dump(j2, open(out, "w"), indent=1); print("job written", out, hashlib.sha256(open(out, "rb").read()).hexdigest()[:16])
PYEOF
mkdir -p runs/$JID; WK=scripts/worker_d6_s2.py; T0=$(date -u +%FT%TZ)
echo "$T0 s2_prod_run: $WK ($(sha256sum $WK | cut -c1-16)) job $JOB ($(sha256sum $JOB | cut -c1-16)) on GPU $GPU (exclusive, hand-launched; lead 04:15:58Z item 2 (2))" | tee -a $LOG
OPEN=status/gpu_hours_open_hand.jsonl
# v3 (V632): the open row is written by a side watcher at the worker's actual START line (the launcher may wait at the lock for minutes), not at the launch request
( while ! grep -q "START job" runs/$JID/worker.log 2>/dev/null; do sleep 5; done; TS=$(grep -m1 "START job" runs/$JID/worker.log | cut -c1-20)
  $PY - "$TS" "$GPU" "$JID" "$OPEN" <<'PYEOF'
import json, sys
t0, gpu, jid, openf = sys.argv[1:5]
row = dict(kind="gpu_use", what=f"strategy-2 production comparison {jid} (worker_d6_s2.py, step_jacobian J_c; hand-launched; lead 04:15:58Z item 2 (2)) [OPEN: running]", label="FREE", gpu=int(gpu), start=t0, end=None, shared_jobs_on_gpu=1, open_hand_launched=True, job_id=jid)
open(openf, "a").write(json.dumps(row) + "\n"); print("open row written at the worker START:", row["start"])
PYEOF
) &
bash validation/l_launch_v6.sh cmd "cd $D && CUDA_VISIBLE_DEVICES=$GPU OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 10 taskset -c 31-34 $PY $WK $JOB runs/$JID > runs/$JID/stdout.log 2>&1"
RC=$?; T1=$(date -u +%FT%TZ); echo "$T1 s2_prod_run: worker ended (exit $RC)" | tee -a $LOG
TS0=$(grep -m1 "START job" runs/$JID/worker.log | cut -c1-20); [ -n "$TS0" ] || TS0=$T0
$PY - "$JID" "$OPEN" <<'PYEOF'
import json, sys
jid, openf = sys.argv[1:3]
rows = [l for l in open(openf).read().splitlines() if l.strip() and json.loads(l).get("job_id") != jid]
open(openf, "w").write("\n".join(rows) + ("\n" if rows else "")); print("open row removed for", jid)
PYEOF
$PY - "$TS0" "$T1" "$GPU" "$JID" <<'PYEOF'
import json, sys, datetime as dt
t0, t1, gpu, jid = sys.argv[1:5]; f = lambda s: dt.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")
row = dict(kind="gpu_use", what=f"strategy-2 production comparison {jid} (worker_d6_s2.py, step_jacobian J_c; hand-launched; lead 04:15:58Z item 2 (2))", label="FREE", gpu=int(gpu), start=t0, end=t1, hours=round((f(t1) - f(t0)).total_seconds() / 3600.0, 4), shared_jobs_on_gpu=1, note="FREE production run outside the supervisor (no launch row in status/ledger.jsonl; the worker's own job_end/segment_end rows exist); counted here as FREE")
open("status/gpu_hours_manual.jsonl", "a").write(json.dumps(row) + "\n"); print("ledger row:", row)
PYEOF
grep -E "LM finished|JOB DONE" runs/$JID/worker.log | tail -2 | cut -c1-300
# end chain (FREE segment): J_c EVAL, --full record vs P1_start_v10 with segment start cont1_s4_S01_end_v10, wrapper (information)
NAME=jceval_v5_s2_P1s4_Jc_$(date -u +%H%M%S); bash validation/l_launch_v6.sh frozen $NAME $GPU jc_eval_state.py $D/runs/$JID cuda:0 256
if [ -d runs_l/$NAME/validation/jc_eval/$JID ]; then mkdir -p validation/jc_eval/$JID; cp -n runs_l/$NAME/validation/jc_eval/$JID/* validation/jc_eval/$JID/; echo "$(date -u +%FT%TZ) J_c EVAL of $JID copied" | tee -a $LOG; fi
bash scripts/r63a_run.sh $GPU s2_P1s4_Jc_end end $D/runs/$JID --full --start-ref $D/validation/records_63a/P1_start_v10.json --segment-start $D/validation/records_63a/cont1_s4_S01_end_v10.json
DEC=$($PY scripts/r63a_decide.py --end s2_P1s4_Jc_end --ref P1_start_v10); echo "$(date -u +%FT%TZ) wrapper r63a_decide: --end s2_P1s4_Jc_end --ref P1_start_v10" > validation/records_63a/s2_P1s4_Jc_end.decision.txt; echo "$DEC" >> validation/records_63a/s2_P1s4_Jc_end.decision.txt
echo "$(date -u +%FT%TZ) 6.3 (a) decision for s2_P1s4_Jc_end vs P1_start_v10: $DEC" | tee -a $LOG
echo "$(date -u +%FT%TZ) s2_prod_run done (no enqueue)" | tee -a $LOG
