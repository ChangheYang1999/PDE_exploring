"""Augmented cheapest-c_l cost with the h(P) - 1 row (exact gradient) as a hard constraint, and with h-row + Taylor patch (K 10, r 1.5).
Usage: python3 src/hrow_cost.py <lsq_state.npz>"""
import sys, math, numpy as np, torch
sys.path.insert(0, 'src')
import diag, ipm1lsq, taylorpatch, charac
dev = 'cuda'; path = sys.argv[1]
m, b, cl, d = diag.load(path, device=dev); m.k_tail = 1 / cl
ls = ipm1lsq.LSQ(m, Qr=int(d['Qr']), Qth=int(d['Qth']), chunk=256, verbose=False)
cl, c, fl = ls.cl_of_b(b, cl); ls.set_weights(b, cl); F, E, q = ls.F(b, cl, fl)
J = ls.jacobian(b, cl, q); a = ls.dcl_db
hr = ipm1lsq.h_row(ls, b, cl); gH = hr['grad'][None, :]
cc0 = ipm1lsq.cheapest_cl_cost(ls, J, a)
cch = ipm1lsq.cheapest_cl_cost(ls, J, a, G=gH, w=1.0)
print(f"[hcost] state {path}: c_l {cl:.7f}, h(P)-1 {hr['H']:+.3e}; cheapest c_l cost: PDE only {cc0['alpha']:.3e}; with h(P)-1 = 0 HARD: {cch['alpha_hard']:.3e}  (PDE |F|_2 {F[:ls.Q].norm().item():.2e} -> c_l determined to about {F[:ls.Q].norm().item()/cch['alpha_hard']:.2e} by the floor if h(P) = 1 were exact)", flush=True)
# where does the cheapest direction live with the h-row hard
Qf, _ = torch.linalg.qr(gH.T, mode='complete'); Z = Qf[:, 1:]
JZ = J @ Z; aZ = Z.T @ a; Rz = torch.linalg.qr(JZ, mode='r')[1]
yz = torch.linalg.solve_triangular(Rz.T, aZ[:, None], upper=False)[:, 0]
v = Z @ (torch.linalg.solve_triangular(Rz, yz[:, None], upper=True)[:, 0] / (yz @ yz)); v = v / v.norm()
vb = v.reshape(ls.N, ls.M).cpu().numpy() ** 2; rr = m.rad.rR.cpu().numpy()[1:]; thd = np.degrees(m.ang.theta_np); rad = vb.sum(1); ang = vb.sum(0)
print(f"[hcost] cheapest direction with h-row hard: energy r<1 {rad[rr<1].sum():.2f}, 1-5 {rad[(rr>=1)&(rr<5)].sum():.2f}, 5-15 {rad[(rr>=5)&(rr<15)].sum():.2f}, 15-100 {rad[(rr>=15)&(rr<100)].sum():.2f}, >100 {rad[rr>=100].sum():.2f}; theta 0-10 {ang[thd<10].sum():.2f}, 10-45 {ang[(thd>=10)&(thd<45)].sum():.2f}, 45-80 {ang[(thd>=45)&(thd<80)].sum():.2f}, 80-90 {ang[thd>=80].sum():.2f}", flush=True)
del JZ, Z, Qf
# h-row + Taylor patch
xs = hr['x_star']
tp = taylorpatch.TaylorPatch(ls, K=10, r_fit=1.5, r_patch=1.5, n_patch=48, verbose=False)
rows, G, info = tp.evaluate(b, cl, xs, a)
Gall = torch.cat([gH, G], 0)
cca = ipm1lsq.cheapest_cl_cost(ls, J, a, G=Gall, w=1.0)
print(f"[hcost] with h-row AND 48 Taylor-patch rows (K 10, r 1.5) hard: {cca['alpha_hard']:.3e}", flush=True)
