"""Speed-ups for lin_assembly (same mathematics): single-mode f-terms and a vectorized (over polynomial degree) version of the
cell integrals. Patched into LinAssembler.green via subclassing. Consistency with the generic path is tested in __main__."""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from expoly import _S, _GLX, _GLW
from lin_assembly import LinAssembler, ExpPolyBasis


def f_expoly_single(G, m, alpha, c, e2ta):
    """Equivalent of G._f_expoly([(alpha, cmat)], e2ta) with cmat having only column m = c; returns [(alpha + 2, fc (deg+1, Nf))]."""
    deg = len(c) - 1; M = G.M; Nf = G.Nf
    # R_from_a of the unit vector e_m: entries at frequencies 2m+1, -(2m-1), 2m+3, -(2m-3), each with coefficient 1/8 (sign by reflection)
    Rc = np.zeros((deg + 1, M + 1))
    for freq in (2 * m + 1, -(2 * m - 1), 2 * m + 3, -(2 * m - 3)):
        sgn = 1.0
        if freq < 0: freq, sgn = -freq, -1.0
        if freq == 0: continue
        j = (freq - 1) // 2
        if j <= M: Rc[:, j] += sgn * c / 8.0
    dRc = (3 + alpha) * Rc.copy()
    if deg >= 1: dRc[:-1] += Rc[1:] * np.arange(1, deg + 1)[:, None]
    fc = np.zeros((deg + 1, Nf))
    for j in np.where(np.any(Rc != 0, axis=0) | np.any(dRc != 0, axis=0))[0]:
        twoj1 = 2 * j + 1
        up = 0.5 * (dRc[:, j] - twoj1 * Rc[:, j]); dn = 0.5 * (dRc[:, j] + twoj1 * Rc[:, j])
        if j + 1 <= Nf: fc[:, j] += up
        if j >= 1: fc[:, j - 1] += dn
    return [(alpha + 2.0, fc * e2ta)]


def integ_all(lam, deg, tau0, tau1, shift, gl_threshold=1.5):
    """int_{tau0}^{tau1} e^{lam (s - shift)} s^p ds for p = 0..deg and the array lam: returns (deg+1, len(lam)). Same branches as
    expoly.integ_shift (Gauss-Legendre for |lam| h < threshold on finite intervals, closed form otherwise)."""
    lam = np.asarray(lam, float); out = np.zeros((deg + 1, len(lam)))
    shift = np.broadcast_to(np.asarray(shift, float), lam.shape)
    finite = not (np.isinf(tau0) or np.isinf(tau1))
    small = (np.abs(lam) * (tau1 - tau0) < gl_threshold) if finite else np.zeros_like(lam, bool)
    if small.any():
        s = 0.5 * (tau0 + tau1) + 0.5 * (tau1 - tau0) * _GLX
        E = np.exp(lam[small, None] * (s[None, :] - shift[small, None]))            # (ns, 32)
        Sp = s[None, :] ** np.arange(deg + 1)[:, None]                                # (deg+1, 32)
        out[:, small] = 0.5 * (tau1 - tau0) * (Sp * _GLW[None, :]) @ E.T
    big = ~small
    if big.any():
        lb = lam[big]; sb = shift[big]; nz = lb != 0
        for p in range(deg + 1):
            unit = np.zeros(deg + 1); unit[p] = 1.0
            def end(tau):
                if np.isinf(tau): return np.zeros_like(lb)
                v = _S(lb, unit, tau); e = np.ones_like(lb); e[nz] = np.exp(lb[nz] * (tau - sb[nz])); return v * e
            out[p, big] = end(tau1) - end(tau0)
    return out


def scaled_all(lam, deg, a, b, extra):
    """exp(extra) int_a^b e^{lam s} s^p ds for p = 0..deg (vectorized version of expoly.scaled_integral)."""
    lam = np.asarray(lam, float); extra = np.broadcast_to(np.asarray(extra, float), lam.shape)
    sh = np.where(lam > 0, b, a)
    I = integ_all(lam, deg, a, b, sh)
    return np.exp(extra + lam * sh)[None, :] * I


class FastAssembler(LinAssembler):
    def _terms(self, fterms, tau, a_lo, a_hi, b_lo, b_hi):
        n = self.n; accA = np.zeros(self.Nf); accB = np.zeros(self.Nf)
        for alpha, fc in fterms:
            deg = fc.shape[0] - 1; lam = (2 * n + 2) + alpha; mu = (2 - 2 * n) + alpha
            if a_hi > a_lo: accA += (fc * scaled_all(lam, deg, a_lo, a_hi, -2 * n * tau)).sum(0)
            if b_hi > b_lo: accB += (fc * scaled_all(mu, deg, b_lo, b_hi, 2 * n * tau)).sum(0)
        return accA, accB

    def green(self, m, basis):
        n = self.n; Nf = self.Nf; t = self.t; Ne = self.Ne; G = self.G
        A = np.zeros((Ne, Nf)); B = np.zeros((Ne, Nf))
        for (a, b, alpha, c) in basis.pieces:
            if np.isinf(a):
                base = b; ft = f_expoly_single(G, m, alpha, c, np.exp(2 * base)); e2 = np.exp(2 * base)
                Ap = e2 * self._terms(ft, 0.0, -np.inf, 0.0, 0.0, 0.0)[0]
                out = t >= b
                if out.any(): A[out] += np.exp(-2 * np.outer(t[out] - b, n)) * Ap[None, :]
                for i in np.where(~out)[0]:
                    tau = t[i] - b; accA, accB = self._terms(ft, tau, -np.inf, tau, tau, 0.0); A[i] += e2 * accA; B[i] += e2 * accB
            elif np.isinf(b):
                base = a; ft = f_expoly_single(G, m, alpha, c, np.exp(2 * base)); e2 = np.exp(2 * base)
                Bp = e2 * self._terms(ft, 0.0, 0.0, 0.0, 0.0, np.inf)[1]
                out = t <= a
                if out.any(): B[out] += np.exp(-2 * np.outer(a - t[out], n)) * Bp[None, :]
                for i in np.where(~out)[0]:
                    tau = t[i] - a; accA, accB = self._terms(ft, tau, 0.0, tau, tau, np.inf); A[i] += e2 * accA; B[i] += e2 * accB
            else:
                base = a; h = b - a; ft = f_expoly_single(G, m, alpha, c, np.exp(2 * base)); e2 = np.exp(2 * base)
                Ap = e2 * self._terms(ft, h, 0.0, h, 0.0, 0.0)[0]          # e^{-2n h} int_0^h : tau = h in the A shift
                Bp = e2 * self._terms(ft, 0.0, 0.0, 0.0, 0.0, h)[1]
                right = t >= b; left = t <= a; mid = ~(right | left)
                if right.any(): A[right] += np.exp(-2 * np.outer(t[right] - b, n)) * Ap[None, :]
                if left.any(): B[left] += np.exp(-2 * np.outer(a - t[left], n)) * Bp[None, :]
                for i in np.where(mid)[0]:
                    tau = t[i] - a; accA, accB = self._terms(ft, tau, 0.0, tau, tau, h); A[i] += e2 * accA; B[i] += e2 * accB
        return A, B


if __name__ == "__main__":
    from modal_fit import Trial
    from trial_green import TrialGreen
    from gn_refit import free_set, spline_bases
    T0 = Trial(dict(np.load("data/trial_v2_h0.008.npz"))); Ts = Trial(dict(np.load("data/trial_s02.npz")))
    free, lo, hi = free_set(T0, Ts, 1.7918, 2.4849); bases = spline_bases(Ts, free)
    G = TrialGreen(Ts); G.build()
    t_eval = np.unique(np.r_[np.linspace(-7, -4.9, 5), np.linspace(1.7, 2.6, 120), np.linspace(2.7, 9.5, 10)])
    LA = LinAssembler(G, t_eval, 100); FA = FastAssembler(G, t_eval, 100)
    from lin_assembly import trial_mode_basis
    tests = [(5, bases[0]), (5, bases[20]), (0, bases[41]), (37, bases[10]), (2, ExpPolyBasis([(-np.inf, Ts.tmin, 4.0, [1.0])])),
             (1, ExpPolyBasis([(Ts.t0, np.inf, Ts.k - 3 - (1 - Ts.k), [1.0])])), (3, trial_mode_basis(Ts, 3))]
    for m, bas in tests:
        t0 = time.time(); o1, c1 = LA.column(m, bas); t1 = time.time(); o2, c2 = FA.column(m, bas); t2 = time.time()
        print("m=%2d pieces=%4d: generic %.2fs fast %.2fs  max|diff| %.2e (scale %.2e) c %.3e / %.3e" % (m, len(bas.pieces), t1 - t0, t2 - t1, np.abs(o1 - o2).max(), np.abs(o1).max(), c1, c2))
