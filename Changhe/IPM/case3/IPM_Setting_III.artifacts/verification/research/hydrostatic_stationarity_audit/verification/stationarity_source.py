"""First-order stationarity of the least-squares functional at the HS stalls (verifier 08:49Z: a stalled Gauss-Newton point is not known to minimise).
For F(u) (rows: hydrostatic residual at the collocation points, a0 - 1, K - 1 [, centre row]) and J = dF/du with SVD J = U S V^T, the Gauss-Newton direction
restricted to the kept singular values (s >= 1e-13 smax, as in the solver) has directional derivative d/dlam (1/2)|F + lam J du|^2 = -|U_keep^T F|^2 at lam = 0.
The ratio rho_1 = |U_keep^T F| / |F| is the fraction of the residual in the (kept) range of J: rho_1 = 0 is a first-order stationary point of the least-squares
functional (a local minimiser or a saddle; second order not tested here).  Also reported: the gradient norm |J^T F| relative to smax |F|, the same with all
singular values kept, and rho_1 restricted to the visible subspace of src/hs_dilation_overlap.py.
Usage: python3 src/hs_stationarity.py runs/hsA_c3.0_N64.pt [more .pt]"""
import sys, time, numpy as np, torch
sys.path.insert(0, 'src'); import hs_solve
torch.set_default_dtype(torch.float64)
for f in sys.argv[1:]:
    t0 = time.time(); st = torch.load(f, weights_only=False); N, M, c = st['N'], st['M'], st['c']; io = st.get('inverse_options', {})
    P = st.get('map_exponent_P', st.get('p')); c_map = P / (P - 1)
    hsm = hs_solve.HSModel(N, M, c_map, n_in=io.get('n_in', 24), n_tail=io.get('n_tail', 80), fine=io.get('fine', False), hstep=io.get('hstep', 'x'))   # map from c_start (free-c states)
    centre = io.get('centre', 'drop'); hsm.centre_mode = centre; hsm.build_maps(); m = hsm.m; u = st['u'].to(m.dev)
    F, info = hsm.residual(u, c, centre); J = hsm.jacobian(u, c, False)
    U, S, Vh = torch.linalg.svd(J, full_matrices=False); keep = S >= 1e-13 * S[0]
    nF = F.norm().item(); r_keep = (U[:, keep].T @ F).norm().item() / nF; r_all = (U.T @ F).norm().item() / nF
    g = J.T @ F; gn = g.norm().item() / (S[0].item() * nF)
    # visible subspace
    Vs = []
    for k in range(m.M):
        A = (m.rad.sigR[:, None] ** k) * m.Ext[k]; U_, S_, Vh_ = torch.linalg.svd(A, full_matrices=False); kp = S_ >= 1e-8 * S_[0]
        Vk = torch.zeros(m.nu, int(kp.sum()), device=m.dev); Vk[m.offs[k]:m.offs[k + 1], :] = Vh_[kp].T; Vs.append(Vk)
    V = torch.cat(Vs, 1); JV = J @ V; Uv, Sv, Vhv = torch.linalg.svd(JV, full_matrices=False); kv = Sv >= 1e-13 * Sv[0]
    r_vis = (Uv[:, kv].T @ F).norm().item() / nF
    # the actual decrease available along the kept GN direction: predicted |F|^2 reduction fraction = r_keep^2
    print(f"{f:32s} {N:3d}x{M:<3d} c {c:.3f} rows {J.shape[0]} unknowns {J.shape[1]}: |F|2 {nF:.2e} |F|max {F.abs().max().item():.2e}  rho_1 = |U_keep^T F|/|F| {r_keep:.2e} (all s: {r_all:.2e}; visible subspace: {r_vis:.2e})  |J^T F|/(smax |F|) {gn:.2e}  [{time.time()-t0:.0f}s]")
