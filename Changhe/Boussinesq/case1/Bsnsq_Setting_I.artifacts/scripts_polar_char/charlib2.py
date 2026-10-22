"""charlib2: Psi-only characteristic (slaved-transport) representation on the GPU, batched over coefficient vectors.
Mathematics as in charlib_gpu.py (same basis, jets and propagator); implementation differences:
  * Chebyshev polynomials and their q-derivatives via T_k = cos(k theta), theta = arccos(2q-1), computed with one complex
    cumulative product (no recurrence loop); dT/dx = k sin(k theta)/sin theta, d2T/dx2 = (x T' - k^2 T)/(1-x^2);
  * all B*N points are integrated in lockstep without gathering; finished points (|Y| < r_stop) are frozen by a mask.
"""
import math, numpy as np, torch
DT = torch.float64

def dev():
    return torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def cheb_all(q, K):
    """T_k(2q-1), d/dq T_k, d2/dq2 T_k for k=0..K-1, q (...) in (0,1). Returns (..., K) x 3."""
    x = (2.0 * q - 1.0).clamp(-1.0 + 1e-15, 1.0 - 1e-15)
    th = torch.acos(x)
    k = torch.arange(K, dtype=DT, device=q.device)
    kth = th[..., None] * k
    T = torch.cos(kth); Sk = torch.sin(kth)
    s = torch.sin(th)[..., None]
    Dx = k * Sk / s                                     # dT/dx
    D2x = (x[..., None] * Dx - k * k * T) / (1.0 - x[..., None] * x[..., None])
    return T, 2.0 * Dx, 4.0 * D2x

class PsiBasis:
    def __init__(self, beta, NO, K, L=1.0, gamma_P=None, mu=None):
        self.beta = float(beta); self.NO = NO; self.K = K; self.L = float(L)
        self.mu = (1.0 / beta) if mu is None else float(mu)
        self.gamma_P = (2.0 - 1.0 / beta) if gamma_P is None else float(gamma_P)
        self.ms = [2 * n for n in range(1, NO + 1)]

    def q_of_u(self, u):
        return 1.0 - (1.0 + u * u) ** (-self.mu / 2)

    def u_of_q(self, q):
        E = (1.0 - q) ** (-2.0 / self.mu)
        return torch.sqrt(torch.clamp(E - 1.0, min=0.0))

    def ms_t(self, device):
        return torch.tensor(self.ms, dtype=DT, device=device)

    def fields(self, cP, x, y, need_second=True):
        """cP (B, NO, K); x, y (B, N) or (N,). Returns dict of (B, N): Psi, Psi_x, Psi_y[, Psi_xx, Psi_xy, Psi_yy, Om = -Lap Psi]."""
        if cP.dim() == 2: cP = cP[None]
        B = cP.shape[0]
        if x.dim() == 1: x = x[None].expand(B, -1); y = y[None].expand(B, -1)
        dvc = x.device
        r = torch.sqrt(x * x + y * y); cs = x / r; sn = y / r
        u = r / self.L; E = 1.0 + u * u; q = 1.0 - E ** (-self.mu / 2)
        # Chebyshev contractions with the k and k^2 factors folded into the coefficient matrices (less memory traffic):
        #   PT = sum_k c_k T_k,  PD = d/dq sum_k c_k T_k = 2 (sum_k k c_k sin k.th)/sin th,
        #   PD2 = d2/dq2 ... = 4 (x PDx - sum_k k^2 c_k T_k)/(1-x^2),  x = 2q-1 = cos th
        xx = (2.0 * q - 1.0).clamp(-1.0 + 1e-15, 1.0 - 1e-15)
        th = torch.acos(xx); sth = torch.sin(th)
        kk = torch.arange(self.K, dtype=DT, device=dvc)
        kth = th[..., None] * kk
        cT = cP.transpose(1, 2)                                       # (B, K, NO)
        PT = torch.cos(kth) @ cT
        PDx = (torch.sin(kth) @ (kk[:, None] * cT)) / sth[..., None]
        PD = 2.0 * PDx
        if need_second:
            PD2 = 4.0 * (xx[..., None] * PDx - torch.cos(kth) @ ((kk * kk)[:, None] * cT)) / (1.0 - xx * xx)[..., None]
        mu = self.mu
        qp = mu * u * E ** (-mu / 2 - 1)
        qpp = mu * E ** (-mu / 2 - 1) - mu * (mu + 2) * u * u * E ** (-mu / 2 - 2)
        ms = self.ms_t(dvc)                                           # (NO,)
        lu = torch.log(torch.clamp(u, min=1e-300))[..., None]; lE = torch.log(E)[..., None]
        a = (self.gamma_P - ms) / 2.0
        # envelope A*B = u^m E^a and its u-derivatives, all through a single exponential (no overflow at large u)
        L0 = ms * lu + a * lE
        AB = torch.exp(L0)
        AB1 = ms * torch.exp(L0 - lu) + 2 * a * u[..., None] * torch.exp(L0 - lE)          # A1 B + A B1
        C = PT; C1 = PD * qp[..., None]
        p = AB * C
        dp = (AB1 * C + AB * C1) / self.L
        phi = torch.atan2(y, x)
        S = torch.sin(phi[..., None] * ms); Cc = torch.cos(phi[..., None] * ms)
        f = (p * S).sum(-1); fr = (dp * S).sum(-1); fphi = (p * ms * Cc).sum(-1)
        out = dict(Psi=f, r=r)
        out['Psi_x'] = cs * fr - sn * fphi / r
        out['Psi_y'] = sn * fr + cs * fphi / r
        if need_second:
            AB2 = (ms * (ms - 1) * torch.exp(L0 - 2 * lu) + 4 * a * ms * u[..., None] * torch.exp(L0 - lu - lE)
                   + torch.exp(L0 - lE) * (2 * a + 4 * a * (a - 1) * (u * u)[..., None] / E[..., None]))   # A2 B + 2 A1 B1 + A B2
            C2 = PD2 * (qp * qp)[..., None] + PD * qpp[..., None]
            d2p = (AB2 * C + 2 * AB1 * C1 + AB * C2) / self.L ** 2
            frr = (d2p * S).sum(-1); frphi = (dp * ms * Cc).sum(-1); fpp = -(p * ms * ms * S).sum(-1)
            out['Om'] = -(frr + fr / r + fpp / (r * r))
            t1 = frphi / r - fphi / (r * r); t2 = fr / r + fpp / (r * r)
            out['Psi_xx'] = cs * cs * frr - 2 * sn * cs * t1 + sn * sn * t2
            out['Psi_yy'] = sn * sn * frr + 2 * sn * cs * t1 + cs * cs * t2
            out['Psi_xy'] = sn * cs * (frr - t2) + (cs * cs - sn * sn) * t1
        return out

    def radial_matrices(self, r):
        """H, dH (N, NO, K): radial basis functions p_{n,k}(r) and d/dr for all modes at radii r (N,); env (N, NO)."""
        u = r / self.L; E = 1.0 + u * u; q = 1.0 - E ** (-self.mu / 2)
        T, D, _ = cheb_all(q, self.K)
        ms = self.ms_t(r.device); a = (self.gamma_P - ms) / 2.0
        lu = torch.log(torch.clamp(u, min=1e-300))[:, None]; lE = torch.log(E)[:, None]
        L0 = ms * lu + a * lE
        AB = torch.exp(L0); AB1 = ms * torch.exp(L0 - lu) + 2 * a * u[:, None] * torch.exp(L0 - lE)
        qp = (self.mu * u * E ** (-self.mu / 2 - 1))[:, None]
        H = AB[:, :, None] * T[:, None, :]
        dH = (AB1[:, :, None] * T[:, None, :] + AB[:, :, None] * qp[:, :, None] * D[:, None, :]) / self.L
        return H, dH, AB

    def centre_functionals(self, device):
        """Linear functionals (NO*K,) for c, h10, h01 in Psi = xy(c + h10 x^2 + h01 y^2 + ...)."""
        K = self.K; sgn = torch.tensor([(-1.0) ** k for k in range(K)], dtype=DT, device=device)
        dsgn = torch.tensor([(-1.0) ** (k + 1) * k * k * 2.0 for k in range(K)], dtype=DT, device=device)
        n = self.NO * K
        vc = torch.zeros(n, dtype=DT, device=device); vc[:K] = 2.0 * sgn / self.L ** 2
        a1 = (self.gamma_P - 2) / 2.0
        p12 = (a1 * sgn + 0.5 * self.mu * dsgn) / self.L ** 4
        v10 = torch.zeros(n, dtype=DT, device=device); v01 = torch.zeros(n, dtype=DT, device=device)
        v10[:K] = 2.0 * p12; v01[:K] = 2.0 * p12
        if self.NO > 1:
            v10[K:2 * K] = 4.0 * sgn / self.L ** 4; v01[K:2 * K] = -4.0 * sgn / self.L ** 4
        return dict(c=vc, h10=v10, h01=v01)


def jets(beta, a0, h10, h01):
    f10 = -3.0 * a0 * h10 / (2 * beta + 4); f01 = -a0 * h01 / (2 * beta - 4); g00 = 2.0 * f10 / (2 * beta + 1)
    return f10, f01, g00


def transport(basis, cP, a0, beta, x, y, dt=0.005, r_stop=1e-3, T_max=60.0):
    """Slaved transport at points (x, y) (N,) for the coefficient batch cP (B, NO, K), amplitude a0 (B,) or scalar.
    Returns dict (B, N): Th, Thx, Thy, Om (reconstructed), T (backward time), fail; and c, h10, h01 (B,)."""
    dvc = x.device
    if cP.dim() == 2: cP = cP[None]
    B = cP.shape[0]; N = x.shape[0]
    a0 = torch.as_tensor(a0, dtype=DT, device=dvc).reshape(-1)
    if a0.numel() == 1: a0 = a0.expand(B)
    F = basis.centre_functionals(dvc); cflat = cP.reshape(B, -1)
    cval = cflat @ F['c']; h10 = cflat @ F['h10']; h01 = cflat @ F['h01']
    b = beta - 2.0
    X = x[None].expand(B, -1).clone(); Y = y[None].expand(B, -1).clone()
    P = torch.eye(3, dtype=DT, device=dvc).expand(B, N, 3, 3).clone()
    Tt = torch.zeros(B, N, dtype=DT, device=dvc)
    active = torch.ones(B, N, dtype=torch.bool, device=dvc)
    def rhs(Xc, Yc, Pc):
        o = basis.fields(cP, Xc, Yc)
        W1 = beta * Xc - o['Psi_y']; W2 = beta * Yc + o['Psi_x']
        M = torch.zeros(B, N, 3, 3, dtype=DT, device=dvc)
        M[..., 0, 0] = b - (beta - o['Psi_xy']); M[..., 0, 1] = -o['Psi_xx']
        M[..., 1, 0] = o['Psi_yy']; M[..., 1, 1] = b - (beta + o['Psi_xy'])
        M[..., 2, 0] = 1.0; M[..., 2, 2] = -1.0
        return -W1, -W2, Pc @ M
    nsteps = 0
    while bool(active.any()) and nsteps * dt < T_max:
        k1x, k1y, k1p = rhs(X, Y, P)
        k2x, k2y, k2p = rhs(X + 0.5 * dt * k1x, Y + 0.5 * dt * k1y, P + 0.5 * dt * k1p)
        k3x, k3y, k3p = rhs(X + 0.5 * dt * k2x, Y + 0.5 * dt * k2y, P + 0.5 * dt * k2p)
        k4x, k4y, k4p = rhs(X + dt * k3x, Y + dt * k3y, P + dt * k3p)
        am = active.to(DT)
        X = X + am * (dt / 6) * (k1x + 2 * k2x + 2 * k3x + k4x)
        Y = Y + am * (dt / 6) * (k1y + 2 * k2y + 2 * k3y + k4y)
        P = P + am[..., None, None] * (dt / 6) * (k1p + 2 * k2p + 2 * k3p + k4p)
        Tt = Tt + am * dt
        active = active & ((X * X + Y * Y) >= r_stop * r_stop)
        bad = ~(torch.isfinite(X) & torch.isfinite(Y) & torch.isfinite(P).all(-1).all(-1))
        active = active & ~bad
        X = torch.where(bad, torch.full_like(X, float('nan')), X)
        nsteps += 1
    f10, f01, g00 = jets(beta, a0[:, None], h10[:, None], h01[:, None])
    Th0 = Y * (a0[:, None] + f10 * X * X + f01 * Y * Y)
    V0 = torch.stack([2 * f10 * X * Y, a0[:, None] + f10 * X * X + 3 * f01 * Y * Y, g00 * X * Y], -1)
    V = torch.einsum('bnij,bnj->bni', P, V0)
    Th = torch.exp(b * Tt) * Th0
    fail = active | ~torch.isfinite(X) | ~torch.isfinite(V).all(-1)
    return dict(Th=Th, Thx=V[..., 0], Thy=V[..., 1], Om=V[..., 2], T=Tt, fail=fail, nsteps=nsteps, c=cval, h10=h10, h01=h01, Xend=X, Yend=Y)
