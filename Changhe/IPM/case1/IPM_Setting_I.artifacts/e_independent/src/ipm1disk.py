"""
ipm1disk.py -- SPEC N3(a) disk closure: unknowns on r <= R only; the far field r > R is the homogeneous extension
rho(r, theta) = (r/R)^k rho(R, theta), k = 1/c_l (frozen gamma), whose contribution to the modal Green function is analytic:
    int_R^inf s^{1-n} f_n(s) ds = f_n(R) R^{2-n} / (n - k - 1).
Radial map r(t) = L (1+t) / (1 - t + 2L/R), t in [-1, 1] (r(1) = R), Chebyshev-Radau collocation for b (t = -1 included,
t = 1 excluded), Lobatto grid for the Poisson ODEs.  The transport equation needs no boundary condition at r = R
(outflow).  Everything else (parity classes, dealiased angular products, weights w, v) as in ipm1.py.
"""
import math
import numpy as np
import torch
import ipm1
from ipm1 import Angular, bary_weights, diff_matrix, interp_matrix, cheb_lobatto, cheb_radau, clenshaw_curtis_weights


class RadialDisk:
    """Radial grid on [0, R]. Computational variable s in [-1, 1] (Chebyshev nodes), t = T(s) an optional clustering map
    t = s + alpha (s_P - s) exp(-((s - s_P)/w)^2) (T' = 1 - alpha at s_P: points are alpha/(1-alpha) times denser there; monotone
    for 0 <= alpha < 1), then r = L (1 + t)/(1 - t + 2L/R).  cluster = None (identity) or (s_P, w, alpha)."""
    def __init__(self, N, L, R, device, cluster=None, p=1.0):
        self.N, self.L, self.R = N, L, R
        self.p = float(p)                      # map exponent: r = L (1+t)/(1-t+a)^p, a = (2L/R)^(1/p); p > 1 puts more points in the far field
        self.cluster = None if cluster is None else tuple(float(v) for v in cluster)
        tR = cheb_radau(N); tL = cheb_lobatto(N)
        self.tR_np, self.tL_np = tR, tL
        wR, wL = bary_weights(tR), bary_weights(tL)
        T = lambda A: torch.tensor(np.asarray(A, dtype=np.float64), device=device)
        self.DR = T(diff_matrix(tR, wR)); self.DL = T(diff_matrix(tL, wL))
        self.P_RL = T(interp_matrix(tR, tL, wR)); self.P_LR = T(interp_matrix(tL, tR, wL))
        self.ext1_R = T(interp_matrix(tR, [1.0], wR))
        self.tR, self.tL = T(tR), T(tL)
        self.a = (2.0 * L / R) ** (1.0 / self.p)
        self.rR = self.rmap(self.tR); self.rL = self.rmap(self.tL)
        # r d/dr = S d/dt with S = r / (dr/dt)
        self.SR = self.rmap(self.tR) / self.drdt(self.tR); self.SL = self.rmap(self.tL) / self.drdt(self.tL)
        self.SR[0] = 0.0; self.SL[0] = 0.0
        self.ccw = T(clenshaw_curtis_weights(N))

    def Tmap(self, s):
        if self.cluster is None: return s
        sP, w, al = self.cluster; u = (s - sP) / w
        return s + al * (sP - s) * torch.exp(-u * u)

    def dTmap(self, s):
        if self.cluster is None: return torch.ones_like(s)
        sP, w, al = self.cluster; u = (s - sP) / w
        return 1 - al * torch.exp(-u * u) * (1 - 2 * u * u)

    def r_of_t(self, t):
        return self.L * (1 + t) / (1 - t + self.a) ** self.p

    def drdt_t(self, t):
        p, a = self.p, self.a
        return self.L * ((1 - t + a) + p * (1 + t)) / (1 - t + a) ** (p + 1)

    def rmap(self, s):
        return self.r_of_t(self.Tmap(s))

    def drdt(self, s):
        """dr/ds (the derivative with respect to the computational variable)."""
        return self.drdt_t(self.Tmap(s)) * self.dTmap(s)

    def t_of_r(self, r):
        """computational variable s for given r (closed form for t if p = 1, Newton otherwise; Newton for s if clustered)."""
        if self.p == 1.0:
            t = ((r * (1 + self.a) - self.L) / (self.L + r)).clamp(-1.0, 1.0)
        else:
            # start from the p = 1 formula with the same a, then Newton on r(t) - r = 0 (monotone)
            t = ((r * (1 + self.a) - self.L) / (self.L + r)).clamp(-1.0 + 1e-15, 1.0 - 1e-15)
            for _ in range(80):
                f = self.r_of_t(t) - r
                t = (t - f / self.drdt_t(t)).clamp(-1.0, 1.0 - 1e-16)
                if (f.abs() / (r + 1e-300)).max() < 1e-15: break
        if self.cluster is None: return t
        s = t.clone()
        for _ in range(60):
            f = self.Tmap(s) - t
            s = (s - f / self.dTmap(s)).clamp(-1.0, 1.0)
            if f.abs().max() < 1e-15: break
        return s

    @staticmethod
    def s_for_r(L, R, r_c, cluster_w, alpha, p=1.0):
        """helper: the (s_P, w, alpha) tuple that centres the cluster at r = r_c (T(s_P) = s_P, so s_P = t(r_c))."""
        tmp = RadialDisk.__new__(RadialDisk); tmp.L, tmp.R, tmp.p = L, R, float(p); tmp.a = (2.0 * L / R) ** (1.0 / tmp.p); tmp.cluster = None
        t_c = tmp.t_of_r(torch.tensor([float(r_c)], dtype=torch.float64))[0].item()
        return (t_c, cluster_w, alpha)


class IPM1Disk:
    def __init__(self, N=64, M=16, L=1.0, R=100.0, gamma=0.5, device='cpu', cluster=None, p=1.0):
        self.dev = torch.device(device)
        self.N, self.M, self.L, self.R, self.gamma = N, M, L, R, gamma
        self.cluster = cluster; self.pmap = float(p)
        self.beta = 0.0; self.p = None
        self.k_tail = gamma          # far-field exponent used in the tail; set to 1/c_l by the solver for consistency
        self.ang = Angular(M, self.dev)
        self.M2 = M + 2; self.angf = Angular(self.M2, self.dev)
        self.nmodes = self.M2; self.nf = self.angf.n['OO']
        self.rad = RadialDisk(N, L, R, self.dev, cluster=cluster, p=p)
        self._angular_maps(); self._weights(); self._poisson_setup()

    def _angular_maps(self):
        ang, angf = self.ang, self.angf
        sf = angf.s; k = torch.arange(self.M, device=self.dev, dtype=torch.float64)
        S_EE_f = torch.cos(sf[:, None] * (2 * k)[None, :]); D_EE_f = -(2 * k)[None, :] * torch.sin(sf[:, None] * (2 * k)[None, :])
        self.T_cf = S_EE_f @ ang.A['EE']; self.Td_cf = D_EE_f @ ang.A['EE']
        self.Aq_OO = angf.A['OO']
        nf = self.nf; thc = ang.theta
        self.S_OO_fc = torch.sin(thc[:, None] * nf[None, :]); self.Sd_OO_fc = nf[None, :] * torch.cos(thc[:, None] * nf[None, :])

    def _weights(self):
        L, g = self.L, self.gamma
        rR, rL = self.rad.rR, self.rad.rL
        self.s2R = rR ** 2 / (L ** 2 + rR ** 2); self.s2L = rL ** 2 / (L ** 2 + rL ** 2)
        self.wR = (1 + rR ** 2 / L ** 2) ** ((g - 3) / 2); self.vR = (1 + rR ** 2 / L ** 2) ** ((g - 1) / 2)
        self.wL = (1 + rL ** 2 / L ** 2) ** ((g - 3) / 2); self.vL = (1 + rL ** 2 / L ** 2) ** ((g - 1) / 2)
        self.omegaR = (g - 3) * self.s2R; self.omegaL = (g - 3) * self.s2L

    def _poisson_setup(self):
        """I1~ = I1/(r^2 v), I2~ = I2/(r^2 v) on [0, R]:
           I1' = -n I1/r + r f ;  I2' = n I2/r - r f ;  with f = r^2 w F^.
           Multiply by S_L = r/(dr/dt):  S dI~/dt = I~ [-n - r W'/W] + r f / W   (I1),  I~ [n - r W'/W] - r f/W  (I2),
           W = r^2 v, r W'/W = 2 + (g-1) s2,  r f / W = r F^ / (1 + r^2/L^2).
           Rows: t = -1: I1~(0) = 0 (n>=2 ... both vanish: I2~(0) = 0 for n > 2, I2~'(0)=0 form for n = 2);
                 t = +1: I2~(R) = tail / (R^2 v(R)),  tail = f_n(R) R^2/(n - k - 1), k = gamma."""
        N, g = self.N, self.gamma
        tL = self.rad.tL; DL = self.rad.DL; S = self.rad.SL
        kap = 2 + (g - 1) * self.s2L
        self.rhs_scale = (self.rad.rL ** 2 / (1 + self.rad.rL ** 2 / self.L ** 2))      # multiplies F^_n: r f/W * S... see below
        A1, A2 = [], []
        base = S[:, None] * DL
        for n in self.modes_list():
            c1 = -n - kap; c2 = n - kap
            M1 = base - torch.diag(c1); M2 = base - torch.diag(c2)
            # row t=-1: I1~(0)=0 ; for I2: n>2 -> I2~(0)=0 ; n==2 -> derivative condition
            M1[0, :] = 0.0; M1[0, 0] = 1.0
            if n == 2:
                M2[0, :] = DL[0, :]
            else:
                M2[0, :] = 0.0; M2[0, 0] = 1.0
            # row t=+1 for I2: boundary value from the tail (set in poisson_modes)
            M2[-1, :] = 0.0; M2[-1, -1] = 1.0
            A1.append(M1); A2.append(M2)
        self.A1 = torch.stack(A1); self.A2 = torch.stack(A2)
        self.LU1 = torch.linalg.lu_factor(self.A1); self.LU2 = torch.linalg.lu_factor(self.A2)
        self.S_L = S

    def modes_list(self):
        return [int(v) for v in self.nf.cpu().numpy()]

    def poisson_modes(self, Fhat_L, Fext=None):
        """Fhat_L: (..., N+1, M2) values on Lobatto grid of F^ = f/(r^2 w). Returns psi~ values on fine grid and PsiC (..., N+1, nmodes).
        Fext (..., M2): fine-grid values at r = R of the EXTERIOR source F^_ext = k cos(theta) P - sin(theta) P_theta, P = cos^2 sin b(R,.),
        i.e. d_x of the homogeneous extension (r/R)^k rho(R, theta) divided by r^2 w; it feeds the tail integral.  If None, the interior
        source at r = R is used (the pre-2026-10-18 behaviour; wrong unless the data are exactly homogeneous at R; astra review lsqpin)."""
        C = Fhat_L @ self.Aq_OO.T                                     # (..., N+1, nmodes) F^_n(t)
        Cext = C[..., -1, :] if Fext is None else Fext @ self.Aq_OO.T
        # rhs: S * r f / W = S * r F^ /(1 + r^2/L^2)
        rhs = (self.rad.rL ** 2 / (1 + self.rad.rL ** 2 / self.L ** 2))[:, None] * C          # r^2 f / W = r^2 F^/(1 + r^2/L^2)
        shp = rhs.shape
        R_ = rhs.reshape(-1, shp[-2], shp[-1]).permute(2, 1, 0)       # (nmodes, N+1, B)
        R1 = R_.clone(); R2 = -R_.clone()
        R1[:, 0, :] = 0.0; R2[:, 0, :] = 0.0
        # tail boundary value at t = +1: I2(R) = f_n(R) R^2/(n - k - 1),  f_n(R) = R^2 w(R) F^_n(R);  I2~ = I2/(R^2 v(R))
        n = self.nf; k = self.k_tail
        fR = (self.rad.rL[-1] ** 2 * self.wL[-1]) * Cext                                # (..., nmodes)
        tail = fR * self.R ** 2 / (n - k - 1)[None, :]
        I2R = tail / (self.R ** 2 * self.vL[-1])
        R2[:, -1, :] = I2R.reshape(-1, shp[-1]).T
        I1 = torch.linalg.lu_solve(*self.LU1, R1).permute(2, 1, 0).reshape(shp)
        I2 = torch.linalg.lu_solve(*self.LU2, R2).permute(2, 1, 0).reshape(shp)
        PsiC = (I1 + I2) / (2 * n)[None, :]
        return PsiC @ torch.sin(self.angf.theta[:, None] * n[None, :]).T, PsiC

    def fields(self, b):
        ang, angf, rad = self.ang, self.angf, self.rad
        cosf, sinf = angf.cos[None, :], angf.sin[None, :]
        bL = rad.P_RL @ b
        bLf = bL @ self.T_cf.T; bLf_th = bL @ self.Td_cf.T
        P_L = cosf ** 2 * sinf * bLf
        rP_r = rad.SL[..., :, None] * (rad.DL @ bLf) * cosf ** 2 * sinf
        P_th = (cosf ** 3 - 2 * cosf * sinf ** 2) * bLf + cosf ** 2 * sinf * bLf_th
        Fhat_L = cosf * ((3 + self.omegaL)[..., :, None] * P_L + rP_r) - sinf * P_th
        Fext = self.k_tail * cosf * P_L[..., -1, :] - sinf * P_th[..., -1, :]          # exterior source of the homogeneous extension at r = R
        Psi_Lf, PsiC = self.poisson_modes(Fhat_L, Fext=Fext)
        PsiC_R = rad.P_LR @ PsiC
        rPsiC_r = rad.SR[..., :, None] * (rad.DR @ PsiC_R)
        Psi = PsiC_R @ self.S_OO_fc.T; rPsi_r = rPsiC_r @ self.S_OO_fc.T; Psi_th = PsiC_R @ self.Sd_OO_fc.T
        cos, sin = ang.cos[None, :], ang.sin[None, :]
        G = (2 + (self.gamma - 1) * self.s2R)[..., :, None] * Psi + rPsi_r
        Uhat1 = -(sin * G + cos * Psi_th); Uhat2 = cos * G - sin * Psi_th
        v = self.vR[..., :, None]
        Ur_over_r = v * (Uhat1 * cos + Uhat2 * sin); Uth_over_r = v * (-Uhat1 * sin + Uhat2 * cos)
        coefU = v * (2 * Uhat1 / cos + Uhat2 / sin)
        return dict(Uhat1=Uhat1, Uhat2=Uhat2, Ur_over_r=Ur_over_r, Uth_over_r=Uth_over_r, coefU=coefU,
                    Psi_L=Psi_Lf, PsiC=PsiC, PsiC_R=PsiC_R, rPsiC_r=rPsiC_r, Fhat_L=Fhat_L, bL=bL)

    def residual(self, b, cl, flds=None):
        if flds is None: flds = self.fields(b)
        rad, ang = self.rad, self.ang
        rb_r = rad.SR[:, None] * (rad.DR @ b)
        b_th = ang.dtheta(b, 'EE')
        A0 = (cl * self.omegaR)[:, None] + flds['Ur_over_r'] * self.omegaR[:, None] + (3 * cl - 1) + flds['coefU']
        return (cl + flds['Ur_over_r']) * rb_r + flds['Uth_over_r'] * b_th + A0 * b

    def psi_xy0(self, flds):
        return 2.0 * flds['PsiC'][..., 0, 0]

    def rho_from_b(self, b):
        r = self.rad.rR[:, None]
        return r ** 3 * self.wR[:, None] * self.ang.cos[None, :] ** 2 * self.ang.sin[None, :] * b

    def velocity(self, flds):
        rv = (self.rad.rR * self.vR)[:, None]
        return rv * flds['Uhat1'], rv * flds['Uhat2']

    def psi(self, flds):
        return (self.rad.rR ** 2 * self.vR)[:, None] * (flds['PsiC_R'] @ self.S_OO_fc.T)
