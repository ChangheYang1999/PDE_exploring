"""
charac.py -- characteristics-based transport solve (SPEC Lemma 4): for a frozen field W = c_l X + U[rho],
rho = C eta_P on the basin of the x-axis stagnation point P, computed by integrating backward characteristics
from each target point to a small disk around P, where rho ~ C y.

Off-grid evaluation of the spectral fields: radial barycentric interpolation in t, exact angular basis.
All trajectories are integrated together (batched RK4 on the GPU) with per-trajectory stopping.
"""
import math, numpy as np, torch
import ipm1


class FieldEval:
    """Evaluate W = c_l X + U at arbitrary points from the fine psi~ mode functions (bounded), exactly as fields() does."""

    def __init__(self, m: 'ipm1.IPM1', b, cl):
        self.m, self.cl = m, cl
        flds = m.fields(b)
        self.flds = flds
        self.PsiC_R = flds['PsiC_R']            # (Nr, M2) psi~ mode functions on Radau
        self.rPsiC_r = flds['rPsiC_r']          # r d/dr of them (on the grid)
        self.DPsiC_R = m.rad.DR @ self.PsiC_R   # d/dt of the mode functions at the Radau nodes (exact, degree N-1): interpolated off-grid
        #   and multiplied by S(t) = r/(dr/dt) pointwise, so that off-grid derivatives are those of the interpolated psi (astra lsqpin)
        self.nf = m.nf                # (M2,) harmonics n = 2, 4, ...
        self.tR = m.rad.tR
        self.wbar = torch.tensor(ipm1.bary_weights(m.rad.tR_np), device=m.dev)
        self.c = m.psi_xy0(flds).item()

    def t_of_r(self, r):
        """invert the radial map (closed form for the disk map, Newton for the compactified map)."""
        if hasattr(self.m.rad, 'a'):
            return self.m.rad.t_of_r(r)
        L, p = self.m.L, self.m.p
        t = torch.where(r < L, -1 + 2 * r / L / (1 + r / L), 1 - (2 * L / r.clamp_min(1e-300)) ** (1 / p))
        t = t.clamp(-1 + 1e-15, 1 - 1e-15)
        for _ in range(12):
            f = L * (1 + t) / (1 - t) ** p - r
            df = self.m.rad.drdt(t)
            t = (t - f / df).clamp(-1 + 1e-16, 1 - 1e-16)
        return t

    def radial_interp_matrix(self, t):
        """(K, Nr) barycentric interpolation weights at points t (K,)."""
        d = t[:, None] - self.tR[None, :]
        small = d.abs() < 1e-14
        d = torch.where(small, torch.ones_like(d), d)
        Wt = self.wbar[None, :] / d
        Wt = torch.where(small.any(1, keepdim=True), small.to(Wt.dtype), Wt)
        return Wt / Wt.sum(1, keepdim=True)

    def uhat(self, r, th):
        """U^1 = U1/(r v), U^2 = U2/(r v), U^2/sin(theta) at (r, theta) in the closed quadrant (vectorised)."""
        m = self.m
        t = self.t_of_r(r)
        P = self.radial_interp_matrix(t)
        Psi_n = P @ self.PsiC_R
        S_t = r / self.m.rad.drdt(t)                                        # r/(dr/dt) at the evaluation points
        rPsi_n = S_t[:, None] * (P @ self.DPsiC_R)                          # (K, M2): derivative of the interpolant
        sn = torch.sin(th[:, None] * self.nf[None, :]); cn = torch.cos(th[:, None] * self.nf[None, :])
        Psi = (Psi_n * sn).sum(1); rPsi_r = (rPsi_n * sn).sum(1); Psi_th = (Psi_n * self.nf[None, :] * cn).sum(1)
        s2 = r ** 2 / (m.L ** 2 + r ** 2)
        G = (2 + (m.gamma - 1) * s2) * Psi + rPsi_r
        cs, si = torch.cos(th), torch.sin(th)
        U1h = -(si * G + cs * Psi_th)
        U2h = cs * G - si * Psi_th
        # U2h / sin(theta) without division: sin(n th)/sin(th) = sum_{j} ... use the identity cos*G*? -> compute directly, safe
        # for theta away from 0; at theta -> 0 use sin(n th)/sin(th) -> n.  We use the stable form:
        ratio = torch.where((si.abs() > 1e-8)[:, None], sn / si.clamp_min(1e-300)[:, None], self.nf[None, :].expand_as(sn))
        Psi_over_sin = (Psi_n * ratio).sum(1); rPsi_over_sin = (rPsi_n * ratio).sum(1)
        G_over_sin = (2 + (m.gamma - 1) * s2) * Psi_over_sin + rPsi_over_sin
        # U2h/sin = cs*G/sin - Psi_th ; Psi_th = sum n Psi_n cos(n th)
        U2s = cs * G_over_sin - Psi_th
        return U1h, U2h, U2s

    def velocity(self, x, y):
        """W = c_l X + U at points (x, y) (any quadrant, parity used). Returns W1, W2, W2/y."""
        m = self.m
        sx = torch.sign(x); sy = torch.sign(y)
        xa, ya = x.abs(), y.abs()
        r = torch.sqrt(xa ** 2 + ya ** 2)
        th = torch.atan2(ya, xa)
        U1h, U2h, U2s = self.uhat(r, th)
        v = (1 + r ** 2 / m.L ** 2) ** ((m.gamma - 1) / 2)
        U1 = r * v * U1h * torch.where(sx == 0, torch.ones_like(sx), sx)
        U2 = r * v * U2h * torch.where(sy == 0, torch.ones_like(sy), sy)
        return self.cl * x + U1, self.cl * y + U2, self.cl + v * U2s

    def axis_W1(self, x):
        W1, _, _ = self.velocity(x, torch.zeros_like(x))
        return W1

    def find_P(self, xmax=None):
        """first positive zero of W1(x,0) by bisection on a log grid."""
        m = self.m
        xs = torch.logspace(-4, 8, 2000, device=m.dev, dtype=torch.float64)
        W1 = self.axis_W1(xs)
        idx = torch.where((W1[:-1] < 0) & (W1[1:] >= 0))[0]
        if len(idx) == 0:
            return None
        a, bb = xs[idx[0]].item(), xs[idx[0] + 1].item()
        for _ in range(100):
            mid = 0.5 * (a + bb)
            if self.axis_W1(torch.tensor([mid], device=m.dev))[0].item() < 0:
                a = mid
            else:
                bb = mid
        xs_ = 0.5 * (a + bb)
        hx = 1e-6 * max(xs_, 1e-3)
        W1p = self.axis_W1(torch.tensor([xs_ + hx], device=m.dev))[0].item()
        W1m = self.axis_W1(torch.tensor([xs_ - hx], device=m.dev))[0].item()
        mu1 = (W1p - W1m) / (2 * hx)
        _, _, bW = self.velocity(torch.tensor([xs_], device=m.dev), torch.zeros(1, device=m.dev))
        return dict(x_star=xs_, mu1=mu1, h=bW[0].item(), n_zero=int(len(idx)))


def eta_P(fe: FieldEval, X0, Y0, x_star, C=1.0, dt=0.005, tmax=80.0, delta=1e-6, record=False):
    """
    rho(X0) for each target point: backward RK4 integration of dX/dt = -W(X) until the trajectory enters the box
    B = {|x - x*| < delta, y < delta} around P, with the entry time found by log-linear interpolation inside the last
    step (so that T(X) is a continuous function with W.grad T = 1).  Data on the box boundary: rho = C y.
    Returns rho = C * y_entry * exp(T_entry), T_entry, ok mask, I (= log(rho/(C Y0))).
    """
    dev = X0.device
    K = X0.shape[0]
    x = X0.clone(); y = Y0.clone()
    T = torch.zeros(K, device=dev)
    rho = torch.zeros(K, device=dev)
    active = torch.ones(K, dtype=torch.bool, device=dev)
    nsteps = int(tmax / dt)
    def rhs(x, y):
        W1, W2, bW = fe.velocity(x, y)
        return -W1, -W2
    for step in range(nsteps):
        if not active.any():
            break
        idx = torch.where(active)[0]
        xa, ya = x[idx], y[idx]
        k1x, k1y = rhs(xa, ya)
        k2x, k2y = rhs(xa + 0.5 * dt * k1x, ya + 0.5 * dt * k1y)
        k3x, k3y = rhs(xa + 0.5 * dt * k2x, ya + 0.5 * dt * k2y)
        k4x, k4y = rhs(xa + dt * k3x, ya + dt * k3y)
        xn = xa + dt / 6 * (k1x + 2 * k2x + 2 * k3x + k4x)
        yn = (ya + dt / 6 * (k1y + 2 * k2y + 2 * k3y + k4y)).clamp_min(1e-300)
        dxn = (xn - x_star).abs(); dxa = (xa - x_star).abs()
        inside = (dxn < delta) & (yn < delta)
        # entry fraction tau in (0,1]: max over coordinates that were outside before the step
        tau_x = torch.where(dxa >= delta, torch.log(dxa / delta) / torch.log((dxa / dxn).clamp_min(1 + 1e-15)), torch.zeros_like(dxa))
        tau_y = torch.where(ya >= delta, torch.log(ya / delta) / torch.log((ya / yn).clamp_min(1 + 1e-15)), torch.zeros_like(ya))
        tau = torch.maximum(tau_x, tau_y).clamp(0.0, 1.0)
        y_entry = ya * (yn / ya) ** tau
        T_entry = T[idx] + tau * dt
        done_idx = idx[inside]
        rho[done_idx] = C * y_entry[inside] * torch.exp(T_entry[inside])
        T[done_idx] = T_entry[inside]
        active[done_idx] = False
        keep = ~inside
        x[idx[keep]] = xn[keep]; y[idx[keep]] = yn[keep]; T[idx[keep]] += dt
    I = torch.log((rho / (C * Y0)).clamp_min(1e-300))
    return rho, T, ~active, I


def axis_g(fe: FieldEval, x_star, xs, C=1.0, delta=1e-7):
    """g(x) = rho_y(x,0) on (0, x*): g = C exp( int_{x*-delta}^{x} (1-h)/w ds ), integrated as an ODE in s=ln x (high-order)."""
    dev = xs.device
    # integrate dlog g / dx = (1-h)/w from x*-delta down to each x using fine composite Gauss-Legendre in log x
    a = math.log(1e-8); b = math.log(x_star - delta)
    n = 4000
    nodes, wts = np.polynomial.legendre.leggauss(8)
    edges = np.linspace(a, b, n + 1)
    mids = 0.5 * (edges[1:] + edges[:-1]); half = 0.5 * (edges[1:] - edges[:-1])
    s = (mids[:, None] + half[:, None] * nodes[None, :]).reshape(-1)
    w_ = (half[:, None] * wts[None, :]).reshape(-1)
    s_t = torch.tensor(s, device=dev); w_t = torch.tensor(w_, device=dev)
    xq = torch.exp(s_t)
    W1, _, bW = fe.velocity(xq, torch.zeros_like(xq))
    integrand = (1 - bW) / W1 * xq          # d/ds with s = ln x: dx = x ds
    # cumulative integral from b down to s: F(s) = int_s^b integrand ds'
    cum = torch.flip(torch.cumsum(torch.flip(integrand * w_t, [0]), 0), [0])   # sum over nodes >= index (approximate per node)
    # log g(x) = log C - int_x^{x*-delta} (1-h)/w ds  => g = C exp(-F)
    # interpolate F at requested xs (log-linear interpolation on the fine grid)
    ls = torch.log(xs)
    F = torch.tensor(np.interp(ls.cpu().numpy(), s, cum.cpu().numpy()), device=dev)
    return C * torch.exp(-F), (s_t, cum)


def picard_step(m: 'ipm1.IPM1', b, cl=None, dt=0.005, delta=1e-6, verbose=True, C=None):
    """One Picard step: rho' = C eta_P[W(b, c_l)], with c_l = (1 + c[b])/3 if cl is None and C from a(0)=1."""
    fe = FieldEval(m, b, cl if cl is not None else 1.0)
    if cl is None:
        cl = (1 + fe.c) / 3
        fe = FieldEval(m, b, cl)
    Pinfo = fe.find_P()
    if Pinfo is None:
        return None
    xs_ = Pinfo['x_star']
    r = m.rad.rR[:, None]; cos = m.ang.cos[None, :]; sin = m.ang.sin[None, :]
    X0 = (r * cos).reshape(-1); Y0 = (r * sin).reshape(-1)
    mask = X0 > 0        # exclude r = 0 row
    rho = torch.zeros_like(X0); T = torch.zeros_like(X0); ok = torch.zeros_like(X0, dtype=torch.bool)
    rho_m, T_m, ok_m, I_m = eta_P(fe, X0[mask], Y0[mask], xs_, C=1.0, dt=dt, delta=delta)
    rho[mask] = rho_m; T[mask] = T_m; ok[mask] = ok_m
    rho = rho.reshape(m.N + 1, m.M); T = T.reshape(m.N + 1, m.M); ok = ok.reshape(m.N + 1, m.M)
    # normalisation: a(0) = lim g(x)/x^2 with g from the axis ODE (C=1)
    xs_small = torch.tensor([1e-6, 3e-6, 1e-5, 3e-5, 1e-4], device=m.dev)
    g, _ = axis_g(fe, xs_, xs_small, C=1.0, delta=delta)
    a0_vals = (g / xs_small ** 2)
    a0 = a0_vals[0].item()
    if C is None:
        C = 1.0 / a0
    rho = C * rho
    bnew = rho / (r ** 3 * m.wR[:, None] * cos ** 2 * sin)
    bnew[0, :] = 1.0
    info = dict(cl=cl, c=fe.c, P=Pinfo, a0_vals=(C * a0_vals).cpu().numpy(), C=C, T=T, ok=ok)
    if verbose:
        print(f"  picard step: c_l={cl:.8f} c={fe.c:.6f} x*={xs_:.6f} mu1={Pinfo['mu1']:.6f} (2c_l-1={2*cl-1:.6f}) h(P)={Pinfo['h']:.6f}  "
              f"C={C:.5g}  a0 check {np.array2string(info['a0_vals'], precision=6)}  T max {T.max().item():.2f}  ok {ok[1:].float().mean().item():.4f}  "
              f"max b'={bnew.abs().max().item():.4g}  min b'={bnew[1:].min().item():.4g}", flush=True)
    return bnew, cl, info
