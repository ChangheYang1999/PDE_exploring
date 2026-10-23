"""
ipm3.py -- numerics for IPM Setting III: the y-leading (nondegenerate axis) branch of the full-plane
even-x / odd-y self-similar profile problem

    (c_l X + U) . grad rho = rho,   U = (-psi_y, psi_x),   -Laplace psi = d_x rho   on R^2,
    rho even in x, odd in y;  psi odd in x and in y;  U = o(|X|)  (canonical full-plane velocity law).

Representation (written independently of the Setting I code, same architecture):

    rho = y w(r) b(r, theta),   w(r) = (1 + r^2/L^2)^((gamma-1)/2),   gamma = frozen far-field exponent (target 1/c_l)
    r(t) = L (1+t)/(1-t)^p,  t in [-1, 1],  p = 1/(1-gamma)  (so r^(gamma-1) ~ (1-t) near t = 1)

b is even in x and y, bounded on the closed compactified plane, b(0, theta) = a_0 := rho_y(0,0).
Profile equation divided by y w (omega = r w'/w = (gamma-1) r^2/(L^2+r^2)):

    E[b] = (c_l + U_r/r) r b_r + (U_theta/r) b_theta + [c_l - 1 + U_2/y + (c_l + U_r/r) omega] b = 0.

At r = 0 this reads (c_l - 1 + c) a_0 = 0 with c = psi_xy(0): the origin identity c_l + c = 1.

Angular classes on the quadrant grid theta_j = (j+1/2) pi/(2M), j = 0..M-1:
    EE: cos(2k theta)        (b, U_r/r, U_2/y)
    EO: sin((2k+1) theta)    (rho, U_2)
    OO: sin(2(k+1) theta)    (psi, d_x rho, U_theta/r, b_theta)
    OE: cos((2k+1) theta)    (U_1)

Canonical inverse, mode by mode (n even >= 2), f_n = sin(n theta) coefficient of d_x rho:
    psi_n(r) = (1/2n) [ r^-n int_0^r s^(n+1) f_n ds + r^n int_r^inf s^(1-n) f_n ds ],
the unique solution regular at 0 with psi_n = o(r^n) at infinity.  With d_x rho = w Fhat, Fhat in class OO,
and psi = r^2 v Psi~ (v = w), the two integrals I1, I2 rescaled as I = r^2 v I~ solve

    r dI1~/dr = -(n + 2 + omega) I1~ + Fhat_n,      I1~(0) = 0,
    r dI2~/dr =  (n - 2 - omega) I2~ - Fhat_n,      I2~ bounded at infinity (this is the gauge condition),
    Psi~_n = (I1~ + I2~)/(2n),   c = psi_xy(0) = 2 Psi~_2(0) = I2~_2(0)/2.

These are collocated in t on a Chebyshev-Lobatto grid (both ends included; t = 1 is r = infinity where the ODE row
is the algebraic far-field relation).  b lives on a Chebyshev-Radau grid (t = -1 included, t = 1 not).
"""
import math
import numpy as np
import torch

torch.set_default_dtype(torch.float64)


# ------------------------------------------------------------------------------------------------
# 1-D spectral tools (barycentric Lagrange on arbitrary nodes)
# ------------------------------------------------------------------------------------------------
def bary_weights(x):
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
    x = np.asarray(x, dtype=np.float64)
    xi = np.atleast_1d(np.asarray(xi, dtype=np.float64))
    if w is None:
        w = bary_weights(x)
    P = np.zeros((len(xi), len(x)))
    for k, xx in enumerate(xi):
        d = xx - x
        hit = np.where(np.abs(d) < 1e-15)[0]
        if len(hit):
            P[k, hit[0]] = 1.0
        else:
            tmp = w / d
            P[k, :] = tmp / tmp.sum()
    return P


def cheb_lobatto(N):
    return -np.cos(np.pi * np.arange(N + 1) / N)


def cheb_radau(N):
    """N+1 points including -1, excluding +1, increasing."""
    return -np.cos(2.0 * np.pi * np.arange(N + 1) / (2 * N + 1))


def gauss_legendre(n):
    x, w = np.polynomial.legendre.leggauss(n)
    return x, w


# ------------------------------------------------------------------------------------------------
# angular transforms on the quadrant grid
# ------------------------------------------------------------------------------------------------
class Angular:
    def __init__(self, M, device):
        self.M = M
        self.dev = device
        th = (np.arange(M) + 0.5) * np.pi / (2 * M)
        self.theta_np = th
        k = np.arange(M)
        self.n_EE = 2 * k
        self.n_EO = 2 * k + 1
        self.n_OO = 2 * (k + 1)
        self.n_OE = 2 * k + 1
        S_EE = np.cos(np.outer(th, self.n_EE))
        S_EO = np.sin(np.outer(th, self.n_EO))
        S_OO = np.sin(np.outer(th, self.n_OO))
        S_OE = np.cos(np.outer(th, self.n_OE))
        T = lambda A: torch.tensor(np.asarray(A, dtype=np.float64), device=device)
        self.S = {'EE': T(S_EE), 'EO': T(S_EO), 'OO': T(S_OO), 'OE': T(S_OE)}
        self.A = {key: torch.linalg.inv(val) for key, val in self.S.items()}
        self.theta = T(th)
        self.cos = torch.cos(self.theta)
        self.sin = torch.sin(self.theta)
        # d/dtheta on values: EE -> OO, OO -> EE, EO -> OE, OE -> EO
        Dc = np.zeros((M, M))
        for kk in range(1, M):
            Dc[kk - 1, kk] = -2.0 * kk            # d cos(2k th) = -2k sin(2k th): EE coef k -> OO coef k-1
        D_EE = T(S_OO @ Dc) @ self.A['EE']
        Dc = np.zeros((M, M))
        for kk in range(0, M - 1):
            Dc[kk + 1, kk] = 2.0 * (kk + 1)       # d sin(2(k+1) th) = 2(k+1) cos(2(k+1) th): OO coef k -> EE coef k+1
        # (the top mode cos(2M theta) vanishes on the grid, so dropping it is exact on the grid)
        D_OO = T(S_EE @ Dc) @ self.A['OO']
        D_EO = T(S_OE @ np.diag(2 * k + 1.0)) @ self.A['EO']
        D_OE = T(S_EO @ np.diag(-(2 * k + 1.0))) @ self.A['OE']
        self.D = {'EE': D_EE, 'OO': D_OO, 'EO': D_EO, 'OE': D_OE}

    def dtheta(self, F, cls):
        return F @ self.D[cls].T

    def to_coef(self, F, cls):
        return F @ self.A[cls].T

    def to_val(self, C, cls):
        return C @ self.S[cls].T


# ------------------------------------------------------------------------------------------------
# radial grid and compactification map
# ------------------------------------------------------------------------------------------------
class Radial:
    def __init__(self, N, L, p, device):
        self.N, self.L, self.p, self.dev = N, L, p, device
        tR = cheb_radau(N)
        tL = cheb_lobatto(N)
        self.tR_np, self.tL_np = tR, tL
        self.wR_np, self.wL_np = bary_weights(tR), bary_weights(tL)
        T = lambda A: torch.tensor(np.asarray(A, dtype=np.float64), device=device)
        self.DR = T(diff_matrix(tR, self.wR_np))
        self.DL = T(diff_matrix(tL, self.wL_np))
        self.P_RL = T(interp_matrix(tR, tL, self.wR_np))    # Radau values -> Lobatto values
        self.P_LR = T(interp_matrix(tL, tR, self.wL_np))    # Lobatto -> Radau
        self.ext1_R = T(interp_matrix(tR, [1.0], self.wR_np))   # Radau values -> value at t = 1
        self.tR, self.tL = T(tR), T(tL)
        self.rR = self.rmap(self.tR)
        self.QR = (1 - self.tR) + p * (1 + self.tR)          # Q = (1-t^2) (dr/dt)/r
        self.QL = (1 - self.tL) + p * (1 + self.tL)
        self.gR = (1 - self.tR ** 2) / self.QR               # r d/dr = g d/dt
        self.gL = (1 - self.tL ** 2) / self.QL
        # s^2 = r^2/(L^2 + r^2) computed from t directly (finite at t = 1)
        self.s2R = self.s2_of_t(self.tR)
        self.s2L = self.s2_of_t(self.tL)

    def rmap(self, t):
        return self.L * (1 + t) / (1 - t) ** self.p

    def s2_of_t(self, t):
        a = (1 + t) ** 2
        c = (1 - t) ** (2 * self.p)
        return a / (a + c)

    def one_minus_s2_of_t(self, t):
        """1 - s^2 = L^2/(L^2 + r^2) computed without cancellation near t = 1."""
        a = (1 + t) ** 2
        c = (1 - t) ** (2 * self.p)
        return c / (a + c)

    def w_of_t(self, t, gamma):
        """w = (1 + r^2/L^2)^((gamma-1)/2) = (1 - s^2)^((1-gamma)/2), cancellation-free."""
        return self.one_minus_s2_of_t(t) ** ((1 - gamma) / 2)

    def t_of_r(self, r):
        """inverse map by bisection (numpy)."""
        r = np.atleast_1d(np.asarray(r, dtype=np.float64))
        lo = -np.ones_like(r)
        hi = np.ones_like(r) - 1e-16
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            rm = self.L * (1 + mid) / (1 - mid) ** self.p
            big = rm > r
            hi = np.where(big, mid, hi)
            lo = np.where(big, lo, mid)
        return 0.5 * (lo + hi)


# ------------------------------------------------------------------------------------------------
# the model
# ------------------------------------------------------------------------------------------------
class IPM3:
    def __init__(self, N=64, M=16, L=1.0, gamma=0.6, p=None, device='cpu', M2=None, couple_gamma=False):
        self.dev = torch.device(device)
        self.N, self.M, self.L, self.gamma = N, M, L, gamma
        if p is None:
            p = 1.0 / (1.0 - gamma)
        self.p = p
        self.couple_gamma = couple_gamma      # if True, system() and jacobian() use gamma = 1/c_l (p stays fixed)
        self.ang = Angular(M, self.dev)
        self.M2 = M + 2 if M2 is None else M2
        self.angf = Angular(self.M2, self.dev)
        self.rad = Radial(N, L, p, self.dev)
        self._weights()
        self._angular_maps()
        self._poisson_setup()

    def set_gamma(self, gamma):
        """Change the far-field exponent in w, omega, v and the Poisson matrices (grid and p unchanged)."""
        if gamma != self.gamma:
            self.gamma = gamma
            self._weights()
            self._poisson_setup()

    # ---- weights --------------------------------------------------------------------------------
    def _weights(self):
        g = self.gamma
        rad = self.rad
        self.omegaR = (g - 1) * rad.s2R                 # r w'/w on Radau
        self.omegaL = (g - 1) * rad.s2L
        self.wR = rad.w_of_t(rad.tR, g)                 # w = v = (1 + r^2/L^2)^((g-1)/2) on Radau (cancellation-free)
        self.vR = self.wR

    # ---- coarse <-> fine angular maps ----------------------------------------------------------
    def _angular_maps(self):
        ang, angf = self.ang, self.angf
        thf = angf.theta
        k = torch.tensor(self.ang.n_EE, dtype=torch.float64, device=self.dev)
        S_EE_f = torch.cos(thf[:, None] * k[None, :])
        D_EE_f = -k[None, :] * torch.sin(thf[:, None] * k[None, :])
        self.T_cf = S_EE_f @ ang.A['EE']                # coarse EE values -> fine values
        self.Td_cf = D_EE_f @ ang.A['EE']               # coarse EE values -> fine d/dtheta values
        self.nf = torch.tensor(angf.n_OO, dtype=torch.float64, device=self.dev)   # modes 2, 4, ..., 2 M2
        thc = ang.theta
        self.S_OO_fc = torch.sin(thc[:, None] * self.nf[None, :])      # fine modes -> coarse values
        self.Sd_OO_fc = self.nf[None, :] * torch.cos(thc[:, None] * self.nf[None, :])

    # ---- Poisson ODE matrices (Lobatto collocation) ---------------------------------------------
    def _poisson_setup(self):
        rad = self.rad
        tL, DL, Q, om = rad.tL, rad.DL, rad.QL, self.omegaL
        base = (1 - tL ** 2)[:, None] * DL
        A1, A2 = [], []
        self.modes = np.asarray(self.angf.n_OO)
        for n in self.modes:
            n = float(n)
            M1 = base + torch.diag(Q * (n + 2 + om))      # (1-t^2) I1' + Q (n+2+om) I1 = Q Fhat_n
            M2 = base - torch.diag(Q * (n - 2 - om))      # (1-t^2) I2' - Q (n-2-om) I2 = -Q Fhat_n
            if n == 2.0:
                M2[0, :] = DL[0, :]                      # regularity row at t = -1 (row otherwise vacuous)
            A1.append(M1)
            A2.append(M2)
        self.A1 = torch.stack(A1)
        self.A2 = torch.stack(A2)
        self.LU1 = torch.linalg.lu_factor(self.A1)
        self.LU2 = torch.linalg.lu_factor(self.A2)

    def poisson_modes(self, Fhat_L):
        """Fhat_L: (..., N+1, M2) values on the Lobatto x fine-angular grid of Fhat = d_x rho / w (class OO).
        Returns PsiC (..., N+1, M2): Lobatto values of the mode functions Psi~_n(t), n = 2, 4, ..., 2 M2."""
        C = Fhat_L @ self.angf.A['OO'].T                 # (..., N+1, M2) mode coefficients
        rhs = self.rad.QL[:, None] * C
        shp = rhs.shape
        R = rhs.reshape(-1, shp[-2], shp[-1]).permute(2, 1, 0)      # (M2, N+1, B)
        R1 = R.clone()
        R2 = -R.clone()
        R2[0, 0, :] = 0.0                                             # n = 2 regularity row
        I1 = torch.linalg.lu_solve(*self.LU1, R1).permute(2, 1, 0).reshape(shp)
        I2 = torch.linalg.lu_solve(*self.LU2, R2).permute(2, 1, 0).reshape(shp)
        PsiC = (I1 + I2) / (2 * self.nf)
        return PsiC, I1, I2

    # ---- fields from b ---------------------------------------------------------------------------
    def fields(self, b):
        """b: (..., N+1, M) Radau values, class EE.  Returns the velocity-derived fields on the coarse Radau grid:
        Ur_r = U_r/r (EE), Uth_r = U_theta/r (OO), U2y = U_2/y (EE), plus mode data."""
        rad, ang, angf = self.rad, self.ang, self.angf
        cosf, sinf = angf.cos[None, :], angf.sin[None, :]
        bL = rad.P_RL @ b                                   # Lobatto radial, coarse angular
        bLf = bL @ self.T_cf.T                              # fine angular values
        bLf_th = bL @ self.Td_cf.T
        P = sinf * bLf                                      # rho/(r w), class EO on the fine grid
        rP_r = rad.gL[:, None] * (rad.DL @ bLf) * sinf      # r P_r
        P_th = cosf * bLf + sinf * bLf_th
        Fhat_L = cosf * ((1 + self.omegaL)[:, None] * P + rP_r) - sinf * P_th     # d_x rho / w, class OO
        PsiC, I1, I2 = self.poisson_modes(Fhat_L)
        PsiC_R = rad.P_LR @ PsiC
        rPsiC_r = rad.gR[:, None] * (rad.DR @ PsiC_R)
        Psi = PsiC_R @ self.S_OO_fc.T                       # Psi~ on the coarse grid (OO)
        rPsi_r = rPsiC_r @ self.S_OO_fc.T
        Psi_th = PsiC_R @ self.Sd_OO_fc.T                   # (EE)
        cos, sin = ang.cos[None, :], ang.sin[None, :]
        v = self.vR[:, None]
        G = (2 + self.omegaR)[:, None] * Psi + rPsi_r       # r psi_r/(r^2 v) = psi_r/(r v)
        Ur_r = -v * Psi_th                                  # U_r/r
        Uth_r = v * G                                       # U_theta/r
        U2y = v * (G * cos / sin - Psi_th)                  # U_2/y
        Uhat1 = -(sin * G + cos * Psi_th)                   # U_1/(r v)
        Uhat2 = cos * G - sin * Psi_th                      # U_2/(r v)
        return dict(Ur_r=Ur_r, Uth_r=Uth_r, U2y=U2y, Uhat1=Uhat1, Uhat2=Uhat2, PsiC=PsiC, PsiC_R=PsiC_R,
                    rPsiC_r=rPsiC_r, Psi=Psi, Psi_th=Psi_th, Fhat_L=Fhat_L, I1=I1, I2=I2, bL=bL)

    def psi_xy0(self, flds):
        """c = psi_xy(0) = 2 Psi~_2(t = -1)."""
        return 2.0 * flds['PsiC'][..., 0, 0]

    def residual(self, b, cl, flds=None):
        """E[b] on the Radau grid (all rows; the t = -1 row is (c_l - 1 + c) b(0) when b(0, .) is constant)."""
        if flds is None:
            flds = self.fields(b)
        rad, ang = self.rad, self.ang
        rb_r = rad.gR[:, None] * (rad.DR @ b)
        b_th = ang.dtheta(b, 'EE')
        A0 = cl - 1 + flds['U2y'] + (cl + flds['Ur_r']) * self.omegaR[:, None]
        return (cl + flds['Ur_r']) * rb_r + flds['Uth_r'] * b_th + A0 * b

    def linearized(self, b, cl, delta, flds=None, dflds=None):
        """DE[b](delta) for a batch delta (..., N+1, M); dcl not included (see dE_dcl)."""
        if flds is None:
            flds = self.fields(b)
        if dflds is None:
            dflds = self.fields(delta)
        rad, ang = self.rad, self.ang
        rb_r = rad.gR[:, None] * (rad.DR @ b)
        b_th = ang.dtheta(b, 'EE')
        rd_r = rad.gR[:, None] * (rad.DR @ delta)
        d_th = ang.dtheta(delta, 'EE')
        om = self.omegaR[:, None]
        A0 = cl - 1 + flds['U2y'] + (cl + flds['Ur_r']) * om
        out = (cl + flds['Ur_r']) * rd_r + dflds['Ur_r'] * rb_r + flds['Uth_r'] * d_th + dflds['Uth_r'] * b_th \
            + A0 * delta + (dflds['U2y'] + om * dflds['Ur_r']) * b
        return out

    def dE_dcl(self, b):
        rad = self.rad
        rb_r = rad.gR[:, None] * (rad.DR @ b)
        return rb_r + (1 + self.omegaR)[:, None] * b

    # ---- full discrete system F(u) = 0, u = (b, c_l) -------------------------------------------
    # rows: i = 0: M-1 continuity rows b(0,th_j) - b(0,th_0), j = 1..M-1, and the identity row c_l - 1 + c[b];
    #       i = 1..N: E[b](t_i, th_j); last: gauge row  mean_j b(t=1, th_j) - gauge_value.
    def gauge_row(self, b, gauge_value=1.0):
        """Scalar gauge functional fixing the scaling freedom.
        gauge = 'inf' : mean_theta b(t=1) - gauge_value   (far-field amplitude; weak when gamma is close to 1)
        gauge = 'half': mean_theta b(t=0) - [b(0,0) + mean_theta b(t=1)]/2 - gauge_value  (r = L is where the mean of b
                        is halfway between its centre and far-field values; gauge_value normally 0)."""
        g = getattr(self, 'gauge', 'inf')
        if g == 'inf':
            return (self.rad.ext1_R @ b).mean() - gauge_value
        elif g == 'half':
            if not hasattr(self.rad, 'ext0_R'):
                self.rad.ext0_R = torch.tensor(interp_matrix(self.rad.tR_np, [0.0], self.rad.wR_np), device=self.dev)
            return (self.rad.ext0_R @ b).mean() - 0.5 * (b[0, 0] + (self.rad.ext1_R @ b).mean()) - gauge_value
        else:
            raise ValueError(g)

    def forcing_shape(self):
        """phi(r)/w(r) on the Radau grid for the smooth forcing mu y phi(r), phi = (1 + r^2/Lf^2)^-2 with the forcing
        width Lf (attribute self.Lf; default = the grid scale L, which reproduces the earlier runs exactly)."""
        Lf = getattr(self, 'Lf', self.L)
        if Lf == self.L:
            one_m_s2 = self.rad.one_minus_s2_of_t(self.rad.tR)
            return one_m_s2 ** (2 - (1 - self.gamma) / 2)
        r = self.rad.rR
        return (1 + r ** 2 / Lf ** 2) ** (-2) / self.wR

    def system(self, b, cl, flds=None, gauge_value=1.0, target=None, mu=None, forced=False):
        """mu is None: unknowns (b, c_l), identity row c_l - 1 + c[b] = 0.
        mu given, forced False (defect mode): c_l fixed, identity row c_l - 1 + c[b] - mu = 0 (ill-posed, kept for record).
        mu given, forced True: c_l fixed, equation (c_l X + U).grad rho - rho = mu y phi(r) with the smooth bump phi,
        i.e. E[b] = mu phi/w at every node including the centre, where E(0) = (c_l - 1 + c) b(0,0)."""
        if self.couple_gamma:
            self.set_gamma(1.0 / cl)
            flds = None
        if flds is None:
            flds = self.fields(b)
        E = self.residual(b, cl, flds)
        if target is not None:
            E = E - target
        M = self.M
        F = torch.empty((self.N + 1) * M + 1, device=self.dev)
        F[0:M - 1] = b[0, 1:] - b[0, 0]
        if mu is not None and forced:
            fs = self.forcing_shape()
            F[M - 1] = (cl - 1 + self.psi_xy0(flds)) * b[0, 0] - mu
            F[M:(self.N + 1) * M] = (E[1:] - mu * fs[1:, None]).reshape(-1)
        else:
            F[M - 1] = cl - 1 + self.psi_xy0(flds) - (0.0 if mu is None else mu)
            F[M:(self.N + 1) * M] = E[1:].reshape(-1)
        F[-1] = self.gauge_row(b, gauge_value)
        return F, E, flds

    def jacobian(self, b, cl, flds=None, batch=None, defect=False, forced=False):
        """Dense Jacobian of system() with respect to u = (b.flatten(), c_l), or (b.flatten(), mu) if defect/forced."""
        if self.couple_gamma:
            self.set_gamma(1.0 / cl)
        if flds is None:
            flds = self.fields(b)
        N, M = self.N, self.M
        nb = (N + 1) * M
        J = torch.zeros(nb + 1, nb + 1, device=self.dev)
        if batch is None:
            batch = max(1, int(6e8 // ((N + 1) * self.M2 * 8 * 12)))
        for k0 in range(0, nb, batch):
            k1 = min(nb, k0 + batch)
            I = torch.zeros(k1 - k0, nb, device=self.dev)
            I[torch.arange(k1 - k0), torch.arange(k0, k1)] = 1.0
            delta = I.reshape(k1 - k0, N + 1, M)
            dflds = self.fields(delta)
            dE = self.linearized(b, cl, delta, flds, dflds)         # (B, N+1, M)
            dc = self.psi_xy0(dflds)                                 # (B,)
            J[M:nb, k0:k1] = dE[:, 1:, :].reshape(k1 - k0, -1).T
            J[M - 1, k0:k1] = dc * (b[0, 0] if forced else 1.0)
        if forced:
            J[M - 1, 0] += cl - 1 + self.psi_xy0(flds)
        # continuity rows
        for j in range(1, M):
            J[j - 1, j] = 1.0
            J[j - 1, 0] = -1.0
        # gauge row (linear in b): assemble by applying gauge_row to basis vectors via its linear structure
        g = getattr(self, 'gauge', 'inf')
        if g == 'inf':
            J[nb, 0:nb] = (self.rad.ext1_R.reshape(-1, 1).expand(N + 1, M) / M).reshape(-1)
        elif g == 'half':
            if not hasattr(self.rad, 'ext0_R'):
                self.rad.ext0_R = torch.tensor(interp_matrix(self.rad.tR_np, [0.0], self.rad.wR_np), device=self.dev)
            row = (self.rad.ext0_R.reshape(-1, 1).expand(N + 1, M) / M - 0.5 * self.rad.ext1_R.reshape(-1, 1).expand(N + 1, M) / M).reshape(-1).clone()
            row[0] -= 0.5
            J[nb, 0:nb] = row
        # last column: mu (defect/forced mode) or c_l
        if defect or forced:
            J[M - 1, nb] = -1.0
            if forced:
                J[M:nb, nb] = -self.forcing_shape()[1:, None].expand(N, M).reshape(-1)
            return J
        if self.couple_gamma:
            h = 1e-6 * max(1.0, abs(cl))
            Fp, _, _ = self.system(b, cl + h, gauge_value=0.0)
            Fm, _, _ = self.system(b, cl - h, gauge_value=0.0)
            self.set_gamma(1.0 / cl)
            J[:, nb] = (Fp - Fm) / (2 * h)
        else:
            dEc = self.dE_dcl(b)
            J[M:nb, nb] = dEc[1:].reshape(-1)
            J[M - 1, nb] = 1.0
        return J

    # ---- physical fields on the grid ------------------------------------------------------------
    def xy(self):
        r = self.rad.rR[:, None]
        return r * self.ang.cos[None, :], r * self.ang.sin[None, :]

    def rho_from_b(self, b):
        return (self.rad.rR * self.wR)[:, None] * self.ang.sin[None, :] * b

    def velocity(self, flds):
        rv = (self.rad.rR * self.vR)[:, None]
        return rv * flds['Uhat1'], rv * flds['Uhat2']

    def psi(self, flds):
        return (self.rad.rR ** 2 * self.vR)[:, None] * flds['Psi']

    # ---- off-grid evaluation ---------------------------------------------------------------------
    def evaluate(self, b, cl, flds, r_pts, th_pts):
        """Evaluate rho, grad rho, U, psi and the transport residual at arbitrary points (r_pts, th_pts) (numpy
        arrays, same shape; theta in (0, pi/2)), using the spectral representation (barycentric in t, trig in theta)
        and the computed mode functions Psi~_n(t).  Returns a dict of numpy arrays."""
        r_pts = np.atleast_1d(np.asarray(r_pts, dtype=np.float64))
        th_pts = np.atleast_1d(np.asarray(th_pts, dtype=np.float64))
        shp = r_pts.shape
        r = r_pts.reshape(-1)
        th = th_pts.reshape(-1)
        rad, ang = self.rad, self.ang
        dev = self.dev
        t = rad.t_of_r(r)
        PR = torch.tensor(interp_matrix(rad.tR_np, t, rad.wR_np), device=dev)       # (P, N+1)
        PL = torch.tensor(interp_matrix(rad.tL_np, t, rad.wL_np), device=dev)
        tt = torch.tensor(t, device=dev)
        th_t = torch.tensor(th, device=dev)
        g = (1 - tt ** 2) / ((1 - tt) + self.p * (1 + tt))
        s2 = rad.s2_of_t(tt)
        om = (self.gamma - 1) * s2
        w = rad.w_of_t(tt, self.gamma)
        rr = torch.tensor(r, device=dev)
        # b and derivatives: b(t, th) = sum_k bhat_k(t) cos(2k th)
        bhat = ang.to_coef(b, 'EE')                                   # (N+1, M)
        bhat_t = rad.DR @ bhat
        kk = torch.tensor(self.ang.n_EE, dtype=torch.float64, device=dev)
        C = torch.cos(th_t[:, None] * kk[None, :])
        S = torch.sin(th_t[:, None] * kk[None, :])
        bp = ((PR @ bhat) * C).sum(1)
        rb_r = g * ((PR @ bhat_t) * C).sum(1)
        b_th = -((PR @ bhat) * kk[None, :] * S).sum(1)
        # modes of Psi~
        PsiC = flds['PsiC']                                          # (N+1, M2) Lobatto
        PsiC_t = rad.DL @ PsiC
        nf = self.nf
        Sn = torch.sin(th_t[:, None] * nf[None, :])
        Cn = torch.cos(th_t[:, None] * nf[None, :])
        Psi = ((PL @ PsiC) * Sn).sum(1)
        rPsi_r = g * ((PL @ PsiC_t) * Sn).sum(1)
        Psi_th = ((PL @ PsiC) * nf[None, :] * Cn).sum(1)
        cos, sin = torch.cos(th_t), torch.sin(th_t)
        G = (2 + om) * Psi + rPsi_r
        U1 = rr * w * (-(sin * G + cos * Psi_th))
        U2 = rr * w * (cos * G - sin * Psi_th)
        psi = rr ** 2 * w * Psi
        # rho and gradient: rho = r w P, P = sin th b
        P = sin * bp
        rP_r = sin * rb_r
        P_th = cos * bp + sin * b_th
        rho = rr * w * P
        rho_r = w * ((1 + om) * P + rP_r)
        rho_th_over_r = w * P_th
        rho_x = cos * rho_r - sin * rho_th_over_r
        rho_y = sin * rho_r + cos * rho_th_over_r
        x, y = rr * cos, rr * sin
        W1, W2 = cl * x + U1, cl * y + U2
        R = W1 * rho_x + W2 * rho_y - rho
        Nf = (W1 * rho_x).abs() + (W2 * rho_y).abs() + rho.abs()
        Nv = rho.abs() + (x * rho_x + y * rho_y).abs() + (U1 * rho_x + U2 * rho_y).abs()
        out = dict(rho=rho, rho_x=rho_x, rho_y=rho_y, U1=U1, U2=U2, psi=psi, R=R, Nf=Nf, Nv=Nv, b=bp,
                   x=x, y=y, W1=W1, W2=W2)
        return {k: v.detach().cpu().numpy().reshape(shp) for k, v in out.items()}


# ------------------------------------------------------------------------------------------------
# Newton solver
# ------------------------------------------------------------------------------------------------
def newton(mdl, b, cl, gauge_value=1.0, target=None, maxit=30, tol=1e-12, verbose=True, damping=True, log=None,
           mu=None, forced=False):
    """Newton with backtracking on |F|_inf.  Returns (b, cl, info); in defect mode (mu given) c_l is fixed and the
    scalar unknown is mu, returned in info['mu']."""
    N, M = mdl.N, mdl.M
    nb = (N + 1) * M
    defect = mu is not None
    hist = []
    F, E, flds = mdl.system(b, cl, gauge_value=gauge_value, target=target, mu=mu, forced=forced)
    nF = F.abs().max().item()
    J = None
    for it in range(maxit):
        J = mdl.jacobian(b, cl, flds, defect=defect and not forced, forced=forced)
        du = torch.linalg.solve(J, -F)
        db = du[:nb].reshape(N + 1, M)
        ds = du[nb].item()
        lam = 1.0
        accepted = False
        for _ in range(30 if damping else 1):
            b_new = b + lam * db
            cl_new = cl if defect else cl + lam * ds
            mu_new = mu + lam * ds if defect else None
            F_new, E_new, flds_new = mdl.system(b_new, cl_new, gauge_value=gauge_value, target=target, mu=mu_new, forced=forced)
            nF_new = F_new.abs().max().item()
            if (not damping) or nF_new < (1 - 1e-4 * lam) * nF or not math.isfinite(nF):
                accepted = True
                break
            lam *= 0.5
        msg = (f"  newton it {it:3d}: |F|={nF:.3e} -> {nF_new:.3e}  lam={lam:.3g}  |db|={db.abs().max().item():.3e} "
               f"{'dmu' if defect else 'dcl'}={ds:.3e}  cl={cl_new:.10f}  c={mdl.psi_xy0(flds_new).item():.10f} b0={b_new[0,0].item():.8f}"
               + (f" mu={mu_new:.10f}" if defect else ""))
        if verbose:
            print(msg, flush=True)
        if log is not None:
            log.write(msg + "\n"); log.flush()
        hist.append((nF, nF_new, lam, ds))
        b, cl, mu, F, E, flds, nF = b_new, cl_new, mu_new, F_new, E_new, flds_new, nF_new
        if not accepted:
            break
        if nF < tol:
            break
    return b, cl, dict(F=F, E=E, flds=flds, nF=nF, hist=hist, J=J, mu=mu)


def regrid(mdl_old, b_old, mdl_new):
    """Transfer b from one model (L, gamma, p, grid) to another: rho is the same function.
    b_new(r, th) = w_old(r)/w_new(r) * b_old(r, th)."""
    rad_new, rad_old = mdl_new.rad, mdl_old.rad
    r_new = rad_new.rR.cpu().numpy()
    t_old = rad_old.t_of_r(r_new)
    P = torch.tensor(interp_matrix(rad_old.tR_np, t_old, rad_old.wR_np), device=mdl_old.dev)
    b_int = P @ b_old                                                   # (N_new+1, M_old) at old angles
    # angular: same quadrant grid family; map coefficients if M differs
    if mdl_new.M != mdl_old.M:
        C = mdl_old.ang.to_coef(b_int, 'EE')
        Mn, Mo = mdl_new.M, mdl_old.M
        C2 = torch.zeros(C.shape[0], Mn, device=mdl_old.dev)
        m = min(Mn, Mo)
        C2[:, :m] = C[:, :m]
        b_int = mdl_new.ang.to_val(C2.to(mdl_new.dev), 'EE')
    # weights
    tt_old = torch.tensor(t_old, device=mdl_old.dev)
    w_old = rad_old.w_of_t(tt_old, mdl_old.gamma)
    w_new = mdl_new.wR
    return (w_old / w_new)[:, None].to(mdl_new.dev) * b_int.to(mdl_new.dev)
