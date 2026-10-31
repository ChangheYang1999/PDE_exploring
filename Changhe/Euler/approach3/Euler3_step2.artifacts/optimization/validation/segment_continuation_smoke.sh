#!/bin/bash
# D6FP gpu_v1p1 validation of the segment continuation (SPEC v1.14 3.6 (f); lead 05:23Z item 2, 05:30Z item 2): job A (SMOKE, S01, max_iter 3, cheap battery)
# then job B (SMOKE, cfg continue_from_run = runs/<A>, max_iter 5 total, otherwise identical) on the same GPU; checks in validation/segment_continuation_check.json:
# B logs SEGMENT CONTINUATION; B's first record has it_cum 3 and counters continuing A's end counters; the vector B loads equals A's checkpoint_segment_end z_opt
# bytes; A's and B's ledger rows (segment_end, segment_continuation); A's run also receives a continuation attempt with a changed config (cfg chunk 128),
# which must be refused and recorded (continuation_refused) and run as a fresh start of 1 iteration. Usage: validation/segment_continuation_smoke.sh <gpu> <core>
ROOT=$(cd "$(dirname "$0")/.." && pwd); cd "$ROOT"; GPU=$1; CORE=${2:-31-34}; LOG=validation/logs/segment_continuation_smoke.log
PY=python3
EXTRA_A='{"complete_gradient_every": 4, "battery": "cheap"}'
echo "$(date -u +%FT%TZ) continuation smoke on GPU $GPU core $CORE: job A" >> $LOG
CORES=$CORE bash scripts/run_smoke_job.sh $GPU segA --start starts/S01_nest6_cl0.45_om1.0_p0.pt --max_iter 3 --ckpt_interval 60 --time_limit 1800 --extra "$EXTRA_A" --note "segment continuation smoke, segment 1 (A)" >> $LOG 2>&1
RUNA=$(ls -d runs/segA_* | head -1); PIDA=$(pgrep -f "worker_d6.py $RUNA/job.json" | head -1); while kill -0 $PIDA 2>/dev/null; do sleep 10; done
echo "$(date -u +%FT%TZ) A finished ($RUNA); job B (continuation, max_iter 5 total)" >> $LOG
EXTRA_B="{\"complete_gradient_every\": 4, \"battery\": \"cheap\", \"continue_from_run\": \"$RUNA\"}"
CORES=$CORE bash scripts/run_smoke_job.sh $GPU segB --start starts/S01_nest6_cl0.45_om1.0_p0.pt --max_iter 5 --ckpt_interval 60 --time_limit 1800 --extra "$EXTRA_B" --note "segment continuation smoke, segment 2 (B) continuing A" >> $LOG 2>&1
RUNB=$(ls -d runs/segB_* | head -1); PIDB=$(pgrep -f "worker_d6.py $RUNB/job.json" | head -1); while kill -0 $PIDB 2>/dev/null; do sleep 10; done
echo "$(date -u +%FT%TZ) B finished ($RUNB); job C (continuation with a changed config: chunk 128 -> must be refused)" >> $LOG
EXTRA_C="{\"complete_gradient_every\": 4, \"battery\": \"cheap\", \"continue_from_run\": \"$RUNA\", \"chunk\": 128}"
CORES=$CORE bash scripts/run_smoke_job.sh $GPU segC --start starts/S01_nest6_cl0.45_om1.0_p0.pt --max_iter 1 --ckpt_interval 60 --time_limit 1800 --extra "$EXTRA_C" --note "segment continuation smoke, refused continuation (C)" >> $LOG 2>&1
RUNC=$(ls -d runs/segC_* | head -1); PIDC=$(pgrep -f "worker_d6.py $RUNC/job.json" | head -1); while kill -0 $PIDC 2>/dev/null; do sleep 10; done
echo "$(date -u +%FT%TZ) C finished ($RUNC); checking" >> $LOG
$PY - "$RUNA" "$RUNB" "$RUNC" <<'PYEOF' > validation/logs/segment_continuation_check.out 2>&1
import sys, os, json, glob, hashlib, re, torch
A, B, C = sys.argv[1:4]; out = dict(A=A, B=B, C=C); ck = {}
segA = torch.load(os.path.join(A, "checkpoint_segment_end.pt"), map_location="cpu", weights_only=False); ca = segA["current"]
out["A_end"] = dict(it=ca["it"], counters=ca.get("counters"), lam=ca["lam"], z_sha=hashlib.sha256(ca["z_opt"].numpy().tobytes()).hexdigest(), status=ca.get("lm_status"))
logB = open(os.path.join(B, "worker.log")).read(); logC = open(os.path.join(C, "worker.log")).read()
mB = re.search(r"resumed vector sha256 ([0-9a-f]+)", logB); ck["B_logs_segment_continuation"] = "SEGMENT CONTINUATION from" in logB
ck["B_loaded_vector_equals_A_end_bytes"] = bool(mB) and mB.group(1) == out["A_end"]["z_sha"]
finB = sorted(glob.glob(os.path.join(B, "starts", "start_000*.pt")))
if finB:
    hb = torch.load(finB[-1], map_location="cpu", weights_only=False).get("history") or []
    post = [r for r in hb if r.get("it_cum") == ca["it"]]; out["B_first_record"] = ({k: post[0].get(k) for k in ("it", "it_cum", "counters", "lam", "accepted")} if post else None)
    ck["B_first_record_it_cum_equals_A_end_it"] = bool(post)
    ck["B_counters_continue"] = bool(post) and post[0]["counters"]["n_acc"] == ca["counters"]["n_acc"] + int(bool(post[0]["accepted"]))
    ck["B_history_prefix_is_A"] = len(hb) >= ca["it"] and all(r.get("it_cum") == i for i, r in enumerate(hb[: ca["it"]]))
    out["B_n_records"] = len(hb)
mc = re.search(r"LM initial cost ([0-9.eE+-]+)", logB.split("SEGMENT CONTINUATION")[-1]) if "SEGMENT CONTINUATION" in logB else None
pre_cost = ca["history"][-1]["cost"] if ca.get("history") else None
ck["B_initial_O1_equals_A_end_cost_1e-12"] = bool(mc) and pre_cost is not None and abs(float(mc.group(1)) - pre_cost) / abs(pre_cost) <= 1e-12
ck["C_refused_and_fresh"] = ("SEGMENT CONTINUATION REFUSED" in logC) and ("job config differs" in logC)
led = [json.loads(l) for l in open("status/ledger.jsonl") if l.strip()]
kinds = lambda run: sorted(set(r.get("kind") for r in led if r.get("job_id") == os.path.basename(run)))
out["ledger_kinds"] = dict(A=kinds(A), B=kinds(B), C=kinds(C))
ck["ledger_A_segment_end"] = "segment_end" in out["ledger_kinds"]["A"]; ck["ledger_B_segment_continuation"] = "segment_continuation" in out["ledger_kinds"]["B"]; ck["ledger_C_continuation_refused"] = "continuation_refused" in out["ledger_kinds"]["C"]
out["checks"] = ck; out["PASS"] = all(v is True for v in ck.values())
json.dump(out, open("validation/segment_continuation_check.json", "w"), indent=1, default=str); print(json.dumps(ck), "PASS", out["PASS"])
PYEOF
cat validation/logs/segment_continuation_check.out >> $LOG; echo "$(date -u +%FT%TZ) continuation smoke done" >> $LOG
