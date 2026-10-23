"""
hs_stationarity.py -- is a saved hydrostatic stall a first-order stationary point of the discrete least-squares problem, or an artifact of the line-search
acceptance rule?  (Referee referee cauchy2 claims 5 and 12.)  Rebuilds the solver's maps for the saved state's size and quadrature (standard rule unless the
state records 'quad'), then computes at the saved coefficient vector u:
  F = residual rows (as the solver), J = exact Jacobian, thin SVD J = U S V^T;
  rho_K = |U_K^T F| / |F| for the cutoffs 1e-13 (the solver's), 1e-10, 1e-8 (retained residual fraction; the truncated Gauss-Newton step can reduce |F|^2 by at
          most rho_K^2 relative in the linear model);
  the first-order stationarity measure |J^T F| / (|J| |F|) (full) and |V_K S_K U_K^T F| / (|S_K| |F|) (retained);
  the truncated GN step du (cutoff 1e-13) and the EXACT profile phi(lam) = |F(u + lam du)|^2 for lam = 1, 0.5, ..., 2^-12 (the residual is quadratic in u, so
  phi is a quartic; evaluated directly), against the solver's acceptance test |F(u + lam du)| < (1 - 1e-4 lam) |F(u)|: if some lam gives |F(u + lam du)| < |F(u)|
  while no lam passes the test, the stall is an acceptance artifact (descent exists); if no lam reduces |F|, the point is a (numerical) local minimum along du.
usage: python3 src/hs_stationarity.py runs/state.pt
"""
import sys, json, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import hs_solve
torch.set_default_dtype(torch.float64)

def main(f, batch=4):
    st = torch.load(f, weights_only=False); N, M, c = st['N'], st['M'], st['c']; P = st.get('map_exponent_P', st.get('p')); c_map = P / (P - 1)
    io = st.get('inverse_options', {}); res = st.get('result') or {}; quad = res.get('quad', {})
    kw = dict(n_in=io.get('n_in', 24), n_tail=io.get('n_tail', 80), hstep=io.get('hstep', 'r'), inner=io.get('inner', 'log'),
              n0=quad.get('n0', 24), per_decade=quad.get('per_decade', 4), ngl=quad.get('ngl', 8), q=quad.get('q', 3))
    hsm = hs_solve.HSModel(N, M, c_map, **kw); hsm.centre_mode = 'drop'; hsm.build_maps(batch=batch); u = st['u'].to(hsm.dev)
    F, info = hsm.residual(u, c, 'drop'); nF = F.norm().item()
    print(f"{f.split('/')[-1]} {N}x{M} c={c} maps {kw}: |F|2 {nF:.4e} |F|max {F.abs().max().item():.4e} (saved: {res.get('nodes_F2', float('nan')):.4e} / {res.get('nodes_Fmax', float('nan')):.4e})")
    J = hsm.jacobian(u, c, False); U, S, Vh = torch.linalg.svd(J, full_matrices=False)
    UtF = U.T @ F; g = J.T @ F
    print(f"  smax {S[0].item():.3e}  smin {S[-1].item():.3e}  |J^T F|/(smax |F|) = {g.norm().item() / (S[0].item() * nF):.3e}  (first-order stationarity, full)")
    for cut in [1e-13, 1e-10, 1e-8, 1e-6]:
        keep = S > cut * S[0]; rho = UtF[keep].norm().item() / nF
        gK = (S[keep] * UtF[keep]).norm().item() / (S[0].item() * nF)
        print(f"  cutoff {cut:.0e}: retained {int(keep.sum())}/{len(S)}  rho_K = |U_K^T F|/|F| = {rho:.3e}  (max relative decrease of |F|^2 in the linear model rho_K^2 = {rho**2:.2e});  |S_K U_K^T F|/(smax |F|) = {gK:.3e}")
    keep = S > 1e-13 * S[0]; du = Vh[keep].T @ ((UtF[keep]) * (-1.0) / S[keep])
    print(f"  truncated GN step: |du| {du.norm().item():.3e}, directional derivative F^T J du = {(F @ (J @ du)).item():.4e} (= -|U_K^T F|^2 = {-(UtF[keep].norm().item()**2):.4e})")
    print("  exact profile along du: lam, |F(u+lam du)|/|F(u)|, acceptance threshold (1 - 1e-4 lam):")
    best = (1.0, 0.0)
    for k in range(0, 13):
        lam = 2.0 ** (-k); Fn, _ = hsm.residual(u + lam * du, c, 'drop'); r = Fn.norm().item() / nF
        print(f"    {lam:9.3e}  {r:.8f}  {1 - 1e-4 * lam:.8f}  {'PASS' if r < 1 - 1e-4 * lam else ('descent but rejected' if r < 1 else 'increase')}")
        if r < best[0]: best = (r, lam)
    print(f"  best ratio {best[0]:.8f} at lam {best[1]:.3e}: {'the stall is NOT a local minimum along du (acceptance artifact)' if best[0] < 1 else 'no decrease along du: numerical local minimum along the GN direction'}")
    # retained-subspace exact minimiser estimate: the attainable |F| in the linear model
    print(f"  linear-model attainable |F|/|F_0| = sqrt(1 - rho_K^2) = {np.sqrt(max(0.0, 1 - (UtF[keep].norm().item()/nF)**2)):.8f}")

    # ---- PART 2 (external referee mapq1 item 2): sensitivity of the solver's endpoint to the map error ---------------------------------------------
    # b = F_ref(u) - F_map(u) = delta V_1 . (G_x u) + delta V_2 . (G_y u) with delta V = V_ref - V_map at the nodes (V_ref: resolved evaluator hs_layer.hydro_V_log);
    # d = -V_K S_K^-1 U_K^T b is the first-order response of the endpoint to correcting the maps; reported: max |g_d|/(1 + r)^p on the hs_cauchy points
    # (the metric of the between-size differences), the unabsorbed forcing |(I - U_K U_K^T) b|/|b|, and the distribution of U_K^T b over the singular values.
    import hs, hs_layer, hs_cauchy
    X, Y = hsm.X, hsm.Y; ge = hs.GEval(hsm.m, hsm.m.beta_full(u)); npts = len(X)
    V1r = np.zeros(npts); V2r = np.zeros(npts); CH = int(__import__('os').environ.get('HS_CH', '300'))
    for k0 in range(0, npts, CH):
        sl = slice(k0, min(npts, k0 + CH))
        v1, v2 = hs_layer.hydro_V_log(ge, X[sl], Y[sl], n0=32, per_decade=10, ngl=16, n_tail=400, q=2, hrel=1e-5, ymax_dec=np.log10(max(Y.max(), 10.0)))
        V1r[sl] = np.asarray(v1).reshape(-1); V2r[sl] = np.asarray(v2).reshape(-1)
    mp = hsm.maps; V1m = (mp['M1'] @ u).cpu().numpy(); V2m = (mp['M2'] @ u).cpu().numpy(); gx = (mp['Gx'] @ u).cpu().numpy(); gy = (mp['Gy'] @ u).cpu().numpy()
    dV1 = V1r - V1m; dV2 = V2r - V2m; b_rows = dV1 * gx + dV2 * gy
    R = np.hypot(X, Y)
    print("  PART 2: map error at the nodes (V_ref - V_map) and the forcing b = dV1 gx + dV2 gy, by region: max|dV1|, max|dV2|, max|b|, max|b|/N_f")
    g_nodes = (mp['G'] @ u).cpu().numpy(); Nf = np.abs((c * X + V1r) * gx) + np.abs((c * Y + V2r) * gy) + np.abs(g_nodes)
    for lo, hi in [(0, 0.1), (0.1, 1), (1, 100), (100, 1e300)]:
        msk = (R >= lo) & (R < hi)
        if msk.any(): print(f"    r in [{lo:g}, {hi:g}): {np.abs(dV1[msk]).max():.3e}  {np.abs(dV2[msk]).max():.3e}  {np.abs(b_rows[msk]).max():.3e}  {(np.abs(b_rows) / Nf)[msk].max():.3e}")
    nF_rows = F[:len(X)].norm().item()
    # export for the verifier: nodes, map velocities, resolved velocities, derivatives, solver residual rows (artifacts/data/hs_points_export/<tag>_nodes_maps.npz)
    import os; tag = f.split('/')[-1][:-3]; outdir = 'numerics/data/hs_points_export'; os.makedirs(outdir, exist_ok=True)
    np.savez_compressed(f"{outdir}/{tag}_nodes_maps.npz", X=X, Y=Y, V1_map=V1m, V2_map=V2m, V1_ref=V1r, V2_ref=V2r, gx=gx, gy=gy, g=g_nodes, F_rows=F[:len(X)].cpu().numpy(), b_rows=b_rows,
                        quad_map=np.array(str(kw)), quad_ref=np.array('hs_layer.hydro_V_log n0=32 per_decade=10 ngl=16 n_tail=400 q=2 hrel=1e-5 (step 1e-5 (1 + r))'), N=N, M=M, c=c)
    print(f"    exported {outdir}/{tag}_nodes_maps.npz (X, Y, V1_map, V2_map, V1_ref, V2_ref, gx, gy, g, F_rows, b_rows)")
    b = torch.zeros_like(F); b[:len(X)] = torch.tensor(b_rows, device=F.device)        # zero perturbation of the normalisation rows
    print(f"    |b| {b.norm().item():.3e} against |F_rows| {nF_rows:.3e}; F_ref = F + b has |F_ref|max {(F + b).abs().max().item():.3e}")
    Utb = U.T @ b
    for cut in [1e-13, 1e-10, 1e-8]:
        keep = S > cut * S[0]; d = -(Vh[keep].T @ (Utb[keep] / S[keep]))
        ged = hs.GEval(hsm.m, hsm.m.beta_full(d)); Xc, Yc, Rc = hs_cauchy.points(); gd, gxd, gyd = ged(Xc, Yc); p = 1.0 / c
        line = f"    cutoff {cut:.0e}: unabsorbed |(I - U_K U_K^T) b|/|b| = {(b - U[:, keep] @ Utb[keep]).norm().item() / b.norm().item():.3e}; |d| {d.norm().item():.3e}; predicted change of the function max |g_d|/(1+r)^p by region:"
        for lo, hi in [(0, 0.1), (0.1, 1), (1, 100), (100, 1e4), (1e4, 1e7)]:
            m_ = (Rc >= lo) & (Rc < hi); line += f" {(np.abs(gd[m_]) / (1 + Rc[m_]) ** p).max():.2e}"
        print(line + f"   (gradient: {(np.hypot(gxd, gyd) / (1 + Rc) ** (p - 1))[(Rc >= 1) & (Rc < 100)].max():.2e} in [1, 100))")
    keep = S > 1e-13 * S[0]; w = (Utb[keep] ** 2); w = w / w.sum(); Sk = S[keep]
    for lo, hi in [(1e-13, 1e-10), (1e-10, 1e-7), (1e-7, 1e-4), (1e-4, 1e-1), (1e-1, 2)]:
        m_ = (Sk > lo * S[0]) & (Sk <= hi * S[0])
        print(f"    share of |U_K^T b|^2 in singular values in ({lo:.0e}, {hi:.0e}] smax: {w[m_].sum().item():.3f} ({int(m_.sum())} directions)")
    # exact nonlinear check of the linear prediction with the OLD maps: F_map(u + d) vs F_map(u) + J d (remainder (M1 d)(Gx d) + (M2 d)(Gy d))
    d = -(Vh[keep].T @ (Utb[keep] / S[keep])); Fd, _ = hsm.residual(u + d, c, 'drop')
    print(f"    nonlinear check with the old maps: |F_map(u + d)|max {Fd.abs().max().item():.3e} against linear |F + J d|max {(F + J @ d).abs().max().item():.3e}; |F_map(u+d) + b|max (the corrected residual if b were constant) {(Fd + b).abs().max().item():.3e}")

if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 4)
