# Independent verifier evaluator (verification), written from scratch.
#
# Canonical full-plane inverse for densities rho even in x, odd in y, |rho| <= C(1+r)^gamma, gamma<1.
#   rho(r,th) = sum_{m>=0} b_{2m+1}(r) sin((2m+1) th)
#   psi(r,th) = sum_{n>=1} psi_n(r) sin(2 n th)
# Derivative-free form (integrations by parts of the modal Green function, derived in VERIFY_REPORT.md):
#   psi_n(r) = (1/2) [ Q_n(r) - P_n(r) ],
#   P_n(r) = r^{-2n} int_0^r s^{2n} b_{2n-1}(s) ds,   Q_n(r) = r^{2n} int_r^inf s^{-2n} b_{2n+1}(s) ds,
#   r psi_n'(r) = n (Q_n + P_n) - (r/2)(b_{2n-1} + b_{2n+1}).
# In t = log r:  P_n(t) = int_{-inf}^t e^{-2n(t-tau)} h_{2n-1}(tau) dtau,  Q_n(t) = int_t^inf e^{-2n(tau-t)} h_{2n+1}(tau) dtau,
#   h_k(tau) = e^tau b_k(e^tau).
# Radial discretization: uniform panels in t with Gauss-Legendre nodes; exponential-kernel weights computed
# by high-order quadrature of Lagrange polynomials; panel-to-panel linear recurrence. Angular: DST-IV on
# theta_j = (2j+1) pi/(4M), j=0..M-1 (quarter-wave symmetry).
import numpy as np
from numpy.polynomial.legendre import leggauss


def lagrange_basis(nodes, x):
    """Values L[j, i] = ell_j(x_i) of Lagrange basis on 'nodes' at points x (barycentric)."""
    nodes = np.asarray(nodes); x = np.asarray(x)
    q = len(nodes)
    w = np.array([1.0 / np.prod(nodes[j] - np.delete(nodes, j)) for j in range(q)])
    d = x[None, :] - nodes[:, None]
    exact = np.isclose(d, 0.0, atol=1e-15)
    d[exact] = 1.0
    tmp = w[:, None] / d
    L = tmp / tmp.sum(axis=0, keepdims=True)
    cols = np.where(exact.any(axis=0))[0]
    for c in cols:
        L[:, c] = exact[:, c].astype(float)
    return L


class Radial:
    def __init__(self, tmin, tmax, npan, q=16):
        self.tmin, self.tmax, self.npan, self.q = tmin, tmax, npan, q
        self.edges = np.linspace(tmin, tmax, npan + 1)
        self.H = (tmax - tmin) / npan
        xg, wg = leggauss(q)
        self.xg = xg  # reference nodes in [-1,1]
        self.t = (0.5 * (self.edges[:-1, None] + self.edges[1:, None]) + 0.5 * self.H * xg[None, :])  # (npan,q)
        self.r = np.exp(self.t)
        self._cache = {}

    def weights(self, kappa):
        """For kernel e^{-kappa (t_i - tau)} on a panel [a, a+H] (reference coordinates):
        Wf[i,j] = int_a^{t_i} e^{-kappa(t_i - tau)} ell_j(tau) dtau   (forward, from left edge to node i)
        Ef[j]   = int_a^{a+H} e^{-kappa(a+H - tau)} ell_j(tau) dtau    (forward, whole panel to right edge)
        Wb[i,j] = int_{t_i}^{a+H} e^{-kappa(tau - t_i)} ell_j(tau) dtau (backward)
        Eb[j]   = int_a^{a+H} e^{-kappa(tau - a)} ell_j(tau) dtau
        """
        key = float(kappa)
        if key in self._cache:
            return self._cache[key]
        q, H, xg = self.q, self.H, self.xg
        xs, ws = leggauss(80)
        Wf = np.zeros((q, q)); Wb = np.zeros((q, q))
        for i in range(q):
            # forward: tau from -1 to x_i (reference), t_i - tau = (x_i - s) H/2
            lo, hi = -1.0, xg[i]
            s = 0.5 * (hi - lo) * xs + 0.5 * (hi + lo); w = 0.5 * (hi - lo) * ws * (H / 2)
            L = lagrange_basis(xg, s)
            Wf[i] = L @ (w * np.exp(-kappa * (xg[i] - s) * H / 2))
            lo, hi = xg[i], 1.0
            s = 0.5 * (hi - lo) * xs + 0.5 * (hi + lo); w = 0.5 * (hi - lo) * ws * (H / 2)
            L = lagrange_basis(xg, s)
            Wb[i] = L @ (w * np.exp(-kappa * (s - xg[i]) * H / 2))
        s = xs; w = ws * (H / 2)
        L = lagrange_basis(xg, s)
        Ef = L @ (w * np.exp(-kappa * (1.0 - s) * H / 2))
        Eb = L @ (w * np.exp(-kappa * (s + 1.0) * H / 2))
        self._cache[key] = (Wf, Ef, Wb, Eb)
        return self._cache[key]

    def causal(self, h, kappa, left_value=0.0):
        """P(t) = int_{-inf}^t e^{-kappa(t-tau)} h(tau) dtau at all nodes; h shape (npan,q,...);
        left_value = P(tmin) (tail contribution)."""
        Wf, Ef, _, _ = self.weights(kappa)
        dec = np.exp(-kappa * self.H)
        loc_nodes = np.einsum('ij,pj...->pi...', Wf, h)
        loc_edge = np.einsum('j,pj...->p...', Ef, h)
        out = np.empty_like(loc_nodes)
        Pa = np.broadcast_to(np.asarray(left_value, dtype=float), h.shape[2:]).copy()
        decay_nodes = np.exp(-kappa * (self.xg + 1.0) * self.H / 2)
        for p in range(self.npan):
            out[p] = decay_nodes.reshape((-1,) + (1,) * (h.ndim - 2)) * Pa[None] + loc_nodes[p]
            Pa = dec * Pa + loc_edge[p]
        return out

    def anticausal(self, h, kappa, right_value=0.0):
        """Q(t) = int_t^{inf} e^{-kappa(tau-t)} h(tau) dtau at all nodes; right_value = Q(tmax)."""
        _, _, Wb, Eb = self.weights(kappa)
        dec = np.exp(-kappa * self.H)
        loc_nodes = np.einsum('ij,pj...->pi...', Wb, h)
        loc_edge = np.einsum('j,pj...->p...', Eb, h)
        out = np.empty_like(loc_nodes)
        Qb = np.broadcast_to(np.asarray(right_value, dtype=float), h.shape[2:]).copy()
        decay_nodes = np.exp(-kappa * (1.0 - self.xg) * self.H / 2)
        for p in range(self.npan - 1, -1, -1):
            out[p] = decay_nodes.reshape((-1,) + (1,) * (h.ndim - 2)) * Qb[None] + loc_nodes[p]
            Qb = dec * Qb + loc_edge[p]
        return out


def theta_grid(M):
    return (2 * np.arange(M) + 1) * np.pi / (4 * M)


def odd_sine_coeffs(vals, M):
    """vals[..., j] at theta_j; returns b[..., m] for k = 2m+1 (DST-IV, exact for k<=2M-1)."""
    th = theta_grid(M)
    S = np.sin(np.outer(2 * np.arange(M) + 1, th))  # (m, j)
    return (2.0 / M) * vals @ S.T


def tail_exponent(rad, b, npt=3):
    """Estimate local log-slope d log|h| / dt of h at the right end (per mode), for tail closure."""
    return None


class ModalInverse:
    """Canonical inverse on radial panels x DST-IV angles.
    rho_fun(x, y) -> rho (numpy, vectorized). Tail closures: power-law fit at both ends per mode."""

    def __init__(self, rad: Radial, M: int):
        self.rad, self.M = rad, M
        self.th = theta_grid(M)

    def modes(self, rho_fun):
        r = self.rad.r.reshape(-1)
        X = r[:, None] * np.cos(self.th)[None, :]
        Y = r[:, None] * np.sin(self.th)[None, :]
        vals = rho_fun(X, Y)
        b = odd_sine_coeffs(vals, self.M)  # (Nr, M) : b_{2m+1}
        return b.reshape(self.rad.npan, self.rad.q, self.M), vals.reshape(self.rad.npan, self.rad.q, self.M)

    def psi_modes(self, b, tails='powerlaw'):
        """Returns psi_n, r psi_n' for n=1..M (arrays (npan,q,M)), plus c=psi_xy(0) estimate and pieces."""
        rad, M = self.rad, self.M
        r = rad.r[:, :, None]
        h = r * b  # h_{2m+1}
        n = np.arange(1, M + 1)
        # h_{2n-1} -> index n-1 ; h_{2n+1} -> index n (zero for n=M)
        hm = h  # index n-1 for n=1..M
        hp = np.concatenate([h[:, :, 1:], np.zeros_like(h[:, :, :1])], axis=2)
        P = np.empty_like(h); Q = np.empty_like(h)
        for k, nn in enumerate(n):
            kap = 2.0 * nn
            # left tail: h ~ A e^{s t} near tmin  => P(tmin) = h(tmin)/(kap + s)
            left = 0.0; right = 0.0
            if tails == 'powerlaw':
                left = self._left_tail(hm[:, :, k], kap)
                right = self._right_tail(hp[:, :, k], kap)
            P[:, :, k] = rad.causal(hm[:, :, k], kap, left)
            Q[:, :, k] = rad.anticausal(hp[:, :, k], kap, right)
        psi = 0.5 * (Q - P)
        rpsi_r = n[None, None, :] * (Q + P) - 0.5 * (hm + hp)
        return psi, rpsi_r, P, Q

    def _left_tail(self, h, kap):
        # fit log|h| slope on first panel ends
        t = self.rad.t
        h0, h1 = h[0, 0], h[0, -1]
        if h0 == 0.0 or h1 == 0.0 or np.sign(h0) != np.sign(h1):
            return 0.0
        s = np.log(abs(h1 / h0)) / (t[0, -1] - t[0, 0])
        if kap + s <= 0:
            return 0.0
        # extrapolate to edge tmin
        he = h0 * np.exp(s * (self.rad.tmin - t[0, 0]))
        return he / (kap + s)

    def _right_tail(self, h, kap):
        t = self.rad.t
        h0, h1 = h[-1, 0], h[-1, -1]
        if h0 == 0.0 or h1 == 0.0 or np.sign(h0) != np.sign(h1):
            return 0.0
        s = np.log(abs(h1 / h0)) / (t[-1, -1] - t[-1, 0])
        if kap - s <= 0.05:
            # not a decaying tail (noise-level mode or non-admissible growth): flag via attribute, no closure
            self.tail_warnings = getattr(self, 'tail_warnings', 0) + 1
            return 0.0
        he = h1 * np.exp(s * (self.rad.tmax - t[-1, -1]))
        return he / (kap - s)

    def velocity_on_grid(self, rho_fun, tails='powerlaw'):
        b, vals = self.modes(rho_fun)
        psi_n, rpsir_n, P, Q = self.psi_modes(b, tails)
        th = self.th
        n = np.arange(1, self.M + 1)
        S2 = np.sin(np.outer(th, 2 * n))   # (j, n)
        C2 = np.cos(np.outer(th, 2 * n))
        psi = psi_n @ S2.T          # (npan,q,j)
        rpsi_r = rpsir_n @ S2.T
        psi_th = (psi_n * (2 * n)) @ C2.T
        r = self.rad.r[:, :, None]
        st, ct = np.sin(th)[None, None, :], np.cos(th)[None, None, :]
        psi_r = rpsi_r / r
        U1 = -(st * psi_r + ct * psi_th / r)
        U2 = ct * psi_r - st * psi_th / r
        return dict(b=b, rho=vals, psi=psi, U1=U1, U2=U2, psi_n=psi_n, rpsir_n=rpsir_n, P=P, Q=Q)

    def strain_at_origin(self, b, P, Q):
        """c = psi_xy(0) = 2 lim psi_1/r^2 = lim (Q_1 - P_1)/r^2 ; also integral form -a0/4 + int b_3 r^-2 dr."""
        rad = self.rad
        r = rad.r
        # integral form: int_0^inf b_3 r^{-2} dr = int e^{-t} b_3(e^t) dt
        w = (rad.H / 2) * leggauss(rad.q)[1][None, :] * np.ones_like(r)
        I3 = np.sum(w * np.exp(-rad.t) * b[:, :, 1])
        a0 = b[0, 0, 0] / r[0, 0]
        return dict(a0=a0, I3=I3, c_int=-a0 / 4 + I3,
                    c_lim=(Q[0, 0, 0] - P[0, 0, 0]) / r[0, 0] ** 2)
