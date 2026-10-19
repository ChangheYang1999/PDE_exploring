"""Resolution dependence of the c_l softness: project construct1 onto (N, M), R, run a few LSQ iterations (to be near the discrete
minimiser), then the cheapest-c_l cost 1/|R^{-T} dc_l/db| and the smallest singular values. Usage: python3 src/cost_vs_res.py N M R L [its] [ovs] [p]"""
import sys, math, numpy as np, torch
sys.path.insert(0, 'src')
import ipm1disk, ipm1lsq, charac
from scipy.interpolate import RegularGridInterpolator
dev = 'cuda'
N, M, R, L = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
its = int(sys.argv[5]) if len(sys.argv) > 5 else 6; ovs = float(sys.argv[6]) if len(sys.argv) > 6 else 2.0; pmap = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
cluster = None
for arg in sys.argv[8:]:
    if arg.startswith('cluster:'):
        rc_, w_, al_ = [float(v) for v in arg[8:].split(',')]; cluster = ipm1disk.RadialDisk.s_for_r(L, R, rc_, w_, al_, p=pmap)
cand = np.load('final_candidate.npz', allow_pickle=True)
cl = float(cand['c_l']); rc = cand['r']; thc = cand['theta']; H = cand['H']
m = ipm1disk.IPM1Disk(N=N, M=M, L=L, R=R, gamma=1 / cl, device=dev, p=pmap, cluster=cluster); m.k_tail = 1 / cl
print(f'[cost] cluster {cluster}', flush=True)
interp = RegularGridInterpolator((np.log(rc), thc), H, method='cubic', bounds_error=False, fill_value=None)
rR = m.rad.rR.cpu().numpy(); thR = m.ang.theta_np
pts = np.array([[math.log(max(r, rc[0])), t] for r in rR[1:] for t in thR]); Hg = interp(pts).reshape(N, M)
b = torch.ones(N + 1, M, device=dev); b[1:] = torch.tensor(np.exp(Hg), device=dev) / m.wR[1:, None]
Qr, Qth = int(round(ovs * N)), 2 * M + 1
ls = ipm1lsq.LSQ(m, Qr=Qr, Qth=Qth, chunk=256, verbose=True)
cl0, c0, fl0 = ls.cl_of_b(b, cl); ls.set_weights(b, cl0)
b1, cl1, info = ls.solve(b, cl0, maxit=its, lam=1e-6, svd_at_end=False, rel_stop=1e-9)
F, E, q = ls.F(b1, cl1); J = ls.jacobian(b1, cl1, q); a = ls.dcl_db
Rf = torch.linalg.qr(J, mode='r')[1]
cond = ls.conditioning(J, F, nvec=8, R=Rf)
y = torch.linalg.solve_triangular(Rf.T, a[:, None], upper=False)[:, 0]
pde = math.sqrt((F[:ls.Q] ** 2).sum().item() / ls.Q)
xs = charac.FieldEval(m, b1, cl1).find_P()['x_star']
den = ls.denominators(b1, cl1, q); rel = (E / den); Xq = ls.rq[:, None] * ls.cq[None, :]; Yq = ls.rq[:, None] * ls.sq[None, :]; dP = torch.sqrt((Xq - xs) ** 2 + Yq ** 2)
shells = "; ".join(f"[{lo},{hi}) {math.sqrt((rel[(dP>=lo)&(dP<hi)]**2).mean().item()):.1e}/{rel[(dP>=lo)&(dP<hi)].abs().max().item():.1e}" for lo, hi in [(0,0.5),(0.5,1),(1,2),(2,4),(4,8)])
print(f"[cost] near-P shells |X-P| (rms/max): {shells}", flush=True)
print(f"[cost] (N,M)=({N},{M}) R={R} L={L} p={pmap} ovs={ovs}: after {len(info['hist'])-1} its c_l {cl1:.7f} x* {xs:.5f} PDE rms {pde:.3e} |F|_2 {F.norm().item():.3e}; cheapest c_l cost {1/y.norm().item():.4e} per unit c_l (=> c_l undetermined to about {F.norm().item()*y.norm().item():.2e} at this floor); smallest singular values {np.array2string(cond['sig_small'], precision=2)} with dc_l {np.array2string(cond['dcl_dv'], precision=2)}; sigma_max {cond['sig_max']:.2e}", flush=True)
