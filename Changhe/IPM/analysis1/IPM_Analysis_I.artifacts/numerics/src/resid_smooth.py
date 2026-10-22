"""Residual-derivative-penalized refit on the FINE knots near P (floating point, evidence only; the experiment suggested by the astra
referee smooth1 and by the lead's item 4): minimize over the fine-knot coefficients delta of modes m < Mfit on the band
   sum_rows w^2 (eps + L delta)^2  +  lam * sum_rows w^2 [ (e^{-3t} D_t^3 (eps + L delta))^2 + ((2N+1)^3 e^{-3t} (eps + L delta))^2 ]
(rows = residual modes N < Mout on a uniform fine t-grid of the band; D_t^3 = third finite difference along t; w = 1/m(r)), with the
constraint c[delta] = 0, for several lam. Reports per lam the predicted weighted sup/L2 of the residual and of its third-derivative
proxy, and writes the updated trial for each lam (then evaluate with pdisc_explore / pdisc_norms).
Usage: python3 resid_smooth.py trial.npz t1 t2 Mfit Mout dt out_prefix lam1,lam2,...
"""
import os, sys, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.linalg import cho_factor, cho_solve
from modal_fit import Trial
from trial_green import TrialGreen
from lin_fast import FastAssembler
from gn_refit2 import coarse_space, to_fine


def main(path, t1, t2, Mfit, Mout, dt, out_prefix, lams):
    d = dict(np.load(path)); T = Trial(d)
    cknots, free, bases, fa, fb, cells = coarse_space(T, t1, t2, 1)        # stride 1: the fine space itself on the band
    nfree = len(free); print("fine-knot free functions per mode: %d (region [%.4f, %.4f]); modes %d -> %d columns" % (nfree, fa, fb, Mfit, nfree * Mfit), flush=True)
    t_eval = np.arange(fa, fb + 0.5 * dt, dt); Ne = len(t_eval); print("rows: %d radii x %d modes = %d" % (Ne, Mout, Ne * Mout), flush=True)
    r = np.exp(t_eval); u = r / T.L; mr = u ** 3 * (1 + u ** 2) ** ((T.k - 3) / 2); w = 1.0 / mr
    G = TrialGreen(T); t0 = time.time(); G.build(); LA = FastAssembler(G, t_eval, Mout)
    eps = G.residual_modes(t_eval)[:, :Mout]; print("Green + residual %.0fs" % (time.time() - t0), flush=True)
    cols = [(m, bases[j], "m%d_f%d" % (m, free[j])) for m in range(Mfit) for j in range(nfree)]
    t0 = time.time(); Mat, cvec = LA.assemble(cols, verbose=1000); print("assembly %d columns: %.0fs" % (len(cols), time.time() - t0), flush=True)
    nc = Mat.shape[1]
    # weights and derivative-penalty operator (acts on the (Ne, Mout) layout, flattened row-major: index i*Mout + N)
    W = np.repeat(w, Mout)
    e3 = np.exp(-3 * t_eval); twoN1 = 2.0 * np.arange(Mout) + 1.0
    def D3(vecs):
        """third t-difference along radii of an array (Ne*Mout, k) -> (Ne-3)*Mout rows, scaled by e^{-3t}/dt^3 and weighted by w; plus the angular
        third-derivative proxy rows (2N+1)^3 e^{-3t} w * value."""
        V = vecs.reshape(Ne, Mout, -1)
        d3 = (V[3:] - 3 * V[2:-1] + 3 * V[1:-2] - V[:-3]) / dt ** 3
        rad = (d3 * (e3[1:-2] * w[1:-2])[:, None, None]).reshape(-1, vecs.shape[1])
        ang = (V * (twoN1[None, :] ** 3)[:, :, None] * (e3 * w)[:, None, None]).reshape(-1, vecs.shape[1])
        return np.vstack([rad, ang])
    b = eps.ravel()
    t0 = time.time()
    Aw = Mat * W[:, None]; bw = b * W
    Pm = D3(Mat); pb = D3(b[:, None])[:, 0]
    cs = np.linalg.norm(Aw, axis=0); cs[cs == 0] = 1.0; Aw /= cs[None, :]; Pm /= cs[None, :]; crow = cvec / cs
    N0 = Aw.T @ Aw; g0 = Aw.T @ bw; N1 = Pm.T @ Pm; g1 = Pm.T @ pb
    print("normal matrices %.0fs" % (time.time() - t0), flush=True)
    base = dict(sup0=float(np.abs(bw).max()), l2_0=float(np.linalg.norm(bw)), d3_0=float(np.linalg.norm(pb)), d3sup_0=float(np.abs(pb).max()))
    print("start: weighted residual sup %.3e, L2 %.3e; third-derivative proxy L2 %.3e, sup %.3e" % (base["sup0"], base["l2_0"], base["d3_0"], base["d3sup_0"]), flush=True)
    results = []
    cw = 1e6 * max(np.abs(N0).max(), 1.0) ** 0.5
    for lam in lams:
        N = N0 + lam * N1 + np.outer(cw * crow, cw * crow); N[np.diag_indices_from(N)] += 1e-14 * N.diagonal().max()
        g = -(g0 + lam * g1)
        y = cho_solve(cho_factor(N, lower=True), g); delta = y / cs
        res_w = bw + Aw @ y; d3_new = pb + Pm @ y
        rec = dict(lam=lam, sup=float(np.abs(res_w).max()), l2=float(np.linalg.norm(res_w)), d3=float(np.linalg.norm(d3_new)), d3sup=float(np.abs(d3_new).max()), cdelta=float(cvec @ delta), delta_max=float(np.abs(delta).max()))
        # Wiener-like sup over radii: sum_N |res| per radius (weighted)
        rec["wiener_sup"] = float(np.abs(res_w).reshape(Ne, Mout).sum(1).max()); rec["wiener_sup0"] = float(np.abs(bw).reshape(Ne, Mout).sum(1).max())
        print("lam=%.1e: weighted residual sup %.3e (Wiener %.3e, from %.3e), L2 %.3e; D3 proxy L2 %.3e (from %.3e), sup %.3e; c[delta] %.1e; |delta| max %.2e" % (
            lam, rec["sup"], rec["wiener_sup"], rec["wiener_sup0"], rec["l2"], rec["d3"], base["d3_0"], rec["d3sup"], rec["cdelta"], rec["delta_max"]), flush=True)
        coef = delta.reshape(Mfit, nfree); dS, err = to_fine(T, cknots, free, coef, fa, fb)
        dd = dict(d); S = d["S"].copy(); S[:Mfit] += dS; dd["S"] = S
        np.savez_compressed("%s_lam%g.npz" % (out_prefix, lam), **dd); rec["file"] = "%s_lam%g.npz" % (out_prefix, lam); rec["reexpr_err"] = float(err)
        results.append(rec)
    json.dump(dict(path=path, t1=t1, t2=t2, Mfit=Mfit, Mout=Mout, dt=dt, Ne=Ne, nfree=nfree, base=base, results=results), open(out_prefix + "_summary.json", "w"), indent=1)
    print("done")


if __name__ == "__main__":
    a = sys.argv; main(a[1], float(a[2]), float(a[3]), int(a[4]), int(a[5]), float(a[6]), a[7], [float(x) for x in a[8].split(",")])
