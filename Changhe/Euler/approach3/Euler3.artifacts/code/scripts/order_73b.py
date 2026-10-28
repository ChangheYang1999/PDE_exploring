#!/usr/bin/env python
"""SPEC 7.3b pairwise order among saved states, from their ledger rows (reports/arm_reading_<job>.json, written by scripts/arm_reading.py --json).
X ranks ahead of Y only if X's holdout rho_u^max is lower on BOTH shell families and X's core-set sigma_u^max, sigma_Om and core-set a_max each exceed
Y's by at most 10 per cent (ratio <= 1.10), both states core resolved; a missing value makes the pair 'not ordered' (lead d128 GU item 2; the rule of
scripts/shortlist.py). Prints every pair with the five ratios and the relation; writes an optional JSON.
Usage: .venv/bin/python scripts/order_73b.py <job_id> <job_id> [...] [--json out.json]"""
import sys, os, json, argparse, subprocess
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PY = os.path.join(ROOT, ".venv", "bin", "python")
ap = argparse.ArgumentParser(); ap.add_argument("jobs", nargs="+"); ap.add_argument("--json", default=None)
a = ap.parse_args()
rows = {}
for j in a.jobs:
    fn = os.path.join(ROOT, "reports", f"arm_reading_{j}.json")
    if not os.path.exists(fn):
        subprocess.run([PY, os.path.join(ROOT, "scripts", "arm_reading.py"), j, "--json"], cwd=ROOT, env=dict(os.environ, CUDA_VISIBLE_DEVICES="-1"), check=True, stdout=subprocess.DEVNULL)
    rows[j] = json.load(open(fn))["row"]
KEYS = ("rho_u_max_holdout", "rho_u_max_holdout_half", "sigma_u_max_core", "sigma_Om", "a_max_core")


def rel(x, y):
    """relation of x against y: '>' x ahead, '<' y ahead, '-' not ordered, '?' missing value"""
    vx = [x.get(k) for k in KEYS]; vy = [y.get(k) for k in KEYS]
    if any(v is None for v in vx + vy) or not (x.get("core_resolved") and y.get("core_resolved")):
        return "?", None
    r = [vx[i] / vy[i] if vy[i] else None for i in range(5)]
    if any(v is None for v in r):
        return "?", r
    ahead = r[0] < 1 and r[1] < 1 and all(v <= 1.10 for v in r[2:])
    rinv = [vy[i] / vx[i] for i in range(5)]
    behind = rinv[0] < 1 and rinv[1] < 1 and all(v <= 1.10 for v in rinv[2:])
    return (">" if ahead else ("<" if behind else "-")), r


out = dict(rule="SPEC 7.3b (lead d128 GU item 2): lower holdout on both families and core-set sigma_u^max, sigma_Om, core-set a_max ratios <= 1.10, both core resolved", conditions="(lead d128 HB item 1 (c) / HA item 3) every relation across degrees is conditional on the 7.3b sigma_Om 'same radius and quadrature' leg: the holdout angular counts differ by degree (6380 at L10, 4700 at L8, 3276 at L6) on the same 23 shells and 138 radii; the core-resolved flags are primary-reported, not independently verified", pairs=[])
print("| X | Y | holdout std X/Y | holdout half X/Y | core sigma_u X/Y | sigma_Om X/Y | core a_max X/Y | resolved X / Y | relation |")
print("|---|---|---|---|---|---|---|---|---|")
for i, x in enumerate(a.jobs):
    for y in a.jobs[i + 1:]:
        s, r = rel(rows[x], rows[y])
        rs = " | ".join(f"{v:.3f}" for v in r) if r else "n/a | n/a | n/a | n/a | n/a"
        word = {">": f"{x} ahead of {y}", "<": f"{y} ahead of {x}", "-": "not ordered", "?": "not ordered (missing value or unresolved core)"}[s]
        print(f"| {x} | {y} | {rs} | {rows[x].get('core_resolved')} / {rows[y].get('core_resolved')} | {word} |")
        out["pairs"].append(dict(X=x, Y=y, ratios=r, relation=s, words=word))
if a.json:
    json.dump(out, open(a.json, "w"), indent=1); print("wrote", a.json)
