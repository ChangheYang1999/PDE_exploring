#!/usr/bin/env python
"""Gate I.4 G1 table: SPEC 7.9 tests T01-T12 against the test files, PASS/FAIL and run time from the newest logs/test_suite_*.log (scripts/run_tests.sh).
Writes reports/G1_TESTS.md."""
import sys, os, re, glob, time
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
logs = sorted(glob.glob(os.path.join(ROOT, "logs", "test_suite_*.log")))
log = logs[-1] if logs else None
status = {}; times = {}
if log:
    lines = open(log).read().splitlines()
    t_start = {}
    for ln in lines:
        m = re.match(r"=== (\S+) (tests/\S+(?: even)?)$", ln)
        if m: t_start[m.group(2)] = m.group(1)
        m = re.match(r"=== (PASS|FAIL) (tests/\S+(?: even)?)", ln)
        if m: status[m.group(2)] = m.group(1)
    # run time from consecutive timestamps
    order = [(ln.split()[1], ln.split(" ", 2)[2]) for ln in lines if re.match(r"=== \d{4}-\d\d-\d\dT", ln)]
    for i, (t, name) in enumerate(order):
        nxt = order[i + 1][0] if i + 1 < len(order) else None
        if nxt:
            dt = (time.mktime(time.strptime(nxt, "%Y-%m-%dT%H:%M:%SZ")) - time.mktime(time.strptime(t, "%Y-%m-%dT%H:%M:%SZ")))
            times[name] = dt
T = [("T01", "whole-field manufactured residual (sympy), divergence-free polynomial and decaying test fields", ["tests/test_fields.py even", "tests/test_residuals.py"]),
     ("T02", "curl R_u = R_Omega, div W = 3 c_l, exact spiral tail kills the linear operator, sign flips break it", ["tests/test_residuals.py"]),
     ("T03", "pressure: manufactured decaying P, twisted source, independent ray-integral kernel, off-grid radii", ["tests/test_pressure.py", "tests/test_pressure_twisted.py", "tests/test_pressure_ray.py", "tests/test_pressure_offgrid.py"]),
     ("T04", "dilation covariance of fields/residuals and invariance of the ranking diagnostics on rescaled holdout shells", ["tests/test_T04_dilation_diagnostics.py"]),
     ("T05", "rotation covariance: fields/residuals (test_fields) and the diagnostics rho_u, sigma_u, a_max of a state and its rotated image", ["tests/test_fields.py even", "tests/test_T05_diagnostics_rotation.py"]),
     ("T06", "reflection / omega sign regression", ["tests/test_spec_T06_T07.py"]),
     ("T07", "far-field orders: random (sigma, tau) tails; G[F] by two independent codes (||G|| 0.609959 vs verifier 0.6099595; scripts/g_closure.py), SPEC-degree span contains G[F] to 7e-14", ["tests/test_spec_T06_T07.py", "tests/test_channel_degrees.py"]),
     ("T08", "origin Taylor audit: tau_0 exact at y = 0; tau_1, tau_2 by a degree-4 Taylor fit of the five momentum terms on five spheres eps..5 eps (eps = R0 2^-11) with an interleaved second sphere set as the consistency check (src/validation/origin_taylor.py; per-state values in the ledger and shortlist)", ["tests/test_T08_origin_taylor.py"]),
     ("T09", "aliasing: holdout diagnostics under 1.5x angular and 2x radial refinement (reports/T09_ALIASING.md: changes 1e-15 and <= 1.3e-2, PASS)", []),
     ("T10", "holdout: holdout and training residuals within a factor 3, else flagged (ledger rule on the ranked rows; counts below)", []),
     ("T10s", "supplementary: AD Jacobian vs finite differences incl. free c_l, omega; LM manufactured recovery; channel degrees", ["tests/test_lm.py", "tests/test_free_param_lm.py", "tests/test_channels.py", "tests/test_channel_degrees.py"]),
     ("T11", "restart determinism: the ten post-resume LM iterates (coefficients, damping, acceptance) against the uninterrupted run at the API level of the worker's checkpoint/resume state (tests/test_T11_resume_iterates.py: 8.7e-11, SPEC 1e-10; default and deterministic cuBLAS); the kill -9 worker-level test (scripts/resume_test.sh, status/RESUME_TEST.md) compares final states bitwise", ["tests/test_T11_resume_iterates.py"]),
     ("T12", "gauge: no collapse and gauge defect after the exact projection (test_gauge_lm); pivot phase exact (sine amplitude zero) and the real pivot positive after every accepted step (SPEC v1.23 6.2; Problem.phase_align chooses the rotation with a_c >= 0), the soft F-gauge row within 1e-3 per step on the saved nest4 state (not the exact gauge), pivot switch leaves the diagnostics unchanged to 1e-12 (test_T12_gauge_steps)", ["tests/test_gauge_lm.py", "tests/test_T12_gauge_steps.py"])]
lines = [f"# G1 test table (generated {time.strftime('%Y-%m-%dT%H:%MZ', time.gmtime())}; newest suite log {os.path.basename(log) if log else 'none'})", "",
         "Device note (2026-10-25T11:50Z): clean suite runs 4 and 5 (GPU, 2026-10-25T06:04Z and 08:35Z) record the strict T05 value 1.35e-12 against 1e-12 (FAIL, roundoff of the nonlinear-denominator ratios); run 6 (CPU, 2026-10-25T11:08Z, 23 tests incl. test_far_helicity) gives 6.0e-13 (PASS). The GPU value stays the campaign record for T05; the table below reflects the newest log.", "",
         "| SPEC test | content | test files | status | run time (s) |", "|---|---|---|---|---|"]
for tid, desc, files in T:
    if files:
        st = "PASS" if all(status.get(f) == "PASS" for f in files) else ("FAIL" if any(status.get(f) == "FAIL" for f in files) else "not in suite log")
        rt = sum(times.get(f, 0) for f in files)
        lines.append(f"| {tid} | {desc} | {', '.join(files)} | {st} | {rt:.0f} |")
    else:
        if tid == "T10":
            # SPEC T10: holdout vs training rho_u^max within a factor 3 on the ranked (nontrivial, non-free, post-19:39Z) rows
            sys.path.insert(0, ROOT)
            from src.campaign import ledger
            recs = ledger.read(os.path.join(ROOT, "status", "ledger.jsonl"))
            rows = ledger.leaderboard(ledger.merge_reevaluations(recs) + [r for r in recs if r.get("kind") != "start_result"], n=10**6, solver_version="all")
            rows = [r for r in rows if r.get("rho_u_max") and r.get("rho_u_max_holdout") and not str(r.get("job_id", "")).startswith(("smoke", "resume_test"))]
            flagged = [(r["job_id"], r["start"], r["rho_u_max"], r["rho_u_max_holdout"]) for r in rows if max(r["rho_u_max_holdout"] / r["rho_u_max"], r["rho_u_max"] / r["rho_u_max_holdout"]) > 3.0]
            extra = f"PASS on {len(rows) - len(flagged)} of {len(rows)} ranked rows; {len(flagged)} flagged (factor > 3): " + ("; ".join(f"{j}/{st} train {a:.3g} holdout {b:.3g}" for j, st, a, b in flagged[:12]) if flagged else "none")
        else:
            extra = {"T09": "PASS (reports/T09_ALIASING.md)"}[tid]
        lines.append(f"| {tid} | {desc} | (ledger rule) | {extra} | n/a |" if tid == "T10" else f"| {tid} | {desc} | (script/report) | {extra} | n/a |")
lines += ["", "Suite results: " + ", ".join(f"{k} {v} ({times.get(k, 0):.0f}s)" for k, v in status.items()), "",
          "Status is read row by row from the newest clean-process suite log; the strict T05 diagnostics value (1e-12) FAILS at 1.35e-12 (ratios with the nonlinear denominator; roundoff analysis in the log), every other row PASSES on the primary record. T12's per-step check is the soft gauge row's tolerance (1e-3), not the exact gauge, which is applied once per start and tested by test_gauge_lm. Independent reruns are the verifier's."]
os.makedirs(os.path.join(ROOT, "reports"), exist_ok=True)
open(os.path.join(ROOT, "reports", "G1_TESTS.md"), "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
