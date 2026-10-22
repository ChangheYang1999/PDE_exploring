"""charlib_gpu: Psi-only characteristic (slaved-transport) representation on the GPU.

Unknowns: Chebyshev coefficients of the stream function modes
    Psi(r,phi) = sum_{n=1}^{NO} p_n(r) sin(2n phi),   p_n = (u^2/E)^{n} E^{gamma_P/2} T_k(2q-1) coefficients (K per mode),
    u = r/L, E = 1+u^2, q = 1-E^{-mu/2}, gamma_P = 2 - 1/beta (far-field exponent of Psi for W ~ beta X), mu = 1/beta.
Psi in this basis is smooth at the origin (p_n ~ u^{2n}) and O(r^{gamma_P}) at infinity, hence it is the canonical
full-plane inverse of its own Laplacian (no harmonic function with these parities is smooth and o(r^2)).
Omega_basis = -Lap Psi exactly (closed form).  U = (-Psi_y, Psi_x), W = beta X + U, DW exact.

Transport reconstruction (slaved Theta and Omega): for an evaluation point X integrate backward
    dY/ds = -W(Y),  dP/ds = P M(Y),  P(0) = I_3,  M = [[b - W1_x, -W2_x, 0], [-W1_y, b - W2_y, 0], [1, 0, -1]],  b = beta-2,
until |Y| < r_stop; then with the centre jets (Psi = xy(-2 + h10 x^2 + h01 y^2 + ...), Theta = y(a0 + f10 x^2 + f01 y^2 + ...),
Omega = g00 xy + ...; f10 = -3 a0 h10/(2beta+4), f01 = -a0 h01/(2beta-4), g00 = 2 f10/(2beta+1))
    V(X) = P(T) V(Y(T)),  V = (Theta_x, Theta_y, Omega),   Theta(X) = e^{bT} Theta_jet(Y(T)).
These satisfy (P1), (P2) exactly along characteristics; the only remaining equation is Omega_basis = Omega_char.
"""
import math, numpy as np, torch
DT = torch.float64

def dev():
    return torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def cheb_T_d1_d2(q, K):
    """T_k(2q-1), d/dq, d2/dq2 for k = 0..K-1; q (...). Returns three (..., K) tensors."""
    x = 2.0 * q - 1.0
    T = [torch.ones_like(q)]; D = [torch.zeros_like(q)]; D2 = [torch.zeros_like(q)]
    if K > 1:
        T.append(x); D.append(torch.ones_like(q)); D2.append(torch.zeros_like(q))
    for k in range(2, K):
        T.append(2 * x * T[-1] - T[-2])
        D.append(2 * T[-2] + 2 * x * D[-1] - D[-2])
        D2.append(4 * D[-2] + 2 * x * D2[-1] - D2[-2])
    T = torch.stack(T, -1); D = 2.0 * torch.stack(D, -1); D2 = 4.0 * torch.stack(D2, -1)
    return T, D, D2

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

    def radial(self, r):
        """Radial functions and derivatives for all modes: returns H, dH, d2H of shape (..., NO, K) (derivatives w.r.t. r)."""
        u = r / self.L
        E = 1.0 + u * u
        q = 1.0 - E ** (-self.mu / 2)
        T, D, D2 = cheb_T_d1_d2(q, self.K)                       # (..., K)
        mu = self.mu
        qp = mu * u * E ** (-mu / 2 - 1)                            # dq/du
        qpp = mu * E ** (-mu / 2 - 1) - mu * (mu + 2) * u * u * E ** (-mu / 2 - 2)
        C = T; C1 = D * qp[..., None]; C2 = D2 * (qp * qp)[..., None] + D * qpp[..., None]
        Hs = []; dHs = []; d2Hs = []
        lu = torch.log(torch.clamp(u, min=1e-300)); lE = torch.log(E)
        for m in self.ms:
            a = (self.gamma_P - m) / 2.0
            A = torch.exp(m * lu); A1 = m * torch.exp((m - 1) * lu); A2 = m * (m - 1) * torch.exp((m - 2) * lu) if m > 2 else 2.0 * torch.ones_like(u)
            if m == 2: A1 = 2.0 * u
            B = torch.exp(a * lE); B1 = 2 * a * u * torch.exp((a - 1) * lE); B2 = 2 * a * torch.exp((a - 1) * lE) + 4 * a * (a - 1) * u * u * torch.exp((a - 2) * lE)
            AB = A * B; AB1 = A1 * B + A * B1; AB2 = A2 * B + 2 * A1 * B1 + A * B2
            H = AB[..., None] * C
            dH = AB1[..., None] * C + AB[..., None] * C1
            d2H = AB2[..., None] * C + 2 * AB1[..., None] * C1 + AB[..., None] * C2
            Hs.append(H); dHs.append(dH); d2Hs.append(d2H)
        H = torch.stack(Hs, -2); dH = torch.stack(dHs, -2) / self.L; d2H = torch.stack(d2Hs, -2) / self.L ** 2
        return H, dH, d2H

    def fields(self, cP, x, y, need_second=True):
        """cP: (B, NO, K) or (NO, K); x, y: (N,) [or (B, N)]. Returns dict with Psi, Psi_x, Psi_y, and if need_second
        Psi_xx, Psi_xy, Psi_yy, Om (= -Lap Psi).  Shapes (B, N) (B = 1 if cP unbatched; squeezed)."""
        squeeze = cP.dim() == 2
        if squeeze: cP = cP[None]
        B = cP.shape[0]
        if x.dim() == 1: x = x[None].expand(B, -1); y = y[None].expand(B, -1)
        r = torch.sqrt(x * x + y * y); cs = x / r; sn = y / r
        phi = torch.atan2(y, x)
        H, dH, d2H = self.radial(r)                                 # (B, N, NO, K)
        p = torch.einsum('bnmk,bmk->bnm', H, cP); dp = torch.einsum('bnmk,bmk->bnm', dH, cP)
        d2p = torch.einsum('bnmk,bmk->bnm', d2H, cP) if need_second else None
        ms = torch.tensor(self.ms, dtype=DT, device=x.device)
        S = torch.sin(phi[..., None] * ms); Cc = torch.cos(phi[..., None] * ms)
        f = (p * S).sum(-1); fr = (dp * S).sum(-1); fphi = (p * ms * Cc).sum(-1)
        out = dict(Psi=f, r=r)
        out['Psi_x'] = cs * fr - sn * fphi / r
        out['Psi_y'] = sn * fr + cs * fphi / r
        if need_second:
            frr = (d2p * S).sum(-1); frphi = (dp * ms * Cc).sum(-1); fpp = -(p * ms * ms * S).sum(-1)
            lap = frr + fr / r + fpp / (r * r)
            out['Om'] = -lap
            t1 = frphi / r - fphi / (r * r)
            t2 = fr / r + fpp / (r * r)
            out['Psi_xx'] = cs * cs * frr - 2 * sn * cs * t1 + sn * sn * t2
            out['Psi_yy'] = sn * sn * frr + 2 * sn * cs * t1 + cs * cs * t2
            out['Psi_xy'] = sn * cs * (frr - t2) + (cs * cs - sn * sn) * t1
        if squeeze:
            out = {k: v[0] for k, v in out.items()}
        return out

    # ---- centre functionals (linear in cP): Psi = xy(c + h10 x^2 + h01 y^2 + ...)
    def centre_functionals(self, device):
        """Vectors (NO*K,) for c, h10, h01. Near 0: p_1 = u^2 E^{a1} T(q) ~ u^2 [P(0) + u^2 (a1 P(0) + (mu/2) P'(0))],
        p_2 ~ u^4 P_2(0).  r^2 sin2phi = 2xy; r^4 sin2phi = 2xy(x^2+y^2); r^4 sin4phi = 4xy(x^2-y^2)."""
        K = self.K; sgn = torch.tensor([(-1.0) ** k for k in range(K)], dtype=DT, device=device)
        dsgn = torch.tensor([(-1.0) ** (k + 1) * k * k * 2.0 for k in range(K)], dtype=DT, device=device)   # d/dq T_k(2q-1) at q=0
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


def transport(basis, cP, a0, beta, x, y, dt=0.005, r_stop=1e-3, T_max=60.0, return_T=False):
    """Slaved transport reconstruction at points (x, y) (N,) for coefficient batch cP (B, NO, K) and a0 (B,) or float.
    Returns Theta, Theta_x, Theta_y, Omega_char (B, N), plus the basis Omega at the points, and bookkeeping."""
    device = x.device
    if cP.dim() == 2: cP = cP[None]
    B = cP.shape[0]; N = x.shape[0]
    a0 = torch.as_tensor(a0, dtype=DT, device=device).reshape(-1)
    if a0.numel() == 1: a0 = a0.expand(B)
    F = basis.centre_functionals(device)
    cflat = cP.reshape(B, -1)
    cval = cflat @ F['c']; h10 = cflat @ F['h10']; h01 = cflat @ F['h01']
    b = beta - 2.0
    # state: Y (B, N, 2), P (B, N, 3, 3), time (B, N)
    Y = torch.stack([x[None].expand(B, -1), y[None].expand(B, -1)], -1).clone()
    Pm = torch.eye(3, dtype=DT, device=device).expand(B, N, 3, 3).clone()
    Tt = torch.zeros(B, N, dtype=DT, device=device)
    active = torch.ones(B, N, dtype=torch.bool, device=device)
    # flat active bookkeeping over (B, N)
    def rhs(Yf, bidx):
        # Yf (A, 2), bidx (A,) batch index of each active point -> W (A, 2), M (A, 3, 3)
        cPa = cP[bidx]                                              # (A, NO, K)  (gather; A can be large)
        out = basis.fields(cPa, Yf[:, 0:1], Yf[:, 1:2])             # shapes (A, 1)
        Px, Py = out['Psi_x'][:, 0], out['Psi_y'][:, 0]
        Pxx, Pxy, Pyy = out['Psi_xx'][:, 0], out['Psi_xy'][:, 0], out['Psi_yy'][:, 0]
        W1 = beta * Yf[:, 0] - Py; W2 = beta * Yf[:, 1] + Px
        W1x = beta - Pxy; W1y = -Pyy; W2x = Pxx; W2y = beta + Pxy
        M = torch.zeros(Yf.shape[0], 3, 3, dtype=DT, device=device)
        M[:, 0, 0] = b - W1x; M[:, 0, 1] = -W2x; M[:, 1, 0] = -W1y; M[:, 1, 1] = b - W2y; M[:, 2, 0] = 1.0; M[:, 2, 2] = -1.0
        return -torch.stack([W1, W2], -1), M
    nsteps = 0
    while True:
        idx = torch.nonzero(active)
        if idx.shape[0] == 0: break
        bi, ni = idx[:, 0], idx[:, 1]
        Ya = Y[bi, ni]; Pa = Pm[bi, ni]
        k1y, M1 = rhs(Ya, bi); k1p = Pa @ M1
        k2y, M2 = rhs(Ya + 0.5 * dt * k1y, bi); k2p = (Pa + 0.5 * dt * k1p) @ M2
        k3y, M3 = rhs(Ya + 0.5 * dt * k2y, bi); k3p = (Pa + 0.5 * dt * k2p) @ M3
        k4y, M4 = rhs(Ya + dt * k3y, bi); k4p = (Pa + dt * k3p) @ M4
        Yn = Ya + dt / 6 * (k1y + 2 * k2y + 2 * k3y + k4y)
        Pn = Pa + dt / 6 * (k1p + 2 * k2p + 2 * k3p + k4p)
        Y[bi, ni] = Yn; Pm[bi, ni] = Pn; Tt[bi, ni] += dt
        rn = torch.sqrt((Yn * Yn).sum(-1))
        done = (rn < r_stop) | (Tt[bi, ni] > T_max)
        active[bi[done], ni[done]] = False
        nsteps += 1
    # jets at the end points
    f10, f01, g00 = jets(beta, a0[:, None], h10[:, None], h01[:, None])
    x0, y0 = Y[..., 0], Y[..., 1]
    Th0 = y0 * (a0[:, None] + f10 * x0 * x0 + f01 * y0 * y0)
    V0 = torch.stack([2 * f10 * x0 * y0, a0[:, None] + f10 * x0 * x0 + 3 * f01 * y0 * y0, g00 * x0 * y0], -1)   # (B, N, 3)
    V = torch.einsum('bnij,bnj->bni', Pm, V0)
    Th = torch.exp(b * Tt) * Th0
    fail = (torch.sqrt(x0 * x0 + y0 * y0) >= r_stop)
    out = dict(Th=Th, Thx=V[..., 0], Thy=V[..., 1], Om=V[..., 2], T=Tt, fail=fail, nsteps=nsteps, c=cval, h10=h10, h01=h01)
    return out
