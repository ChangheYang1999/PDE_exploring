"""Rigorous upper bounds (this lane's certificate data, floating summation with upward rounding) of the diagnostic X norms of the residual eps~ and of
eps~ - X.grad eps~ = eps~ - d_t eps~ from the per-cell derivative certificate (runs/cert_deriv_middle.json: per sub-cell [t_a, t_a + h] of the middle
region 0.00765 <= r <= 3413, W_i_j >= sum_N (2N+1)^j sup_cell |d_t^i eps_N|). With ||f||_X^2 = pi int e^{2t} w(t) sum_N [f_N^2 + (d_t f_N)^2 +
(2N+1)^2 f_N^2] dt, w = m^-2 (1+u^2)^-3/2, and sum_N a_N^2 <= (sum_N |a_N|)^2:
  ||eps~||_X^2 <= pi sum_cells h max_cell(e^{2t} w) [W_0_0^2 + W_1_0^2 + W_0_1^2],
  ||eps~ - d_t eps~||_X^2 <= pi sum_cells h max_cell(e^{2t} w) [(W_0_0 + W_1_0)^2 + (W_1_0 + W_2_0)^2 + (W_0_1 + W_1_1)^2].
e^{2t} w = L^2 u^-4 (1+u^2)^(3/2-k) is decreasing in u (log-derivative -4/u + (3-2k) u/(1+u^2) < 0), so its cell maximum is at the left end t_a.
The regions outside the middle band (r < 0.00765, r > 3413) are bounded from the outer/inner region certificates when their rows carry the same keys;
otherwise they are reported as not included. Usage: python3 src/xnorm_cert.py"""
import json, math, numpy as np


def _jopen(path):
    """Open a JSON result file for reading; falls back to path + '.gz' (the artifacts folder stores JSON files above 1 MB gzipped)."""
    import os, gzip
    if not os.path.exists(path) and os.path.exists(str(path) + ".gz"):
        return gzip.open(str(path) + ".gz", "rt")
    return open(path)
k = 0.17936053129375418; L = 7.651424601381517
def e2tw(t):
    u = math.exp(t) / L; return L ** 2 * u ** -4 * (1 + u * u) ** (1.5 - k)
def bound(rows, lo=None, hi=None):
    S_eps = 0.0; S_F = 0.0; n = 0
    for c in rows:
        ta = c["t_a"]; h = c["h"]
        if lo is not None and math.exp(ta + h) <= lo: continue
        if hi is not None and math.exp(ta) >= hi: continue
        wmax = e2tw(ta) * (1 + 1e-12)
        W00, W10, W20, W01, W11 = c["W_0_0"], c["W_1_0"], c["W_2_0"], c["W_0_1"], c["W_1_1"]
        S_eps += h * wmax * (W00 ** 2 + W10 ** 2 + W01 ** 2) * (1 + 1e-12)
        S_F += h * wmax * ((W00 + W10) ** 2 + (W10 + W20) ** 2 + (W01 + W11) ** 2) * (1 + 1e-12)
        n += 1
    return math.sqrt(math.pi * S_eps) * (1 + 1e-12), math.sqrt(math.pi * S_F) * (1 + 1e-12), n
mid = json.load(_jopen("runs/cert_deriv_middle.json"))
rows = mid["rows"] if "rows" in mid else mid["cells"]
out = {}
for name, lo, hi in (("r<2", None, 2.0), ("4<=r<=16", 4.0, 16.0), ("middle region 0.00765<=r<=3413", None, None)):
    e, F, n = bound(rows, lo, hi); out[name] = dict(eps_X_upper=e, eps_minus_dteps_X_upper=F, cells=n)
    print("%-32s cells %5d  ||eps~||_X <= %.4e   ||eps~ - X.grad eps~||_X <= %.4e" % (name, n, e, F))
for reg in ("outer", "inner"):
    try:
        d = json.load(_jopen("runs/cert_deriv_regions_%s.json" % reg)); r = d["rows"] if "rows" in d else d["cells"]
        e, F, n = bound(r); out[reg] = dict(eps_X_upper=e, eps_minus_dteps_X_upper=F, cells=n); print("%-32s cells %5d  ||eps~||_X <= %.4e   ||eps~ - X.grad eps~||_X <= %.4e" % (reg + " region", n, e, F))
    except Exception as ex: out[reg] = "not included: %s" % ex; print(reg, "region: not included:", ex)
tot_e = math.sqrt(sum(v["eps_X_upper"] ** 2 for v in out.values() if isinstance(v, dict) and "region" not in v)) if False else None
tot = {q: math.sqrt(sum(out[r][q] ** 2 for r in out if isinstance(out[r], dict) and r in ("middle region 0.00765<=r<=3413", "outer", "inner"))) for q in ("eps_X_upper", "eps_minus_dteps_X_upper")}
print("TOTAL over the certified regions (5.2e-5 <= r <= 8.2e10 if outer/inner included): ||eps~||_X <= %.4e, ||eps~ - X.grad eps~||_X <= %.4e" % (tot["eps_X_upper"], tot["eps_minus_dteps_X_upper"]))
out["total"] = tot; out["note"] = "upper bounds from the per-cell Wiener sums W_i_j of the derivative certificate (this lane's rigorous bounds, audit pending); sum_N a_N^2 <= (sum_N |a_N|)^2; cell maximum of e^{2t} w at the left end (monotone decreasing)"
json.dump(out, open("runs/xnorm/xnorm_cert.json", "w"), indent=1)
