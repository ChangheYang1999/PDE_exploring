#!/usr/bin/env python
"""D6FP (lead 03:02:22Z item 1, SPEC v1.10 section 9): per-iteration timing samples of a worker run (the lagJ smoke) as the second source of the
profiling report: from the run's history (checkpoint.pt while running, or starts/start_000*.pt when finished) list, for every accepted iteration,
J age, t_jac (J_cw all columns), t_param_cols, t_normal, t_solve, t_trial (sum over the trials of the iteration; n_trials), the complete-gradient
seconds and t_iter; then medians and spread over the fresh-J iterations (J_age 0) and over the reused-J iterations. Markdown to stdout.
Usage: python scripts/smoke_timing_samples.py runs/<job>"""
import sys, os, glob, json, statistics, torch
run = sys.argv[1]
fins = sorted(glob.glob(os.path.join(run, "starts", "start_000*.pt")))
if fins:
    src = fins[-1]; d = torch.load(src, map_location="cpu", weights_only=False); hist = d.get("history") or []
else:
    src = os.path.join(run, "checkpoint.pt"); d = torch.load(src, map_location="cpu", weights_only=False); hist = (d.get("current") or {}).get("history") or []
rows = []
for h in hist:
    cg = h.get("complete_gradient") or {}
    rows.append(dict(it=h.get("it"), acc=h.get("accepted"), J_age=h.get("J_age"), J_fresh=h.get("J_fresh"), n_trials=h.get("n_trials"), t_jac=h.get("t_jac"), t_param_cols=h.get("t_param_cols"),
                     t_normal=h.get("t_normal"), t_solve=h.get("t_solve"), t_trial=h.get("t_trial"), t_grad=cg.get("seconds"), t_iter=h.get("t_iter"), rho=h.get("rho")))
print(f"Source {src}: {len(rows)} iteration records.\n")
print("| it | accepted | J age | trials | t_jac (s) | t_param_cols (s) | t_normal (s) | t_solve (s) | t_trial total (s) | complete gradient (s) | t_iter (s) | rho |\n|---|---|---|---|---|---|---|---|---|---|---|---|")
f = lambda v: "n/a" if v is None else (f"{v:.1f}" if isinstance(v, (int, float)) else str(v))
for r in rows:
    print(f"| {r['it']} | {r['acc']} | {r['J_age']} | {r['n_trials']} | {f(r['t_jac'])} | {f(r['t_param_cols'])} | {f(r['t_normal'])} | {f(r['t_solve'])} | {f(r['t_trial'])} | {f(r['t_grad'])} | {f(r['t_iter'])} | {f(r['rho'])} |")
def stats(vals):
    vals = [v for v in vals if isinstance(v, (int, float))]
    return (f"median {statistics.median(vals):.1f} s (min {min(vals):.1f}, max {max(vals):.1f}, n {len(vals)})" if vals else "n/a")
fresh = [r for r in rows if r["acc"] and (r["J_age"] in (0, None))]; reused = [r for r in rows if r["acc"] and r["J_age"] not in (0, None)]
print(f"\nFresh-J accepted iterations ({len(fresh)}): J_cw all columns {stats([r['t_jac'] for r in fresh])}; parameter columns {stats([r['t_param_cols'] for r in fresh])}; normal equations {stats([r['t_normal'] for r in fresh])}; solve {stats([r['t_solve'] for r in fresh])}; trial evaluation per trial {stats([r['t_trial'] / r['n_trials'] for r in fresh if r.get('n_trials')])}; complete gradient {stats([r['t_grad'] for r in fresh])}; whole iteration {stats([r['t_iter'] for r in fresh])}.")
print(f"Reused-J accepted iterations ({len(reused)}): trial evaluation per trial {stats([r['t_trial'] / r['n_trials'] for r in reused if r.get('n_trials')])}; solve {stats([r['t_solve'] for r in reused])}; complete gradient {stats([r['t_grad'] for r in reused])}; whole iteration {stats([r['t_iter'] for r in reused])}.")
acc = [r for r in rows if r["acc"]]
if acc:
    print(f"Mean wall time per accepted iteration over the run (p of the lead's segment rule, fresh and reused): {sum(r['t_iter'] for r in rows if isinstance(r['t_iter'], (int, float))) / len(acc):.1f} s over {len(acc)} accepted of {len(rows)} iterations.")
