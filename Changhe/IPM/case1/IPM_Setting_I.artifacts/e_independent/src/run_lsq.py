"""Driver for the oversampled least-squares solver (src/ipm1lsq.py).
Usage: python3 src/run_lsq.py <state.npz | project:N,M,L,R> <tag> [maxit] [oversampling factor, default 2] [chunk]
Steps: load/project the start (construct1 projection as in reproduce.py), LSQ Gauss-Newton/LM with c_l eliminated
(c_l = (1 + c[b])/3 exactly), then diagnostics: c_l, c, x*, mu1, h(P), between-node residual on the quadrature grid (divided
form, pointwise-normalised: rms/max by band), SPEC N4 bands on the Radau grid, random-point finite-difference transport residual
(src/check_fd.py), Green-vs-quadrature consistency of c, D14 direct, min b, singular values of the weighted Jacobian;
exports runs/lsq_<tag>.npz (state), runs/fields_lsq_<tag>.npz (plain arrays), runs/axis_lsq_<tag>.npz + axis_w_lsq_<tag>.txt."""
import sys, time, math, numpy as np, torch
sys.path.insert(0, 'src')
import ipm1disk, ipm1lsq, diag, charac, export_axis, consistency, check_fd
dev = 'cuda'; base = ''
path, tag = sys.argv[1], sys.argv[2]
maxit = int(sys.argv[3]) if len(sys.argv) > 3 else 20
ovs = float(sys.argv[4]) if len(sys.argv) > 4 else 2.0
chunk = int(sys.argv[5]) if len(sys.argv) > 5 else 256
rel_stop = float(sys.argv[6]) if len(sys.argv) > 6 else 1e-4
cluster = None; pmap = 1.0; qth_fac = 2.0
for arg in sys.argv[7:]:
    if arg.startswith('cluster:'):     # cluster:r_c,w,alpha  (radial points 1/(1-alpha) times denser near r_c)
        rc_, w_, al_ = [float(v) for v in arg[8:].split(',')]
    if arg.startswith('p:'):           # map exponent r = L(1+t)/(1-t+a)^p
        pmap = float(arg[2:])
    if arg.startswith('qth:'):         # angular oversampling factor: Qth = round(F M) + 1 (default 2M + 1)
        qth_fac = float(arg[4:])
has_cluster = any(a.startswith('cluster:') for a in sys.argv[7:])
t_start = time.time()
if path.startswith('project:'):
    N, M, L, R = path[8:].split(','); N, M, L, R = int(N), int(M), float(L), float(R)
    from scipy.interpolate import RegularGridInterpolator
    cand = np.load('final_candidate.npz', allow_pickle=True)
    cl = float(cand['c_l']); rc = cand['r']; thc = cand['theta']; H = cand['H']
    if has_cluster: cluster = ipm1disk.RadialDisk.s_for_r(L, R, rc_, w_, al_, p=pmap)
    m = ipm1disk.IPM1Disk(N=N, M=M, L=L, R=R, gamma=1 / cl, device=dev, cluster=cluster, p=pmap); m.k_tail = 1 / cl
    interp = RegularGridInterpolator((np.log(rc), thc), H, method='cubic', bounds_error=False, fill_value=None)
    rR = m.rad.rR.cpu().numpy(); thR = m.ang.theta_np
    pts = np.array([[math.log(max(r, rc[0])), t] for r in rR[1:] for t in thR]); Hg = interp(pts).reshape(N, M)
    b = torch.ones(N + 1, M, device=dev); b[1:] = torch.tensor(np.exp(Hg), device=dev) / m.wR[1:, None]
    src = 'projection of construct1 final_candidate'
else:
    d = np.load(path); N, M, L, R = int(d['N']), int(d['M']), float(d['L']), float(d['R']); cl = float(d['cl'])
    cluster = tuple(d['cluster']) if 'cluster' in d.files and d['cluster'].size == 3 else None
    pmap = float(d['pmap']) if 'pmap' in d.files else 1.0
    gamma_saved = float(d['gamma'])      # the frozen weight exponent of the saved state (rho = x^2 y w_gamma b): must be reused
    m = ipm1disk.IPM1Disk(N=N, M=M, L=L, R=R, gamma=gamma_saved, device=dev, cluster=cluster, p=pmap); m.k_tail = 1 / cl
    b = torch.tensor(d['b'], device=dev); b[0, :] = 1.0; src = path + f' (gamma {gamma_saved:.8f})'
Qr, Qth = int(round(ovs * N)), int(round(qth_fac * M)) + 1
print(f"[lsq] cluster (s_P, w, alpha) = {cluster}; map exponent p = {pmap}", flush=True)
print(f"[lsq] start: {src}; grid N={N} M={M} L={L} R={R}; quadrature grid {Qr} x {Qth} ({Qr*Qth} rows, {N*M} unknowns); start c_l {cl:.10f}", flush=True)
ls = ipm1lsq.LSQ(m, Qr=Qr, Qth=Qth, chunk=chunk, verbose=True)
cl0, c0, fl0 = ls.cl_of_b(b, cl)
E0, q0 = ls.set_weights(b, cl0)
F0 = E0.reshape(-1) * ls.wrow
rq = ls.rq.cpu().numpy()
def bands(vals2d, rq):
    out = []
    for name, (a_, b_) in {'r<=2': (0, 2), '2-10': (2, 10), '10-100': (10, 100), '>100': (100, np.inf)}.items():
        mask = (rq > a_) & (rq <= b_)
        if mask.sum():
            v = vals2d[mask]; out.append(f"{name} rms {math.sqrt((v**2).mean().item()):.2e} max {v.abs().max().item():.2e}")
    return "; ".join(out)
print(f"[lsq] start state: self-consistent c_l {cl0:.10f} (c = {c0:.8f}); between-node normalised residual by band: {bands((E0 / ls.denominators(b, cl0, q0)), rq)}", flush=True)
log = open(base + f'runs/lsq_{tag}.dat', 'w')
b1, cl1, info = ls.solve(b, cl0, maxit=maxit, lam=1e-6, log=log, rel_stop=rel_stop)
log.close()
print(f"[lsq] done: {len(info['hist'])-1} iterations, rms {info['rms']:.3e}, max {info['max']:.3e}, c_l = {cl1:.10f} (construct1 5.5763219; diff {cl1-5.5763219:+.3e}); time {time.time()-t_start:.0f}s", flush=True)
E1, q1 = info['E'], info['q']
den1 = ls.denominators(b1, cl1, q1)
print(f"[lsq] between-node normalised residual |E|/den by band (quadrature grid): {bands(E1 / den1, rq)}", flush=True)
# where is the max?
iq = (E1 / den1).abs().argmax().item(); ir, it_ = divmod(iq, ls.Qth)
print(f"[lsq]   max at r = {rq[ir]:.4g}, theta = {math.degrees(ls.thq[it_].item()):.2f} deg", flush=True)
# near P band
if 'sig_min' in info: print(f"[lsq] weighted Jacobian (QR): sigma_max {info['sig_max']:.3e}, smallest singular values {info['sig_small']}; dc_l per unit norm along them {info['dcl_dv']}; u_j.F {info['uF']}", flush=True)
# ---- standard diagnostics on the Radau grid
m.k_tail = 1 / cl1; fl1 = m.fields(b1)
fe = charac.FieldEval(m, b1, cl1)
xs = torch.logspace(-3, math.log10(R * 0.9), 4000, device=dev); W1 = fe.axis_W1(xs); idx = torch.where((W1[:-1] < 0) & (W1[1:] >= 0))[0]
xst = float('nan'); mu1 = float('nan'); hP = float('nan')
if len(idx):
    a_, b_ = xs[idx[0]].item(), xs[idx[0] + 1].item()
    for _ in range(80):
        mid = 0.5 * (a_ + b_)
        if fe.axis_W1(torch.tensor([mid], device=dev))[0].item() < 0: a_ = mid
        else: b_ = mid
    xst = 0.5 * (a_ + b_); hx = 1e-6 * xst
    mu1 = (fe.axis_W1(torch.tensor([xst + hx], device=dev))[0] - fe.axis_W1(torch.tensor([xst - hx], device=dev))[0]).item() / (2 * hx)
    hP = fe.velocity(torch.tensor([xst], device=dev), torch.zeros(1, device=dev))[2][0].item()
    print(f"[lsq] P: x* = {xst:.8f} (construct1 8.60088), mu1 = {mu1:.8f} (2c_l-1 = {2*cl1-1:.8f}), h(P) - 1 = {hP-1:+.3e}, zeros of W1 = {len(idx)}", flush=True)
    # near-P between-node residual: quadrature points with |X - P| < 1
    Xq = ls.rq[:, None] * ls.cq[None, :]; Yq = ls.rq[:, None] * ls.sq[None, :]
    dP = torch.sqrt((Xq - xst) ** 2 + Yq ** 2)
    for dd in [0.5, 1.0, 2.0]:
        mk = dP < dd
        if mk.sum(): print(f"[lsq]   |X-P| < {dd}: {int(mk.sum())} quadrature points, |E|/den rms {math.sqrt(((E1/den1)[mk]**2).mean().item()):.2e} max {(E1/den1)[mk].abs().max().item():.2e}", flush=True)
rn, Rr, den = diag.residual_norms(m, b1, cl1, fl1)
print("[lsq] SPEC N4 bands on the Radau grid (|R|max, max pointwise |R|/(|rho|+|X.grad rho|+|U.grad rho|), |R|max/sup denom):", flush=True)
for k, v in rn.items():
    if isinstance(v, dict): print(f"       {k:10s} n={v['n']:5d}  {v['R_abs_max']:.3e}  {v['R_rel_max']:.3e}  {v['R_abs_over_sup']:.3e}", flush=True)
Eell, dxrho = diag.elliptic_residual(m, b1, fl1); rr = m.rad.rR
for name, (a_, b_) in {'r<=2': (0, 2), '2<r<=10': (2, 10), '10<r<=100': (10, 100), 'r>100': (100, np.inf)}.items():
    mask = (rr > a_) & (rr <= b_)
    if mask.sum(): print(f"[lsq] elliptic residual {name:10s}: |E|max/max|d_x rho| = {(Eell[mask].abs().max()/dxrho[mask].abs().max()).item():.3e}", flush=True)
cq = consistency.c_quadrature(m, b1, cl1); cm = m.psi_xy0(fl1).item()
print(f"[lsq] identity: 3c_l - 1 - c = {3*cl1-1-cm:+.2e}; far-field consistency: c Green {cm:.8f} vs quadrature {cq:.8f} (rel {abs(cq-cm)/abs(cm):.2e}); min b = {b1[1:].min().item():.4g}; b(R) max = {(m.rad.ext1_R @ b1).abs().max().item():.3f}", flush=True)
Cb = m.ang.to_coef(b1, 'EE').abs().max(0).values.cpu().numpy(); print(f"[lsq] angular coefficient decay (max over r), k = 0, M/4, M/2, 3M/4, M-1: {Cb[[0, M//4, M//2, 3*M//4, M-1]]}", flush=True)
import scipy.fft
bL = (m.rad.P_RL @ b1).cpu().numpy(); coef = np.abs(scipy.fft.dct(bL[:, M // 2], type=1) / N)
print(f"[lsq] radial Chebyshev coefficients (mid angle) at n = 0, N/4, N/2, 3N/4, N: {coef[[0, N//4, N//2, 3*N//4, N]]}", flush=True)
E1c = m.residual(b1, cl1, fl1); CE = m.ang.to_coef(E1c, 'EE').cpu().numpy(); rqq = m.rad.rR.cpu().numpy(); sel = slice(1, 7)
pf0 = np.polyfit(rqq[sel] ** 2, CE[sel, 0], 1); pf1 = np.polyfit(rqq[sel] ** 2, CE[sel, 1], 1)
print(f"[lsq] D14 direct from the residual (rows r = {rqq[1]:.2e}..{rqq[6]:.2e}): x^4 y coefficient {pf0[0]+pf1[0]:+.3e}, x^2 y^3 coefficient {pf0[0]-pf1[0]:+.3e}, E(0) fit {pf0[1]:+.2e}", flush=True)
np.savez(base + f'runs/lsq_{tag}.npz', b=b1.cpu().numpy(), cl=cl1, gamma=m.gamma, N=N, M=M, L=L, R=R, disk=True, eps=1.0, x_star=xst, lsq=True, Qr=Qr, Qth=Qth, rms=info['rms'], maxres=info['max'], cluster=np.array(cluster if cluster is not None else [], dtype=float), pmap=pmap)
rho = m.rho_from_b(b1); psi = m.psi(fl1); U1, U2 = m.velocity(fl1); r_ = m.rad.rR; th_ = m.ang.theta
np.savez(base + f'runs/fields_lsq_{tag}.npz', r=r_.cpu().numpy(), theta=th_.cpu().numpy(), rho=rho.cpu().numpy(), a=(m.wR[:, None] * b1).cpu().numpy(), psi=psi.cpu().numpy(), U1=U1.cpu().numpy(), U2=U2.cpu().numpy(),
         W1=(cl1*r_[:, None]*torch.cos(th_)[None, :] + U1).cpu().numpy(), W2=(cl1*r_[:, None]*torch.sin(th_)[None, :] + U2).cpu().numpy(), c_l=cl1, c=cm, R=R, N=N, M=M, L=L, gamma=m.gamma, k_tail=1/cl1, x_star=xst, cluster=np.array(cluster if cluster is not None else [], dtype=float), pmap=pmap,
         note='disk closure (SPEC N3a), oversampled least squares; grid = Chebyshev-Radau radii x midpoint angles on (0, pi/2); rho = x^2 y a')
# random-point FD transport residual (independent evaluator)
out = check_fd.check(base + f'runs/lsq_{tag}.npz', K=3000, rmin=1e-3, rmax=R * 0.98, hrel=1e-5, device=dev)
if len(idx):
    n_ax = 2000; k = np.arange(n_ax); xax = 1.3 * xst * 0.5 * (1 - np.cos(np.pi * (k + 0.5) / n_ax)); xax = xax[xax > 1e-4]
    q = export_axis.axis_quantities(m, b1, cl1, torch.tensor(xax, device=dev), hrel=1e-3)
    np.savez(base + f'runs/axis_lsq_{tag}.npz', cl=cl1, x_star=xst, mu1=mu1, h_P=hP, **q)
    with open(base + f'runs/axis_w_lsq_{tag}.txt', 'w') as fh:
        fh.write(f"# w = W_1(x,0), disk LSQ {tag}; c_l = {cl1:.12f}; x* = {xst:.12f}\n")
        for xx, ww in zip(q['x'], q['w']): fh.write(f"{xx:.12e} {ww:.12e}\n")
print(f"[lsq] exported runs/lsq_{tag}.npz, runs/fields_lsq_{tag}.npz, runs/axis_lsq_{tag}.npz, runs/axis_w_lsq_{tag}.txt; total time {time.time()-t_start:.0f}s", flush=True)
