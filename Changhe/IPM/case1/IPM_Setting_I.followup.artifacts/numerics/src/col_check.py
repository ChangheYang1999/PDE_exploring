"""Consistency of Jacobian columns built with (Npsi_J, dt_J, F_fixed) against central differences of the accurate residual
(Npsi 480, dt 0.005, charmap.F) for a few representative columns of a state.
Usage: python3 src/col_check.py runs/state.npz [Npsi_J=240] [dt_J=0.01] [eps=1e-5]"""
import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn, charmap as cm, jtools as jt
spath = sys.argv[1]; NpJ = int(sys.argv[2]) if len(sys.argv) > 2 else 240; dtJ = float(sys.argv[3]) if len(sys.argv) > 3 else 0.01; eps = float(sys.argv[4]) if len(sys.argv) > 4 else 1e-5
m0, x, d = ipn.load_state(spath); b, cl = m0.unpack(x); C = float(d['C']); N, M = m0.N, m0.M
mJ = ipn.Model(N, M, m0.L, device='cuda', beta=m0.beta, nmodes=m0.nmodes, Mq=m0.Mq, Npsi=NpJ); chJ = cm.Charac(mJ)
mR = ipn.Model(N, M, m0.L, device='cuda', beta=m0.beta, nmodes=m0.nmodes, Mq=m0.Mq, Npsi=480); chR = cm.Charac(mR)
z = chR.pack(b, cl, C); n = z.numel(); r, _, _ = m0.radii(float(cl)); thd = m0.ang.theta_np * 180 / np.pi
REF_KW = dict(dt=0.005, dt_near=0.02, far_psi=True, r_far=1e10, n_coll=3, coll_scale=0.02)   # the reference is pinned (not jt.RES_KW, which changed to dt 0.01 at 07:30Z)
FJ = lambda zz: chJ.F_fixed(zz, dt=dtJ, dt_near=4 * dtJ); FR = lambda zz: chR.F(zz, **REF_KW)
xs = chR.find_P(chR.prepare(b, cl))[0].item()
# columns: node nearest P, a far y-axis node (r ~ 2e3, theta > 85), a node near the origin (r ~ 0.5, 45 deg), c_l
rr = r[1:][:, None] * np.ones((1, M)); tt = thd[None, :] * np.ones((N, 1)); xx = rr * np.cos(np.deg2rad(tt)); yy = rr * np.sin(np.deg2rad(tt))
cols = {'nearP': int(np.argmin(((xx - xs) ** 2 + yy ** 2).ravel())), 'far_yaxis': int(np.argmin((np.log(rr / 2e3) ** 2 + ((tt - 88) / 10) ** 2).ravel())),
        'near_origin': int(np.argmin((np.log(rr / 0.5) ** 2 + ((tt - 45) / 10) ** 2).ravel())), 'mid_x': int(np.argmin((np.log(rr / 3.0) ** 2 + ((tt - 5) / 10) ** 2).ravel())), 'c_l': n - 2}
out = {}
for name, j in cols.items():
    e = torch.zeros(n, device='cuda'); h = eps if j < N * M else 1e-5; e[j] = h
    t0 = time.time(); cJ = (FJ(z + e) - FJ(z - e)) / (2 * h); cJ1 = (FJ(z + e) - FJ(z)) / h; cR = (FR(z + e) - FR(z - e)) / (2 * h)
    out[name] = dict(col=j, r=float(rr.ravel()[j]) if j < N * M else None, theta=float(tt.ravel()[j]) if j < N * M else None, norm_R=float(cR.norm()),
                     diff_central_J_vs_R=float((cJ - cR).norm()), diff_onesided_J_vs_R=float((cJ1 - cR).norm()), diff_onesided_vs_central_J=float((cJ1 - cJ).norm()),
                     max_entry_diff_J_vs_R=float((cJ - cR).abs().max()), where_max=int((cJ - cR).abs().argmax()))
    print(f'{name}: col {j} r {out[name]["r"]} th {out[name]["theta"]}: |col| {out[name]["norm_R"]:.4e}; central (Npsi {NpJ}, dt {dtJ}) vs accurate: {out[name]["diff_central_J_vs_R"]:.3e} (max entry {out[name]["max_entry_diff_J_vs_R"]:.2e} at row {out[name]["where_max"]}); one-sided vs accurate {out[name]["diff_onesided_J_vs_R"]:.3e}; one-sided vs central (same inverse) {out[name]["diff_onesided_vs_central_J"]:.3e}  ({time.time()-t0:.0f}s)', flush=True)
json.dump(out, open(f'{jt.LANE}/runs/colcheck_{os.path.basename(spath).replace(".npz","")}_npsi{NpJ}_dt{dtJ}_eps{eps}.json', 'w'), indent=1)
