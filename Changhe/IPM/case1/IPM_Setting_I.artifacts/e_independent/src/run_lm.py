import sys, time, argparse, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1, solve, diag
ap = argparse.ArgumentParser()
ap.add_argument('--start', type=str, default='')          # npz file, or 'hom2' for b0=1+A s2
ap.add_argument('--cl0', type=float, default=3.0); ap.add_argument('--N', type=int, default=48); ap.add_argument('--M', type=int, default=10)
ap.add_argument('--L', type=float, default=1.0); ap.add_argument('--maxit', type=int, default=300); ap.add_argument('--tag', type=str, default='lm')
ap.add_argument('--fixcl', type=int, default=0); ap.add_argument('--regamma', type=int, default=1)
args = ap.parse_args()
dev = 'cuda'
if args.start and args.start != 'hom2':
    m, b, cl, d = diag.load(args.start, device=dev)
else:
    cl = args.cl0; gamma = 1 / cl
    m = ipm1.IPM1(N=args.N, M=args.M, L=args.L, gamma=gamma, device=dev)
    r = m.rad.rR[:, None]; th = m.ang.theta[None, :]
    s2 = r ** 2 / (m.L ** 2 + r ** 2) + 0 * th; one = torch.ones_like(s2)
    c1 = m.psi_xy0(m.fields(one)).item(); cs = m.psi_xy0(m.fields(s2)).item()
    b = one + (3 * cl - 1 - c1) / cs * s2
nw = solve.Newton(m, verbose=False)
log = open(f'{args.tag}.dat', 'w')
t0 = time.time()
for rnd in range(3 if args.regamma else 1):
    b, cl, info = solve.levenberg_marquardt(nw, b, cl, lam=1e-2, maxit=args.maxit, log=log, fix_cl=bool(args.fixcl))
    print(f"[round {rnd}] gamma={m.gamma:.6f} c_l={cl:.8f} 1/c_l={1/cl:.6f} |F|_inf={info['nrm_inf']:.3e} |F|_2={info['nrm_2']:.3e} time={time.time()-t0:.0f}s", flush=True)
    F, flds = nw.residual_full(b, cl)
    E = F[:-1].reshape(m.N + 1, m.M)
    i, j = np.unravel_index(E.abs().argmax().item(), E.shape)
    print(f"    residual peak at r={m.rad.rR[i].item():.4g} theta={m.ang.theta_np[j]:.3f}; identity row {F[-1].item():+.3e}; c={m.psi_xy0(flds).item():.6f}", flush=True)
    np.savez(f'{args.tag}_r{rnd}.npz', b=b.cpu().numpy(), cl=cl, gamma=m.gamma, N=m.N, M=m.M, L=m.L, p=m.p, Finf=info['nrm_inf'])
    if info['converged'] or not args.regamma or abs(1 / cl - m.gamma) < 1e-8:
        break
    # re-freeze gamma = 1/c_l: interpolate b to the new grid (same t nodes, different r) by keeping values at t nodes (b smooth in t)
    m = ipm1.IPM1(N=m.N, M=m.M, L=m.L, gamma=1 / cl, device=dev); nw = solve.Newton(m, verbose=False)
