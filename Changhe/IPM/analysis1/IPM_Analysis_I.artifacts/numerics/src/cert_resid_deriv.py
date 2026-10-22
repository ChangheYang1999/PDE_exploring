"""Derivative certificate (SPEC v2 items R1, R3, R5): Taylor models of d_t^i eps_N (i <= nder) on the middle-region sub-cells,
and on the outer/inner sub-cells if their Arb boundary files exist. nder = 2 everywhere; nder = 5 on the sub-cells meeting the
disc |X - P| < x_*/4 (r in [0.75 x_*, 1.25 x_*]).  Per sub-cell: W_i_j = sum_N (2N+1)^j sup|d_t^i eps_N| (i + j <= nder),
W_eps_minus_dteps, W_K and W1_K (K~ = rho~ - X.grad rho~ modes), W_dtK, m_inf, wf_sup.
Usage: python3 cert_resid_deriv.py data/cert_green.npz trial.npz out_prefix [outer_green.npz inner_green.npz]
"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from flint import arb, ctx
from midrad import MR, succ
from cert_resid import Certifier
from cert_resid_regions import recentre_terms

XSTAR = 8.600063805


def run_middle(C, out_prefix):
    rows = []; t0 = time.time()
    lo, hi = np.log(0.75 * XSTAR), np.log(1.25 * XSTAR)
    for ci in range(C.nc):
        ta = C.tb.m[ci]; tb = C.tb.m[ci + 1]
        nder = 5 if (tb > lo and ta < hi) else 2
        r = C.cell_deriv(ci, nder=nder); r["nder"] = nder; rows.append(r)
        if ci % 100 == 0:
            print("middle cell %d/%d r=%.4g nder=%d W=%.3e W_1_0=%.3e W_0_1=%.3e W_2_0=%.3e W_K=%.3e (%.0fs)" % (
                ci, C.nc, np.exp(ta), nder, r["W_0_0"], r["W_1_0"], r["W_0_1"], r["W_2_0"], r["W_K"], time.time() - t0), flush=True)
            json.dump(dict(rows=rows, done=False), open(out_prefix + "_middle.json", "w"))
    json.dump(dict(rows=rows, done=True, time=time.time() - t0), open(out_prefix + "_middle.json", "w"))
    print("middle done %.0fs" % (time.time() - t0), flush=True)


def run_region(C, path, region, out_prefix):
    d = np.load(path); tau = MR(d["tau"], d["tau_rad"]); A = MR(d["A_mid"], d["A_rad"]); B = MR(d["B_mid"], d["B_rad"])
    alphas = d["alphas"]; base_m = d["base_mid"]; base_r = d["base_rad"]; nc = len(d["tau"]) - 1
    base_t = float(d["t0"]) if region == "outer" else float(d["tmin"]); base_r_ = float(d["t0_rad"]) if region == "outer" else float(d["tmin_rad"])
    ctx.prec = 128; k = arb(C.k); L = arb(C.L); rows = []; t0 = time.time()
    for ci in range(nc):
        h = tau[ci + 1] - tau[ci]; h_up = h.mag()
        tau_a = arb(float(d["tau"][ci]), float(d["tau_rad"][ci])); ta = arb(base_t, base_r_) + tau_a
        e = ta.exp(); u = e / L
        m_ta = MR.from_arb([u ** 3 * (1 + u * u) ** ((k - 3) / 2)])[0]; wf = MR.from_arb([(1 + u).sqrt()])[0]; e_ta = MR.from_arb([e])[0]
        a_terms = recentre_terms(alphas, base_m, base_r, tau_a, d["alphas_rad"] if "alphas_rad" in d.files else None)
        r = C.cell_core_deriv(h_up, e_ta, a_terms, A[ci], B[ci], m_ta, wf, 2)
        r.update(ci=ci, region=region, t_a=float(ta.mid()), r_a=float(e.mid()), h=float(h_up), nder=2); rows.append(r)
        if ci % 200 == 0:
            print("%s cell %d/%d r=%.4g W=%.3e W_1_0=%.3e W_0_1=%.3e (%.0fs)" % (region, ci, nc, r["r_a"], r["W_0_0"], r["W_1_0"], r["W_0_1"], time.time() - t0), flush=True)
    json.dump(dict(rows=rows, done=True, time=time.time() - t0), open(out_prefix + "_%s.json" % region, "w"))
    print("%s done %.0fs" % (region, time.time() - t0), flush=True)


if __name__ == "__main__":
    a = sys.argv
    C = Certifier(a[1], a[2], Q=12)
    if os.environ.get("DERIV_SKIP_MIDDLE") != "1": run_middle(C, a[3])      # DERIV_SKIP_MIDDLE=1: regions only (the middle is in runs/cert_deriv_middle.json)
    if len(a) > 5:
        if os.path.exists(a[4]): run_region(C, a[4], "outer", a[3])
        if os.path.exists(a[5]): run_region(C, a[5], "inner", a[3])
