"""Taylor patch at P (src/taylorpatch.py): values, FD gradient check (2 directions), hard-constraint cheapest-c_l cost, and the
dependence on K, r_patch. Usage: python3 src/patch_diag.py <lsq_state.npz> [K] [r_fit] [r_patch] [n_patch]"""
import sys, math, numpy as np, torch
sys.path.insert(0, 'src')
import diag, ipm1lsq, taylorpatch, charac
dev = 'cuda'; path = sys.argv[1]
K = int(sys.argv[2]) if len(sys.argv) > 2 else 8; r_fit = float(sys.argv[3]) if len(sys.argv) > 3 else 2.0
r_patch = float(sys.argv[4]) if len(sys.argv) > 4 else 2.0; n_patch = int(sys.argv[5]) if len(sys.argv) > 5 else 48
m, b, cl, d = diag.load(path, device=dev); m.k_tail = 1 / cl
ls = ipm1lsq.LSQ(m, Qr=int(d['Qr']), Qth=int(d['Qth']), chunk=256, verbose=False)
cl, c, fl = ls.cl_of_b(b, cl); ls.set_weights(b, cl); F, E, q = ls.F(b, cl, fl)
a = ls.compute_dcl_db(b, cl)
xs = charac.FieldEval(m, b, cl).find_P()['x_star']
tp = taylorpatch.TaylorPatch(ls, K=K, r_fit=r_fit, r_patch=r_patch, n_patch=n_patch)
rows, G, info = tp.evaluate(b, cl, xs, a)
print(f"[patch] rows: {np.array2string(rows.cpu().numpy(), precision=2, max_line_width=250)}", flush=True)
M = ls.M
for k in [5, ls.n // 2 + 3]:
    h = 1e-6; vals = []
    for sgn in (+1, -1):
        bt = b.clone(); bt.reshape(-1)[M + k] += sgn * h
        clt, _, _ = ls.cl_of_b(bt, cl); m.k_tail = 1 / clt; xst = charac.FieldEval(m, bt, clt).find_P()['x_star']
        with torch.no_grad():
            rt, _ = tp.values(bt, clt, xst); vals.append(rt)
    fd = (vals[0] - vals[1]) / (2 * h)
    print(f"[patch] FD check dir {k}: max |FD - grad| = {(fd - G[:, k]).abs().max().item():.2e} (max |grad| {G[:, k].abs().max().item():.2e})", flush=True)
J = ls.jacobian(b, cl, q)
cc0 = ipm1lsq.cheapest_cl_cost(ls, J, a)
cc = ipm1lsq.cheapest_cl_cost(ls, J, a, G=G, w=1.0)
print(f"[patch] cheapest c_l cost: PDE rows only {cc0['alpha']:.3e}; with the {G.shape[0]} patch rows hard: {cc['alpha_hard']:.3e}; soft (w=1) {cc['alpha']:.3e}", flush=True)
Qf, _ = torch.linalg.qr(G.T, mode='complete'); Z = Qf[:, G.shape[0]:]
JZ = J @ Z; aZ = Z.T @ a; Rz = torch.linalg.qr(JZ, mode='r')[1]
yz = torch.linalg.solve_triangular(Rz.T, aZ[:, None], upper=False)[:, 0]
v = Z @ (torch.linalg.solve_triangular(Rz, yz[:, None], upper=True)[:, 0] / (yz @ yz)); v = v / v.norm()
vb = v.reshape(ls.N, M).cpu().numpy() ** 2; rr = m.rad.rR.cpu().numpy()[1:]; thd = np.degrees(m.ang.theta_np); rad = vb.sum(1); ang = vb.sum(0)
print(f"[patch] cheapest c_l direction with patch rows hard: energy r<1 {rad[rr<1].sum():.2f}, 1-5 {rad[(rr>=1)&(rr<5)].sum():.2f}, 5-15 {rad[(rr>=5)&(rr<15)].sum():.2f}, 15-100 {rad[(rr>=15)&(rr<100)].sum():.2f}, >100 {rad[rr>=100].sum():.2f}; theta 0-10 {ang[thd<10].sum():.2f}, 10-45 {ang[(thd>=10)&(thd<45)].sum():.2f}, 45-80 {ang[(thd>=45)&(thd<80)].sum():.2f}, 80-90 {ang[thd>=80].sum():.2f}", flush=True)
# sensitivity to K and r_patch (values only)
for K2, rp2 in [(6, 2.0), (10, 2.0), (8, 1.5), (8, 3.0)]:
    tp2 = taylorpatch.TaylorPatch(ls, K=K2, r_fit=max(rp2, 2.0), r_patch=rp2, n_patch=n_patch, verbose=False)
    with torch.no_grad():
        r2, inf2 = tp2.values(b, cl, xs)
    print(f"[patch] K={K2} r_patch={rp2}: rows rms {r2.pow(2).mean().sqrt().item():.2e} max {r2.abs().max().item():.2e}; W fit residuals {inf2['fit_res'][0].item():.1e} {inf2['fit_res'][1].item():.1e}", flush=True)
