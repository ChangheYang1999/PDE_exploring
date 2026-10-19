"""Verifier's polar-mode full-plane inverse for the IPM profile problem (verifier).

Independent of the numerics lane.  Parity class: rho even in x, odd in y,
  rho = sum_{m odd} f_m(r) sin(m t),   psi = sum_{n even >= 2} p_n(r) sin(n t).
Derivative-free Green's formula (derived in notes/analysis_v1.md, section B):
  p_n(r)  = (1/2) [ S_hi - S_lo ],  S_hi = r^n int_r^inf s^{-n} f_{n+1} ds,  S_lo = r^{-n} int_0^r s^n f_{n-1} ds
  p_n'(r) = (n/2r)(S_hi + S_lo) - (f_{n+1} + f_{n-1})/2
This is the unique odd/odd solution of -Lap psi = d_x rho with p_n = o(r^n) (gauge fixed),
valid when f_m = O(r^k), k < 1, at infinity.  psi_xy(0) = int_0^inf f_3(s) s^{-2} ds.
Radial discretization: uniform grid in u = log r on [log r0, log R]; the exponentially
weighted cumulative integrals are done by exact integration of exp(-n(u-u')) against
local Lagrange interpolants (order q), which is stable for all n.
Tails: f_m ~ alpha_m r^{beta_m} for r < r0, f_m ~ A_m r^{k_m} for r > R (analytic).
"""
import numpy as np


class LogGrid:
    def __init__(self, N, r0, R, q=8):
        self.N = N
        self.u = np.linspace(np.log(r0), np.log(R), N)
        self.h = self.u[1] - self.u[0]
        self.r = np.exp(self.u)
        self.q = q
        self._wcache = {}

    def _stencil(self, j):
        q = self.q
        lo = min(max(j - q // 2 + 1, 0), self.N - q)
        return np.arange(lo, lo + q)

    def _weights(self, lam, j, backward):
        # forward: int_{u_j}^{u_{j+1}} e^{-lam (u_{j+1}-u')} L_k(u') du'
        # backward: int_{u_j}^{u_{j+1}} e^{-lam (u'-u_j)} L_k(u') du'
        key = (lam, j, backward)
        if key in self._wcache:
            return self._wcache[key]
        st = self._stencil(j)
        xs = (st - j).astype(float)  # nodes in units of h, interval is [0,1]
        gx, gw = np.polynomial.legendre.leggauss(24)
        t = 0.5 * (gx + 1)
        w = 0.5 * gw
        ker = np.exp(-lam * self.h * ((1 - t) if not backward else t))
        L = np.ones((len(xs), len(t)))
        for a in range(len(xs)):
            for b in range(len(xs)):
                if a != b:
                    L[a] *= (t - xs[b]) / (xs[a] - xs[b])
        W = self.h * (L * (ker * w)[None, :]).sum(1)
        self._wcache[key] = (st, W)
        return st, W

    def expcum_fwd(self, g, lam, Q0=0.0):
        """Q_j = int_{u_0}^{u_j} e^{-lam(u_j-u')} g du' + Q0 e^{-lam(u_j-u_0)}."""
        Q = np.empty(self.N)
        Q[0] = Q0
        e = np.exp(-lam * self.h)
        for j in range(self.N - 1):
            st, W = self._weights(lam, j, False)
            Q[j + 1] = e * Q[j] + W @ g[st]
        return Q

    def expcum_bwd(self, g, lam, QN=0.0):
        """Q_j = int_{u_j}^{u_N} e^{-lam(u'-u_j)} g du' + QN e^{-lam(u_N-u_j)}."""
        Q = np.empty(self.N)
        Q[-1] = QN
        e = np.exp(-lam * self.h)
        for j in range(self.N - 2, -1, -1):
            st, W = self._weights(lam, j, True)
            Q[j] = e * Q[j + 1] + W @ g[st]
        return Q

    def integral(self, g):
        return self.expcum_fwd(g, 0.0)[-1]

    def du(self, F, order=1):
        """d/du along axis 0 by high-order (8th) central differences, one-sided at ends."""
        from numpy.polynomial import polynomial as P
        N, q = self.N, 9
        D = np.zeros_like(F)
        for j in range(N):
            lo = min(max(j - q // 2, 0), N - q)
            st = np.arange(lo, lo + q)
            xs = (st - j) * self.h
            V = np.vander(xs, q, increasing=True)
            # derivative weights at 0: row of inverse
            Vi = np.linalg.inv(V)
            wts = Vi[order] * (1 if order == 1 else 2)
            D[j] = np.tensordot(wts, F[st], axes=(0, 0))
        return D


def modes_from_samples(rho_rt, Mmax):
    """rho_rt[j, i] on theta_i = 2 pi i / Nt; returns sin coefficients f_m (m odd <= Mmax),
    the max size of coefficients forbidden by parity, and the size of the top modes."""
    Nt = rho_rt.shape[1]
    F = np.fft.rfft(rho_rt, axis=1) / Nt
    b = -2 * F.imag
    a = 2 * F.real
    a[:, 0] /= 2
    m = np.arange(F.shape[1])
    fm = {mm: b[:, mm].copy() for mm in range(1, Mmax + 1, 2)}
    bad = max(np.abs(a).max(), np.abs(b[:, m % 2 == 0]).max())
    return fm, bad, np.abs(b[:, -4:]).max()


def _expcum_vec(g, gg, lam, Q, backward):
    """expcum_fwd / expcum_bwd with the same weights, vectorized: on the uniform grid the weights depend on j only
    through the stencil offset, so they are computed once per offset; the recursion is done by lfilter."""
    from scipy.signal import lfilter
    N = g.N
    key = ('vec', lam, backward)
    if key not in g._wcache:
        st = np.array([g._stencil(j) for j in range(N - 1)])
        off = st[:, 0] - np.arange(N - 1)
        W = np.empty((N - 1, g.q))
        for o in np.unique(off):
            j = int(np.where(off == o)[0][0])
            W[off == o] = g._weights(lam, j, backward)[1]
        g._wcache[key] = (st, W)
    st, W = g._wcache[key]
    b = np.einsum('jk,jk->j', W, gg[st])
    e = np.exp(-lam * g.h)
    out = np.empty(N)
    if not backward:
        out[0] = Q
        out[1:] = lfilter([1.0], [1.0, -e], b, zi=[e * Q])[0]
    else:
        out[-1] = Q
        out[:-1] = lfilter([1.0], [1.0, -e], b[::-1], zi=[e * Q])[0][::-1]
    return out


def psi_modes(g, fm, nmax, tail_hi=None, tail_lo=None, slow=False):
    """As psi_modes_slow (same discretization); slow=True uses the original loops."""
    if slow:
        return psi_modes_slow(g, fm, nmax, tail_hi, tail_lo)
    r = g.r
    r0, R = r[0], r[-1]
    z = np.zeros_like(r)
    out = {}
    for n in range(2, nmax + 1, 2):
        flo = fm.get(n - 1, z)
        fhi = fm.get(n + 1, z)
        Q0 = 0.0
        if tail_lo and (n - 1) in tail_lo:
            al, be = tail_lo[n - 1]
            Q0 = al * r0 ** (be + 1) / (n + be + 1)
        QN = 0.0
        if tail_hi and (n + 1) in tail_hi:
            A, k = tail_hi[n + 1]
            QN = A * R ** (k + 1) / (n - k - 1)
        Slo = _expcum_vec(g, r * flo, float(n), Q0, False)
        Shi = _expcum_vec(g, r * fhi, float(n), QN, True)
        p = 0.5 * (Shi - Slo)
        dp = n / (2 * r) * (Shi + Slo) - 0.5 * (fhi + flo)
        out[n] = (p, dp)
    return out


def psi_modes_slow(g, fm, nmax, tail_hi=None, tail_lo=None):
    """p_n, p_n' at nodes for even n=2..nmax. tail_hi: m -> (A,k), tail_lo: m -> (alpha,beta)."""
    r = g.r
    r0, R = r[0], r[-1]
    z = np.zeros_like(r)
    out = {}
    for n in range(2, nmax + 1, 2):
        flo = fm.get(n - 1, z)
        fhi = fm.get(n + 1, z)
        Q0 = 0.0
        if tail_lo and (n - 1) in tail_lo:
            al, be = tail_lo[n - 1]
            Q0 = al * r0 ** (be + 1) / (n + be + 1)
        QN = 0.0
        if tail_hi and (n + 1) in tail_hi:
            A, k = tail_hi[n + 1]
            QN = A * R ** (k + 1) / (n - k - 1)
        Slo = g.expcum_fwd(r * flo, n, Q0)
        Shi = g.expcum_bwd(r * fhi, n, QN)
        p = 0.5 * (Shi - Slo)
        dp = n / (2 * r) * (Shi + Slo) - 0.5 * (fhi + flo)
        out[n] = (p, dp)
    return out


def center_c(g, f3, tail_hi=None, tail_lo=None):
    """psi_xy(0) = int_0^inf f_3 s^{-2} ds = int f_3 e^{-u} du."""
    r = g.r
    c = g.integral(f3 / r)
    if tail_hi is not None:
        A, k = tail_hi
        c += A * r[-1] ** (k - 1) / (1 - k)
    if tail_lo is not None:
        al, be = tail_lo
        c += al * r[0] ** (be - 1) / (be - 1)
    return c


def synth(pm, theta):
    psi = psr = pst = 0.0
    for n, (p, dp) in pm.items():
        s = np.sin(n * theta)[None, :]
        co = np.cos(n * theta)[None, :]
        psi = psi + p[:, None] * s
        psr = psr + dp[:, None] * s
        pst = pst + n * p[:, None] * co
    return psi, psr, pst


def velocity_polar(r, theta, psr, pst):
    R = r[:, None]
    ct, st = np.cos(theta)[None, :], np.sin(theta)[None, :]
    psx = ct * psr - st * pst / R
    psy = st * psr + ct * pst / R
    return -psy, psx
