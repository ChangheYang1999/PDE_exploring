"""h(P) = 1 as an extra least-squares row (astra lsqpin recommendation; lead 21:49Z idea in the LSQ setting).
Usage: python3 src/hrow_lsq.py <lsq_state.npz> <tag> [weight alpha] [maxit]
Step 1 (diagnostic): at the state, compute the weighted Jacobian J, its R factor, the 4 softest right singular directions v_j and
  sigma_j = |J v_j|; compute DH[v_j] for H = h(P) - 1 (exact gradient incl. motion of P); print the gain alpha^2 |DH v_j|^2 / sigma_j^2
  for the given alpha, and the c_l component dc_l/dv_j. If the H row acts on the c_l-carrying soft directions, adding it pins c_l.
Step 2: re-solve with the row alpha (h(P) - 1) appended; report c_l, x*, h(P), between-node bands, conditioning with the row."""
import sys, time, math, numpy as np, torch
sys.path.insert(0, 'src')
import diag, ipm1lsq, check_fd
dev = 'cuda'; base = ''
path, tag = sys.argv[1], sys.argv[2]; alpha = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0; maxit = int(sys.argv[4]) if len(sys.argv) > 4 else 60
m, b, cl, d = diag.load(path, device=dev); m.k_tail = 1 / cl
Qr, Qth = int(d['Qr']), int(d['Qth'])
ls = ipm1lsq.LSQ(m, Qr=Qr, Qth=Qth, chunk=256, verbose=True)
cl, c, fl = ls.cl_of_b(b, cl); ls.set_weights(b, cl); F, E, q = ls.F(b, cl, fl)
print(f"[hrow] state {path}: c_l {cl:.10f}, rms {math.sqrt((F**2).mean().item()):.3e}", flush=True)
J = ls.jacobian(b, cl, q)
Rf = torch.linalg.qr(J, mode='r')[1]
cond = ls.conditioning(J, F, nvec=6, R=Rf)
hr = ipm1lsq.h_row(ls, b, cl)
print(f"[hrow] H = h(P) - 1 = {hr['H']:+.3e}; x* {hr['x_star']:.8f}; w'(P) {hr['wP']:.6f} (2c_l-1 {2*cl-1:.6f}); h_x(P) {hr['h_x']:+.5f}; |grad H| {hr['grad'].norm().item():.3e}", flush=True)
V = torch.tensor(cond['Vsmall'], device=dev)
DH = (hr['grad'] @ V).cpu().numpy()
print(f"[hrow] softest directions: sigma_j = {cond['sig_small']}", flush=True)
print(f"[hrow]   dc_l/dv_j        = {cond['dcl_dv']}", flush=True)
print(f"[hrow]   DH[v_j]          = {DH}", flush=True)
print(f"[hrow]   gain alpha^2 |DH v_j|^2 / sigma_j^2 for alpha = {alpha}: {(alpha**2 * DH**2 / cond['sig_small']**2)}", flush=True)
# for reference: a direction that changes c_l by 1e-3 along v_j costs residual sigma_j * 1e-3/|dc_l/dv_j|
with np.errstate(divide='ignore'):
    print(f"[hrow]   residual cost of dc_l = 1e-3 along v_j: {cond['sig_small'] * 1e-3 / np.abs(cond['dcl_dv'])} (|F|_2 = {F.norm().item():.2e}); with the H row: {np.sqrt(cond['sig_small']**2 + alpha**2 * DH**2) * 1e-3 / np.abs(cond['dcl_dv'])}", flush=True)
v_cl = torch.tensor(cond['v_cl'], device=dev); DHc = (hr['grad'] @ v_cl).item()
print(f"[hrow] cheapest c_l direction: cost per unit c_l {cond['cost_cl']:.3e} (c_l change of 1e-3 costs {cond['cost_cl']*1e-3:.2e} vs |F|_2 {F.norm().item():.2e}); dH/dc_l along it = {DHc:+.4e}; with the row (alpha {alpha}) the cost per unit c_l becomes {math.sqrt(cond['cost_cl']**2 + (alpha*DHc)**2):.3e}", flush=True)
del J, Rf
if alpha == 0.0:
    print('[hrow] alpha = 0: diagnostic only', flush=True); sys.exit(0)
# step 2
ls.extra_rows = [('h', alpha)]
t0 = time.time()
log = open(base + f'runs/hlsq_{tag}.dat', 'w')
b1, cl1, info = ls.solve(b, cl, maxit=maxit, lam=1e-6, log=log, rel_stop=1e-7); log.close()
hr1 = ipm1lsq.h_row(ls, b1, cl1)
print(f"[hrow] with the row (alpha {alpha}): c_l {cl1:.10f} (was {cl:.10f}; construct1 5.5763219), h(P)-1 {hr1['H']:+.3e}, x* {hr1['x_star']:.8f}, rms (all rows) {info['rms']:.3e}, {len(info['hist'])-1} its, {time.time()-t0:.0f}s", flush=True)
E1 = info['E']; q1 = info['q']; den1 = ls.denominators(b1, cl1, q1); rq = ls.rq.cpu().numpy(); rel = (E1 / den1)
for name, (a_, b_) in {'r<=2': (0, 2), '2-10': (2, 10), '10-100': (10, 100), '>100': (100, np.inf)}.items():
    mk = (rq > a_) & (rq <= b_); v = rel[mk]; print(f"[hrow]   between-node |E|/den {name}: rms {math.sqrt((v**2).mean().item()):.2e} max {v.abs().max().item():.2e}", flush=True)
Xq = ls.rq[:, None] * ls.cq[None, :]; Yq = ls.rq[:, None] * ls.sq[None, :]; dP = torch.sqrt((Xq - hr1['x_star']) ** 2 + Yq ** 2)
for dd in [0.5, 1.0, 2.0]:
    mk = dP < dd; print(f"[hrow]   |X-P| < {dd}: rms {math.sqrt((rel[mk]**2).mean().item()):.2e} max {rel[mk].abs().max().item():.2e}", flush=True)
if 'sig_small' in info: print(f"[hrow] conditioning with the row: sigma_small {info['sig_small']}, dc_l/dv {info['dcl_dv']}", flush=True)
np.savez(base + f'runs/hlsq_{tag}.npz', b=b1.cpu().numpy(), cl=cl1, gamma=m.gamma, N=m.N, M=m.M, L=m.L, R=float(d['R']), disk=True, eps=1.0, x_star=hr1['x_star'], lsq=True, Qr=Qr, Qth=Qth, hrow_alpha=alpha,
         cluster=d['cluster'] if 'cluster' in d.files else np.array([]), pmap=float(d['pmap']) if 'pmap' in d.files else 1.0)
check_fd.check(base + f'runs/hlsq_{tag}.npz', K=3000, rmin=1e-3, rmax=float(d['R']) * 0.98, hrel=1e-5, device=dev)
print(f"[hrow] saved runs/hlsq_{tag}.npz", flush=True)
