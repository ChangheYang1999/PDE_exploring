"""
ipm3s.py -- smooth-centre representation (SCR) for IPM Setting III, y-leading branch.

Same problem and same pipeline structure as ipm3.py (angular classes, modal Green function on a Lobatto grid), but

  * radial map  r(t) = L sigma(t)^(1/2) (1-t)^(-p),  sigma = (1+t)/2,  p = 1/(1-gamma):
        r^2 is analytic in t at the centre (r^2 ~ L^2 2^(-2p) (1+t)), and r^(gamma-1) ~ (1-t) at infinity;
  * weight     w(t) = (1-t)/2  exactly (an analytic function of r^2 at 0, ~ r^(gamma-1) at infinity);
        omega = r w'/w = g w_t / w = -(1+t)/Q,  Q = (1-t)/2 + p (1+t),  g = (1-t^2)/Q  (r d/dr = g d/dt);
  * unknowns   beta_k(t_i), k = 0..M-1 on the Radau grid, with
        b(t, theta) = sum_k sigma(t)^k beta_k(t) cos(2k theta),
    so that b_k = O(r^(2k)) with even powers only: rho = y w b is smooth at the origin for every analytic beta.
    The non-integer indicial modes r^d Theta(theta) of the coupled linearisation at the source are NOT representable.

Rows: interior equations at (t_i, theta_j), i >= 1; the centre identity (c_l - 1 + c) beta_0(-1) = 0; for k >= 1 the
degree-reduction rows "beta_k(-1) equals the degree-(N-1) extrapolation from t_1..t_N" (beta_k(-1) is otherwise
invisible since sigma(-1) = 0); the gauge row.  Gauge 'K': b(t=1, theta=pi/2) = sum_k (-1)^k beta_k(1) = gauge_value,
i.e. the y-axis far-field amplitude rho(0,y) ~ K y^gamma with K = gauge_value * L^(1-gamma) 2^(-(1-gamma)/2) ...
(exact constant computed in K_of_state); SPEC 5.3 proves K != 0 for every profile, so the slice is attainable.
"""
import math
import numpy as np
import torch
from ipm3 import bary_weights, diff_matrix, interp_matrix, cheb_lobatto, cheb_radau, Angular

torch.set_default_dtype(torch.float64)


class Radial2:
    def __init__(self, N, L, p, device):
        self.N, self.L, self.p, self.dev = N, L, p, device
        tR = cheb_radau(N)
        tL = cheb_lobatto(N)
        self.tR_np, self.tL_np = tR, tL
        self.wR_np, self.wL_np = bary_weights(tR), bary_weights(tL)
        T = lambda A: torch.tensor(np.asarray(A, dtype=np.float64), device=device)
        self.DR = T(diff_matrix(tR, self.wR_np))
        self.DL = T(diff_matrix(tL, self.wL_np))
        self.P_RL = T(interp_matrix(tR, tL, self.wR_np))
        self.P_LR = T(interp_matrix(tL, tR, self.wL_np))
        self.ext1_R = T(interp_matrix(tR, [1.0], self.wR_np))
        self.ext0_R = T(interp_matrix(tR, [0.0], self.wR_np))
        self.extm1_int = T(interp_matrix(tR[1:], [-1.0]))          # degree-(N-1) extrapolation to t = -1 from t_1..t_N
        self.tR, self.tL = T(tR), T(tL)
        self.rR = self.rmap(self.tR)
        self.QR = self.Q(self.tR)
        self.QL = self.Q(self.tL)
        self.gR = (1 - self.tR ** 2) / self.QR
        self.gL = (1 - self.tL ** 2) / self.QL
        self.sigR = (1 + self.tR) / 2
        self.sigL = (1 + self.tL) / 2
        self.omR = -(1 + self.tR) / self.QR          # omega = r w'/w
        self.omL = -(1 + self.tL) / self.QL
        self.wR = (1 - self.tR) / 2
        self.wL = (1 - self.tL) / 2

    def Q(self, t):
        return (1 - t) / 2 + self.p * (1 + t)

    def rmap(self, t):
        return self.L * torch.sqrt((1 + t) / 2) / (1 - t) ** self.p

    def rmap_np(self, t):
        return self.L * np.sqrt((1 + t) / 2) / (1 - t) ** self.p

    def t_of_r(self, r):
        r = np.atleast_1d(np.asarray(r, dtype=np.float64))
        lo = -np.ones_like(r)
        hi = np.ones_like(r) - 1e-16
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            big = self.rmap_np(mid) > r
            hi = np.where(big, mid, hi)
            lo = np.where(big, lo, mid)
        return 0.5 * (lo + hi)


class IPM3S:
    def __init__(self, N=64, M=16, L=1.0, gamma=0.6, p=None, device='cpu', M2=None, couple_gamma=False):
        self.dev = torch.device(device)
        self.N, self.M, self.L, self.gamma = N, M, L, gamma
        if p is None:
            p = 1.0 / (1.0 - gamma)
        self.p = p
        self.couple_gamma = couple_gamma
        self.gauge = 'K'
        self.ang = Angular(M, self.dev)
        self.M2 = M + 2 if M2 is None else M2
        self.angf = Angular(self.M2, self.dev)
        self.rad = Radial2(N, L, p, self.dev)
        self.kk = torch.tensor(np.arange(M, dtype=np.float64), device=self.dev)      # k = 0..M-1
        self._angular_maps()
        self._poisson_setup()

    def set_gamma(self, gamma):
        """gamma enters only through p; keep p fixed inside a Newton solve (grid fixed): nothing to do here except
        record gamma (the weight w = (1-t)/2 and omega do not depend on gamma for fixed p)."""
        self.gamma = gamma

    def _angular_maps(self):
        ang, angf = self.ang, self.angf
        thf = angf.theta
        n = torch.tensor(self.ang.n_EE, dtype=torch.float64, device=self.dev)      # 2k
        self.C_f = torch.cos(thf[:, None] * n[None, :])                             # modes -> fine values
        self.Cd_f = -n[None, :] * torch.sin(thf[:, None] * n[None, :])              # modes -> fine d/dtheta values
        self.C_c = ang.S['EE']                                                      # modes -> coarse values
        self.Cd_c = -n[None, :] * torch.sin(ang.theta[:, None] * n[None, :])
        self.nf = torch.tensor(angf.n_OO, dtype=torch.float64, device=self.dev)
        thc = ang.theta
        self.S_OO_fc = torch.sin(thc[:, None] * self.nf[None, :])
        self.Sd_OO_fc = self.nf[None, :] * torch.cos(thc[:, None] * self.nf[None, :])

    def _poisson_setup(self):
        rad = self.rad
        tL, DL, Q, om = rad.tL, rad.DL, rad.QL, rad.omL
        base = (1 - tL ** 2)[:, None] * DL
        A1, A2 = [], []
        self.modes = np.asarray(self.angf.n_OO)
        for n in self.modes:
            n = float(n)
            M1 = base + torch.diag(Q * (n + 2 + om))
            M2 = base - torch.diag(Q * (n - 2 - om))
            if n == 2.0:
                # regularised centre row for n = 2 (the ODE row is vacuous there).  With r^2 ~ (1+t) the regular
                # solution has a nonzero t-derivative at t = -1; dividing the ODE by (1+t) gives
                #     2 I2~'(-1) - I2~(-1) = -Fhat_2'(-1)      (Q(-1) = 1, omega/(1+t) -> -1, Fhat_2(-1) = 0)
                M2[0, :] = 2.0 * DL[0, :]
                M2[0, 0] -= 1.0
            A1.append(M1)
            A2.append(M2)
        self.A1 = torch.stack(A1)
        self.A2 = torch.stack(A2)
        self.LU1 = torch.linalg.lu_factor(self.A1)
        self.LU2 = torch.linalg.lu_factor(self.A2)

    def poisson_modes(self, Fhat_L):
        C = Fhat_L @ self.angf.A['OO'].T
        rhs = self.rad.QL[:, None] * C
        shp = rhs.shape
        R = rhs.reshape(-1, shp[-2], shp[-1]).permute(2, 1, 0)
        R1 = R.clone()
        R2 = -R.clone()
        Cp = C.reshape(-1, shp[-2], shp[-1]).permute(2, 1, 0)          # (M2, N+1, B) mode coefficients Fhat_n(t)
        R2[0, 0, :] = -(self.rad.DL[0, :] @ Cp[0])                      # -Fhat_2'(-1)
        I1 = torch.linalg.lu_solve(*self.LU1, R1).permute(2, 1, 0).reshape(shp)
        I2 = torch.linalg.lu_solve(*self.LU2, R2).permute(2, 1, 0).reshape(shp)
        PsiC = (I1 + I2) / (2 * self.nf)
        return PsiC, I1, I2

    # ---- b and its derivatives from beta --------------------------------------------------------
    def b_modes(self, beta, grid='R'):
        """mode coefficients b_k(t) = sigma^k beta_k and their t-derivative on the Radau ('R') or Lobatto ('L') grid.
        beta: (..., N+1, M) Radau values."""
        rad = self.rad
        if grid == 'R':
            sig, D, bt = rad.sigR, rad.DR, beta
        else:
            sig, D, bt = rad.sigL, rad.DL, rad.P_RL @ beta
        k = self.kk
        sk = sig[:, None] ** k[None, :]                                  # sigma^k  (N+1, M)
        skm1 = torch.where(k[None, :] > 0, sig[:, None] ** torch.clamp(k[None, :] - 1, min=0), torch.zeros_like(sk))
        bk = sk * bt
        bk_t = 0.5 * k[None, :] * skm1 * bt + sk * (D @ bt)              # d/dt (sigma^k beta_k), sigma' = 1/2
        return bk, bk_t

    def b_values(self, beta):
        bk, bk_t = self.b_modes(beta, 'R')
        b = bk @ self.C_c.T
        rb_r = self.rad.gR[:, None] * (bk_t @ self.C_c.T)
        b_th = bk @ self.Cd_c.T
        return b, rb_r, b_th

    def fields(self, beta):
        rad, ang, angf = self.rad, self.ang, self.angf
        cosf, sinf = angf.cos[None, :], angf.sin[None, :]
        bk, bk_t = self.b_modes(beta, 'L')
        bLf = bk @ self.C_f.T
        bLf_t = bk_t @ self.C_f.T
        bLf_th = bk @ self.Cd_f.T
        P = sinf * bLf
        rP_r = rad.gL[:, None] * bLf_t * sinf
        P_th = cosf * bLf + sinf * bLf_th
        Fhat_L = cosf * ((1 + rad.omL)[:, None] * P + rP_r) - sinf * P_th
        PsiC, I1, I2 = self.poisson_modes(Fhat_L)
        PsiC_R = rad.P_LR @ PsiC
        rPsiC_r = rad.gR[:, None] * (rad.DR @ PsiC_R)
        Psi = PsiC_R @ self.S_OO_fc.T
        rPsi_r = rPsiC_r @ self.S_OO_fc.T
        Psi_th = PsiC_R @ self.Sd_OO_fc.T
        cos, sin = ang.cos[None, :], ang.sin[None, :]
        v = rad.wR[:, None]
        G = (2 + rad.omR)[:, None] * Psi + rPsi_r
        Ur_r = -v * Psi_th
        Uth_r = v * G
        U2y = v * (G * cos / sin - Psi_th)
        Uhat1 = -(sin * G + cos * Psi_th)
        Uhat2 = cos * G - sin * Psi_th
        return dict(Ur_r=Ur_r, Uth_r=Uth_r, U2y=U2y, Uhat1=Uhat1, Uhat2=Uhat2, PsiC=PsiC, PsiC_R=PsiC_R,
                    rPsiC_r=rPsiC_r, Psi=Psi, Psi_th=Psi_th, Fhat_L=Fhat_L, I1=I1, I2=I2)

    def psi_xy0(self, flds):
        return 2.0 * flds['PsiC'][..., 0, 0]

    def residual(self, beta, cl, flds=None):
        if flds is None:
            flds = self.fields(beta)
        b, rb_r, b_th = self.b_values(beta)
        om = self.rad.omR[:, None]
        A0 = cl - 1 + flds['U2y'] + (cl + flds['Ur_r']) * om
        return (cl + flds['Ur_r']) * rb_r + flds['Uth_r'] * b_th + A0 * b

    def linearized(self, beta, cl, delta, flds=None, dflds=None):
        if flds is None:
            flds = self.fields(beta)
        if dflds is None:
            dflds = self.fields(delta)
        b, rb_r, b_th = self.b_values(beta)
        d, rd_r, d_th = self.b_values(delta)
        om = self.rad.omR[:, None]
        A0 = cl - 1 + flds['U2y'] + (cl + flds['Ur_r']) * om
        return (cl + flds['Ur_r']) * rd_r + dflds['Ur_r'] * rb_r + flds['Uth_r'] * d_th + dflds['Uth_r'] * b_th \
            + A0 * d + (dflds['U2y'] + om * dflds['Ur_r']) * b

    def forcing_shape(self):
        """phi/w on the Radau grid for the smooth forcing mu y phi(r): phi/w = ((1-t)/2)^3 (phi = w^4 ~ r^{-4(1-gamma)})."""
        return ((1 - self.rad.tR) / 2) ** 3

    def gauge_row(self, beta, gauge_value):
        if self.gauge == 'K':
            bk1 = self.rad.ext1_R @ beta                        # beta_k(1), shape (1, M)
            return (bk1 * torch.cos(math.pi * self.kk)[None, :]).sum() - gauge_value
        elif self.gauge == 'inf':
            return (self.rad.ext1_R @ beta)[0, 0] - gauge_value        # mean over theta of b(inf) = beta_0(1)
        raise ValueError(self.gauge)

    def gauge_row_vec(self):
        N, M = self.N, self.M
        if self.gauge == 'K':
            row = (self.rad.ext1_R.reshape(-1, 1) * torch.cos(math.pi * self.kk)[None, :]).reshape(-1)
        else:
            row = torch.zeros(N + 1, M, device=self.dev); row[:, 0] = self.rad.ext1_R.reshape(-1); row = row.reshape(-1)
        return row

    def system(self, beta, cl, flds=None, gauge_value=1.0, target=None, mu=None, forced=False):
        if self.couple_gamma:
            self.set_gamma(1.0 / cl)
        if flds is None:
            flds = self.fields(beta)
        E = self.residual(beta, cl, flds)
        if target is not None:
            E = E - target
        N, M = self.N, self.M
        F = torch.empty((N + 1) * M + 1, device=self.dev)
        # degree-reduction rows for beta_k(-1), k >= 1
        F[0:M - 1] = beta[0, 1:] - (self.rad.extm1_int @ beta[1:, 1:]).reshape(-1)
        a0 = beta[0, 0]
        if mu is not None and forced:
            fs = self.forcing_shape()
            F[M - 1] = (cl - 1 + self.psi_xy0(flds)) * a0 - mu
            F[M:(N + 1) * M] = (E[1:] - mu * fs[1:, None]).reshape(-1)
        else:
            F[M - 1] = (cl - 1 + self.psi_xy0(flds)) * a0 - (0.0 if mu is None else mu)
            F[M:(N + 1) * M] = E[1:].reshape(-1)
        F[-1] = self.gauge_row(beta, gauge_value)
        return F, E, flds

    def jacobian(self, beta, cl, flds=None, batch=None, defect=False, forced=False):
        if self.couple_gamma:
            self.set_gamma(1.0 / cl)
        if flds is None:
            flds = self.fields(beta)
        N, M = self.N, self.M
        nb = (N + 1) * M
        J = torch.zeros(nb + 1, nb + 1, device=self.dev)
        if batch is None:
            batch = max(1, int(6e8 // ((N + 1) * self.M2 * 8 * 12)))
        c0 = self.psi_xy0(flds)
        a0 = beta[0, 0]
        for k0 in range(0, nb, batch):
            k1 = min(nb, k0 + batch)
            I = torch.zeros(k1 - k0, nb, device=self.dev)
            I[torch.arange(k1 - k0), torch.arange(k0, k1)] = 1.0
            delta = I.reshape(k1 - k0, N + 1, M)
            dflds = self.fields(delta)
            dE = self.linearized(beta, cl, delta, flds, dflds)
            dc = self.psi_xy0(dflds)
            J[M:nb, k0:k1] = dE[:, 1:, :].reshape(k1 - k0, -1).T
            J[M - 1, k0:k1] = dc * a0
        J[M - 1, 0] += cl - 1 + c0
        # degree-reduction rows
        ext = self.rad.extm1_int.reshape(-1)          # (N,)
        for k in range(1, M):
            J[k - 1, k] = 1.0                           # beta[0, k] has flat index k
            for i in range(1, N + 1):
                J[k - 1, i * M + k] = -ext[i - 1]
        J[nb, 0:nb] = self.gauge_row_vec()
        if defect or forced:
            J[M - 1, nb] = -1.0
            if forced:
                J[M:nb, nb] = -self.forcing_shape()[1:, None].expand(N, M).reshape(-1)
            return J
        # c_l column (p fixed; gamma enters nowhere else, so the column is the explicit derivative)
        b, rb_r, b_th = self.b_values(beta)
        dEc = rb_r + (1 + self.rad.omR)[:, None] * b
        J[M:nb, nb] = dEc[1:].reshape(-1)
        J[M - 1, nb] = a0
        return J

    # ---- physical fields -----------------------------------------------------------------------
    def rho_from_beta(self, beta):
        b, _, _ = self.b_values(beta)
        return (self.rad.rR * self.rad.wR)[:, None] * self.ang.sin[None, :] * b

    def K_of_state(self, beta, cl):
        """far-field amplitude K of rho(0, y) ~ K y^gamma (gamma = 1/cl) and the lead's canonical length
        L_can = (K/a0)^(cl/(cl-1)).  rho(0,y) = y w b(t, pi/2); w = (1-t)/2 and r = L sqrt(sigma) (1-t)^-p give, as t -> 1,
        (1-t) = (L/r)^(1/p) (sigma -> 1), so w ~ (1/2) (L/r)^(1-gamma) and K = (1/2) L^(1-gamma) * b(1, pi/2)
        (checked against ipm3.py: w_ipm3/w_Q -> 2 at infinity, WORKLOG 17:33Z; the earlier (L/sqrt2) factor was wrong)."""
        gamma = 1.0 / cl
        bK = (self.rad.ext1_R @ beta * torch.cos(math.pi * self.kk)[None, :]).sum().item()
        K = 0.5 * self.L ** (1 - gamma) * bK        # corrected 17:35Z: r = L sigma^(1/2) (1-t)^-p -> (1-t) = (L/r)^(1-gamma), w = (1-t)/2 (no sqrt 2)
        a0 = beta[0, 0].item()
        Lcan = (K / a0) ** (cl / (cl - 1)) if K / a0 > 0 else float('nan')
        return K, Lcan

    def evaluate(self, beta, cl, flds, r_pts, th_pts):
        r_pts = np.atleast_1d(np.asarray(r_pts, dtype=np.float64))
        th_pts = np.atleast_1d(np.asarray(th_pts, dtype=np.float64))
        shp = r_pts.shape
        r = r_pts.reshape(-1); th = th_pts.reshape(-1)
        rad, dev = self.rad, self.dev
        t = rad.t_of_r(r)
        PR = torch.tensor(interp_matrix(rad.tR_np, t, rad.wR_np), device=dev)
        PL = torch.tensor(interp_matrix(rad.tL_np, t, rad.wL_np), device=dev)
        tt = torch.tensor(t, device=dev); th_t = torch.tensor(th, device=dev); rr = torch.tensor(r, device=dev)
        Q = rad.Q(tt); g = (1 - tt ** 2) / Q; om = -(1 + tt) / Q; w = (1 - tt) / 2; sig = (1 + tt) / 2
        k = self.kk
        beta_t = rad.DR @ beta
        bet = PR @ beta; bet_t = PR @ beta_t                                 # (P, M)
        sk = sig[:, None] ** k[None, :]
        skm1 = torch.where(k[None, :] > 0, sig[:, None] ** torch.clamp(k[None, :] - 1, min=0), torch.zeros_like(sk))
        bk = sk * bet
        bk_t = 0.5 * k[None, :] * skm1 * bet + sk * bet_t
        n = 2 * k
        C = torch.cos(th_t[:, None] * n[None, :]); S = torch.sin(th_t[:, None] * n[None, :])
        bp = (bk * C).sum(1)
        rb_r = g * (bk_t * C).sum(1)
        b_th = -(bk * n[None, :] * S).sum(1)
        PsiC = flds['PsiC']; PsiC_t = rad.DL @ PsiC; nf = self.nf
        Sn = torch.sin(th_t[:, None] * nf[None, :]); Cn = torch.cos(th_t[:, None] * nf[None, :])
        Psi = ((PL @ PsiC) * Sn).sum(1)
        rPsi_r = g * ((PL @ PsiC_t) * Sn).sum(1)
        Psi_th = ((PL @ PsiC) * nf[None, :] * Cn).sum(1)
        cos, sin = torch.cos(th_t), torch.sin(th_t)
        G = (2 + om) * Psi + rPsi_r
        U1 = rr * w * (-(sin * G + cos * Psi_th))
        U2 = rr * w * (cos * G - sin * Psi_th)
        psi = rr ** 2 * w * Psi
        P = sin * bp; rP_r = sin * rb_r; P_th = cos * bp + sin * b_th
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
        out = dict(rho=rho, rho_x=rho_x, rho_y=rho_y, U1=U1, U2=U2, psi=psi, R=R, Nf=Nf, Nv=Nv, b=bp, x=x, y=y,
                   W1=W1, W2=W2, w=w, t=tt)
        return {kk: v.detach().cpu().numpy().reshape(shp) for kk, v in out.items()}


def regrid_s(mdl_old, beta_old, mdl_new):
    """Transfer beta between two SCR models (rho is the same function):
    b_k,new(r) = (w_old/w_new) b_k,old(r)  and  beta_k = sigma^-k b_k, so
    beta_k,new(t_new) = beta_k,old(t_old) (w_old/w_new) (sigma_old/sigma_new)^k, with
    sigma_old/sigma_new = (L_new/L_old)^2 (1-t_old)^(2 p_old) / (1-t_new)^(2 p_new)  (from r^2 = L^2 sigma (1-t)^-2p),
    an O(1) ratio: no cancellation.  Angular modes are truncated or zero-padded."""
    dev = mdl_new.dev
    r_new = mdl_new.rad.rR.cpu().numpy()
    t_old = mdl_old.rad.t_of_r(r_new)
    P = torch.tensor(interp_matrix(mdl_old.rad.tR_np, t_old, mdl_old.rad.wR_np), device=mdl_old.dev)
    bet = P @ beta_old                                               # beta_old,k at the new radii (N_new+1, M_old)
    tt_old = torch.tensor(t_old, device=mdl_old.dev)
    tt_new = mdl_new.rad.tR.to(mdl_old.dev)
    w_ratio = ((1 - tt_old) / 2) / ((1 - tt_new) / 2)
    sig_ratio = (mdl_new.L / mdl_old.L) ** 2 * (1 - tt_old) ** (2 * mdl_old.p) / (1 - tt_new) ** (2 * mdl_new.p)
    Mo, Mn = mdl_old.M, mdl_new.M
    m = min(Mo, Mn)
    k = torch.arange(m, dtype=torch.float64, device=mdl_old.dev)
    beta_new = torch.zeros(len(r_new), Mn, device=mdl_old.dev)
    beta_new[:, :m] = bet[:, :m] * (w_ratio[:, None] * sig_ratio[:, None] ** k[None, :])
    beta_new[0, 1:] = (mdl_new.rad.extm1_int.to(mdl_old.dev) @ beta_new[1:, 1:]).reshape(-1)
    return beta_new.to(dev)
