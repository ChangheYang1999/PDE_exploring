"""verifier: axis data from SAMPLED traces (x, w, w', w'') on a uniform grid in t = log x (first-run gen4 traces), with the
interface of vaxis.AxisData, so that vaxis.B3 runs unchanged (written for this run), and the integrated-by-parts estimator
fp_ibp below (needs w'' but not w''' on [xc, x*]).

Jets at the Gauss-Legendre nodes of axis panels: w, w', w'' by local polynomial fits in t (interpolation on n points, or
least squares of degree p on n points); w''' = (1/x) d/dt of the fit of w''.  For x < x* only samples with x_i < x* are
used (onesided; w''' of the traces jumps at x*).  Near x* (x > (1 - near_frac) x*) the fits (near_n, near_p) apply to
w, w', w'' (least squares: extrapolation of a high-degree interpolant from x_i < x* to x* amplifies the sample noise).
g = g_w from w: (log g)' = (w' - A_g)/w, g ~ x^2 at 0.  h(P) regularization (the traces have h(P) - 1 = 2c_l - 1 - w'(x*)
of order 1e-6 to 1e-5, which makes g_w and H_3 weakly singular at x*):
  reg = 'cl':  c_l replaced by c_l_eff = (1 + mu1)/2, mu1 = w'(x*) (A_g = A_eff = mu1, constant);
  reg = 'Ag':  A_g(x) = A + (mu1 - A)(x/x*)^2 in the g_w equation only;
  reg = None:  A_g = A.
G_3 is not available (set to 0; T3 and ident are meaningless here)."""
import math
import numpy as np
import torch
from numpy.polynomial import legendre as Lg
from scipy.optimize import brentq
from scipy.special import roots_jacobi
import jets as J
from vaxis import AxisData

DT = torch.float64


class TraceAxis(AxisData):
    def __init__(self, path, c_l=None, wppkey='wpp_ode', K=3, q=20, xmin=1e-3, hmax=0.25, fit01=(12, 11), fit2=(12, 11),
                 onesided=True, near_frac=0.0, near_fit=(24, 6), reg='cl', extra_breaks=()):
        z = np.load(path, allow_pickle=True)
        self.path = path
        self.xd = np.asarray(z['x'], float)
        self.td = np.log(self.xd)
        self.dtd = float(np.mean(np.diff(self.td)))
        assert np.abs(np.diff(self.td) - self.dtd).max() < 1e-9 * max(1.0, abs(self.dtd)) + 1e-12
        self.data = np.stack([z['w'], z['wp'], z[wppkey]])          # (3, Nd)
        self.c_l_file = float(z['c_l'])
        self.c_l = self.c_l_file if c_l is None else float(c_l)
        self.K, self.q = K, q
        if K != 3:
            raise ValueError('K = 3 for sampled traces')
        self.fit01, self.fit2, self.near_frac, self.near_fit = fit01, fit2, near_frac, near_fit
        self.mode1, self.mode_tol = None, None
        self.ileft = None
        self.xs = None
        # x* from the centred interpolant of w (w is C^2 across x*), then the one-sided data
        wv = self.data[0]
        i = [k for k in np.where(np.diff(np.sign(wv)) != 0)[0] if self.xd[k] > 1e-2][0]
        self.xs = brentq(lambda x: self._vals(np.array([x]))[0][0, 0], self.xd[i], self.xd[i + 1], xtol=1e-15, rtol=1e-15)
        if onesided:
            self.ileft = int(np.searchsorted(self.xd, self.xs) - 1)
            self.xs = brentq(lambda x: self._vals(np.array([x]))[0][0, 0], self.xd[i] - 2 * (self.xd[i + 1] - self.xd[i]),
                             self.xd[i + 1] + 2 * (self.xd[i + 1] - self.xd[i]), xtol=1e-15, rtol=1e-15)
        self.mu1 = float(self._vals(np.array([self.xs]))[0][1, 0])
        self.hP_file = 2 * self.c_l_file - self.mu1                     # h(P) of the trace with its own c_l
        self.reg = reg
        if reg == 'cl':
            self.c_l = (1 + self.mu1) / 2
        A = 2 * self.c_l - 1
        self.Ag = (lambda X: A + (self.mu1 - A) * (X / self.xs) ** 2) if reg == 'Ag' else (lambda X: A + 0 * X)
        self.Ag_jet = (lambda X: J.const(torch.full_like(X, A), 1) + (self.mu1 - A) / self.xs ** 2 * J.mul(J.var(X, 1), J.var(X, 1))[:2]) \
            if reg == 'Ag' else (lambda X: J.const(torch.full_like(X, A), 1))
        ts = math.log(self.xs)
        b = np.arange(math.log(xmin), ts, hmax)
        self.b = np.unique(np.concatenate([[math.log(xmin)], b[b > math.log(xmin)], list(extra_breaks), [ts]]))
        self.b = self.b[np.concatenate([[True], np.diff(self.b) > 1e-3])]
        self.b[-1] = ts
        self.P = len(self.b) - 1
        self.xg, self.wg = Lg.leggauss(q)
        self.t = np.concatenate([self.b[j] + (self.xg + 1) * (self.b[j + 1] - self.b[j]) / 2 for j in range(self.P)])
        self.x = np.exp(self.t)
        self.wj = self.jets_at(self.x)
        self.coef = {key: self._fit(arr) for key, arr in self.wj.items()}
        self._build_g()

    # ---------------- local fits ----------------
    def _weights(self, t, n, pdeg):
        """Local polynomial fit (degree pdeg) in t on n consecutive samples: stencil indices and weights for the value and
        for d/dt at the points t (interpolation if n = pdeg + 1, least squares otherwise)."""
        u = (t - self.td[0]) / self.dtd
        jmax = len(self.td) - n if self.ileft is None else self.ileft - n + 1
        j0 = np.clip(np.floor(u).astype(int) - (n // 2 - 1), 0, jmax)
        tau = u - j0
        k = np.arange(n)
        c = 0.5 * n                                                                          # scaling (conditioning)
        V = ((k[None, :, None] - tau[:, None, None]) / c) ** np.arange(pdeg + 1)[None, None, :]
        Pi = np.linalg.pinv(V)                                                              # (nt, pdeg+1, n)
        return j0[:, None] + k[None, :], Pi[:, 0, :], Pi[:, 1, :] / (c * self.dtd)

    def _vals(self, x):
        """(3, n) values of w, w', w'' at x and d/dt of the fit of w''."""
        t = np.log(np.atleast_1d(x))
        near = np.zeros(len(t), bool) if (self.xs is None or self.near_frac <= 0) else \
            np.exp(t) > (1 - self.near_frac) * self.xs
        vals = np.empty((3, len(t)))
        dpp = np.empty(len(t))
        for sel, (n01, p01), (n2, p2) in [(~near, self.fit01, self.fit2), (near, self.near_fit, self.near_fit)]:
            if not sel.any():
                continue
            idx, L0, _ = self._weights(t[sel], n01, p01)
            vals[:2, sel] = np.einsum('cik,ik->ci', self.data[:2][:, idx], L0)
            idx2, M0, M1 = self._weights(t[sel], n2, p2)
            D2 = self.data[2][idx2]
            vals[2, sel] = np.einsum('ik,ik->i', D2, M0)
            dpp[sel] = np.einsum('ik,ik->i', D2, M1)
        return vals, dpp

    def jets_at(self, x):
        x = np.atleast_1d(np.asarray(x, float))
        vals, dpp = self._vals(x)
        W = np.stack([vals[0], vals[1], vals[2] / 2, dpp / x / 6])
        if not hasattr(self, '_cum_e'):
            return dict(w=W, g=np.zeros_like(W), G3=np.zeros_like(W))
        X = torch.as_tensor(x, dtype=DT)
        Wt = torch.as_tensor(W)
        wp = J.deriv(Wt)                                                 # order 2
        Ag = self.Ag_jet(X)                                              # order 1 (A_g is quadratic in x)
        Agj = torch.zeros((3, len(x)), dtype=DT)
        Agj[:2] = Ag
        if self.reg == 'Ag':
            Agj[2] = (self.mu1 - (2 * self.c_l - 1)) / self.xs ** 2
        ratio = J.mul(wp - Agj, J.recip(Wt[:3]))                         # (log g)' jet, order 2
        lg = torch.zeros((4, len(x)), dtype=DT)
        lg[0] = torch.as_tensor(2 * np.log(x) + self._cum_e(x))
        for j in range(1, 4):
            lg[j] = ratio[j - 1] / j
        return dict(w=W, g=J.exp(lg).numpy(), G3=np.zeros_like(W))

    def _build_g(self):
        """Cumulative int_0^x e, e = (w' - A_g)/w - 2/x, on the panels (Legendre), then the g jets at the nodes."""
        W = self.wj['w']
        e = (W[1] - self.Ag(self.x)) / W[0] - 2 / self.x
        C = self._fit(e * self.x)
        xm = math.exp(self.b[0])
        base = (e[0] / self.x[0]) * xm ** 2 / 2.0                       # e = O(x) below xmin
        ints = []
        for j in range(self.P):
            hj = (self.b[j + 1] - self.b[j]) / 2
            ci = Lg.legint(C[j], lbnd=-1) * hj
            ints.append((base, ci))
            base = base + Lg.legval(1.0, ci)

        def cum(xx):
            j, xi = self.locate(np.log(np.atleast_1d(xx)))
            return np.array([ints[jj][0] + Lg.legval(v, ints[jj][1]) for jj, v in zip(j, xi)])
        self._cum_e = cum
        self.wj = self.jets_at(self.x)
        self.coef = {key: self._fit(arr) for key, arr in self.wj.items()}
        return self

    def build_g(self):                                                   # backward compatibility
        return self


def _parts(ad, x):
    W, G = ad.interp('w', x), ad.interp('g', x)
    w, wp, wpp = W[0], W[1], 2 * W[2]
    g, gp = G[0], G[1]
    a2 = 0.5 * (gp - wpp)
    return dict(Q=a2 / g ** 3, m=-w / g, mp=-wp / g + w * gp / g ** 2, w=w, wp=wp, g=g)


def _endfit(f, xe, xs, deg, nf, eta):
    """Least-squares polynomial (degree deg) in sigma = (x* - x)/d, d = x* - xe, of f on nf Chebyshev points of
    sigma in [eta, 1]; returns the monomial coefficients in sigma and the relative fit residual."""
    d = xs - xe
    sg = eta + (1 - eta) * (np.cos(np.pi * (np.arange(nf) + 0.5) / nf) + 1) / 2
    xx = xs - d * sg
    v = f(xx)
    ch = np.polynomial.chebyshev.Chebyshev.fit(sg, v, deg, domain=[0.0, 1.0])
    res = float(np.abs(ch(sg) - v).max() / np.abs(v).max())
    return ch.convert(kind=np.polynomial.Polynomial, domain=[-1, 1], window=[-1, 1]).coef, res


def b3_trace(b, form, xlo, xc, deg=12, frac_e=0.92, end_deg=6, nf=80, eta=0.02, nmid=40):
    """B_3 (natural units) on sampled traces.  [0, xc]: finite-part fit of the F2b integrand (b.fp).  [xc, x*]:
    form 'F2b': int J, J = (1/(3N)) Q' m^(beta-1) (third derivative of w from the data) on [xc, x_e] by Gauss-Legendre;
        on [x_e, x*] J = (x* - x)^(beta - 1) S, S fitted by a polynomial in sigma on [eta, 1] (x_e = frac_e x*), integrated
        exactly;
    form 'ibp': -Q mu|_xc - (beta - 1) f.p. int_xc^x* Q m' m^(beta-2) (needs w'' only), with phi = Q m' n^(beta - 2),
        m = (x* - x) n, fitted on [x_e, x*] in the same way; f.p. int_0^d s^(beta-2) sum c_k (s/d)^k ds
        = d^(beta-1) sum c_k/(beta-1+k) (Hadamard finite part at x*).
    Q = a2/g^3, a2 = (g' - w'')/2, m = -w/g, mu = m^(beta-1), g = stored g_w."""
    ad = b.ad
    be, N, xs = b.be, b.N, ad.xs
    r = b.fp('F2b', xlo, xc, deg=deg)
    xe = frac_e * xs
    d = xs - xe
    tb = np.concatenate([[math.log(xc)], ad.b[(ad.b > math.log(xc)) & (ad.b < math.log(xe))], [math.log(xe)]])
    gq, wq = Lg.leggauss(nmid)
    mid = 0.0
    if form == 'F2b':
        for j in range(len(tb) - 1):
            tt = tb[j] + (gq + 1) * (tb[j + 1] - tb[j]) / 2
            xx = np.exp(tt)
            mid += float(np.sum(wq * b.integrands(xx)['F2b'] * xx) * (tb[j + 1] - tb[j]) / 2)
        c, res = _endfit(lambda xx: b.integrands(xx)['F2b'] * (xs - xx) ** (1 - be), xe, xs, end_deg, nf, eta)
        end = float(d ** be * sum(c[k] / (be + k) for k in range(len(c))))
        B = r['fp0'] + mid + end
    elif form == 'ibp':
        p = _parts(ad, np.array([xc]))
        bnd = -p['Q'][0] * p['m'][0] ** (be - 1)
        for j in range(len(tb) - 1):
            tt = tb[j] + (gq + 1) * (tb[j + 1] - tb[j]) / 2
            xx = np.exp(tt)
            p = _parts(ad, xx)
            mid += float(np.sum(wq * p['Q'] * p['mp'] * p['m'] ** (be - 2) * xx) * (tb[j + 1] - tb[j]) / 2)

        def phi(xx):
            p = _parts(ad, xx)
            return p['Q'] * p['mp'] * (p['m'] / (xs - xx)) ** (be - 2)
        c, res = _endfit(phi, xe, xs, end_deg, nf, eta)
        end = float(d ** (be - 1) * sum(c[k] / (be - 1 + k) for k in range(len(c))))
        B = r['fp0'] + (bnd - (be - 1) * (mid + end)) / (3 * N)
    else:
        raise ValueError(form)
    return dict(B=B, Bnat=B * xs ** (b.p3 - 2), fitres=r['fitres'], endres=res)


def _fp0_fit(fun, expo, xlo, xc, deg, nfit=400):
    """f.p. int_0^xc f, f = x^expo * (even series): least squares of x^(-expo) f by a polynomial in sigma = (x/xc)^2 of
    degree deg on nfit Chebyshev points of sigma in [(xlo/xc)^2, 1]; exact finite part of the monomials."""
    sl = (xlo / xc) ** 2
    sg = sl + (1 - sl) * (np.cos(np.pi * (np.arange(nfit) + 0.5) / nfit) + 1) / 2
    xf = xc * np.sqrt(sg)
    Qv = fun(xf) * xf ** (-expo)
    ch = np.polynomial.chebyshev.Chebyshev.fit(sg, Qv, deg, domain=[sl, 1.0])
    res = float(np.abs(ch(sg) - Qv).max() / np.abs(Qv).max())
    mono = ch.convert(kind=np.polynomial.Polynomial, domain=[-1, 1], window=[-1, 1]).coef
    return float(xc ** (expo + 1) * sum(mono[k] / (expo + 2 * k + 1) for k in range(len(mono)))), res


def b3_ibp_full(b, xlo, xc, deg=12, frac_e=0.92, end_deg=6, nf=80, eta=0.02, nmid=40):
    """B_3 = -((beta - 1)/(3N)) f.p. int_0^x* Q m' m^(beta - 2) dx (integration by parts of the w-only form on the whole
    interval; the boundary terms are pure non-integer powers at 0 and at x*, with zero finite part).  Needs w'' only.
    [0, xc]: even-polynomial fit of x^(5+beta) Q m' m^(beta-2); [xc, x_e]: Gauss-Legendre in t; [x_e, x*]: as b3_trace."""
    ad = b.ad
    be, N, xs = b.be, b.N, ad.xs

    def f(xx):
        p = _parts(ad, xx)
        return p['Q'] * p['mp'] * p['m'] ** (be - 2)
    fp0, fres = _fp0_fit(f, -5 - be, xlo, xc, deg)
    xe = frac_e * xs
    d = xs - xe
    tb = np.concatenate([[math.log(xc)], ad.b[(ad.b > math.log(xc)) & (ad.b < math.log(xe))], [math.log(xe)]])
    gq, wq = Lg.leggauss(nmid)
    mid = 0.0
    for j in range(len(tb) - 1):
        tt = tb[j] + (gq + 1) * (tb[j + 1] - tb[j]) / 2
        xx = np.exp(tt)
        mid += float(np.sum(wq * f(xx) * xx) * (tb[j + 1] - tb[j]) / 2)

    def phi(xx):
        p = _parts(ad, xx)
        return p['Q'] * p['mp'] * (p['m'] / (xs - xx)) ** (be - 2)
    c, res = _endfit(phi, xe, xs, end_deg, nf, eta)
    end = float(d ** (be - 1) * sum(c[k] / (be - 1 + k) for k in range(len(c))))
    B = -(be - 1) * (fp0 + mid + end) / (3 * N)
    return dict(B=B, Bnat=B * xs ** (b.p3 - 2), fitres=fres, endres=res)
