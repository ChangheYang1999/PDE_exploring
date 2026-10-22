"""Desingularized far-field evaluation of the A1 residual for generating-function states (outer basis only).
For x = l xh, eta = se l^(1/m) eh, sigma = l^(-1/beta), m = beta/(beta - 2), the outer basis of model.py (m = 3) and model_fb.py is
  G(x, eta) = l^2 se g(xh, eh, sigma),  g = xh eh Eh^(1/beta) P(tau(t), w),  Eh = xh^2 + (sigma^q + eh^(2M))^(m/M),  q = 2M(beta - 2),
  t = sigma Eh^(-1/(2 beta)),  w = eh^2 Eh^(-1/m)
identically in l. For f(x, eta) = l^k F(xh, eh, sigma) identically in l, d/dl = 0 at fixed (x, eta) gives
  (beta xh d_xh + (beta - 2) eh d_eh + sigma d_sigma) F = beta k F, hence D f = l^k (beta k - sigma d_sigma) F for the weighted Euler
  operator D = beta x d_x + (beta - 2) eta d_eta. For G (k = 2): Psi = (D - 2 beta) G = -l^2 se sigma g_sigma; for k = 0 (Omega = sigma om)
  D = -sigma d_sigma. With phi = -se g_sigma, ghat = g_xhxh / g_xheh, Dxh = d_xh - ghat d_eh, Dyh = (se g_xheh)^(-1) d_eh (at fixed sigma), om = -(Dxh^2 + Dyh^2) phi:
  Psi = l^2 sigma phi, Omega = sigma om, U = l sigma (-Dyh phi, Dxh phi), X = l xh, Y = l se g_xh, Theta_x = -sigma^2 a0 se ghat,
  R  = sigma^2 [ -Dyh phi om_xh - om_sigma + a0 se ghat ]                       (= W.grad Omega + Omega - Theta_x),
  N2 = sigma^2 [ |Dyh phi Dxh om| + |Dxh phi Dyh om| + |om_sigma + (Dyh phi ghat + Dxh phi / (se g_xheh)) om_eh| + |a0 se ghat| ],
  N  = sigma [ |(beta xh - sigma Dyh phi) Dxh om| + |(beta se g_xh + sigma Dxh phi) Dyh om| + |om| + sigma |a0 se ghat| ].
(beta X.grad Omega = D Omega - (U.grad eta) Omega_eta uses W.grad eta = (beta - 2) eta, which the chart satisfies identically.)
The forced subtractions of the large-radius terms (the O(l^2) terms of Psi, the leading orders of R and of the grouped term of N2) are
done analytically; the brackets remain signed sums and the residual bracket itself cancels when the profile nearly solves (P1).
Validity (external audit): the brackets are bounded as sigma -> 0 on compact interior sets with a positive lower bound on g_xheh if
q = 1 or q >= 2 (a generic sigma^q term gives om_sigma ~ sigma^(q - 2) for 1 < q < 2, and worse for q < 1); here q = 6 (beta - 2),
so q >= 2 for beta >= 7/3. For beta = 3, M = 3, Eh = xh^2 + eh^6 + sigma^6 and the jets are regular away from Eh = 0. On the symmetry
axes xh = 0, eh = 0 every summand of both normalizers vanishes (0/0: limits there are separate statements); the CLI keeps
S in [1e-8, 1 - 1e-8] and prints min g_xheh over the points. At sigma = 0 (beta = 3, q integer) R/N2 is the far limit C/N20 of
farrows.py (as a continuous extension). For q non-integer sigma > 0 is required.
tau = 1 - log((1 - t)(e^alpha - 1) + 1)/alpha is evaluated as -log1p(-(1 - e^(-alpha)) t)/alpha (no cancellation at small t).
Points: (t, S) with t = sigma (the radial variable of the solver grid, E = t^(-2 beta)) and S = w / wmax(t), via Eh = 1:
  eh = sqrt(w), xh = sqrt(1 - (t^q + w^M)^(m/M)), wmax = (1 - t^q)^(1/M) (the same S as ts_to_xeta_fb and model.ts_to_xeta).
Core patches carry exp(-(x^2 + eta^2)/Lc^2); they are dropped and points with (x^2 + eta^2)/Lc^2 < 700 are refused.
Usage: python3 desing.py state.npz [t1,t2,...|rand:N:tlo:thi] [--S s1,s2,..|--NS n] [--check] [--seed k]
  --check: also evaluate the same points with model.fields (binary64, direct) and print both."""
import sys, math, numpy as np, torch
torch.set_num_threads(1)
from jets3 import Jet3, DT


class Desing:
    def __init__(self, J, Kw, c, a0, beta=3.0, M=3, alpha=3.0, se=1.0, gam=0.0):
        self.J, self.Kw, self.a0 = J, Kw, float(a0)
        self.beta, self.M, self.alpha, self.se, self.gam = float(beta), int(M), float(alpha), float(se), float(gam)
        self.m = self.beta / (self.beta - 2); self.q = 2 * self.M * (self.beta - 2)
        self.qint = abs(self.q - round(self.q)) < 1e-12; self.mM1 = abs(self.m / self.M - 1) < 1e-12
        self.cm = torch.as_tensor(np.asarray(c)[:(J + 1) * (Kw + 1)], dtype=DT).reshape(J + 1, Kw + 1)

    def points(self, t, S):
        """section points with Eh = 1 for given t (= sigma) and S = w/wmax; returns xh, eh, sigma (numpy) and wmax"""
        t = np.asarray(t, float); S = np.asarray(S, float)
        # Eh = 1: xh^2 = 1 - (t^q + w^M)^(m/M) >= 0  <=>  w <= (1 - t^q)^(1/M)
        wmax = np.maximum(1 - t ** self.q, 0) ** (1.0 / self.M)
        w = S * wmax
        xh = np.sqrt(np.maximum(1 - (t ** self.q + w ** self.M) ** (self.m / self.M), 0))
        return xh, np.sqrt(w), t, wmax

    def set_beta(self, beta):
        self.beta = float(beta); self.m = self.beta / (self.beta - 2); self.q = 2 * self.M * (self.beta - 2)
        self.qint = abs(self.q - round(self.q)) < 1e-12; self.mM1 = abs(self.m / self.M - 1) < 1e-12

    def _parts(self, xh, eh, sg, P=4, Q=2):
        """prefactor jet and the Chebyshev jets T_n(2 tau - 1), T_k(2 w - 1) at the scaled points"""
        X = Jet3.var(torch.as_tensor(xh, dtype=DT), 0, P, Q); H = Jet3.var(torch.as_tensor(eh, dtype=DT), 1, P, Q)
        s = Jet3.var(torch.as_tensor(sg, dtype=DT), 2, P, Q)
        if not self.qint and (np.asarray(sg) <= 0).any(): raise SystemExit('non-integer q = %g needs sigma > 0' % self.q)
        inner = (s.ipow(int(round(self.q))) if self.qint else s.pow(self.q)) + H.ipow(2 * self.M)
        Eh = X * X + (inner if self.mM1 else inner.pow(self.m / self.M))
        pre = X * H * Eh.pow(1.0 / self.beta)
        t = s * Eh.pow(-1.0 / (2 * self.beta))
        if self.alpha > 0:
            dA = -math.expm1(-self.alpha)
            Lg = (1 - t * dA).log(); Lg.c[0] = torch.log1p(-dA * t.val())
            t = Lg * (-1.0 / self.alpha)
        w = H * H * Eh.pow(-1.0 / self.m)
        if self.gam > 0:
            w = (w * (math.exp(self.gam) - 1.0) + 1).log() * (1.0 / self.gam)
        N = X.c.shape[1]
        def cheb(z, K):
            u = 2 * z - 1
            T = [Jet3.const(1.0, P, Q, N), u]
            for k in range(2, K + 1): T.append(2 * u * T[-1] - T[-2])
            return T[:K + 1]
        return pre, cheb(t, self.J), torch.stack([T.c for T in cheb(w, self.Kw)], 0)

    def basis_matrix(self, xh, eh, sg, P=4, Q=2):
        """tensor (n3, N, (J+1)(Kw+1)): jet coefficients of the outer basis functions g_nk = xh eh Eh^(1/beta) T_n T_k (row-major (n, k)),
        so that the jet of g is basis_matrix @ c (G = l^2 se g)"""
        pre, Tt, Tw = self._parts(xh, eh, sg, P, Q)
        from jets3 import _multab
        ko, ka, kb = _multab(P, Q)
        cols = []
        for n in range(self.J + 1):
            a = (pre * Tt[n]).c
            cols.append(torch.zeros_like(Tw).index_add(1, ko, a[ka][None] * Tw[:, kb]))     # (K+1, n3, N)
        return torch.stack(cols, 0).reshape((self.J + 1) * (self.Kw + 1), -1, Tw.shape[2]).permute(1, 2, 0)

    def g_jet(self, xh, eh, sg, P=4, Q=2, c=None):
        pre, Tt, Tw = self._parts(xh, eh, sg, P, Q)
        cm = self.cm if c is None else torch.as_tensor(c[:(self.J + 1) * (self.Kw + 1)], dtype=DT).reshape(self.J + 1, self.Kw + 1)
        Qn = torch.einsum('nk,kpi->npi', cm, Tw)
        S_ = None
        for n in range(self.J + 1):
            term = Tt[n] * Jet3(Qn[n], P, Q)
            S_ = term if S_ is None else S_ + term
        return pre * S_

    def evaluate(self, xh, eh, sg):
        return self.fields3(self.g_jet(xh, eh, sg).c, xh, sg, self.a0)

    def fields3(self, Gc, xh, sg, a0, P=4, Q=2):
        """R/sigma^2 (Rb), N2/sigma^2 (N2b), N/sigma (Nb) and the ratios from the jet coefficients Gc (n3, N) of g (torch,
        differentiable in Gc and a0; a0 may be a tensor)"""
        g = Jet3(Gc, P, Q)
        se, b = self.se, self.beta
        sv = torch.as_tensor(sg, dtype=DT)
        gx = g.dx(); gxx = gx.dx(); gxe = gx.de()
        ghat = gxx * gxe.pow(-1.0)
        iA = (gxe * se).pow(-1.0)
        Dx = lambda f: f.dx() - ghat * f.de()
        Dy = lambda f: iA * f.de()
        phi = g.ds() * (-se)
        om = -(Dx(Dx(phi)) + Dy(Dy(phi)))
        Dyphi = Dy(phi).val(); Dxphi = Dx(phi).val()
        omx = om.dx().val(); ome = om.de().val(); oms = om.ds().val(); omv = om.val()
        gh = ghat.val(); gxev = gxe.val(); gxv = gx.val()
        Dxom = omx - gh * ome; Dyom = ome / (se * gxev)
        Rb = -Dyphi * omx - oms + a0 * se * gh
        N2b = (Dyphi * Dxom).abs() + (Dxphi * Dyom).abs() + (oms + (Dyphi * gh + Dxphi / (se * gxev)) * ome).abs() + (a0 * se * gh).abs()
        Nb = ((b * torch.as_tensor(xh, dtype=DT) - sv * Dyphi) * Dxom).abs() + ((b * se * gxv + sv * Dxphi) * Dyom).abs() + omv.abs() \
            + sv * (a0 * se * gh).abs()
        lam = sv ** (-b)
        return dict(Rb=Rb, N2b=N2b, Nb=Nb, rN2=Rb / N2b, rN=sv * Rb / Nb, A=gxev, xh=xh, yh=se * gxv,
                    X=torch.as_tensor(xh, dtype=DT) * lam, Y=se * gxv * lam, terms=[-Dyphi * omx, -oms, a0 * se * gh])


def load(path):
    d = np.load(path)
    J, Kw = int(d['J']), int(d['Kw'])
    beta = float(d['beta']) if 'beta' in d.files else 3.0
    if 'm' in d.files and int(d['m']) != 3 and 'beta' not in d.files: raise SystemExit('model.py state with m != 3')
    M = int(d['M']) if 'M' in d.files else 3
    se = float(d['se']) if 'se' in d.files else 1.0; gam = float(d['gam']) if 'gam' in d.files else 0.0
    core = d['core'] if 'core' in d.files else None
    return d, Desing(J, Kw, d['c'], float(d['a0']), beta=beta, M=M, alpha=float(d['alpha']), se=se, gam=gam), core


def direct(d, x, eta):
    """binary64 direct evaluation with model.fields (core-aware), returns R/N2 and R/N"""
    from model import fields
    from model_core_fb import ModelCoreFB
    from model_fb import ModelFB
    J, Kw = int(d['J']), int(d['Kw']); beta = float(d['beta']) if 'beta' in d.files else 3.0; M = int(d['M']) if 'M' in d.files else 3
    se = float(d['se']) if 'se' in d.files else 1.0; gam = float(d['gam']) if 'gam' in d.files else 0.0
    if 'core' in d.files:
        mod = ModelCoreFB(J, Kw, d['core'], beta=beta, M=M, alpha=float(d['alpha']), se=se, gam=gam); c = np.concatenate([d['c'], d['cc']])
    else:
        mod = ModelFB(J, Kw, beta=beta, M=M, alpha=float(d['alpha']), se=se, gam=gam); c = d['c']
    x = torch.as_tensor(x, dtype=DT); eta = torch.as_tensor(eta, dtype=DT)
    Gc = mod.g_jet(torch.as_tensor(c, dtype=DT), x, eta)
    F = fields(Gc, x, eta, float(d['a0']), beta)
    N2 = (F['U1'] * F['Ox']).abs() + (F['U2'] * F['Oy']).abs() + (beta * (x * F['Ox'] + F['y'] * F['Oy']) + F['Om']).abs() + F['Thx'].abs()
    return (F['R'] / N2).numpy(), (F['R'] / F['N']).numpy()


if __name__ == '__main__':
    d, ds, core = load(sys.argv[1])
    arg = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith('--') else '0,1e-4,1e-3,3e-3,1e-2,3e-2,0.1'
    seed = int(sys.argv[sys.argv.index('--seed') + 1]) if '--seed' in sys.argv else 0
    rng = np.random.default_rng(seed)
    if arg.startswith('rand:'):
        _, n_, lo, hi = arg.split(':'); n_ = int(n_); lo, hi = float(lo), float(hi)
        ts = np.exp(rng.uniform(np.log(lo), np.log(hi), n_)) if lo > 0 else rng.uniform(lo, hi, n_)
        Ss = rng.uniform(0, 1, n_) ** 1.0
        T = ts; S = Ss
    else:
        ts = np.array([float(v) for v in arg.split(',')])
        if '--S' in sys.argv: Ss = np.array([float(v) for v in sys.argv[sys.argv.index('--S') + 1].split(',')])
        else:
            nS = int(sys.argv[sys.argv.index('--NS') + 1]) if '--NS' in sys.argv else 13
            Ss = np.concatenate([[1e-8, 1e-4, 1e-2], 0.5 * (1 - np.cos(np.pi * (np.arange(nS) + 0.5) / nS)), [1 - 1e-4, 1 - 1e-8]])
        T, S = [a.ravel() for a in np.meshgrid(ts, Ss, indexing='ij')]
    xh, eh, sg, wmax = ds.points(T, S)
    with np.errstate(divide='ignore'):
        lam = np.where(sg > 0, sg ** (-ds.beta), np.inf)
    if core is not None:
        Lc = float(np.max(np.asarray(core).reshape(-1, 4)[:, 3]))
        with np.errstate(over='ignore'):
            rr = (xh * lam) ** 2 + (ds.se * eh * lam ** (1 / ds.m)) ** 2
        if (rr / Lc ** 2 < 700).any(): raise SystemExit('points too close to the core: min (x^2+eta^2)/Lc^2 = %g' % (rr / Lc ** 2).min())
    ev = ds.evaluate(xh, eh, sg)
    rN2 = ev['rN2'].numpy(); rN = ev['rN'].numpy()
    if '--check' in sys.argv:
        x = xh * lam; eta = ds.se * eh * lam ** (1 / ds.m)
        dN2, dN = direct(d, x, eta)
    print('state %s  beta %.6f a0 %.6f  J %d Kw %d' % (sys.argv[1], ds.beta, ds.a0, ds.J, ds.Kw))
    print('     t          S          r          R/N2 (desing)   R/N (desing)' + ('    R/N2 (direct)   R/N (direct)' if '--check' in sys.argv else ''))
    for i in range(len(T)):
        r = math.hypot(float(ev['X'][i]), float(ev['Y'][i])) if sg[i] > 0 else float('inf')
        line = '  %.3e  %.6f  %.3e  %+.6e  %+.6e' % (T[i], S[i], r, rN2[i], rN[i])
        if '--check' in sys.argv: line += '  %+.6e  %+.6e' % (dN2[i], dN[i])
        if not arg.startswith('rand:') or i < 40: print(line)
    print('max |R/N2| %.4e  max |R/N| %.4e over %d points; min g_xheh %.4e' % (np.abs(rN2).max(), np.abs(rN).max(), len(T), float(ev['A'].min())))
