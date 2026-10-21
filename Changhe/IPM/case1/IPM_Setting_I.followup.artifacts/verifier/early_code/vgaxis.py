"""verifier: axis jets of w by Green-function quadrature (second, independent inverse; written for this run).

For each angular mode n (psi = sum_n psi_n(t) sin(2 n theta), psi_n'' - 4 n^2 psi_n = -phi_n, phi_n = sin(2n theta)
coefficient of r^2 d_x rho):
    4 n psi_n = J_n + K_n,  J_n(t) = int_0^inf e^{-2nu} phi_n(t+u) du,  K_n(t) = int_0^inf e^{-2nu} phi_n(t-u) du.
t-derivatives commute with J and K, so psi_n^(j) = (J_n[phi_n^(j)] + K_n[phi_n^(j)])/(4n) with the exact t-jets phi_n^(j)
of the trial: no ODE recursion and no numerical differentiation.  For n <= nM (default nM = 1) the harmonic part is split
off exactly (for n >= 3 the moments M_n would multiply the angular FFT floor of phi_n at small r by e^{-2nt}: unusable):
    J_n = M_n e^{2nt} - L_n,  L_n(t) = int_{-inf}^t e^{2n(t-s)} phi_n(s) ds,  M_n = int e^{-2ns} phi_n ds,
and w = (c_l - M_1/2) x - sum_{2 <= n <= nM} (M_n/2) x^(2n-1) - rest/x,
    rest = sum_{n <= nM} (K_n - L_n)/2 + sum_{n > nM} (J_n + K_n)/2   (as t-jets, converted to x-jets).
Quadrature: sub-intervals of width <= hmax in t (aligned with the trial's knots and with the targets), phi_n^(j)
interpolated by Chebyshev polynomials on each sub-interval, exponential moments int_{-1}^1 e^{-mu(1+tau)} T_k(tau) dtau
by Gauss-Legendre, stable recursions (J backward, K forward, L forward with growth e^{2nh} only for n <= nM).
"""
import math
import numpy as np
import torch
from numpy.polynomial import legendre as Lg
import jets as J
from vres import analyse_sin
from vaxis import AxisData

DT = torch.float64


class GreenAxis(AxisData):
    def __init__(self, trial, c_l=None, K=6, q=20, xmin=1e-4, Nth=2048, nmax=None, dev='cuda', xstar=None,
                 t_lo=math.log(1e-8), t_hi=math.log(1e12), hmax=0.05, qf=14, nM=1, NG=128, chunk=128,
                 extra_breaks=(), xguess=8.6, t_s=math.log(30.0), n_rec=8):
        self.tr, self.K, self.q, self.Nth, self.dev, self.chunk = trial, K, q, Nth, dev, chunk
        self.c_l = trial.c_l if c_l is None else c_l
        self.nmax = Nth // 4 - 1 if nmax is None else nmax
        self.ns = np.arange(1, self.nmax + 1)
        self.nM, self.qf, self.NG, self.hmax, self.t_s, self.n_rec = nM, qf, NG, hmax, t_s, n_rec
        self.mode_mask = None
        kn = np.log(trial.interior_knots_r())
        self.base = np.unique(np.concatenate([[t_lo, t_hi], kn[(kn > t_lo) & (kn < t_hi)]]))
        tau = np.cos(np.pi * (np.arange(qf) + 0.5) / qf)                # Chebyshev nodes (first kind)
        self.tau = tau
        Tm = np.polynomial.chebyshev.chebvander(tau, qf - 1)             # (qf, qf)
        self.Vinv = torch.as_tensor(np.linalg.inv(Tm), dtype=DT, device=dev)
        g, wg = Lg.leggauss(NG)
        self.gl = torch.as_tensor(g, dtype=DT, device=dev)
        self.glw = torch.as_tensor(wg, dtype=DT, device=dev)
        self.Tg = torch.as_tensor(np.polynomial.chebyshev.chebvander(g, qf - 1), dtype=DT, device=dev)  # (NG, qf)
        self.info = {}
        if xstar is None:
            # pass 1: w on a short bracket around the guess, x* by interpolation of the jets
            xx = np.linspace(xguess * 0.995, xguess * 1.005, 9)
            w = self.jets_at(xx)['w']
            i = np.where(np.diff(np.sign(w[0])) != 0)[0][0]
            x0 = xx[i] - w[0, i] / w[1, i]
            for _ in range(3):
                wj = self.jets_at(np.array([x0]))['w']
                x0 = x0 - wj[0, 0] / wj[1, 0]
            xstar = x0
        self.xs = xstar
        ts = math.log(xstar)
        b = np.unique(np.concatenate([np.log(trial.interior_knots_r()), np.arange(math.log(xmin), ts, 0.25)]))
        bb = np.concatenate([[math.log(xmin)], b[(b > math.log(xmin)) & (b < ts)], list(extra_breaks), [ts]])
        self.b = np.unique(bb)
        self.P = len(self.b) - 1
        self.xg, self.wg = Lg.leggauss(q)
        self.t = np.concatenate([self.b[j] + (self.xg + 1) * (self.b[j + 1] - self.b[j]) / 2 for j in range(self.P)])
        self.x = np.exp(self.t)
        self.wj = self.jets_at(self.x)
        self.coef = {key: self._fit(arr) for key, arr in self.wj.items()}

    # ---- phi_n t-jets at arbitrary points: (Jmax+1, Npts, nmax), phi^(j) (not divided by j!)
    def phi_jets(self, tpts, Jmax):
        tr, dev = self.tr, self.dev
        th = (torch.arange(self.Nth, dtype=DT, device=dev) + 0.5) * 2 * math.pi / self.Nth
        an = tr.angular(th)
        co, si = torch.cos(th), torch.sin(th)
        out = []
        for i0 in range(0, len(tpts), self.chunk):
            r = torch.as_tensor(np.exp(tpts[i0:i0 + self.chunk]), dtype=DT, device=dev)
            rad = tr.radial(r, Jmax + 1)
            rho, rhot = tr.field(rad, an, Jmax + 1)
            rr = J.deriv(rho)
            invr = J.recip(J.var(r, Jmax))
            dx = co * rr - si * J.mul(rhot[:Jmax + 1], invr.unsqueeze(-1))
            dxt = J.r_to_t(dx, r)
            e2 = torch.stack([r ** 2 * 2.0 ** j / math.factorial(j) for j in range(Jmax + 1)])
            ph = J.mul(e2.unsqueeze(-1), dxt)
            Ph = torch.stack([math.factorial(j) * analyse_sin(ph[j], th, 2 * self.nmax)[0][:, 2:2 * self.nmax + 1:2]
                              for j in range(Jmax + 1)])
            out.append(Ph)
        return torch.cat(out, 1)

    def _moments(self, h, Fh, Jn):
        """DJ, DK (Jn, ns, nmax): int over each sub-interval of e^{-2n(s - left)} f, e^{-2n(right - s)} f."""
        dev = self.dev
        nn = torch.as_tensor(self.ns, dtype=DT, device=dev)
        ht = torch.as_tensor(h, dtype=DT, device=dev)
        mu = ht[:, None] * nn[None, :]                                   # (ns, nmax), lambda h / 2 = n h
        sgn = torch.as_tensor((-1.0) ** np.arange(self.qf), dtype=DT, device=dev)
        ns_ = len(h)
        DJ = torch.empty((Jn, ns_, self.nmax), dtype=DT, device=dev)
        DK = torch.empty_like(DJ)
        cs = 64
        for s0 in range(0, ns_, cs):
            ex = torch.exp(-mu[s0:s0 + cs, :, None] * (1 + self.gl[None, None, :]))   # (cs, nmax, NG)
            E = torch.einsum('snG,G,Gk->snk', ex, self.glw, self.Tg)                   # (cs, nmax, qf)
            fh = Fh[:, s0:s0 + cs]
            DJ[:, s0:s0 + cs] = torch.einsum('jsnk,snk->jsn', fh, E) * ht[None, s0:s0 + cs, None] / 2
            DK[:, s0:s0 + cs] = torch.einsum('jsnk,snk,k->jsn', fh, E, sgn) * ht[None, s0:s0 + cs, None] / 2
        return DJ, DK, torch.exp(-2 * mu)

    def _cheb(self, brk, Jmax):
        h = np.diff(brk)
        nodes = (brk[:-1, None] + (self.tau[None, :] + 1) * h[:, None] / 2).ravel()
        F = self.phi_jets(nodes, Jmax).reshape(Jmax + 1, len(h), self.qf, self.nmax)
        return h, torch.einsum('kq,jsqn->jsnk', self.Vinv, F)           # Chebyshev coefficients (Jmax+1, ns, nmax, qf)

    def green(self, ttar, Jmax):
        """J_n, K_n (n > nM) or K_n, L_n (n <= nM) of phi_n^(j) at the target points ttar (sorted unique inside
        (t_lo, t_s)); returns rest t-derivatives (Jmax+1, Ntar) and M_n (n <= nM).
        Far field: on [t_s, t_hi] only phi_n itself is used (the high t-jets of the trial at large r carry relative
        errors up to 1e-7); J_n[phi^(j)](t_s) follows from J_n[phi](t_s) and the local jets phi^(i)(t_s) by
        J[f'] = 2n J[f] - f (integration by parts), and M_n[phi^(j)] = (2n)^j M_n[phi] is not needed."""
        dev = self.dev
        ts_ = max(self.t_s, float(ttar.max()) + 0.25)
        allb = np.unique(np.concatenate([self.base, ttar, [ts_]]))
        bb = [allb[0]]
        for a, c in zip(allb[:-1], allb[1:]):
            m = int(math.ceil((c - a) / self.hmax - 1e-9))
            bb.extend(list(a + (c - a) * np.arange(1, m) / m))
            bb.append(c)
        brk = np.array(bb)
        i_s = int(np.argmin(np.abs(brk - ts_)))
        assert abs(brk[i_s] - ts_) < 1e-13
        bl, br = brk[:i_s + 1], brk[i_s:]
        nn = torch.as_tensor(self.ns, dtype=DT, device=dev)
        nM = self.nM
        # far part [t_s, t_hi]: phi only
        hr, Fhr = self._cheb(br, 0)
        DJr, _, decr = self._moments(hr, Fhr, 1)
        del Fhr
        Jfar = torch.zeros(self.nmax, dtype=DT, device=dev)
        for m in range(len(hr) - 1, -1, -1):
            Jfar = decr[m] * Jfar + DJr[0, m]
        btr = torch.as_tensor(br, dtype=DT, device=dev)
        Ifar = (torch.exp(-2 * nn[None, :nM] * btr[:-1, None]) * DJr[0, :, :nM]).sum(0)     # int_{t_s}^{t_hi} e^{-2ns} phi
        Fe = self.phi_jets(np.array([br[-1]]), 1)                        # right tail of M_n
        kk = Fe[1, 0, :nM] / Fe[0, 0, :nM]
        tail = torch.exp(-2 * nn[:nM] * btr[-1]) * Fe[0, 0, :nM] / (2 * nn[:nM] - kk)
        # jets of J at t_s by J[f'] = 2n J[f] - f
        ph_s = self.phi_jets(np.array([ts_]), Jmax)[:, 0, :]             # (Jmax+1, nmax)
        Js = torch.empty((Jmax + 1, self.nmax), dtype=DT, device=dev)
        Js[0] = Jfar
        for j in range(1, Jmax + 1):
            Js[j] = 2 * nn * Js[j - 1] - ph_s[j - 1]
        # near part [t_lo, t_s]: full jets
        hl, Fhl = self._cheb(bl, Jmax)
        DJ, DK, dec = self._moments(hl, Fhl, Jmax + 1)
        del Fhl
        ns_ = len(hl)
        Jv = torch.zeros((Jmax + 1, ns_ + 1, self.nmax), dtype=DT, device=dev)
        Kv = torch.zeros_like(Jv)
        Jv[:, ns_] = Js
        for m in range(ns_ - 1, -1, -1):
            Jv[:, m] = dec[m][None] * Jv[:, m + 1] + DJ[:, m]
        for m in range(ns_):
            Kv[:, m + 1] = dec[m][None] * Kv[:, m] + DK[:, m]
        # L_n and M_n for n <= nM: I(b_m) = int_{t_lo}^{b_m} e^{-2ns} phi ds
        bt = torch.as_tensor(bl, dtype=DT, device=dev)
        Iv = torch.zeros((Jmax + 1, ns_ + 1, nM), dtype=DT, device=dev)
        for m in range(ns_):
            Iv[:, m + 1] = Iv[:, m] + torch.exp(-2 * nn[None, :nM] * bt[m]) * DJ[:, m, :nM]
        M0 = Iv[0, -1] + Ifar + tail                                     # M_n[phi], n <= nM
        self.info['M'] = M0.cpu().numpy()
        self.info['M_tail'] = tail.cpu().numpy()
        self.info['t_s'] = ts_
        idx = np.searchsorted(bl, ttar)
        assert np.allclose(bl[idx], ttar, rtol=0, atol=1e-13)
        it = torch.as_tensor(idx, device=dev)
        Jt, Kt_ = Jv[:, it], Kv[:, it]                                   # (Jmax+1, Ntar, nmax)
        if self.n_rec > 0 and Jmax > 0:
            # J_n[phi^(j)] for n <= n_rec from J_n[phi] and the local jets by J[f'] = 2n J[f] - f: the direct quadrature
            # of phi^(j) over the trial's fine-knot region near P (r in [5, 10], where |phi_2^(5)| reaches 7e10)
            # cancels by up to 1e10 (measured: relative error 2e-9 in J_2^(5)); the recursion amplifies by at most
            # (2 n / kappa)^j, kappa the local t-frequency of phi
            nr = min(self.n_rec, self.nmax)
            pt = self.phi_jets(ttar, Jmax - 1)[:, :, :nr]                # (Jmax, Ntar, nr)
            Jr = torch.empty((Jmax + 1, len(ttar), nr), dtype=DT, device=dev)
            Jr[0] = Jt[0, :, :nr]
            for j in range(1, Jmax + 1):
                Jr[j] = 2 * nn[None, :nr] * Jr[j - 1] - pt[j - 1]
            self.info['Jrec_minus_direct'] = (Jr - Jt[:, :, :nr]).cpu().numpy()
            Jt = torch.cat([Jr, Jt[:, :, nr:]], -1)
        tt = torch.as_tensor(ttar, dtype=DT, device=dev)
        Lt = torch.exp(2 * nn[None, None, :nM] * tt[None, :, None]) * Iv[:, it]   # L_n = e^{2nt} I_n(t)
        parts = 0.5 * torch.cat([Kt_[:, :, :nM] - Lt, Jt[:, :, nM:] + Kt_[:, :, nM:]], -1)   # per mode
        if getattr(self, 'keep_parts', False):
            self.info['parts'] = parts.cpu().numpy()
        return parts.sum(-1), M0

    def jets_at(self, x):
        K = self.K
        x = np.atleast_1d(np.asarray(x, float))
        order = np.argsort(x)
        xs_ = x[order]
        ttar, inv = np.unique(np.log(xs_), return_inverse=True)
        rest, M = self.green(ttar, K)                                    # rest^(j)(t), (K+1, Ntar); M = M_n[phi_n]
        fac = torch.as_tensor([1.0 / math.factorial(j) for j in range(K + 1)], dtype=DT, device=self.dev)
        restT = rest * fac[:, None]                                      # Taylor coefficients in t
        r = torch.as_tensor(np.exp(ttar), dtype=DT, device=self.dev)
        Rr = J.t_to_r(restT, r)
        X = J.var(r, K)
        w = (self.c_l - M[0] / 2) * X - J.mul(Rr, J.recip(X))
        for n in range(2, self.nM + 1):
            w = w - (M[n - 1] / 2) * J.pw(X, float(2 * n - 1))     # (2n)^j M_n[phi] are the jets of M_n e^{2nt}
        w = w.cpu().numpy()[:, inv]
        wout = np.empty_like(w)
        wout[:, order] = w
        self.info['M_n'] = M.cpu().numpy()
        ax = self.tr.axis(torch.as_tensor(x, dtype=DT, device=self.dev), K)
        return dict(w=wout, g=ax['g'].cpu().numpy(), G3=ax['G3'].cpu().numpy())
