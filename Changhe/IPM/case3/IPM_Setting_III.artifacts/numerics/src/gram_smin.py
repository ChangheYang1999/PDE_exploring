"""Lead's request (14:47Z item 5): sigma_N^2 = min_v (J v)^T M_Y (J v) / (v^T M_X v) with explicit Gram matrices.
Crude but physical version.  Unknown perturbation: delta b on the grid; delta rho = y w delta b (diagonal map).
Measure dmu = dX/(1 + r^2)  (= dX near 0, = dr/r dtheta at infinity), weight Wt = (1 + r^2)^(-nu), nu in (1/c_l, 1).
M_Y = diag(q Wt) on delta rho (L^2 part only);  M_X = M_Y + B^T diag(q Wt) B  (graph norm) with
   s = 1:  B = (1 + r^2)^(1/2) grad        (rows for d_x and d_y),
   s = 2:  B = (1 + r^2) Laplacian,
built from the spectral differentiation matrices (r d_r = g d_t on Radau nodes, d_theta on the quadrant grid), applied to
delta rho.  J = square unforced linearization at fixed c_l on delta b (rows: continuity, gauge in place of the identity
row, interior equations); the scaling direction is fixed by the gauge row so no projection is needed.  sigma_N^2 is the
smallest generalized eigenvalue of (J^T M_Y J, M_X)  [after mapping b -> rho: J acts on delta b; M on delta rho].
Quadrature weights q: Clenshaw-Curtis-like via the exact integration of the Radau interpolant in t is complex; we use
the trapezoid-free approach: q_ij = (dX/dmu factor) * w_t(i) * dtheta with w_t from Gauss-Radau weights computed by
lstsq on monomials in t (exact for degree <= N)."""
import sys, math, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
def radau_weights(tR):
    """quadrature weights on the Radau nodes exact for polynomials of degree <= N, via Chebyshev moments."""
    N = len(tR) - 1; VT = np.cos(np.outer(np.arange(N + 1), np.arccos(tR)))        # VT[k, i] = T_k(t_i)
    m = np.array([2.0/(1 - k*k) if k % 2 == 0 else 0.0 for k in range(N + 1)])     # int_-1^1 T_k dt
    return np.linalg.solve(VT, m)
def analyze(mdl, b, cl, label, nu=None):
    N, M = mdl.N, mdl.M; nb = (N+1)*M; gamma = 1/cl
    if nu is None: nu = 0.5*(gamma + 1)
    flds = mdl.fields(b)
    Jfull = mdl.jacobian(b, cl, flds); rows = list(range(0, M-1)) + [nb] + list(range(M, nb)); J = Jfull[rows][:, :nb]
    rad, ang = mdl.rad, mdl.ang
    r = rad.rR; th = ang.theta; g = rad.gR; t = rad.tR
    # dX/dmu: dX = r dr dtheta = r^2 (Q/(1-t^2)) dt dtheta -> dmu = dX/(1+r^2)
    wt = torch.tensor(radau_weights(rad.tR_np), device=dev)
    dmu = (r**2/(1 + r**2)*(rad.QR/(1 - t**2)))[:, None]*wt[:, None]*(math.pi/(2*M))*torch.ones(1, M, device=dev)   # (N+1, M); row 0 (t=-1): (1-t^2)=0 -> inf? handle
    dmu[0, :] = 0.0                                                     # the centre node has zero measure
    Wt = ((1 + r**2)**(-nu))[:, None]*torch.ones(1, M, device=dev)
    q = (dmu*Wt).reshape(-1)
    # map delta b -> delta rho (diagonal)
    yw = ((r*mdl.wR)[:, None]*ang.sin[None, :]).reshape(-1)
    # derivative operators on grid functions f (N+1, M) flattened row-major (i*M + j):
    # r d_r f = g D_R f  -> kron(diag(g) D_R, I_M);  d_theta f -> kron(I, Dth^T) (values -> values, class EO for rho)
    DR = torch.kron((g[:, None]*rad.DR).contiguous(), torch.eye(M, device=dev))        # r d_r
    Dth = torch.kron(torch.eye(N+1, device=dev), ang.D['EO'].T.contiguous())           # d_theta on class EO (rho is EO)
    rinv = (1.0/r.clamp_min(1e-300))[:, None].expand(N+1, M).reshape(-1)
    cos = ang.cos[None, :].expand(N+1, M).reshape(-1); sin = ang.sin[None, :].expand(N+1, M).reshape(-1)
    # d_x = cos d_r - sin d_th / r = (1/r)(cos r d_r - sin d_th);  d_y = (1/r)(sin r d_r + cos d_th)
    Dx = rinv[:, None]*(cos[:, None]*DR - sin[:, None]*Dth); Dy = rinv[:, None]*(sin[:, None]*DR + cos[:, None]*Dth)
    Dx[:M, :] = 0; Dy[:M, :] = 0                                        # centre node excluded (zero measure anyway)
    fac1 = torch.sqrt(1 + r**2)[:, None].expand(N+1, M).reshape(-1)
    B1 = torch.cat([fac1[:, None]*Dx, fac1[:, None]*Dy], 0); q2 = torch.cat([q, q])
    # Laplacian = (1/r^2)[(r d_r)^2 + d_th^2] on EO class: d_th^2 = Dth_OE . Dth_EO
    Dth2 = torch.kron(torch.eye(N+1, device=dev), (ang.D['OE'] @ ang.D['EO']).T.contiguous())
    Lap = (rinv**2)[:, None]*(DR @ DR + Dth2); Lap[:M, :] = 0
    B2 = ((1 + r**2)[:, None].expand(N+1, M).reshape(-1))[:, None]*Lap
    Yw = torch.diag(yw)
    MY = Yw @ torch.diag(q) @ Yw
    # the centre unknowns delta b(0, theta_j) do not enter delta rho at any node (y = 0 there); give them the H^1-at-origin
    # weight |d_y delta rho(0)|^2 = |delta b(0)|^2 times the measure of the first interior ring
    cw = q[M:2*M].sum().item()/M
    for j in range(M): MY[j, j] += cw
    out = [f"{label} N={N} M={M} cl={cl:.4f} nu={nu:.3f}:"]
    for s, B, qq in [(0, None, None), (1, B1, q2), (2, B2, q)]:
        MX = MY.clone() if B is None else MY + Yw @ (B.T @ (qq[:, None]*B)) @ Yw
        A = J.T @ MY @ J
        # generalized eigenvalue min of (A, MX): Cholesky of MX
        MXs = 0.5*(MX + MX.T)
        # Jacobi pre-scaling to tame the dynamic range, then symmetric square root by eigendecomposition
        d = torch.sqrt(torch.diag(MXs).clamp_min(1e-300)); Dm = 1.0/d
        MXn = Dm[:, None]*MXs*Dm[None, :]
        w_, V_ = torch.linalg.eigh(MXn); w_ = w_.clamp_min(w_.max()*1e-14)
        MXn_mhalf = V_ @ torch.diag(w_**-0.5) @ V_.T
        # G = M_Y^{1/2} J M_X^{-1/2}: with M_Y diagonal, M_Y^{1/2} = diag(sqrt(diag MY))
        MYh = torch.sqrt(torch.diag(MY).clamp_min(0))
        G = (MYh[:, None]*J) @ (Dm[:, None]*MXn_mhalf)
        sv = torch.linalg.svdvals(G)
        out.append(f" s={s}: sigma_min={sv[-1].item():.3e} (2nd {sv[-2].item():.3e}, max {sv[0].item():.3e})")
    svraw = torch.linalg.svdvals(J)
    out.append(f" | raw coefficient smin {svraw[-1].item():.2e}")
    msg = " ".join(out); print(msg, flush=True); return msg
if __name__ == '__main__':
    log = open('runs/gram_smin.log', 'a')
    for f in sys.argv[1:]:
        st = torch.load(f); mdl = ipm3.IPM3(N=st['N'], M=st['M'], L=st['L'], gamma=st['gamma'], p=st['p'], device=dev); mdl.gauge = 'inf'
        try:
            msg = analyze(mdl, st['b'].to(dev), st['cl'], f); log.write(msg + "\n"); log.flush()
        except Exception as e:
            print(f, "failed:", repr(e), flush=True)
