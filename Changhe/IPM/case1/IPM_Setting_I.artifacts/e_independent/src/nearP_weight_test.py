"""Does upweighting the near-P rows make the least-squares objective determine c_l?  Project construct1 at (N, M) (optional cluster),
6 unweighted LSQ iterations (state S), then for w_P in {1, 10, 100, 1000}: multiply the rows with |X - P| < d_P by w_P (in J and F) and
report the cheapest c_l cost alpha(w_P), the floor |F_w|_2, and the Gauss-Newton exponent step dk*(w_P) = -<F_w, s>/|s|^2 (where the
weighted minimiser lies in c_l). If dk* converges with w_P, that value is the c_l of the near-P-weighted fit on this grid.
Then (if solve_its > 0) run the LSQ solve with the near-P weight w_solve applied inside the objective and report c_l, shells, cost.
Usage: python3 src/nearP_weight_test.py N M R L [its] [ovs] [p] [cluster:r,w,a] [dP:4] [wsolve:100] [solve_its:15] [tag]"""
import sys, math, numpy as np, torch
sys.path.insert(0, 'src')
import ipm1disk, ipm1lsq, charac
from scipy.interpolate import RegularGridInterpolator
dev = 'cuda'; base = ''
N, M, R, L = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
its = int(sys.argv[5]) if len(sys.argv) > 5 else 6; ovs = float(sys.argv[6]) if len(sys.argv) > 6 else 2.0; pmap = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
cluster = None; dP = 4.0; wsolve = 100.0; solve_its = 15; tag = f'npw_N{N}M{M}R{int(R)}'
for arg in sys.argv[8:]:
    if arg.startswith('cluster:'):
        rc_, w_, al_ = [float(v) for v in arg[8:].split(',')]; cluster = ipm1disk.RadialDisk.s_for_r(L, R, rc_, w_, al_, p=pmap)
    if arg.startswith('dP:'): dP = float(arg[3:])
    if arg.startswith('wsolve:'): wsolve = float(arg[7:])
    if arg.startswith('solve_its:'): solve_its = int(arg[10:])
    if arg.startswith('tag:'): tag = arg[4:]
cand = np.load('final_candidate.npz', allow_pickle=True)
cl = float(cand['c_l']); rc = cand['r']; thc = cand['theta']; H = cand['H']
m = ipm1disk.IPM1Disk(N=N, M=M, L=L, R=R, gamma=1 / cl, device=dev, p=pmap, cluster=cluster); m.k_tail = 1 / cl
interp = RegularGridInterpolator((np.log(rc), thc), H, method='cubic', bounds_error=False, fill_value=None)
rR = m.rad.rR.cpu().numpy(); thR = m.ang.theta_np
pts = np.array([[math.log(max(r, rc[0])), t] for r in rR[1:] for t in thR]); Hg = interp(pts).reshape(N, M)
b = torch.ones(N + 1, M, device=dev); b[1:] = torch.tensor(np.exp(Hg), device=dev) / m.wR[1:, None]
ls = ipm1lsq.LSQ(m, Qr=int(round(ovs * N)), Qth=2 * M + 1, chunk=256, verbose=False)
cl0, c0, fl0 = ls.cl_of_b(b, cl); ls.set_weights(b, cl0)
b0, cl0, info = ls.solve(b, cl0, maxit=its, lam=1e-6, svd_at_end=False, rel_stop=1e-9)
print(f"[npw] (N,M)=({N},{M}) R={R} cluster={cluster}: state S after {its} its: c_l {cl0:.8f}", flush=True)
F, E, q = ls.F(b0, cl0); J = ls.jacobian(b0, cl0, q); a = ls.dcl_db
xs = charac.FieldEval(m, b0, cl0).find_P()['x_star']
Xq = ls.rq[:, None] * ls.cq[None, :]; Yq = ls.rq[:, None] * ls.sq[None, :]; dPq = torch.sqrt((Xq - xs) ** 2 + Yq ** 2).reshape(-1)
near = (dPq < dP); nnear = int(near.sum())
print(f"[npw] near-P rows (|X-P| < {dP}): {nnear} of {ls.Q}; x* {xs:.5f}", flush=True)
for wP in [1.0, 10.0, 100.0, 1000.0]:
    wvec = torch.where(near, torch.full_like(dPq, wP), torch.ones_like(dPq))
    J.mul_(wvec[:, None]); Fw = F * wvec                        # in place (memory): J is unscaled below
    Rf = torch.linalg.qr(J, mode='r')[1]
    y = torch.linalg.solve_triangular(Rf.T, a[:, None], upper=False)[:, 0]
    v_cl = torch.linalg.solve_triangular(Rf, y[:, None], upper=True)[:, 0] / (y @ y); del Rf; torch.cuda.empty_cache()
    s = J @ v_cl; cost = s.norm().item(); dk = -(Fw @ s).item() / (s @ s).item()
    J.div_(wvec[:, None])
    print(f"[npw] w_P = {wP:6.0f}: cost per unit c_l {cost:.3e}; |F_w|_2 {Fw.norm().item():.3e} (near-P part {Fw[near].norm().item():.3e}); dk* = {dk:+.4e} (linearised c_l offset of the w_P-weighted minimiser); => c_l determined to about {Fw.norm().item()/cost:.2e}", flush=True)
    del Fw, s
del J
if solve_its > 0:
    # solve with the near-P weight inside the objective: scale ls.wrow
    ls.wrow = ls.wrow * torch.where(near, torch.full_like(dPq, wsolve), torch.ones_like(dPq))
    b1, cl1, info1 = ls.solve(b0, cl0, maxit=solve_its, lam=1e-6, svd_at_end=False, rel_stop=1e-9)
    F1, E1, q1 = ls.F(b1, cl1); den1 = ls.denominators(b1, cl1, q1); rel = (E1 / den1)
    xs1 = charac.FieldEval(m, b1, cl1).find_P()
    dP1 = torch.sqrt((Xq - xs1['x_star']) ** 2 + Yq ** 2)
    shells = "; ".join(f"[{lo},{hi}) {math.sqrt((rel[(dP1>=lo)&(dP1<hi)]**2).mean().item()):.1e}/{rel[(dP1>=lo)&(dP1<hi)].abs().max().item():.1e}" for lo, hi in [(0,0.5),(0.5,1),(1,2),(2,4),(4,8)])
    rq = ls.rq.cpu().numpy(); bands = "; ".join(f"{nm} {math.sqrt((rel[(rq>a_)&(rq<=b_)]**2).mean().item()):.1e}/{rel[(rq>a_)&(rq<=b_)].abs().max().item():.1e}" for nm, (a_, b_) in {'r<=2': (0, 2), '2-10': (2, 10), '10-100': (10, 100), '>100': (100, np.inf)}.items())
    print(f"[npw] SOLVE with near-P weight {wsolve} ({len(info1['hist'])-1} its): c_l {cl0:.8f} -> {cl1:.8f}, x* {xs1['x_star']:.5f}, h(P)-1 {xs1['h']-1:+.2e}; near-P shells (rms/max, unweighted normalisation): {shells}; bands: {bands}", flush=True)
    J1 = ls.jacobian(b1, cl1, q1); a1 = ls.dcl_db
    Rf = torch.linalg.qr(J1, mode='r')[1]; y = torch.linalg.solve_triangular(Rf.T, a1[:, None], upper=False)[:, 0]
    v1 = torch.linalg.solve_triangular(Rf, y[:, None], upper=True)[:, 0] / (y @ y); s1 = J1 @ v1
    print(f"[npw]   at the weighted solution: cost per unit c_l {s1.norm().item():.3e}, |F_w|_2 {F1.norm().item():.3e}, dk* {-(F1 @ s1).item()/(s1 @ s1).item():+.3e}", flush=True)
    np.savez(base + f'runs/{tag}.npz', b=b1.cpu().numpy(), cl=cl1, gamma=m.gamma, N=N, M=M, L=L, R=R, disk=True, eps=1.0, x_star=xs1['x_star'], lsq=True, Qr=ls.Qr, Qth=ls.Qth, cluster=np.array(cluster if cluster is not None else [], dtype=float), pmap=pmap, nearP_weight=wsolve, dP=dP)
    print(f"[npw] saved runs/{tag}.npz", flush=True)
