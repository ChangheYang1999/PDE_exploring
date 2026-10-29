"""Resource totals from the run ledger (result.json of finished runs): GPU-slot hours (device cuda), CPU-worker hours (device cpu), counts,
split at the GPU revocation (00:58:14Z) and restoration (04:59:18Z). Usage: python3 scripts/resource_totals.py"""
import json, glob, os
import re as _re
gpu1 = gpu2 = cpu = 0.0; n_gpu1 = n_gpu2 = n_cpu = 0; s3 = []; cpu_prev = 0.0; n_cpu_resumed = 0; cpu_val = 0.0
for f in glob.glob(os.path.join(os.path.dirname(__file__), "..", "runs", "*", "result.json")):
    r = json.load(open(f)); e = r.get("elapsed_s") or 0; fin = r.get("finished") or ""
    vf = os.path.join(os.path.dirname(f), "validation.json")           # elapsed_s of result.json is captured BEFORE the final validation
    ve = (json.load(open(vf)).get("elapsed_s") or 0.0) if os.path.exists(vf) else 0.0
    if fin > "2026-10-29T11:40:09Z":          # Stage III: no optimization; only protected test runs after the freeze (reported separately)
        s3.append((os.path.basename(os.path.dirname(f)), fin, e, ve)); continue
    if r.get("device", "cuda") == "cpu" or str(r.get("gpu") or "").startswith("cpu"):
        cpu += e; n_cpu += 1; cpu_val += ve
        # elapsed_s of a resumed job = earlier segments (from the checkpoint) + the last segment; the six jobs resumed on CPU at 01:06:44Z
        # and 01:21:59Z carry their earlier GPU segments; the first "resumed from checkpoint ... elapsed Ns" marker of log.txt gives them
        lg = os.path.join(os.path.dirname(f), "log.txt")
        if os.path.exists(lg):
            m = _re.search(r"resumed from checkpoint: stage \d+ it \d+ cost \S+ elapsed (\d+)s", open(lg, errors="replace").read())
            if m: cpu_prev += float(m.group(1)); n_cpu_resumed += 1
    elif fin > "2026-10-29T04:59:18Z":
        gpu2 += e; n_gpu2 += 1
    else:
        gpu1 += e; n_gpu1 += 1
print(f"GPU phase 1 (to 00:58:14Z): {n_gpu1} finished runs, {gpu1/3600:.1f} GPU-slot hours (two slots per GPU)")
print(f"CPU-only phase (01:06:41Z to 04:59:18Z): {n_cpu} finished CPU runs, {cpu/3600:.1f} hours of cumulative job wall time of the {n_cpu} runs completed on CPU, including"
      f" earlier GPU segments of resumed jobs (sum of elapsed_s; one core each, nice 19; the {n_cpu_resumed} jobs resumed on CPU from GPU checkpoints contribute"
      f" {cpu_prev:.0f} s of earlier GPU segments, so the CPU-only part is approximately {(cpu-cpu_prev)/3600:.1f} hours of prevalidation elapsed wall time;"
      f" elapsed_s is captured before the final validation, and the {n_cpu} final validations add {cpu_val:.0f} s of wall time not included in these sums;"
      f" none of these counters is CPU consumption)")
print(f"GPU phase 2 (from 04:59:18Z): {n_gpu2} finished runs, {gpu2/3600:.1f} GPU-slot hours")
print("Stage III disposable resume-test runs after the 11:40:09Z freeze (no discovery or refinement optimization; the tests themselves perform LM iterations; GPU 0): "
      + (", ".join(f"{j} finished {fin}: prevalidation elapsed_s {e:.2f} s, final validation {ve:.2f} s" for j, fin, e, ve in s3) if s3 else "none")
      + "; the complete wrapper intervals are 291.6 s (12:03:17Z to 12:08:09Z) and 293.8 s (12:22:01Z to 12:26:55Z); no GPU kernel time was measured")
print("Frozen 11:40Z summary (docs/RESOURCE_TOTALS_frozen_1140.txt): 370 / 90 / 70 runs; the Stage III rerun of the resume test at 12:08Z overwrote the historical")
print("runs/zz_test_resume record of phase 1 (one disposable test run, part of the 787 s of the four test runs), so a recount of phase 1 now gives one run less.")
# nested closed-problem solves (external/t1nk2, two single-thread CPU runners): sum of (exit - invoke) over the bounded invocations in logs/t1nk2_*.log
import re, datetime
def ts(x): return datetime.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ")
tot = 0.0; n_inv = 0; first = None; last = None
for lf in sorted(glob.glob(os.path.join(os.path.dirname(__file__), "..", "logs", "t1nk2_*.log"))):
    inv = None
    for line in open(lf, errors="replace"):
        m = re.match(r"(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ) (invoke|exit)", line)
        if not m: continue
        t = ts(m.group(1))
        if m.group(2) == "invoke": inv = t; first = t if (first is None or t < first) else first
        elif inv is not None: tot += (t - inv).total_seconds(); n_inv += 1; last = t if (last is None or t > last) else last; inv = None
print(f"nested closed-problem solves (t1nk2, referee code, one core per invocation): {n_inv} bounded invocations, {tot:.0f} seconds ({tot/3600:.1f} hours) of summed invocation wall time; CPU consumption was not measured"
      + (f" ({first:%Y-%m-%dT%H:%M}Z to {last:%Y-%m-%dT%H:%M}Z)" if first and last else ""))
