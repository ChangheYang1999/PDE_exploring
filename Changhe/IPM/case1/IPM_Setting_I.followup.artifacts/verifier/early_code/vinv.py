"""verifier: independent full-plane inverse by spectral-element collocation (written for this run).

Parity class: d_x rho = sum_{n>=1} f_n(r) sin(2 n theta), psi = sum_{n>=1} psi_n(r) sin(2 n theta).  With t = log r and
phi_n = r^2 f_n, -Laplace psi = d_x rho is, mode by mode,
    psi_n'' - 4 n^2 psi_n = -phi_n         (' = d/dt),
and the canonical solution (V1 of the published report) is psi_n = (1/(4n)) int e^{-2n|t-tau|} phi_n(tau) dtau, i.e. the
unique solution with psi_n = o(e^{2n|t|}) at both ends.  Discretization: t in [t_min, t_max] split into panels
(breakpoints chosen by the caller, e.g. at the knots of the trial's splines), Chebyshev-Lobatto collocation of order p
on each panel, psi continuous (shared nodes) and psi' continuous at breakpoints, and exact radiation conditions at the
two ends,
    psi' - 2n psi = -A(t_min),  A(t) = int_{-inf}^t e^{-2n(t-tau)} phi dtau,
    psi' + 2n psi =  B(t_max),  B(t) = int_t^inf e^{-2n(tau-t)} phi dtau,
with the tails A, B from asymptotic power laws phi ~ sum_i alpha_i e^{mu_i t} fitted on the end panels
(B = sum alpha_i e^{mu_i t}/(2n - mu_i), A = sum alpha_i e^{mu_i t}/(2n + mu_i)).
This is a different discretization from a quadrature of the Green's function integrals.
"""
import numpy as np
from scipy.linalg import solve_banded


def cheb(p):
    """Chebyshev-Lobatto nodes on [-1,1] (increasing) and the differentiation matrix."""
    x = -np.cos(np.pi * np.arange(p + 1) / p)
    c = np.ones(p + 1)
    c[0] = c[-1] = 2.0
    c = c * (-1.0) ** np.arange(p + 1)
    X = np.tile(x, (p + 1, 1)).T
    dX = X - X.T
    D = np.outer(c, 1 / c) / (dX + np.eye(p + 1))
    D = D - np.diag(D.sum(axis=1))
    return x, D


def clenshaw_curtis_weights(p):
    """Weights for int_{-1}^{1} f on the increasing Lobatto nodes (exact for the interpolant)."""
    # via the Chebyshev moments
    x = -np.cos(np.pi * np.arange(p + 1) / p)
    V = np.cos(np.outer(np.arange(p + 1), np.arccos(x)))      # T_k(x_j)
    mom = np.zeros(p + 1)
    for kk in range(0, p + 1, 2):
        mom[kk] = 2.0 / (1 - kk ** 2)
    w = np.linalg.solve(V, mom)
    return w


class Panels:
    def __init__(self, breaks, p):
        self.b = np.asarray(breaks, float)
        assert np.all(np.diff(self.b) > 0)
        self.P = len(self.b) - 1
        self.p = p
        self.x, self.D = cheb(p)
        self.h = np.diff(self.b)
        self.N = self.P * p + 1
        t = np.empty(self.N)
        for j in range(self.P):
            t[j * p: j * p + p + 1] = self.b[j] + (self.x + 1) * self.h[j] / 2
        self.t = t
        self.r = np.exp(t)
        self.wcc = clenshaw_curtis_weights(p)
        self.D2 = self.D @ self.D

    def integrate(self, f):
        """int_{t_min}^{t_max} f dt of the panel interpolant; f (N, ...) ."""
        p = self.p
        out = 0.0
        for j in range(self.P):
            out = out + (self.h[j] / 2) * np.tensordot(self.wcc, f[j * p: j * p + p + 1], axes=(0, 0))
        return out

    def dt(self, f):
        """d/dt of the panel interpolants at the nodes (average of left/right values at breakpoints)."""
        p = self.p
        out = np.zeros_like(f)
        cnt = np.zeros(self.N)
        for j in range(self.P):
            sl = slice(j * p, j * p + p + 1)
            out[sl] += (2 / self.h[j]) * np.tensordot(self.D, f[sl], axes=(1, 0))
            cnt[sl] += 1
        return out / cnt.reshape((-1,) + (1,) * (f.ndim - 1))

    def locate(self, tq):
        tq = np.atleast_1d(np.asarray(tq, float))
        j = np.clip(np.searchsorted(self.b, tq, side='right') - 1, 0, self.P - 1)
        return tq, j

    def interp(self, f, tq, deriv=0):
        """Panel interpolant of f (N, ...) (or of its t-derivative of order deriv) at the points tq (barycentric
        Chebyshev-Lobatto formula on the panel containing each point)."""
        tq, j = self.locate(tq)
        p = self.p
        wb = (-1.0) ** np.arange(p + 1)
        wb[0] *= 0.5
        wb[-1] *= 0.5
        out = []
        for q, jp in zip(tq, j):
            sl = slice(jp * p, jp * p + p + 1)
            fl = f[sl]
            for _ in range(deriv):
                fl = (2 / self.h[jp]) * np.tensordot(self.D, fl, axes=(1, 0))
            xq = 2 * (q - self.b[jp]) / self.h[jp] - 1
            d = xq - self.x
            k = np.argmin(np.abs(d))
            if abs(d[k]) < 1e-14:
                out.append(fl[k])
                continue
            c = wb / d
            out.append(np.tensordot(c, fl, axes=(0, 0)) / c.sum())
        return np.array(out)

    def base_banded(self):
        """Banded storage (l = u = p) of the collocation matrix for psi'' with the rows of the radiation conditions
        (row 0: psi'; row N-1: psi'); the lambda-dependent diagonal is added in banded(lam).  Collocation rows are
        scaled by h^2, matching rows by the mean panel width, radiation rows by h."""
        if hasattr(self, '_ab0'):
            return self._ab0
        p, N = self.p, self.N
        u = p
        ab = np.zeros((2 * p + 1, N))
        ii, jj = np.meshgrid(np.arange(p + 1), np.arange(p + 1), indexing='ij')
        diag_sc = np.zeros(N)
        for jp in range(self.P):
            h = self.h[jp]
            g0 = jp * p
            M2 = 4.0 * self.D2       # h^2 (2/h)^2 D2
            rows = g0 + ii[1:p]
            cols = g0 + jj[1:p]
            ab[u + rows - cols, cols] += M2[1:p]
            diag_sc[g0 + 1: g0 + p] = h ** 2
            if jp < self.P - 1:
                gi = g0 + p
                hn = self.h[jp + 1]
                scm = 0.5 * (h + hn)
                cl = g0 + np.arange(p + 1)
                ab[u + gi - cl, cl] += scm * (2 / h) * self.D[p]
                cr = gi + np.arange(p + 1)
                ab[u + gi - cr, cr] += -scm * (2 / hn) * self.D[0]
        cl = np.arange(p + 1)
        ab[u + 0 - cl, cl] += 2.0 * self.D[0]
        g0 = (self.P - 1) * p
        cl = g0 + np.arange(p + 1)
        ab[u + (N - 1) - cl, cl] += 2.0 * self.D[p]
        self._ab0 = ab
        self._diag_sc = diag_sc
        return ab

    def banded(self, lam):
        ab = self.base_banded().copy()
        u = self.p
        ab[u, :] += -self._diag_sc * lam ** 2
        ab[u, 0] += -self.h[0] * lam
        ab[u, -1] += self.h[-1] * lam
        return (self.p, self.p), ab

    def rhs_scale(self):
        """Row scaling vector applied to the collocation rows (h^2) so that rhs = -h^2 phi."""
        p = self.p
        s = np.zeros(self.N)
        for jp in range(self.P):
            s[jp * p + 1: jp * p + p] = self.h[jp] ** 2
        return s


def fit_tail(t, phi, mus):
    """Least-squares fit phi ~ sum_i alpha_i e^{mu_i t} on the given nodes; phi (Nt, Nmodes) -> alpha (len(mus), Nm)."""
    t0 = t.mean()
    E = np.exp(np.outer(t - t0, mus))
    alpha, *_ = np.linalg.lstsq(E, phi, rcond=None)
    return alpha, t0


def solve_modes(pan, phi, ns, mu_left=(4.0,), mu_right=None, tail_panels=2):
    """Canonical modal inverse.  phi: (N, len(ns)) values of phi_n = r^2 f_n at the panel nodes.
    Returns psi (N, len(ns)), dpsi = d psi/dt (N, len(ns)), and the tail data."""
    p, N = pan.p, pan.N
    ns = np.asarray(ns)
    psi = np.zeros_like(phi)
    sc = pan.rhs_scale()
    # tails
    nl = tail_panels * p + 1
    tl, tr = pan.t[:nl], pan.t[-nl:]
    al, t0l = fit_tail(tl, phi[:nl], np.asarray(mu_left))
    tail = dict()
    if mu_right is not None:
        ar, t0r = fit_tail(tr, phi[-nl:], np.asarray(mu_right))
        fitres = np.abs(np.exp(np.outer(tr - t0r, mu_right)) @ ar - phi[-nl:]).max(axis=0) / \
            (np.abs(phi[-nl:]).max(axis=0) + 1e-300)
        tail['right_fit_relres'] = fitres
        tail['alpha_right'] = ar
    for jn, n in enumerate(ns):
        lam = 2.0 * n
        (l, u), ab = pan.banded(lam)
        b = -sc * phi[:, jn]
        # A(t_min) and B(t_max)
        mul = np.asarray(mu_left)
        A = np.sum(al[:, jn] * np.exp(mul * (pan.t[0] - t0l)) / (lam + mul))
        b[0] = -pan.h[0] * A
        if mu_right is not None:
            mur = np.asarray(mu_right)
            assert np.all(lam > mur)
            B = np.sum(ar[:, jn] * np.exp(mur * (pan.t[-1] - t0r)) / (lam - mur))
        else:
            B = 0.0
        b[-1] = pan.h[-1] * B
        psi[:, jn] = solve_banded((l, u), ab, b)
    dpsi = pan.dt(psi)
    return psi, dpsi, tail
