"""Fast floating-point assembly of the linearized operator L on single-mode radial basis functions (evidence only).

  L h = (V~.grad - 1) h + W[h].grad rho~,   W[h] = U[h] + (c[h]/3) X,   h = x^2 y b(t) cos(2m theta),  t = log r,
with b an exponential-polynomial piecewise function (pieces (t_lo, t_hi, alpha, coeffs) in sigma = t - t_lo; t_lo = -inf: sigma = t - t_hi).
Output: the sine modes (L h)_N(t_i), N < Mout, at the collocation radii t_i, and the scalar c[h].

Green data of the single-mode density: for every piece the complete moments give A_n(t) = e^{-2n(t - t_hi)} A_piece(t_hi) for t >= t_hi
and B_n(t) = e^{-2n(t_lo - t)} B_piece(t_lo) for t <= t_lo (closed forms, vectorized over the collocation radii); only radii inside a
piece need incomplete integrals (trial_green._AB_terms). Same formulas and sign conventions as trial_green (validated there and in the
certificate); consistency with finite_section2.column and with the identity L rho~ = 2 eps~ + rho~ - X.grad rho~/3 is tested in __main__.
"""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from expoly import scaled_integral
from trial_green import TrialGreen
from modal_fit import Trial


class ExpPolyBasis:
    def __init__(self, pieces):
        self.pieces = [(float(a), float(b), float(al), np.asarray(c, float)) for (a, b, al, c) in pieces]

    def eval(self, t, nu=0):
        t = np.atleast_1d(np.asarray(t, float)); out = np.zeros_like(t)
        for (a, b, alpha, c) in self.pieces:
            if np.isinf(a): sel = t < b; sig = t[sel] - b
            elif np.isinf(b): sel = t >= a; sig = t[sel] - a
            else: sel = (t >= a) & (t < b); sig = t[sel] - a
            if not sel.any(): continue
            cc = c.copy()
            for _ in range(nu):
                dc = alpha * cc
                if len(cc) > 1: dc[:-1] += cc[1:] * np.arange(1, len(cc))
                cc = dc
            pv = np.zeros_like(sig)
            for j in range(len(cc) - 1, -1, -1): pv = pv * sig + cc[j]
            out[sel] += np.exp(alpha * sig) * pv
        return out


class LinAssembler:
    def __init__(self, G, t_eval, Mout):
        self.G = G; self.t = np.asarray(t_eval, float); self.Ne = len(self.t); self.n = G.n; self.Nf = G.Nf; self.M = G.M
        self.Mout = Mout; self.c_l = G.c_l
        self.R, self.Rt = G.rho_modes(self.t)                     # background density modes R_j, d_t R_j  (Ne, M+1)
        psi, dpsi = G.psi_at(self.t)                               # psi_n, psi_r  (Ne, Nf)
        self.P = 2 * self.n[None, :] * psi; self.Q = dpsi
        self.em = np.exp(-self.t); self.em2 = np.exp(-2 * self.t); self.e3 = np.exp(3 * self.t)
        self.r = np.exp(self.t)

    # ---- Green data of a single-mode density ----
    def green(self, m, basis):
        G = self.G; n = self.n; Nf = self.Nf; t = self.t; Ne = self.Ne
        A = np.zeros((Ne, Nf)); B = np.zeros((Ne, Nf))
        for (a, b, alpha, c) in basis.pieces:
            cmat = np.zeros((len(c), self.M)); cmat[:, m] = c
            if np.isinf(a):
                base = b; ft = G._f_expoly([(alpha, cmat)], np.exp(2 * base)); e2 = np.exp(2 * base)
                Ap = e2 * G._acc(ft, "in", -np.inf, 0.0, 0.0)                     # A_piece(b)
                out = t >= b
                if out.any(): A[out] += np.exp(-2 * np.outer(t[out] - b, n)) * Ap[None, :]
                for i in np.where(~out)[0]:
                    tau = t[i] - b
                    accA, accB = G._AB_terms(ft, tau, -np.inf, tau, tau, 0.0)
                    A[i] += e2 * accA; B[i] += e2 * accB
            elif np.isinf(b):
                base = a; ft = G._f_expoly([(alpha, cmat)], np.exp(2 * base)); e2 = np.exp(2 * base)
                Bp = e2 * G._acc(ft, "out", 0.0, np.inf, 0.0)                     # B_piece(a)
                out = t <= a
                if out.any(): B[out] += np.exp(-2 * np.outer(a - t[out], n)) * Bp[None, :]
                for i in np.where(~out)[0]:
                    tau = t[i] - a
                    accA, accB = G._AB_terms(ft, tau, 0.0, tau, tau, np.inf)
                    A[i] += e2 * accA; B[i] += e2 * accB
            else:
                base = a; h = b - a; ft = G._f_expoly([(alpha, cmat)], np.exp(2 * base)); e2 = np.exp(2 * base)
                inc = np.zeros(Nf)
                for al2, fc in ft:
                    lam = (2 * n + 2) + al2
                    for p in range(fc.shape[0]):
                        if not np.any(fc[p]): continue
                        unit = np.zeros(fc.shape[0]); unit[p] = 1.0
                        inc += fc[p] * scaled_integral(lam, unit, 0.0, h, -2 * n * h)
                Ap = e2 * inc                                                     # A_piece(b)
                Bp = e2 * G._acc(ft, "out", 0.0, h, 0.0)                           # B_piece(a)
                right = t >= b; left = t <= a; mid = ~(right | left)
                if right.any(): A[right] += np.exp(-2 * np.outer(t[right] - b, n)) * Ap[None, :]
                if left.any(): B[left] += np.exp(-2 * np.outer(a - t[left], n)) * Bp[None, :]
                for i in np.where(mid)[0]:
                    tau = t[i] - a
                    accA, accB = G._AB_terms(ft, tau, 0.0, tau, tau, h)
                    A[i] += e2 * accA; B[i] += e2 * accB
        return A, B

    def c_of(self, m, basis):
        wm = {0: 0.25, 1: 0.125, 2: -0.125, 3: -0.125}.get(m, 0.0)
        if wm == 0.0: return 0.0
        ch = 0.0
        for (a, b, alpha, c) in basis.pieces:
            if np.isinf(a): base, lo, hi = b, -np.inf, 0.0
            elif np.isinf(b): base, lo, hi = a, 0.0, np.inf
            else: base, lo, hi = a, 0.0, b - a
            ch += wm * np.exp(2 * base) * scaled_integral(np.array([2.0 + alpha]), c, lo, hi, np.array([0.0]))[0]
        return ch

    # ---- L applied to one column ----
    def column(self, m, basis, want_parts=False):
        G = self.G; n = self.n; Ne = self.Ne; Mout = self.Mout; t = self.t
        bval = basis.eval(t, 0); bder = basis.eval(t, 1)
        a_vec = np.zeros((Ne, self.M)); a_vec[:, m] = bval; ad_vec = np.zeros((Ne, self.M)); ad_vec[:, m] = bder
        Rh = self.e3[:, None] * G.R_from_a(a_vec); Rht = self.e3[:, None] * (3 * G.R_from_a(a_vec) + G.R_from_a(ad_vec))
        Ah, Bh = self.green(m, basis)
        psih = (Ah + Bh) / (4 * n[None, :]); Ph = 2 * n[None, :] * psih; Qh = (Bh - Ah) / (2 * self.r[:, None])
        ch = self.c_of(m, basis)
        out = np.zeros((Ne, Mout)); outT = np.zeros((Ne, Mout)); outB = np.zeros((Ne, Mout)); outC = np.zeros((Ne, Mout))
        def addsin(arr, freq, coef):
            if freq < 0: freq, coef = -freq, -coef
            if freq == 0: return
            N = (freq - 1) // 2
            if N < Mout: arr[:, N] += coef
        jj = [j for j in range(self.M + 1) if np.any(Rh[:, j]) or np.any(Rht[:, j])]
        for j in jj:
            addsin(outT, 2 * j + 1, self.c_l * Rht[:, j] - Rh[:, j])
        if ch != 0.0:
            for j in range(self.M + 1): addsin(outC, 2 * j + 1, (ch / 3.0) * self.Rt[:, j])
        # background velocity acting on h
        for ni, nn in enumerate(n):
            Pn = self.P[:, ni]; Qn = self.Q[:, ni]
            for j in jj:
                coef = -0.5 * Pn * Rht[:, j] * self.em2; addsin(outT, 2 * j + 1 + 2 * nn, coef); addsin(outT, 2 * j + 1 - 2 * nn, coef)
                coef2 = 0.5 * Qn * (2 * j + 1) * Rh[:, j] * self.em; addsin(outT, 2 * nn + 2 * j + 1, coef2); addsin(outT, 2 * nn - 2 * j - 1, coef2)
        # velocity of h acting on the background
        act = [ni for ni in range(len(n)) if np.any(Ph[:, ni]) or np.any(Qh[:, ni])]
        for ni in act:
            nn = n[ni]; Pn = Ph[:, ni]; Qn = Qh[:, ni]
            for j in range(self.M + 1):
                coef = -0.5 * Pn * self.Rt[:, j] * self.em2; addsin(outB, 2 * j + 1 + 2 * nn, coef); addsin(outB, 2 * j + 1 - 2 * nn, coef)
                coef2 = 0.5 * Qn * (2 * j + 1) * self.R[:, j] * self.em; addsin(outB, 2 * nn + 2 * j + 1, coef2); addsin(outB, 2 * nn - 2 * j - 1, coef2)
        out = outT + outB + outC
        if want_parts: return out, ch, dict(T=outT, B=outB, C=outC, Rh=Rh, Rht=Rht, psih=psih, Qh=Qh)
        return out, ch

    def assemble(self, cols, verbose=200):
        """cols: list of (m, basis, label). Returns Mat (Ne*Mout, ncol), cvec (ncol,)."""
        ncol = len(cols); Mat = np.zeros((self.Ne * self.Mout, ncol)); cvec = np.zeros(ncol); t0 = time.time()
        for ic, (m, basis, label) in enumerate(cols):
            out, ch = self.column(m, basis); Mat[:, ic] = out.ravel(); cvec[ic] = ch
            if verbose and (ic + 1) % verbose == 0: print("  column %d/%d (%.0fs)" % (ic + 1, ncol, time.time() - t0), flush=True)
        return Mat, cvec


def trial_mode_basis(T, m):
    """The trial's own a_m as one ExpPolyBasis (inner + spline cells + outer)."""
    from scipy.interpolate import BSpline
    from math import factorial
    pieces = []
    inner = T.inner_terms(); outer = T.outer_terms()
    for alpha, c in inner: pieces.append((-np.inf, T.tmin, alpha, c[:, m]))
    kn = T.knots[T.p + 1:-(T.p + 1)]; tb = np.r_[T.tmin, kn, T.t0]
    spl = BSpline(T.knots, T.S.T, T.p, extrapolate=True)
    pc = np.stack([spl(tb[:-1], nu=i) / factorial(i) for i in range(T.p + 1)], axis=1)   # (nc, p+1, M)
    for ci in range(len(tb) - 1): pieces.append((tb[ci], tb[ci + 1], 0.0, pc[ci, :, m]))
    for alpha, c in outer: pieces.append((T.t0, np.inf, alpha, c[:, m]))
    return ExpPolyBasis(pieces)


def _test():
    T = Trial(np.load("data/trial_small_M20.npz")); G = TrialGreen(T); G.build()
    t_eval = np.array([-6.0, T.tmin - 0.3, -3.0, -1.0, 0.5, 1.5, 2.1517, 3.0, 5.0, 7.0, T.t0 + 0.3, 9.5])
    Mout = 2 * G.M + 3
    LA = LinAssembler(G, t_eval, Mout)
    # identity: sum_m L(a_m-column) = L rho~ = 2 eps~ + rho~ - G/3   (G = X.grad rho~ = Rt modes)
    tot = np.zeros((len(t_eval), Mout)); ctot = 0.0; t0 = time.time()
    for m in range(G.M):
        out, ch = LA.column(m, trial_mode_basis(T, m)); tot += out; ctot += ch
    print("assembly of %d trial-mode columns: %.1fs; c[rho~] = %.12f (closed form %.12f)" % (G.M, time.time() - t0, ctot, G.c))
    eps = G.residual_modes(t_eval); R, Rt = G.rho_modes(t_eval)
    ref = 2 * eps[:, :Mout]; ref[:, :R.shape[1]] += R - Rt / 3.0
    for i, tt in enumerate(t_eval):
        print("  t = %7.3f: max|L rho~ - (2eps + rho - G/3)| = %.2e   (|L rho~| max %.2e, |eps| max %.2e)" % (tt, np.abs(tot[i] - ref[i]).max(), np.abs(tot[i]).max(), np.abs(eps[i]).max()))
    # consistency with finite_section2.column for a few spline basis functions
    import finite_section2 as FS
    radial, knots = FS.build_basis(T, 8)
    t_eval2 = np.linspace(T.tmin - 1, T.t0 + 1, 37); LA2 = LinAssembler(G, t_eval2, 12)
    for (bas, lab) in [radial[0], radial[3], radial[10], radial[len(radial) // 2], radial[-3], radial[-1]]:
        for m in [0, 3, 9]:
            o1, c1 = LA2.column(m, ExpPolyBasis(bas.pieces))
            # finite_section2.column equivalent: reimplement via its code path (green_single + same scatter) using its own module
            A2, B2 = FS.green_single(G, m, bas, t_eval2); A1, B1 = LA2.green(m, ExpPolyBasis(bas.pieces))
            print("  basis %-6s m=%2d: Green max|dA| %.1e |dB| %.1e (scale %.1e) c=%.3e" % (lab, m, np.abs(A1 - A2).max(), np.abs(B1 - B2).max(), max(np.abs(A2).max(), np.abs(B2).max(), 1e-300), c1))


if __name__ == "__main__":
    _test()
