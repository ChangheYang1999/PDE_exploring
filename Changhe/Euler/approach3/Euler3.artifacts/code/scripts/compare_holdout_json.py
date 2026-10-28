#!/usr/bin/env python
"""Compare two holdout re-evaluations of the same state written by reevaluate_holdout.py --json_out (e.g. source nodes 60 against 120; lead 2026-10-25T18:4xZ item 2):
per shell on both families (rho_u, rho_nl, rho_sp, absolute RMS of R_u and of the terms where present), the maxima, the single-sphere maxima, and the far-coefficient
and balance scalars of the summary. Prints relative changes (B - A) / A and absolute values. Usage: compare_holdout_json.py <A.json> <B.json>"""
import sys, json, math
A = json.load(open(sys.argv[1])); B = json.load(open(sys.argv[2]))
print(f"A: {A['zfile']} Nr_src {A.get('Nr_src')}  |  B: Nr_src {B.get('Nr_src')}  (light={A.get('light')})")
def num(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool) and x is not None and math.isfinite(x)
def walk(a, b, path=""):
    out = []
    if isinstance(a, dict) and isinstance(b, dict):
        for k in a:
            if k in b:
                out += walk(a[k], b[k], path + "/" + str(k))
    elif isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
        if all(num(x) or x is None for x in a):
            out.append((path, a, b))
        else:
            for i, (x, y) in enumerate(zip(a, b)):
                out += walk(x, y, path + f"[{i}]")
    elif num(a) and num(b):
        out.append((path, [a], [b]))
    return out
def report(section, pats):
    print(f"\n== {section}")
    for path, a, b in walk(A[section], B[section]):
        if not any(p in path for p in pats):
            continue
        rel = [((y - x) / abs(x) if (num(x) and num(y) and abs(x) > 0) else None) for x, y in zip(a, b)]
        rels = [r for r in rel if r is not None]
        if not rels:
            continue
        mx = max(abs(r) for r in rels)
        print(f"{path}: max |rel change| {mx:.3e}; A {['%.6e' % x if num(x) else x for x in a][:12]}{' ...' if len(a) > 12 else ''}; rel {['%.1e' % r if r is not None else None for r in rel][:12]}")
pats = ["rho_u", "rho_nl", "rho_sp", "rho_lin", "rms", "abs", "term", "max", "a_max", "sigma", "edges"]
for sec in ("holdout_std", "holdout_half"):
    report(sec, pats)
report("spheres", ["rho", "rms", "r"])
report("summary", ["rho_u_max", "rho_nl_max", "sphere", "K_ratio", "K_H", "carried", "E_ren", "H_tot", "sigma_u_max", "a_max", "rho_lin", "rho_sp", "G_defect"])
