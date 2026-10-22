"""Taylor-model residual bounds on the OUTER (r > R0) and INNER (r < rmin) sub-cells (SPEC item R0, regions r < r_min and r > R0),
using Certifier.cell_core with the exponential-polynomial terms of a_m exported by cert_green_outer.py.
Outer weight: W/m * (1+u)^delta with delta = 0.5 (SPEC v1); inner: W/m (and W/r^5 for R4).
Usage: python3 cert_resid_regions.py data/cert_green.npz trial.npz data/cert_outer_green.npz data/cert_inner_green.npz out.json
"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from flint import arb, ctx
from midrad import MR, succ, U
from cert_resid import Certifier


def recentre_terms(alphas, base_m, base_r, tau_a, alphas_rad=None, ctxprec=128):
    """Base terms (alpha, p(tau)) -> terms in sigma = tau - tau_a: e^{alpha tau_a} e^{alpha sigma} p(tau_a + sigma), in MR.
    alpha is an enclosing ball (double midpoint, radius alphas_rad); e^{alpha tau_a} from Arb; the re-centring is MR arithmetic.
    Returns terms (alpha as MR scalar, polynomial MR (deg+1, M))."""
    from math import comb
    out = []
    for it, alpha in enumerate(alphas):
        arad = float(alphas_rad[it]) if alphas_rad is not None else 0.0
        c = MR(base_m[it], base_r[it])                                 # (deg+1, M)
        deg = c.m.shape[0] - 1
        ea = MR.from_arb([(arb(float(alpha), arad) * tau_a).exp()])[0]
        d = MR.from_arb([tau_a])[0]
        rows_m = []; rows_r = []
        for q in range(deg + 1):
            acc = MR(np.zeros(c.m.shape[1]), np.zeros(c.m.shape[1]))
            dp = MR.exact(1.0)
            for pp in range(q, deg + 1):
                acc = acc + c[pp] * MR.exact(float(comb(pp, q))) * dp
                dp = dp * d
            acc = acc * ea
            rows_m.append(acc.m); rows_r.append(acc.r)
        out.append((MR(np.array(float(alpha)), np.array(arad)), MR(np.array(rows_m), np.array(rows_r))))
    return out


def region_run(C, path, region, out_rows, log_every=200):
    d = np.load(path); tau = MR(d["tau"], d["tau_rad"]); A = MR(d["A_mid"], d["A_rad"]); B = MR(d["B_mid"], d["B_rad"])
    alphas = d["alphas"]; base_m = d["base_mid"]; base_r = d["base_rad"]; nc = len(d["tau"]) - 1
    base_t = float(d["t0"]) if region == "outer" else float(d["tmin"]); base_r_ = float(d["t0_rad"]) if region == "outer" else float(d["tmin_rad"])
    ctx.prec = 128; k = arb(C.k); L = arb(C.L)
    t0 = time.time()
    for ci in range(nc):
        h = tau[ci + 1] - tau[ci]; h_up = h.mag()
        tau_a = arb(float(d["tau"][ci]), float(d["tau_rad"][ci]))
        ta = arb(base_t, base_r_) + tau_a
        e = ta.exp(); u = e / L
        m_ta = MR.from_arb([u ** 3 * (1 + u * u) ** ((k - 3) / 2)])[0]; wf = MR.from_arb([(1 + u).sqrt()])[0]; e_ta = MR.from_arb([e])[0]
        a_terms = recentre_terms(alphas, base_m, base_r, tau_a, d["alphas_rad"] if "alphas_rad" in d.files else None)
        res = C.cell_core(h_up, e_ta, a_terms, A[ci], B[ci], m_ta, wf)
        r_a = float(e.mid())
        res.update(ci=ci, region=region, t_a=float(ta.mid()), r_a=r_a, h=float(h_up))
        if region == "inner":
            res["W_over_r5"] = float(succ(res["W"] / np.nextafter(float((e ** 5).lower()), -np.inf)))
        out_rows.append(res)
        if ci % log_every == 0:
            print("%s cell %d/%d r=%.4g W=%.3e W/m=%.3e W/m*wfar=%.3e rem_eps=%.1e (%.0fs)" % (region, ci, nc, r_a, res["W"], res["W_over_m"], res["W_over_m_far"], res["rem_eps"], time.time() - t0), flush=True)
    return out_rows


def main(green, trial, outer, inner, out):
    C = Certifier(green, trial, Q=12)
    rows = []
    if os.path.exists(outer): region_run(C, outer, "outer", rows)
    if os.path.exists(inner): region_run(C, inner, "inner", rows)
    json.dump(dict(rows=rows), open(out, "w"))
    for region in ("outer", "inner"):
        rr = [r for r in rows if r["region"] == region]
        if not rr: continue
        key = "W_over_m_far" if region == "outer" else "W_over_m"
        v = np.array([r[key] for r in rr]); ra = np.array([r["r_a"] for r in rr])
        print("%s: %d cells; max W/m = %.4e at r = %.4g; max %s = %.4e at r = %.4g" % (region, len(rr), max(r["W_over_m"] for r in rr), ra[np.argmax([r["W_over_m"] for r in rr])], key, v.max(), ra[np.argmax(v)]))


if __name__ == "__main__":
    main(*sys.argv[1:6])
