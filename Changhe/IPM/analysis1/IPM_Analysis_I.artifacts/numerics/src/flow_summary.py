"""Aggregate the N1' flow certification (runs/flow_middle.json, flow_outer.json, flow_inner.json, flow_tails.json) into the certified
statements requested by the lead (notes/global_flow.md section 10): m_0 (min V_2/y on Q), axis signs of V_1, kappa_0 for r >= R_0,
T_0 maxima on and off B_1, V_1 maximum on B_1, and the number of unresolved angular cells. Float post-processing of certified per-cell bounds.
Usage: python3 flow_summary.py [x_star]
"""
import sys, json, os, gzip
import numpy as np


def _jopen(path):
    """Open a JSON result file for reading; falls back to path + '.gz' (the artifacts folder stores JSON files above 400 KB gzipped)."""
    if not os.path.exists(path) and os.path.exists(str(path) + ".gz"):
        return gzip.open(str(path) + ".gz", "rt")
    return open(path)


def _exists(path):
    return os.path.exists(path) or os.path.exists(str(path) + ".gz")


XS = float(sys.argv[1]) if len(sys.argv) > 1 else 8.600063805157177
rows = []
for f in ["runs/flow_middle.json", "runs/flow_outer.json", "runs/flow_inner.json"]:
    if _exists(f):
        d = json.load(_jopen(f)); rows += d["rows"]; print("%s: %d cells, done=%s, time %.0fs" % (f, len(d["rows"]), d.get("done"), d.get("time", 0)))
tails = json.load(_jopen("runs/flow_tails.json")) if _exists("runs/flow_tails.json") else None
if not rows: raise SystemExit("no cell data")
r_lo = np.array([r["r_lo"] for r in rows]); r_hi = np.array([r["r_hi"] for r in rows])
v2 = np.array([r["v2y_min"] for r in rows]); smin = np.array([r["s_min"] for r in rows])
Tin = np.array([r["T0_max_in"] for r in rows]); Tout = np.array([r["T0_max_out"] for r in rows]); V1in = np.array([r["V1_max_in"] for r in rows])
axlo = np.array([r["v1x_axis_lo"] for r in rows]); axhi = np.array([r["v1x_axis_hi"] for r in rows]); unres = np.array([r["n_unresolved"] for r in rows])
print("coverage: r from %.4e to %.4e (%d cells); gaps > 1e-12 relative: %d" % (r_lo.min(), r_hi.max(), len(rows), int(np.sum(np.sort(r_lo)[1:] > np.sort(r_hi)[:-1] * (1 + 1e-12)))))
i = np.argmin(v2); print("(Y)  min over cells of the certified lower bound of V_2/y: %.7f (raw; round DOWN when quoting) at r in [%.4f, %.4f]" % (v2[i], r_lo[i], r_hi[i]))
import math



def _jexists(path):
    import os
    return os.path.exists(path) or os.path.exists(str(path) + ".gz")
def lo6(v): return math.floor(v * 1e6) / 1e6      # outward rounding of a LOWER bound
def hi6(v): return math.ceil(v * 1e6) / 1e6       # outward rounding of an UPPER bound
if tails: print("     tails: outer V_2/y >= %.6f (r >= %.3e), inner V_2/y >= %.6f (r <= %.3e)   [rounded OUTWARD (floor); raw %.10f, %.10f]" % (lo6(tails["outer"]["v2y_min"]), tails["outer"]["R_T_hi"], lo6(tails["inner"]["v2y_min"]), tails["inner"]["r_T_lo"], tails["outer"]["v2y_min"], tails["inner"]["v2y_min"]))
for R0 in [10.0, 15.0, 20.0, 30.0]:
    sel = r_lo >= R0
    if sel.any(): print("(H4) r >= %.0f: X.V/r^2 >= %.6f (cells) %s" % (R0, smin[sel].min(), ("; outer tail >= %.6f [floor; raw %.10f]" % (lo6(tails["outer"]["s_min"]), tails["outer"]["s_min"])) if tails else ""))
# axis signs of V_1 = x (V_1/x)
below = r_hi < XS; above = r_lo > XS; cont = ~(below | above)
print("(H2') axis: cells entirely below x_*: max of V_1/x upper bound = %s (negative required); cells above: min of lower bound = %s (positive required); cells containing x_*: %d" % (
    ("%.6f" % axhi[below].max()) if below.any() else "n/a", ("%.6f" % axlo[above].min()) if above.any() else "n/a", int(cont.sum())))
for j in np.where(cont)[0]: print("      cell containing x_*: r in [%.6f, %.6f], V_1/x axis range [%.3e, %.3e]" % (r_lo[j], r_hi[j], axlo[j], axhi[j]))
# box inequalities
fin = lambda a: a[np.isfinite(a)].max() if np.isfinite(a).any() else float("nan")
print("(B_1) T_0 max on cells meeting B_1: %.7f ; V_1 max on B_1: %.7f ; T_0 max off B_1: %.7f (raw aggregates; round UP when quoting) (%s)" % (fin(Tin), fin(V1in), fin(Tout), ("outer tail T_0 <= %.8f, inner tail <= %.8f (raw; round UP when quoting)" % (tails["outer"]["T0_max"], tails["inner"]["T0_max"])) if tails else ""))
j = np.argmax(np.where(np.isfinite(Tout), Tout, -np.inf)); print("      T_0 off-box maximum at r in [%.4f, %.4f]" % (r_lo[j], r_hi[j]))
j = np.argmax(np.where(np.isfinite(Tin), Tin, -np.inf)); print("      T_0 on-box maximum at r in [%.4f, %.4f]" % (r_lo[j], r_hi[j]))
axf = np.array([r.get("axis_sign_fail", 0) for r in rows])
print("unresolved angular cells (target not met at max depth): %d in %d radial cells; axis-sign failures: %d" % (unres.sum(), int((unres > 0).sum()), int(axf.sum())))
for f in ["runs/flow_middle.json", "runs/flow_outer.json", "runs/flow_inner.json"]:
    if _jexists(f):
        d = json.load(_jopen(f)); print("%s: complete_region=%s, nc_total=%s, selection=%s, ntheta=%s" % (f, d.get("complete_region"), d.get("nc_total"), d.get("selection"), d.get("ntheta")))
if (unres > 0).any():
    for j in np.where(unres > 0)[0][:10]: print("      r in [%.4f, %.4f]: %d unresolved; V2/y min %.4f, T0 in/out %.4f/%.4f, V1_in %.3f" % (r_lo[j], r_hi[j], unres[j], v2[j], Tin[j], Tout[j], V1in[j]))
