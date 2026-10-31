#!/usr/bin/env python
"""D6FP: markdown report (SPEC 9, CPU variant after the GPU revocation of 2026-10-29T00:57:59Z) from validation/cpu_profile_S01.json
(written progressively by validation/cpu_profile_S01.py: the per-thread component table appears after each thread phase, the full-J and
projection entries at the end). Usage: python scripts/cpu_profile_report.py [json] [more json files for supplementary thread counts]."""
import json, sys, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
paths = sys.argv[1:] or [os.path.join(ROOT, "validation", "cpu_profile_S01.json")]
d = json.load(open(paths[0]))
threads = dict(d.get("threads", {}))
for p in paths[1:]:
    e = json.load(open(p))
    for k, v in e.get("threads", {}).items():
        threads[k + " (supplementary run %s)" % os.path.basename(p)] = v
def f(v):
    return "n/a" if v is None else f"{v['median']:.2f} s (min {v['min']:.2f}, max {v['max']:.2f}, n {v['n']})"
print(f"CPU timing of S01 (label VALIDATION; validation/cpu_profile_S01.py, started {d.get('started')}, cores {d.get('cores')}, start {d.get('start')}): "
      f"n_opt {d.get('n_opt')}, rows {d.get('n_rows')}, RSS after the build {d.get('rss_after_build_GB', float('nan')) * 1.024:.2f} GB (the record stores ru_maxrss KiB / 1e6; multiplied by 1.024 here, verifier remark 02:4xZ). Wall times (time.perf_counter; CPU "
      f"operations are synchronous), median of n samples (n per entry; the first run used 3 samples for the cheap items and 1 or 2 for the expensive "
      f"double-double items, as the verifier noted at 01:20Z). J_cw is timed on one chunk of 64 coefficient columns and extrapolated linearly to the 1469 columns.")
keys = ["residual_vector_wd_fp64", "objective_at_fp64", "trial_evaluation_fp64", "complete_gradient_fp64", "objective_at_dd", "trial_evaluation_dd", "complete_gradient_dd",
        "param_columns_fp64", "Jcw_chunk64_fp64", "param_columns_dd", "Jcw_chunk64_dd", "param_columns_dd_fp64tangent", "Jcw_chunk64_dd_fp64tangent", "param_columns_dd_fp64jac", "Jcw_chunk64_dd_fp64jac"]
cols = list(threads.keys())
print("\n| component | " + " | ".join(f"threads {c}" for c in cols) + " |\n|---|" + "---|" * len(cols))
for k in keys:
    row = []
    for c in cols:
        v = threads[c].get(k)
        s = f(v)
        if v is not None and "extrapolated_1469_columns" in v:
            s += f"; 1469 columns {v['extrapolated_1469_columns']:.0f} s"
        row.append(s)
    print(f"| {k} | " + " | ".join(row) + " |")
for k in ("full_Jcw_fp64_4threads", "normal_equations_4threads", "cholesky_solve_4threads", "normal_equations_1thread", "cholesky_solve_1thread"):
    if k in d:
        v = d[k]
        if "median" in v:
            print(f"- {k}: {f(v)}")
        else:
            print(f"- {k}: {v.get('seconds', float('nan')):.1f} s, shape {v.get('shape')}, peak RSS {v.get('rss_peak_GB', float('nan')) * 1.024:.2f} GB (ru_maxrss KiB x 1024)")
proj = d.get("projected_per_accepted_iteration")
if proj:
    print("\nProjected cost per accepted LM iteration (J_cw + parameter columns + normal equations + solve + two trial evaluations + complete gradient):\n\n| threads | mode | s per accepted iteration | accepted iterations per hour per job | ratio to fp64 (M3 limit 1.5) |\n|---|---|---|---|---|")
    for nth, p in proj.items():
        f64 = p["fp64"]["seconds_per_accepted_iteration"]
        for mode, q in p.items():
            s = q["seconds_per_accepted_iteration"]
            print(f"| {nth} | {mode} | {s:.0f} | {3600 / s:.2f} | {s / f64:.3f} |")
    print(f"\nPeak RSS of the profiling process at the end: {d.get('rss_peak_GB_end', float('nan')) * 1.024:.2f} GB (ru_maxrss KiB x 1024; includes the full float64 J_cw of 433009 x 1469, 5.1 GB).")
else:
    print("\nNo projection yet (the run has not reached its final stage).")
