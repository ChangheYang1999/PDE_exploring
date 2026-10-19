"""Diagnostics for a candidate (b, c_l) on the compactified grid: SPEC.md section 6 items D1-D8 (partial)."""
import sys, math, numpy as np, torch
sys.path.insert(0, 'src')
import ipm1


def load(path, device='cpu'):
    d = np.load(path)
    beta = float(d['beta']) if 'beta' in d.files else 0.0
    if 'disk' in d.files:
        import ipm1disk
        cluster = tuple(d['cluster']) if 'cluster' in d.files and d['cluster'].size == 3 else None
        pmap = float(d['pmap']) if 'pmap' in d.files else 1.0
        m = ipm1disk.IPM1Disk(N=int(d['N']), M=int(d['M']), L=float(d['L']), R=float(d['R']), gamma=float(d['gamma']), device=device, cluster=cluster, p=pmap)
        m.k_tail = 1.0 / float(d['cl'])
    else:
        m = ipm1.IPM1(N=int(d['N']), M=int(d['M']), L=float(d['L']), gamma=float(d['gamma']), p=float(d['p']), device=device, beta=beta)
    b = torch.tensor(d['b'], device=device)
    return m, b, float(d['cl']), d


def trace0(m, F, cls):
    """values at theta=0 of a (Nr, M) field in class cls (EE or OE); zero for EO/OO."""
    C = m.ang.to_coef(F, cls)
    if cls in ('EE', 'OE'):
        return C.sum(1)
    return torch.zeros(F.shape[0], device=F.device)


def trace90(m, F, cls):
    """values at theta=pi/2."""
    C = m.ang.to_coef(F, cls)
    k = torch.arange(m.M, device=F.device, dtype=F.dtype)
    if cls == 'EE':
        return (C * torch.cos(math.pi * k)[None, :]).sum(1)
    if cls == 'EO':
        return (C * torch.cos(math.pi * k)[None, :]).sum(1)   # sin((2k+1)pi/2) = (-1)^k
    return torch.zeros(F.shape[0], device=F.device)


def dy3_at_axis(m, F, cls, r):
    """d_y^3 F(x,0) for F in class EO (sum F_n sin(n theta), n odd), r = radii (x values); needs r>0."""
    C = m.ang.to_coef(F, cls)                  # (Nr, M) mode functions F_n(r)
    n = m.ang.n[cls][None, :]
    S = (m.rad.SR if hasattr(m.rad, 'SR') else (1 - m.rad.tR ** 2) / m.rad.QR)[:, None]
    rCp = S * (m.rad.DR @ C)                   # r F_n'(r)
    x = r[:, None]
    val = (-2 * n * C - n ** 3 * C) / x ** 3 + 3 * n * rCp / x ** 3
    return val.sum(1)


def dy2_at_axis(m, F, cls, r):
    """d_y^2 F(x,0) for F in class OE (sum G_n cos(n theta), n odd)."""
    C = m.ang.to_coef(F, cls)
    n = m.ang.n[cls][None, :]
    S = (m.rad.SR if hasattr(m.rad, 'SR') else (1 - m.rad.tR ** 2) / m.rad.QR)[:, None]
    rCp = S * (m.rad.DR @ C)
    x = r[:, None]
    return (rCp / x ** 2 - n ** 2 * C / x ** 2).sum(1)


def axis_data(m, b, cl, flds=None):
    """Return dict of x-axis traces on the Radau radii (excluding r=0 where needed)."""
    if flds is None:
        flds = m.fields(b)
    r = m.rad.rR
    rv = (r * m.vR)
    U1 = rv[:, None] * flds['Uhat1']; U2 = rv[:, None] * flds['Uhat2']
    W1_0 = cl * r + trace0(m, U1, 'OE')                                    # W_1(x,0)
    # d_y W_2(x,0) = c_l + (1/r) d_theta U2 at theta=0 ; (1/r) d_theta U2 = v * d_theta Uhat2
    h = cl + m.vR * trace0(m, m.ang.dtheta(flds['Uhat2'], 'EO'), 'OE')
    rho = m.rho_from_b(b)
    # rho_y(x,0) = (1/r) d_theta rho at theta = 0
    rho_y = trace0(m, m.ang.dtheta(rho, 'EO'), 'OE') / torch.where(r > 0, r, torch.ones_like(r))
    rho_y[0] = 0.0
    out = dict(r=r, W1=W1_0, h=h, rho_y=rho_y)
    mask = r > 0
    out['dy3_rho'] = dy3_at_axis(m, rho, 'EO', torch.where(mask, r, torch.ones_like(r)))
    out['dy3_rho'][0] = float('nan')
    out['dy2_W1'] = dy2_at_axis(m, U1, 'OE', torch.where(mask, r, torch.ones_like(r))); out['dy2_W1'][0] = float('nan')
    out['dy3_W2'] = dy3_at_axis(m, U2, 'EO', torch.where(mask, r, torch.ones_like(r))); out['dy3_W2'][0] = float('nan')
    # y-axis: W_2(0,y)/y = c_l + U_2(0,y)/y
    out['W2_over_y_axis'] = cl + m.vR * trace90(m, flds['Uhat2'], 'EO')
    return out, flds


def stagnation(m, b, cl, flds=None):
    ad, flds = axis_data(m, b, cl, flds)
    r = ad['r'].cpu().numpy(); W1 = ad['W1'].cpu().numpy()
    # first sign change of W1 for r>0 (W1 ~ (1-2cl) x < 0 near 0)
    idx = np.where((W1[1:-1] < 0) & (W1[2:] > 0))[0]
    res = dict(x_star=None)
    if len(idx) == 0:
        return res, ad, flds
    i = idx[0] + 1
    # refine with polynomial interpolation in t of the W1 trace
    tR = m.rad.tR_np
    from ipm1 import interp_matrix, bary_weights
    w = bary_weights(tR)
    def W1_at(t):
        P = interp_matrix(tR, [t], w)
        return float(P @ W1)
    ta, tb = tR[i], tR[i + 1]
    for _ in range(80):
        tm = 0.5 * (ta + tb)
        if W1_at(ta) * W1_at(tm) <= 0: tb = tm
        else: ta = tm
    ts = 0.5 * (ta + tb)
    xs = m.rad.rmap(torch.tensor(ts)).item()
    # mu1 = d_x W1(x*,0) = dW1/dr = (dt/dr) dW1/dt
    DR = m.rad.DR.cpu().numpy()
    dW1dt = interp_matrix(tR, [ts], w) @ (DR @ W1)
    mu1 = float(dW1dt) / m.rad.drdt(torch.tensor(ts)).item()
    h_at = float(interp_matrix(tR, [ts], w) @ ad['h'].cpu().numpy())
    g_at = float(interp_matrix(tR, [ts], w) @ ad['rho_y'].cpu().numpy())
    res = dict(x_star=xs, t_star=ts, mu1=mu1, mu2_from_div=2 * cl - mu1, h_at_P=h_at, rho_y_at_P=g_at,
               n_sign_changes=int(len(idx)))
    return res, ad, flds


def residual_norms(m, b, cl, flds=None):
    """Transport residual R = W.grad rho - rho (absolute) and normalised by |rho|+|X.grad rho|+|U.grad rho|, on regions."""
    if flds is None:
        flds = m.fields(b)
    E = m.residual(b, cl, flds)                           # equation divided by x^2 y w
    r = m.rad.rR[:, None]; cos = m.ang.cos[None, :]; sin = m.ang.sin[None, :]
    pref = r ** 3 * m.wR[:, None] * cos ** 2 * sin
    R = pref * E
    R[0, :] = 0.0
    rho = pref * b
    P = cos ** 2 * sin * b
    S = (m.rad.SR if hasattr(m.rad, 'SR') else (1 - m.rad.tR ** 2) / m.rad.QR)[:, None]
    rP_r = S * (m.rad.DR @ P)
    P_th = m.ang.dtheta(P, 'EO')
    Xgrad = r ** 3 * m.wR[:, None] * ((3 + m.omegaR)[:, None] * P + rP_r)
    Ugrad = r ** 3 * m.wR[:, None] * (flds['Ur_over_r'] * ((3 + m.omegaR)[:, None] * P + rP_r) + flds['Uth_over_r'] * P_th)
    denom = rho.abs() + Xgrad.abs() + Ugrad.abs()
    rr = m.rad.rR.cpu().numpy()
    out = {}
    regions = {'r<=2': (0, 2), '2<r<=10': (2, 10), '10<r<=100': (10, 100), 'r>100': (100, np.inf), 'all': (0, np.inf)}
    for name, (a, bnd) in regions.items():
        mask = torch.tensor((rr > a) & (rr <= bnd), device=b.device)
        if mask.sum() == 0:
            continue
        Rm = R[mask]; dm = denom[mask]
        out[name] = dict(R_abs_max=Rm.abs().max().item(), R_rel_max=(Rm.abs() / dm.clamp_min(1e-300)).max().item(),
                         R_abs_over_sup=(Rm.abs().max() / dm.max()).item(), n=int(mask.sum()))
    out['E_eq_max'] = E[1:].abs().max().item()
    return out, R, denom


def elliptic_residual(m, b, flds=None):
    """-Laplace psi - d_x rho on the coarse Radau grid from the fine psi~ mode functions (bounded), with spectral
    radial derivatives of the mode functions and exact angular derivatives (independent of the Green-ODE route)."""
    if flds is None:
        flds = m.fields(b)
    S = (m.rad.SR if hasattr(m.rad, 'SR') else (1 - m.rad.tR ** 2) / m.rad.QR)[:, None]
    s2 = m.s2R[:, None]; g = m.gamma
    kappa = 2 + (g - 1) * s2; rkappa_p = (g - 1) * 2 * s2 * (1 - s2)
    PsiC_R = flds['PsiC_R']; rPsiC_r = flds['rPsiC_r']
    nf = m.nf[None, :]
    Sm = m.S_OO_fc.T
    Psi = PsiC_R @ Sm; rPsi_r = rPsiC_r @ Sm
    r_d_r_rPsi_r = (S * (m.rad.DR @ rPsiC_r)) @ Sm
    Psi_thth = (PsiC_R * (-nf ** 2)) @ Sm
    G = kappa * Psi + rPsi_r
    rG_r = rkappa_p * Psi + kappa * rPsi_r + r_d_r_rPsi_r
    lap_over_v = kappa * G + rG_r + Psi_thth
    v = m.vR[:, None]
    # d_x rho on the coarse grid, pointwise exact (product rule in theta)
    cos = m.ang.cos[None, :]; sin = m.ang.sin[None, :]
    bth = m.ang.dtheta(b, 'EE')
    P = cos ** 2 * sin * b
    rP_r = S * (m.rad.DR @ b) * cos ** 2 * sin
    P_th = (cos ** 3 - 2 * cos * sin ** 2) * b + cos ** 2 * sin * bth
    Fhat = cos * ((3 + m.omegaR)[:, None] * P + rP_r) - sin * P_th
    r = m.rad.rR[:, None]
    dxrho = r ** 2 * m.wR[:, None] * Fhat
    Eell = -v * lap_over_v - dxrho
    return Eell, dxrho


def far_field(m, b):
    """Theta(theta) = rho / r^gamma at t->1 and at the last few radii."""
    g = m.gamma; L = m.L
    cos = m.ang.cos; sin = m.ang.sin
    binf = (m.rad.ext1_R @ b)[0]
    Theta_inf = L ** (3 - g) * cos ** 2 * sin * binf
    rows = {}
    r = m.rad.rR
    for i in range(m.N - 2, m.N + 1):
        rows[float(r[i])] = (r[i] ** 3 * m.wR[i] * cos ** 2 * sin * b[i] / r[i] ** g)
    return Theta_inf, rows


def report(path, device='cpu'):
    m, b, cl, d = load(path, device)
    flds = m.fields(b)
    c = m.psi_xy0(flds).item()
    print(f"file {path}\n N={m.N} M={m.M} L={m.L} gamma(frozen)={m.gamma:.8f} p={m.p:.4f}  c_l={cl:.10f}  1/c_l={1/cl:.8f}")
    print(f" D1: c=psi_xy(0)={c:.10f}  3c_l-1={3*cl-1:.10f}  |3c_l-1-c|={abs(3*cl-1-c):.2e}")
    print(f" D2: a(0)={b[0].mean().item():.12f} (spread {b[0].max().item()-b[0].min().item():.1e}); min b in Q = {b.min().item():.4e} (rho>0 iff b>0); max|b|={b.abs().max().item():.4g}")
    st, ad, _ = stagnation(m, b, cl, flds)
    if st['x_star'] is None:
        print(" D3: no sign change of W_1(x,0) found on the grid")
    else:
        print(f" D3: P=({st['x_star']:.6f},0)  mu1=d_xW_1(P)={st['mu1']:.6f}  2c_l-1={2*cl-1:.6f}  |mu1-(2c_l-1)|={abs(st['mu1']-(2*cl-1)):.2e}"
              f"  h(P)=d_yW_2(P)={st['h_at_P']:.6f} (|h-1|={abs(st['h_at_P']-1):.2e})  mu2_from_div={st['mu2_from_div']:.6f}  rho_y(P)={st['rho_y_at_P']:.4e}  sign changes of W1: {st['n_sign_changes']}")
    w2y = ad['W2_over_y_axis']
    print(f" D3: min_y W_2(0,y)/y = {w2y.min().item():.6f} at r={ad['r'][w2y.argmin()].item():.4g}")
    rn, R, denom = residual_norms(m, b, cl, flds)
    print(" D4/N4 transport residual (abs max, max pointwise rel, abs max / sup denom):")
    for k, v in rn.items():
        if isinstance(v, dict):
            print(f"    {k:10s} n={v['n']:5d}  |R|max={v['R_abs_max']:.3e}  rel_max={v['R_rel_max']:.3e}  |R|max/sup={v['R_abs_over_sup']:.3e}")
    print(f"    equation residual (divided form) max over t>-1: {rn['E_eq_max']:.3e}")
    Eell, dxrho = elliptic_residual(m, b, flds)
    rr = m.rad.rR
    for name, (a_, b_) in {'r<=2': (0, 2), '2<r<=10': (2, 10), '10<r<=100': (10, 100), 'r>100': (100, np.inf)}.items():
        mask = ((rr > a_) & (rr <= b_))
        if mask.sum() > 0:
            print(f" D8 elliptic residual {name:10s}: |E|max={Eell[mask].abs().max().item():.3e}  |E|max/max|d_x rho|={(Eell[mask].abs().max()/dxrho[mask].abs().max()).item():.3e}")
    Th, rows = far_field(m, b)
    print(" D5 far field Theta(theta)=rho/r^gamma at t=1:", np.array2string(Th.cpu().numpy(), precision=4, max_line_width=200))
    for rv, row in rows.items():
        print(f"      at r={rv:.3e}:", np.array2string(row.cpu().numpy(), precision=4, max_line_width=200))
    print(" D4 rho_y(x,0) on grid (first 12 radii):", np.array2string(ad['rho_y'][:12].cpu().numpy(), precision=4, max_line_width=200))
    print("    W_1(x,0) (first 16 radii):", np.array2string(ad['W1'][:16].cpu().numpy(), precision=4, max_line_width=200))
    print("    r (first 16):", np.array2string(ad['r'][:16].cpu().numpy(), precision=4, max_line_width=200))
    return m, b, cl, flds, st, ad


if __name__ == '__main__':
    report(sys.argv[1])


def weighted_identity(m, b, cl, flds=None):
    """D10: Q3 = int_{R^2} rho U.grad(phi) dX with phi = sin(3 theta) r^-3, and q = Q3/c^2 (target (pi/3)(1 - 2/c)).
    Quadrature: Clenshaw-Curtis in t on the Lobatto grid (integrand transferred by interpolation) x midpoint rule in theta
    (exact for the trigonometric degree present), times 4 for the four quadrants (integrand even/even)."""
    if flds is None:
        flds = m.fields(b)
    rad, ang = m.rad, m.ang
    # integrand on the Radau grid: rho * (U_r phi_r + U_theta phi_theta / r) * r  (area element r dr dtheta)
    r = rad.rR[:, None]; cos = ang.cos[None, :]; sin = ang.sin[None, :]
    rho = m.rho_from_b(b)
    rv = (rad.rR * m.vR)[:, None]
    Ur = rv * (flds['Uhat1'] * cos + flds['Uhat2'] * sin); Uth = rv * (-flds['Uhat1'] * sin + flds['Uhat2'] * cos)
    th = ang.theta[None, :]
    phi_r = -3 * torch.sin(3 * th) / r.clamp_min(1e-300) ** 4; phi_th_over_r = 3 * torch.cos(3 * th) / r.clamp_min(1e-300) ** 4
    integrand = rho * (Ur * phi_r + Uth * phi_th_over_r) * r      # per dr dtheta
    integrand[0, :] = 0.0
    # dr = (dr/dt) dt ; transfer to Lobatto for Clenshaw-Curtis: multiply by dr/dt (finite at t<1, integrand decays)
    drdt = rad.drdt(rad.tR)
    f_t = integrand * drdt[:, None]
    f_L = rad.P_RL @ f_t
    f_L[-1, :] = 0.0     # t = 1: integrand * dr/dt -> 0 (decay r^{2 gamma - 4} * r^{1+1/p})
    Q3 = 4.0 * ((rad.ccw @ f_L) * ang.dtheta_ds).sum().item() * (math.pi / (2 * m.M))
    c = m.psi_xy0(flds).item()
    return Q3, Q3 / c ** 2, (math.pi / 3) * (1 - 2 / c)
