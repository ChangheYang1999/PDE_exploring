#!/usr/bin/env python
"""Nested-ladder promotion (lead 2026-10-24T23:06Z item 2): for each parameter point of a nested sweep tag (default nest2), rank its
finished starts by the holdout rho_u^max on BOTH shell families (key = max(standard, half-offset); ties by the standard value), drop
failed/trivial starts, and enqueue continuation jobs for the best n_promote starts at the next level (exact embedding, fixed parameters,
all5 weighting, tail constraints, no Sigma_Z row). Usage: promote_nest.py --tag nest2 --to_tag nest4 --L 4 --Nk 12 [--n_promote 5] [--priority 12] [--dry]"""
import sys, os, json, argparse, subprocess, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
from src.campaign import ledger
ap = argparse.ArgumentParser(); ap.add_argument("--tag", default="nest2"); ap.add_argument("--to_tag", default="nest4"); ap.add_argument("--L", type=int, default=4)
ap.add_argument("--Nk", type=int, default=12); ap.add_argument("--n_promote", type=int, default=5); ap.add_argument("--priority", type=int, default=12)
ap.add_argument("--dry", action="store_true"); ap.add_argument("--channels", default=None); ap.add_argument("--chdeg", default=None); ap.add_argument("--nl_den", default="all5")
ap.add_argument("--min_starts", type=int, default=1, help="promote a parameter point only when at least this many of its starts are finished")
ap.add_argument("--max_iter", type=int, default=300); ap.add_argument("--chunk", type=int, default=None); ap.add_argument("--exclusive", action="store_true")
ap.add_argument("--closure_lambda", type=float, default=None, help="closure rows weight passed to enqueue_continuation (channel runs)")
a = ap.parse_args()
recs = ledger.merge_reevaluations(ledger.read(os.path.join(ROOT, "status", "ledger.jsonl")))
rows = [r for r in recs if str(r.get("job_id", "")).startswith(a.tag + "_") and not r.get("failure") and r.get("rho_u_max_holdout") is not None
        and (r.get("max_abs_Omega", 0) > 1e-6) and (r.get("rotation_content_rel", 0) > 1e-3) and (r.get("e_F") is None or r["e_F"] >= 1e-4)]
groups = collections.defaultdict(list)
for r in rows:
    groups[(r["c_l"], r["omega"])].append(r)
def key(r):
    both = [v for v in (r.get("rho_u_max_holdout"), r.get("rho_u_max_holdout_half")) if v is not None]
    return (max(both), r["rho_u_max_holdout"])
n = 0
for (cl, om), rs in sorted(groups.items()):
    n_all = sum(1 for r in recs if str(r.get("job_id", "")).startswith(a.tag + "_") and r["c_l"] == cl and r["omega"] == om)
    if n_all < a.min_starts:
        print(f"({cl}, {om}): {n_all} finished starts < {a.min_starts}: not promoted yet"); continue
    rs.sort(key=key)
    print(f"({cl}, {om}): {len(rs)} ranked starts; best (std, half): " + ", ".join(f"({r['rho_u_max_holdout']:.3f}, {r.get('rho_u_max_holdout_half') if r.get('rho_u_max_holdout_half') is None else round(r['rho_u_max_holdout_half'], 3)})" for r in rs[:a.n_promote]))
    for i, r in enumerate(rs[:a.n_promote]):
        src = os.path.join(ROOT, r["zfile"])
        cmd = [os.path.join(ROOT, ".venv/bin/python"), os.path.join(ROOT, "scripts/enqueue_continuation.py"), "--src", src, "--tag", a.to_tag, "--L", str(a.L), "--Nk", str(a.Nk),
               "--nl_den", a.nl_den, "--priority", str(a.priority), "--suffix", f"_p{i}_{r['job_id'].split('_')[-1]}s{r['start']}", "--max_iter", str(a.max_iter)]
        if a.channels: cmd += ["--channels", a.channels]
        if a.chdeg: cmd += ["--chdeg", a.chdeg]
        if a.chunk: cmd += ["--chunk", str(a.chunk)]
        if a.exclusive: cmd += ["--exclusive"]
        if a.closure_lambda is not None: cmd += ["--closure_lambda", str(a.closure_lambda)]
        if a.dry: print("  would run:", " ".join(cmd[2:]))
        else:
            out = subprocess.run(cmd, capture_output=True, text=True); print("  " + (out.stdout.strip() or out.stderr.strip()[-200:])); n += 1
print(f"{'would enqueue' if a.dry else 'enqueued'} {n} promotion jobs")
