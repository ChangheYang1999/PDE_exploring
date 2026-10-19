"""
green_inverse.py -- independent evaluation of the class-S per-mode full-plane inverse by product integration
of the Green-function formulas (no differentiation matrices, no ODE collocation):

  n = |m| >= 1:  psi_m = (Z + Y)/(2n),   psi_m' = (Y - Z)/(2r),
     Z(r) = r^{-n} int_0^r t^{n+1} f_m dt,
     Y(r) = r^{ n} int_r^R t^{1-n} f_m dt + r^n I_tail        (Robin / decaying modes, |m| >= 2)
     Y(r) = - r^{n} int_0^r t^{1-n} f_m dt                    (renormalised modes |m| = 1: removes U(0))
  n = 0:         psi_0' = -(1/r) int_0^r t f_0 dt  (= -Re rho_1(r)),  psi_0 itself not needed.
With f_m = r^kappa g_m (g_m smooth in xi) and the substitutions t = r e^{-u} (inner) / t = r e^{u} (outer):
     Z = r^{2+kappa} int_0^inf  e^{-(n+2+kappa) u} g_m(r e^{-u}) du
     Y = r^{2+kappa} int_0^{U}  e^{(2+kappa-n) u}  g_m(r e^{u})  du,  U = log(R/r)      (Robin)
     Y = -r^{2+kappa} int_0^inf e^{(n-2-kappa) u}  g_m(r e^{-u}) du                      (renormalised, n <= kappa)
g_m at off-node points is the barycentric interpolant in xi.  Composite Gauss-Legendre rules in u.
All quadrature operators are precomputed as dense [Nr x Nr] matrices per mode (batched on the GPU).
"""
import math
import numpy as np
import torch
from ipm2polar import Disc, bary_weights


def gauss_legendre(n, a, b):
    x, w = np.polynomial.legendre.leggauss(n)
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w


class GreenInverse:
    def __init__(self, d: Disc, nq=48):
        self.d = d
        dev = d.dev
        Nr, M = d.Nr, d.M
        r = d.r_np
        L = d.L
        xnodes = d.x
        wb = bary_weights(xnodes)
        self.Z = np.zeros((M + 1, Nr, Nr))
        self.Y = np.zeros((M + 1, Nr, Nr))
        self.tailpow = np.zeros((M + 1, Nr))      # r^n multiplying I_tail
        for mm in range(M + 1):
            n = mm
            kap = d._kappa(mm)
            # ---- inner integral Z: u in [0, inf), rate a = n + 2 + kap >= 2
            a = n + 2 + kap
            umax = 40.0 / a
            us, ws = [], []
            # composite: [0, 2/a], [2/a, 8/a], [8/a, umax]
            for (ua, ub) in ((0.0, 2.0 / a), (2.0 / a, 8.0 / a), (8.0 / a, umax)):
                uu, ww = gauss_legendre(nq, ua, ub)
                us.append(uu); ws.append(ww)
            u = np.concatenate(us); w = np.concatenate(ws)
            fac = w * np.exp(-a * u)                               # [nq_tot]
            t = r[:, None] * np.exp(-u[None, :])                   # [Nr, nq]
            xi_t = np.log1p(t ** 2 / L ** 2)
            x_t = 2.0 * xi_t / d.xi_max - 1.0
            P = self._interp_matrix(x_t, xnodes, wb)               # [Nr, nq, Nr]
            self.Z[mm] = (r[:, None] ** (2 + kap)) * np.einsum("q,jqk->jk", fac, P)
            # ---- outer integral Y
            if mm in d.renorm_modes:
                if n == 0:
                    continue                                       # psi_0 not needed
                b = n - 2 - kap                                    # rate: integrand e^{b u}, b <= -2
                a2 = -b
                umax = 40.0 / a2
                us, ws = [], []
                for (ua, ub) in ((0.0, 2.0 / a2), (2.0 / a2, 8.0 / a2), (8.0 / a2, umax)):
                    uu, ww = gauss_legendre(nq, ua, ub)
                    us.append(uu); ws.append(ww)
                u = np.concatenate(us); w = np.concatenate(ws)
                fac = -w * np.exp(b * u)
                t = r[:, None] * np.exp(-u[None, :])
                xi_t = np.log1p(t ** 2 / L ** 2)
                x_t = 2.0 * xi_t / d.xi_max - 1.0
                P = self._interp_matrix(x_t, xnodes, wb)
                self.Y[mm] = (r[:, None] ** (2 + kap)) * np.einsum("q,jqk->jk", fac, P)
            else:
                # u in [0, U_j], U_j = log(R / r_j); integrand e^{(2+kap-n) u}; split near 0 when decaying fast
                c = 2 + kap - n
                Yrow = np.zeros((Nr, Nr))
                for j in range(Nr):
                    U = math.log(d.R / r[j])
                    if U <= 0:
                        continue
                    if c < -1:
                        u1 = min(U, 6.0 / (-c)); u2 = min(U, 24.0 / (-c))
                        segs = [(0.0, u1)]
                        if u2 > u1: segs.append((u1, u2))
                        if U > u2: segs.append((u2, U))
                    else:
                        segs = [(0.0, U / 2), (U / 2, U)]
                    us, ws = [], []
                    for (ua, ub) in segs:
                        uu, ww = gauss_legendre(nq, ua, ub)
                        us.append(uu); ws.append(ww)
                    u = np.concatenate(us); w = np.concatenate(ws)
                    fac = w * np.exp(c * u)
                    t = r[j] * np.exp(u)
                    t = np.minimum(t, d.R)
                    xi_t = np.log1p(t ** 2 / L ** 2)
                    x_t = np.minimum(2.0 * xi_t / d.xi_max - 1.0, 1.0)
                    Pj = self._interp_matrix(x_t[None, :], xnodes, wb)[0]    # [nq, Nr]
                    Yrow[j] = (r[j] ** (2 + kap)) * (fac @ Pj)
                self.Y[mm] = Yrow
                self.tailpow[mm] = r ** n
        f64 = dict(dtype=torch.float64, device=dev)
        self.Zt = torch.tensor(self.Z, **f64).to(torch.complex128)
        self.Yt = torch.tensor(self.Y, **f64).to(torch.complex128)
        self.tailpow_t = torch.tensor(self.tailpow, **f64).to(torch.complex128)
        self.n = torch.arange(M + 1, device=dev).to(torch.float64)

    @staticmethod
    def _interp_matrix(x_eval, xnodes, wb):
        """Barycentric interpolation matrices: x_eval [A, Q] -> [A, Q, Nr]."""
        diff = x_eval[..., None] - xnodes[None, None, :]
        small = np.abs(diff) < 1e-15
        diff = np.where(small, 1.0, diff)
        T = wb[None, None, :] / diff
        T = np.where(small, 0.0, T)
        S = T.sum(axis=-1, keepdims=True)
        P = T / S
        # exact hits
        hit = small.any(axis=-1)
        if hit.any():
            P[hit] = small[hit].astype(np.float64)
        return P

    def apply(self, f_m, rho_m=None, cl=None):
        """f_m: modes of d_x rho [M+1, Nr] (complex).  Returns psi_m (n>=1; psi_0 = 0), Ur_m, Ut_m on the nodes."""
        d = self.d
        g = f_m / d.rk
        Z = torch.einsum("mjk,mk->mj", self.Zt, g)
        Y = torch.einsum("mjk,mk->mj", self.Yt, g)
        if rho_m is not None and d.tail != "zero":
            Itail = d.tail_Iout(rho_m, cl)                         # [M+1]
            Y = Y + self.tailpow_t * Itail[:, None]
        r = d.r.to(torch.complex128)[None, :]
        n = self.n.to(torch.complex128)[:, None]
        psi = torch.zeros_like(Z)
        psi[1:] = (Z[1:] + Y[1:]) / (2.0 * n[1:])
        dpsi = (Y - Z) / (2.0 * r)
        dpsi[0] = -Z[0] / r[0]                                     # psi_0' = -(1/r) int_0^r t f_0 dt
        Ur = -(1j * n) * psi / r
        Ut = dpsi
        return psi, Ur, Ut
