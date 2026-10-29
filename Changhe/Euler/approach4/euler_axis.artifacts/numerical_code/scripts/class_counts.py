"""Per-class counts for FINAL_REPORT 4.6 (lead notes 41 item 3 and 43 item 4): for each search class of the primary search, the number
of finished runs, the number that keep swirl (swirl magnitude filter: s_core and s_far >= 0.05), the best swirl-retaining holdout
rho_max with its job, final c_l and level, and the c_l values tried with run counts. Classes are assigned by job_id prefix
(the campaign's naming) from FAILURE_MAP.csv (run scripts/failure_map.py first). Output: docs/CLASS_COUNTS.md and stdout.
Usage: python3 scripts/class_counts.py [path/to/FAILURE_MAP.csv]"""
import csv, sys, os, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "FAILURE_MAP.csv")
rows = list(csv.DictReader(open(path)))

def cls(r):
    j = r["job_id"]; st = r["stage"]
    if st == "I-critical" or j.startswith("crit"):
        return "c_l = 1/2 experiment"
    if j.startswith("refl"):
        return "reflection class (phi odd, q even)"
    if j.startswith(("t1seed", "freecl_t1seed", "freeclwide_t1seed", "freeclmid_t1seed", "fmD", "fmE", "fmF")):   # free-c_l restarts of the seeds (any bound); fmD/fmE/fmF chains from the 0.68 and 0.74 states
        return "direct positive-strain seeds at fixed c_l (0.74, 0.68 and others; levels, continuations, free c_l, the chains fmD/fmE/fmF from the 0.68 and 0.74 states, outer-domain and sensitivity variants)"
    if j.startswith(("chain", "fmA", "fmB", "fmC", "fmap", "lad2c07", "lad3c07", "freecl_fmC")):
        return "fixed-c_l continuation from 0.749 (chains fmA, fmB, fmC, fmap, chain*; levels and outer-domain variants)"
    if j.startswith(("t1lad", "lad2", "lad3", "lad4", "rm5")):
        return "pinned-amplitude single-source ladder (positive-strain seeds of lead note 20, free c_l to the bound 0.749; levels, q0 scan, outer interface 5/10/20)"
    return "generic and S1-structured seeds, q0 free or pinned, c_l free or fixed (Stage I families and their continuations)"

def f(x):
    try: return float(x)
    except Exception: return None

groups = collections.OrderedDict()
order = ["generic and S1-structured seeds, q0 free or pinned, c_l free or fixed (Stage I families and their continuations)",
         "c_l = 1/2 experiment",
         "pinned-amplitude single-source ladder (positive-strain seeds of lead note 20, free c_l to the bound 0.749; levels, q0 scan, outer interface 5/10/20)",
         "reflection class (phi odd, q even)",
         "fixed-c_l continuation from 0.749 (chains fmA, fmB, fmC, fmap, chain*; levels and outer-domain variants)",
         "direct positive-strain seeds at fixed c_l (0.74, 0.68 and others; levels, continuations, free c_l, the chains fmD/fmE/fmF from the 0.68 and 0.74 states, outer-domain and sensitivity variants)"]
for k in order: groups[k] = []
for r in rows: groups[cls(r)].append(r)
import datetime
lines = [f"# Per-class counts of the primary search (from {os.path.relpath(path, ROOT)}, {len(rows)} finished runs; generated {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')})", "",
         f"Frozen run count: {len(rows)} finished runs in the failure map at generation time; class partition by job-name prefix (scripts/class_counts.py); "
         f"swirl-retaining = swirl magnitude filter only (not B2 stability under refinement).", "",
         "Swirl-retaining = swirl magnitude filter (s_core >= 0.05 and s_far >= 0.05). Best = smallest holdout SPEC rho_max among swirl-retaining runs",
         "(an order-one residual in every class; no run meets B1). c_l tried = final c_l rounded to 3 decimals with the run count.", "",
         "| search class | finished runs | swirl-retaining | best swirl-retaining rho_max (job; final c_l; level) | best with 0.5 < final c_l < 0.7485 | c_l values (final, rounded) with run counts |", "|---|---|---|---|---|---|"]
for k, g in groups.items():
    ok = [r for r in g if (f(r["s_core"]) or 0) >= 0.05 and (f(r["s_far"]) or 0) >= 0.05 and f(r["rho_max"]) is not None]
    best = min(ok, key=lambda r: f(r["rho_max"])) if ok else None
    cl_counts = collections.Counter(round(f(r["cl_final"]), 3) for r in g if f(r["cl_final"]) is not None)
    cl_txt = ", ".join(f"{c:.3f} ({n})" for c, n in sorted(cl_counts.items()))
    b = f"{f(best['rho_max']):.2f} ({best['job_id']}; {f(best['cl_final']):.4f}; {best['level']})" if best else "none"
    inner = [r for r in ok if 0.5 < f(r["cl_final"]) < 0.7485]    # inside the target interval and away from the imposed bound 0.749 (excludes the c_l = 1/2 row)
    bi = min(inner, key=lambda r: f(r["rho_max"])) if inner else None
    bi_txt = f"{f(bi['rho_max']):.2f} ({bi['job_id']}; {f(bi['cl_final']):.4f}; {bi['level']})" if bi else "none"
    lines.append(f"| {k} | {len(g)} | {len(ok)} | {b} | {bi_txt} | {cl_txt} |")
lines.append(f"| all | {len(rows)} | {sum(1 for r in rows if (f(r['s_core']) or 0) >= 0.05 and (f(r['s_far']) or 0) >= 0.05)} | | | |")
out = "\n".join(lines) + "\n"
os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)
open(os.path.join(ROOT, "docs", "CLASS_COUNTS.md"), "w").write(out)
print(out)
