#!/bin/bash
# D6FP G7 folded into the lagJ smoke (lead 02:48:22Z item 5; SPEC v1.10 3.5 (b)). Usage: validation/lagj_g7_driver.sh <run_dir> <worker_pid> <core>
# v2 (2026-10-29T04:58Z): FALLBACK_ITERS (default 8): if no reused-J step is accepted within that many iterations, the kill follows the next checkpoint after any accepted step.
# Waits for the first ACCEPTED step taken with a reused J (LM log line "acc(" with "tjac 0.0s") and for the next "checkpoint at start" line after it,
# then SIGKILLs the worker, keeps checkpoint_at_kill.pt, relaunches the worker with the production resume path (same job.json and run directory, same
# core, one thread), waits for it to finish and writes validation/lagj_g7_check.json with: checkpoint iterate hash vs the record at the kill point,
# resume lines, J refreshed on resume (first resumed record J_fresh, J_age 0), lam, iteration counter, geometry base, RNG state restored, and the
# ledger rows (kind resume). Log: validation/logs/lagj_g7_driver.log
ROOT=$(cd "$(dirname "$0")/.." && pwd); cd "$ROOT"; RUN=$1; PID=$2; CORE=${3:-32}; DEV=${4:-}; LOG=validation/logs/lagj_g7_driver.log   # DEV: CUDA_VISIBLE_DEVICES for the relaunch (empty = CPU)
PY=python3
echo "$(date -u +%FT%TZ) G7/lagJ driver: run $RUN pid $PID core $CORE" >> $LOG
trig=0; nck0=0
for i in $(seq 1 4320); do          # up to 6 h
  if ! kill -0 $PID 2>/dev/null; then echo "$(date -u +%FT%TZ) worker exited before a reused-J accepted step was seen; no kill" >> $LOG; exit 2; fi
  if [ $trig = 0 ]; then
    if grep -E "LM it .* acc\(.*tjac 0\.0s" $RUN/worker.log >/dev/null 2>&1; then
      trig=1; nck0=$(grep -c "checkpoint at start" $RUN/worker.log); echo "$(date -u +%FT%TZ) reused-J accepted step seen: $(grep -E 'LM it .* acc\(.*tjac 0\.0s' $RUN/worker.log | head -1 | cut -c1-160); checkpoints so far $nck0" >> $LOG
    elif [ "$(grep -c 'LM it ' $RUN/worker.log 2>/dev/null)" -ge "${FALLBACK_ITERS:-8}" ] && grep -E "LM it .* acc\(" $RUN/worker.log >/dev/null 2>&1; then
      trig=1; nck0=$(grep -c "checkpoint at start" $RUN/worker.log); echo "$(date -u +%FT%TZ) FALLBACK trigger (v2): no reused-J step was accepted in the first ${FALLBACK_ITERS:-8} iterations (every stale-J trial was rejected and J refreshed); killing after the next checkpoint following an accepted step; checkpoints so far $nck0" >> $LOG
    fi
  fi
  if [ $trig = 1 ]; then
    nck=$(grep -c "checkpoint at start" $RUN/worker.log)
    if [ "$nck" -gt "$nck0" ]; then sleep 4; break; fi
  fi
  sleep 5
done
[ $trig = 1 ] || { echo "$(date -u +%FT%TZ) timeout waiting for the trigger" >> $LOG; exit 3; }
echo "$(date -u +%FT%TZ) SIGKILL pid $PID after checkpoint: $(grep 'checkpoint at start' $RUN/worker.log | tail -1)" >> $LOG
kill -9 $PID; sleep 2; cp $RUN/checkpoint.pt $RUN/checkpoint_at_kill.pt
grep -E "LM it" $RUN/worker.log | tail -3 | cut -c1-200 >> $LOG
echo "$(date -u +%FT%TZ) relaunch (production resume path)" >> $LOG
CUDA_VISIBLE_DEVICES=$DEV OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 10 taskset -c $CORE $PY scripts/worker_d6.py $RUN/job.json $RUN > $RUN/stdout_run2.log 2>&1 < /dev/null
echo "$(date -u +%FT%TZ) resumed run exit $?" >> $LOG
$PY - "$RUN" <<'PYEOF' > validation/logs/lagj_g7_check.out 2>&1
import sys, torch, json, os, hashlib, glob, re
run = sys.argv[1]; out = dict(run=run)
ck = torch.load(os.path.join(run, "checkpoint_at_kill.pt"), map_location="cpu", weights_only=False); cur = ck["current"]
zsha = hashlib.sha256(cur["z_opt"].numpy().tobytes()).hexdigest()
out["checkpoint"] = dict(it=cur["it"], lam=cur["lam"], geometry_base=cur.get("geometry_base"), z_opt_sha256=zsha, rng_state_present=("rng_state" in cur), history_len=len(cur.get("history", [])))
log = open(os.path.join(run, "worker.log")).read().splitlines()
out["resume_lines"] = [l for l in log if ("RESUME from checkpoint" in l or "resuming at iteration" in l)]
fins = sorted(glob.glob(os.path.join(run, "starts", "start_000*.pt")))
if fins:
    fin = torch.load(fins[-1], map_location="cpu", weights_only=False); h = fin.get("history") or []
    out["final"] = dict(file=os.path.basename(fins[-1]), iterations=fin.get("iterations"), status=fin.get("status"), n_records=len(h))
    pre = [r for r in h if r["it"] == cur["it"] - 1]; post = [r for r in h if r["it"] == cur["it"]]
    out["record_at_checkpoint_iterate"] = ({k: pre[0].get(k) for k in ("it", "cost", "lam", "z_sha256_12", "J_age", "J_fresh", "rho")} if pre else None)
    out["first_resumed_record"] = ({k: post[0].get(k) for k in ("it", "cost", "lam", "z_sha256_12", "J_age", "J_fresh", "rho", "accepted")} if post else None)
    out["checks"] = dict(z_bitwise=(bool(pre) and pre[0].get("z_sha256_12") == zsha[:12]), lam_continuity=(bool(pre) and abs(pre[0]["lam"] - cur["lam"]) <= 1e-15 * max(1.0, abs(cur["lam"]))),
                         iteration_counter=(bool(post) and post[0]["it"] == cur["it"]), J_refreshed_on_resume=(bool(post) and bool(post[0].get("J_fresh")) and int(post[0].get("J_age", 0)) == 0),
                         geometry_same=(fin.get("d6fp", {}).get("geometry_base") == cur.get("geometry_base")) if isinstance(fin.get("d6fp"), dict) else None)
    out["costs"] = [r["cost"] for r in h]; out["J_ages"] = [r.get("J_age") for r in h]; out["rhos"] = [r.get("rho") for r in h]
    d6 = fin.get("d6fp") or {}
    out["record_fields"] = {k: d6.get(k) for k in ("battery_set", "t_battery_s", "battery_cpu_time_s", "lag_jacobian", "precision_mode") if k in d6}
    cg = [r.get("complete_gradient") for r in h if r.get("complete_gradient")]
    out["complete_gradient_records"] = len(cg); out["g_param_phys_example"] = next((c.get("g_param_phys") for c in cg if isinstance(c, dict) and c.get("g_param_phys")), None)
    out["params_prestep_present"] = any("params_prestep" in r for r in h)
# the initial O1 of the resumed LM run vs the cost at the checkpoint iterate (1e-12 relative), from the resumed log if printed
init = [l for l in log if "LM initial cost" in l]
try:
    c0 = [float(re.search(r"LM initial cost ([0-9.eE+-]+)", l).group(1)) for l in init]
    out["initial_costs"] = c0
    if len(c0) >= 2 and out.get("record_at_checkpoint_iterate"):
        cpre = out["record_at_checkpoint_iterate"]["cost"]; out["checks"]["O1_at_resume_point_rel_diff"] = abs(c0[-1] - cpre) / max(abs(cpre), 1e-300); out["checks"]["O1_within_1e-12"] = out["checks"]["O1_at_resume_point_rel_diff"] <= 1e-12
except Exception as e:
    out["initial_cost_parse_error"] = repr(e)
out["lm_start_lines"] = init[-2:]
led = [json.loads(l) for l in open(os.path.join(os.path.dirname(os.path.dirname(run)), "status", "ledger.jsonl")) if os.path.basename(run) in l]
out["ledger_resume_rows"] = [r for r in led if r.get("kind") == "resume"]
json.dump(out, open(os.path.join(os.path.dirname(os.path.dirname(run)), "validation", "lagj_g7_check.json"), "w"), indent=1, default=str)
print(json.dumps(out.get("checks")), out.get("record_fields"), out.get("resume_lines"))
PYEOF
cat validation/logs/lagj_g7_check.out >> $LOG; echo "$(date -u +%FT%TZ) G7/lagJ driver done" >> $LOG
