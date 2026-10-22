"""
polarlib: polar-modal discretization for the A1 Boussinesq self-similar profile problem.

Theta(r,th) = sum_{n=0}^{NT-1} f_n(r) sin((2n+1) th)      (even in x, odd in y)
Omega(r,th) = sum_{n=1}^{NO}   g_n(r) sin(2n th)          (odd in x, odd in y)
Psi  (r,th) = sum_{n=1}^{NO}   psi_n(r) sin(2n th),  -Lap Psi = Omega (canonical full-plane inverse, modal Green formula)

Radial basis for a mode with angular wavenumber m and far-field exponent gamma:
   h(r) = (u^2/E)^{m/2} E^{gamma/2} P(q),  u = r/L, E = 1+u^2, q = 1 - E^{-mu/2}, P polynomial (Chebyshev in 2q-1).
Near 0: h ~ u^m * (smooth even function of u)  -> smooth 2D field. Far: h ~ u^gamma P(1) (1 + O(u^{-mu})).
Default exponents from W ~ beta X at infinity: gamma_Theta = 1-2/beta, gamma_Omega = -1/beta, mu = 1/beta.

Inverse: psi_n(r) = (1/(4n)) [J_in(r) + J_out(r)],  psi_n'(r) = (J_out - J_in)/(2r),
   J_in(r)  = int_0^r (s/r)^{2n} s g_n(s) ds,   J_out(r) = int_r^inf (r/s)^{2n} s g_n(s) ds,
computed by composite Gauss-Legendre quadrature in t = u^2 on panels between consecutive radii and an exact
tail integral in q on [q_last, 1) (closed from the basis's own analytic continuation).
All tensors are torch float64.
"""
import math
import numpy as np
import torch

DT = torch.float64


def dev():
    return torch.device('cuda' if torch.cuda.is_available() else 'cpu')


# ---------------------------------------------------------------- Chebyshev on [0,1]
def cheb_T_and_dT(q, K):
    """T_k(2q-1) and d/dq T_k(2q-1) for k=0..K-1. q: tensor (...). Returns (..., K). Autograd-safe."""
    x = 2.0 * q - 1.0
    Ts = [torch.ones_like(q)]
    dTs = [torch.zeros_like(q)]
    if K > 1:
        Ts.append(x)
        dTs.append(torch.ones_like(q))
    for k in range(2, K):
        Ts.append(2 * x * Ts[-1] - Ts[-2])
        dTs.append(2 * Ts[-2] + 2 * x * dTs[-1] - dTs[-2])
    T = torch.stack(Ts, -1)
    dT = 2.0 * torch.stack(dTs, -1)
    return T, dT


def cheb_integral_01(K):
    """int_0^1 T_k(2q-1) dq for k=0..K-1  (= (1/2) int_{-1}^1 T_k(x) dx)."""
    out = np.zeros(K)
    for k in range(K):
        if k % 2 == 0:
            out[k] = 0.5 * 2.0 / (1 - k * k)
    return torch.tensor(out, dtype=DT)


# ---------------------------------------------------------------- geometry maps
class Params:
    def __init__(self, beta, L=1.0, gamma_T=None, gamma_O=None, mu=None):
        self.beta = float(beta)
        self.L = float(L)
        self.mu = 1.0 / beta if mu is None else float(mu)
        self.gamma_T = (1.0 - 2.0 / beta) if gamma_T is None else float(gamma_T)
        self.gamma_O = (-1.0 / beta) if gamma_O is None else float(gamma_O)

    def q_of_u(self, u):
        return 1.0 - (1.0 + u * u) ** (-self.mu / 2)

    def u_of_q(self, q):
        E = (1.0 - q) ** (-2.0 / self.mu)
        return torch.sqrt(torch.clamp(E - 1.0, min=0.0))

    def t_of_q(self, q):
        return (1.0 - q) ** (-2.0 / self.mu) - 1.0


def radial_basis(P, r, m, gamma, K, deriv=True):
    """Radial basis h_k(r), h_k'(r) for angular wavenumber m, far-field exponent gamma, K Chebyshev modes.
    r: tensor (N,). Returns H (N,K), dH (N,K) [dH = None if deriv False].
    h = (u^2/E)^{m/2} E^{gamma/2} T_k(2q-1)."""
    u = r / P.L
    t = u * u
    E = 1.0 + t
    q = P.q_of_u(u)
    T, dT = cheb_T_and_dT(q, K)
    env = (t / E) ** (m / 2.0) * E ** (gamma / 2.0)
    H = env[:, None] * T
    if not deriv:
        return H, None
    # h' = (1/L) u^{m-1} E^{a-1} [ (m E + 2 a u^2) P + mu u^2 E^{-mu/2} P' ],  a = (gamma-m)/2
    a = (gamma - m) / 2.0
    pref = (t / E) ** ((m - 1) / 2.0) * E ** ((gamma - 3) / 2.0) / P.L   # = u^{m-1} E^{a-1} / L
    A = (m * E + 2 * a * t)
    B = P.mu * t * E ** (-P.mu / 2)
    dH = pref[:, None] * (A[:, None] * T + B[:, None] * dT)
    return H, dH


# ---------------------------------------------------------------- modal inverse
def gl_nodes(n, device):
    x, w = np.polynomial.legendre.leggauss(n)
    return torch.tensor(x, dtype=DT, device=device), torch.tensor(w, dtype=DT, device=device)


def modal_inverse(P, r, m, gfun_t, tail, ngl=16):
    """J_in, J_out at increasing radii r (N,) for angular wavenumber m, for a family of radial functions
    g(t) given by gfun_t(t) -> (..., K) with t = u^2 = (r/L)^2.  tail: (K,) = J_out(r_N) (exact tail integral).
    Returns Jin (N,K), Jout (N,K).
    J_in(r)  = int_0^r (s/r)^m s g ds = (L^2/2) int_0^{t_r} (t/t_r)^{m/2} g dt,
    J_out(r) = int_r^inf (r/s)^m s g ds = (L^2/2) int_{t_r}^inf (t_r/t)^{m/2} g dt."""
    device = r.device
    N = r.shape[0]
    u = r / P.L
    tcol = u * u
    xg, wg = gl_nodes(ngl, device)
    tlo = torch.cat([torch.zeros(1, dtype=DT, device=device), tcol[:-1]])
    thi = tcol
    mid = 0.5 * (tlo + thi); half = 0.5 * (thi - tlo)
    tn = mid[:, None] + half[:, None] * xg[None, :]
    wn = half[:, None] * wg[None, :]
    gn = gfun_t(tn)                                                  # (N, ngl, K)
    K = gn.shape[-1]
    L2 = P.L ** 2
    fac_in = (tn / thi[:, None]) ** (m / 2.0)
    Iin = 0.5 * L2 * torch.einsum('ng,ngk->nk', wn * fac_in, gn)
    ratio_out = torch.where(tlo[:, None] > 0, (tlo[:, None] / torch.clamp(tn, min=1e-300)) ** (m / 2.0), torch.zeros_like(tn))
    Iout = 0.5 * L2 * torch.einsum('ng,ngk->nk', wn * ratio_out, gn)
    s = (tlo / thi) ** (m / 2.0)
    Jin = torch.zeros(N, K, dtype=DT, device=device)
    Jout = torch.zeros(N, K, dtype=DT, device=device)
    cur = torch.zeros(K, dtype=DT, device=device)
    for i in range(N):
        cur = s[i] * cur + Iin[i]
        Jin[i] = cur
    cur = tail.clone()
    Jout[N - 1] = cur
    for i in range(N - 2, -1, -1):
        cur = s[i + 1] * cur + Iout[i + 1]
        Jout[i] = cur
    return Jin, Jout


def basis_gfun(P, m, gamma, K):
    def g(t):
        E = 1.0 + t
        q = 1.0 - E ** (-P.mu / 2)
        T, _ = cheb_T_and_dT(q, K)
        return ((t / E) ** (m / 2.0) * E ** (gamma / 2.0))[..., None] * T
    return g


def basis_tail(P, rN, m, gamma, K, ngl_tail=192):
    """J_out(r_N) = int_{r_N}^inf (r_N/s)^m s g ds for the basis g = (t/E)^{m/2} E^{gamma/2} T_k(q).
    = (L^2/mu) (u_N^2/E_N)^{m/2} E_N^{(gamma+mu)/2+1} int_{q_N}^1 [(1-q)/(1-q_N)]^{expo} T_k dq,  expo = -(gamma-m+2)/mu - 1."""
    device = rN.device
    uN = rN / P.L
    tN = uN * uN; EN = 1.0 + tN
    qN = 1.0 - EN ** (-P.mu / 2)
    xq, wq = gl_nodes(ngl_tail, device)
    qt = qN + (1.0 - qN) * 0.5 * (xq + 1.0)
    wqt = (1.0 - qN) * 0.5 * wq
    Tt, _ = cheb_T_and_dT(qt, K)
    expo = -(gamma - m + 2.0) / P.mu - 1.0
    pref = (P.L ** 2 / P.mu) * (tN / EN) ** (m / 2.0) * EN ** ((gamma + P.mu) / 2.0 + 1.0)
    return pref * torch.einsum('g,gk->k', wqt * ((1.0 - qt) / (1.0 - qN)) ** expo, Tt)


def c_row(P, gamma, K):
    """c = Psi_xy(0) = (1/2) int_0^inf g_1(s)/s ds for the mode-1 basis (m=2): (K,) coefficients."""
    device = dev()
    xq2, wq2 = gl_nodes(256, device)
    q2 = 0.5 * (xq2 + 1.0); w2 = 0.5 * wq2
    T2, _ = cheb_T_and_dT(q2, K)
    expo_c = -gamma / P.mu - 1.0
    return 0.25 * (2.0 / P.mu) * torch.einsum('g,gk->k', w2 * (1.0 - q2) ** expo_c, T2)


def inverse_matrices(P, r, NO, K, ngl=16, ngl_tail=192):
    """PSI (NO,N,K), DPSI (NO,N,K): coefficients of g_n -> psi_n(r_i), psi_n'(r_i); CROW (K,) for c = Psi_xy(0)."""
    device = r.device
    N = r.shape[0]
    PSI = torch.zeros(NO, N, K, dtype=DT, device=device)
    DPSI = torch.zeros(NO, N, K, dtype=DT, device=device)
    for n in range(1, NO + 1):
        m = 2 * n
        tail = basis_tail(P, r[-1], m, P.gamma_O, K, ngl_tail=ngl_tail)
        Jin, Jout = modal_inverse(P, r, m, basis_gfun(P, m, P.gamma_O, K), tail, ngl=ngl)
        PSI[n - 1] = (Jin + Jout) / (4.0 * n)
        DPSI[n - 1] = (Jout - Jin) / (2.0 * r[:, None])
    CROW = c_row(P, P.gamma_O, K).to(device)
    return PSI, DPSI, CROW


# ---------------------------------------------------------------- field evaluation on a polar grid
class Grid:
    """Tensor-product polar grid: radii r (N,), angles th (M,) in (0, pi/2). Points flattened row-major (N*M,)."""
    def __init__(self, r, th):
        self.r = r
        self.th = th
        self.N = r.shape[0]
        self.M = th.shape[0]
        R, TH = torch.meshgrid(r, th, indexing='ij')
        self.R = R.reshape(-1)
        self.TH = TH.reshape(-1)
        self.x = self.R * torch.cos(self.TH)
        self.y = self.R * torch.sin(self.TH)
        self.cos = torch.cos(self.TH)
        self.sin = torch.sin(self.TH)


def field_matrices(P, grid, NT, NO, K, ngl=16, ngl_tail=192):
    """Build dense matrices on the grid (Npts x ncoef):
    TH, THx, THy for Theta (ncoef = NT*K), OM, OMx, OMy for Omega (NO*K), U1, U2 for velocity (NO*K), PSI (NO*K).
    Coefficient ordering: mode-major (n, k)."""
    r, th = grid.r, grid.th
    N, M = grid.N, grid.M
    device = r.device
    # Theta
    cols = []
    for n in range(NT):
        m = 2 * n + 1
        H, dH = radial_basis(P, r, m, P.gamma_T, K)         # (N,K)
        Hr = H / r[:, None]
        s_m = torch.sin(m * th); c_m = torch.cos(m * th)   # (M,)
        # field: H(r) sin(m th)
        F = H[:, None, :] * s_m[None, :, None]
        Fr = dH[:, None, :] * s_m[None, :, None]
        Fth_over_r = m * Hr[:, None, :] * c_m[None, :, None]
        Fx = grid.cos.reshape(N, M)[:, :, None] * Fr - grid.sin.reshape(N, M)[:, :, None] * Fth_over_r
        Fy = grid.sin.reshape(N, M)[:, :, None] * Fr + grid.cos.reshape(N, M)[:, :, None] * Fth_over_r
        cols.append((F.reshape(N * M, K), Fx.reshape(N * M, K), Fy.reshape(N * M, K)))
    TH = torch.cat([c[0] for c in cols], 1); THx = torch.cat([c[1] for c in cols], 1); THy = torch.cat([c[2] for c in cols], 1)
    # Omega and velocity
    PSI, DPSI, CROW = inverse_matrices(P, r, NO, K, ngl=ngl, ngl_tail=ngl_tail)
    colsO = []; colsU = []; colsP = []
    for n in range(1, NO + 1):
        m = 2 * n
        H, dH = radial_basis(P, r, m, P.gamma_O, K)
        Hr = H / r[:, None]
        s_m = torch.sin(m * th); c_m = torch.cos(m * th)
        F = H[:, None, :] * s_m[None, :, None]
        Fr = dH[:, None, :] * s_m[None, :, None]
        Fth_over_r = m * Hr[:, None, :] * c_m[None, :, None]
        C = grid.cos.reshape(N, M)[:, :, None]; S = grid.sin.reshape(N, M)[:, :, None]
        Fx = C * Fr - S * Fth_over_r
        Fy = S * Fr + C * Fth_over_r
        colsO.append((F.reshape(N * M, K), Fx.reshape(N * M, K), Fy.reshape(N * M, K)))
        psi = PSI[n - 1]; dpsi = DPSI[n - 1]; psir = psi / r[:, None]
        G = psi[:, None, :] * s_m[None, :, None]
        Gr = dpsi[:, None, :] * s_m[None, :, None]
        Gth_over_r = m * psir[:, None, :] * c_m[None, :, None]
        Gx = C * Gr - S * Gth_over_r
        Gy = S * Gr + C * Gth_over_r
        colsU.append((-Gy.reshape(N * M, K), Gx.reshape(N * M, K)))   # U1 = -Psi_y, U2 = Psi_x
        colsP.append(G.reshape(N * M, K))
    OM = torch.cat([c[0] for c in colsO], 1); OMx = torch.cat([c[1] for c in colsO], 1); OMy = torch.cat([c[2] for c in colsO], 1)
    U1 = torch.cat([c[0] for c in colsU], 1); U2 = torch.cat([c[1] for c in colsU], 1)
    PS = torch.cat(colsP, 1)
    # full c-row over all Omega coefficients (only mode 1 contributes)
    crow = torch.zeros(NO * K, dtype=DT, device=device)
    crow[:K] = CROW
    return dict(TH=TH, THx=THx, THy=THy, OM=OM, OMx=OMx, OMy=OMy, U1=U1, U2=U2, PSI=PS, crow=crow)


def residuals(Mx, grid, cT, cO, beta):
    """Cartesian residuals R_Theta, R_Omega and normalizers N_Theta, N_Omega on the grid, plus fields."""
    Th = Mx['TH'] @ cT; Thx = Mx['THx'] @ cT; Thy = Mx['THy'] @ cT
    Om = Mx['OM'] @ cO; Omx = Mx['OMx'] @ cO; Omy = Mx['OMy'] @ cO
    U1 = Mx['U1'] @ cO; U2 = Mx['U2'] @ cO
    W1 = beta * grid.x + U1; W2 = beta * grid.y + U2
    RT = W1 * Thx + W2 * Thy - (beta - 2.0) * Th
    RO = W1 * Omx + W2 * Omy + Om - Thx
    NT_ = W1.abs() * Thx.abs() + W2.abs() * Thy.abs() + abs(beta - 2.0) * Th.abs()
    NO_ = W1.abs() * Omx.abs() + W2.abs() * Omy.abs() + Om.abs() + Thx.abs()
    return dict(RT=RT, RO=RO, NT=NT_, NO=NO_, Th=Th, Thx=Thx, Thy=Thy, Om=Om, Omx=Omx, Omy=Omy, U1=U1, U2=U2, W1=W1, W2=W2)
