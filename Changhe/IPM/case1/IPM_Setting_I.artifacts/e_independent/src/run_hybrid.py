import sys, time, argparse, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1, solve, hybrid, diag
ap = argparse.ArgumentParser(); ap.add_argument('--N', type=int, default=128); ap.add_argument('--M', type=int, default=32)
ap.add_argument('--Ri', type=float, default=10.0); ap.add_argument('--cl0', type=float, default=3.0); ap.add_argument('--dt', type=float, default=0.01)
ap.add_argument('--tag', type=str, default='hyb'); ap.add_argument('--deps', type=float, default=0.05); ap.add_argument('--start', type=str, default='')
args = ap.parse_args(); dev = 'cuda'; base = ''
cl0 = args.cl0
m = ipm1.IPM1(N=args.N, M=args.M, L=1.0, gamma=1 / cl0, device=dev)
hy = hybrid.Hybrid(m, args.Ri, dt=args.dt)
r = m.rad.rR[:, None]; th = m.ang.theta[None, :]
s2 = r ** 2 / (m.L ** 2 + r ** 2) + 0 * th; one = torch.ones_like(s2)
c1 = m.psi_xy0(m.fields(one)).item(); cs = m.psi_xy0(m.fields(s2)).item()
b0 = one + (3 * cl0 - 1 - c1) / cs * s2; b0[0, :] = 1.0
F0, fl0 = hy.nw.residual_full(b0, cl0); E0 = m.residual(b0, cl0, fl0); S0 = E0.clone(); S0[0, :] = 0; S0[hy.far_idx, :] = 0.0
if args.start:
    m_s, b, cl, d = diag.load(base + args.start, device=dev); eps0 = float(d['eps'])
else:
    b, cl, eps0 = b0.clone(), cl0, 0.0
log = open(base + f'runs/{args.tag}.dat', 'w')
eps = eps0
while True:
    t0 = time.time()
    b_new, cl_new, info = hy.solve(b, cl, S0=S0, eps=eps, tol=1e-9, maxit=25, log=log)
    print(f"[run_hybrid] eps={eps:.4f} converged={info['converged']} |F|={info['nrm']:.3e} c_l={cl_new:.8f} b(inf)max={(m.rad.ext1_R@b_new).abs().max().item():.1f} min b={b_new[1:].min().item():.3g} ({time.time()-t0:.0f}s)", flush=True)
    if not info['converged']:
        print("[run_hybrid] stop", flush=True); break
    b, cl = b_new, cl_new
    np.savez(base + f'runs/{args.tag}_eps{eps:.3f}.npz', b=b.cpu().numpy(), cl=cl, eps=eps, gamma=m.gamma, N=m.N, M=m.M, L=m.L, p=m.p, beta=0.0, Ri=args.Ri)
    if eps >= 1.0 - 1e-12: break
    eps = min(1.0, eps + args.deps)
