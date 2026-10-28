"""Rerun the independent rechecks and exact audits of the late global certificates in a restored layout and compare
each output with the shipped record.

Usage: python3 run_late_rechecks.py CERTIFICATES_DIR BASE_DIR

BASE_DIR must first be filled by restore_layout.py (S1_RESTART.md section 3a), and its last path component must be
named research: these programs address their inputs as <parent of BASE_DIR>/research/<part>/verification/... The runs:
the ten rechecks of P99, the two rechecks and the exact residual algebra audit of P101, the three rechecks and the
third-derivative algebra audit of P104, the consolidation of P95 (104 hash and completion checks), the contract audit
of P105 (47 exact checks) and the seven independent rechecks of the d2 covers of P95 (three matrix groups and four norm
groups, 640 bits). Each program writes its record next to itself in BASE_DIR (the two audits hash the shipped P95
rechecks and therefore run before the rechecks rewrite them), so use a fresh restore. A record is compared with the shipped one without its time stamps and elapsed
times; for the P95 rechecks only the verdict, the leaf count and the rows of leaf bounds are compared (two shipped
rechecks were produced in resumable chunks and carry bookkeeping fields). About 28 minutes on one core.
"""
import json, subprocess, sys, time
from pathlib import Path

cert, base = Path(sys.argv[1]), Path(sys.argv[2])
assert base.name == "research", "BASE_DIR must be named research"
PY = sys.executable
CORE = ("all_pass", "leaves", "rows")
jobs = []
for n in ["A_global", "rho_scaled_global", "M_r1e4", "B1_r1e4", "B2_r1e4", "B3_r1e4", "M_r1e6", "B1_r1e6", "B2_r1e6",
          "B3_r1e6"]:
    jobs.append(("P99_original_global_signs", "99_original_global_signs", "recheck.py", n + ".json", n + ".recheck.json", None))
for n in ["bound_0243535", "bound_0244"]:
    jobs.append(("P101_directed_far_residual", "101_directed_far_residual", "recheck.py", n + ".json", n + ".recheck.json", None))
jobs.append(("P101_directed_far_residual", "101_directed_far_residual", "audit_algebra.py", None, "algebra_audit.json", None))
for n in ["Drho", "Du", "u"]:
    jobs.append(("P104_original_decay_recomputation", "104_original_decay_recomputation", "recheck.py", n, n + ".recheck.json", None))
jobs.append(("P104_original_decay_recomputation", "104_original_decay_recomputation", "audit_algebra.py", None, "algebra.json", None))
# the two audits hash the shipped P95 rechecks, so they run before the rechecks rewrite them
jobs.append(("P95_refit_global_hypotheses", "95_refit_global_hypotheses", "consolidate.py", None, "audit_complete.json", None))
jobs.append(("P105_refit_reference_contract", "105_refit_reference_contract", "audit.py", None, "audit.json", None))
for g in ["M", "M1", "M2"]:
    jobs.append(("P95_refit_global_hypotheses", "95_refit_global_hypotheses", "recheck_fast.py", f"nb_d2_exact.{g}.correlated.json",
                 f"nb_d2_exact.{g}.correlated.recheck.json", CORE))
for g in ["u", "fourth", "D2u", "D2rho"]:
    jobs.append(("P95_refit_global_hypotheses", "95_refit_global_hypotheses", "recheck_norms.py", f"nb_d2_exact.{g}.correlated.json",
                 f"nb_d2_exact.{g}.correlated.recheck.json", CORE))

def strip(x):
    if isinstance(x, dict):
        return {k: strip(v) for k, v in x.items() if k not in ("utc", "seconds")}
    if isinstance(x, list):
        return [strip(v) for v in x]
    return x


bad = 0
for folder, topic, prog, arg, out, keys in jobs:
    d = base / topic / "verification"
    t = time.monotonic()
    r = subprocess.run([PY, str(d / prog)] + ([arg] if arg else []), capture_output=True, text=True, timeout=1200)
    if r.returncode == 0:
        a, b = strip(json.loads((d / out).read_text())), strip(json.loads((cert / folder / out).read_text()))
        ks = keys or tuple(set(a) | set(b))
        diff = sorted(k for k in ks if a.get(k) != b.get(k))
    else:
        diff = ["exit status %d: %s" % (r.returncode, r.stderr[-300:])]
    bad += bool(diff)
    print(f"{folder:34s} {prog:17s} {arg or '':36s} {time.monotonic() - t:7.1f} s  "
          f"{'same' if not diff else 'DIFFERS ' + ' '.join(diff)}", flush=True)
print(f"{len(jobs)} runs, {bad} not reproduced")
sys.exit(1 if bad else 0)
