"""Independent reproduction of the lead's construct1 candidate with the disk closure (SPEC N3a).
Usage: python3 src/reproduce.py N M R L [tag]
Steps: load final_candidate.npz (H = log a on r[2560] x theta[641]); project onto the disk grid by interpolation in
(log r, theta); b = e^H / w with gamma = 1/c_l; Newton on the TRUE equations with the identity row (c_l free);
diagnostics: c_l, c, x*, mu1, h(P), residual bands (normalised by |rho| + |X.grad rho| + |U.grad rho|), far-field
consistency (Green vs quadrature c), D14 centre coefficients, axis export w(x) on [0, 1.3 x*] (12 digits)."""
import sys, time, math, numpy as np, torch
sys.path.insert(0, 'src')
import ipm1disk, solve, diag, charac, export_axis, consistency
from scipy.interpolate import RegularGridInterpolator
dev = 'cuda'; base = ''
N, M, R, L = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
tag = sys.argv[5] if len(sys.argv) > 5 else f'rep_N{N}M{M}R{int(R)}L{L:g}'
cand = np.load('final_candidate.npz', allow_pickle=True)
cl0 = float(cand['c_l']); rc = cand['r']; thc = cand['theta']; H = cand['H']
gamma = 1.0 / cl0
m = ipm1disk.IPM1Disk(N=N, M=M, L=L, R=R, gamma=gamma, device=dev); m.k_tail = gamma
# interpolate H in (log r, theta): cubic is not available on 2D RegularGrid for scipy 1.13 'cubic' -> use 'cubic' if possible
interp = RegularGridInterpolator((np.log(rc), thc), H, method='cubic', bounds_error=False, fill_value=None)
rR = m.rad.rR.cpu().numpy(); thR = m.ang.theta_np
pts = np.array([[math.log(max(r, rc[0])), t] for r in rR[1:] for t in thR])
Hg = interp(pts).reshape(N, M)
b = torch.ones(N + 1, M, device=dev)
b[1:] = torch.tensor(np.exp(Hg), device=dev) / m.wR[1:, None]
print(f"[rep] grid N={N} M={M} R={R} L={L}: r range of grid {rR[1]:.3g}..{rR[-1]:.3g} (candidate {rc[0]:.3g}..{rc[-1]:.3g}); b range {b.min().item():.3g}..{b.max().item():.3g}", flush=True)
nw = solve.Newton(m, verbose=False, chunk=1024)
F0, fl0 = nw.residual_full(b, cl0)
E0 = m.residual(b, cl0, fl0)
rn0, R0, den0 = diag.residual_norms(m, b, cl0, fl0)
print(f"[rep] initial (projected candidate): |F|_inf={F0.abs().max().item():.3e}, identity residual {F0[-1].item():+.3e}, c={m.psi_xy0(fl0).item():.6f}; normalised transport residual: " + ", ".join(f"{k}: {v['R_rel_max']:.2e}" for k, v in rn0.items() if isinstance(v, dict)), flush=True)
t0 = time.time()
b1, cl1, info = nw.solve(b, cl0, tol=1e-9, maxit=8)
print(f"[rep] Newton: converged={info['converged']} iters={len(info['hist'])-1} |F|={info['nrm']:.3e} history={['%.1e' % h for h in info['hist']]} time {time.time()-t0:.0f}s", flush=True)
if not info['converged']:
    b1, cl1, info = solve.levenberg_marquardt_reduced(nw, b, cl0, lam=1e-4, maxit=int(sys.argv[6]) if len(sys.argv) > 6 else 60, tol=1e-10, verbose=True, every=5)
    print(f"[rep] LM on the true equations: converged={info['converged']} |F|_inf={info['nrm_inf']:.3e} |F|_2={info['nrm_2']:.3e} iterations={len(info['hist'])-1} time {time.time()-t0:.0f}s", flush=True)
    F1, fl1_ = nw.residual_full(b1, cl1); E1 = m.residual(b1, cl1, fl1_)
    print(f"[rep] LM state: normalisation defect max|a(0)-1| = {(b1[0]-1).abs().max().item():.2e} (a tiny spatial rescaling), max|E| over equation rows = {E1[1:].abs().max().item():.3e}, identity row {F1[-1].item():+.2e}", flush=True)
    info['nrm'] = E1[1:].abs().max().item()
print(f"[rep] c_l = {cl1:.10f} (candidate {cl0:.10f}, diff {cl1-cl0:+.3e}); 3c_l-1 = {3*cl1-1:.8f}", flush=True)
# diagnostics
fl1 = m.fields(b1)
fe = charac.FieldEval(m, b1, cl1)
xs = torch.logspace(-3, math.log10(R * 0.9), 4000, device=dev); W1 = fe.axis_W1(xs); idx = torch.where((W1[:-1] < 0) & (W1[1:] >= 0))[0]
if len(idx):
    a_, b_ = xs[idx[0]].item(), xs[idx[0] + 1].item()
    for _ in range(80):
        mid = 0.5 * (a_ + b_)
        if fe.axis_W1(torch.tensor([mid], device=dev))[0].item() < 0: a_ = mid
        else: b_ = mid
    xst = 0.5 * (a_ + b_); hx = 1e-6 * xst
    mu1 = (fe.axis_W1(torch.tensor([xst + hx], device=dev))[0] - fe.axis_W1(torch.tensor([xst - hx], device=dev))[0]).item() / (2 * hx)
    hP = fe.velocity(torch.tensor([xst], device=dev), torch.zeros(1, device=dev))[2][0].item()
    print(f"[rep] P: x* = {xst:.8f} (candidate 8.60088), mu1 = {mu1:.8f} (2c_l-1 = {2*cl1-1:.8f}), h(P) = {hP:.10f} (h-1 = {hP-1:+.2e}), zeros of W1: {len(idx)}", flush=True)
else:
    print("[rep] no stagnation point found", flush=True); xst = float('nan')
rn, Rr, den = diag.residual_norms(m, b1, cl1, fl1)
print("[rep] transport residual bands (|R|max, max pointwise |R|/(|rho|+|X.grad rho|+|U.grad rho|), |R|max/sup denom):")
for k, v in rn.items():
    if isinstance(v, dict): print(f"      {k:10s} n={v['n']:5d}  {v['R_abs_max']:.3e}  {v['R_rel_max']:.3e}  {v['R_abs_over_sup']:.3e}", flush=True)
Eell, dxrho = diag.elliptic_residual(m, b1, fl1)
rr = m.rad.rR
for name, (a_, b_) in {'r<=2': (0, 2), '2<r<=10': (2, 10), '10<r<=100': (10, 100), 'r>100': (100, np.inf)}.items():
    mask = (rr > a_) & (rr <= b_)
    if mask.sum(): print(f"[rep] elliptic residual {name:10s}: |E|max/max|d_x rho| = {(Eell[mask].abs().max()/dxrho[mask].abs().max()).item():.3e}", flush=True)
cq = consistency.c_quadrature(m, b1, cl1); cm = m.psi_xy0(fl1).item()
print(f"[rep] far-field consistency: c Green {cm:.8f} vs quadrature {cq:.8f} (rel {abs(cq-cm)/abs(cm):.2e}); min b = {b1[1:].min().item():.4g}; b(R) max = {(m.rad.ext1_R @ b1).abs().max().item():.3f}", flush=True)
Cb = m.ang.to_coef(b1, 'EE').abs().max(0).values.cpu().numpy(); print(f"[rep] angular coefficient decay (max over r) k=0..M-1: {np.array2string(Cb, precision=2, max_line_width=300)}", flush=True)
# D14: centre Taylor coefficients.  a = w b; a = 1 + delta x^2 + gam y^2 + ...; psi = c xy + alpha x y^3 + beta x^3 y + ...
# radial Taylor of b near 0 from the Radau polynomial: b(r, theta) ~ b0 + r^2 (b20 + b22 cos 2theta); a = (1 + (gamma-3)/2 r^2/L^2 + ...) b
Cb_coef = m.ang.to_coef(b1, 'EE')          # (Nr, M): coefficients of cos(2k theta)
fe0 = charac.FieldEval(m, b1, cl1)
rs = torch.tensor([1e-3, 2e-3, 4e-3], device=dev); t = fe0.t_of_r(rs); P = fe0.radial_interp_matrix(t)
C_at = (P @ Cb_coef).cpu().numpy()        # (3, M)
# fit b_k(r) = b_k0 + b_k2 r^2 for k=0 (constant) and k=1 (cos 2theta)
rs_np = rs.cpu().numpy()
b00 = C_at[:, 0]; b10 = C_at[:, 1]
b20 = np.polyfit(rs_np ** 2, b00, 1)[0]; b22 = np.polyfit(rs_np ** 2, b10, 1)[0]; b0 = np.polyfit(rs_np ** 2, b00, 1)[1]
wq = (gamma - 3) / 2 / L ** 2      # w = 1 + wq r^2 + ...
# a = w b: a = b0 + r^2 (b20 + b0 wq) + r^2 b22 cos 2theta = 1 + delta x^2 + gam y^2 with x^2 = r^2 (1+cos2theta)/2, y^2 = r^2 (1-cos2theta)/2
# delta + gam = 2 (b20 + b0 wq), delta - gam = 2 b22
delta = (b20 + b0 * wq) + b22; gam = (b20 + b0 * wq) - b22
# psi modes: psi_n(r) = r^2 v psi~_n ; near 0: psi_2 ~ (c/2) r^2 + p4 r^4, psi_4 ~ q4 r^4 ; x^3 y = r^4 (2 sin2 + sin4)/8, x y^3 = r^4 (2 sin2 - sin4)/8
# so coefficient of r^4 sin2theta: (beta + alpha)/4 = p4 ; of r^4 sin4theta: (beta - alpha)/8 = q4
PsiC_R = fl1['PsiC_R']       # (Nr, nmodes) psi~_n = psi_n/(r^2 v)
Pc = (P @ PsiC_R).cpu().numpy()
vq = (gamma - 1) / 2 / L ** 2
# psi_n = r^2 (1 + vq r^2) psi~_n -> r^4 coefficient = psi~_n'' /2 term: psi~_n(r) = s0 + s2 r^2 ; psi_n = s0 r^2 + (s2 + s0 vq) r^4
s0_2, s2_2 = np.polyfit(rs_np ** 2, Pc[:, 0], 1)[1], np.polyfit(rs_np ** 2, Pc[:, 0], 1)[0]
s0_4, s2_4 = np.polyfit(rs_np ** 2, Pc[:, 1], 1)[1], np.polyfit(rs_np ** 2, Pc[:, 1], 1)[0]
p4 = s2_2 + s0_2 * vq; q4 = s2_4 + s0_4 * vq
beta = 2 * p4 + 4 * q4; alpha = 2 * p4 - 4 * q4
A = 2 * cl1 - 1
# direct D14 from the residual E on the equation rows (r > 0): E ~ e0 + r^2 (e20 + e22 cos 2theta); R = x^2 y w E
E1 = m.residual(b1, cl1, m.fields(b1)); CE = m.ang.to_coef(E1, 'EE').cpu().numpy(); rq = m.rad.rR.cpu().numpy()
sel = slice(1, 7)
pf0 = np.polyfit(rq[sel] ** 2, CE[sel, 0], 1); pf1 = np.polyfit(rq[sel] ** 2, CE[sel, 1], 1)
print(f"[rep] D14 (direct, from the residual): x^4 y coefficient = {pf0[0] + pf1[0]:+.3e}, x^2 y^3 coefficient = {pf0[0] - pf1[0]:+.3e} (E(0) fit = {pf0[1]:+.2e}; rows r = {rq[1]:.2e}..{rq[6]:.2e})", flush=True)
# (Taylor-based D14 combination removed 21:38Z: the extraction was wrong; the direct residual coefficients above are the D14 numbers)
np.savez(base + f'runs/{tag}.npz', b=b1.cpu().numpy(), cl=cl1, gamma=gamma, N=N, M=M, L=L, R=R, disk=True, eps=1.0, converged=info['converged'], Finf=info['nrm'], x_star=xst)
# axis export on [0, 1.3 x*]
if len(idx):
    n_ax = 2000; k = np.arange(n_ax); xax = 1.3 * xst * 0.5 * (1 - np.cos(np.pi * (k + 0.5) / n_ax)); xax = xax[xax > 1e-4]
    q = export_axis.axis_quantities(m, b1, cl1, torch.tensor(xax, device=dev), hrel=1e-3)
    np.savez(base + f'runs/axis_{tag}.npz', cl=cl1, x_star=xst, mu1=mu1, h_P=hP, **q)
    with open(base + f'runs/axis_w_{tag}.txt', 'w') as fh:
        fh.write(f"# w = W_1(x,0) for the disk reproduction {tag}; c_l = {cl1:.12f}; x* = {xst:.12f}\n")
        for xx, ww in zip(q['x'], q['w']): fh.write(f"{xx:.12e} {ww:.12e}\n")
    print(f"[rep] axis export: runs/axis_{tag}.npz and runs/axis_w_{tag}.txt ({len(xax)} points on (0, 1.3 x*])", flush=True)
