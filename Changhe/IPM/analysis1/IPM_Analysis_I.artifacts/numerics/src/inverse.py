"""Canonical full-plane inverse (float64, floating-point estimate; not rigorous) for odd/odd sources.

Given d_x rho on a tensor grid (r_i log-uniform, theta_j uniform on [0, pi/2] with endpoints), expand
  d_x rho = sum_{n>=1} f_n(r) sin(2 n theta)   (odd in x and in y),
and compute, by the modal Green formula (PROMPT eq. (Green)),
  psi_n(r) = (1/(4n)) [ r^{-2n} I_in(r) + r^{2n} I_out(r) ],  I_in = int_0^r s^{2n+1} f_n ds,  I_out = int_r^inf s^{1-2n} f_n ds,
  psi_n'(r) = (1/2) [ -r^{-2n-1} I_in + r^{2n-1} I_out ],
  c = psi_xy(0) = (1/2) int_0^inf f_1(s)/s ds.
Radial quadrature: p-point Lagrange interpolation of g_n(t) = f_n(e^t) in t = log s on each cell with exact exponential
moments (Gauss-Legendre, 16 nodes) and the normalized recurrences
  a_n(r_{i+1}) = e^{-2n dt} a_n(r_i) + r_{i+1}^2 int_0^1 e^{(2n+2) dt (tau-1)} g_n(t_i + tau dt) dtau,   a_n = r^{-2n} I_in,
  b_n(r_i)     = e^{-2n dt} b_n(r_{i+1}) + r_i^2 int_0^1 e^{(2-2n) dt tau} g_n(t_i + tau dt) dtau,        b_n = r^{2n} I_out.
Inner start: a_n(r_0) from f_n ~ C s^{2n} below r_0 (a_n(r_0) = r_0^{-2n} int_0^{r_0} C s^{4n+1} ds = r_0^2 f_n(r_0)/(4n+2)).
Outer start: b_n(R) from a power-law fit of f_n on the last decade (powers k-1, 2k-2, k-3 by default).
Velocity: U = grad^perp psi = (-psi_y, psi_x); psi_r = sum psi_n' sin(2n theta), psi_theta = sum 2n psi_n cos(2n theta);
U_r = -(1/r) psi_theta, U_theta = psi_r;  U_x = U_r cos - U_theta sin, U_y = U_r sin + U_theta cos.
"""
import numpy as np
from scipy.fft import dst
from numpy.polynomial.legendre import leggauss


def lagrange_exp_weights(lam, p, shift):
    """Weights w_a (a = 0..p-1) with  int_0^1 e^{lam (tau - shift)} g(tau) dtau ~ sum_a w_a g(tau_a), where the p stencil
    nodes are tau_a = a - (p//2 - 1)  (so the cell [0,1] lies between nodes p//2-1 and p//2). lam may be an array."""
    lam = np.asarray(lam, float)
    x, w = leggauss(16); x = (x + 1) / 2; w = w / 2
    nodes = np.arange(p) - (p // 2 - 1)
    W = np.empty(lam.shape + (p,))
    E = np.exp(lam[..., None] * (x[None, :] - shift))            # (..., 16)
    for a in range(p):
        ell = np.ones_like(x)
        for b in range(p):
            if b != a:
                ell *= (x - nodes[b]) / (nodes[a] - nodes[b])
        W[..., a] = (E * (w * ell)[None, :]).sum(-1)
    return W, nodes


class ModalInverse:
    def __init__(self, r, theta, p=6, tail_powers=None, k=None, tail_decades=1.0):
        self.r = np.asarray(r, float); self.theta = np.asarray(theta, float)
        self.t = np.log(self.r); dt = np.diff(self.t)
        assert np.allclose(dt, dt[0], rtol=1e-10), "r must be log-uniform"
        self.dt = float(dt[0]); self.Nr = len(self.r)
        Nt = len(self.theta) - 1
        assert abs(self.theta[0]) < 1e-15 and abs(self.theta[-1] - np.pi / 2) < 1e-13
        self.Nt = Nt
        self.n = np.arange(1, Nt)                 # modes sin(2 n theta), n = 1..Nt-1
        self.p = p; self.k = k
        self.tail_powers = tail_powers; self.tail_decades = tail_decades
        self.Win, self.nodes = lagrange_exp_weights((2 * self.n + 2) * self.dt, p, 1.0)   # inner: e^{lam (tau-1)}
        self.Wout, _ = lagrange_exp_weights((2 - 2 * self.n) * self.dt, p, 0.0)           # outer: e^{lam tau}
        self.ein = np.exp(-2 * self.n * self.dt)

    def modes(self, fx):
        """sin(2 n theta) coefficients of fx (Nr, Nt+1) sampled on theta_j = j pi/(2 Nt): f_n = (4/pi) int_0^{pi/2} fx sin(2n th) dth
        by the exact DST-I of the interior samples (trapezoid on the odd-odd periodic extension)."""
        return dst(fx[:, 1:-1], type=1, axis=1) / self.Nt           # (Nr, Nt-1)

    def _stencil_values(self, g, i):
        """g values on the p stencil nodes around cell [i, i+1], clamped at the array ends (one-sided extrapolation by
        polynomial continuation is replaced by nearest-cell stencil shift)."""
        p = self.p; lo = i - (p // 2 - 1)
        lo = min(max(lo, 0), self.Nr - p)
        return g[lo:lo + p], lo - (i - (p // 2 - 1))

    def solve(self, fx, verbose=False):
        f = self.modes(fx)                        # (Nr, Nmodes)
        Nr, Nm = f.shape; n = self.n; r = self.r; dt = self.dt; p = self.p
        # --- inner recurrence a_n = r^{-2n} int_0^r s^{2n+1} f_n ds
        a = np.zeros((Nr, Nm))
        a[0] = r[0] ** 2 * f[0] / (4 * n + 2)
        for i in range(Nr - 1):
            lo = i - (p // 2 - 1); lo = min(max(lo, 0), Nr - p); off = lo - (i - (p // 2 - 1))
            if off == 0:
                W = self.Win
            else:   # shifted stencil near the ends: recompute weights for the shifted nodes
                W = self._shifted_weights((2 * n + 2) * dt, 1.0, off)
            a[i + 1] = self.ein * a[i] + dt * r[i + 1] ** 2 * np.einsum('ma,am->m', W, f[lo:lo + p])
        # --- outer start from power-law tail fit of f_n on the last decade(s)
        b = np.zeros((Nr, Nm))
        b[-1] = self._tail_start(f)
        for i in range(Nr - 2, -1, -1):
            lo = i - (p // 2 - 1); lo = min(max(lo, 0), Nr - p); off = lo - (i - (p // 2 - 1))
            W = self.Wout if off == 0 else self._shifted_weights((2 - 2 * n) * dt, 0.0, off)
            b[i] = self.ein * b[i + 1] + dt * r[i] ** 2 * np.einsum('ma,am->m', W, f[lo:lo + p])
        psi = (a + b) / (4 * n)                    # psi_n(r)
        dpsi = (-a + b) / (2 * r[:, None])         # psi_n'(r)  = (1/2)(-r^{-2n-1} I_in + r^{2n-1} I_out)
        # c = psi_xy(0) = 2 lim psi_1/r^2 = (1/2) int_0^inf f_1/s ds = lim_{r->0} b_1(r)/(2 r^2) ... use the integral directly
        c = 0.5 * (b[0, 0] / r[0] ** 2 + f[0, 0] / 2.0)   # c = (1/2) int_0^inf f_1/s ds; head int_0^{r0} f_1/s ds = f_1(r0)/2 for f_1 ~ s^2 (d_x(x^2 y) = 2xy)
        self.f, self.a, self.b, self.psi, self.dpsi, self.c = f, a, b, psi, dpsi, c
        return psi, dpsi, c

    def _shifted_weights(self, lam, shift, off):
        """Weights for a stencil whose nodes are shifted by -off relative to the standard one (used at the array ends)."""
        p = self.p
        x, w = leggauss(16); x = (x + 1) / 2; w = w / 2
        nodes = np.arange(p) - (p // 2 - 1) + off          # stencil start moved by +off cells (verifier audit 2026-10-20T13:31Z)
        W = np.empty(lam.shape + (p,))
        E = np.exp(lam[:, None] * (x[None, :] - shift))
        for a_ in range(p):
            ell = np.ones_like(x)
            for b_ in range(p):
                if b_ != a_:
                    ell *= (x - nodes[b_]) / (nodes[a_] - nodes[b_])
            W[:, a_] = (E * (w * ell)[None, :]).sum(-1)
        return W

    def _tail_start(self, f):
        """b_n(R) = R^{2n} int_R^inf s^{1-2n} f_n ds with f_n ~ sum_j A_j s^{q_j} fitted on the last tail_decades of the grid."""
        if self.tail_powers is None:
            return np.zeros(f.shape[1])
        R = self.r[-1]; sel = self.r >= R / 10 ** self.tail_decades
        qs = np.asarray(self.tail_powers, float)
        # least squares fit in the scaled variable (s/R): f_n(s) = sum_j A_j (s/R)^{q_j}
        X = (self.r[sel, None] / R) ** qs[None, :]
        A, *_ = np.linalg.lstsq(X, f[sel], rcond=None)          # (nq, Nm)
        # int_R^inf s^{1-2n} (s/R)^q ds = R^{2-2n} / (2n - 2 - q)   (needs 2n - 2 - q > 0; n=1 needs q < 0)
        n = self.n
        denom = (2 * n[None, :] - 2 - qs[:, None])
        if np.any(denom <= 0):
            raise ValueError("tail power not integrable for n=1")
        return R ** 2 * (A / denom).sum(0)
        
    def _c_integral(self, f1):
        """c = (1/2) int_0^inf f_1(s)/s ds = (1/2) int g_1(t) dt, with power-law head (f_1 ~ s^3) and fitted tail."""
        t = self.t; g = f1
        # composite trapezoid with end corrections is enough at these resolutions; use Simpson
        from scipy.integrate import simpson
        I = simpson(g, x=t)
        head = f1[0] / 3.0                       # int_0^{r0} C s^3 / s ds = f_1(r0)/3
        tail = 0.0
        if self.tail_powers is not None:
            R = self.r[-1]; sel = self.r >= R / 10 ** self.tail_decades
            qs = np.asarray(self.tail_powers, float)
            X = (self.r[sel, None] / R) ** qs[None, :]
            A, *_ = np.linalg.lstsq(X, f1[sel], rcond=None)
            tail = float((A / (-qs)).sum())      # int_R^inf (s/R)^q / s ds = 1/(-q)
        return 0.5 * (I + head + tail)

    def velocity(self, theta=None):
        """U_x, U_y, U_r, U_theta, psi on the grid r x theta (theta defaults to the solve grid)."""
        th = self.theta if theta is None else np.asarray(theta, float)
        n = self.n
        S = np.sin(2 * n[:, None] * th[None, :]); C = np.cos(2 * n[:, None] * th[None, :])
        psi = self.psi @ S
        psi_r = self.dpsi @ S
        psi_t = (2 * n[None, :] * self.psi) @ C
        Ur = -psi_t / self.r[:, None]         # U = grad^perp psi = (-psi_y, psi_x): U_r = -psi_theta/r, U_theta = psi_r
        Ut = psi_r
        ct, st = np.cos(th), np.sin(th)
        Ux = Ur * ct[None, :] - Ut * st[None, :]
        Uy = Ur * st[None, :] + Ut * ct[None, :]
        return dict(psi=psi, Ux=Ux, Uy=Uy, Ur=Ur, Ut=Ut)


def test_gaussian(Nr=4000, Nt=64):
    """psi = x y e^{-r^2}: d_x rho = -Lap psi = x y (12 - 4 r^2) e^{-r^2}; psi_xy(0) = 1."""
    r = np.exp(np.linspace(np.log(1e-4), np.log(40.0), Nr)); th = np.linspace(0, np.pi / 2, Nt + 1)
    X = r[:, None] * np.cos(th)[None, :]; Y = r[:, None] * np.sin(th)[None, :]; R2 = X ** 2 + Y ** 2
    fx = X * Y * (12 - 4 * R2) * np.exp(-R2)
    inv = ModalInverse(r, th, p=6)
    psi, dpsi, c = inv.solve(fx)
    V = inv.velocity()
    psi_ex = X * Y * np.exp(-R2)
    Ux_ex = -X * np.exp(-R2) * (1 - 2 * Y ** 2); Uy_ex = Y * np.exp(-R2) * (1 - 2 * X ** 2)
    sel = r < 10
    print("gaussian test: c - 1 =", c - 1, " max|psi err| =", np.abs(V["psi"] - psi_ex)[sel].max(),
          " max|U err| =", max(np.abs(V["Ux"] - Ux_ex)[sel].max(), np.abs(V["Uy"] - Uy_ex)[sel].max()))


def test_powerlaw(Nr=12000, Nt=64, k=0.17936053129375418, Rmax=1e7):
    """psi = x y (1+r^2)^{a}, a = (k-1)/2 (growth r^{k+1}); d_x rho = -Lap psi = -x y [Lap phi + 8 a (1+r^2)^{a-1}],
    Lap phi = 4a(1+r^2)^{a-1} + 4a(a-1) r^2 (1+r^2)^{a-2}. psi_xy(0) = 1."""
    a = (k - 1) / 2
    r = np.exp(np.linspace(np.log(1e-4), np.log(Rmax), Nr)); th = np.linspace(0, np.pi / 2, Nt + 1)
    X = r[:, None] * np.cos(th)[None, :]; Y = r[:, None] * np.sin(th)[None, :]; R2 = X ** 2 + Y ** 2
    lap_phi = 4 * a * (1 + R2) ** (a - 1) + 4 * a * (a - 1) * R2 * (1 + R2) ** (a - 2)
    fx = -X * Y * (lap_phi + 8 * a * (1 + R2) ** (a - 1))
    inv = ModalInverse(r, th, p=6, tail_powers=[k - 1, 2 * k - 2, k - 3, 2 * k - 4], k=k)
    psi, dpsi, c = inv.solve(fx)
    V = inv.velocity()
    psi_ex = X * Y * (1 + R2) ** a
    phi = (1 + R2) ** a; phir = 2 * a * (1 + R2) ** (a - 1)
    psix_ex = Y * phi + X * Y * phir * X; psiy_ex = X * phi + X * Y * phir * Y
    Ux_ex = -psiy_ex; Uy_ex = psix_ex
    for rc in (0.1, 1.0, 10.0, 100.0, 1e3, 1e4, 1e5):
        i = np.argmin(np.abs(r - rc))
        scale = np.abs(Ux_ex[i]).max() + np.abs(Uy_ex[i]).max()
        print("  r=%.0e  rel U err %.2e   rel psi err %.2e" % (r[i], max(np.abs(V["Ux"][i] - Ux_ex[i]).max(), np.abs(V["Uy"][i] - Uy_ex[i]).max()) / scale,
              np.abs(V["psi"][i] - psi_ex[i]).max() / np.abs(psi_ex[i]).max()))
    print("powerlaw test: c - 1 =", c - 1)


if __name__ == "__main__":
    import time
    t0 = time.time(); test_gaussian(); print("  %.1fs" % (time.time() - t0))
    t0 = time.time(); test_powerlaw(); print("  %.1fs" % (time.time() - t0))
