"""Shooting / Picard solver based on characteristics (SPEC Lemma 4).
Inner map at fixed (c_l, C):  rho_{k+1} = (1-theta) rho_k + theta * C eta_P^delta[c_l X + U[rho_k]]  (on the spectral grid, via b).
Outer residuals: F1 = 3 c_l - 1 - c[rho],  F2 = h(P) - 1.  Mode 'inner': just iterate at fixed (c_l, C) and log.
"""
import sys, time, argparse, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1, solve, charac, diag
ap = argparse.ArgumentParser()
ap.add_argument('--start', type=str, default='runs/fixcl_3.0.npz'); ap.add_argument('--cl', type=float, default=None)
ap.add_argument('--C', type=float, default=None); ap.add_argument('--theta', type=float, default=1.0)
ap.add_argument('--iters', type=int, default=10); ap.add_argument('--dt', type=float, default=0.01); ap.add_argument('--delta', type=float, default=1e-6)
ap.add_argument('--tag', type=str, default='shoot'); ap.add_argument('--mode', type=str, default='inner')
ap.add_argument('--normalize', type=int, default=1)   # 1: C from a(0)=1 each step; 0: fixed C
args = ap.parse_args()
dev = 'cuda'
base = ''
m, b, cl_file, d = diag.load(base + args.start, device=dev)
cl = args.cl if args.cl is not None else cl_file
log = open(base + f'runs/{args.tag}.dat', 'w'); log.write("# it cl c identity x* mu1 h(P) C a0 max|b| min_b diff\n")
C = args.C
r = m.rad.rR[:, None]; cos = m.ang.cos[None, :]; sin = m.ang.sin[None, :]
for it in range(args.iters):
    t0 = time.time()
    out = charac.picard_step(m, b, cl=cl, dt=args.dt, delta=args.delta, verbose=False, C=(None if args.normalize else C))
    if out is None:
        print("no stagnation point found; stop"); break
    bnew, _, info = out
    C = info['C']
    Pi = info['P']
    diff = (bnew - b).abs().max().item() / max(1.0, b.abs().max().item())
    msg = (f"it {it:3d}: c_l={cl:.8f} c={info['c']:.6f} ident={3*cl-1-info['c']:+.4e} x*={Pi['x_star']:.6f} mu1={Pi['mu1']:.5f} (2cl-1={2*cl-1:.4f}) "
           f"h(P)={Pi['h']:.6f} C={C:.5g} a0={info['a0_vals'][0]:.6f} a0ratio={info['a0_vals'][-1]/info['a0_vals'][0]:.4f} max|b'|={bnew.abs().max().item():.4g} min b'={bnew[1:].min().item():.4g} rel.change={diff:.3e} ok={info['ok'][1:].float().mean().item():.4f} ({time.time()-t0:.0f}s)")
    print(msg, flush=True)
    log.write(f"{it} {cl:.10f} {info['c']:.8f} {3*cl-1-info['c']:.6e} {Pi['x_star']:.8f} {Pi['mu1']:.6f} {Pi['h']:.8f} {C:.8e} {info['a0_vals'][0]:.6f} {bnew.abs().max().item():.6e} {bnew[1:].min().item():.6e} {diff:.6e}\n"); log.flush()
    b = (1 - args.theta) * b + args.theta * bnew
    if args.mode == 'identity':
        cl = (1 + info['c']) / 3
    np.savez(base + f'runs/{args.tag}_last.npz', b=b.cpu().numpy(), cl=cl, gamma=m.gamma, N=m.N, M=m.M, L=m.L, p=m.p, C=C)
