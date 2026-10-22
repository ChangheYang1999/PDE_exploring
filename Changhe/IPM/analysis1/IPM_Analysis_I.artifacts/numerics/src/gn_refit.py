"""Gauss-Newton re-solve of the profile equation in a COARSE spline space on a band (floating point, evidence only).
Start: a band-smoothed trial (src/smooth_band.py output). Unknowns: the spline coefficients of modes m < Mfit whose basis functions
meet the band (same 'free' set as smooth_band). Linearization L assembled by src/lin_assembly.py (full nonlocal operator, including the
(c[h]/3) X.grad rho~ term); rows: residual modes N < Mout at collocation radii (4 per coarse cell on the band, coarse outside), weighted
by 1/m(r), m = u^3 (1+u^2)^{(k-3)/2}; constraint c[delta] = 0 (so c_l = 1/k stays exact); damped least squares (LSQR) with
column scaling. Output: updated trial npz, predicted residual reduction.
Usage: python3 gn_refit.py base.npz smooth.npz t1 t2 Mfit Mout damp out.npz [iters]
"""
import os, sys, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from math import factorial
from scipy.interpolate import BSpline
from scipy.sparse.linalg import lsqr
from modal_fit import Trial
from trial_green import TrialGreen
from lin_assembly import ExpPolyBasis
from lin_fast import FastAssembler as LinAssembler


def free_set(T0, Ts, t1, t2):
    p = Ts.p; kin0 = T0.knots[p + 1:-(p + 1)]
    lo = kin0[kin0 < t1].max(); hi = kin0[kin0 > t2].min()
    nk = Ts.knots; nb = len(nk) - p - 1
    free = [i for i in range(nb) if not (nk[i + p + 1] <= lo + 1e-12 or nk[i] >= hi - 1e-12)]
    return np.array(free), lo, hi


def spline_bases(Ts, idx):
    """ExpPolyBasis (polynomial pieces per cell) of the B-splines idx of Ts's knot vector."""
    p = Ts.p; nk = Ts.knots; nb = len(nk) - p - 1
    cells = np.unique(nk); cells = cells[(cells >= Ts.tmin) & (cells <= Ts.t0)]
    spl = BSpline(nk, np.eye(nb), p, extrapolate=True)
    tab = np.stack([spl(cells[:-1], nu=nu) / factorial(nu) for nu in range(p + 1)], axis=-1)      # (ncell, nb, p+1)
    out = []
    for i in idx:
        pieces = [(cells[ci], cells[ci + 1], 0.0, tab[ci, i]) for ci in range(len(cells) - 1) if np.any(tab[ci, i])]
        out.append(ExpPolyBasis(pieces))
    return out


def main(base, smooth, t1, t2, Mfit, Mout, damp, out, iters=1):
    T0 = Trial(dict(np.load(base))); d = dict(np.load(smooth)); Ts = Trial(d)
    free, lo, hi = free_set(T0, Ts, t1, t2); p = Ts.p
    fa, fb = Ts.knots[free[0]], Ts.knots[free[-1] + p + 1]
    print("free basis functions per mode: %d (supports within [%.4f, %.4f]); unknown modes %d -> %d columns" % (len(free), fa, fb, Mfit, len(free) * Mfit), flush=True)
    bases = spline_bases(Ts, free)
    # collocation radii
    cells = np.unique(Ts.knots); cells = cells[(cells >= fa) & (cells <= fb)]
    tb = np.concatenate([np.linspace(a, b, 6)[1:-1] for a, b in zip(cells[:-1], cells[1:])])
    t_eval = np.unique(np.r_[np.linspace(Ts.tmin - 2.0, Ts.tmin, 4), np.linspace(Ts.tmin, fa, 18)[1:-1], tb, np.linspace(fb, Ts.t0, 18)[1:-1], np.linspace(Ts.t0, Ts.t0 + 6, 6)])
    Ne = len(t_eval); print("collocation radii: %d (band %d); rows %d" % (Ne, len(tb), Ne * Mout), flush=True)
    r = np.exp(t_eval); u = r / Ts.L; mr = u ** 3 * (1 + u ** 2) ** ((Ts.k - 3) / 2); wrow = np.repeat(1.0 / mr, Mout)
    hist = []
    for it in range(iters):
        G = TrialGreen(Ts); t0 = time.time(); G.build(); print("iter %d: Green build %.0fs" % (it, time.time() - t0), flush=True)
        LA = LinAssembler(G, t_eval, Mout)
        eps = G.residual_modes(t_eval)[:, :Mout]
        cols = [(m, bases[j], "m%d_b%d" % (m, free[j])) for m in range(Mfit) for j in range(len(free))]
        t0 = time.time(); Mat, cvec = LA.assemble(cols, verbose=500); print("assembly %d columns: %.0fs" % (len(cols), time.time() - t0), flush=True)
        # weighted system with the constraint row c[delta] = 0 (in place, memory-lean; constraint via a LinearOperator)
        from scipy.sparse.linalg import LinearOperator
        b = -(eps.ravel() * wrow)
        Mat *= wrow[:, None]
        cw = 1e6 * np.abs(Mat).max() / max(np.abs(cvec).max(), 1e-300)
        cs = np.linalg.norm(Mat, axis=0); cs[cs == 0] = 1.0; Mat /= cs[None, :]
        crow = cw * cvec / cs
        nr, nc = Mat.shape
        Aop = LinearOperator((nr + 1, nc), matvec=lambda x: np.r_[Mat @ x, crow @ x], rmatvec=lambda y: Mat.T @ y[:-1] + crow * y[-1], dtype=float)
        b = np.r_[b, 0.0]
        t0 = time.time()
        np.save(out.replace(".npz", "_mat_iter%d.npy" % it), Mat); np.save(out.replace(".npz", "_rhs_iter%d.npy" % it), np.r_[b, cs, crow])
        if nc <= 6000:
            # direct damped least squares via the SVD of the augmented matrix (reliable; also reports the singular spectrum)
            Afull = np.vstack([Mat, crow[None, :]])
            U_, S_, Vt = np.linalg.svd(Afull, full_matrices=False)
            uy = U_.T @ b
            y = Vt.T @ (S_ / (S_ ** 2 + damp ** 2) * uy)
            print("  direct SVD solve %.0fs: singular values max %.3e, min %.3e; count below 1e-6*max: %d, below 1e-3*max: %d" % (
                time.time() - t0, S_[0], S_[-1], int((S_ < 1e-6 * S_[0]).sum()), int((S_ < 1e-3 * S_[0]).sum())), flush=True)
            sol = (y, 0, 0)
            del Afull, U_
        else:
            # normal equations with damping (Cholesky); Mat is column-scaled so damp is relative
            N = Mat.T @ Mat + np.outer(crow, crow); N[np.diag_indices_from(N)] += damp ** 2
            g = Mat.T @ b[:-1] + crow * b[-1]
            from scipy.linalg import cho_factor, cho_solve
            y = cho_solve(cho_factor(N, lower=True), g); sol = (y, 0, 0); del N
            print("  normal-equation solve %.0fs" % (time.time() - t0), flush=True)
        delta = y / cs
        pred = Aop.matvec(y) - b
        band_rows = np.repeat((t_eval >= fa) & (t_eval <= fb), Mout)
        res0 = np.linalg.norm(b[:-1]); res1 = np.linalg.norm(pred[:-1])
        bmax0 = np.abs(b[:-1][band_rows]).max(); bmax1 = np.abs(pred[:-1][band_rows]).max()
        omax0 = np.abs(b[:-1][~band_rows]).max(); omax1 = np.abs(pred[:-1][~band_rows]).max()
        print("iter %d: solve %.0fs; weighted residual norm %.3e -> %.3e (linear prediction); band max %.3e -> %.3e; outside max %.3e -> %.3e; c[delta] = %.2e; |delta| max %.2e" % (
            it, time.time() - t0, res0, res1, bmax0, bmax1, omax0, omax1, cvec @ delta, np.abs(delta).max()), flush=True)
        hist.append(dict(res0=res0, res1=res1, band_max0=bmax0, band_max1=bmax1, out_max0=omax0, out_max1=omax1, cdelta=float(cvec @ delta)))
        # update the trial
        S = d["S"].copy()
        for m in range(Mfit):
            S[m, free] += delta[m * len(free):(m + 1) * len(free)]
        d["S"] = S; Ts = Trial(d)
        np.savez_compressed(out, **d)
    json.dump(dict(base=base, smooth=smooth, t1=t1, t2=t2, Mfit=Mfit, Mout=Mout, damp=damp, Ne=Ne, free=len(free), hist=hist), open(out.replace(".npz", "_gn.json"), "w"), indent=1)
    print("saved", out)


if __name__ == "__main__":
    a = sys.argv
    main(a[1], a[2], float(a[3]), float(a[4]), int(a[5]), int(a[6]), float(a[7]), a[8], int(a[9]) if len(a) > 9 else 1)
