"""
ipm1.py  --  numerics for IPM Setting I (even-x / odd-y self-similar profiles, fixed centre).

Unknowns: b(t, theta) on a compactified polar grid and the scalar c_l, with

    rho = x^2 y a,   a = w(r) b,   w(r) = (1 + r^2/L^2)^((gamma-3)/2),   gamma = 1/c_l  (target, frozen per solve)
    r(t) = L (1+t) / (1-t)^p ,  t in [-1, 1],   p = 1/(1-gamma) (default; any p >= 1 allowed)

Parity classes on the quadrant grid theta_j = (j+1/2) pi/(2M), j = 0..M-1:
    EE (even x, even y): cos(2k theta), k = 0..M-1          (a, b, U1/x, U2/y, ...)
    EO (even x, odd  y): sin((2k+1) theta), k = 0..M-1     (rho, U2)
    OO (odd  x, odd  y): sin(2k theta), k = 1..M            (psi, d_x rho)
    OE (odd  x, even y): cos((2k+1) theta), k = 0..M-1     (U1)

Full-plane Poisson inverse, mode by mode (n even >= 2):
    psi_n(r) = (1/2n) [ r^-n int_0^r s^(n+1) f_n ds + r^n int_r^infty s^(1-n) f_n ds ]
which is the unique solution regular at 0 with psi_n = o(r^n) at infinity (canonical choice, valid for
f_n = o(r^(n-2)), i.e. for rho growth gamma < 1 when n = 2).  The two integrals are obtained as solutions
of first-order ODEs collocated on a Chebyshev-Lobatto grid in t, after rescaling by W_psi = r^2 v(r),
v = (1 + r^2/L^2)^((gamma-1)/2), so that all quantities are bounded on [-1, 1].

All arrays are torch float64 tensors; layout (radial, angular) = (Nr, M).
"""
import math
import numpy as np
import torch

torch.set_default_dtype(torch.float64)


# ----------------------------------------------------------------------------------------------
# 1-D spectral tools (barycentric Lagrange on arbitrary nodes)
# ----------------------------------------------------------------------------------------------
def bary_weights(x):
    """Barycentric weights for nodes x (numpy 1-D), scaled to max |w| = 1 (log-sum for stability)."""
    x = np.asarray(x, dtype=np.float64)
    n = len(x)
    logw = np.zeros(n)
    sgn = np.ones(n)
    for j in range(n):
        d = x[j] - np.delete(x, j)
        logw[j] = -np.sum(np.log(np.abs(d)))
        sgn[j] = np.prod(np.sign(d))
    logw -= logw.max()
    return sgn * np.exp(logw)


def diff_matrix(x, w=None):
    """First-derivative collocation matrix on nodes x."""
    x = np.asarray(x, dtype=np.float64)
    if w is None:
        w = bary_weights(x)
    n = len(x)
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                D[i, j] = (w[j] / w[i]) / (x[i] - x[j])
        D[i, i] = -np.sum(D[i, :])
    return D


def interp_matrix(x, xi, w=None):
    """Matrix mapping values on nodes x to values of the interpolating polynomial at points xi."""
    x = np.asarray(x, dtype=np.float64)
    xi = np.atleast_1d(np.asarray(xi, dtype=np.float64))
    if w is None:
        w = bary_weights(x)
    P = np.zeros((len(xi), len(x)))
    for k, xx in enumerate(xi):
        d = xx - x
        hit = np.where(np.abs(d) < 1e-14)[0]
        if len(hit):
            P[k, hit[0]] = 1.0
        else:
            tmp = w / d
            P[k, :] = tmp / tmp.sum()
    return P


def cheb_lobatto(N):
    """N+1 Chebyshev-Gauss-Lobatto points in increasing order."""
    return -np.cos(np.pi * np.arange(N + 1) / N)


def cheb_radau(N):
    """N+1 Chebyshev-Gauss-Radau points including -1 (not +1), increasing."""
    return -np.cos(2.0 * np.pi * np.arange(N + 1) / (2 * N + 1))


def clenshaw_curtis_weights(N):
    """Clenshaw-Curtis weights on the N+1 Lobatto points (increasing order)."""
    if N == 0:
        return np.array([2.0])
    c = np.zeros(N + 1)
    for k in range(0, N + 1, 2):
        c[k] = 2.0 / (1.0 - k * k) if k != 1 else 0.0
    # weights via DCT: w_j = (2/N) sum_k'' c_k cos(k pi j /N)
    j = np.arange(N + 1)
    w = np.zeros(N + 1)
    for jj in j:
        s = 0.0
        for k in range(0, N + 1, 2):
            fac = 0.5 if (k == 0 or k == N) else 1.0
            s += fac * c[k] * math.cos(k * math.pi * jj / N)
        w[jj] = 2.0 * s / N
    w[0] *= 0.5
    w[-1] *= 0.5
    return w[::-1].copy() if False else w  # symmetric


# ----------------------------------------------------------------------------------------------
# angular transforms on the quadrant grid
# ----------------------------------------------------------------------------------------------
class Angular:
    """Quadrant angular grid with an optional map theta(s) = s + (beta/2) sin(2s), s_j = (j+1/2) pi/(2M).
    beta > 0 clusters the collocation angles near theta = pi/2 (theta'(pi/2) = 1 - beta). The four parity classes use
    trigonometric bases in s (parities are preserved by the map); d/dtheta = (1/theta'(s)) d/ds."""

    def __init__(self, M, device, beta=0.0):
        self.M = M
        self.dev = device
        self.beta = beta
        sj = (np.arange(M) + 0.5) * np.pi / (2 * M)
        if beta >= 0:        # cluster near theta = pi/2 only
            th = sj + 0.5 * beta * np.sin(2 * sj)
            dth = 1.0 + beta * np.cos(2 * sj)
        else:                # beta < 0: cluster near both axes with strength |beta|: theta = s - (|beta|/4) sin 4s
            bb = -beta
            th = sj - 0.25 * bb * np.sin(4 * sj)
            dth = 1.0 - bb * np.cos(4 * sj)
        self.s_np, self.theta_np, self.dtheta_ds_np = sj, th, dth
        k = np.arange(M)
        S_EE = np.cos(np.outer(sj, 2 * k)); S_EO = np.sin(np.outer(sj, 2 * k + 1))
        S_OO = np.sin(np.outer(sj, 2 * (k + 1))); S_OE = np.cos(np.outer(sj, 2 * k + 1))
        self.n_EE = 2 * k; self.n_EO = 2 * k + 1; self.n_OO = 2 * (k + 1); self.n_OE = 2 * k + 1
        T = lambda A: torch.tensor(np.asarray(A, dtype=np.float64), device=device)
        self.S = {'EE': T(S_EE), 'EO': T(S_EO), 'OO': T(S_OO), 'OE': T(S_OE)}
        self.A = {key: torch.linalg.inv(val) for key, val in self.S.items()}
        self.n = {'EE': T(self.n_EE.astype(float)), 'EO': T(self.n_EO.astype(float)),
                  'OO': T(self.n_OO.astype(float)), 'OE': T(self.n_OE.astype(float))}
        self.s = T(sj); self.theta = T(th); self.dtheta_ds = T(dth)
        self.cos = torch.cos(self.theta); self.sin = torch.sin(self.theta)
        # d/ds maps on values (class changes as before), then chain rule
        Dc = np.zeros((M, M))
        for kk in range(1, M):
            Dc[kk - 1, kk] = -2.0 * kk
        Ds = {'EE': T(S_OO @ Dc) @ self.A['EE'], 'EO': T(S_OE @ np.diag(2 * k + 1.0)) @ self.A['EO']}
        Dc = np.zeros((M, M))
        for kk in range(0, M - 1):
            Dc[kk + 1, kk] = 2.0 * (kk + 1)
        Ds['OO'] = T(S_EE @ Dc) @ self.A['OO']
        Ds['OE'] = T(S_EO @ np.diag(-(2 * k + 1.0))) @ self.A['OE']
        self.Dth = {key: (1.0 / self.dtheta_ds)[:, None] * val for key, val in Ds.items()}   # d/dtheta on values

    def s_of_theta(self, th):
        """inverse map (vectorised Newton)."""
        if self.beta == 0.0:
            return th
        s = th.clone()
        for _ in range(40):
            if self.beta >= 0:
                f = s + 0.5 * self.beta * torch.sin(2 * s) - th; df = 1.0 + self.beta * torch.cos(2 * s)
            else:
                bb = -self.beta
                f = s - 0.25 * bb * torch.sin(4 * s) - th; df = 1.0 - bb * torch.cos(4 * s)
            s = s - f / df
        return s

    def dtheta(self, F, cls):
        """F: (..., M) values in class cls -> d/dtheta values (class changes)."""
        return F @ self.Dth[cls].T

    def to_coef(self, F, cls):
        return F @ self.A[cls].T

    def to_val(self, C, cls):
        return C @ self.S[cls].T


# ----------------------------------------------------------------------------------------------
# radial grids and map
# ----------------------------------------------------------------------------------------------
class Radial:
    def __init__(self, N, L, p, device, kind='radau'):
        self.N = N
        self.L = L
        self.p = p
        self.dev = device
        tR = cheb_radau(N)
        tL = cheb_lobatto(N)
        self.tR_np, self.tL_np = tR, tL
        wR, wL = bary_weights(tR), bary_weights(tL)
        T = lambda A: torch.tensor(np.asarray(A, dtype=np.float64), device=device)
        self.DR = T(diff_matrix(tR, wR))
        self.DL = T(diff_matrix(tL, wL))
        self.P_RL = T(interp_matrix(tR, tL, wR))   # Radau values -> Lobatto values
        self.P_LR = T(interp_matrix(tL, tR, wL))   # Lobatto -> Radau
        self.ext1_R = T(interp_matrix(tR, [1.0], wR))   # Radau values -> value at t=1 (1 x N+1)
        self.tR, self.tL = T(tR), T(tL)
        self.rR = self.rmap(self.tR)
        self.rL = self.rmap(self.tL)           # rL[-1] = inf
        self.QR = (1 - self.tR) + p * (1 + self.tR)    # Q = (1-t^2) (dr/dt)/r
        self.QL = (1 - self.tL) + p * (1 + self.tL)
        self.ccw = T(clenshaw_curtis_weights(N))

    def rmap(self, t):
        return self.L * (1 + t) / (1 - t) ** self.p

    def drdt(self, t):
        return self.L * ((1 - t) ** self.p + self.p * (1 + t) * (1 - t) ** (self.p - 1)) / (1 - t) ** (2 * self.p)


# ----------------------------------------------------------------------------------------------
# the model
# ----------------------------------------------------------------------------------------------
class IPM1:
    """
    Discretisation of Setting I on the compactified polar grid.
    gamma is the frozen far-field exponent used in the weights (target gamma = 1/c_l);
    p is the map power (default 1/(1-gamma)).
    """

    def __init__(self, N=64, M=16, L=1.0, gamma=0.5, p=None, device='cpu', inverse='canonical', gauge_c=None, beta=0.0, M2=None):
        self.dev = torch.device(device)
        self.N, self.M, self.L = N, M, L
        self.gamma = gamma
        self.beta = beta
        if p is None:
            p = 1.0 / (1.0 - gamma) if gamma < 1 else 2.0
        self.p = p
        self.inverse = inverse      # 'canonical' or 'renormalised' (mode 2 subtracted, gauge_c * (-x, y) added)
        self.gauge_c = gauge_c
        self.ang = Angular(M, self.dev, beta=beta)
        self.M2 = (M + 2 if beta == 0.0 else 4 * M) if M2 is None else M2   # fine angular grid for products / Poisson source
        self.angf = Angular(self.M2, self.dev, beta=beta)
        # theta-Fourier modes kept for psi: all M2 (exact, beta = 0) or the lower half (quadrature, beta != 0)
        self.nmodes = self.M2 if beta == 0.0 else self.M2 // 2
        self.nf = self.angf.n['OO'][:self.nmodes]
        self.rad = Radial(N, L, p, self.dev)
        self._angular_maps()
        self._weights()
        self._poisson_setup()

    # ---- weight functions ------------------------------------------------------------------
    def _weights(self):
        L, g = self.L, self.gamma
        rR, rL = self.rad.rR, self.rad.rL
        tL = self.rad.tL
        self.s2R = rR ** 2 / (L ** 2 + rR ** 2)                  # r^2/(L^2+r^2) on Radau
        s2L = torch.where(torch.isfinite(rL), rL ** 2 / (L ** 2 + rL ** 2), torch.ones_like(rL))
        self.s2L = s2L
        self.wR = (1 + rR ** 2 / L ** 2) ** ((g - 3) / 2)        # w on Radau
        self.vR = (1 + rR ** 2 / L ** 2) ** ((g - 1) / 2)        # v on Radau
        self.omegaR = (g - 3) * self.s2R                         # r w'/w
        self.omegaL = (g - 3) * s2L
        # lim v/(1-t) etc. not needed on Radau
        # Lobatto quantities with r = inf handled: r^2 F/(1+r^2/L^2) -> L^2 F
        self.rr_over_1pr2_L = torch.where(torch.isfinite(rL), rL ** 2 / (1 + rL ** 2 / L ** 2),
                                          torch.full_like(rL, L ** 2))
        self.r_over_1pr2_R = rR / (1 + rR ** 2 / L ** 2)

    # ---- coarse <-> fine angular maps ------------------------------------------------------
    def _angular_maps(self):
        ang, angf = self.ang, self.angf
        sf = angf.s
        k = torch.arange(self.M, device=self.dev, dtype=torch.float64)
        S_EE_f = torch.cos(sf[:, None] * (2 * k)[None, :])
        D_EE_f = -(2 * k)[None, :] * torch.sin(sf[:, None] * (2 * k)[None, :])
        self.T_cf = (S_EE_f @ ang.A['EE'])                                   # coarse EE values -> fine values
        self.Td_cf = ((1.0 / angf.dtheta_ds)[:, None] * D_EE_f) @ ang.A['EE']   # coarse EE values -> fine d/dtheta values
        # Poisson source analysis on the fine grid: theta-Fourier sine modes n = 2..2 M2 by quadrature in s
        nf = self.nf
        thf = angf.theta
        if self.beta == 0.0:
            self.Aq_OO = angf.A['OO']                                         # exact inverse (midpoint grid), all M2 modes
        else:
            ds = math.pi / (2 * self.M2)
            self.Aq_OO = (4.0 / math.pi) * ds * torch.sin(nf[:, None] * thf[None, :]) * angf.dtheta_ds[None, :]   # (nmodes x M2)
        # fine modes -> coarse-grid values of psi~ and d/dtheta psi~ (theta-harmonics at the mapped coarse angles)
        thc = ang.theta
        self.S_OO_fc = torch.sin(thc[:, None] * nf[None, :])
        self.Sd_OO_fc = nf[None, :] * torch.cos(thc[:, None] * nf[None, :])

    # ---- Poisson ODE matrices --------------------------------------------------------------
    def _poisson_setup(self):
        """Build and factor, for each even n, the Lobatto collocation matrices for
        I1~ and I2~ (rescaled by W_psi = r^2 v)."""
        N, g, p = self.N, self.gamma, self.p
        tL = self.rad.tL
        DL = self.rad.DL
        Q = self.rad.QL
        s2 = self.s2L
        one_m_t2 = 1 - tL ** 2
        # (1-t^2) d/dt  - diag(coef) applied to I~
        # I1:  (1-t^2) I1' = I1 [ -nQ - 2Q - (g-1) Q s2 ] + Q * rr_over_1pr2 * F_n
        # I2:  (1-t^2) I2' = I2 [  nQ - 2Q - (g-1) Q s2 ] - Q * rr_over_1pr2 * F_n
        self.modes = np.asarray(self.angf.n_OO)[:self.nmodes]  # theta-harmonics kept
        A1, A2 = [], []
        base = one_m_t2[:, None] * DL
        for n in self.modes:
            c1 = -n * Q - 2 * Q - (g - 1) * Q * s2
            c2 = n * Q - 2 * Q - (g - 1) * Q * s2
            M1 = base - torch.diag(c1)
            M2 = base - torch.diag(c2)
            if n == 2 and self.inverse == 'canonical':
                # row t=-1 is vacuous for I2 (coefficient -> 0): replace by divided form: 2 I2'(-1) = 0
                M2[0, :] = 2.0 * DL[0, :]
            A1.append(M1)
            A2.append(M2)
        self.A1 = torch.stack(A1)   # (M, N+1, N+1)
        self.A2 = torch.stack(A2)
        self.LU1 = torch.linalg.lu_factor(self.A1)
        self.LU2 = torch.linalg.lu_factor(self.A2)
        self.rhs_scale = Q * self.rr_over_1pr2_L     # (N+1,)

    def poisson_modes(self, Fhat_L):
        """
        Fhat_L: (N+1, M) values on Lobatto grid of F^ = f/(r^2 w) in class OO (sin n theta, n even).
        Returns Psi~ (N+1, M) values on Lobatto grid of psi/(r^2 v), class OO.
        """
        C = Fhat_L @ self.Aq_OO.T                     # (..., N+1, M2) theta-Fourier mode coefficients F^_n(t) (fine grid input)
        rhs = self.rhs_scale[:, None] * C             # (..., N+1, M)
        shp = rhs.shape
        R = rhs.reshape(-1, shp[-2], shp[-1]).permute(2, 1, 0)   # (M, N+1, B)
        R1 = R.clone()
        R2 = -R.clone()
        # boundary rows: for I1 row t=-1 has rhs 0 automatically (rhs_scale(-1)=0 since r=0). For I2 n=2 row t=-1 -> 0.
        if self.inverse == 'canonical':
            R2[0, 0, :] = 0.0
        I1 = torch.linalg.lu_solve(*self.LU1, R1).permute(2, 1, 0).reshape(shp)   # (..., N+1, M)
        I2 = torch.linalg.lu_solve(*self.LU2, R2).permute(2, 1, 0).reshape(shp)
        n = self.nf
        PsiC = (I1 + I2) / (2 * n)[None, :]
        return PsiC @ torch.sin(self.angf.theta[:, None] * n[None, :]).T, PsiC

    # ---- fields from b --------------------------------------------------------------------
    def fields(self, b):
        """
        b: (..., N+1, M) on the Radau grid, class EE.  Dealiased pipeline:
          b -> fine angular grid (M2 = M+2 points, exact) -> P = cos^2 sin b, P_r, P_theta (product rule, exact)
          -> F^ = d_x rho/(r^2 w) on the fine grid (exact pointwise; has <= M+1 odd modes, represented exactly by M2)
          -> Poisson modes n = 2..2M2 -> psi~ mode functions (Lobatto) -> psi~, r psi~_r, psi~_theta evaluated pointwise
          on the coarse grid -> U^ fields (exact pointwise for the represented b).
        Returns dict with Uhat1 (OE), Uhat2 (EO), Ur_over_r, Uth_over_r, coefU (EE) on the coarse Radau grid,
        PsiC (fine mode coefficients on Lobatto, (..., N+1, M2)), Psi_L (fine-grid values), Fhat_L (fine grid), bL.
        """
        ang, angf, rad = self.ang, self.angf, self.rad
        cosf, sinf = angf.cos[None, :], angf.sin[None, :]
        bL = rad.P_RL @ b                                              # Lobatto, coarse angular
        bLf = bL @ self.T_cf.T                                         # fine angular values
        bLf_th = bL @ self.Td_cf.T                                     # d/dtheta on the fine grid
        P_L = cosf ** 2 * sinf * bLf                                   # rho/(r^3 w)
        rP_r = ((1 - rad.tL ** 2) / rad.QL)[..., :, None] * (rad.DL @ bLf) * cosf ** 2 * sinf
        P_th = (cosf ** 3 - 2 * cosf * sinf ** 2) * bLf + cosf ** 2 * sinf * bLf_th
        Fhat_L = cosf * ((3 + self.omegaL)[..., :, None] * P_L + rP_r) - sinf * P_th     # fine OO, exact pointwise
        Psi_Lf, PsiC = self.poisson_modes(Fhat_L)                      # PsiC: (..., N+1, M2)
        # mode functions on Radau and their r-derivative, then pointwise evaluation on the coarse grid
        PsiC_R = rad.P_LR @ PsiC                                        # (..., N+1, M2)
        rPsiC_r = ((1 - rad.tR ** 2) / rad.QR)[..., :, None] * (rad.DR @ PsiC_R)
        Psi = PsiC_R @ self.S_OO_fc.T                                   # psi~ on coarse grid
        rPsi_r = rPsiC_r @ self.S_OO_fc.T
        Psi_th = PsiC_R @ self.Sd_OO_fc.T
        cos, sin = ang.cos[None, :], ang.sin[None, :]
        G = (2 + (self.gamma - 1) * self.s2R)[..., :, None] * Psi + rPsi_r     # r psi_r /(r^2 v)
        Uhat1 = -(sin * G + cos * Psi_th)       # U1 / (r v), class OE
        Uhat2 = cos * G - sin * Psi_th          # U2 / (r v), class EO
        if self.inverse == 'renormalised':
            c = self.gauge_c
            Uhat1 = Uhat1 - c * cos / self.vR[..., :, None]
            Uhat2 = Uhat2 + c * sin / self.vR[..., :, None]
        v = self.vR[..., :, None]
        Ur_over_r = v * (Uhat1 * cos + Uhat2 * sin)
        Uth_over_r = v * (-Uhat1 * sin + Uhat2 * cos)
        coefU = v * (2 * Uhat1 / cos + Uhat2 / sin)
        return dict(Uhat1=Uhat1, Uhat2=Uhat2, Ur_over_r=Ur_over_r, Uth_over_r=Uth_over_r, coefU=coefU,
                    Psi_L=Psi_Lf, PsiC=PsiC, PsiC_R=PsiC_R, rPsiC_r=rPsiC_r, Fhat_L=Fhat_L, bL=bL)

    def residual(self, b, cl, flds=None):
        """E[b] on the Radau grid (all rows, including t=-1 where it degenerates)."""
        if flds is None:
            flds = self.fields(b)
        rad, ang = self.rad, self.ang
        b_t = rad.DR @ b
        rb_r = ((1 - rad.tR ** 2) / rad.QR)[:, None] * b_t
        b_th = ang.dtheta(b, 'EE')
        A0 = (cl * self.omegaR)[:, None] + flds['Ur_over_r'] * self.omegaR[:, None] + (3 * cl - 1) + flds['coefU']
        E = (cl + flds['Ur_over_r']) * rb_r + flds['Uth_over_r'] * b_th + A0 * b
        return E

    def psi_xy0(self, flds):
        """c = psi_xy(0) from the mode-2 coefficient: psi ~ (c/2) r^2 sin 2theta, psi/(r^2 v) -> c/2 at t=-1."""
        PsiC = flds['PsiC']
        return 2.0 * PsiC[..., 0, 0]

    # ---- helpers ---------------------------------------------------------------------------
    def xy(self):
        r = self.rad.rR[:, None]
        return r * self.ang.cos[None, :], r * self.ang.sin[None, :]

    def rho_from_b(self, b):
        """rho = r^3 w cos^2 sin b on Radau grid."""
        r = self.rad.rR[:, None]
        return r ** 3 * self.wR[:, None] * self.ang.cos[None, :] ** 2 * self.ang.sin[None, :] * b

    def velocity(self, flds):
        """U1, U2 on the Radau grid (actual, unscaled)."""
        rv = (self.rad.rR * self.vR)[:, None]
        return rv * flds['Uhat1'], rv * flds['Uhat2']

    def psi(self, flds):
        """psi on the coarse Radau grid."""
        Psi = flds['PsiC_R'] @ self.S_OO_fc.T
        return (self.rad.rR ** 2 * self.vR)[:, None] * Psi

    def psi_tilde_coarse(self, flds):
        """psi~ = psi/(r^2 v) and its theta-derivative on the coarse Radau grid."""
        return flds['PsiC_R'] @ self.S_OO_fc.T, flds['PsiC_R'] @ self.Sd_OO_fc.T
