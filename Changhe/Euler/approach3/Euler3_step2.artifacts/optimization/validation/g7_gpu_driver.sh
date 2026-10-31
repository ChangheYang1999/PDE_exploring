#!/bin/bash
# D6FP G7 on the GPU (SPEC v1.13 3.6 (d)), snapshot gpu_v1, production configuration (dd_fp64jac, lagged Jacobian OFF), start S01.
# Usage: validation/g7_gpu_driver.sh <gpu index> <core> <tag>   e.g. validation/g7_gpu_driver.sh 6 32 g7_gpu_v1
# v2 2026-10-29T05:47Z (lead 05:41Z): trigger baseline by log line order; checker asserts the kill checkpoint is the first after the second accepted step and compares grad_every.
# Launches the worker (label SMOKE, max_iter 8, checkpoint every 60 s), SIGKILLs it after the first checkpoint that follows the SECOND accepted step,
# resumes it by the production path on the same GPU, waits for the end (at least three further accepted steps), and writes validation/<tag>_check.json:
# the vector at the first resumed objective/Jacobian (the first resumed linearization record's z_opt, and the resume log line) byte-identical to the saved
# vector; damping; cumulative counters and the complete-gradient schedule; histories; RNG state hash and quadrature layout before the first resumed trial;
# O1 at the resume point within 1e-12 relative; the ledger interruption; the first resumed record identified by its cumulative iteration (it_cum).
ROOT=$(cd "$(dirname "$0")/.." && pwd); cd "$ROOT"; GPU=$1; CORE=${2:-32}; TAG=${3:-g7_gpu_v1}; LOG=validation/logs/${TAG}_driver.log
PY=python3
echo "$(date -u +%FT%TZ) G7 driver: GPU $GPU core $CORE tag $TAG" >> $LOG
CORES=$CORE bash scripts/run_smoke_job.sh $GPU $TAG --start starts/S01_nest6_cl0.45_om1.0_p0.pt --max_iter 8 --ckpt_interval 60 --time_limit 3600 --extra '{"complete_gradient_every": 4}' \
   --note "G7 on gpu_v1 (SPEC v1.13 3.6 (d)): production configuration (dd_fp64jac, lagged Jacobian off), S01; SIGKILL after the first checkpoint following the second accepted step, resume by the production path; disposable SMOKE" >> $LOG 2>&1
RUN=$(ls -d runs/${TAG}_* | head -1); PID=$(pgrep -f "worker_d6.py $RUN/job.json" | head -1)
echo "$(date -u +%FT%TZ) run $RUN pid $PID" >> $LOG
# v2 (lead 05:41Z item 1): the baseline is the number of "checkpoint at start" lines that come BEFORE the second accepted-step line in worker.log, by line
# order; the kill follows the first checkpoint line after it (the first checkpoint following the second accepted step, SPEC 3.6 (d)).
trig=0; nck0=0
for i in $(seq 1 720); do
  if ! kill -0 $PID 2>/dev/null; then echo "$(date -u +%FT%TZ) worker exited before the trigger" >> $LOG; exit 2; fi
  nacc=$(grep -cE 'LM it .* acc\(' $RUN/worker.log 2>/dev/null); nacc=${nacc:-0}
  if [ $trig = 0 ] && [ "$nacc" -ge 2 ]; then
    L2=$(grep -nE 'LM it .* acc\(' $RUN/worker.log | sed -n 2p | cut -d: -f1)                      # line number of the second accepted-step line
    nck0=$(head -n $L2 $RUN/worker.log | grep -c "checkpoint at start"); trig=1
    echo "$(date -u +%FT%TZ) second accepted step at log line $L2: $(sed -n ${L2}p $RUN/worker.log | cut -c1-120); checkpoint lines before it: $nck0" >> $LOG
  fi
  if [ $trig = 1 ] && [ "$(grep -c 'checkpoint at start' $RUN/worker.log)" -gt "$nck0" ]; then break; fi
  sleep 2
done
TARGET=$(grep "checkpoint at start" $RUN/worker.log | sed -n "$((nck0 + 1))p")
echo "$(date -u +%FT%TZ) SIGKILL pid $PID after the first checkpoint following the second accepted step: $TARGET" >> $LOG
kill -9 $PID; sleep 2; cp $RUN/checkpoint.pt $RUN/checkpoint_at_kill.pt
NCK_AT_KILL=$(grep -c "checkpoint at start" $RUN/worker.log); echo "$(date -u +%FT%TZ) checkpoint lines at the kill: $NCK_AT_KILL (expected $((nck0 + 1)))" >> $LOG
echo "$TARGET" > $RUN/target_checkpoint_line.txt; echo "$((nck0 + 1))" > $RUN/target_checkpoint_index.txt
echo "$(date -u +%FT%TZ) relaunch (production resume path, GPU $GPU)" >> $LOG
CUDA_VISIBLE_DEVICES=$GPU OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 10 taskset -c $CORE $PY scripts/worker_d6.py $RUN/job.json $RUN > $RUN/stdout_run2.log 2>&1 < /dev/null
echo "$(date -u +%FT%TZ) resumed run exit $?" >> $LOG
$PY - "$RUN" "$TAG" <<'PYEOF' > validation/logs/${TAG}_check.out 2>&1
import sys, torch, json, os, hashlib, glob, re, numpy as np
run, tag = sys.argv[1], sys.argv[2]; out = dict(run=run, tag=tag)
ck = torch.load(os.path.join(run, "checkpoint_at_kill.pt"), map_location="cpu", weights_only=False); cur = ck["current"]
zsha = hashlib.sha256(cur["z_opt"].numpy().tobytes()).hexdigest()
out["checkpoint"] = dict(it=cur["it"], lam=cur["lam"], geometry_base=cur.get("geometry_base"), counters=cur.get("counters"), grad_every=cur.get("grad_every"), z_opt_sha256=zsha,
                         z_opt_sha256_saved=cur.get("z_opt_sha256"), rng_state_sha256_saved=cur.get("rng_state_sha256"), history_len=len(cur.get("history", [])), pre_cost=(cur["history"][-1]["cost"] if cur.get("history") else None))
log = open(os.path.join(run, "worker.log")).read().splitlines()
res = [l for l in log if "resuming at iteration" in l]; out["resume_lines"] = [l for l in log if ("RESUME from checkpoint" in l or "resuming at iteration" in l or "LM counters restored" in l)]
m = re.search(r"rng_state_sha256 ([0-9a-f]+); resumed vector sha256 ([0-9a-f]+)", res[-1]) if res else None
out["resume_rng_sha256"] = m.group(1) if m else None; out["resume_vector_sha256"] = m.group(2) if m else None
mg = re.search(r"geometry base (\{.*?\}); counters", res[-1]) if res else None; out["resume_geometry_base_str"] = mg.group(1) if mg else None
init = [l for l in log if "LM initial cost" in l]; costs0 = [float(re.search(r"LM initial cost ([0-9.eE+-]+)", l).group(1)) for l in init]; out["initial_costs"] = costs0
fins = sorted(glob.glob(os.path.join(run, "starts", "start_000*.pt"))); checks = {}
if fins:
    fin = torch.load(fins[-1], map_location="cpu", weights_only=False); h = fin.get("history") or []
    out["final"] = dict(file=os.path.basename(fins[-1]), status=fin.get("status"), n_records=len(h), iterations=fin.get("iterations"))
    pre = [r for r in h if r.get("it_cum") == cur["it"] - 1]; post = [r for r in h if r.get("it_cum") == cur["it"]]
    out["record_at_checkpoint_iterate"] = ({k: pre[0].get(k) for k in ("it", "it_cum", "cost", "lam", "z_sha256_12", "counters", "accepted")} if pre else None)
    out["first_resumed_record"] = ({k: post[0].get(k) for k in ("it", "it_cum", "cost", "lam", "z_sha256_12", "counters", "accepted", "n_trials", "t_jac")} if post else None)
    after = [r for r in h if r.get("it_cum", -1) >= cur["it"]]
    out["accepted_after_resume"] = sum(1 for r in after if r.get("accepted"))
    # linearization record of the first resumed iteration: full vector bytes
    lin = os.path.join(run, f"linearization_{cur['it']:05d}.npz"); out["first_resumed_linearization_record"] = os.path.basename(lin) if os.path.exists(lin) else None
    if os.path.exists(lin):
        zl = np.load(lin)["z_opt"]; out["linearization_z_sha256"] = hashlib.sha256(np.ascontiguousarray(zl).tobytes()).hexdigest()
    c_pre = pre[0]["counters"] if pre and pre[0].get("counters") else None; c_post = post[0]["counters"] if post and post[0].get("counters") else None
    checks["vector_bytes_first_resumed_linearization_equals_checkpoint"] = (out.get("linearization_z_sha256") == zsha) if out.get("linearization_z_sha256") else None
    checks["vector_bytes_resume_log_equals_checkpoint"] = (out["resume_vector_sha256"] == zsha) if out["resume_vector_sha256"] else None
    checks["damping_lam_continuity"] = (abs(float(re.search(r"with lam ([0-9.eE+-]+)", res[-1]).group(1)) - cur["lam"]) <= 1e-15 * max(1.0, abs(cur["lam"]))) if res else None
    checks["counters_continuity"] = (c_pre is not None and c_post is not None and cur.get("counters") == c_pre and c_post["n_acc"] == c_pre["n_acc"] + int(bool(post[0]["accepted"])) and c_post["n_rej"] >= c_pre["n_rej"])
    checks["gradient_schedule_continuity"] = all(("complete_gradient" in r) == bool(r.get("accepted")) for r in h if r.get("accepted")) if h else None   # lagJ off: every accepted (fresh-J) step carries the gradient
    checks["history_continuity"] = (len(h) == len(cur["history"]) + len(after)) and all(a.get("it_cum") == b.get("it_cum") for a, b in zip(h[: len(cur["history"])], cur["history"]))
    checks["rng_state_before_first_resumed_trial"] = (out["resume_rng_sha256"] == cur.get("rng_state_sha256")) if out["resume_rng_sha256"] and cur.get("rng_state_sha256") else None
    checks["quadrature_layout_same"] = (out["resume_geometry_base_str"] == str(cur.get("geometry_base"))) if out["resume_geometry_base_str"] else None
    checks["O1_at_resume_point_within_1e-12"] = (abs(costs0[-1] - pre[0]["cost"]) / abs(pre[0]["cost"]) <= 1e-12) if (len(costs0) >= 2 and pre) else None
    out["O1_at_resume_point_rel_diff"] = (abs(costs0[-1] - pre[0]["cost"]) / abs(pre[0]["cost"])) if (len(costs0) >= 2 and pre) else None
    checks["at_least_three_accepted_after_resume"] = out["accepted_after_resume"] >= 3
# (lead 05:41Z (b)) eligible checkpoints: every "checkpoint at start" line with its cumulative iteration (the checkpoint stores it + 1); the kill checkpoint must be the
# first one after the second accepted-step line (by log line order), and no later checkpoint may have been written before the kill landed
lines = open(os.path.join(run, "worker.log")).read().splitlines()
acc_idx = [i for i, l in enumerate(lines) if re.search(r"LM it .* acc\(", l)]
ck_lines = [(i, int(re.search(r" it (\d+) \(", l).group(1)) + 1) for i, l in enumerate(lines) if "checkpoint at start" in l]
first_run_ck = [(i, it) for (i, it) in ck_lines if not any("RESUME from checkpoint" in l for l in lines[:i])]   # checkpoints of the first (killed) run only
out["eligible_checkpoints_first_run"] = [dict(log_line=i + 1, cumulative_it=it) for (i, it) in first_run_ck]
second_acc_line = acc_idx[1] if len(acc_idx) >= 2 else None
after = [(i, it) for (i, it) in first_run_ck if second_acc_line is not None and i > second_acc_line]
out["second_accepted_step_log_line"] = (second_acc_line + 1) if second_acc_line is not None else None
out["first_checkpoint_after_second_accepted"] = (dict(log_line=after[0][0] + 1, cumulative_it=after[0][1]) if after else None)
out["checkpoint_at_kill_sha256"] = hashlib.sha256(open(os.path.join(run, "checkpoint_at_kill.pt"), "rb").read()).hexdigest()
checks["kill_checkpoint_is_first_after_second_accepted_step"] = bool(after) and cur["it"] == after[0][1] and len(after) == 1
job = json.load(open(os.path.join(run, "job.json"))); ge_cfg = int(job["config"].get("complete_gradient_every", 1) or 1)
out["grad_every"] = dict(checkpoint=cur.get("grad_every"), cfg=ge_cfg); checks["grad_every_checkpoint_equals_cfg"] = (cur.get("grad_every") == ge_cfg)
# (SPEC v1.15 3.6 (i) (ii)) the pre-kill part is a fresh start with the configuration of the 05:21:55Z gpu_v1 run: same counts and costs (1e-10) at the same cumulative iterations
REF = os.environ.get("G7_REFERENCE_RUN", "runs/g7_gpu_v1_L6_cl0.4500_om1.0000_free")
try:
    rf = sorted(glob.glob(os.path.join(REF, "starts", "start_000*.pt")))[-1]; rh = torch.load(rf, map_location="cpu", weights_only=False).get("history") or []
    pre_recs = cur.get("history") or []
    cmp = []
    for a in pre_recs:
        b = next((r for r in rh if r.get("it_cum") == a.get("it_cum")), None)
        if b is not None:
            cmp.append(dict(it_cum=a.get("it_cum"), cost_rerun=a["cost"], cost_ref=b["cost"], rel_diff=abs(a["cost"] - b["cost"]) / abs(b["cost"]), trials=(a.get("n_trials"), b.get("n_trials")), accepted=(a.get("accepted"), b.get("accepted"))))
    out["fresh_start_equivalence_vs_reference"] = dict(reference=REF, n_compared=len(cmp), rows=cmp, max_rel_cost_diff=(max(c["rel_diff"] for c in cmp) if cmp else None))
    checks["pre_kill_reproduces_reference_counts_and_costs_1e-10"] = bool(cmp) and len(cmp) == len(pre_recs) and all(c["rel_diff"] <= 1e-10 and c["trials"][0] == c["trials"][1] and c["accepted"][0] == c["accepted"][1] for c in cmp)
except Exception as e:
    out["fresh_start_equivalence_vs_reference"] = dict(error=repr(e)); checks["pre_kill_reproduces_reference_counts_and_costs_1e-10"] = None
job_cfg = json.load(open(os.path.join(run, "job.json")))["config"]
out["config_sha256_job_json"] = hashlib.sha256(json.dumps(job_cfg, sort_keys=True).encode()).hexdigest()
out["checkpoint_versions"] = {k: str(v) for k, v in (ck.get("versions") or {}).items()} if isinstance(ck.get("versions"), dict) else None
led = [json.loads(l) for l in open(os.path.join(os.path.dirname(os.path.dirname(run)), "status", "ledger.jsonl")) if os.path.basename(run) in l]
out["config_sha256_ledger_launch"] = [r.get("config_sha256") for r in led if r.get("kind") == "job_code_versions"]
out["ledger_resume_rows"] = [r for r in led if r.get("kind") == "resume"]; checks["ledger_shows_interruption"] = len(out["ledger_resume_rows"]) >= 1
out["checks"] = checks; out["G7_PASS"] = all(v is True for v in checks.values())
json.dump(out, open(os.path.join(os.path.dirname(os.path.dirname(run)), "validation", f"{tag}_check.json"), "w"), indent=1, default=str)
print(json.dumps(checks), "G7_PASS", out["G7_PASS"])
PYEOF
cat validation/logs/${TAG}_check.out >> $LOG; echo "$(date -u +%FT%TZ) G7 driver done" >> $LOG
