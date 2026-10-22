"""Closed-form canonical inverse and transport residual of the explicit modal trial (float64 version; the Arb
version mirrors it for the certificate).

Trial (modal_fit.Trial): rho~ = x^2 y sum_{m<M} a_m(r) cos(2 m theta), a_m exponential-polynomial splines in t = log r.
Cells: (-inf, tmin], spline cells, [t0, +inf). On every cell, with sigma = t - t_a (t_a the cell's left end; for the
inner cell sigma = t - tmin <= 0), each a_m is sum_terms e^{alpha sigma} p(sigma).  Then (R_j = coefficient of
sin((2j+1) theta) of rho~, f_n = coefficient of sin(2n theta) of d_x rho~):
  R_j = e^{3t} T_j[a],  T the banded map of cos^2 sin cos(2m) into sines;   f_n(e^t) = F_n(sigma) = sum e^{alpha' sigma} p~(sigma)
  with alpha' = alpha + 2 and p~ containing the factor e^{2 t_a} (d_x rho~ ~ r^2 a).
Green:  A_n(t) = e^{-2n t} int_{-inf}^t e^{(2n+2) s} f_n(e^s) ds,   B_n(t) = e^{2n t} int_t^inf e^{(2-2n) s} f_n(e^s) ds,
  psi_n = (A_n + B_n)/(4n),  psi_n' = (B_n - A_n)/(2r),  c = psi_xy(0) = (1/2) int_R f_1(e^s) ds.
Within a cell (lam = 2n+2+alpha', mu = 2-2n+alpha'):
  A_n(t) = e^{-2n sigma} A_n(t_a) + e^{2 t_a} e^{(2+alpha') sigma} int_0^sigma e^{lam (s - sigma)} p~(s) ds
  B_n(t) = e^{-2n (h - sigma)} B_n(t_b) + e^{2 t_a} e^{(2+alpha') sigma} int_sigma^h e^{mu (s - sigma)} p~(s) ds
(all exponentials bounded: shifted primitives).  Half-infinite cells: the same with the far end at -inf / +inf and
the requirements lam > 0 (inner) and mu < 0 (outer).
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from math import factorial
from scipy.interpolate import BSpline
from modal_fit import Trial, OUTER_JL, NIN, NCOR, NOUT


from expoly import integ_shift, _S, scaled_integral


class TrialGreen:
    def __init__(self, trial, Mcut=None):
        T = trial; self.T = T
        self.M = T.M if Mcut is None else Mcut
        self.k = T.k; self.L = T.L; self.c_l = 1.0 / self.k
        kn = T.knots[T.p + 1:-(T.p + 1)]
        self.tb = np.r_[T.tmin, kn, T.t0]; self.nc = len(self.tb) - 1
        spl = BSpline(T.knots, T.S.T, T.p, extrapolate=True)
        ta = self.tb[:-1]
        self.pc = np.stack([spl(ta, nu=i) / factorial(i) for i in range(T.p + 1)], axis=1)[:, :, :self.M]   # (nc, p+1, M)
        self.Mj = self.M + 1; self.Nf = self.M + 1
        self.n = np.arange(1, self.Nf + 1)

    # ---------- modal algebra ----------
    def R_from_a(self, a):
        """R_j = coefficient of sin((2j+1)theta) in cos^2 sin * sum_m a_m cos 2m theta  (a: (..., M) -> (..., M+1))."""
        M = self.M; R = np.zeros(a.shape[:-1] + (M + 1,))
        def add(freq, coef):
            if freq < 0: freq, coef = -freq, -coef
            if freq == 0: return
            j = (freq - 1) // 2
            if j <= M: R[..., j] += coef
        for m in range(M):
            am = a[..., m] / 8.0
            add(2 * m + 1, am); add(-(2 * m - 1), am); add(2 * m + 3, am); add(-(2 * m - 3), am)
        return R

    def eval_a(self, t, nu=0):
        return self.T.eval(np.atleast_1d(t), nu)[:, :self.M]

    def rho_modes(self, t):
        t = np.atleast_1d(t); e3 = np.exp(3 * t)[:, None]
        a0 = self.eval_a(t, 0); a1 = self.eval_a(t, 1)
        R = e3 * self.R_from_a(a0); Rt = e3 * (3 * self.R_from_a(a0) + self.R_from_a(a1))
        return R, Rt

    def f_modes(self, t):
        t = np.atleast_1d(t); R, Rt = self.rho_modes(t)
        em = np.exp(-t)[:, None]; M = self.M
        f = np.zeros((len(t), self.Nf))
        for j in range(M + 1):
            twoj1 = 2 * j + 1
            up = 0.5 * em[:, 0] * (Rt[:, j] - twoj1 * R[:, j]); dn = 0.5 * em[:, 0] * (Rt[:, j] + twoj1 * R[:, j])
            if j + 1 <= self.Nf: f[:, j] += up
            if j >= 1: f[:, j - 1] += dn
        return f

    def _f_expoly(self, terms_a, e2ta):
        """a-terms [(alpha, coeffs (deg+1, M))] on a cell (sigma local) -> f-terms [(alpha+2, coeffs (deg+1, Nf))] including e^{2 t_a}."""
        out = []
        for alpha, c in terms_a:
            deg = c.shape[0] - 1
            Rc = np.stack([self.R_from_a(c[p]) for p in range(deg + 1)])
            dRc = (3 + alpha) * Rc.copy()
            if deg >= 1: dRc[:-1] += Rc[1:] * np.arange(1, deg + 1)[:, None]
            fc = np.zeros((deg + 1, self.Nf))
            for j in range(self.M + 1):
                twoj1 = 2 * j + 1
                up = 0.5 * (dRc[:, j] - twoj1 * Rc[:, j]); dn = 0.5 * (dRc[:, j] + twoj1 * Rc[:, j])
                if j + 1 <= self.Nf: fc[:, j] += up
                if j >= 1: fc[:, j - 1] += dn
            out.append((alpha + 2.0, fc * e2ta))
        return out

    # ---------- Green integrals ----------
    def _acc(self, fterms, which, tau0, tau1, shift):
        """sum over f-terms of int_{tau0}^{tau1} e^{lam (s - shift)} p~(s) ds with lam = (2n+2)+alpha' (which='in') or (2-2n)+alpha' ('out')."""
        n = self.n; acc = np.zeros(self.Nf)
        for alpha, fc in fterms:
            lam = ((2 * n + 2) if which == "in" else (2 - 2 * n)) + alpha
            for p in range(fc.shape[0]):
                if not np.any(fc[p]): continue
                unit = np.zeros(fc.shape[0]); unit[p] = 1.0
                acc += fc[p] * integ_shift(lam, unit, tau0, tau1, shift)
        return acc

    def build(self):
        n = self.n; Nf = self.Nf; nc = self.nc; tb = self.tb
        A = np.zeros((nc + 1, Nf)); B = np.zeros((nc + 1, Nf))
        self.inner_fterms = self._f_expoly(self.T.inner_terms(), np.exp(2 * tb[0]))
        A[0] = np.exp(2 * tb[0]) * self._acc(self.inner_fterms, "in", -np.inf, 0.0, 0.0)      # lam > 0 there: shift 0 is bounded
        self.cell_fterms = []
        for ci in range(nc):
            ta, tbb = tb[ci], tb[ci + 1]; h = tbb - ta
            ft = self._f_expoly([(0.0, self.pc[ci])], np.exp(2 * ta)); self.cell_fterms.append(ft)
            # A(t_b) = e^{-2n h} A(t_a) + e^{2 t_a} sum e^{(2+alpha') h} int_0^h e^{lam (s-h)} p~
            inc = np.zeros(Nf)
            for alpha, fc in ft:
                lam = (2 * n + 2) + alpha
                for p in range(fc.shape[0]):
                    if not np.any(fc[p]): continue
                    unit = np.zeros(fc.shape[0]); unit[p] = 1.0
                    inc += fc[p] * scaled_integral(lam, unit, 0.0, h, -2 * n * h)        # e^{-2n h} int_0^h e^{lam s} p
            A[ci + 1] = np.exp(-2 * n * h) * A[ci] + np.exp(2 * ta) * inc
        self.outer_fterms = self._f_expoly(self.T.outer_terms(), np.exp(2 * tb[-1]))
        B[nc] = np.exp(2 * tb[-1]) * self._acc(self.outer_fterms, "out", 0.0, np.inf, 0.0)
        for ci in range(nc - 1, -1, -1):
            ta, tbb = tb[ci], tb[ci + 1]; h = tbb - ta
            # B(t_a) = e^{-2n h} B(t_b) + e^{2 t_a} int_0^h e^{mu s} p~
            B[ci] = np.exp(-2 * n * h) * B[ci + 1] + np.exp(2 * ta) * self._acc(self.cell_fterms[ci], "out", 0.0, h, 0.0)
        self.A, self.B = A, B
        # c = (1/2) int_R f_1 dt = (1/2) [int_{-inf}^{tmin} f_1 + e^{-2 tmin} B_1(tmin)]
        head = 0.0
        for alpha, fc in self.inner_fterms:
            for p in range(fc.shape[0]):
                unit = np.zeros(fc.shape[0]); unit[p] = 1.0
                head += fc[p][0] * integ_shift(np.array([alpha]), unit, -np.inf, 0.0, 0.0)[0]
        self.c = 0.5 * (head + B[0, 0] * np.exp(-2 * tb[0]))
        return A, B

    def _AB_terms(self, fterms, tau, a_lo, a_hi, b_lo, b_hi):
        """sum over f-terms of  e^{-2n tau} int_{a_lo}^{a_hi} e^{lam s} p~  and  e^{2n tau} int_{b_lo}^{b_hi} e^{mu s} p~."""
        n = self.n; accA = np.zeros(self.Nf); accB = np.zeros(self.Nf)
        for alpha, fc in fterms:
            lam = (2 * n + 2) + alpha; mu = (2 - 2 * n) + alpha
            for p in range(fc.shape[0]):
                if not np.any(fc[p]): continue
                unit = np.zeros(fc.shape[0]); unit[p] = 1.0
                if a_hi > a_lo: accA += fc[p] * scaled_integral(lam, unit, a_lo, a_hi, -2 * n * tau)
                if b_hi > b_lo: accB += fc[p] * scaled_integral(mu, unit, b_lo, b_hi, 2 * n * tau)
        return accA, accB

    def AB_at(self, t):
        t = np.atleast_1d(np.asarray(t, float)); n = self.n; Nf = self.Nf
        A = np.zeros((len(t), Nf)); B = np.zeros((len(t), Nf))
        for i, tt in enumerate(t):
            if tt <= self.tb[0]:
                tau = tt - self.tb[0]; e2 = np.exp(2 * self.tb[0])
                accA, accB = self._AB_terms(self.inner_fterms, tau, -np.inf, tau, tau, 0.0)
                A[i] = e2 * accA
                B[i] = np.exp(2 * n * tau) * self.B[0] + e2 * accB
            elif tt >= self.tb[-1]:
                tau = tt - self.tb[-1]; e2 = np.exp(2 * self.tb[-1])
                accA, accB = self._AB_terms(self.outer_fterms, tau, 0.0, tau, tau, np.inf)
                A[i] = np.exp(-2 * n * tau) * self.A[-1] + e2 * accA
                B[i] = e2 * accB
            else:
                ci = min(np.searchsorted(self.tb, tt, side="right") - 1, self.nc - 1)
                ta = self.tb[ci]; tau = tt - ta; h = self.tb[ci + 1] - ta; e2 = np.exp(2 * ta)
                accA, accB = self._AB_terms(self.cell_fterms[ci], tau, 0.0, tau, tau, h)
                A[i] = np.exp(-2 * n * tau) * self.A[ci] + e2 * accA
                B[i] = np.exp(-2 * n * (h - tau)) * self.B[ci + 1] + e2 * accB
        return A, B

    def psi_at(self, t):
        A, B = self.AB_at(t); n = self.n; r = np.exp(np.atleast_1d(t))[:, None]
        return (A + B) / (4 * n), (B - A) / (2 * r)

    def residual_modes(self, t, c_l=None):
        """eps_N(t) (coefficient of sin((2N+1) theta), N = 0..2M+1) of eps = (c_l X + U).grad rho - rho."""
        t = np.atleast_1d(np.asarray(t, float)); c_l = self.c_l if c_l is None else c_l
        R, Rt = self.rho_modes(t); psi, dpsi = self.psi_at(t)
        n = self.n; M = self.M; Nmax = 2 * M + 2
        eps = np.zeros((len(t), Nmax + 1)); eps[:, :M + 1] += c_l * Rt - R
        em1 = np.exp(-t); em2 = np.exp(-2 * t)
        def addsin(freq, coef):
            if freq < 0: freq, coef = -freq, -coef
            if freq == 0: return
            N = (freq - 1) // 2
            if N <= Nmax: eps[:, N] += coef
        for ni, nn in enumerate(n):
            P_ = 2 * nn * psi[:, ni]; Q_ = dpsi[:, ni]
            for j in range(M + 1):
                coef = -0.5 * P_ * Rt[:, j] * em2                 # -(psi_theta / r) rho_r ; rho_r = e^{-t} Rt
                addsin(2 * j + 1 + 2 * nn, coef); addsin(2 * j + 1 - 2 * nn, coef)
                coef2 = 0.5 * Q_ * (2 * j + 1) * R[:, j] * em1     # (psi_r / r) rho_theta
                addsin(2 * nn + 2 * j + 1, coef2); addsin(2 * nn - 2 * j - 1, coef2)
        return eps


if __name__ == "__main__":
    from inverse import ModalInverse
    T = Trial(np.load(sys.argv[1] if len(sys.argv) > 1 else "data/trial_v2_h0.008.npz"))
    G = TrialGreen(T)
    t0 = time.time(); G.build(); print("build %.1fs; c = %.12f  (3/k - 1 = %.12f)" % (time.time() - t0, G.c, 3 / G.k - 1))
    Nr, Nt = 16000, 1024
    r = np.exp(np.linspace(np.log(1e-4 * T.L), np.log(1e6 * T.L), Nr)); th = np.linspace(0, np.pi / 2, Nt + 1); t = np.log(r)
    f = G.f_modes(t); S = np.sin(2 * G.n[:, None] * th[None, :]); fx = f @ S
    inv = ModalInverse(r, th, p=6, tail_powers=[T.k - 1, 2 * T.k - 2, T.k - 3, 3 * T.k - 3], k=T.k)
    psi_g, dpsi_g, c_g = inv.solve(fx)
    sel = np.argmin(np.abs(r[:, None] - np.array([0.003, 0.1, 1, 8.6, 50, 300, 3000, 3e4])[None, :]), axis=0)
    t1 = time.time(); psi_c, dpsi_c = G.psi_at(t[sel]); print("psi_at for %d points: %.2fs" % (len(sel), time.time() - t1))
    for i, idx in enumerate(sel):
        nmax = min(G.Nf, psi_g.shape[1])
        e1 = np.abs(psi_c[i, :nmax] - psi_g[idx, :nmax]).max() / np.abs(psi_c[i, :nmax]).max()
        e2 = np.abs(dpsi_c[i, :nmax] - dpsi_g[idx, :nmax]).max() / np.abs(dpsi_c[i, :nmax]).max()
        print("r=%8.3g  rel err psi modes %.2e  psi' modes %.2e" % (r[idx], e1, e2))
    print("c closed form %.12f vs grid inverse %.12f (diff %.2e)" % (G.c, c_g, G.c - c_g))
