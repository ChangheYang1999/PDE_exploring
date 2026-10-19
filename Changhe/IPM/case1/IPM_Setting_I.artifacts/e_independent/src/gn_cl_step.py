"""Lead 02:07Z item 4: Gauss-Newton exponent step along the cheapest c_l direction: s = J v_cl (residual change per unit c_l along the
valley), dk* = -<F, s>/|s|^2 = the (linearised) c_l offset of the discrete least-squares minimiser from the current state; its noise
level: the component of F along s has relative size |s| |dk*| / |F|. Usage: python3 src/gn_cl_step.py <lsq_state.npz>  (or project:N,M,L,R with 6 its)"""
import sys, math, numpy as np, torch
sys.path.insert(0, 'src')
import diag, ipm1lsq, ipm1disk, charac
dev = 'cuda'; path = sys.argv[1]
if path.startswith('project:'):
    from scipy.interpolate import RegularGridInterpolator
    N, M, L, R = path[8:].split(','); N, M, L, R = int(N), int(M), float(L), float(R)
    cand = np.load('final_candidate.npz', allow_pickle=True)
    cl = float(cand['c_l']); rc = cand['r']; thc = cand['theta']; H = cand['H']
    m = ipm1disk.IPM1Disk(N=N, M=M, L=L, R=R, gamma=1 / cl, device=dev); m.k_tail = 1 / cl
    interp = RegularGridInterpolator((np.log(rc), thc), H, method='cubic', bounds_error=False, fill_value=None)
    rR = m.rad.rR.cpu().numpy(); thR = m.ang.theta_np
    pts = np.array([[math.log(max(r, rc[0])), t] for r in rR[1:] for t in thR]); Hg = interp(pts).reshape(N, M)
    b = torch.ones(N + 1, M, device=dev); b[1:] = torch.tensor(np.exp(Hg), device=dev) / m.wR[1:, None]
    ls = ipm1lsq.LSQ(m, Qr=2 * N, Qth=2 * M + 1, chunk=256, verbose=False)
    cl, c, fl = ls.cl_of_b(b, cl); ls.set_weights(b, cl); b, cl, info = ls.solve(b, cl, maxit=6, lam=1e-6, svd_at_end=False, rel_stop=1e-9)
else:
    m, b, cl, d = diag.load(path, device=dev); m.k_tail = 1 / cl
    ls = ipm1lsq.LSQ(m, Qr=int(d['Qr']), Qth=int(d['Qth']), chunk=256, verbose=False)
    cl, c, fl = ls.cl_of_b(b, cl); ls.set_weights(b, cl)
F, E, q = ls.F(b, cl); J = ls.jacobian(b, cl, q); a = ls.dcl_db
Rf = torch.linalg.qr(J, mode='r')[1]
y = torch.linalg.solve_triangular(Rf.T, a[:, None], upper=False)[:, 0]
v_cl = torch.linalg.solve_triangular(Rf, y[:, None], upper=True)[:, 0] / (y @ y); del Rf
s = J @ v_cl; cost = s.norm().item()
dk = -(F @ s).item() / (s @ s).item()
print(f"[gnstep] state c_l {cl:.8f}: cost per unit c_l |s| = {cost:.4e}; <F,s>/|s|^2 -> dk* = {dk:+.4e} (linearised c_l offset of the discrete minimiser along the valley); relative size of F's component along s: {cost*abs(dk)/F.norm().item():.2e}; |F|_2 {F.norm().item():.3e}; rows {J.shape[0]} cols {J.shape[1]}", flush=True)
# the full Gauss-Newton step's c_l component (for comparison): d_GN = -J^+ F -> dc_l = a . d_GN. cusolver gels fails for
# large J (workspace size); fall back to the R factor: d = -R^{-1} R^{-T} J^T F (same minimiser; diagnostic only).
try:
    d_gn = -torch.linalg.lstsq(J, F[:, None], driver='gels').solution[:, 0]; how = 'gels'
except Exception as e:
    Rf = torch.linalg.qr(J, mode='r')[1]; g = J.T @ F
    y = torch.linalg.solve_triangular(Rf.T, g[:, None], upper=False)
    d_gn = -torch.linalg.solve_triangular(Rf, y, upper=True)[:, 0]; how = 'R-factor fallback'; del Rf
print(f"[gnstep]   full GN step dc_l = {(a @ d_gn).item():+.4e}, |d_GN| {d_gn.norm().item():.3e} ({how})", flush=True)
