"""verifier: axis traces and the coefficient B_3 (written for this run).

Axis jets.  On theta = 0, psi_y(x,0) = P_1(x) = S_1(t)/x with S_1 = sum_n 2n psi_n(t), t = log x.  The t-jet of psi_n at a
point is built from psi_n and psi_n' (panel interpolation of the inverse) and the modal ODE
    psi_n^(j+2) = 4 n^2 psi_n^(j) - phi_n^(j),
with phi_n^(j) from the exact t-jets of r^2 d_x rho (jets of the trial, FFT in theta).  So no numerical differentiation
beyond the first t-derivative is used.  w = c_l x - P_1 as an x-jet of order K.

B_3 forms (R10 of the published report, with J the integrand of f.p. int_0^{x*} J dx):
  F1  w-only:  g_w from (log g_w)' = (w' - A)/w, g_w ~ x^2 at 0;  J = (1/(3N)) (a2/g^3)' m^(beta-1), m = |w|/g,
       a2 = (g' - w'')/2, all with g = g_w;  N = A^beta, A = 2 c_l - 1, beta = 2/A.
  F2a  original form with the true homogeneous solution from w:  H'/H = (1 - 3h)/w, h = 2 c_l - w', H ~ x^(p3);
       J = F/(w H), F = a2 g' + b3 g with the trial's g, a2 = (g' - w'')/2, b3 = -a2'/3.
  F2b  as F1 but with the trial's g (equivalently F/(w H_b) with H_b = N g^(3+beta) |w|^(-beta)).
  own  the trial's own coefficient T(-1) L^(-p3).
Natural units: B_nat = B_3 x*^(p3 - 2).
"""
import math
import numpy as np
import torch
from numpy.polynomial import legendre as Lg
from scipy.special import roots_jacobi
from scipy.optimize import brentq
import jets as J
from vinv import Panels
from vres import analyse_sin

DT = torch.float64


class AxisData:
    """Jets (in x) of w and of the trial's g, G_3 at Gauss-Legendre nodes of axis panels in t, with per-panel Legendre
    representations for interpolation."""

    def __init__(self, trial, evnpz, c_l=None, K=4, q=20, xmin=1e-4, Nth=2048, chunk=64, dev='cuda', xstar=None,
                 extra_breaks=(), mode1='integral', mode_tol=None):
        d = np.load(evnpz, allow_pickle=True)
        self.mode1 = mode1
        self.mode_tol = mode_tol
        if mode1 == 'integral':
            self._setup_mode1(d)
        self.tr = trial
        self.pan = Panels(d['breaks'], int(d['p']))
        self.psi = d['psi_modes']
        self.ns = d['ns']
        self.c_l = trial.c_l if c_l is None else c_l
        self.K, self.q, self.Nth, self.dev, self.chunk = K, q, Nth, dev, chunk
        nmax = len(self.ns)
        assert Nth // 2 - 2 >= 2 * nmax
        # x* from the stored nodal w (refined below with the jets)
        S1n = (2 * self.ns[None, :] * self.psi).sum(1)
        wn = self.c_l * self.pan.r - S1n / self.pan.r
        if xstar is None:
            i0 = [i for i in np.where(np.diff(np.sign(wn)) != 0)[0] if self.pan.r[i] > 1e-3][0]
            f = lambda x: self.c_l * x - self.pan.interp(S1n, [math.log(x)])[0] / x
            xstar = brentq(f, self.pan.r[i0], self.pan.r[i0 + 1], xtol=1e-15, rtol=1e-15)
            # refine with the w actually used (jets; mode 1 by its integral representation)
            fj = lambda x: float(self.jets_at(np.array([x]))['w'][0, 0])
            xstar = brentq(fj, xstar * (1 - 1e-6), xstar * (1 + 1e-6), xtol=1e-15, rtol=1e-15)
        self.xs = xstar
        ts = math.log(xstar)
        b = self.pan.b
        bb = np.concatenate([[math.log(xmin)], b[(b > math.log(xmin)) & (b < ts)], list(extra_breaks), [ts]])
        self.b = np.unique(bb)
        self.P = len(self.b) - 1
        self.xg, self.wg = Lg.leggauss(q)
        self.t = np.concatenate([self.b[j] + (self.xg + 1) * (self.b[j + 1] - self.b[j]) / 2 for j in range(self.P)])
        self.x = np.exp(self.t)
        self.wj = self.jets_at(self.x)                 # dict of numpy arrays (K+1, Nx) Taylor coefficients in x
        # Legendre coefficients per panel for every jet coefficient
        self.coef = {}
        for key, arr in self.wj.items():
            self.coef[key] = self._fit(arr)

    def _setup_mode1(self, d):
        """Mode 1 by its Green-function representation (no differentiation of the collocation solution):
        2 psi_1 = (M_1/2) e^{2t} - Lam(t), Lam = (e^{2t} I_-(t) - e^{-2t} I_+(t))/2, I_-+ = int_{-inf}^t e^{-+2s} phi_1 ds,
        M_1 = int e^{-2s} phi_1 ds = 2 c_int.  Lam' = e^{2t} I_- + e^{-2t} I_+, Lam'' = 2 phi_1 + 4 Lam."""
        pan = Panels(d['breaks'], int(d['p']))
        summ = __import__('json').loads(str(d['summary']))
        self.M1 = 2 * summ['c_int']
        phi1 = pan.r ** 2 * d['f_modes'][:, 0]
        p = pan.p
        self.m1 = {}
        for key, sg in [('Im', -2.0), ('Ip', 2.0)]:
            f = np.exp(sg * pan.t) * phi1
            base = f[0] / (4.0 + sg)                    # left tail, phi_1 ~ e^{4t}
            ints = []
            for j in range(pan.P):
                fl = f[j * p: j * p + p + 1]
                c = np.polynomial.chebyshev.chebfit(pan.x, fl, p)
                ci = np.polynomial.chebyshev.chebint(c, lbnd=-1) * pan.h[j] / 2
                ints.append((base, ci))
                base = base + np.polynomial.chebyshev.chebval(1.0, ci)
            self.m1[key] = ints
        self.pan1 = pan

    def _mode1_cum(self, key, t):
        _, j = self.pan1.locate(t)
        out = np.empty(len(t))
        for i, (tt, jj) in enumerate(zip(t, j)):
            base, ci = self.m1[key][jj]
            xi = 2 * (tt - self.pan1.b[jj]) / self.pan1.h[jj] - 1
            out[i] = base + np.polynomial.chebyshev.chebval(xi, ci)
        return out

    def _fit(self, arr):
        """arr (..., P*q) -> Legendre coefficients (P, ..., q) per panel (exact interpolation on the GL nodes)."""
        q = self.q
        V = Lg.legvander(self.xg, q - 1)
        Vi = np.linalg.inv(V)
        out = []
        for j in range(self.P):
            a = arr[..., j * q:(j + 1) * q]
            out.append(np.einsum('kq,...q->...k', Vi, a))
        return np.array(out)

    def locate(self, t):
        t = np.atleast_1d(t)
        j = np.clip(np.searchsorted(self.b, t, side='right') - 1, 0, self.P - 1)
        xi = 2 * (t - self.b[j]) / (self.b[j + 1] - self.b[j]) - 1
        return j, xi

    def interp(self, key, x):
        """Interpolate the stored jets at arbitrary x in (xmin, x*]: (K+1, len(x))."""
        t = np.log(np.atleast_1d(x))
        j, xi = self.locate(t)
        C = self.coef[key]                               # (P, K+1, q)
        out = np.empty((C.shape[1], len(t)))
        for i in range(len(t)):
            out[:, i] = Lg.legval(xi[i], C[j[i]].T)
        return out

    def jets_at(self, x):
        """w, g, G3 x-jets (Taylor coefficients) of order K at the points x (numpy)."""
        tr, K, dev = self.tr, self.K, self.dev
        Kt = K                                           # t-jet order for S1
        th = (torch.arange(self.Nth, dtype=DT, device=dev) + 0.5) * 2 * math.pi / self.Nth
        an = tr.angular(th)
        co, si = torch.cos(th), torch.sin(th)
        nmax = len(self.ns)
        nn = torch.as_tensor(self.ns, dtype=DT, device=dev)
        out_w, out_S = [], []
        for i0 in range(0, len(x), self.chunk):
            xc = x[i0:i0 + self.chunk]
            r = torch.as_tensor(xc, dtype=DT, device=dev)
            rad = tr.radial(r, Kt - 1)                   # phi jets needed to order Kt-2; rho to order Kt-1
            rho, rhot = tr.field(rad, an, Kt - 1)        # (Kt, Nr, Nth)
            rr = J.deriv(rho)                            # order Kt-2
            invr = J.recip(J.var(r, Kt - 2))
            dx = co * rr - si * J.mul(rhot[:Kt - 1], invr.unsqueeze(-1))
            dxt = J.r_to_t(dx, r)                        # t-jet, order Kt-2
            e2 = torch.zeros((Kt - 1, len(xc)), dtype=DT, device=dev)
            for j in range(Kt - 1):
                e2[j] = r ** 2 * 2.0 ** j / math.factorial(j)
            ph = J.mul(e2.unsqueeze(-1), dxt)            # t-jet of r^2 d_x rho
            Ph = torch.stack([analyse_sin(ph[j], th, 2 * nmax)[0][:, 2:2 * nmax + 1:2] for j in range(Kt - 1)])
            # psi t-jets
            tq = np.log(xc)
            p0 = torch.as_tensor(self.pan.interp(self.psi, tq, 0), device=dev)
            p1 = torch.as_tensor(self.pan.interp(self.psi, tq, 1), device=dev)
            Ps = torch.zeros((Kt + 1, len(xc), nmax), dtype=DT, device=dev)
            Ps[0], Ps[1] = p0, p1
            if self.mode_tol is not None:
                # modes whose source and ODE terms are both at the FFT / collocation floor are numerically zero; keeping
                # them injects noise amplified by 4 n^2 in the higher t-derivatives (origin layer)
                # keep n <= n_sig(x) + 2, n_sig = last mode with |phi_n| >= mode_tol max_m |phi_m| (geometric decay in n
                # in the origin layer makes the dropped modes negligible; a per-element floor test toggles and adds noise)
                fl = self.mode_tol * Ph[0].abs().max(1, keepdim=True).values
                idx = torch.arange(nmax, device=dev)[None, :]
                nsig = torch.where(Ph[0].abs() >= fl, idx, torch.zeros_like(idx)).max(1, keepdim=True).values
                live = (idx <= nsig + 2).to(DT)
                Ph = Ph * live[None]
                Ps = Ps * live[None]
            for j in range(Kt - 1):
                Ps[j + 2] = (4 * nn ** 2 * Ps[j] - Ph[j]) / ((j + 1) * (j + 2))
            if getattr(self, 'mode_mask', None) is not None:     # diagnostics only: drop modes consistently
                Ps = Ps * torch.as_tensor(self.mode_mask, dtype=DT, device=dev)[None, None, :]
            if self.mode1 == 'integral':
                # S1 = (M_1/2) x^2 + rest; rest = sum_{n>=2} 2n psi_n - Lam (t-jets), w = (c_l - M_1/2) x - rest/x
                Im = torch.as_tensor(self._mode1_cum('Im', tq), device=dev)
                Ip = torch.as_tensor(self._mode1_cum('Ip', tq), device=dev)
                e2t, em2t = r ** 2, r ** -2
                ph1 = [math.factorial(j) * Ph[j][:, 0] for j in range(Kt - 1)]    # phi_1^(j)
                Ld = [0.5 * (e2t * Im - em2t * Ip), e2t * Im + em2t * Ip]
                for j in range(2, Kt + 1):
                    Ld.append(2 * ph1[j - 2] + 4 * Ld[j - 2])
                Lt = torch.stack([Ld[j] / math.factorial(j) for j in range(Kt + 1)])
                rest = (2 * nn[1:] * Ps[:, :, 1:]).sum(-1) - Lt
                Rr = J.t_to_r(rest, r)
                P1r = J.mul(Rr, J.recip(J.var(r, Kt)))
                w = (self.c_l - self.M1 / 2) * J.var(r, Kt) - P1r
            else:
                S1t = (2 * nn * Ps).sum(-1)              # (Kt+1, Nx)
                S1r = J.t_to_r(S1t, r)
                P1 = J.mul(S1r, J.recip(J.var(r, Kt)))
                w = self.c_l * J.var(r, Kt) - P1
            out_w.append(w.cpu().numpy())
        w = np.concatenate(out_w, axis=1)
        ax = tr.axis(torch.as_tensor(x, dtype=DT, device=dev), K)
        return dict(w=w, g=ax['g'].cpu().numpy(), G3=ax['G3'].cpu().numpy())


# ---------------- jet helpers in numpy (Taylor coefficients, shape (K+1, n)) ----------------
def tj(a):
    return torch.as_tensor(a, dtype=DT)


def forms_at(ad, x, c_l, which):
    """Integrand pieces at points x for the forms; returns dict of numpy arrays."""
    K = ad.K
    W = tj(ad.interp('w', x))
    if c_l != ad.c_l:                                 # w = c_l x - P_1: shift with c_l (x* is then not a zero of w)
        W[0] += (c_l - ad.c_l) * tj(x)
        W[1] += (c_l - ad.c_l)
    G = tj(ad.interp('g', x))
    G3 = tj(ad.interp('G3', x))
    A = 2 * c_l - 1
    be = 2 / A
    N = A ** be
    xx = J.var(tj(x), K)
    wp = J.deriv(W)                                   # order K-1
    Kp = K - 1
    one = J.const(torch.ones(len(x), dtype=DT), Kp)
    res = {}
    # e = (w'-A)/w - 2/x  and its jet (order K-1)
    ratio = J.mul(wp - A * one, J.recip(W[:Kp + 1]))
    res['e'] = (ratio - 2 * J.recip(xx[:Kp + 1]))[0].numpy()
    h = 2 * c_l * one - wp
    ratioH = J.mul(one - 3 * h, J.recip(W[:Kp + 1]))
    res['eH'] = (ratioH - (6 + be) * J.recip(xx[:Kp + 1]))[0].numpy()
    res['ratio'] = ratio
    res['ratioH'] = ratioH
    res['W'] = W
    res['G'] = G
    res['G3'] = G3
    return res


class B3:
    def __init__(self, ad, c_l=None):
        self.ad = ad
        self.c_l = ad.c_l if c_l is None else c_l
        self.A = 2 * self.c_l - 1
        self.be = 2 / self.A
        self.p3 = 6 + self.be
        self.N = self.A ** self.be
        # cumulative integrals of e (log g_w / x^2) and eH (log H / x^p3) over the axis panels
        ad = self.ad
        x = ad.x
        pc = forms_at(ad, x, self.c_l, None)
        e, eH = pc['e'], pc['eH']
        eT = self._eT(pc)
        self.e0 = (e[0] / x[0], eH[0] / x[0])        # leading odd coefficients e ~ e1 x at 0 (assumed)
        self.cum = {}
        # 'eH' (log H_3/x^p3 by integrating (1-3h)/w) is kept for the record only: (1-3h)/w has a pole at x*, which the
        # panel interpolation cannot integrate (error 2e-3 in H at x = 8 on exact R12 data).  F2a uses 'eT':
        # (log H_3/H_b)' = -(3+beta) T_1/(g w), smooth at x* when h(P) = 1 and at 0 when w'(0) = -A.
        for key, val in [('e', e), ('eH', eH), ('eT', eT)]:
            f = val * x                                # d/dt integrand: int e dx = int e x dt
            C = ad._fit(f)                             # (P, q)
            tot = []
            xm = math.exp(ad.b[0])
            base = (val[0] / x[0]) * xm ** 2 / 2.0     # int_0^{xmin} e1 s ds, e ~ e1 s assumed
            ints = []
            for j in range(ad.P):
                hj = (ad.b[j + 1] - ad.b[j]) / 2
                ci = Lg.legint(C[j], lbnd=-1) * hj
                ints.append((base, ci))
                base = base + Lg.legval(1.0, ci)
            self.cum[key] = ints

    def _eT(self, pc):
        W, G = pc['W'], pc['G']
        gp = J.deriv(G)[0]
        h = 2 * self.c_l - J.deriv(W)[0]
        T1 = W[0] * gp + (h - 1) * G[0]
        return (-(3 + self.be) * T1 / (G[0] * W[0])).numpy()

    def cumval(self, key, x):
        t = np.log(np.atleast_1d(x))
        j, xi = self.ad.locate(t)
        ints = self.cum[key]
        return np.array([ints[jj][0] + Lg.legval(xx, ints[jj][1]) for jj, xx in zip(j, xi)])

    def integrands(self, x, gsrc='w'):
        """J for F1 (gsrc='w'), F2b (gsrc='trial'), and F2a, at points x; returns dict."""
        ad, K = self.ad, self.ad.K
        pc = forms_at(ad, x, self.c_l, None)
        W, G = pc['W'], pc['G']
        Kp = K - 1
        A, be, N = self.A, self.be, self.N
        xt = tj(x)
        out = {}
        # g_w jet from log g_w = log x^2 + cum e, (log g)' = ratio
        lg = torch.zeros((Kp + 1, len(x)), dtype=DT)
        lg[0] = torch.as_tensor(2 * np.log(x) + self.cumval('e', x))
        for j in range(1, Kp + 1):
            lg[j] = pc['ratio'][j - 1] / j
        gw = J.exp(lg)
        for name, g in [('F1', gw), ('F2b', G[:Kp + 1])]:
            gp = J.deriv(g)                                  # order Kp-1
            wpp = J.deriv(J.deriv(W))[:Kp]                   # order K-2 = Kp-1
            a2 = 0.5 * (gp - wpp)
            g3 = J.pw(g[:Kp], -3.0)
            q = J.mul(a2, g3)
            dq = J.deriv(q)[0]
            m = -W[0] / g[0]
            out[name] = (dq * m ** (be - 1) / (3 * N)).numpy()
            out[name + '_m'] = m.numpy()
        # F2a: true homogeneous solution from w; F with trial g
        g = G[:Kp + 1]
        gp = J.deriv(g)
        wpp = J.deriv(J.deriv(W))[:Kp]
        a2 = 0.5 * (gp - wpp)
        b3 = -J.deriv(a2)[0] / 3
        F = a2[0] * gp[0] + b3 * g[0]
        Hb0 = N * g[0].numpy() ** (3 + be) * np.abs(W[0].numpy()) ** (-be)
        out['F2a'] = (F / W[0]).numpy() / (Hb0 * np.exp(self.cumval('eT', x)))
        lH = self.p3 * np.log(x) + self.cumval('eH', x)
        out['F2a_ode'] = (F / W[0]).numpy() * np.exp(-lH)           # superseded (pole of (1-3h)/w at x*)
        # defects of the trial on the axis: T1 = w g' + (h-1) g, T3 = w G3' + (3h-1) G3 + a2 g' + b3 g
        h = 2 * self.c_l - J.deriv(W)[0]
        G3 = pc['G3']
        out['T1'] = (W[0] * gp[0] + (h - 1) * g[0]).numpy()
        out['T3'] = (W[0] * J.deriv(G3)[0] + (3 * h - 1) * G3[0] + F).numpy()
        out['g'] = g[0].numpy()
        out['gw'] = gw[0].numpy()
        out['G3'] = G3[0].numpy()
        out['w'] = W[0].numpy()
        Hb = N * g[0].numpy() ** (3 + be) * np.abs(W[0].numpy()) ** (-be)
        out['Hb'] = Hb
        out['ident'] = (out['T3'] - (3 + be) * (out['G3'] / out['g']) * out['T1']) / (out['w'] * Hb)
        return out

    def fp(self, key, xlo, xc, deg=12, nfit=400, nend=60, xe_panels=1):
        """f.p. int_0^{x*} J_key dx with: [0, xc] even-polynomial fit of x^(5+beta) J on [xlo, xc] (Chebyshev in s = x^2,
        degree deg), exact finite part; [xc, x_e] Gauss-Legendre on the axis panels (split at xc); [x_e, x*] Gauss-Jacobi
        in t with weight (t* - t)^(beta-1) on the last xe_panels axis panels."""
        ad, be = self.ad, self.be
        # fit in sigma = s / xc^2 on [sig_lo, 1] (Chebyshev nodes), then monomials in sigma
        sl = (xlo / xc) ** 2
        sg = np.cos(np.pi * (np.arange(nfit) + 0.5) / nfit)
        sg = sl + (1 - sl) * (sg + 1) / 2
        xf = xc * np.sqrt(sg)
        Q = self.integrands(xf)[key] * xf ** (5 + be)
        ch = np.polynomial.chebyshev.Chebyshev.fit(sg, Q, deg, domain=[sl, 1.0])
        fitres = float(np.abs(ch(sg) - Q).max() / np.abs(Q).max())
        mono = ch.convert(kind=np.polynomial.Polynomial, domain=[-1, 1], window=[-1, 1]).coef  # in sigma
        # f.p. int_0^{xc} x^(-5-beta) sum_k chat_k (x/xc)^(2k) dx = xc^(-4-beta) sum_k chat_k / (2k - 4 - beta)
        fp0 = float(xc ** (-4 - be) * sum(mono[k] / (2 * k - 4 - be) for k in range(len(mono))))
        # middle
        tc = math.log(xc)
        b = ad.b
        jlast = ad.P - xe_panels
        brk = np.concatenate([[tc], b[(b > tc) & (b < b[jlast])], [b[jlast]]])
        mid = 0.0
        gq, wq = Lg.leggauss(ad.q + 10)
        for j in range(len(brk) - 1):
            tt = brk[j] + (gq + 1) * (brk[j + 1] - brk[j]) / 2
            xx = np.exp(tt)
            mid += float(np.sum(wq * self.integrands(xx)[key] * xx) * (brk[j + 1] - brk[j]) / 2)
        # end: Gauss-Jacobi in t on [b[jlast], t*] with weight (t* - t)^(beta - 1)
        ts = b[-1]
        ta = b[jlast]
        tj_, wj_ = roots_jacobi(nend, be - 1, 0.0)          # weight (1-u)^(be-1) on [-1,1]
        tt = ta + (tj_ + 1) * (ts - ta) / 2
        xx = np.exp(tt)
        val = self.integrands(xx)[key] * xx * (ts - tt) ** (1 - be)
        endp = float(np.sum(wj_ * val) * ((ts - ta) / 2) ** be)
        B = fp0 + mid + endp
        return dict(B=B, Bnat=B * self.ad.xs ** (self.p3 - 2), fp0=fp0, mid=mid, endp=endp, fitres=fitres,
                    k0=float(mono[0]), coef_sigma=mono)
