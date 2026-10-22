"""Gauss-Newton re-solve in a COARSE spline space defined on the ORIGINAL knot vector (floating point, evidence only).
The coarse space: degree-7 B-splines on every `stride`-th original knot of the band t in [t1, t2] (a subspace of the trial's spline space).
Unknowns: coarse coefficients of modes m in [m_lo, m_hi) whose basis functions meet the band. The linearization L (src/lin_fast.py, full
nonlocal operator with the (c[h]/3) X.grad rho~ term) is assembled on these coarse basis functions; rows = residual modes N < Mout at
collocation radii (5 per coarse cell on the affected region, coarse outside), weighted by 1/m(r); constraint c[delta] = 0; damped least
squares by SVD (ncol <= 6000) or Cholesky normal equations. The update is re-expressed exactly on the original knots.
Usage: python3 gn_refit2.py start.npz t1 t2 stride m_lo m_hi Mout damp out.npz [iters]
"""
import os, sys, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from math import factorial
from scipy.interpolate import BSpline
from modal_fit import Trial
from trial_green import TrialGreen
from lin_assembly import ExpPolyBasis
from lin_fast import FastAssembler


def coarse_space(T, t1, t2, stride):
    p = T.p; kn = T.knots; kin = kn[p + 1:-(p + 1)]
    inband = np.where((kin >= t1) & (kin <= t2))[0]
    keep = np.unique(np.r_[np.arange(0, inband[0]), inband[::stride], inband[-1], np.arange(inband[-1] + 1, len(kin))])
    cknots = np.r_[np.full(p + 1, T.tmin), kin[keep], np.full(p + 1, T.t0)]
    lo, hi = kin[inband[0]], kin[inband[-1]]
    nbc = len(cknots) - p - 1
    free = [i for i in range(nbc) if not (cknots[i + p + 1] <= lo + 1e-12 or cknots[i] >= hi - 1e-12)]
    cells = np.unique(cknots); cells = cells[(cells >= T.tmin) & (cells <= T.t0)]
    spl = BSpline(cknots, np.eye(nbc), p, extrapolate=True)
    tab = np.stack([spl(cells[:-1], nu=nu) / factorial(nu) for nu in range(p + 1)], axis=-1)
    bases = [ExpPolyBasis([(cells[ci], cells[ci + 1], 0.0, tab[ci, i]) for ci in range(len(cells) - 1) if np.any(tab[ci, i])]) for i in free]
    fa, fb = cknots[free[0]], cknots[free[-1] + p + 1]
    return cknots, np.array(free), bases, fa, fb, cells


def to_fine(T, cknots, free, coef_by_mode, fa, fb):
    """Express sum_i coef[m, i] * coarse basis_i on the fine knot vector of T (exact: subspace); returns dS (modes, nb_fine)."""
    p = T.p; kn = T.knots; nb = len(kn) - p - 1; nbc = len(cknots) - p - 1
    cells = np.unique(kn); cells = cells[(cells >= fa) & (cells <= fb)]
    tg = np.unique(np.concatenate([np.linspace(a, b, 12) for a, b in zip(cells[:-1], cells[1:])]))
    Bc = np.nan_to_num(BSpline(cknots, np.eye(nbc), p, extrapolate=False)(tg))[:, free]
    vals = Bc @ coef_by_mode.T                                   # (ng, modes)
    ffree = [i for i in range(nb) if not (kn[i + p + 1] <= fa + 1e-12 or kn[i] >= fb - 1e-12)]
    Bf = np.nan_to_num(BSpline(kn, np.eye(nb), p, extrapolate=False)(tg))[:, ffree]
    c = np.linalg.lstsq(Bf, vals, rcond=None)[0]
    err = np.abs(Bf @ c - vals).max()
    dS = np.zeros((coef_by_mode.shape[0], nb)); dS[:, ffree] = c.T
    return dS, err


def main(start, t1, t2, stride, m_lo, m_hi, Mout, damp, out, iters=1):
    d = dict(np.load(start)); Ts = Trial(d)
    cknots, free, bases, fa, fb, ccells = coarse_space(Ts, t1, t2, stride)
    nfree = len(free); nm = m_hi - m_lo
    print("coarse space: %d free functions per mode (affected region [%.4f, %.4f]); modes [%d, %d) -> %d columns" % (nfree, fa, fb, m_lo, m_hi, nfree * nm), flush=True)
    cc = ccells[(ccells >= fa) & (ccells <= fb)]
    tb = np.concatenate([np.linspace(a, b, 7)[1:-1] for a, b in zip(cc[:-1], cc[1:])])
    t_eval = np.unique(np.r_[np.linspace(Ts.tmin - 2.0, Ts.tmin, 4), np.linspace(Ts.tmin, fa, 18)[1:-1], tb, np.linspace(fb, Ts.t0, 18)[1:-1], np.linspace(Ts.t0, Ts.t0 + 6, 6)])
    Ne = len(t_eval); print("collocation radii %d (affected region %d); rows %d" % (Ne, len(tb), Ne * Mout), flush=True)
    r = np.exp(t_eval); u = r / Ts.L; mr = u ** 3 * (1 + u ** 2) ** ((Ts.k - 3) / 2); wrow = np.repeat(1.0 / mr, Mout)
    band_rows = np.repeat((t_eval >= fa) & (t_eval <= fb), Mout)
    hist = []
    for it in range(iters):
        G = TrialGreen(Ts); t0 = time.time(); G.build(); LA = FastAssembler(G, t_eval, Mout)
        eps = G.residual_modes(t_eval)[:, :Mout]; print("iter %d: Green + residual %.0fs" % (it, time.time() - t0), flush=True)
        cols = [(m, bases[j], "m%d_c%d" % (m, j)) for m in range(m_lo, m_hi) for j in range(nfree)]
        t0 = time.time(); Mat, cvec = LA.assemble(cols, verbose=1000); print("assembly %d columns: %.0fs" % (len(cols), time.time() - t0), flush=True)
        b = -(eps.ravel() * wrow); Mat *= wrow[:, None]
        cw = 1e6 * np.abs(Mat).max() / max(np.abs(cvec).max(), 1e-300)
        cs = np.linalg.norm(Mat, axis=0); cs[cs == 0] = 1.0; Mat /= cs[None, :]; crow = cw * cvec / cs
        nr, nc = Mat.shape; t0 = time.time()
        if nc <= 6000:
            Afull = np.vstack([Mat, crow[None, :]]); U_, S_, Vt = np.linalg.svd(Afull, full_matrices=False)
            uy = U_.T @ np.r_[b, 0.0]; y = Vt.T @ (S_ / (S_ ** 2 + damp ** 2) * uy)
            print("  SVD solve %.0fs: sigma max %.3e min %.3e; below 1e-6 max: %d; below 1e-3 max: %d" % (time.time() - t0, S_[0], S_[-1], int((S_ < 1e-6 * S_[0]).sum()), int((S_ < 1e-3 * S_[0]).sum())), flush=True)
            del Afull, U_
        else:
            from scipy.linalg import cho_factor, cho_solve
            N = Mat.T @ Mat + np.outer(crow, crow); N[np.diag_indices_from(N)] += damp ** 2
            y = cho_solve(cho_factor(N, lower=True), Mat.T @ b); del N
            print("  normal-equation solve %.0fs" % (time.time() - t0), flush=True)
        delta = y / cs
        pred = Mat @ y - b
        res0, res1 = np.linalg.norm(b), np.linalg.norm(pred)
        print("iter %d: weighted residual norm %.3e -> %.3e (linear prediction); affected-region max %.3e -> %.3e; outside max %.3e -> %.3e; c[delta] = %.2e; |delta| max %.2e" % (
            it, res0, res1, np.abs(b[band_rows]).max(), np.abs(pred[band_rows]).max(), np.abs(b[~band_rows]).max(), np.abs(pred[~band_rows]).max(), cvec @ delta, np.abs(delta).max()), flush=True)
        hist.append(dict(res0=float(res0), res1=float(res1), band_max0=float(np.abs(b[band_rows]).max()), band_max1=float(np.abs(pred[band_rows]).max()), cdelta=float(cvec @ delta)))
        coef = delta.reshape(nm, nfree)
        dS, err = to_fine(Ts, cknots, free, coef, fa, fb); print("  re-expression on the fine knots: error %.1e" % err, flush=True)
        S = d["S"].copy(); S[m_lo:m_hi] += dS; d["S"] = S; Ts = Trial(d); np.savez_compressed(out, **d)
        del Mat
    json.dump(dict(start=start, t1=t1, t2=t2, stride=stride, m_lo=m_lo, m_hi=m_hi, Mout=Mout, damp=damp, Ne=Ne, nfree=nfree, hist=hist), open(out.replace(".npz", "_gn.json"), "w"), indent=1)
    print("saved", out)


if __name__ == "__main__":
    a = sys.argv; main(a[1], float(a[2]), float(a[3]), int(a[4]), int(a[5]), int(a[6]), int(a[7]), float(a[8]), a[9], int(a[10]) if len(a) > 10 else 1)
