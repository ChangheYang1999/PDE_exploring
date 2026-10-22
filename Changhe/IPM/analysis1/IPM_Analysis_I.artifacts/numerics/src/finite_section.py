"""SPEC v2 item C2 (floating point, evidence only): finite sections of the unnormalized linearization
   L h = (V~.grad - 1) h + W[h].grad rho~,   W[h] = U[h] + (c[h]/3) X,
on h = x^2 y sum_{m<Mh} b_m(r) cos(2m theta), b_m = sum_q beta_mq B_q(t), B_q the interior degree-7 B-splines on uniform knots in
t = log r on [t_lo, t_hi] (h vanishes identically outside, C^6).  Columns: basis functions (m, q). Rows: modal coefficients
(L h)_N at the Greville-type collocation radii t_i (knot midpoints), N < Mh_out (output frequencies kept), weighted by the
Y proxy weight 1/(m(r) (1+u)^(gamma-k)) * (1 + (2N+1)^2 + (1/dt)^2)^(s/2) [same-order derivative proxy of order s];
columns weighted by the X proxy norm of the basis function (same formula with the basis function's own frequency and knot
spacing). Smallest singular values of the weighted matrix and the right singular vectors; overlap with K~ = rho~ - X.grad rho~
projected on the basis (least squares).  Usage: python3 finite_section.py trial.npz Mh nb t_lo t_hi s out.json
"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from math import factorial
from scipy.interpolate import BSpline
from modal_fit import Trial
from trial_green import TrialGreen
from expoly import scaled_integral

P = 7


class HBasis:
    """Compactly supported spline basis in t for the radial profiles of h."""
    def __init__(self, t_lo, t_hi, nb):
        # interior knots uniform; total basis = nb interior functions (drop P at each end so that h vanishes to order P at the ends)
        ncell = nb + P
        self.knots_int = np.linspace(t_lo, t_hi, ncell + 1)
        self.knots = np.r_[np.full(P, t_lo), self.knots_int, np.full(P, t_hi)]
        self.nb_all = len(self.knots) - P - 1
        self.keep = np.arange(P, self.nb_all - P)                   # functions with support inside (t_lo, t_hi)
        assert len(self.keep) == nb, (len(self.keep), nb)
        self.nb = nb; self.dt = (t_hi - t_lo) / ncell
        self.spl = BSpline(self.knots, np.eye(self.nb_all), P, extrapolate=False)

    def _taylor_table(self):
        if not hasattr(self, "_tab"):
            starts = self.knots_int[:-1]
            spl = BSpline(self.knots, np.eye(self.nb_all), P, extrapolate=True)
            self._tab = np.stack([spl(starts, nu=nu) / factorial(nu) for nu in range(P + 1)], axis=-1)   # (ncell, nb_all, P+1)
        return self._tab

    def cell_taylor(self, q):
        """cells in the support of basis function keep[q]: list of (t_a, t_b, Taylor coefficients (P+1,) at t_a)."""
        tab = self._taylor_table(); b = self.keep[q]; out = []
        for c in range(b - P, b + 1):
            if 0 <= c < len(self.knots_int) - 1:
                out.append((self.knots_int[c], self.knots_int[c + 1], tab[c, b]))
        return out


def green_of_basis(G, cells, m, t_eval):
    """A_n(t), B_n(t) (n = 1..Nf) of the single-mode density a_m = B_q (support cells), at points t_eval. Closed forms over the
    support cells (alpha = 0 terms), zero elsewhere. Uses TrialGreen's modal algebra (f-terms of a one-mode a)."""
    n = G.n; Nf = G.Nf
    # f-terms per cell: a has only mode m
    fterms = []
    for (a_, b_, coef) in cells:
        c = np.zeros((P + 1, G.M)); c[:, m] = coef
        fterms.append((a_, b_, G._f_expoly([(0.0, c)], np.exp(2 * a_))))
    A = np.zeros((len(t_eval), Nf)); B = np.zeros((len(t_eval), Nf))
    for it, t in enumerate(t_eval):
        for (a_, b_, ft) in fterms:
            if t <= a_: continue
            hi = min(t, b_)          # integrate the cell part below t for A
            for alpha, fc in ft:
                lam = (2 * n + 2) + alpha
                for p in range(fc.shape[0]):
                    if not np.any(fc[p]): continue
                    unit = np.zeros(fc.shape[0]); unit[p] = 1.0
                    A[it] += fc[p] * np.exp(-2 * n * (t - a_)) * scaled_integral(lam, unit, 0.0, hi - a_, 0.0 * lam) * np.exp(2 * a_) * np.exp(0)
        for (a_, b_, ft) in fterms:
            if t >= b_: continue
            lo = max(t, a_)
            for alpha, fc in ft:
                mu = (2 - 2 * n) + alpha
                for p in range(fc.shape[0]):
                    if not np.any(fc[p]): continue
                    unit = np.zeros(fc.shape[0]); unit[p] = 1.0
                    B[it] += fc[p] * np.exp(2 * n * (t - a_)) * scaled_integral(mu, unit, lo - a_, b_ - a_, 0.0 * mu) * np.exp(2 * a_)
    return A, B


def main(trial, Mh, nb, t_lo, t_hi, s_order, out):
    T = Trial(np.load(trial)); G = TrialGreen(T); G.build()
    k = T.k; L = T.L; c_l = 1.0 / k
    H = HBasis(t_lo, t_hi, nb)
    t_eval = 0.5 * (H.knots_int[:-1] + H.knots_int[1:])                 # collocation radii (cell midpoints)
    r_eval = np.exp(t_eval); Ne = len(t_eval)
    # trial data at the collocation radii
    Rt_, Rtt = G.rho_modes(t_eval); psi_t, dpsi_t = G.psi_at(t_eval)      # R~_j, dR~_j/dt, psi~_n, psi~_n'
    n = G.n
    Mout = Mh + 2                                                         # output frequencies kept: N < Mout
    # column loop
    ncol = Mh * nb; nrow = Ne * Mout
    Mat = np.zeros((nrow, ncol)); colw = np.zeros(ncol); t0 = time.time()
    e_m = np.exp(-t_eval); e_2m = np.exp(-2 * t_eval); e3 = np.exp(3 * t_eval)
    for m in range(Mh):
        for q in range(nb):
            col = m * nb + q
            cells = H.cell_taylor(q)
            # h modes: R^h_j = e^{3t} T_j[a] with a = B_q in mode m; values and t-derivative at t_eval
            bval = H.spl(t_eval)[:, H.keep[q]]; bder = H.spl(t_eval, nu=1)[:, H.keep[q]]
            a_vec = np.zeros((Ne, G.M)); a_vec[:, m] = np.nan_to_num(bval); ad_vec = np.zeros((Ne, G.M)); ad_vec[:, m] = np.nan_to_num(bder)
            Rh = e3[:, None] * G.R_from_a(a_vec); Rht = e3[:, None] * (3 * G.R_from_a(a_vec) + G.R_from_a(ad_vec))
            # U[h] modes
            Ah, Bh = green_of_basis(G, cells, m, t_eval)
            psih = (Ah + Bh) / (4 * n); dpsih = (Bh - Ah) / (2 * r_eval[:, None])
            # c[h] = int_0^oo r a_m dr * w_m  (w = 1/4, 1/8, -1/8, -1/8 for m = 0..3)
            wm = {0: 0.25, 1: 0.125, 2: -0.125, 3: -0.125}.get(m, 0.0)
            ch = 0.0
            if wm != 0.0:
                for (a_, b_, coef) in cells:
                    ch += wm * np.exp(2 * a_) * scaled_integral(np.array([2.0]), coef, 0.0, b_ - a_, np.array([0.0]))[0]
            # L h modes at t_eval: eps-like assembly with (trial V) acting on h and (U[h] + c[h]/3 X) acting on rho~
            out_modes = np.zeros((Ne, Mout))
            def addsin(freq, coef):
                if freq < 0: freq, coef = -freq, -coef
                if freq == 0: return
                N = (freq - 1) // 2
                if N < Mout: out_modes[:, N] += coef
            # (c_l X.grad - 1) h + (c[h]/3) X.grad rho~  : X.grad = d_t
            for j in range(G.M + 1):
                addsin(2 * j + 1, c_l * Rht[:, j] - Rh[:, j] + (ch / 3.0) * Rtt[:, j])
            # U~.grad h: -(psi~_theta / r) h_r + (psi~_r / r) h_theta
            for ni, nn in enumerate(n):
                Pn = 2 * nn * psi_t[:, ni]; Qn = dpsi_t[:, ni]
                for j in range(G.M + 1):
                    if not np.any(Rh[:, j]): continue
                    coef = -0.5 * Pn * Rht[:, j] * e_2m; addsin(2 * j + 1 + 2 * nn, coef); addsin(2 * j + 1 - 2 * nn, coef)
                    coef2 = 0.5 * Qn * (2 * j + 1) * Rh[:, j] * e_m; addsin(2 * nn + 2 * j + 1, coef2); addsin(2 * nn - 2 * j - 1, coef2)
            # U[h].grad rho~
            for ni, nn in enumerate(n):
                if not (np.any(psih[:, ni]) or np.any(dpsih[:, ni])): continue
                Pn = 2 * nn * psih[:, ni]; Qn = dpsih[:, ni]
                for j in range(G.M + 1):
                    coef = -0.5 * Pn * Rtt[:, j] * e_2m; addsin(2 * j + 1 + 2 * nn, coef); addsin(2 * j + 1 - 2 * nn, coef)
                    coef2 = 0.5 * Qn * (2 * j + 1) * Rt_[:, j] * e_m; addsin(2 * nn + 2 * j + 1, coef2); addsin(2 * nn - 2 * j - 1, coef2)
            Mat[:, col] = out_modes.ravel()
            # X proxy weight of the basis function: sup |x^2 y B_q cos 2m theta| ~ e^{3t} m-scale, times derivative factor
            colw[col] = (np.exp(3 * t_eval) * np.abs(np.nan_to_num(bval))).max() * (1 + (2 * m) ** 2 + (1.0 / H.dt) ** 2) ** (s_order / 2)
        if m % 4 == 0: print("mode %d/%d done (%.0fs)" % (m, Mh, time.time() - t0), flush=True)
    # row weights: 1/(m(r)(1+u)^(gamma-k)) * derivative proxy
    u = r_eval / L; mr = u ** 3 * (1 + u ** 2) ** ((k - 3) / 2); wrow_r = 1.0 / (mr * (1 + u) ** (0.5 - k))
    Nn = np.arange(Mout); dfac = (1 + (2 * Nn + 1) ** 2 + (1.0 / H.dt) ** 2) ** (s_order / 2)
    roww = (wrow_r[:, None] * dfac[None, :]).ravel()
    Mw = Mat * roww[:, None] / colw[None, :]
    print("matrix %d x %d assembled (%.0fs); SVD ..." % (Mw.shape[0], Mw.shape[1], time.time() - t0), flush=True)
    U_, S_, Vt = np.linalg.svd(Mw, full_matrices=False)
    # K~ projected on the basis: K~ = rho~ - X.grad rho~ = x^2 y (-2 a - a') in modes -> b_m = -2 a_m - a_m' (t-derivative) restricted to m < Mh
    Kb = np.zeros((Ne, Mh)); a0 = T.eval(t_eval, 0)[:, :Mh]; a1 = T.eval(t_eval, 1)[:, :Mh]; Kb = -2 * a0 - a1
    # least squares spline coefficients of Kb per mode
    Bmat = np.nan_to_num(H.spl(t_eval)[:, H.keep])
    beta = np.linalg.lstsq(Bmat, Kb, rcond=None)[0]                     # (nb, Mh)
    kvec = (beta.T).ravel() * colw                                       # coordinates in the weighted column space
    kvec /= np.linalg.norm(kvec)
    overlaps = [float(abs(Vt[i] @ kvec)) for i in range(5)]
    res = dict(Mh=Mh, nb=nb, t_lo=t_lo, t_hi=t_hi, s=s_order, shape=list(Mw.shape), sigma_min5=[float(x) for x in S_[-5:][::-1]], sigma_max=float(S_[0]),
               overlap_K_with_last5_right_vectors=overlaps, time=time.time() - t0)
    print(json.dumps(res, indent=1)); json.dump(res, open(out, "w"), indent=1)
    np.savez_compressed(out.replace(".json", "_vectors.npz"), S=S_, Vt_last5=Vt[-5:], kvec=kvec, colw=colw)


if __name__ == "__main__":
    a = sys.argv
    main(a[1], int(a[2]), int(a[3]), float(a[4]), float(a[5]), float(a[6]), a[7])
