"""Floating-point (evidence only) derivative jets of the trial residual eps~ = (c_l X + U~).grad rho~ - rho~ near a radius range.

All radial derivatives are analytic (no finite differences): a_m^{(i)}(t) from the exponential-polynomial / spline
representation (Trial.eval(t, nu)), the Green functions through the ODEs  A_n' = -2n A_n + g_n,  B_n' = 2n B_n - g_n
(t = log r, g_n = e^{2t} f_n, f_n the sine-2n mode of d_x rho~), psi_n = (A_n + B_n)/(4n).  Angular derivatives are exact
(finite trigonometric sums).  Fields on a (t, theta) grid; products by Leibniz; Cartesian derivatives D^alpha eps (|alpha| <= K)
by the recursion  d_x = e^{-t}(cos th d_t - sin th d_th),  d_y = e^{-t}(sin th d_t + cos th d_th)  applied to (t, theta)-jets.

Conventions: eps = c_l rho_t - rho + e^{-2t} (psi_t rho_th - psi_th rho_t)  [polar form of (c_l X + grad^perp psi).grad rho - rho].
"""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from math import comb
from modal_fit import Trial
from trial_green import TrialGreen


class TrialJets:
    def __init__(self, G, K=4):
        self.G = G; self.K = K; self.M = G.M; self.n = G.n; self.c_l = G.c_l

    # ---------- modal jets (radial derivatives of the mode functions) ----------
    def modal_jets(self, t):
        """Returns dict with R[i] (i <= K+2): d_t^i of the rho modes R_j(t) (sin((2j+1)th), j <= M), shape (K+3, nt, M+1);
        PSI[i] (i <= K+1): d_t^i psi_n(t) (sin(2n th), n = 1..Nf), shape (K+2, nt, Nf)."""
        G = self.G; K = self.K; t = np.atleast_1d(np.asarray(t, float)); nt = len(t)
        Ka = K + 3                                   # a-derivatives needed: R up to K+2 needs a up to K+2
        a = np.stack([G.eval_a(t, nu) for nu in range(Ka)])            # (Ka, nt, M)
        Ra = np.stack([G.R_from_a(a[nu]) for nu in range(Ka)])         # (Ka, nt, M+1): R_from_a(a^{(nu)})
        e3 = np.exp(3 * t)[:, None]
        R = np.zeros((K + 3, nt, self.M + 1))
        for i in range(K + 3):
            R[i] = e3 * sum(comb(i, l) * 3.0 ** (i - l) * Ra[l] for l in range(i + 1))
        # f_n jets: f = 0.5 e^{-t} (R' -/+ (2j+1) R) scattered to n = j+1 (up) and n = j (dn); d_t^i of e^{-t} h = sum C(i,l)(-1)^{i-l} e^{-t} h^{(l)}
        em = np.exp(-t)[:, None]; Nf = G.Nf
        F = np.zeros((K + 2, nt, Nf))
        for i in range(K + 2):
            Hup = np.zeros((nt, Nf)); 
            for l in range(i + 1):
                c = comb(i, l) * (-1.0) ** (i - l)
                for j in range(self.M + 1):
                    twoj1 = 2 * j + 1
                    up = 0.5 * (R[l + 1][:, j] - twoj1 * R[l][:, j]); dn = 0.5 * (R[l + 1][:, j] + twoj1 * R[l][:, j])
                    if j + 1 <= Nf: Hup[:, j] += c * up
                    if j >= 1: Hup[:, j - 1] += c * dn
            F[i] = em * Hup
        # g = e^{2t} f ; A' = -2n A + g, B' = 2n B - g
        e2 = np.exp(2 * t)[:, None]
        Gj = np.zeros((K + 2, nt, Nf))
        for i in range(K + 2):
            Gj[i] = e2 * sum(comb(i, l) * 2.0 ** (i - l) * F[l] for l in range(i + 1))
        A0, B0 = G.AB_at(t)
        A = np.zeros((K + 2, nt, Nf)); B = np.zeros((K + 2, nt, Nf)); A[0] = A0; B[0] = B0
        n = self.n[None, :]
        for i in range(K + 1):
            A[i + 1] = -2 * n * A[i] + Gj[i]; B[i + 1] = 2 * n * B[i] - Gj[i]
        PSI = (A + B) / (4 * n)
        return dict(t=t, R=R, PSI=PSI, F=F)

    # ---------- fields on a (t, theta) grid ----------
    @staticmethod
    def _trig_jets(freqs, th, kind, J):
        """d_th^j of sin(freq th) (kind='sin') for j <= J: array (J+1, nfreq, nth)."""
        out = np.zeros((J + 1, len(freqs), len(th)))
        for j in range(J + 1):
            out[j] = freqs[:, None] ** j * np.sin(freqs[:, None] * th[None, :] + j * np.pi / 2)
        return out

    def eps_jets(self, t, th, K=None):
        """(t, theta)-jets of eps on the grid: E[i, j] = d_t^i d_th^j eps, i + j <= K, shape (K+1, K+1, nt, nth) (unused entries 0).
        Also returns the jets of rho (RHO) for reference (same layout, orders up to K)."""
        K = self.K if K is None else K
        mj = self.modal_jets(t); t = mj["t"]; nt, nth = len(t), len(th)
        fr_rho = 2 * np.arange(self.M + 1) + 1.0; fr_psi = 2.0 * self.n
        Srho = self._trig_jets(fr_rho, th, "sin", K + 1); Spsi = self._trig_jets(fr_psi, th, "sin", K + 1)
        # field jets up to total order K+1 for rho and psi (needed because eps involves first derivatives)
        def field(Rmod, S, order):
            Fj = {}
            for i in range(order + 1):
                for j in range(order + 1 - i):
                    Fj[(i, j)] = Rmod[i] @ S[j]                 # (nt, nth)
            return Fj
        RHO = field(mj["R"], Srho, K + 1); PSI = field(mj["PSI"], Spsi, K + 1)
        em2 = np.exp(-2 * t)[:, None]
        E = {}
        for i in range(K + 1):
            for j in range(K + 1 - i):
                lin = self.c_l * RHO[(i + 1, j)] - RHO[(i, j)]
                # product term: e^{-2t} P, P = psi_t rho_th - psi_th rho_t ; d_t^i (e^{-2t} P) = sum_l C(i,l) (-2)^{i-l} e^{-2t} d_t^l P
                prod = np.zeros((nt, nth))
                for l in range(i + 1):
                    cl = comb(i, l) * (-2.0) ** (i - l)
                    Pl = np.zeros((nt, nth))
                    for l1 in range(l + 1):
                        for j1 in range(j + 1):
                            cc = comb(l, l1) * comb(j, j1)
                            Pl += cc * (PSI[(l1 + 1, j1)] * RHO[(l - l1, j - j1 + 1)] - PSI[(l1, j1 + 1)] * RHO[(l - l1 + 1, j - j1)])
                    prod += cl * Pl
                E[(i, j)] = lin + em2 * prod
        return E, RHO, PSI

    # ---------- Cartesian derivatives ----------
    @staticmethod
    def polar_to_cart(E, t, th, K):
        """From the (t,th)-jet E[(i,j)] (i + j <= K) on the grid, compute D[(a,b)] = d_x^a d_y^b eps for a + b <= K."""
        nt, nth = len(t), len(th)
        emt = np.exp(-t)[:, None]
        def coef(kind, a, b):
            # d_t^a d_th^b of e^{-t} cos th (kind 'c') or e^{-t} sin th (kind 's')
            if kind == "c": ang = np.cos(th + b * np.pi / 2)
            else: ang = np.sin(th + b * np.pi / 2)
            return (-1.0) ** a * emt * ang[None, :]
        def apply(Fj, order, which):
            """Fj: jet dict of orders <= order; returns jet of d_which F of orders <= order-1."""
            out = {}
            for i in range(order):
                for j in range(order - i):
                    acc = np.zeros((nt, nth))
                    for a in range(i + 1):
                        for b in range(j + 1):
                            cc = comb(i, a) * comb(j, b)
                            if which == "x":
                                acc += cc * (coef("c", a, b) * Fj[(i - a + 1, j - b)] - coef("s", a, b) * Fj[(i - a, j - b + 1)])
                            else:
                                acc += cc * (coef("s", a, b) * Fj[(i - a + 1, j - b)] + coef("c", a, b) * Fj[(i - a, j - b + 1)])
                    out[(i, j)] = acc
            return out
        D = {(0, 0): E[(0, 0)]}
        # chains: apply d_x a times, then d_y b times
        cache = {(0, 0): (E, K)}
        for a in range(K + 1):
            for b in range(K + 1 - a):
                if a == 0 and b == 0: continue
                if b == 0:
                    Fj, order = cache[(a - 1, 0)]; cur = apply(Fj, order, "x"); cache[(a, 0)] = (cur, order - 1)
                else:
                    Fj, order = cache[(a, b - 1)]; cur = apply(Fj, order, "y"); cache[(a, b)] = (cur, order - 1)
                D[(a, b)] = cur[(0, 0)]
        return D


def _test():
    """Consistency tests: order-0 against residual_modes; t-derivatives against finite differences; Cartesian derivatives against
    finite differences of the mode sum."""
    T = Trial(np.load("data/trial_v2_h0.008.npz")); G = TrialGreen(T); G.build()
    J = TrialJets(G, K=4)
    t = np.array([2.05, 2.1517, 2.2]); th = np.array([0.003, 0.02, 0.05, 0.3])
    E, RHO, PSI = J.eps_jets(t, th)
    eps_modes = G.residual_modes(t); N = np.arange(eps_modes.shape[1])
    E0 = eps_modes @ np.sin((2 * N[:, None] + 1) * th[None, :])
    print("order 0 vs residual_modes: max rel diff %.2e" % (np.abs(E[(0, 0)] - E0).max() / np.abs(E0).max()))
    # t-derivatives by finite differences of the mode sum
    h = 1e-4
    for i in [1, 2, 3, 4]:
        st = np.arange(-i, i + 1) if i % 2 == 0 else np.arange(-(i + 1) // 2 - 0, (i + 1) // 2 + 1)
        # use simple central stencils via np.polyfit-free approach: finite difference weights from Fornberg
        from scipy.special import comb as scomb
        pts = np.arange(-3, 4) * h  # 7-point stencil
        Vand = np.vander(pts, increasing=True).T   # rows: powers
        rhs = np.zeros(7); rhs[i] = __import__("math").factorial(i)
        w = np.linalg.solve(Vand, rhs)
        fd = np.zeros((len(t), len(th)))
        for wk, pk in zip(w, pts):
            em = G.residual_modes(t + pk); fd += wk * (em @ np.sin((2 * N[:, None] + 1) * th[None, :]))
        print("d_t^%d: jet vs FD(h=%.0e): rel diff %.2e   (|jet| max %.3e)" % (i, h, np.abs(E[(i, 0)] - fd).max() / np.abs(E[(i, 0)]).max(), np.abs(E[(i, 0)]).max()))
    # Cartesian derivatives at one point vs finite differences in x, y of the mode sum
    D = J.polar_to_cart(E, t, th, 4)
    x0, y0 = np.exp(t[1]) * np.cos(th[2]), np.exp(t[1]) * np.sin(th[2])
    def eps_xy(x, y):
        rr = np.hypot(x, y); tt = np.log(rr); hh = np.arctan2(y, x)
        em = G.residual_modes(np.atleast_1d(tt)); return (em @ np.sin((2 * N + 1) * hh))[0]
    hx = 1e-3
    pts = np.arange(-3, 4) * hx
    Vand = np.vander(pts, increasing=True).T
    import math
    for (a, b) in [(1, 0), (0, 1), (2, 0), (1, 1), (0, 2), (3, 0), (0, 3), (2, 2), (4, 0), (0, 4), (3, 1), (1, 3)]:
        wa = np.linalg.solve(Vand, np.eye(7)[a] * math.factorial(a)); wb = np.linalg.solve(Vand, np.eye(7)[b] * math.factorial(b))
        fd = 0.0
        for wi, pi in zip(wa, pts):
            if wi == 0: continue
            for wj, pj in zip(wb, pts):
                if wj == 0: continue
                fd += wi * wj * eps_xy(x0 + pi, y0 + pj)
        print("D^(%d,%d) eps at (%.3f, %.3f): jet %.6e  FD %.6e  rel %.1e" % (a, b, x0, y0, D[(a, b)][1, 2], fd, abs(D[(a, b)][1, 2] - fd) / max(abs(fd), 1e-300)))


if __name__ == "__main__":
    _test()
