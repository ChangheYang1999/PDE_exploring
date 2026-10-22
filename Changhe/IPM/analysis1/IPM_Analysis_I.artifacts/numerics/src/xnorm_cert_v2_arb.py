"""Rigorous upper bounds (this lane's certificate data; ALL arithmetic in Arb balls, upper endpoints taken) of the diagnostic X norms of the
residual eps~ and of eps~ - X.grad eps~ = eps~ - d_t eps~ from the per-cell derivative certificate (runs/cert_deriv_middle.json, 7809 sub-cells
[t_a, t_a + h] of the middle region rmin <= r <= R0; runs/cert_deriv_regions_outer.json, 8948 cells R0 <= r <= r_T,out; runs/cert_deriv_regions_inner.json,
2632 cells r_T,in <= r <= rmin), where W_i_j >= sum_N (2N+1)^j sup_cell |d_t^i eps_N| are the saved per-cell majorants (doubles, each an upper bound).
With ||f||_X^2 = pi int e^{2t} w(t) sum_N [f_N^2 + (d_t f_N)^2 + (2N+1)^2 f_N^2] dt, w = m^-2 (1+u^2)^-3/2, and sum_N a_N^2 <= (sum_N |a_N|)^2:
  ||eps~||_X^2 <= pi sum_cells h max_cell(e^{2t} w) [W_0_0^2 + W_1_0^2 + W_0_1^2],
  ||eps~ - d_t eps~||_X^2 <= pi sum_cells h max_cell(e^{2t} w) [(W_0_0 + W_1_0)^2 + (W_1_0 + W_2_0)^2 + (W_0_1 + W_1_1)^2].
e^{2t} w = L^2 u^-4 (1+u^2)^(3/2-k) is decreasing in u (log-derivative -4/u + (3-2k) u/(1+u^2) < 0 for u > 0 since (3-2k) u^2 < 4 (1+u^2)), so its
cell maximum is its value at the left end t_a (evaluated as an Arb ball from the exact double t_a). h is the stored double (an upper bound of the cell
length is not needed: h is the exact cell length used by the certificate). Output: runs/xnorm/xnorm_cert.json (upper endpoints of the Arb balls,
rounded outward to the printed digits) and the totals over the three finite regions r_T,in <= r <= r_T,out; the two tails are NOT included (no
derivative majorants there; the verifier's topic 178 bounds them separately).  Version 2 (shift 7): Arb arithmetic replaces the floating sums with
1e-12 inflation factors of version 1 (src/xnorm_cert_v1_float.py, kept for the record).  Usage: python3 src/xnorm_cert.py"""
import json, math, os, gzip
from flint import arb, ctx
ctx.prec = 128
k = arb("0.17936053129375418"); L = arb("7.651424601381517")      # the stored doubles, read as exact decimals (both are shortest repr of the doubles)
import numpy as np
assert float(k) == 0.17936053129375418 and float(L) == 7.651424601381517


def _jopen(path):
    if not os.path.exists(path) and os.path.exists(str(path) + ".gz"): return gzip.open(str(path) + ".gz", "rt")
    return open(path)


def e2tw(ta):
    u = arb(ta).exp() / L
    return L ** 2 * u ** (-4) * (1 + u * u) ** (arb(3) / 2 - k)


def bound(rows, lo=None, hi=None):
    S_eps = arb(0); S_F = arb(0); n = 0
    for c in rows:
        ta = c["t_a"]; h = c["h"]
        if lo is not None and math.exp(ta + h) <= lo: continue
        if hi is not None and math.exp(ta) >= hi: continue
        wmax = e2tw(ta)
        W00, W10, W20, W01, W11 = (arb(c[key]) for key in ("W_0_0", "W_1_0", "W_2_0", "W_0_1", "W_1_1"))
        S_eps += arb(h) * wmax * (W00 ** 2 + W10 ** 2 + W01 ** 2)
        S_F += arb(h) * wmax * ((W00 + W10) ** 2 + (W10 + W20) ** 2 + (W01 + W11) ** 2)
        n += 1
    return (arb.pi() * S_eps).sqrt(), (arb.pi() * S_F).sqrt(), n


def upper(b, digits=6):
    """decimal upper bound of an arb ball with `digits` significant digits (rounded up)."""
    from decimal import Decimal, ROUND_CEILING
    x = Decimal(b.upper().str(30, radius=False)); q = Decimal(1).scaleb(x.adjusted() - digits + 1)
    return format(x.quantize(q, rounding=ROUND_CEILING), "e")


lane = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
mid = json.load(_jopen(os.path.join(lane, "runs/cert_deriv_middle.json")))
rows = mid["rows"] if "rows" in mid else mid["cells"]
out = {}; balls = {}
for name, lo, hi in (("r<2", None, 2.0), ("4<=r<=16", 4.0, 16.0), ("middle region rmin<=r<=R0", None, None)):
    e, F, n = bound(rows, lo, hi); balls[name] = (e, F); out[name] = dict(eps_X_upper=upper(e), eps_minus_dteps_X_upper=upper(F), cells=n, eps_ball=e.str(10), F_ball=F.str(10))
    print("%-32s cells %5d  ||eps~||_X <= %s   ||eps~ - X.grad eps~||_X <= %s" % (name, n, upper(e), upper(F)))
for reg in ("outer", "inner"):
    d = json.load(_jopen(os.path.join(lane, "runs/cert_deriv_regions_%s.json" % reg))); r = d["rows"] if "rows" in d else d["cells"]
    e, F, n = bound(r); balls[reg] = (e, F); out[reg] = dict(eps_X_upper=upper(e), eps_minus_dteps_X_upper=upper(F), cells=n, eps_ball=e.str(10), F_ball=F.str(10))
    print("%-32s cells %5d  ||eps~||_X <= %s   ||eps~ - X.grad eps~||_X <= %s" % (reg + " region", n, upper(e), upper(F)))
tot_e = (balls["middle region rmin<=r<=R0"][0] ** 2 + balls["outer"][0] ** 2 + balls["inner"][0] ** 2).sqrt()
tot_F = (balls["middle region rmin<=r<=R0"][1] ** 2 + balls["outer"][1] ** 2 + balls["inner"][1] ** 2).sqrt()
print("TOTAL over the three finite regions r_T,in <= r <= r_T,out (5.1555e-5 <= r <= 8.2440e10; tails NOT included): ||eps~||_X <= %s, ||eps~ - X.grad eps~||_X <= %s" % (upper(tot_e), upper(tot_F)))
out["total_finite_regions"] = dict(eps_X_upper=upper(tot_e), eps_minus_dteps_X_upper=upper(tot_F), eps_ball=tot_e.str(12), F_ball=tot_F.str(12), r_range="[r_T,in, r_T,out] = [5.1555e-5, 8.2440e10]; the two tails are not included")
out["note"] = ("upper bounds from the per-cell majorants W_i_j of the derivative certificate (this lane's rigorous bounds, audit pending); sum_N a_N^2 <= (sum_N |a_N|)^2; "
               "cell maximum of e^{2t} w at the left end (monotone decreasing); all arithmetic in Arb balls at 128 bits, upper endpoints printed with ceiling rounding")
json.dump(out, open(os.path.join(lane, "runs/xnorm/xnorm_cert.json"), "w"), indent=1)
