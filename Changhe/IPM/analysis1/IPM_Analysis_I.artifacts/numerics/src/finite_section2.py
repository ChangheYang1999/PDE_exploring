"""SPEC v2 item C2 (floating point, evidence only), trial-type basis version.
Finite sections of the unnormalized linearization  L h = (V~.grad - 1) h + W[h].grad rho~,  W[h] = U[h] + (c[h]/3) X,
for h = x^2 y sum_{m<Mh} b_m(r) cos(2m theta) with b_m in the trial's own three-region exponential-polynomial basis at reduced
resolution: inner powers e^{2j (t - tmin)} (j = 1..7; the constant only for m = 0, i.e. the J-direction is included: unnormalized),
degree-7 B-splines in t on every `stride`-th knot of the trial, outer power laws e^{alpha_q (t - t0)} (10). No join
constraints are imposed on h (the basis is a superset of the join-constrained space; K~ = rho~ - X.grad rho~ lies in its span
up to the spline-derivative approximation). Each basis function's Green data are closed form (half-infinite and cell
integrals, src/expoly.scaled_integral).
Rows: modal coefficients (L h)_N(t_i) for N < Mout at collocation radii t_i (inner: 6 points; middle: midpoints of the
coarse cells; outer: 40 log-spaced points to 1e5 L), weighted by w_Y(r) = (1+u)^(gamma-k)/m(r) * (1 + (2N+1)^2)^(s/2);
columns weighted by a proxy of the X norm (sup of |basis| e^{3t}/m ... see code). SVD -> smallest singular values and the
overlap of the right singular vectors with K~'s coefficient vector.
Usage: python3 finite_section2.py trial.npz Mh stride s out.json
"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from math import factorial
from scipy.interpolate import BSpline
from modal_fit import Trial, OUTER_JL, NIN, outer_alphas
from trial_green import TrialGreen
from expoly import scaled_integral

P = 7


class ExpPolyBasis:
    """One scalar radial basis function given as exponential-polynomial pieces: list of (t_lo, t_hi, alpha, coeffs) with
    coeffs ascending in sigma = t - t_lo (t_lo may be -inf: then sigma = t - t_hi <= 0; t_hi may be +inf: sigma = t - t_lo)."""
    def __init__(self, pieces):
        self.pieces = pieces

    def eval(self, t, nu=0):
        t = np.atleast_1d(t); out = np.zeros_like(t)
        for (a, b, alpha, c) in self.pieces:
            if np.isinf(a):
                sel = t < b; sig = t[sel] - b
            elif np.isinf(b):
                sel = t >= a; sig = t[sel] - a
            else:
                sel = (t >= a) & (t < b); sig = t[sel] - a
            if not sel.any(): continue
            cc = np.array(c, float)
            for _ in range(nu):
                dc = alpha * cc
                if len(cc) > 1: dc[:-1] += cc[1:] * np.arange(1, len(cc))
                cc = dc
            pv = np.zeros_like(sig)
            for j in range(len(cc) - 1, -1, -1): pv = pv * sig + cc[j]
            out[sel] = np.exp(alpha * sig) * pv
        return out


def build_basis(T, stride):
    """List of (mode m, ExpPolyBasis) for the h-basis. Returns list of (m, basis, label)."""
    tmin, t0 = T.tmin, T.t0
    kn_int = T.knots[P + 1:-(P + 1)][::stride]
    knots = np.r_[np.full(P + 1, tmin), kn_int, np.full(P + 1, t0)]
    nb = len(knots) - P - 1
    spl = BSpline(knots, np.eye(nb), P, extrapolate=True)
    starts = knots[P:-(P + 1)]
    starts = np.unique(np.r_[tmin, kn_int])
    tab = np.stack([spl(starts, nu=nu) / factorial(nu) for nu in range(P + 1)], axis=-1)      # (ncell, nb, P+1)
    cells = list(zip(starts, np.r_[starts[1:], t0]))
    alphas = outer_alphas(T.k)
    radial = []
    for j in range(1, NIN + 1):
        radial.append((ExpPolyBasis([(-np.inf, tmin, 2.0 * j, [1.0])]), "in%d" % j))
    for b in range(nb):
        pieces = [(a, c_, 0.0, tab[ci, b]) for ci, (a, c_) in enumerate(cells) if np.any(tab[ci, b])]
        radial.append((ExpPolyBasis(pieces), "sp%d" % b))
    for q, al in enumerate(alphas):
        radial.append((ExpPolyBasis([(t0, np.inf, float(al), [1.0])]), "out%d" % q))
    return radial, knots


def green_single(G, m, basis, t_eval):
    """A_n, B_n (n = 1..Nf) of the single-mode density a_m = basis (other modes zero) at points t_eval, closed forms."""
    n = G.n; Nf = G.Nf; A = np.zeros((len(t_eval), Nf)); B = np.zeros((len(t_eval), Nf))
    for (a, b, alpha, c) in basis.pieces:
        cmat = np.zeros((len(c), G.M)); cmat[:, m] = c
        if np.isinf(a):            # inner piece, sigma = t - b (<= 0)
            ft = G._f_expoly([(alpha, cmat)], np.exp(2 * b)); base = b
        else:
            ft = G._f_expoly([(alpha, cmat)], np.exp(2 * a)); base = a
        for it, t in enumerate(t_eval):
            for al2, fc in ft:
                lam = (2 * n + 2) + al2; mu = (2 - 2 * n) + al2
                for p in range(fc.shape[0]):
                    if not np.any(fc[p]): continue
                    unit = np.zeros(fc.shape[0]); unit[p] = 1.0
                    if np.isinf(a):
                        # A: int_{-inf}^{min(t,b)} ; B: int_{max(t,-inf)=t}^{b} if t < b
                        hi = min(t, b) - base
                        A[it] += fc[p] * scaled_integral(lam, unit, -np.inf, hi, -2 * n * (t - base)) * np.exp(2 * base)
                        if t < b:
                            B[it] += fc[p] * scaled_integral(mu, unit, t - base, 0.0, 2 * n * (t - base)) * np.exp(2 * base)
                    elif np.isinf(b):
                        if t > a:
                            A[it] += fc[p] * scaled_integral(lam, unit, 0.0, t - base, -2 * n * (t - base)) * np.exp(2 * base)
                        lo = max(t, a) - base
                        B[it] += fc[p] * scaled_integral(mu, unit, lo, np.inf, 2 * n * (t - base)) * np.exp(2 * base)
                    else:
                        if t > a:
                            A[it] += fc[p] * scaled_integral(lam, unit, 0.0, min(t, b) - base, -2 * n * (t - base)) * np.exp(2 * base)
                        if t < b:
                            B[it] += fc[p] * scaled_integral(mu, unit, max(t, a) - base, b - base, 2 * n * (t - base)) * np.exp(2 * base)
    return A, B


def main(trial, Mh, stride, s_order, out):
    T = Trial(np.load(trial)); G = TrialGreen(T); G.build(); k = T.k; L = T.L; c_l = 1.0 / k
    radial, knots = build_basis(T, stride); nrad = len(radial)
    # collocation radii
    kn_int = knots[P + 1:-(P + 1)]
    t_mid = 0.5 * (np.r_[T.tmin, kn_int][:-1] + np.r_[T.tmin, kn_int][1:]); t_mid = np.r_[t_mid, 0.5 * (kn_int[-1] + T.t0)]
    t_eval = np.r_[T.tmin - np.linspace(0.3, 3.0, 6)[::-1], t_mid, T.t0 + np.linspace(0.05, np.log(1e5 * L / T.R0), 40)]
    r_eval = np.exp(t_eval); Ne = len(t_eval)
    Rt_, Rtt = G.rho_modes(t_eval); psi_t, dpsi_t = G.psi_at(t_eval); n = G.n
    Mout = Mh + 2; ncol = Mh * nrad + 1; nrow = Ne * Mout
    print("basis: %d radial functions x %d modes (+1 constant) = %d columns; %d radii x %d output modes = %d rows" % (nrad, Mh, ncol, Ne, Mout, nrow), flush=True)
    Mat = np.zeros((nrow, ncol)); colw = np.ones(ncol); t0 = time.time()
    e_m = np.exp(-t_eval); e_2m = np.exp(-2 * t_eval); e3 = np.exp(3 * t_eval)
    u = r_eval / L; mr = u ** 3 * (1 + u ** 2) ** ((k - 3) / 2)
    def column(m, basis):
        bval = basis.eval(t_eval, 0); bder = basis.eval(t_eval, 1)
        a_vec = np.zeros((Ne, G.M)); a_vec[:, m] = bval; ad_vec = np.zeros((Ne, G.M)); ad_vec[:, m] = bder
        Rh = e3[:, None] * G.R_from_a(a_vec); Rht = e3[:, None] * (3 * G.R_from_a(a_vec) + G.R_from_a(ad_vec))
        Ah, Bh = green_single(G, m, basis, t_eval)
        psih = (Ah + Bh) / (4 * n); dpsih = (Bh - Ah) / (2 * r_eval[:, None])
        wm = {0: 0.25, 1: 0.125, 2: -0.125, 3: -0.125}.get(m, 0.0); ch = 0.0
        if wm != 0.0:
            for (a, b, alpha, c) in basis.pieces:
                base = b if np.isinf(a) else a
                lo = -np.inf if np.isinf(a) else 0.0; hi = np.inf if np.isinf(b) else (b - base if not np.isinf(a) else 0.0)
                ch += wm * np.exp(2 * base) * scaled_integral(np.array([2.0 + alpha]), c, lo, hi, np.array([0.0]))[0]
        outm = np.zeros((Ne, Mout))
        def addsin(freq, coef):
            if freq < 0: freq, coef = -freq, -coef
            if freq == 0: return
            N = (freq - 1) // 2
            if N < Mout: outm[:, N] += coef
        for j in range(G.M + 1):
            if np.any(Rh[:, j]) or np.any(Rht[:, j]): addsin(2 * j + 1, c_l * Rht[:, j] - Rh[:, j])
            if ch != 0.0: addsin(2 * j + 1, (ch / 3.0) * Rtt[:, j])
        jj = [j for j in range(G.M + 1) if np.any(Rh[:, j]) or np.any(Rht[:, j])]
        for ni, nn in enumerate(n):
            Pn = 2 * nn * psi_t[:, ni]; Qn = dpsi_t[:, ni]
            for j in jj:
                coef = -0.5 * Pn * Rht[:, j] * e_2m; addsin(2 * j + 1 + 2 * nn, coef); addsin(2 * j + 1 - 2 * nn, coef)
                coef2 = 0.5 * Qn * (2 * j + 1) * Rh[:, j] * e_m; addsin(2 * nn + 2 * j + 1, coef2); addsin(2 * nn - 2 * j - 1, coef2)
        nn_act = [ni for ni in range(len(n)) if np.any(psih[:, ni]) or np.any(dpsih[:, ni])]
        for ni in nn_act:
            nn = n[ni]; Pn = 2 * nn * psih[:, ni]; Qn = dpsih[:, ni]
            for j in range(G.M + 1):
                coef = -0.5 * Pn * Rtt[:, j] * e_2m; addsin(2 * j + 1 + 2 * nn, coef); addsin(2 * j + 1 - 2 * nn, coef)
                coef2 = 0.5 * Qn * (2 * j + 1) * Rt_[:, j] * e_m; addsin(2 * nn + 2 * j + 1, coef2); addsin(2 * nn - 2 * j - 1, coef2)
        # X-norm proxy of the basis function: sup over radii of |b| e^{3t}/m (size relative to rho~) times derivative factor
        xw = np.max(np.abs(bval) * e3 / mr) * (1 + (2 * m) ** 2) ** (s_order / 2)
        return outm.ravel(), max(xw, 1e-300)
    col = 0
    for m in range(Mh):
        for (basis, label) in radial:
            Mat[:, col], colw[col] = column(m, basis); col += 1
        print("mode %d/%d done (%.0fs)" % (m, Mh, time.time() - t0), flush=True)
    # the constant a_0 = 1 (J direction) as the last column
    # the constant a_0 = 1 (J direction) on the inner and middle regions only (a constant a_0 in the outer region would give rho ~ x^2 y, not admissible)
    Mat[:, col], colw[col] = column(0, ExpPolyBasis([(-np.inf, T.tmin, 0.0, [1.0]), (T.tmin, T.t0, 0.0, [1.0])]))
    roww = ((1 + u) ** (0.5 - k) / mr)[:, None] * ((1 + (2 * np.arange(Mout) + 1) ** 2) ** (s_order / 2))[None, :]
    Mw = Mat * roww.ravel()[:, None] / colw[None, :]
    print("matrix %d x %d assembled (%.0fs); SVD ..." % (Mw.shape[0], Mw.shape[1], time.time() - t0), flush=True)
    U_, S_, Vt = np.linalg.svd(Mw, full_matrices=False)
    # K~ coordinates: b_m = -2 a_m - a_m' -> project each mode's function onto the radial basis by least squares on the collocation radii
    a0 = T.eval(t_eval, 0)[:, :Mh]; a1 = T.eval(t_eval, 1)[:, :Mh]; Kb = -2 * a0 - a1
    Bmat = np.stack([b.eval(t_eval, 0) for (b, lab) in radial], axis=1)                 # (Ne, nrad)
    kvec = np.zeros(ncol)
    for m in range(Mh):
        beta = np.linalg.lstsq(Bmat, Kb[:, m], rcond=None)[0]; kvec[m * nrad:(m + 1) * nrad] = beta
    kvec[-1] = -2.0                                                      # constant part of mode 0: -2 a_0(0) = -2
    kvec_w = kvec * colw; kvec_w /= np.linalg.norm(kvec_w)
    overlaps = [float(abs(Vt[-1 - i] @ kvec_w)) for i in range(5)]
    res = dict(Mh=Mh, stride=stride, s=s_order, shape=list(Mw.shape), sigma_min5=[float(x) for x in S_[-5:][::-1]], sigma_max=float(S_[0]),
               overlap_K_with_last5_right_vectors=overlaps, LK_over_K_proxy=float(np.linalg.norm(Mw @ (kvec_w)) ), time=time.time() - t0)
    print(json.dumps(res, indent=1)); json.dump(res, open(out, "w"), indent=1)
    np.savez_compressed(out.replace(".json", "_vectors.npz"), S=S_, Vt_last5=Vt[-5:], kvec_w=kvec_w, colw=colw)


if __name__ == "__main__":
    a = sys.argv
    main(a[1], int(a[2]), int(a[3]), float(a[4]), a[5])
