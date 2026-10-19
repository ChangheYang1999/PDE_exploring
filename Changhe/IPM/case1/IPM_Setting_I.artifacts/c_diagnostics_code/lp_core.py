"""Lead prototype: log-polar discretization of IPM Setting I (independent of the numerics lane).

Coordinates u = log r on a uniform grid [u0, u1], theta_j = (j + 1/2) pi/(2M), j = 0..M-1 (open quadrant).
rho = wgt(u) phi(u, theta), wgt = r^3 (1 + r^2)^{(k0-3)/2}; phi = sum_{m<M} phi_m(u) sin((2m+1) theta)
(odd in y, even in x). Velocity by the modal Green function (SPEC V1) written in u:
  q_m = rho_m / r,  h_n = (1/2)[q_{n-1}' - (2n-2) q_{n-1} + q_n' + (2n+2) q_n]   (' = d/du, n = 1..M, q_M = 0),
  psit_n := psi_n / r^2 = (1/(4n)) [ int_{-inf}^u e^{-(2n+2)(u-v)} h_n dv + int_u^inf e^{-(2n-2)(v-u)} h_n dv ],
  c = psi_xy(0) = (1/2) int h_1 du.
Transport in (u, theta): W.grad rho = A d_u rho + B d_theta rho, A = c_l - d_theta psit, B = d_u psit + 2 psit.
Tails: for u < u0, rho = x^2 y (q_m ~ e^{2u}); for u > u1, homogeneous extension rho_m ~ r^k (q ~ e^{(k-1)u}).
"""
import numpy as np


class LP:
    def __init__(self, u0=-5.0, u1=7.0, Nu=601, M=24, k0=0.6):
        self.u = np.linspace(u0, u1, Nu)
        self.du = self.u[1] - self.u[0]
        self.Nu, self.M, self.k0 = Nu, M, k0
        j = np.arange(M)
        self.th = (j + 0.5) * np.pi / (2 * M)
        m = np.arange(M)
        self.S = np.sin(np.outer(self.th, 2 * m + 1))          # [j, m] odd modes
        self.Sinv = np.linalg.inv(self.S)
        self.Cd = np.cos(np.outer(self.th, 2 * m + 1)) * (2 * m + 1)  # d_theta of odd modes
        n = np.arange(1, M + 1)
        self.n = n
        self.S2 = np.sin(np.outer(self.th, 2 * n))              # [j, n] even modes (psi)
        self.C2 = np.cos(np.outer(self.th, 2 * n)) * (2 * n)
        r = np.exp(self.u)
        self.r = r
        self.lw = 3 * self.u + 0.5 * (k0 - 3) * np.log1p(r ** 2)   # log wgt
        self.dlw = 3 - (3 - k0) * r ** 2 / (1 + r ** 2)

    # ---------- derivatives in u (4th order central, one-sided near ends) ----------
    def du_c(self, f):
        d = np.empty_like(f)
        h = self.du
        d[2:-2] = (f[:-4] - 8 * f[1:-3] + 8 * f[3:-1] - f[4:]) / (12 * h)
        d[0] = (-25 * f[0] + 48 * f[1] - 36 * f[2] + 16 * f[3] - 3 * f[4]) / (12 * h)
        d[1] = (-3 * f[0] - 10 * f[1] + 18 * f[2] - 6 * f[3] + f[4]) / (12 * h)
        d[-1] = -(-25 * f[-1] + 48 * f[-2] - 36 * f[-3] + 16 * f[-4] - 3 * f[-5]) / (12 * h)
        d[-2] = -(-3 * f[-1] - 10 * f[-2] + 18 * f[-3] - 6 * f[-4] + f[-5]) / (12 * h)
        return d

    # ---------- exponential convolutions (vectorized over modes) ----------
    @staticmethod
    def _wts(alpha, d):
        alpha = np.asarray(alpha, float)
        z = alpha * d
        e = np.exp(-z)
        small = np.abs(z) < 1e-8
        zs = np.where(small, 1.0, z)
        al = np.where(small, 1.0, alpha)
        w1 = np.where(small, d / 2, (1 - (1 - e) / zs) / al)
        w0 = np.where(small, d / 2, ((1 - e) / zs - e) / al)
        return w0, w1, e

    def conv_left(self, h, alpha, tail0):
        """A(u) = int_{-inf}^u e^{-alpha(u-v)} h dv, piecewise-linear h, A(u0) = tail0. h: [Nu, M]."""
        w0, w1, e = self._wts(alpha, self.du)
        A = np.empty_like(h)
        A[0] = tail0
        for i in range(1, h.shape[0]):
            A[i] = e * A[i - 1] + w0 * h[i - 1] + w1 * h[i]
        return A

    def conv_right(self, h, beta, tail1):
        """B(u) = int_u^inf e^{-beta(v-u)} h dv, B(u1) = tail1."""
        w0, w1, e = self._wts(beta, self.du)
        B = np.empty_like(h)
        B[-1] = tail1
        for i in range(h.shape[0] - 2, -1, -1):
            B[i] = e * B[i + 1] + w0 * h[i + 1] + w1 * h[i]
        return B

    # ---------- velocity ----------
    def velocity(self, phi, k):
        """phi on grid [Nu, M]. Returns psit_n [Nu, M], d_u psit_n, c, and h modes."""
        rho_m = (phi @ self.Sinv.T) * np.exp(self.lw)[:, None]     # [Nu, m]
        q = rho_m / self.r[:, None]
        qd = self.du_c(q)
        qn = np.zeros_like(q); qn[:, :-1] = q[:, 1:]     # q_n for n = 1..M (q_M = 0)
        qnd = np.zeros_like(q); qnd[:, :-1] = qd[:, 1:]
        n = self.n[None, :]
        h = 0.5 * (qd - (2 * n - 2) * q + qnd + (2 * n + 2) * qn)
        al = 2.0 * self.n + 2
        be = 2.0 * self.n - 2
        A = self.conv_left(h, al, h[0] / (al + 2))
        B = self.conv_right(h, be, h[-1] / (be + 1 - k))
        psit = (A + B) / (4 * self.n)[None, :]
        dpsit = (-al * A + be * B) / (4 * self.n)[None, :]
        c = 0.5 * (h[0, 0] / 2 + np.trapz(h[:, 0], self.u) + h[-1, 0] / (1 - k))
        return psit, dpsit, c, h

    def fields(self, phi, cl, k):
        psit, dpsit, c, h = self.velocity(phi, k)
        P = psit @ self.S2.T
        Pth = psit @ self.C2.T
        Pu = dpsit @ self.S2.T
        A = cl - Pth
        B = Pu + 2 * P
        return A, B, c, psit

    def transport(self, phi, A, B, ghost_lo, ghost_hi):
        """Returns W.grad rho / wgt in terms of phi: A (d_u phi + dlw phi) + B d_theta phi, upwind-biased 3rd order in u."""
        h = self.du
        f = np.vstack([ghost_lo, phi, ghost_hi])      # 2 ghost rows each side
        dp = (2 * f[3:-1] + 3 * f[2:-2] - 6 * f[1:-3] + f[:-4]) / (6 * h)
        dm = (-f[4:] + 6 * f[3:-1] - 3 * f[2:-2] - 2 * f[1:-3]) / (6 * h)
        dphi = np.where(A > 0, dp, dm)
        dth = (phi @ self.Sinv.T) @ self.Cd.T
        return A * (dphi + self.dlw[:, None] * phi) + B * dth

    def ghosts(self, phi, k):
        h = self.du
        ul = self.u[0] - h * np.array([2, 1])
        base = np.cos(self.th) ** 2 * np.sin(self.th)
        # rho = x^2 y below u0: phi = base * (1 + r^2)^{(3-k0)/2}
        glo = base[None, :] * (1 + np.exp(2 * ul))[:, None] ** ((3 - self.k0) / 2)
        uh = self.u[-1] + h * np.array([1, 2])
        # rho ~ r^k above u1: phi = phi(u1) * exp((k - dlw-integral)) approx with wgt growth k0
        lw1 = self.lw[-1]
        lwh = 3 * uh + 0.5 * (self.k0 - 3) * np.log1p(np.exp(2 * uh))
        ghi = phi[-1][None, :] * np.exp(k * (uh - self.u[-1]) - (lwh - lw1))[:, None]
        return glo, ghi
