"""Fit the explicit modal trial  rho~ = x^2 y sum_{m<M} a_m(r) cos(2 m theta)  to the cosine modes of e^H of X3.
Each a_m is an exponential-polynomial spline in t = log r (three regions, joined C^6 exactly):
  inner  r <  rmin : a_m = delta_{m0} + sum_{j=1}^{7} D_mj e^{2j tau'} + e^{bi tau'} sum_{i=0}^{6} Ei_mi tau'^i,   tau' = t - tmin <= 0
  middle rmin..R0  : degree-7 B-spline in t, knots = X3's knots (mapped to t) with intervals longer than h subdivided,
                     plus uniform knots (spacing h_in) below X3's first knot
  outer  r >  R0   : a_m = sum_q A_mq e^{alpha_q tau} + e^{-bo tau} sum_{i=0}^{6} Eo_mi tau^i,   tau = t - t0 >= 0,
                     alpha_q = (k-3) - j_q (1-k) - 2 l_q, (j,l) in OUTER_JL (10 power laws: u^{k-3} nu^j u^{-2l}).
The local corrections (exponents bi = 1/h_first, bo = 1/h_last) absorb the jet mismatch at the joins without
disturbing the far field or the centre.  Normalization: c = psi_xy(0) = int_0^oo r (a_0/4 + a_1/8 - a_2/8 - a_3/8) dr
must equal 3/k - 1 (so that c_l = 1/k exactly); imposed as a linear constraint (LS-optimal correction).
Constrained least squares (nullspace method), relative weighting by the base factor (1+u^2)^{(k-3)/2}.
Usage: python3 modal_fit.py modes.npz h h_in out.npz
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.interpolate import BSpline, PPoly
from scipy.linalg import null_space, qr
from scipy.fft import dct
from x3 import X3
from expoly import integral_exp_poly, integ_shift

OUTER_JL = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (0, 1), (1, 1), (2, 1), (0, 2)]
NIN = 7            # inner power terms e^{2j tau'}, j = 1..7
NCOR = 7           # local correction terms tau^i e^{-+b tau}, i = 0..6  (C^6 joins)
P = 7              # B-spline degree in t
NOUT = len(OUTER_JL)


def outer_alphas(k):
    return np.array([(k - 3) - j * (1 - k) - 2 * l for (j, l) in OUTER_JL])


class Trial:
    """The fitted representation; float64 evaluation of a_m^{(nu)}(t)."""
    def __init__(self, d):
        self.k = float(d["k"]); self.L = float(d["L"]); self.rmin = float(d["rmin"]); self.R0 = float(d["R0"])
        self.knots = np.asarray(d["knots"]); self.p = int(d["p"])
        self.D = np.asarray(d["D"]); self.Ei = np.asarray(d["Ei"]); self.S = np.asarray(d["S"])
        self.Aout = np.asarray(d["Aout"]); self.Eo = np.asarray(d["Eo"]); self.bi = float(d["bi"]); self.bo = float(d["bo"])
        self.M = self.S.shape[0]
        self.tmin, self.t0 = float(self.knots[0]), float(self.knots[-1])        # DEFINITION: joins at the stored knots
        self.alpha_out = outer_alphas(self.k)
        self.spl = BSpline(self.knots, self.S.T, self.p, extrapolate=False)

    def inner_terms(self):
        """ExpPoly terms of a_m in tau' = t - tmin: list of (alpha, coeffs (deg+1, M))."""
        terms = [(0.0, np.r_[1.0, np.zeros(self.M - 1)][None, :])]
        for j in range(NIN): terms.append((2.0 * (j + 1), self.D[:, j][None, :]))
        terms.append((self.bi, self.Ei.T.copy()))           # (7, M)
        return terms

    def outer_terms(self):
        terms = [(float(self.alpha_out[q]), self.Aout[:, q][None, :]) for q in range(NOUT)]
        terms.append((-self.bo, self.Eo.T.copy()))
        return terms

    @staticmethod
    def _eval_terms(terms, tau, nu):
        """sum_terms d^nu/dtau^nu [e^{alpha tau} p(tau)] at tau (n,) -> (n, M)."""
        out = 0.0
        for alpha, c in terms:
            c = c.copy()
            for _ in range(nu):            # derivative of e^{a tau} p: e^{a tau}(a p + p')
                dc = alpha * c
                if c.shape[0] > 1: dc[:-1] += c[1:] * np.arange(1, c.shape[0])[:, None]
                c = dc
            pv = np.zeros((len(tau), c.shape[1]))
            for i in range(c.shape[0] - 1, -1, -1): pv = pv * tau[:, None] + c[i][None, :]
            out = out + np.exp(alpha * tau)[:, None] * pv
        return out

    def eval(self, t, nu=0):
        t = np.atleast_1d(np.asarray(t, float)); out = np.empty((len(t), self.M))
        inn = t < self.tmin; mid = (t >= self.tmin) & (t <= self.t0); out_ = t > self.t0
        if inn.any(): out[inn] = self._eval_terms(self.inner_terms(), t[inn] - self.tmin, nu)
        if mid.any(): out[mid] = self.spl(t[mid], nu=nu)
        if out_.any(): out[out_] = self._eval_terms(self.outer_terms(), t[out_] - self.t0, nu)
        return out


def build_knots(X, h, h_in, rmin, R0):
    k = X.k; L = X.L
    qk = X.knots[X.order + 1:-(X.order + 1)]
    uk = np.sqrt((1 - qk) ** (-2 / (1 - k)) - 1); tk = np.log(L * uk)
    tk = tk[L * uk <= R0 * (1 + 1e-12)]                 # knots up to R0 (R0 itself is one of them)
    assert abs(L * uk[len(tk) - 1] - R0) < 1e-9
    tmin = np.log(rmin)
    kn = list(np.arange(tmin, tk[0], h_in)[1:])
    for a, b in zip(tk[:-1], tk[1:]):
        n = int(np.ceil((b - a) / h - 1e-9))
        kn.extend(np.linspace(a, b, n + 1)[:-1])
    kn.append(tk[-1])
    kn = np.array(kn); kn = kn[(kn > tmin) & (kn < np.log(R0))]
    return np.r_[np.full(P + 1, tmin), kn, np.full(P + 1, np.log(R0))]


class Basis:
    """Column layout: [inner powers (7) | inner corrections (7) | spline (nb) | outer powers (10) | outer corrections (7)]."""
    def __init__(self, X, knots, rmin, R0):
        self.k = X.k; self.knots = knots; self.nb = len(knots) - P - 1; self.rmin, self.R0 = rmin, R0
        self.tmin, self.t0 = np.log(rmin), np.log(R0)
        self.bi = 1.0 / (knots[P + 1] - self.tmin)            # first cell length
        self.bo = 1.0 / (self.t0 - knots[-P - 2])             # last cell length
        self.alpha = outer_alphas(X.k)
        self.n = NIN + NCOR + self.nb + NOUT + NCOR
        self.sl_in = slice(0, NIN); self.sl_ic = slice(NIN, NIN + NCOR); self.sl_sp = slice(NIN + NCOR, NIN + NCOR + self.nb)
        self.sl_out = slice(NIN + NCOR + self.nb, NIN + NCOR + self.nb + NOUT); self.sl_oc = slice(self.n - NCOR, self.n)

    @staticmethod
    def _poly_exp_cols(alpha, tau, nu):
        """columns d^nu/dtau^nu [e^{alpha tau} tau^i], i = 0..NCOR-1, at tau (n,) -> (n, NCOR)."""
        cols = np.zeros((len(tau), NCOR))
        for i in range(NCOR):
            c = np.zeros(NCOR); c[i] = 1.0
            for _ in range(nu):
                dc = alpha * c; dc[:-1] += c[1:] * np.arange(1, NCOR); c = dc
            pv = np.zeros(len(tau))
            for q in range(NCOR - 1, -1, -1): pv = pv * tau + c[q]
            cols[:, i] = np.exp(alpha * tau) * pv
        return cols

    def design(self, t, nu=0, regions=None):
        """regions=None: each t uses its own region; otherwise a set of region names ('inner','spline','outer') evaluated
        at every t (used for the join conditions)."""
        t = np.atleast_1d(np.asarray(t, float)); Dm = np.zeros((len(t), self.n))
        if regions is None:
            inn = t < self.tmin; mid = (t >= self.tmin) & (t <= self.t0); out_ = t > self.t0
        else:
            ones = np.ones(len(t), bool); zeros = np.zeros(len(t), bool)
            inn = ones if 'inner' in regions else zeros; mid = ones if 'spline' in regions else zeros; out_ = ones if 'outer' in regions else zeros
        j = np.arange(1, NIN + 1)
        tau_i = t[inn] - self.tmin
        Dm[np.ix_(inn, np.arange(NIN))] = np.exp(2 * j[None, :] * tau_i[:, None]) * (2.0 * j[None, :]) ** nu
        Dm[np.ix_(inn, np.arange(NIN, NIN + NCOR))] = self._poly_exp_cols(self.bi, tau_i, nu)
        B = BSpline(self.knots, np.eye(self.nb), P, extrapolate=True)(t[mid], nu=nu)
        Dm[np.ix_(mid, np.arange(NIN + NCOR, NIN + NCOR + self.nb))] = np.nan_to_num(B)
        tau_o = t[out_] - self.t0
        Dm[np.ix_(out_, np.arange(self.sl_out.start, self.sl_out.stop))] = np.exp(self.alpha[None, :] * tau_o[:, None]) * self.alpha[None, :] ** nu
        Dm[np.ix_(out_, np.arange(self.sl_oc.start, self.sl_oc.stop))] = self._poly_exp_cols(-self.bo, tau_o, nu)
        return Dm

    def constraints(self):
        """C^6 joins: rows i: [spline^{(i)} - inner^{(i)}](tmin) = delta_{m0} delta_{i0}; rows 7+i: [spline^{(i)} - outer^{(i)}](t0) = 0."""
        C = np.zeros((2 * NCOR, self.n))
        for i in range(NCOR):
            rowL = self.design(np.array([self.tmin]), nu=i, regions=('inner', 'spline'))[0]
            rowR = self.design(np.array([self.t0]), nu=i, regions=('spline', 'outer'))[0]
            C[i, self.sl_sp] = rowL[self.sl_sp]; C[i, self.sl_in] = -rowL[self.sl_in]; C[i, self.sl_ic] = -rowL[self.sl_ic]
            C[NCOR + i, self.sl_sp] = rowR[self.sl_sp]; C[NCOR + i, self.sl_out] = -rowR[self.sl_out]; C[NCOR + i, self.sl_oc] = -rowR[self.sl_oc]
        return C

    def c_functional(self):
        """kappa (n,): int_0^oo r * basis(r) dr = int e^{2t} basis(t) dt for every column (closed forms)."""
        kap = np.zeros(self.n); e2min = np.exp(2 * self.tmin); e20 = np.exp(2 * self.t0)
        j = np.arange(1, NIN + 1)
        kap[self.sl_in] = e2min / (2 + 2 * j)                                        # int_{-inf}^0 e^{2 tau'} e^{2j tau'} dtau' * e^{2 tmin}
        for i in range(NCOR):
            c = np.zeros(NCOR); c[i] = 1.0
            kap[NIN + i] = e2min * integral_exp_poly(2.0 + self.bi, c, -np.inf, 0.0)
            kap[self.sl_oc.start + i] = e20 * integral_exp_poly(2.0 - self.bo, c, 0.0, np.inf)
        kap[self.sl_out] = e20 * (-1.0 / (2.0 + self.alpha))                          # int_0^oo e^{(2+alpha) tau}, alpha < -2
        # spline: exact piecewise-polynomial x e^{2t} integrals; per-cell Taylor coefficients from derivatives at the cell start
        from math import factorial
        kn = self.knots[P + 1:-(P + 1)]; tb = np.r_[self.tmin, kn, self.t0]
        spl = BSpline(self.knots, np.eye(self.nb), P, extrapolate=True)
        for ci in range(len(tb) - 1):
            ta, tbb = tb[ci], tb[ci + 1]
            coef = np.stack([spl(np.array([ta]), nu=i)[0] / factorial(i) for i in range(P + 1)])     # (P+1, nb) ascending
            for b in range(self.nb):
                if not np.any(coef[:, b]): continue
                kap[self.sl_sp.start + b] += np.exp(2 * ta) * integ_shift(np.array([2.0]), coef[:, b], 0.0, tbb - ta, 0.0)[0]
        return kap


def main(modes_path, h, h_in, out, Mcut=None, R0_index=-1):
    X = X3(); k = X.k; L = X.L
    d = np.load(modes_path); t = d["t"]; A = d["A"]; r = d["r"]
    if Mcut is not None: A = A[:, :Mcut]
    M = A.shape[1]
    qk = X.knots[X.order + 1:-(X.order + 1)]
    R0 = L * np.sqrt((1 - qk[R0_index]) ** (-2 / (1 - k)) - 1); rmin = 1e-3 * L      # R0 = an X3 knot (default the last)
    knots = build_knots(X, h, h_in, rmin, R0)
    Bs = Basis(X, knots, rmin, R0)
    print("degree %d; nb = %d spline functions, %d columns; rmin = %.5g, R0 = %.5g (%.1f L); bi = %.1f, bo = %.1f" % (
        P, Bs.nb, Bs.n, rmin, R0, R0 / L, Bs.bi, Bs.bo), flush=True)
    sel = (r >= rmin / 3.0)
    ts, As = t[sel], A[sel]
    w = 1.0 / (1 + (np.exp(ts) / L) ** 2) ** ((k - 3) / 2)
    t0_ = time.time()
    Dm = Bs.design(ts)
    # column scaling (the correction columns tau^i e^{-b tau} are tiny): work in scaled coordinates coef = cs * coef_s
    cs = 1.0 / np.maximum(np.linalg.norm(Dm * w[:, None], axis=0), 1e-300)
    Dm = Dm * cs[None, :]
    C = Bs.constraints() * cs[None, :]; rs = np.linalg.norm(C, axis=1); C = C / rs[:, None]
    Z = null_space(C)
    e0 = np.zeros(2 * NCOR); e0[0] = 1.0 / rs[0]
    cp0 = C.T @ np.linalg.solve(C @ C.T, e0)
    Y = As.copy(); inn_rows = ts < np.log(rmin); Y[inn_rows, 0] -= 1.0
    DZ = (Dm @ Z) * w[:, None]
    print("design %d x %d, nullspace %d; QR ..." % (Dm.shape[0], Dm.shape[1], Z.shape[1]), flush=True)
    Q, R = qr(DZ, mode="economic")
    rhs = Y * w[:, None]; rhs[:, 0] -= (Dm @ cp0) * w
    y = np.linalg.solve(R, Q.T @ rhs)
    NORMALIZE = os.environ.get('TRIAL_NORMALIZE', '1') == '1'
    # normalization constraint c = int r (a_0/4 + a_1/8 - a_2/8 - a_3/8) dr = 3/k - 1  (couples modes 0..3): LS-optimal correction
    kap = Bs.c_functional() * cs; kapZ = Z.T @ kap          # functional in scaled coordinates
    weights_m = np.array([0.25, 0.125, -0.125, -0.125])
    c_now = sum(weights_m[m] * (kap @ (Z @ y[:, m] + (cp0 if m == 0 else 0.0))) for m in range(4))
    c_const = 0.25 * np.exp(2 * np.log(rmin)) / 2.0        # the fixed constant a_0 = 1 on r < rmin: int_0^rmin r/4 dr
    c_now += c_const
    target = 3.0 / k - 1.0
    print("c before normalization correction: %.12f, target 3/k-1 = %.12f, difference %.3e" % (c_now, target, c_now - target))
    # minimize sum_m ||R dy_m||^2 s.t. sum_m w_m kapZ . dy_m = target - c_now  ->  dy_m = lam w_m (R^T R)^{-1} kapZ
    g = np.linalg.solve(R, np.linalg.solve(R.T, kapZ))         # (R^T R)^{-1} kapZ
    denom = sum(weights_m[m] ** 2 for m in range(4)) * (kapZ @ g)
    lam = (target - c_now) / denom
    if NORMALIZE:
        for m in range(4): y[:, m] += lam * weights_m[m] * g
    else:
        print('normalization correction skipped (TRIAL_NORMALIZE=0)')
    coef = Z @ y; coef[:, 0] += cp0
    c_after = sum(weights_m[m] * (kap @ coef[:, m]) for m in range(4)) + c_const
    coef = coef * cs[:, None]; Dm = Dm / cs[None, :]; kap = kap / cs       # back to unscaled coordinates
    print("c after correction: %.15f (target %.15f); fit done in %.1fs" % (c_after, target, time.time() - t0_), flush=True)
    fit = Dm @ coef; fit[inn_rows, 0] += 1.0
    rel = np.abs(fit - As) * w[:, None]
    print("fit residual on samples (relative to base): max %.2e; modes 0,1,100: %.2e %.2e %.2e" % (rel.max(), rel[:, 0].max(), rel[:, 1].max(), rel[:, 100].max()))
    D = coef[Bs.sl_in].T; Ei = coef[Bs.sl_ic].T; S = coef[Bs.sl_sp].T; Aout = coef[Bs.sl_out].T; Eo = coef[Bs.sl_oc].T
    np.savez_compressed(out, k=k, L=L, rmin=rmin, R0=R0, knots=knots, D=D, Ei=Ei, S=S, Aout=Aout, Eo=Eo, bi=Bs.bi, bo=Bs.bo,
                        h=h, h_in=h_in, M=M, p=P, c_target=target, kappa=kap)
    validate(out, X)


def validate(path, X):
    k = X.k; L = X.L; T = Trial(np.load(path)); M = T.M
    rng = np.random.default_rng(7)
    tv = np.sort(rng.uniform(np.log(1e-4 * L), np.log(1e5 * L), 1500)); rv = np.exp(tv)
    th = np.linspace(0, np.pi / 2, 4097)
    Hv, Hr, Ht = X.H(rv, th); eH = np.exp(Hv)
    cv = dct(eH, type=1, axis=1) / 4096; cv[:, 0] *= 0.5
    cvt = dct(eH * Hr * rv[:, None], type=1, axis=1) / 4096; cvt[:, 0] *= 0.5
    base = (1 + (rv / L) ** 2) ** ((k - 3) / 2)
    fv = T.eval(tv, 0); fvt = T.eval(tv, 1)
    err = np.abs(fv - cv[:, :M]) / base[:, None]; errt = np.abs(fvt - cvt[:, :M]) / base[:, None]
    trunc = np.abs(cv[:, M:]).max(1) / base
    regions = {"inner r<rmin": rv < T.rmin, "middle": (rv >= T.rmin) & (rv <= T.R0), "outer r>R0": rv > T.R0, "all": rv > 0}
    for name, msk in regions.items():
        i0, m0 = np.unravel_index(np.argmax(err[msk]), err[msk].shape)
        print("validation %-14s: max rel err values %.2e (mode %d, r=%.4g), derivatives %.2e, dropped modes %.1e" % (
            name, err[msk].max(), m0, rv[msk][i0], errt[msk].max(), trunc[msk].max()))
    wien = np.abs(fv - cv[:, :M]).sum(1) / base; wient = np.abs(fvt - cvt[:, :M]).sum(1) / base
    print("validation: max_r sum_m |fit - true|/base = %.2e (values), %.2e (t-derivatives)" % (wien.max(), wient.max()))
    # join check: jets at tmin and t0 from both sides
    for tj, name in ((T.tmin, "tmin"), (T.t0, "t0")):
        left = T.eval(np.array([tj - 1e-12]), 0); right = T.eval(np.array([tj + 1e-12]), 0)
        print("join at %s: max |a(left) - a(right)| = %.2e" % (name, np.abs(left - right).max()))


if __name__ == "__main__":
    a = sys.argv
    main(a[1], float(a[2]), float(a[3]), a[4], int(a[5]) if len(a) > 5 and a[5] != "-" else None, int(a[6]) if len(a) > 6 else -1)
