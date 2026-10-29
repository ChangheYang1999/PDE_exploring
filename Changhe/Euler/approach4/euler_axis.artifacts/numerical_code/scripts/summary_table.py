"""Branch-wise summary of PARAMETER_SWEEP.csv for NUM_REPORT.md: per branch and c_l start value, the best SPEC rho_max, the
median rho_max, best s_core, number of jobs, and the c_l drift for free-c_l jobs.  Usage: python3 scripts/summary_table.py"""
import csv, os, math, statistics, json
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
rows = list(csv.DictReader(open(os.path.join(ROOT, "PARAMETER_SWEEP.csv"))))
def fl(v):
    try: return float(v)
    except Exception: return float("nan")
groups = {}
for r in rows:
    cl0 = fl(json.loads(r["init_extra"]).get("cl0", "nan")) if False else None
    key = (r["branch"], r["stage"])
    groups.setdefault(key, []).append(r)
print(f"{'branch':14s} {'stage':11s} {'n':>3s} {'best rho':>9s} {'median rho':>10s} {'best s_core':>11s} {'n swirl>=0.05':>13s} {'c_l range (final)':>22s}")
for key in sorted(groups):
    g = groups[key]
    rh = [fl(r["rho_max_spec"]) for r in g if r["rho_max_spec"]]
    sc = [fl(r["s_core_spec"]) for r in g if r["s_core_spec"]]
    cls = [fl(r["cl"]) for r in g]
    print(f"{key[0]:14s} {key[1]:11s} {len(g):3d} {min(rh) if rh else float('nan'):9.2e} {statistics.median(rh) if rh else float('nan'):10.2e} {max(sc) if sc else float('nan'):11.3f} "
          f"{sum(1 for v in sc if v >= 0.05):13d} {min(cls):.4f} .. {max(cls):.4f}")
# per c_l start (fixed-c_l branches): best rho and family
print("\nfixed c_l (S1 / generic), best rho_max per c_l:")
byc = {}
for r in rows:
    if r["free_cl"] == "True": continue
    byc.setdefault(round(fl(r["cl"]), 3), []).append(r)
for c in sorted(byc):
    g = [r for r in byc[c] if r["rho_max_spec"]]
    if not g: continue
    b = min(g, key=lambda r: fl(r["rho_max_spec"]))
    print(f"  c_l={c:.3f}: n={len(byc[c]):3d} best rho_max={fl(b['rho_max_spec']):.2e} (s_core {fl(b['s_core_spec']):.3f}, {b['branch']}, {b['family']}) ; swirl>=0.05 in {sum(1 for r in g if fl(r['s_core_spec'])>=0.05)} jobs")
