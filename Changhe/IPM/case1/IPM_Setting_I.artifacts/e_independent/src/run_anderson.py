import sys, argparse, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1, charac, diag, shootmap
ap = argparse.ArgumentParser()
ap.add_argument('--cl', type=float, required=True); ap.add_argument('--start', type=str, default='')
ap.add_argument('--N', type=int, default=48); ap.add_argument('--M', type=int, default=10); ap.add_argument('--L', type=float, default=1.0)
ap.add_argument('--iters', type=int, default=30); ap.add_argument('--beta', type=float, default=0.5); ap.add_argument('--mem', type=int, default=6)
ap.add_argument('--dt', type=float, default=0.01); ap.add_argument('--tag', type=str, default='and')
args = ap.parse_args()
dev = 'cuda'; base = ''
cl = args.cl; m = ipm1.IPM1(N=args.N, M=args.M, L=args.L, gamma=1/cl, device=dev)
r = m.rad.rR[:, None]; cos = m.ang.cos[None, :]
if args.start:
    m0, b, cl0, d0 = diag.load(base + args.start, device=dev)
else:
    s2 = r**2/(m.L**2 + r**2) + 0*cos; b = 1 + 10*s2
c = m.psi_xy0(m.fields(b)).item(); b = b * ((3*cl - 1)/c)
# fix a(0)=1 by the spectral normalisation trick: rescale space approximately by evaluating b at r/L: skip, just set row 0 to 1
b[0, :] = 1.0
log = open(base + f'runs/{args.tag}.dat', 'w')
b, ok = shootmap.anderson(m, b, cl, iters=args.iters, mem=args.mem, beta=args.beta, dt=args.dt, log=log)
np.savez(base + f'runs/{args.tag}_last.npz', b=b.cpu().numpy(), cl=cl, gamma=m.gamma, N=m.N, M=m.M, L=m.L, p=m.p, ok=ok)
print("converged:", ok)
