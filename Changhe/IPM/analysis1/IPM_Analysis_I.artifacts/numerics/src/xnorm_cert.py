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
1e-12 inflation factors of version 1 (src/xnorm_cert_v1_float.py, kept for the record). Version 3 (shift 7, after astra/numrep4 round 2): k and L are
the stored binary64 values converted exactly; every cell start is the Arb ball (midpoint, radius) of the Green boundary files data/cert_green.npz
(tb, tb_rad), data/cert_outer_green.npz (t0 + tau with radii) and data/cert_inner_green.npz (tmin + tau), not the saved midpoint alone; the stored
h is an upper bound of the cell length (conservative). Version 2 kept as src/xnorm_cert_v2_arb.py.  Usage: python3 src/xnorm_cert.py"""
import json, math, os, gzip
from flint import arb, ctx
ctx.prec = 128
import numpy as np
_T = np.load(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data/trial_v2_h0.008.npz"))
k = arb(float(_T["k"])); L = arb(float(_T["L"]))      # the stored binary64 values, converted EXACTLY (arb from a Python float is exact)
assert float(k) == 0.17936053129375418 and float(L) == 7.651424601381517


def _jopen(path):
    if not os.path.exists(path) and os.path.exists(str(path) + ".gz"): return gzip.open(str(path) + ".gz", "rt")
    return open(path)


def e2tw(tball):
    u = tball.exp() / L
    return L ** 2 * u ** (-4) * (1 + u * u) ** (arb(3) / 2 - k)


def bound(rows, starts, lo=None, hi=None):
    """starts: dict ci -> arb ball enclosing the exact cell start t_a (from the Green boundary files); the weight maximum is evaluated at the
    ball (its lower end is the most pessimistic point, e^{2t} w being decreasing). h is the stored cell length (an upper bound, conservative)."""
    S_eps = arb(0); S_F = arb(0); n = 0
    for c in rows:
        ta = c["t_a"]; h = c["h"]
        if lo is not None and math.exp(ta + h) <= lo: continue
        if hi is not None and math.exp(ta) >= hi: continue
        tball = starts[c["ci"]]; assert tball.contains(arb(ta)) or abs(float(tball) - ta) < 1e-12, "cell start mismatch"
        wmax = e2tw(tball)
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
# exact cell starts as Arb balls from the Green boundary files (mid, rad doubles -> ball with both radii added)
if os.path.exists(os.path.join(lane, "data/cert_green.npz")):
    G = np.load(os.path.join(lane, "data/cert_green.npz")); Go = np.load(os.path.join(lane, "data/cert_outer_green.npz")); Gi = np.load(os.path.join(lane, "data/cert_inner_green.npz"))
    tb, tb_rad, t0, t0_rad, tau_o, tau_o_rad, tmin, tmin_rad, tau_i, tau_i_rad = G["tb"], G["tb_rad"], Go["t0"], Go["t0_rad"], Go["tau"], Go["tau_rad"], Gi["tmin"], Gi["tmin_rad"], Gi["tau"], Gi["tau_rad"]
    print("cell boundaries from the Green files")
else:   # the published artifacts ship the boundary balls alone (src/export_boundaries.py -> data/cell_boundaries.npz)
    B = np.load(os.path.join(lane, "data/cell_boundaries.npz"))
    tb, tb_rad, t0, t0_rad, tau_o, tau_o_rad, tmin, tmin_rad, tau_i, tau_i_rad = B["tb"], B["tb_rad"], B["t0"], B["t0_rad"], B["tau_out"], B["tau_out_rad"], B["tmin"], B["tmin_rad"], B["tau_in"], B["tau_in_rad"]
    print("cell boundaries from data/cell_boundaries.npz")
starts_mid = {i: arb(float(tb[i]), float(tb_rad[i])) for i in range(len(tb) - 1)}
starts_out = {i: arb(float(t0), float(t0_rad)) + arb(float(tau_o[i]), float(tau_o_rad[i])) for i in range(len(tau_o) - 1)}
starts_in = {i: arb(float(tmin), float(tmin_rad)) + arb(float(tau_i[i]), float(tau_i_rad[i])) for i in range(len(tau_i) - 1)}
out = {}; balls = {}
for name, lo, hi in (("r<2", None, 2.0), ("4<=r<=16", 4.0, 16.0), ("middle region rmin<=r<=R0", None, None)):
    e, F, n = bound(rows, starts_mid, lo, hi); balls[name] = (e, F); out[name] = dict(eps_X_upper=upper(e), eps_minus_dteps_X_upper=upper(F), cells=n, eps_ball=e.str(10), F_ball=F.str(10))
    print("%-32s cells %5d  ||eps~||_X <= %s   ||eps~ - X.grad eps~||_X <= %s" % (name, n, upper(e), upper(F)))
for reg, starts in (("outer", starts_out), ("inner", starts_in)):
    d = json.load(_jopen(os.path.join(lane, "runs/cert_deriv_regions_%s.json" % reg))); r = d["rows"] if "rows" in d else d["cells"]
    e, F, n = bound(r, starts); balls[reg] = (e, F); out[reg] = dict(eps_X_upper=upper(e), eps_minus_dteps_X_upper=upper(F), cells=n, eps_ball=e.str(10), F_ball=F.str(10))
    print("%-32s cells %5d  ||eps~||_X <= %s   ||eps~ - X.grad eps~||_X <= %s" % (reg + " region", n, upper(e), upper(F)))
tot_e = (balls["middle region rmin<=r<=R0"][0] ** 2 + balls["outer"][0] ** 2 + balls["inner"][0] ** 2).sqrt()
tot_F = (balls["middle region rmin<=r<=R0"][1] ** 2 + balls["outer"][1] ** 2 + balls["inner"][1] ** 2).sqrt()
print("TOTAL over the three finite regions r_T,in <= r <= r_T,out (5.1555e-5 <= r <= 8.2440e10; tails NOT included): ||eps~||_X <= %s, ||eps~ - X.grad eps~||_X <= %s" % (upper(tot_e), upper(tot_F)))
out["total_finite_regions"] = dict(eps_X_upper=upper(tot_e), eps_minus_dteps_X_upper=upper(tot_F), eps_ball=tot_e.str(12), F_ball=tot_F.str(12), r_range="[r_T,in, r_T,out] = [5.1555e-5, 8.2440e10]; the two tails are not included")
out["note"] = ("upper bounds from the per-cell majorants W_i_j of the derivative certificate (this lane's rigorous bounds, audit pending); sum_N a_N^2 <= (sum_N |a_N|)^2; "
               "cell maximum of e^{2t} w at the left end (monotone decreasing); all arithmetic in Arb balls at 128 bits with exact binary64 inputs and enclosed cell starts (v3), upper endpoints printed with ceiling rounding")
json.dump(out, open(os.path.join(lane, "runs/xnorm/xnorm_cert.json"), "w"), indent=1)
