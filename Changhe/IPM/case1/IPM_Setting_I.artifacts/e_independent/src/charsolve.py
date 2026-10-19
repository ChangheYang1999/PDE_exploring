"""Characteristic-matching rows (fixed-W rigidity) appended to the LSQ system.
Usage: python3 src/charsolve.py <lsq_state.npz> <tag> <weight> [maxit] [n_circle] [circles e.g. 20,60,200] [delta] [dt]
Step 1: at the state, C_i = log rho(X_i) - T_i - log y_e,i - log g(P) for targets X_i (circles, angles 3..75 deg); their gradients;
  the softest directions v_j of the weighted Jacobian and DC[v_j] (does the row set act on the c_l-carrying directions?).
Step 2 (weight > 0): re-solve with the rows weight * C_i appended; report c_l, x*, h(P), C spread, bands, FD check."""
import sys, time, math, numpy as np, torch
sys.path.insert(0, 'src')
import diag, ipm1lsq, charrows, charac, check_fd
dev = 'cuda'; base = ''
path, tag, lam_w = sys.argv[1], sys.argv[2], float(sys.argv[3])     # lam_w: NORMALISED weight: objective = |F|^2/Q + lam_w^2 |C|^2/K, i.e. row weight w = lam_w sqrt(Q/K)
maxit = int(sys.argv[4]) if len(sys.argv) > 4 else 40
n_circle = int(sys.argv[5]) if len(sys.argv) > 5 else 12
circles = tuple(float(v) for v in sys.argv[6].split(',')) if len(sys.argv) > 6 else (20.0, 60.0, 200.0)
delta = float(sys.argv[7]) if len(sys.argv) > 7 else 1e-4
dt = float(sys.argv[8]) if len(sys.argv) > 8 else 0.005
m, b, cl, d = diag.load(path, device=dev); m.k_tail = 1 / cl
Qr, Qth = int(d['Qr']), int(d['Qth'])
ls = ipm1lsq.LSQ(m, Qr=Qr, Qth=Qth, chunk=256, verbose=True)
K_rows = n_circle * len([rc for rc in circles if rc < float(d['R'])]); wgt = lam_w * math.sqrt(ls.Q / K_rows)
print(f"[char] normalised weight lam = {lam_w} -> row weight w = {wgt:.3f} (Q = {ls.Q}, K = {K_rows})", flush=True)
cl, c, fl = ls.cl_of_b(b, cl); ls.set_weights(b, cl); F, E, q = ls.F(b, cl, fl)
print(f"[char] state {path}: c_l {cl:.10f}, rms {math.sqrt((F**2).mean().item()):.3e}", flush=True)
J = ls.jacobian(b, cl, q); Rf = torch.linalg.qr(J, mode='r')[1]
cond = ls.conditioning(J, F, nvec=6, R=Rf)
hr = ipm1lsq.h_row(ls, b, cl)
xs = hr['x_star']
tg = charrows.default_targets(xs, float(d['R']), n_circle=n_circle, r_circles=circles)
cr = charrows.CharRows(ls, tg, delta=delta, dt=dt, tmax=60.0)
C, G, info = cr.evaluate(b, cl, xs, hr['wP'], ls.dcl_db)
print(f"[char] {len(tg)} targets; C_i = {np.array2string(C.cpu().numpy(), precision=2, max_line_width=250)}", flush=True)
print(f"[char] T_i = {np.array2string(info['T'].cpu().numpy(), precision=2, max_line_width=250)}; g(P) = {info['g']:.6f}; h(P)-1 = {hr['H']:+.3e}", flush=True)
V = torch.tensor(cond['Vsmall'], device=dev)
DC = (G @ V).cpu().numpy()          # (K, nvec)
print(f"[char] softest directions: sigma_j {cond['sig_small']}; dc_l/dv_j {cond['dcl_dv']}", flush=True)
print(f"[char]   |DC[v_j]|_2 over rows = {np.linalg.norm(DC, axis=0)}; gain weight^2 |DC v_j|^2/sigma_j^2 = {wgt**2 * np.linalg.norm(DC, axis=0)**2 / cond['sig_small']**2}", flush=True)
with np.errstate(divide='ignore'):
    print(f"[char]   residual cost of dc_l = 1e-3 along v_j: without rows {cond['sig_small'] * 1e-3 / np.abs(cond['dcl_dv'])}, with rows (upper bound along v_j) {np.sqrt(cond['sig_small']**2 + wgt**2 * np.linalg.norm(DC, axis=0)**2) * 1e-3 / np.abs(cond['dcl_dv'])} (|F|_2 {F.norm().item():.2e})", flush=True)
cc = ipm1lsq.cheapest_cl_cost(ls, J, ls.dcl_db, G=G, w=wgt if wgt > 0 else 1.0)
print(f"[char] AUGMENTED cheapest c_l cost (min over all v with dc_l.v = 1): PDE rows only {cond['cost_cl']:.3e}; with the C rows at weight {wgt:.3f}: {cc['alpha']:.3e}; with C v = 0 as a hard constraint: {cc['alpha_hard']:.3e}  (PDE |F|_2 {F[:ls.Q].norm().item():.2e}; so c_l determined to about {F[:ls.Q].norm().item()/cc['alpha_hard']:.1e} by the floor, if the rows were exact)", flush=True)
print(f"[char] C partials: mean C {C.mean().item():+.3e}, spread {(C.max()-C.min()).item():.2e}; dC/dlog(delta) expected -(h-1)/h = {-(hr['hP']-1)/hr['hP']:+.3e}", flush=True)
v_cl = torch.tensor(cond['v_cl'], device=dev); DCc = (G @ v_cl).cpu().numpy()
print(f"[char] cheapest c_l direction: cost per unit c_l {cond['cost_cl']:.3e} (1e-3 costs {cond['cost_cl']*1e-3:.2e} vs |F|_2 {F.norm().item():.2e}); dC_i/dc_l along it: {np.array2string(DCc, precision=3, max_line_width=250)}; |DC|_2 {np.linalg.norm(DCc):.3e}; with the rows (weight {wgt}) the cost per unit c_l becomes {math.sqrt(cond['cost_cl']**2 + (wgt*np.linalg.norm(DCc))**2):.3e}", flush=True)
del J, Rf
if lam_w == 0.0:
    print("[char] weight 0: diagnostic only", flush=True); sys.exit(0)
ls.extra_rows = [('char', wgt)]; ls.char_rows = cr
t0 = time.time(); log = open(base + f'runs/charsolve_{tag}.dat', 'w')
b1, cl1, info1 = ls.solve(b, cl, maxit=maxit, lam=1e-6, log=log, rel_stop=1e-7, svd_at_end=True); log.close()
hr1 = ipm1lsq.h_row(ls, b1, cl1)
C1, _, inf1 = cr.evaluate(b1, cl1, hr1['x_star'], hr1['wP'], ls.dcl_db, need_grad=False)
print(f"[char] with rows (normalised weight {lam_w}, row weight {wgt:.2f}): c_l {cl1:.10f} (was {cl:.10f}; construct1 5.5763219), x* {hr1['x_star']:.8f}, h(P)-1 {hr1['H']:+.3e}, C spread {(C1.max()-C1.min()).item():.2e} (max |C| {C1.abs().max().item():.2e}), rms {info1['rms']:.3e}, {len(info1['hist'])-1} its, {time.time()-t0:.0f}s", flush=True)
E1 = info1['E']; q1 = info1['q']; den1 = ls.denominators(b1, cl1, q1); rq = ls.rq.cpu().numpy(); rel = (E1 / den1)
for name, (a_, b_) in {'r<=2': (0, 2), '2-10': (2, 10), '10-100': (10, 100), '>100': (100, np.inf)}.items():
    mk = (rq > a_) & (rq <= b_); v = rel[mk]; print(f"[char]   between-node |E|/den {name}: rms {math.sqrt((v**2).mean().item()):.2e} max {v.abs().max().item():.2e}", flush=True)
Xq = ls.rq[:, None] * ls.cq[None, :]; Yq = ls.rq[:, None] * ls.sq[None, :]; dP = torch.sqrt((Xq - hr1['x_star']) ** 2 + Yq ** 2)
for dd in [0.5, 1.0, 2.0]:
    mk = dP < dd; print(f"[char]   |X-P| < {dd}: rms {math.sqrt((rel[mk]**2).mean().item()):.2e} max {rel[mk].abs().max().item():.2e}", flush=True)
if 'sig_small' in info1: print(f"[char] conditioning with rows: sigma_small {info1['sig_small']}, dc_l/dv {info1['dcl_dv']}", flush=True)
np.savez(base + f'runs/charsolve_{tag}.npz', b=b1.cpu().numpy(), cl=cl1, gamma=m.gamma, N=m.N, M=m.M, L=m.L, R=float(d['R']), disk=True, eps=1.0, x_star=hr1['x_star'], lsq=True, Qr=Qr, Qth=Qth, char_weight=wgt, char_lam=lam_w, targets=tg,
         cluster=d['cluster'] if 'cluster' in d.files else np.array([]), pmap=float(d['pmap']) if 'pmap' in d.files else 1.0)
check_fd.check(base + f'runs/charsolve_{tag}.npz', K=3000, rmin=1e-3, rmax=float(d['R']) * 0.98, hrel=1e-5, device=dev)
print(f"[char] saved runs/charsolve_{tag}.npz", flush=True)
