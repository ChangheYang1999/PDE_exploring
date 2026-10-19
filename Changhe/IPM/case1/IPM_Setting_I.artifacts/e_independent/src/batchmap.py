"""
Batched version of the characteristics map Phi(b) for finite-difference Jacobians:
all columns j (perturbed fields b + eps e_j) are integrated simultaneously; each trajectory carries its column index.
"""
import sys, math, time, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1, charac


class BatchFieldEval:
    """Fields for a batch of B inputs b (B, Nr, M) with per-column c_l; evaluation at points with column indices,
    from the fine psi~ mode functions (exact pointwise)."""

    def __init__(self, m, B_b, cl):
        self.m = m
        cl_t = torch.as_tensor(cl, device=m.dev, dtype=torch.float64)
        self.cl_col = cl_t.expand(B_b.shape[0]) if cl_t.dim() == 0 else cl_t
        self.cl = float(self.cl_col[0])
        flds = m.fields(B_b)
        self.PsiC_R = flds['PsiC_R']            # (B, Nr, M2)
        self.rPsiC_r = flds['rPsiC_r']
        self.c = m.psi_xy0(flds)
        self.nf = m.nf
        self.tR = m.rad.tR
        self.wbar = torch.tensor(ipm1.bary_weights(m.rad.tR_np), device=m.dev)
        self.B = B_b.shape[0]

    def t_of_r(self, r):
        if hasattr(self.m.rad, 'a'):
            return self.m.rad.t_of_r(r)
        L, p = self.m.L, self.m.p
        t = torch.where(r < L, -1 + 2 * r / L / (1 + r / L), 1 - (2 * L / r.clamp_min(1e-300)) ** (1 / p)).clamp(-1 + 1e-15, 1 - 1e-15)
        for _ in range(12):
            f = L * (1 + t) / (1 - t) ** p - r
            t = (t - f / self.m.rad.drdt(t)).clamp(-1 + 1e-16, 1 - 1e-16)
        return t

    def velocity(self, x, y, col):
        m = self.m
        sx = torch.sign(x); sy = torch.sign(y)
        xa, ya = x.abs(), y.abs()
        r = torch.sqrt(xa ** 2 + ya ** 2); th = torch.atan2(ya, xa)
        t = self.t_of_r(r)
        d = t[:, None] - self.tR[None, :]
        small = d.abs() < 1e-14
        d = torch.where(small, torch.ones_like(d), d)
        Wt = self.wbar[None, :] / d
        Wt = torch.where(small.any(1, keepdim=True), small.to(Wt.dtype), Wt)
        P = Wt / Wt.sum(1, keepdim=True)                        # (K, Nr)
        Psi_n = torch.einsum('kn,knm->km', P, self.PsiC_R[col]); rPsi_n = torch.einsum('kn,knm->km', P, self.rPsiC_r[col])
        sn = torch.sin(th[:, None] * self.nf[None, :]); cn = torch.cos(th[:, None] * self.nf[None, :])
        Psi = (Psi_n * sn).sum(1); rPsi_r = (rPsi_n * sn).sum(1); Psi_th = (Psi_n * self.nf[None, :] * cn).sum(1)
        s2 = r ** 2 / (m.L ** 2 + r ** 2)
        kap = 2 + (m.gamma - 1) * s2
        G = kap * Psi + rPsi_r
        cs, si = torch.cos(th), torch.sin(th)
        U1h = -(si * G + cs * Psi_th); U2h = cs * G - si * Psi_th
        ratio = torch.where((si.abs() > 1e-8)[:, None], sn / si.clamp_min(1e-300)[:, None], self.nf[None, :].expand_as(sn))
        G_over_sin = kap * (Psi_n * ratio).sum(1) + (rPsi_n * ratio).sum(1)
        U2s = cs * G_over_sin - Psi_th
        v = (1 + r ** 2 / m.L ** 2) ** ((m.gamma - 1) / 2)
        U1 = r * v * U1h * torch.where(sx == 0, torch.ones_like(sx), sx)
        U2 = r * v * U2h * torch.where(sy == 0, torch.ones_like(sy), sy)
        clc = self.cl_col[col]
        return clc * x + U1, clc * y + U2, clc + v * U2s

    def find_P(self, bracket=None, npts=1500):
        m = self.m; B = self.B
        if bracket is None:
            xs = torch.logspace(-4, 8, npts, device=m.dev, dtype=torch.float64)
        else:
            xs = torch.linspace(bracket[0], bracket[1], npts, device=m.dev, dtype=torch.float64)
        X = xs.repeat(B); col = torch.arange(B, device=m.dev).repeat_interleave(len(xs))
        W1, _, _ = self.velocity(X, torch.zeros_like(X), col)
        W1 = W1.reshape(B, -1)
        neg = (W1[:, :-1] < 0) & (W1[:, 1:] >= 0)
        has = neg.any(1)
        idx = torch.argmax(neg.to(torch.int8), dim=1)
        a = xs[idx]; bb = xs[idx + 1]
        cols = torch.arange(B, device=m.dev)
        for _ in range(60):
            mid = 0.5 * (a + bb)
            W1m, _, _ = self.velocity(mid, torch.zeros_like(mid), cols)
            a = torch.where(W1m < 0, mid, a); bb = torch.where(W1m < 0, bb, mid)
        xs_ = 0.5 * (a + bb)
        hx = 1e-6 * xs_.clamp_min(1e-3)
        W1p, _, _ = self.velocity(xs_ + hx, torch.zeros_like(xs_), cols)
        W1m_, _, _ = self.velocity(xs_ - hx, torch.zeros_like(xs_), cols)
        mu1 = (W1p - W1m_) / (2 * hx)
        _, _, bW = self.velocity(xs_, torch.zeros_like(xs_), cols)
        return xs_, mu1, bW, has


def eta_batch(fe: BatchFieldEval, X0, Y0, col, x_star_col, dt=0.01, tmax=80.0, delta=1e-6):
    """Backward characteristics for trajectories with their own columns and stagnation points x_star_col (per column)."""
    dev = X0.device; K = X0.shape[0]
    x = X0.clone(); y = Y0.clone(); T = torch.zeros(K, device=dev); rho = torch.zeros(K, device=dev)
    active = torch.ones(K, dtype=torch.bool, device=dev)
    xs_all = x_star_col[col]
    nsteps = int(tmax / dt)
    for step in range(nsteps):
        if not active.any():
            break
        idx = torch.where(active)[0]
        xa, ya, ca, xsa = x[idx], y[idx], col[idx], xs_all[idx]
        def rhs(xx, yy):
            W1, W2, _ = fe.velocity(xx, yy, ca); return -W1, -W2
        k1x, k1y = rhs(xa, ya); k2x, k2y = rhs(xa + 0.5 * dt * k1x, ya + 0.5 * dt * k1y)
        k3x, k3y = rhs(xa + 0.5 * dt * k2x, ya + 0.5 * dt * k2y); k4x, k4y = rhs(xa + dt * k3x, ya + dt * k3y)
        xn = xa + dt / 6 * (k1x + 2 * k2x + 2 * k3x + k4x)
        yn = (ya + dt / 6 * (k1y + 2 * k2y + 2 * k3y + k4y)).clamp_min(1e-300)
        dxn = (xn - xsa).abs(); dxa = (xa - xsa).abs()
        inside = (dxn < delta) & (yn < delta)
        tau_x = torch.where(dxa >= delta, torch.log(dxa / delta) / torch.log((dxa / dxn).clamp_min(1 + 1e-15)), torch.zeros_like(dxa))
        tau_y = torch.where(ya >= delta, torch.log(ya / delta) / torch.log((ya / yn).clamp_min(1 + 1e-15)), torch.zeros_like(ya))
        tau = torch.maximum(tau_x, tau_y).clamp(0.0, 1.0)
        y_entry = ya * (yn / ya) ** tau; T_entry = T[idx] + tau * dt
        done_idx = idx[inside]
        rho[done_idx] = y_entry[inside] * torch.exp(T_entry[inside]); T[done_idx] = T_entry[inside]; active[done_idx] = False
        keep = ~inside
        x[idx[keep]] = xn[keep]; y[idx[keep]] = yn[keep]; T[idx[keep]] += dt
    return rho, T, ~active


def axis_a0_batch(fe: BatchFieldEval, x_star_col, delta=1e-6, x_eval=1e-6):
    """a(0) for C = 1 per column: g(x_eval)/x_eval^2 with g = exp(-int_{x_eval}^{x*-delta} (1-h)/w dx) (log-x Gauss quadrature)."""
    m = fe.m; B = fe.B; dev = m.dev
    nodes, wts = np.polynomial.legendre.leggauss(8)
    n = 3000
    a0 = torch.zeros(B, device=dev)
    la = math.log(x_eval)
    lb = torch.log(x_star_col - delta)                       # (B,)
    edges = torch.linspace(0, 1, n + 1, device=dev)
    mids = 0.5 * (edges[1:] + edges[:-1]); half = 0.5 * (edges[1:] - edges[:-1])
    u = (mids[:, None] + half[:, None] * torch.tensor(nodes, device=dev)[None, :]).reshape(-1)       # (n*8,) in [0,1]
    wu = (half[:, None] * torch.tensor(wts, device=dev)[None, :]).reshape(-1)
    s = la + (lb[:, None] - la) * u[None, :]                 # (B, Q)
    xq = torch.exp(s)
    col = torch.arange(B, device=dev).repeat_interleave(xq.shape[1])
    W1, _, bW = fe.velocity(xq.reshape(-1), torch.zeros_like(xq.reshape(-1)), col)
    integrand = ((1 - bW) / W1 * xq.reshape(-1)).reshape(B, -1)
    F = (integrand * wu[None, :]).sum(1) * (lb - la)
    g = torch.exp(-F)
    return g / x_eval ** 2


def phi_batch(m, B_b, cl, dt=0.01, delta=1e-6):
    """Phi applied to each column of B_b (B, Nr, M). Returns (B, Nr, M) and info."""
    dev = m.dev; B = B_b.shape[0]
    fe = BatchFieldEval(m, B_b, cl)
    xs_, mu1, hP, has = fe.find_P()
    r = m.rad.rR[:, None]; cos = m.ang.cos[None, :]; sin = m.ang.sin[None, :]
    X = (r * cos).reshape(-1); Y = (r * sin).reshape(-1); mask = X > 0
    Xm, Ym = X[mask], Y[mask]; Kp = Xm.shape[0]
    col = torch.arange(B, device=dev).repeat_interleave(Kp)
    Xb = Xm.repeat(B); Yb = Ym.repeat(B)
    # a0 for C=1 from the 2D transport itself: g(x_eval) = eta(x_eval, y_tiny)/y_tiny, a0 = g/x_eval^2
    x_eval, y_tiny = 1e-4, 1e-12
    colA = torch.arange(B, device=dev)
    etaA, TA, okA = eta_batch(fe, torch.full((B,), x_eval, device=dev), torch.full((B,), y_tiny, device=dev), colA, xs_, dt=dt, delta=delta)
    a0 = etaA / y_tiny / x_eval ** 2
    eta, T, ok = eta_batch(fe, Xb, Yb, col, xs_, dt=dt, delta=delta)
    eta_full = torch.zeros(B, X.shape[0], device=dev); eta_full[:, mask] = eta.reshape(B, Kp)
    eta_full = eta_full.reshape(B, m.N + 1, m.M)
    b_eta = eta_full / (r ** 3 * m.wR[:, None] * cos ** 2 * sin)[None]; b_eta[:, 0, :] = a0[:, None]
    c_eta = m.psi_xy0(m.fields(b_eta))                       # (B,)
    clc = fe.cl_col
    C = (3 * clc - 1) / c_eta
    Lsc = torch.sqrt(C * a0)
    Xs = Xb / Lsc[col]; Ys = Yb / Lsc[col]
    rho, T2, ok2 = eta_batch(fe, Xs, Ys, col, xs_, dt=dt, delta=delta)
    rho = (Lsc[col] * C[col] * rho)
    rho_full = torch.zeros(B, X.shape[0], device=dev); rho_full[:, mask] = rho.reshape(B, Kp)
    rho_full = rho_full.reshape(B, m.N + 1, m.M)
    bnew = rho_full / (r ** 3 * m.wR[:, None] * cos ** 2 * sin)[None]; bnew[:, 0, :] = 1.0
    info = dict(x_star=xs_, mu1=mu1, h=hP, has=has, a0=a0, C=C, Lsc=Lsc, c_eta=c_eta, ok=ok.reshape(B, Kp).all(1) & ok2.reshape(B, Kp).all(1))
    return bnew, info


def hP_batch(m, B_b, cl_col):
    """h(P) - 1 per column for inputs B_b with per-column c_l (amplitude of each column set by the identity)."""
    c_in = m.psi_xy0(m.fields(B_b))
    A = (3 * cl_col - 1) / c_in
    fe = BatchFieldEval(m, A[:, None, None] * B_b, cl_col)
    xs_, mu1, hP, has = fe.find_P()
    return hP - 1.0, has, xs_, mu1


def psi_batch(m, B_b, cl_lo=1.05, cl_hi=12.0, ngrid=23, nbis=45, dt=0.01, delta=1e-6):
    """Doubly consistent map Psi applied to each column: c_l(b) with h(P) = 1 by bracketing + bisection (first root),
    amplitude by the identity, transport from P, renormalisation. Returns bnew (B, N+1, M), cl (B,), info."""
    dev = m.dev; B = B_b.shape[0]
    grid = torch.linspace(cl_lo, cl_hi, ngrid, device=dev)
    vals = torch.zeros(B, ngrid, device=dev); hasg = torch.zeros(B, ngrid, dtype=torch.bool, device=dev)
    for i in range(ngrid):
        f, has, _, _ = hP_batch(m, B_b, grid[i].expand(B))
        vals[:, i] = f; hasg[:, i] = has
    sgn = (vals[:, :-1] * vals[:, 1:] < 0) & hasg[:, :-1] & hasg[:, 1:]
    hasroot = sgn.any(1)
    first = torch.argmax(sgn.to(torch.int8), dim=1)
    a = grid[first]; bb = grid[first + 1]
    fa, _, _, _ = hP_batch(m, B_b, a)
    for _ in range(nbis):
        mid = 0.5 * (a + bb)
        fm, _, _, _ = hP_batch(m, B_b, mid)
        left = fa * fm <= 0
        bb = torch.where(left, mid, bb); a = torch.where(left, a, mid); fa = torch.where(left, fa, fm)
    cl = 0.5 * (a + bb)
    c_in = m.psi_xy0(m.fields(B_b)); A = (3 * cl - 1) / c_in
    bnew, info = phi_batch(m, A[:, None, None] * B_b, cl, dt=dt, delta=delta)
    info['cl'] = cl; info['hasroot'] = hasroot
    return bnew, cl, info
