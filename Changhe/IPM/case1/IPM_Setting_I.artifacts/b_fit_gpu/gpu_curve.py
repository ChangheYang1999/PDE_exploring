"""Objective against cumulative LSQR iteration count from gpu_long_solve / lead long_solve logs (.log or .long.jsonl).
Usage: python3 gpu_curve.py LOG [LOG2 ...]   (prints one table per log and, for two or more logs, the objectives at common counts)"""
import sys, json


def curve(path):
    pts = []; cum = 0; last_outer = None; last_it = 0; start = None; cl0 = None
    for l in open(path):
        try:
            r = json.loads(l)
        except Exception:
            continue
        ev = r.get("event")
        if ev == "start":
            start = r["norm"]; cl0 = r.get("cl")
        elif ev == "linearize":
            cum += last_it; last_it = 0; last_outer = r["outer"]
        elif ev == "check":
            last_it = r["it"]
            pts.append((cum + r["it"], r["actual"], r.get("cl"), r["outer"], r["it"], r.get("predicted")))
    return start, cl0, pts


tabs = []
for path in sys.argv[1:]:
    start, cl0, pts = curve(path)
    print("== %s  start %.6e  cl %s" % (path, start, cl0))
    print("  cum_its  outer  it   objective    ratio_to_start  predicted   cl")
    for n, a, cl, o, it, pr in pts:
        print("  %6d   %3d  %5d  %.6e  %.4f  %.4e  %s" % (n, o, it, a, a / start, pr if pr else float('nan'), ("%.9f" % cl) if cl else "-"))
    tabs.append({n: (a, cl, o, it, pr) for n, a, cl, o, it, pr in pts})
if len(tabs) >= 2:
    common = sorted(set.intersection(*[set(t.keys()) for t in tabs]))
    print("== objectives at common counts:", " | ".join(sys.argv[1:]))
    for n in common:
        print("  %6d  " % n + "  ".join("%.6e" % t[n][0] for t in tabs) + "  ratio %.4f" % (tabs[0][n][0] / tabs[1][n][0]))
