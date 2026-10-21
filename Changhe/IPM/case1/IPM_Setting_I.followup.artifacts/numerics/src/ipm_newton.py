"""
ipm_newton.py -- exact-Jacobian Newton solver for IPM Setting I (even-x / odd-y self-similar profiles, full plane).

Unknowns: b(q_i, theta_j) for i = 1..N (Chebyshev-Lobatto nodes in q, q_0 = 0 excluded: b(0, theta) = 1 is a(0) = 1)
and c_l.  Representation (the lead's compactified radial variable):
    rho = r^3 w(r) Pi(theta) b(q, theta),   Pi = cos^2(theta) sin(theta),   w = (1 + u^2)^((k-3)/2),  u = r/L,  k = 1/c_l,
    q = 1 - (1 + u^2)^(-(1-k)/2)   (q ~ (1-k) u^2/2 at 0, 1 - q ~ u^(k-1) at infinity),
so a = rho/(x^2 y) = w b, a(0) = b(0), and the far field is rho ~ L^(3-k) r^k Pi b(1, theta).
Angular basis: b in class EE (cos 2m theta, m = 0..M-1) on the quadrant midpoint grid theta_j = (j+1/2) pi/(2M).
Velocity: canonical modal inverse (SPEC V1).  With P1 := 1/(1+u^2) = (1-q)^(2/(1-k)), v := (1+u^2)^((k-1)/2) = 1 - q,
    S := r d q/d r = (1-k)(1-q)(1-P1),  omega_w := r w'/w = (k-3)(1-P1),  omega_v := r v'/v = (k-1)(1-P1),
    d_x rho = r^2 w Fhat,  Fhat = cos Pi [(3+omega_w) b + S b_q] - sin [Pi' b + Pi b_theta]   (exact on the fine angular grid),
    Fhat = sum_n Fhat_n(q) sin(2 n theta),  psi = r^2 v sum_n psit_n sin(2 n theta),  psit_n = (J1_n + J2_n)/(4n),
    S J1' = -(2n + 2 + omega_v) J1 + L^2 (1-P1) Fhat_n,   S J2' = (2n - 2 - omega_v) J2 - L^2 (1-P1) Fhat_n   (nu = 2n in the code),
    (J1 = r^(-2n) int_0^r s^(2n+1) f_n ds / (r^2 v), J2 = r^(2n) int_r^inf s^(1-2n) f_n ds / (r^2 v)); the q = 0 row of J2 for
    n = 1 is the divided form J2'(0) - J2(0) + L^2 Fhat_1(0)/(1-k) = 0 (the other q = 0 rows give J1(0) = 0, J2(0) = 0).
    Uhat := U/(r v):  Uhat_r = -psit_theta,  Uhat_theta = (2 + omega_v) psit + S psit_q.   c = psi_xy(0) = J2_1(0)/2.
Residual rows (divided transport residual, regular and O(1) on the whole closed domain including q = 1):
    Ehat := (W.grad rho - rho)/(r^3 w Pi (1-q))
          = c_l (1-k)(1-P1) b_q + Uhat_r [(3+omega_w) b + S b_q] + Uhat_theta [(Pi'/Pi) b + b_theta] + (3 c_l - 1) (P1/(1-q)) b
at (q_i, theta_j), i = 1..N, and the identity row 3 c_l - 1 - c = 0 (the q = 0 rows of the equation reduce to it).
Ehat is quadratic in b at fixed c_l, so the b-columns of the Jacobian are exact central differences; the c_l column is a
forward-mode derivative (torch.func.jvp).
"""
import math, time, json, sys
import numpy as np
import torch

torch.set_default_dtype(torch.float64)
DT = torch.float64


# ----------------------------------------------------------------------------------------------
# 1-D spectral tools
# ----------------------------------------------------------------------------------------------
def cheb_lobatto01(N):
    """N+1 Chebyshev-Gauss-Lobatto points on [0, 1], increasing (q_0 = 0, q_N = 1)."""
    return 0.5 * (1.0 - np.cos(np.pi * np.arange(N + 1) / N))


def bary_weights(x):
    x = np.asarray(x, dtype=np.float64)
    n = len(x)
    logw = np.zeros(n); sgn = np.ones(n)
    for j in range(n):
        d = x[j] - np.delete(x, j)
        logw[j] = -np.sum(np.log(np.abs(d))); sgn[j] = np.prod(np.sign(d))
    logw -= logw.max()
    return sgn * np.exp(logw)


def diff_matrix(x, w=None):
    x = np.asarray(x, dtype=np.float64)
    if w is None: w = bary_weights(x)
    n = len(x); D = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j: D[i, j] = (w[j] / w[i]) / (x[i] - x[j])
        D[i, i] = -np.sum(D[i, :])
    return D


def interp_matrix(x, xi, w=None):
    x = np.asarray(x, dtype=np.float64); xi = np.atleast_1d(np.asarray(xi, dtype=np.float64))
    if w is None: w = bary_weights(x)
    P = np.zeros((len(xi), len(x)))
    for kk, xx in enumerate(xi):
        d = xx - x
        hit = np.where(np.abs(d) < 1e-15)[0]
        if len(hit): P[kk, hit[0]] = 1.0
        else:
            tmp = w / d; P[kk, :] = tmp / tmp.sum()
    return P


# ----------------------------------------------------------------------------------------------
# angular transforms on the quadrant midpoint grid (four parity classes)
# ----------------------------------------------------------------------------------------------
class Angular:
    """Quadrant grid with the map theta(s) = s + (beta/2) sin(2 s), s_j = (j+1/2) pi/(2M), 0 <= beta < 1 (theta'(pi/2) = 1 - beta:
    collocation angles are clustered at the y-axis by 1/(1-beta); theta'(0) = 1 + beta).  Parities are preserved by the map, so
    the four classes use trigonometric bases in s: EE cos(2k s), EO sin((2k+1) s), OO sin(2(k+1) s), OE cos((2k+1) s), k = 0..M-1.
    d/dtheta = (1/theta'(s)) d/ds."""
    def __init__(self, M, device, beta=0.0):
        self.M = M; self.dev = device; self.beta = float(beta)
        sj = (np.arange(M) + 0.5) * np.pi / (2 * M)
        th = sj + 0.5 * self.beta * np.sin(2 * sj); dth = 1.0 + self.beta * np.cos(2 * sj)
        k = np.arange(M)
        S = {'EE': np.cos(np.outer(sj, 2 * k)), 'EO': np.sin(np.outer(sj, 2 * k + 1)),
             'OO': np.sin(np.outer(sj, 2 * (k + 1))), 'OE': np.cos(np.outer(sj, 2 * k + 1))}
        self.n = {'EE': 2 * k, 'EO': 2 * k + 1, 'OO': 2 * (k + 1), 'OE': 2 * k + 1}
        T = lambda A: torch.tensor(np.asarray(A, dtype=np.float64), device=device)
        self.S = {c: T(S[c]) for c in S}
        self.A = {c: torch.linalg.inv(self.S[c]) for c in S}          # values -> coefficients
        self.s_np, self.theta_np, self.dtheta_ds_np = sj, th, dth
        self.s = T(sj); self.theta = T(th); self.dtheta_ds = T(dth)
        self.cos = torch.cos(self.theta); self.sin = torch.sin(self.theta)
        # d/ds on values (class changes), then 1/theta'(s)
        Dc = np.zeros((M, M))
        for kk in range(1, M): Dc[kk - 1, kk] = -2.0 * kk
        D_EE = S['OO'] @ Dc @ np.linalg.inv(S['EE'])
        D_EO = S['OE'] @ np.diag(2 * k + 1.0) @ np.linalg.inv(S['EO'])
        Dc2 = np.zeros((M, M))
        for kk in range(0, M - 1): Dc2[kk + 1, kk] = 2.0 * (kk + 1)
        D_OO = S['EE'] @ Dc2 @ np.linalg.inv(S['OO'])
        D_OE = S['EO'] @ np.diag(-(2 * k + 1.0)) @ np.linalg.inv(S['OE'])
        self.D = {c: T((1.0 / dth)[:, None] * Dm) for c, Dm in [('EE', D_EE), ('EO', D_EO), ('OO', D_OO), ('OE', D_OE)]}

    def s_of_theta(self, th):
        """inverse map (numpy, Newton)."""
        th = np.asarray(th, float); s = th.copy()
        if self.beta == 0.0: return s
        for _ in range(60):
            f = s + 0.5 * self.beta * np.sin(2 * s) - th; df = 1.0 + self.beta * np.cos(2 * s)
            s = s - f / df
            if np.abs(f).max() < 1e-15: break
        return s

    def dtheta(self, F, cls):
        return F @ self.D[cls].T

    def to_coef(self, F, cls):
        return F @ self.A[cls].T

    def to_val(self, C, cls):
        return C @ self.S[cls].T


# ----------------------------------------------------------------------------------------------
# the model
# ----------------------------------------------------------------------------------------------
class Model:
    def __init__(self, N, M, L, device='cuda', beta=0.0, nmodes=None, Mq=None, Npsi=None):
        self.N, self.M, self.L = N, M, float(L)
        self.beta = float(beta)
        self.dev = torch.device(device)
        T = lambda A: torch.tensor(np.asarray(A, dtype=np.float64), device=self.dev)
        q = cheb_lobatto01(N); self.q_np = q
        wq = bary_weights(q); self.wq_np = wq
        self.q = T(q); self.Dq = T(diff_matrix(q, wq))
        # mixed resolution: the Poisson modes psit_nu(q) live on a finer Chebyshev grid (Npsi + 1 nodes) than b (the mode
        # functions of high nu vary much faster in q than b); default Npsi = N (identical grids)
        self.Npsi = N if Npsi is None else int(Npsi)
        if self.Npsi == N:
            self.qpsi_np, self.wqpsi_np, self.qpsi, self.Dqpsi = q, wq, self.q, self.Dq
            self.P_bp = torch.eye(N + 1, device=self.dev); self.P_pb = torch.eye(N + 1, device=self.dev)
        else:
            qp = cheb_lobatto01(self.Npsi); wqp = bary_weights(qp)
            self.qpsi_np, self.wqpsi_np = qp, wqp; self.qpsi = T(qp); self.Dqpsi = T(diff_matrix(qp, wqp))
            self.P_bp = T(interp_matrix(q, qp, wq))        # coarse b nodes -> fine psi nodes
            self.P_pb = T(interp_matrix(qp, q, wqp))       # fine psi nodes -> coarse b nodes
        self.ang = Angular(M, self.dev, beta=self.beta)
        # true Fourier modes nu = 2, 4, ..., 2 nmodes for the Poisson source and psi (quadrature on a fine mapped grid)
        self.nmodes = (2 * M if self.beta != 0.0 else M + 2) if nmodes is None else nmodes
        self.Mq = (8 * M if self.beta != 0.0 else M + 2) if Mq is None else Mq
        self.M2 = self.nmodes
        sf = (np.arange(self.Mq) + 0.5) * np.pi / (2 * self.Mq)
        thf = sf + 0.5 * self.beta * np.sin(2 * sf); dthf = 1.0 + self.beta * np.cos(2 * sf)
        self.thetaf_np = thf
        k = np.arange(M)
        A_EE = np.linalg.inv(np.cos(np.outer(self.ang.s_np, 2 * k)))
        S_EE_f = np.cos(np.outer(sf, 2 * k)); D_EE_f = (1.0 / dthf)[:, None] * (-(2 * k)[None, :] * np.sin(np.outer(sf, 2 * k)))
        self.T_cf = T(S_EE_f @ A_EE); self.Td_cf = T(D_EE_f @ A_EE)
        nf = 2.0 * (np.arange(self.nmodes) + 1); self.nf = T(nf)
        self.nf_np = nf
        # quadrature: Fhat_nu = (4/pi) int_0^{pi/2} Fhat sin(nu theta) dtheta = (2/Mq) sum_f Fhat_f sin(nu theta_f) theta'(s_f)
        self.Aq_OO = T((2.0 / self.Mq) * np.sin(np.outer(nf, thf)) * dthf[None, :])      # (nmodes, Mq)
        thc = self.ang.theta_np
        self.S_fc = T(np.sin(np.outer(thc, nf))); self.Sd_fc = T(nf[None, :] * np.cos(np.outer(thc, nf)))
        c, s_ = self.ang.cos, self.ang.sin
        self.PiPi = c / s_ - 2 * s_ / c      # Pi'/Pi on the coarse grid
        self.angf_cos = T(np.cos(thf)); self.angf_sin = T(np.sin(thf))
        cf, sf_ = self.angf_cos, self.angf_sin
        self.Pif = cf ** 2 * sf_; self.Pipf = cf ** 3 - 2 * cf * sf_ ** 2

    # ---- geometry as a function of c_l (differentiable) -------------------------------------
    def geom(self, cl, q=None):
        k = 1.0 / cl
        q = self.q if q is None else q
        omq = 1.0 - q
        P1 = omq ** (2.0 / (1.0 - k))                 # 1/(1+u^2)
        P1[-1] = 0.0
        omP1 = 1.0 - P1                               # u^2/(1+u^2)
        S = (1.0 - k) * omq * omP1                    # r dq/dr
        omega_w = (k - 3.0) * omP1
        omega_v = (k - 1.0) * omP1
        P1_over_omq = omq ** ((1.0 + k) / (1.0 - k))  # P1/(1-q)
        P1_over_omq[-1] = 0.0
        return dict(k=k, P1=P1, omP1=omP1, S=S, omega_w=omega_w, omega_v=omega_v, P1_over_omq=P1_over_omq)

    def radii(self, cl):
        """r at the nodes (inf at q = 1) and the weights w, v (numpy)."""
        g = self.geom(torch.as_tensor(float(cl), device=self.dev))
        P1 = g['P1'].detach().cpu().numpy()
        with np.errstate(divide='ignore'):
            u2 = np.where(P1 > 0, (1.0 - P1) / np.where(P1 > 0, P1, 1.0), np.inf)
        r = self.L * np.sqrt(u2)
        k = 1.0 / float(cl)
        w = P1 ** ((3.0 - k) / 2.0); v = P1 ** ((1.0 - k) / 2.0)
        return r, w, v

    # ---- Poisson ---------------------------------------------------------------------------
    def poisson_matrices(self, gp):
        """Collocation matrices for J1_n and J2_n, n = 1..M2 (stacked), on the fine psi grid, with the q = 0 rows as in the
        docstring.  gp: geometry on the fine grid (geom(cl, self.qpsi))."""
        S, ov = gp['S'], gp['omega_v']
        base = S[:, None] * self.Dqpsi                # S d/dq
        A1, A2 = [], []
        nf = self.nf
        for i in range(self.M2):
            nu = nf[i]                                 # angular frequency nu = 2n of sin(nu theta)
            M1 = base + torch.diag(nu + 2 + ov)
            M2 = base - torch.diag(nu - 2 - ov)
            if i == 0:   # n = 1: divided row at q = 0:  J2'(0) - J2(0) = -L^2 Fhat_1(0)/(1-k)
                row = self.Dqpsi[0, :].clone(); row[0] = row[0] - 1.0
                M2 = torch.cat([row[None, :], M2[1:, :]], dim=0)
            A1.append(M1); A2.append(M2)
        return torch.stack(A1), torch.stack(A2)

    def fields(self, b, cl, g=None, lu=None):
        """b: (..., N+1, M) coarse EE values.  Returns Uhat_r, Uhat_theta (..., N+1, M) at the coarse nodes, c = psi_xy(0) (...),
        the mode tables psit_n, psit_nq (..., Npsi+1, nmodes) on the fine psi grid, and bq (coarse)."""
        if g is None: g = self.geom(cl)
        gp = g if self.Npsi == self.N else self.geom(cl, self.qpsi)
        L2 = self.L ** 2
        bq = torch.einsum('ij,...jm->...im', self.Dq, b)
        # interpolate b and b_q to the fine psi grid (exact for the degree-N interpolant)
        bP = torch.einsum('ij,...jm->...im', self.P_bp, b); bqP = torch.einsum('ij,...jm->...im', self.P_bp, bq)
        bf = bP @ self.T_cf.T                                       # (..., Npsi+1, Mq)
        bthf = bP @ self.Td_cf.T
        bqf = bqP @ self.T_cf.T
        c3 = (3.0 + gp['omega_w'])[:, None]; Sp = gp['S'][:, None]
        Fhat = self.angf_cos * self.Pif * (c3 * bf + Sp * bqf) - self.angf_sin * (self.Pipf * bf + self.Pif * bthf)
        Fn = Fhat @ self.Aq_OO.T                                    # (..., Npsi+1, nmodes) true Fourier coefficients Fhat_nu(q)
        rhs = (L2 * gp['omP1'])[:, None] * Fn                       # (..., Npsi+1, nmodes)
        shp = rhs.shape
        R = rhs.reshape(-1, shp[-2], shp[-1]).permute(2, 1, 0)      # (nmodes, Npsi+1, B)
        R1 = R.clone(); R2 = -R.clone()
        R2[0, 0, :] = -L2 * Fn.reshape(-1, shp[-2], shp[-1])[:, 0, 0] / (1.0 - gp['k'])   # divided row rhs for n = 1
        if lu is None:
            A1, A2 = self.poisson_matrices(gp)
            J1 = torch.linalg.solve(A1, R1); J2 = torch.linalg.solve(A2, R2)
        else:
            J1 = torch.linalg.lu_solve(*lu[0], R1); J2 = torch.linalg.lu_solve(*lu[1], R2)
        J1 = J1.permute(2, 1, 0).reshape(shp); J2 = J2.permute(2, 1, 0).reshape(shp)
        psit_n = (J1 + J2) / (2.0 * self.nf)                        # (..., Npsi+1, nmodes); 1/(2 nu) = 1/(4n)
        psit_nq = torch.einsum('ij,...jm->...im', self.Dqpsi, psit_n)
        # mode tables at the coarse nodes
        psit_c = torch.einsum('ij,...jm->...im', self.P_pb, psit_n); psit_cq = torch.einsum('ij,...jm->...im', self.P_pb, psit_nq)
        psit = psit_c @ self.S_fc.T                                  # coarse values (..., N+1, M)
        psit_th = psit_c @ self.Sd_fc.T
        psit_q = psit_cq @ self.S_fc.T
        S = g['S'][:, None]
        Ur = -psit_th
        Uth = (2.0 + g['omega_v'])[:, None] * psit + S * psit_q
        c = 0.5 * J2[..., 0, 0]
        return dict(Ur=Ur, Uth=Uth, c=c, psit_n=psit_n, psit_nq=psit_nq, bq=bq, Fn=Fn, J1=J1, J2=J2)

    def residual(self, b, cl, g=None, lu=None, flds=None):
        """Ehat on all nodes (..., N+1, M) (row q = 0 is the identity defect times b) and the identity defect (...)."""
        if g is None: g = self.geom(cl)
        if flds is None: flds = self.fields(b, cl, g, lu)
        k = g['k']
        bth = self.ang.dtheta(b, 'EE')
        bq = flds['bq']
        c3 = (3.0 + g['omega_w'])[:, None]; S = g['S'][:, None]
        E = (cl * (1.0 - k) * g['omP1'])[:, None] * bq + flds['Ur'] * (c3 * b + S * bq) \
            + flds['Uth'] * (self.PiPi * b + bth) + ((3.0 * cl - 1.0) * g['P1_over_omq'])[:, None] * b
        ident = 3.0 * cl - 1.0 - flds['c']
        return E, ident

    # ---- unknown vector <-> (b, cl) -----------------------------------------------------------
    def pack(self, b, cl):
        return torch.cat([b[1:, :].reshape(-1), torch.as_tensor([float(cl)], device=self.dev)])

    def unpack(self, x):
        N, M = self.N, self.M
        b = torch.cat([torch.ones(1, M, device=self.dev), x[:N * M].reshape(N, M)], dim=0)
        return b, x[N * M]

    def F(self, x):
        b, cl = self.unpack(x)
        E, ident = self.residual(b, cl)
        return torch.cat([E[1:, :].reshape(-1), ident.reshape(1)])

    def F_batch(self, bb, cl, g, lu):
        """bb: (B, N+1, M) -> (B, N*M + 1)."""
        E, ident = self.residual(bb, cl, g, lu)
        return torch.cat([E[:, 1:, :].reshape(bb.shape[0], -1), ident.reshape(-1, 1)], dim=1)

    def jacobian(self, x, batch=256, verbose=False):
        """Dense Jacobian (n x n), n = N M + 1.  b-columns by exact central differences (Ehat is quadratic in b);
        c_l column by forward-mode AD."""
        N, M = self.N, self.M
        n = N * M + 1
        b, cl = self.unpack(x)
        g = self.geom(cl)
        gp = g if self.Npsi == self.N else self.geom(cl, self.qpsi)
        A1, A2 = self.poisson_matrices(gp)
        lu = (torch.linalg.lu_factor(A1), torch.linalg.lu_factor(A2))
        J = torch.empty(n, n, device=self.dev)
        t0 = time.time()
        for start in range(0, N * M, batch):
            idx = torch.arange(start, min(start + batch, N * M), device=self.dev)
            B = idx.numel()
            Eb = torch.zeros(B, N + 1, M, device=self.dev)
            ii = idx // M + 1; jj = idx % M
            Eb[torch.arange(B, device=self.dev), ii, jj] = 1.0
            Fp = self.F_batch(b[None] + Eb, cl, g, lu)
            Fm = self.F_batch(b[None] - Eb, cl, g, lu)
            J[:, start:start + B] = (0.5 * (Fp - Fm)).T
            if verbose and (start // batch) % 20 == 0:
                print(f'  jac cols {start}/{N*M}  {time.time()-t0:.1f}s', flush=True)
        # c_l column
        def Fcl(c):
            E, ident = self.residual(b, c)
            return torch.cat([E[1:, :].reshape(-1), ident.reshape(1)])
        _, dF = torch.func.jvp(Fcl, (cl.detach().clone(),), (torch.ones((), device=self.dev),))
        J[:, n - 1] = dF
        return J

    # ---- Newton ------------------------------------------------------------------------------
    def newton(self, x, maxit=12, tol=1e-13, verbose=True, log=None, damping=True, fix_cl=False, batch=256):
        hist = []
        for it in range(maxit):
            t0 = time.time()
            Fx = self.F(x)
            nF = Fx.abs().max().item(); nF2 = Fx.norm().item()
            b, cl = self.unpack(x)
            msg = f'newton it {it}: |F|_inf {nF:.3e} |F|_2 {nF2:.3e} c_l {cl.item():.10f}'
            if verbose: print(msg, flush=True)
            if log is not None: log.write(msg + '\n'); log.flush()
            hist.append((it, nF, nF2, cl.item()))
            if nF < tol: break
            J = self.jacobian(x, batch=batch)
            if fix_cl:
                # keep c_l: drop the identity row and the c_l column
                n = J.shape[0]
                dx_b = torch.linalg.solve(J[:n - 1, :n - 1], -Fx[:n - 1])
                dx = torch.cat([dx_b, torch.zeros(1, device=self.dev)])
            else:
                dx = torch.linalg.solve(J, -Fx)
            lam = 1.0
            if damping:
                for _ in range(8):
                    xn = x + lam * dx
                    nFn = self.F(xn).abs().max().item()
                    if nFn < nF or nF < 1e-11: break
                    lam *= 0.5
            x = x + lam * dx
            if verbose: print(f'   step |dx|_inf {dx.abs().max().item():.3e}  lam {lam}  dc_l {dx[-1].item():.3e}  ({time.time()-t0:.1f}s)', flush=True)
        return x, hist


    # ---- Levenberg-Marquardt / trust-region Newton ------------------------------------------------
    def newton_lm(self, x, maxit=30, tol=1e-12, Delta=0.05, verbose=True, log=None, batch=256, ksub=24, full_svd_limit=12000,
                  fix_cl=False):
        """Trust-region step: dx = -V diag(s/(s^2 + mu)) U^T F with mu chosen so that |dx|_inf <= Delta.  For n <= full_svd_limit the
        full SVD is used; otherwise the Newton step is damped only in the subspace of the ksub smallest singular triplets
        (block inverse iteration on J^T J).  Delta grows by 2 after a step with actual/predicted decrease > 0.5 and shrinks by 4
        after a rejected step."""
        def P(msg):
            if verbose: print(msg, flush=True)
            if log is not None: log.write(msg + '\n'); log.flush()
        hist = []
        Fx = self.F(x); nF = Fx.norm().item()
        for it in range(maxit):
            t0 = time.time()
            b, cl = self.unpack(x)
            P(f'lm it {it}: |F|_inf {Fx.abs().max().item():.3e} |F|_2 {nF:.3e} c_l {cl.item():.10f} Delta {Delta:.2e}')
            hist.append((it, Fx.abs().max().item(), nF, cl.item()))
            if Fx.abs().max().item() < tol: break
            J = self.jacobian(x, batch=batch)
            n = J.shape[0]
            if fix_cl:
                J = J[:n - 1, :n - 1]; Fr = Fx[:n - 1]
            else:
                Fr = Fx
            if J.shape[0] <= full_svd_limit:
                U, S, Vh = torch.linalg.svd(J)
                g = U.T @ Fr                                  # components of F in the left singular basis
                def step(mu):
                    coef = -S / (S * S + mu) * g
                    return Vh.T @ coef
                LU = None
            else:
                LU = torch.linalg.lu_factor(J)
                dxN = torch.linalg.lu_solve(*LU, -Fr[:, None])[:, 0]
                V = torch.randn(J.shape[0], ksub, device=J.device)
                for _ in range(30):
                    Y = torch.linalg.lu_solve(*LU, V, adjoint=True); Z = torch.linalg.lu_solve(*LU, Y); V, _ = torch.linalg.qr(Z)
                JV = J @ V; Uk, sk, Wk = torch.linalg.svd(JV, full_matrices=False); Vk = V @ Wk.T
                proj = Vk.T @ dxN                            # components of the Newton step along the soft directions
                def step(mu):
                    return dxN - Vk @ (proj * (mu / (sk * sk + mu)))
            # choose mu: smallest mu (most Newton-like) with |dx|_inf <= Delta, by bisection in log mu
            dx = step(0.0)
            if dx.abs().max().item() > Delta:
                lo, hi = -30.0, 30.0
                for _ in range(60):
                    mid = 0.5 * (lo + hi); d = step(10.0 ** mid)
                    if d.abs().max().item() > Delta: lo = mid
                    else: hi = mid
                mu = 10.0 ** hi; dx = step(mu)
            else:
                mu = 0.0
            if fix_cl: dx = torch.cat([dx, torch.zeros(1, device=self.dev)])
            # predicted decrease of |F|_2^2 (linear model) and actual
            pred = nF ** 2 - (Fr + (J @ dx[:J.shape[1]])).norm().item() ** 2
            xn = x + dx; Fn = self.F(xn); nFn = Fn.norm().item()
            act = nF ** 2 - nFn ** 2
            ratio = act / pred if pred > 0 else -1.0
            P(f'   mu {mu:.2e} |dx|_inf {dx.abs().max().item():.3e} dc_l {dx[-1].item():+.3e}  |F|_2 -> {nFn:.3e}  ratio {ratio:.3f}  ({time.time()-t0:.1f}s)')
            if act > 0 and ratio > 0.1:
                x, Fx, nF = xn, Fn, nFn
                if ratio > 0.5: Delta = min(Delta * 2.0, 1.0)
            else:
                Delta = Delta / 4.0
                if Delta < 1e-10: P('   trust radius collapsed'); break
        return x, hist

    # ---- interpolant at arbitrary points --------------------------------------------------------
    def q_of_r(self, r, cl):
        k = 1.0 / cl; u2 = (np.asarray(r, float) / self.L) ** 2
        return 1.0 - (1.0 + u2) ** (-(1.0 - k) / 2.0)

    def eval_EE(self, vals, q, th):
        """vals: (N+1, M) coarse EE values (numpy or tensor).  q, th: arrays of the same shape.  Barycentric in q,
        exact cos(2m s(theta)) sum in theta.  Returns numpy array."""
        V = vals.detach().cpu().numpy() if torch.is_tensor(vals) else np.asarray(vals)
        q = np.asarray(q, float).ravel(); th = np.asarray(th, float).ravel()
        C = V @ self.ang.A['EE'].cpu().numpy().T                    # (N+1, M) mode coefficients in s
        Pq = interp_matrix(self.q_np, q, self.wq_np)                # (P, N+1)
        Cq = Pq @ C                                                 # (P, M)
        m = np.arange(self.M)
        sth = self.ang.s_of_theta(th)
        return np.sum(Cq * np.cos(np.outer(sth, 2 * m)), axis=1)

    def eval_modes(self, modes, q, th, cls_n, deriv_th=0):
        """modes: (Npsi+1, K) radial mode functions (on the fine psi grid) for sin(n theta); cls_n: the array of n."""
        V = modes.detach().cpu().numpy() if torch.is_tensor(modes) else np.asarray(modes)
        q = np.asarray(q, float).ravel(); th = np.asarray(th, float).ravel()
        Pq = interp_matrix(self.qpsi_np, q, self.wqpsi_np)
        Cq = Pq @ V
        n = np.asarray(cls_n, float)
        if deriv_th == 0: ang = np.sin(np.outer(th, n))
        elif deriv_th == 1: ang = n[None, :] * np.cos(np.outer(th, n))
        else: ang = -(n[None, :] ** 2) * np.sin(np.outer(th, n))
        return np.sum(Cq * ang, axis=1)


# ----------------------------------------------------------------------------------------------
# state I/O
# ----------------------------------------------------------------------------------------------
def save_state(path, model, x, extra=None):
    b, cl = model.unpack(x)
    d = dict(N=model.N, M=model.M, L=model.L, beta=model.beta, nmodes=model.nmodes, Mq=model.Mq, Npsi=model.Npsi, b=b.detach().cpu().numpy(),
             c_l=float(cl), q=model.q_np, theta=model.ang.theta_np)
    if extra: d.update(extra)
    np.savez(path, **d)


def load_state(path, device='cuda'):
    d = np.load(path, allow_pickle=True)
    model = Model(int(d['N']), int(d['M']), float(d['L']), device=device, beta=float(d['beta']) if 'beta' in d.files else 0.0,
                  nmodes=int(d['nmodes']) if 'nmodes' in d.files else None, Mq=int(d['Mq']) if 'Mq' in d.files else None,
                  Npsi=int(d['Npsi']) if 'Npsi' in d.files else None)
    b = torch.tensor(d['b'], device=model.dev)
    x = model.pack(b, float(d['c_l']))
    return model, x, d


def project_state(model_from, x_from, model_to):
    """Interpolate b from one grid to another (same c_l).  b is smooth in (q, theta) up to the class regularity."""
    b, cl = model_from.unpack(x_from)
    cl = float(cl)
    # target nodes (q, theta): need the same radii, not the same q (q depends on k only, which is shared, but L may differ)
    r_to, _, _ = model_to.radii(cl)
    q_in_from = model_from.q_of_r(np.minimum(r_to, 1e300), cl)
    q_in_from[-1] = 1.0
    Q, TH = np.meshgrid(q_in_from, model_to.ang.theta_np, indexing='ij')
    vals = model_from.eval_EE(b, Q, TH).reshape(model_to.N + 1, model_to.M)
    # the far-field amplitude changes with L: rho = r^3 w Pi b, w = (1+ (r/L)^2)^((k-3)/2) -> b_to = b_from * w_from/w_to
    k = 1.0 / cl
    with np.errstate(divide='ignore', invalid='ignore'):
        ratio = ((1.0 + (r_to / model_from.L) ** 2) / (1.0 + (r_to / model_to.L) ** 2)) ** ((k - 3.0) / 2.0)
    ratio[-1] = (model_to.L / model_from.L) ** (k - 3.0)
    vals = vals * ratio[:, None]
    vals[0, :] = 1.0
    b_to = torch.tensor(vals, device=model_to.dev)
    return model_to.pack(b_to, cl)
