"""Plain Newton on the TRUE equations from a lead-provided seed in the disk format (then reduced LM if Newton stalls);
reports the floor, the smallest singular values/vectors of the Jacobian, c_l, x*, h(P), residual bands, consistency,
direct D14 coefficients; exports fields and axis data.  Usage: python3 src/seed_newton.py <seed.npz> <tag> [newton_its] [lm_its]"""
import sys, time, math, numpy as np, torch
sys.path.insert(0, 'src')
import ipm1disk, solve, diag, charac, export_axis, consistency
dev = 'cuda'; base = ''
path, tag = sys.argv[1], sys.argv[2]; nit = int(sys.argv[3]) if len(sys.argv) > 3 else 15; lmit = int(sys.argv[4]) if len(sys.argv) > 4 else 100
if path.startswith('project:'):
    # project:N,M,L,R  -> build the seed from construct1 final_candidate.npz exactly as src/reproduce.py does
    N, M, L, R = path[8:].split(','); N, M, L, R = int(N), int(M), float(L), float(R)
    from scipy.interpolate import RegularGridInterpolator
    cand = np.load('final_candidate.npz', allow_pickle=True)
    cl = float(cand['c_l']); rc = cand['r']; thc = cand['theta']; H = cand['H']
    m = ipm1disk.IPM1Disk(N=N, M=M, L=L, R=R, gamma=1 / cl, device=dev); m.k_tail = 1 / cl
    interp = RegularGridInterpolator((np.log(rc), thc), H, method='cubic', bounds_error=False, fill_value=None)
    rR = m.rad.rR.cpu().numpy(); thR = m.ang.theta_np
    pts = np.array([[math.log(max(r, rc[0])), t] for r in rR[1:] for t in thR]); Hg = interp(pts).reshape(N, M)
    b = torch.ones(N + 1, M, device=dev); b[1:] = torch.tensor(np.exp(Hg), device=dev) / m.wR[1:, None]
else:
    d = np.load(path); N, M, L, R = int(d['N']), int(d['M']), float(d['L']), float(d['R']); cl = float(d['cl'])
    m = ipm1disk.IPM1Disk(N=N, M=M, L=L, R=R, gamma=1 / cl, device=dev); m.k_tail = 1 / cl
    b = torch.tensor(d['b'], device=dev); b[0, :] = 1.0
nw = solve.Newton(m, verbose=False, chunk=512)
F0, fl0 = nw.residual_full(b, cl); E0 = m.residual(b, cl, fl0)
rn0, _, _ = diag.residual_norms(m, b, cl, fl0)
print(f"[seed] {path}: N={N} M={M} L={L} R={R} c_l={cl:.10f}; seed residual |F|_inf={F0.abs().max().item():.3e} (equation rows max|E|={E0[1:].abs().max().item():.3e}), identity {F0[-1].item():+.3e}; normalised R bands: " + ", ".join(f"{k}: {v['R_rel_max']:.2e}" for k, v in rn0.items() if isinstance(v, dict)), flush=True)
t0 = time.time()
b1, cl1, info = nw.solve(b, cl, tol=1e-10, maxit=nit)
print(f"[seed] plain Newton: converged={info['converged']} its={len(info['hist'])-1} |F|_inf history={['%.2e' % h for h in info['hist']]} c_l={cl1:.10f} ({time.time()-t0:.0f}s)", flush=True)
if not info['converged']:
    b1, cl1, info = solve.levenberg_marquardt_reduced(nw, b1, cl1, lam=1e-6, maxit=lmit, tol=1e-11, verbose=True, every=10)
    print(f"[seed] reduced LM: |F|_inf floor {info['nrm_inf']:.3e} |F|_2 {info['nrm_2']:.3e} after {len(info['hist'])-1} its, c_l={cl1:.10f} ({time.time()-t0:.0f}s)", flush=True)
F1, fl1 = nw.residual_full(b1, cl1); E1 = m.residual(b1, cl1, fl1)
print(f"[seed] final: max|E| equation rows {E1[1:].abs().max().item():.3e}, identity {F1[-1].item():+.3e}, |a(0)-1| {(b1[0]-1).abs().max().item():.1e}, c_l = {cl1:.10f} (seed {cl:.10f}, diff {cl1-cl:+.3e})", flush=True)
# SVD of the Jacobian (smallest singular values / vectors)
try:
    J = nw.jacobian(b1, cl1, fl1); U_, S_, Vh = torch.linalg.svd(J); rr = m.rad.rR.cpu().numpy()
    print(f"[seed] Jacobian singular values: max {S_[0].item():.3e}, smallest {S_[-4:].cpu().numpy()}", flush=True)
    for k in [1, 2]:
        v = Vh[-k]; vb = v[:-1].reshape(N + 1, M).cpu().numpy(); rad = (vb ** 2).sum(1); ang = (vb ** 2).sum(0); thd = np.degrees(m.ang.theta_np)
        u = U_[:-1, -k].reshape(N + 1, M).cpu().numpy(); radu = (u ** 2).sum(1)
        print(f"[seed]   sv {k}: sigma={S_[-k].item():.2e}, c_l component {v[-1].item():+.3e}; right vector radial energy r<1 {rad[rr<1].sum():.2f}, 1-10 {rad[(rr>=1)&(rr<10)].sum():.2f}, 10-100 {rad[(rr>=10)&(rr<100)].sum():.2f}, >100 {rad[rr>=100].sum():.2f}; angular energy in 79-90 deg {ang[thd>=78.75].sum():.2f}, 0-11 deg {ang[thd<11.25].sum():.2f}; left vector energy at r<0.1 {radu[rr<0.1].sum():.2f}, identity row {U_[-1,-k].item():+.2e}", flush=True)
    del J, U_, Vh
except Exception as ex:
    print("[seed] SVD skipped:", ex, flush=True)
fe = charac.FieldEval(m, b1, cl1)
xs = torch.logspace(-3, math.log10(R * 0.9), 4000, device=dev); W1 = fe.axis_W1(xs); idx = torch.where((W1[:-1] < 0) & (W1[1:] >= 0))[0]
a_, b_ = xs[idx[0]].item(), xs[idx[0] + 1].item()
for _ in range(80):
    mid = 0.5 * (a_ + b_)
    if fe.axis_W1(torch.tensor([mid], device=dev))[0].item() < 0: a_ = mid
    else: b_ = mid
xst = 0.5 * (a_ + b_); hx = 1e-6 * xst
mu1 = (fe.axis_W1(torch.tensor([xst + hx], device=dev))[0] - fe.axis_W1(torch.tensor([xst - hx], device=dev))[0]).item() / (2 * hx)
hP = fe.velocity(torch.tensor([xst], device=dev), torch.zeros(1, device=dev))[2][0].item()
print(f"[seed] P: x* = {xst:.8f}, mu1 = {mu1:.8f} (2c_l-1 = {2*cl1-1:.8f}), h(P) - 1 = {hP-1:+.3e}, zeros of W1 = {len(idx)}", flush=True)
rn, Rr, den = diag.residual_norms(m, b1, cl1, fl1)
print("[seed] normalised transport residual bands (|R|max, max pointwise rel, |R|max/sup denom):", flush=True)
for k, v in rn.items():
    if isinstance(v, dict): print(f"       {k:10s} n={v['n']:5d}  {v['R_abs_max']:.3e}  {v['R_rel_max']:.3e}  {v['R_abs_over_sup']:.3e}", flush=True)
cq = consistency.c_quadrature(m, b1, cl1); cm = m.psi_xy0(fl1).item()
print(f"[seed] far-field consistency: c Green {cm:.8f} vs quadrature {cq:.8f} (rel {abs(cq-cm)/abs(cm):.2e}); min b = {b1[1:].min().item():.4g}", flush=True)
CE = m.ang.to_coef(E1, 'EE').cpu().numpy(); rq = m.rad.rR.cpu().numpy(); sel = slice(1, 7)
pf0 = np.polyfit(rq[sel] ** 2, CE[sel, 0], 1); pf1 = np.polyfit(rq[sel] ** 2, CE[sel, 1], 1)
print(f"[seed] D14 direct from the residual (fit rows r = {rq[1]:.2e}..{rq[6]:.2e}): x^4 y coefficient {pf0[0]+pf1[0]:+.3e}, x^2 y^3 coefficient {pf0[0]-pf1[0]:+.3e}", flush=True)
np.savez(base + f'runs/{tag}.npz', b=b1.cpu().numpy(), cl=cl1, gamma=m.gamma, N=N, M=M, L=L, R=R, disk=True, eps=1.0, x_star=xst)
rho = m.rho_from_b(b1); psi = m.psi(fl1); U1, U2 = m.velocity(fl1); r_ = m.rad.rR; th_ = m.ang.theta
np.savez(base + f'runs/fields_{tag}.npz', r=r_.cpu().numpy(), theta=th_.cpu().numpy(), rho=rho.cpu().numpy(), psi=psi.cpu().numpy(), U1=U1.cpu().numpy(), U2=U2.cpu().numpy(),
         W1=(cl1*r_[:, None]*torch.cos(th_)[None, :] + U1).cpu().numpy(), W2=(cl1*r_[:, None]*torch.sin(th_)[None, :] + U2).cpu().numpy(), c_l=cl1, R=R, k_tail=1/cl1, x_star=xst)
n_ax = 2000; k = np.arange(n_ax); xax = 1.3 * xst * 0.5 * (1 - np.cos(np.pi * (k + 0.5) / n_ax)); xax = xax[xax > 1e-4]
q = export_axis.axis_quantities(m, b1, cl1, torch.tensor(xax, device=dev), hrel=1e-3)
np.savez(base + f'runs/axis_{tag}.npz', cl=cl1, x_star=xst, mu1=mu1, h_P=hP, **q)
with open(base + f'runs/axis_w_{tag}.txt', 'w') as fh:
    fh.write(f"# w = W_1(x,0); {tag}; c_l = {cl1:.12f}; x* = {xst:.12f}\n")
    for xx, ww in zip(q['x'], q['w']): fh.write(f"{xx:.12e} {ww:.12e}\n")
print(f"[seed] exported runs/{tag}.npz, runs/fields_{tag}.npz, runs/axis_{tag}.npz, runs/axis_w_{tag}.txt", flush=True)
