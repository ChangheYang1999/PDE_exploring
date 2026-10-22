"""Per-shell table of the rigorous derivative certificate for a region file runs/cert_deriv_regions_{outer,inner}.json (or the middle file):
rows carry W_i_j = sum_N (2N+1)^j sup_cell |d_t^i eps_N| (i + j <= 2), W_eps_minus_dteps, W_K, W1_K, W_dtK, m_inf (certified cell minimum of
m = u^3 (1+u^2)^{(k-3)/2}) and wf_sup (certified cell maximum of (1+u)^{1/2}).  Pointwise on the cell (polar derivatives -> Cartesian):
  r |grad eps~| <= W_1_0 + W_0_1,   r^2 |d^2 eps~| (any second derivative) <= W_2_0 + 2 W_1_1 + W_0_2 + W_1_0 + 2 W_0_1.
Printed per dyadic-decade shell of r: sup W/m, sup r|grad|/m, sup r^2|D^2|/m, the multiplier forms x wf_sup, and sup W_eps_minus_dteps/m, W_K/m,
W_dtK/m (float post-processing of the certified per-cell numbers: max is exact, divisions/products with 1e-15 relative slack are quoted to
4 significant digits rounded up).  Usage: python3 src/deriv_region_shells.py runs/cert_deriv_regions_outer.json [shell edges...]
"""
import sys, json, math
import numpy as np


def _jopen(path):
    """Open a JSON result file for reading; falls back to path + '.gz' (the artifacts folder stores JSON files above 1 MB gzipped)."""
    import os, gzip
    if not os.path.exists(path) and os.path.exists(str(path) + ".gz"):
        return gzip.open(str(path) + ".gz", "rt")
    return open(path)

def up4(x):
    """4-significant-digit ceiling of a positive float (with a 1e-15 relative safety slack)."""
    if not np.isfinite(x) or x <= 0: return "%.4g" % x
    x = x * (1 + 1e-15); e = math.floor(math.log10(x)); q = 10.0 ** (e - 3)
    return "%.4g" % (math.ceil(x / q) * q)

d = json.load(_jopen(sys.argv[1])); rows = d["rows"]
r_a = np.array([r.get("r_a", math.exp(r["t_a"])) for r in rows]); m = np.array([r["m_inf"] for r in rows]); wf = np.array([r.get("wf_sup", np.nan) for r in rows])
col = lambda k: np.array([r.get(k, np.nan) for r in rows], float)
W00, W10, W01, W20, W11, W02 = (col(k) for k in ("W_0_0", "W_1_0", "W_0_1", "W_2_0", "W_1_1", "W_0_2"))
grad = W10 + W01; d2 = W20 + 2 * W11 + W02 + W10 + 2 * W01
Wemd, WK, WdtK = col("W_eps_minus_dteps"), col("W_K"), col("W_dtK")
if len(sys.argv) > 2: edges = [float(x) for x in sys.argv[2:]]
else:
    lo = 10 ** math.floor(math.log10(r_a.min())); edges = [lo * 10 ** k for k in range(0, 14) if lo * 10 ** (k - 1) <= r_a.max() * 10]
print("%s: %d cells, done=%s, r in [%.4g, %.4g]" % (sys.argv[1], len(rows), d.get("done"), r_a.min(), r_a.max()))
print("| shell of r (cell starts) | cells | sup W/m | sup r|grad eps~|/m | sup r^2|D^2 eps~|/m | sup wf W/m | sup wf r|grad|/m | sup wf r^2|D^2|/m | sup (W_eps - d_t eps)/m | sup W_K/m | sup W_dtK/m |")
print("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
for lo, hi in zip(edges[:-1], edges[1:]):
    sel = (r_a >= lo) & (r_a < hi)
    if not sel.any(): continue
    f = lambda v: up4(np.nanmax(v[sel]))
    print("| [%.3g, %.3g) | %d | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (lo, hi, sel.sum(), f(W00 / m), f(grad / m), f(d2 / m), f(wf * W00 / m), f(wf * grad / m), f(wf * d2 / m), f(Wemd / m), f(WK / m), f(WdtK / m)))
print("whole file: sup W/m %s at r = %.4g; sup r|grad|/m %s at r = %.4g; sup r^2|D^2|/m %s at r = %.4g; multiplier forms %s, %s, %s; (W_eps - d_t eps)/m %s; W_K/m %s; W_dtK/m %s" % (
    up4(np.nanmax(W00 / m)), r_a[np.nanargmax(W00 / m)], up4(np.nanmax(grad / m)), r_a[np.nanargmax(grad / m)], up4(np.nanmax(d2 / m)), r_a[np.nanargmax(d2 / m)],
    up4(np.nanmax(wf * W00 / m)), up4(np.nanmax(wf * grad / m)), up4(np.nanmax(wf * d2 / m)), up4(np.nanmax(Wemd / m)), up4(np.nanmax(WK / m)), up4(np.nanmax(WdtK / m))))
