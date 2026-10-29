"""Numerics-side cross-check of primary-search numbers quoted in the lead's FINAL_REPORT (sections 4.3, 4.4a, 4.6) against the frozen
FAILURE_MAP.csv (526 runs). Each claim is checked as: a run exists with the stated final c_l (within 0.003) and holdout rho_max rounding
to the quoted value (half-unit of the last quoted digit), or the stated count holds. Usage: python3 scripts/crosscheck_lead_report.py"""
import csv, os, math
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, ".."))
rows = list(csv.DictReader(open(os.path.join(ROOT, "FAILURE_MAP.csv"))))
def f(x):
    try: return float(x)
    except Exception: return float("nan")
for r in rows:
    for k in ("cl_start", "cl_final", "rho_max", "s_core", "s_far", "rel_Rq", "rel_Reta"): r[k + "_f"] = f(r.get(k))
    r["swirl"] = (r["s_core_f"] >= 0.05 and r["s_far_f"] >= 0.05)
out = []
def check(name, ok, detail=""):
    out.append(("PASS" if ok else "FAIL", name, detail)); 
print(f"{len(rows)} runs in FAILURE_MAP.csv")
# ---- 4.3 Stage I counts
stages = sorted(set(r["stage"] for r in rows)); print("stage labels:", stages)
s1 = [r for r in rows if r["stage"] == "I"]   # the map labels: I (311), I-II (61: Stage I families continued in Stage II), I-critical (46), II (104), II-critical (4)
check("4.3: 311 Stage I runs", len(s1) == 311, f"{len(s1)}")
import datetime as _dt
def _ceil_min(t): d = _dt.datetime.strptime(t, "%Y-%m-%dT%H:%M:%SZ"); d = d + _dt.timedelta(seconds=59); return d.strftime("%H:%M")
fin = sorted(r["finished"] for r in s1); check("4.3: Stage I finished between 19:39Z and 04:47Z (enclosing minutes: floor of the first, ceiling of the last)", fin[0][11:16] == "19:39" and _ceil_min(fin[-1]) == "04:47", f"{fin[0]} .. {fin[-1]}")
before = [r for r in s1 if r["finished"] <= "2026-10-29T00:59:44Z"]; check("4.3: 282 finished before 00:59:44Z", len(before) == 282, f"{len(before)}")
sw1 = [r for r in s1 if r["swirl"]]; check("4.3: 97 swirl-retaining Stage I runs", len(sw1) == 97, f"{len(sw1)}")
check("4.3: 81 of them before 00:59:44Z", len([r for r in sw1 if r["finished"] <= "2026-10-29T00:59:44Z"]) == 81, f"{len([r for r in sw1 if r['finished'] <= '2026-10-29T00:59:44Z'])}")
mins = {}
for r in sw1:
    k = round(r["cl_start_f"], 3)
    if k not in mins or r["rho_max_f"] < mins[k]["rho_max_f"]: mins[k] = r
expect = {0.505: 13.1, 0.525: 79.5, 0.56: 25.6, 0.60: 6.9, 0.64: 6.7, 0.68: 7.2, 0.72: 7.5, 0.74: 7.5}
for k, v in expect.items():
    m = mins.get(k); check(f"4.3: smallest swirl-retaining rho_max at start c_l {k} = {v}", m is not None and abs(m["rho_max_f"] - v) <= 0.05, f"{m['rho_max_f']:.3f} {m['dominant_eq']} {m['job_id']}" if m else "none")
check("4.3: dominant equation axial momentum except 0.505 (reduced vorticity)", all((mins[k]["dominant_eq"].lower().startswith("m_z") or "mz" in mins[k]["dominant_eq"].lower().replace("_", "")) for k in expect if k != 0.505) and "eta" in mins[0.505]["dominant_eq"].lower(), ", ".join(f"{k}:{mins[k]['dominant_eq']}" for k in expect))
from collections import Counter
cc = Counter(r["failure_class"].split()[0] for r in s1); check("4.3: classes F1 214, F7 74, F6 19, F5 4", cc.get("F1") == 214 and cc.get("F7") == 74 and cc.get("F6") == 19 and cc.get("F5") == 4, str(dict(cc)))
fc = [r for r in s1 if r["free_cl"].lower() in ("true", "1", "yes")]; check("4.3: 43 free-c_l Stage I runs", len(fc) == 43, f"{len(fc)}")
hi = [r for r in fc if r["cl_final_f"] >= 0.7485]; check("4.3: six free-c_l runs reach 0.749, from 0.60, 0.64, 0.68", len(hi) == 6 and set(round(r["cl_start_f"], 2) for r in hi) <= {0.6, 0.64, 0.68}, f"{len(hi)} from {sorted(set(round(r['cl_start_f'],3) for r in hi))}")
lo = [r for r in fc if r["cl_final_f"] <= 0.5015]; check("4.3: one free-c_l run reaches 0.501 from 0.60", len(lo) == 1 and abs(lo[0]["cl_start_f"] - 0.6) < 0.001, f"{[(r['cl_start'], r['cl_final']) for r in lo]}")
# ---- c_l = 1/2 experiment
crit = [r for r in rows if abs(r["cl_start_f"] - 0.5) < 1e-6 and r["job_id"].startswith("crit")]
check("4.6: c_l = 1/2 class 50 runs, 29 below the swirl filter, 21 above", len(crit) == 50 and len([r for r in crit if not r["swirl"]]) == 29, f"{len(crit)} / {len([r for r in crit if not r['swirl']])} below")
crit1 = [r for r in crit if r["stage"] == "I-critical"]; check("4.3: 46 Stage I critical runs, 26 lost the swirl, 20 kept it", len(crit1) == 46 and len([r for r in crit1 if not r["swirl"]]) == 26, f"{len(crit1)} / {len([r for r in crit1 if not r['swirl']])}")
kept = [r for r in crit1 if r["swirl"]]; bybasis = {}
for r in kept: bybasis.setdefault("jacobi" if "jacobi" in r["level"] else "cheb", []).append(r["rho_max_f"])
check("4.3: smallest swirl-retaining critical rho_max 12.5 and 24.2 per basis (10 runs each)", sorted(round(min(v), 1) for v in bybasis.values()) == [12.5, 24.2] and all(len(v) == 10 for v in bybasis.values()), str({k: (len(v), round(min(v), 2)) for k, v in bybasis.items()}))
m = min(crit1, key=lambda r: r["rho_max_f"]); check("4.3: smallest critical rho_max of any run 4.7 with swirl fractions 0.03 / 0.02", abs(m["rho_max_f"] - 4.7) <= 0.05 and abs(m["s_core_f"] - 0.03) < 0.006 and abs(m["s_far_f"] - 0.02) < 0.006, f"{m['rho_max_f']:.2f} {m['s_core_f']:.3f}/{m['s_far_f']:.3f} {m['job_id']}")
# ---- 4.6 class totals
check("4.6: 257 swirl-retaining of 526", len([r for r in rows if r["swirl"]]) == 257 and len(rows) == 526, f"{len([r for r in rows if r['swirl']])}")
# ---- quoted (c_l, rho_max) values of 4.4a and 4.6: existence of a run
def exists(cl, v, tol=None, pred=lambda r: True):
    if tol is None:
        s = f"{v}"; tol = 0.5 * 10 ** (-(len(s.split(".")[1]) if "." in s else 0)) if "e" not in s else 0.05 * v
    hits = [r for r in rows if abs(r["cl_final_f"] - cl) <= 0.003 and abs(r["rho_max_f"] - v) <= tol * 1.0001 and pred(r)]
    return hits
claims = [(0.745, 2.39), (0.74, 10.7), (0.735, 15.3), (0.73, 19.3), (0.72, 21.9), (0.70, 24.7), (0.74, 14.6), (0.74, 8.0), (0.749, 2.04), (0.74, 142), (0.72, 40.7), (0.70, 71.9),
          (0.65, 83.5), (0.745, 2.375), (0.74, 23.0), (0.73, 20.1), (0.70, 39.0), (0.68, 7.73), (0.68, 35.1), (0.68, 3.50), (0.68, 3.38), (0.68, 4.83), (0.68, 4.39), (0.68, 6.31),
          (0.68, 5.12), (0.68, 4.85), (0.68, 3.37), (0.6667, 53.4), (0.6667, 33.9), (0.70, 102), (0.70, 60.2), (0.72, 75.6), (0.70, 45.0), (0.749, 2.62), (0.80, 3.09), (0.745, 2.60),
          (0.74, 3.55), (0.74, 2.86), (0.74, 2.85), (0.74, 2.81), (0.74, 2.95), (0.74, 2.65), (0.74, 3.27), (0.74, 2.75), (0.74, 3.12), (0.74, 5.41), (0.74, 3.32), (0.74, 22.4), (0.74, 18.9),
          (0.74, 11.0), (0.74, 16.5), (0.74, 109), (0.74, 5.57), (0.74, 4.70), (0.74, 2.87), (0.74, 4.60), (0.735, 13.7), (0.73, 25.5), (0.725, 35.8), (0.72, 35.9), (0.71, 23.9), (0.70, 31.3),
          (0.685, 7.49), (0.69, 16.5), (0.695, 33.4), (0.70, 110), (0.71, 163), (0.74, 2.83), (0.74, 2.79), (0.74, 8.23), (0.74, 8.54), (0.74, 7.55), (0.74, 14.5), (0.68, 6.39), (0.68, 17.0),
          (0.68, 6.78), (0.68, 16.9), (0.74, 3.02), (0.74, 12.6), (0.745, 3.09), (0.7425, 6.89), (0.7375, 10.7), (0.65, 23.3), (0.749, 1.58), (0.749, 1.88), (0.749, 2.33), (0.749, 2.55),
          (0.749, 4.24), (0.749, 2.79), (0.749, 3.37), (0.749, 3.19), (0.749, 3.15), (0.749, 4.44), (0.749, 10.4), (0.74, 26.6), (0.74, 32.2), (0.749, 4.6), (0.5, 12.5), (0.5, 7.49), (0.5, 12.05), (0.5, 48.2), (0.5, 41.8)]
miss = []
for cl, v in claims:
    h = exists(cl, v)
    if not h: miss.append((cl, v))
check(f"4.4a/4.6: {len(claims)} quoted (c_l, rho_max) pairs each match a run", not miss, f"missing: {miss}" if miss else "all found")
big = [(0.74, 5.7e3, 0.74), (0.60, 1.1e4, 0.60), (0.55, 1.6e6, 0.55)]
for cl, v, _ in big:
    h = [r for r in rows if abs(r["cl_final_f"] - cl) <= 0.003 and abs(r["rho_max_f"] / v - 1) <= 0.06]; check(f"4.4a: rho_max about {v:g} at c_l {cl}", bool(h), h[0]["job_id"] if h else "none")
# the 0.65 chain step: a_eff 13.7 and the q0 = 5 chain losing far swirl at 0.65 (s_far 0.002)
h = [r for r in rows if abs(r["cl_final_f"] - 0.65) <= 0.003 and abs(r["rho_max_f"] - 83.5) <= 0.05]; check("4.4a: 83.5 at 0.65 with far swirl fraction 0.002", bool(h) and abs(h[0]["s_far_f"] - 0.002) < 0.0006, f"{h[0]['s_far_f'] if h else 'none'}")
h = [r for r in rows if abs(r["cl_final_f"] - 0.70) <= 0.003 and abs(r["rho_max_f"] - 60.2) <= 0.05]; check("4.4a: 60.2 at 0.70 with far swirl fraction 0.007", bool(h) and abs(h[0]["s_far_f"] - 0.007) < 0.0006, f"{h[0]['s_far_f'] if h else 'none'}")
import json
h = [r for r in rows if abs(r["cl_final_f"] - 0.74) <= 0.003 and abs(r["rho_max_f"] - 14.5) <= 0.05 and r["job_id"].startswith("t1seedShift")]
vj = json.load(open(os.path.join(ROOT, "runs", h[0]["job_id"], "validation.json"))) if h else {}
check("4.4a: 14.5 at 0.74 (D48 shift 0) with reduced-equation value 0.71", bool(h) and abs(vj.get("rho_reduced_max", 0) - 0.71) < 0.006, f"{h[0]['job_id'] if h else 'none'} rho_reduced_max {vj.get('rho_reduced_max')}")
# ---- section 1 and 7 claims
below = [r for r in rows if r["swirl"] and 0.5 < r["cl_final_f"] < 0.7485]; mb = min(below, key=lambda r: r["rho_max_f"])
check("1: smallest primary swirl-retaining value below c_l 0.7485 is 2.37 (fixed-c_l continuation at 0.745)", abs(mb["rho_max_f"] - 2.37) <= 0.005 and abs(mb["cl_final_f"] - 0.745) < 0.001, f"{mb['rho_max_f']:.3f} {mb['job_id']}")
check("7.2: interface radii 5, 10, 20 at c_l 0.749 (q0 3.5) gave 1.58, 1.88, 8.40", bool(exists(0.749, 1.58)) and bool(exists(0.749, 1.88)) and bool(exists(0.749, 8.40)), "")
import json as _j
try:
    c1 = _j.load(open(os.path.join(ROOT, "runs", "fmE_cl0p735", "result.json")))["cost"]; c0 = _j.load(open(os.path.join(ROOT, "runs", "t1seedC_cl0p74_q2p5", "result.json")))["cost"]
    check("7.2: training cost of the first fmE step 1.35e-2 against 1.46e-2 for its parent", abs(c1 - 1.35e-2) < 5e-5 and abs(c0 - 1.46e-2) < 5e-5, f"{c1:.4e} vs {c0:.4e}")
except Exception as ex:
    check("7.2: fmE first-step cost", False, repr(ex))
npass = sum(1 for s in out if s[0] == "PASS"); nfail = len(out) - npass
for s, n, d in out: print(f"{s}  {n}  [{d}]")
print(f"SUMMARY: {npass} PASS, {nfail} FAIL of {len(out)} checks")
