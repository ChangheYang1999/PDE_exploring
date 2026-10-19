"""Axis rows (src/axisrows.py): FD gradient check on 3 directions, then the hard-constraint cheapest-c_l cost with the axis rows (and with
axis + characteristic rows if a charsolve target set is given). Usage: python3 src/axis_diag.py <lsq_state.npz>"""
import sys, math, numpy as np, torch
sys.path.insert(0, 'src')
import diag, ipm1lsq, axisrows, charac
dev = 'cuda'; path = sys.argv[1]
m, b, cl, d = diag.load(path, device=dev); m.k_tail = 1 / cl
ls = ipm1lsq.LSQ(m, Qr=int(d['Qr']), Qth=int(d['Qth']), chunk=256, verbose=False)
cl, c, fl = ls.cl_of_b(b, cl); ls.set_weights(b, cl); F, E, q = ls.F(b, cl, fl)
a = ls.compute_dcl_db(b, cl)
xs = charac.FieldEval(m, b, cl).find_P()['x_star']
ypts, xpts = axisrows.default_axis_points(xs, float(d['R']))
ar = axisrows.AxisRows(ls, ypts, xpts, n_gl=200)
A, G, info = ar.evaluate(b, cl, xs, a)
print(f"[axis] rows: y-axis {len(ypts)} (y = {ypts[0]:.3g} .. {ypts[-1]:.3g}), x-axis {len(xpts)}; values A_y: {np.array2string(A[:len(ypts)].cpu().numpy(), precision=2, max_line_width=250)}", flush=True)
print(f"[axis] A_x: {np.array2string(A[len(ypts):].cpu().numpy(), precision=2, max_line_width=250)}", flush=True)
# FD check along 3 directions (full recomputation of c_l, x*)
M = ls.M
for k in [5, 2000, ls.n - 7]:
    h = 1e-6; vals = []
    for sgn in (+1, -1):
        bt = b.clone(); bt.reshape(-1)[M + k] += sgn * h
        clt, _, _ = ls.cl_of_b(bt, cl); m.k_tail = 1 / clt; xst = charac.FieldEval(m, bt, clt).find_P()['x_star']
        with torch.no_grad():
            Ayt, Axt, _ = ar.values(bt, clt, xst); vals.append(torch.cat([Ayt, Axt]))
    fd = (vals[0] - vals[1]) / (2 * h)
    print(f"[axis] FD check dir {k}: max |FD - grad| = {(fd - G[:, k]).abs().max().item():.2e} (max |grad| {G[:, k].abs().max().item():.2e})", flush=True)
# hard-constraint cost
J = ls.jacobian(b, cl, q)
cc0 = ipm1lsq.cheapest_cl_cost(ls, J, a)
cc = ipm1lsq.cheapest_cl_cost(ls, J, a, G=G, w=1.0)
print(f"[axis] cheapest c_l cost: PDE rows only {cc0['alpha']:.3e}; with the {G.shape[0]} axis rows hard: {cc['alpha_hard']:.3e}; soft (w=1) {cc['alpha']:.3e}", flush=True)
# y-axis rows only / x-axis rows only
ccy = ipm1lsq.cheapest_cl_cost(ls, J, a, G=G[:len(ypts)], w=1.0); ccx = ipm1lsq.cheapest_cl_cost(ls, J, a, G=G[len(ypts):], w=1.0)
print(f"[axis]   y-axis rows only hard: {ccy['alpha_hard']:.3e}; x-axis rows only hard: {ccx['alpha_hard']:.3e}", flush=True)
# the cheapest direction with the axis rows hard: where does it live?
Qf, _ = torch.linalg.qr(G.T, mode='complete'); Z = Qf[:, G.shape[0]:]
JZ = J @ Z; aZ = Z.T @ a; Rz = torch.linalg.qr(JZ, mode='r')[1]
yz = torch.linalg.solve_triangular(Rz.T, aZ[:, None], upper=False)[:, 0]
v = Z @ (torch.linalg.solve_triangular(Rz, yz[:, None], upper=True)[:, 0] / (yz @ yz)); v = v / v.norm()
vb = v.reshape(ls.N, M).cpu().numpy() ** 2; rr = m.rad.rR.cpu().numpy()[1:]; thd = np.degrees(m.ang.theta_np)
rad = vb.sum(1); ang = vb.sum(0)
print(f"[axis] cheapest c_l direction with axis rows hard: energy r<1 {rad[rr<1].sum():.2f}, 1-5 {rad[(rr>=1)&(rr<5)].sum():.2f}, 5-15 {rad[(rr>=5)&(rr<15)].sum():.2f}, 15-100 {rad[(rr>=15)&(rr<100)].sum():.2f}, >100 {rad[rr>=100].sum():.2f}; theta 0-10 {ang[thd<10].sum():.2f}, 10-45 {ang[(thd>=10)&(thd<45)].sum():.2f}, 45-80 {ang[(thd>=45)&(thd<80)].sum():.2f}, 80-90 {ang[thd>=80].sum():.2f}", flush=True)
