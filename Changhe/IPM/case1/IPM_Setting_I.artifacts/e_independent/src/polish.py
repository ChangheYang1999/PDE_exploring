"""Longer Levenberg-Marquardt polish of a saved reproduction state (true equations), with periodic reporting; then the
usual exports. Usage: python3 src/polish.py runs/<tag>.npz <iterations> <newtag>"""
import sys, time, math, numpy as np, torch
sys.path.insert(0, 'src')
import diag, solve, charac, export_axis, consistency
dev = 'cuda'; base = ''
path, iters, tag = sys.argv[1], int(sys.argv[2]), sys.argv[3]
m, b, cl, d = diag.load(path, device=dev); m.k_tail = 1 / cl
nw = solve.Newton(m, verbose=False, chunk=1024)
t0 = time.time()
b1, cl1, info = solve.levenberg_marquardt_reduced(nw, b, cl, lam=1e-6, maxit=iters, tol=1e-12, verbose=True, every=20)
F1, fl1 = nw.residual_full(b1, cl1); E1 = m.residual(b1, cl1, fl1)
print(f"[polish] after {len(info['hist'])-1} LM iterations ({time.time()-t0:.0f}s): max|E| rows>=1 = {E1[1:].abs().max().item():.3e}, |a(0)-1| = {(b1[0]-1).abs().max().item():.2e}, identity {F1[-1].item():+.2e}, c_l = {cl1:.10f}", flush=True)
fe = charac.FieldEval(m, b1, cl1)
xs = torch.logspace(-3, math.log10(float(d['R']) * 0.9), 4000, device=dev); W1 = fe.axis_W1(xs); idx = torch.where((W1[:-1] < 0) & (W1[1:] >= 0))[0]
a_, b_ = xs[idx[0]].item(), xs[idx[0] + 1].item()
for _ in range(80):
    mid = 0.5 * (a_ + b_)
    if fe.axis_W1(torch.tensor([mid], device=dev))[0].item() < 0: a_ = mid
    else: b_ = mid
xst = 0.5 * (a_ + b_); hx = 1e-6 * xst
mu1 = (fe.axis_W1(torch.tensor([xst + hx], device=dev))[0] - fe.axis_W1(torch.tensor([xst - hx], device=dev))[0]).item() / (2 * hx)
hP = fe.velocity(torch.tensor([xst], device=dev), torch.zeros(1, device=dev))[2][0].item()
Eell, dxr = diag.elliptic_residual(m, b1, fl1); rel = (Eell.abs() / dxr.abs().max())
print(f"[polish] x* = {xst:.8f}, mu1 = {mu1:.8f} (2c_l-1 = {2*cl1-1:.8f}), h(P) - 1 = {hP-1:+.3e}; elliptic residual max {rel.max().item():.2e}; consistency {abs(consistency.c_quadrature(m, b1, cl1) - m.psi_xy0(fl1).item())/m.psi_xy0(fl1).item():.2e}", flush=True)
import scipy.fft
bL = (m.rad.P_RL @ b1).cpu().numpy(); coef = np.abs(scipy.fft.dct(bL[:, m.M // 2], type=1) / m.N)
print(f"[polish] radial coefficients at n = N/4, N/2, 3N/4, N: {coef[[m.N//4, m.N//2, 3*m.N//4, m.N]]}", flush=True)
np.savez(base + f'runs/{tag}.npz', b=b1.cpu().numpy(), cl=cl1, gamma=m.gamma, N=m.N, M=m.M, L=m.L, R=float(d['R']), disk=True, eps=1.0, x_star=xst)
n_ax = 2000; k = np.arange(n_ax); xax = 1.3 * xst * 0.5 * (1 - np.cos(np.pi * (k + 0.5) / n_ax)); xax = xax[xax > 1e-4]
q = export_axis.axis_quantities(m, b1, cl1, torch.tensor(xax, device=dev), hrel=1e-3)
np.savez(base + f'runs/axis_{tag}.npz', cl=cl1, x_star=xst, mu1=mu1, h_P=hP, **q)
with open(base + f'runs/axis_w_{tag}.txt', 'w') as fh:
    fh.write(f"# w = W_1(x,0), disk reproduction {tag}; c_l = {cl1:.12f}; x* = {xst:.12f}\n")
    for xx, ww in zip(q['x'], q['w']): fh.write(f"{xx:.12e} {ww:.12e}\n")
print(f"[polish] exported runs/{tag}.npz, runs/axis_{tag}.npz, runs/axis_w_{tag}.txt", flush=True)
