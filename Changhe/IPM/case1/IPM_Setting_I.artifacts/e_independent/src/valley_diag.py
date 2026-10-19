"""Structure of the c_l valley: (1) the 30 smallest singular values of the weighted PDE Jacobian (corrected inverse iteration);
(2) the cheapest c_l direction v_cl (min |J v|, dc_l.v = 1) and its energy by radial band and angular sector, its effect on the far-field
boundary density b(R, theta), on h(P), on g(P); (3) the same with K characteristic rows as hard constraints (null space of G);
(4) how many of the smallest singular directions carry c_l (dc_l/dv_j).  Usage: python3 src/valley_diag.py <lsq_state.npz> [K per circle] [circles]"""
import sys, math, numpy as np, torch
sys.path.insert(0, 'src')
import diag, ipm1lsq, charrows
dev = 'cuda'
path = sys.argv[1]; nc = int(sys.argv[2]) if len(sys.argv) > 2 else 4
circles = tuple(float(v) for v in sys.argv[3].split(',')) if len(sys.argv) > 3 else (20.0, 60.0, 200.0)
angles = [float(v) for v in sys.argv[4].split(',')] if len(sys.argv) > 4 else None     # explicit angles in degrees (overrides nc)
dt_c = float(sys.argv[5]) if len(sys.argv) > 5 else 0.01; delta_c = float(sys.argv[6]) if len(sys.argv) > 6 else 1e-4
m, b, cl, d = diag.load(path, device=dev); m.k_tail = 1 / cl
ls = ipm1lsq.LSQ(m, Qr=int(d['Qr']), Qth=int(d['Qth']), chunk=256, verbose=False)
cl, c, fl = ls.cl_of_b(b, cl); ls.set_weights(b, cl); F, E, q = ls.F(b, cl, fl)
J = ls.jacobian(b, cl, q); a = ls.dcl_db
Rf = torch.linalg.qr(J, mode='r')[1]
N, M = ls.N, ls.M; rr = m.rad.rR.cpu().numpy()[1:]; thd = np.degrees(m.ang.theta_np)
def energy(v):
    vb = v.reshape(N, M).cpu().numpy() ** 2; rad = vb.sum(1); ang = vb.sum(0)
    bands = {'r<1': rad[rr < 1].sum(), '1-5': rad[(rr >= 1) & (rr < 5)].sum(), '5-15': rad[(rr >= 5) & (rr < 15)].sum(), '15-100': rad[(rr >= 15) & (rr < 100)].sum(), '>100': rad[rr >= 100].sum()}
    sect = {'0-10deg': ang[thd < 10].sum(), '10-45': ang[(thd >= 10) & (thd < 45)].sum(), '45-80': ang[(thd >= 45) & (thd < 80)].sum(), '80-90': ang[thd >= 80].sum()}
    return bands, sect
def describe(v, name):
    v = v / v.norm(); bands, sect = energy(v)
    Jv = (J @ v).norm().item(); dcl = (a @ v).item()
    # far-field boundary change of b: delta b(R, theta)/b(R, theta)
    vb = torch.zeros(N + 1, M, device=dev); vb[1:] = v.reshape(N, M)
    dbR = (m.rad.ext1_R @ vb)[0] / (m.rad.ext1_R @ b)[0]
    hr0 = ipm1lsq.h_row(ls, b, cl); dH = (hr0['grad'] @ v).item()
    print(f"[valley] {name}: |J v| = {Jv:.3e}, dc_l = {dcl:+.3e}, dH = {dH:+.3e} (per unit norm); energy by r: " + ", ".join(f"{k} {val:.2f}" for k, val in bands.items()) + "; by theta: " + ", ".join(f"{k} {val:.2f}" for k, val in sect.items()) + f"; max |delta b(R,.)/b| {dbR.abs().max().item():.2e} at theta {thd[dbR.abs().argmax().item()]:.0f} deg", flush=True)
    return v
# (1) smallest singular values
import os
cond = ls.conditioning(J, F, nvec=int(os.environ.get('NVEC', '30')), R=Rf)
sig = cond['sig_small']; dcl = cond['dcl_dv']
print(f"[valley] 30 smallest singular values of J_w (sigma_max {cond['sig_max']:.3e}):", np.array2string(sig, precision=3, max_line_width=250), flush=True)
print(f"[valley] dc_l per unit norm along them:", np.array2string(dcl, precision=2, max_line_width=250), flush=True)
print(f"[valley] 'cost per unit c_l' of each (sigma_j/|dc_l_j|):", np.array2string(sig / np.abs(dcl), precision=2, max_line_width=250), flush=True)
V = torch.tensor(cond['Vsmall'], device=dev)
for j in range(3): describe(V[:, j], f"softest singular direction {j} (sigma {sig[j]:.3e})")
# (2) cheapest c_l direction
y = torch.linalg.solve_triangular(Rf.T, a[:, None], upper=False)[:, 0]
v_cl = torch.linalg.solve_triangular(Rf, y[:, None], upper=True)[:, 0] / (y @ y)
print(f"[valley] cheapest c_l direction: cost per unit c_l {1/y.norm().item():.3e}, |v_cl| {v_cl.norm().item():.3e}", flush=True)
describe(v_cl, "cheapest c_l direction")
# (3) with characteristic rows as hard constraints
hr = ipm1lsq.h_row(ls, b, cl); xs = hr['x_star']
tg = charrows.default_targets(xs, float(d['R']), n_circle=nc, r_circles=circles, angles_deg=angles)
print(f"[valley] {len(tg)} targets: circles {circles}, angles {angles if angles is not None else 'equispaced'}; dt {dt_c}, delta {delta_c}", flush=True)
cr = charrows.CharRows(ls, tg, delta=delta_c, dt=dt_c, tmax=80.0, verbose=True)
C, G, info = cr.evaluate(b, cl, xs, hr['wP'], a)
Qf, _ = torch.linalg.qr(G.T, mode='complete'); Z = Qf[:, G.shape[0]:]
JZ = J @ Z; aZ = Z.T @ a; Rz = torch.linalg.qr(JZ, mode='r')[1]
yz = torch.linalg.solve_triangular(Rz.T, aZ[:, None], upper=False)[:, 0]
vz = torch.linalg.solve_triangular(Rz, yz[:, None], upper=True)[:, 0] / (yz @ yz); v_hard = Z @ vz
print(f"[valley] with {G.shape[0]} characteristic rows as hard constraints: cost per unit c_l {1/yz.norm().item():.3e}; |G v_hard| = {(G @ v_hard).norm().item():.2e} (should be 0)", flush=True)
describe(v_hard, "cheapest c_l direction with C rows hard")
# also: with the h-row hard
Gh = torch.cat([G, hr['grad'][None, :]], 0)
Qf2, _ = torch.linalg.qr(Gh.T, mode='complete'); Z2 = Qf2[:, Gh.shape[0]:]
JZ2 = J @ Z2; aZ2 = Z2.T @ a; Rz2 = torch.linalg.qr(JZ2, mode='r')[1]
yz2 = torch.linalg.solve_triangular(Rz2.T, aZ2[:, None], upper=False)[:, 0]
print(f"[valley] with C rows AND h(P) - 1 hard: cost per unit c_l {1/yz2.norm().item():.3e}", flush=True)
vz2 = torch.linalg.solve_triangular(Rz2, yz2[:, None], upper=True)[:, 0] / (yz2 @ yz2); describe(Z2 @ vz2, "cheapest c_l direction with C rows and h-row hard")
