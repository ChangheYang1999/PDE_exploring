import sys, time, argparse, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1, solve
ap = argparse.ArgumentParser()
ap.add_argument('--N', type=int, default=48); ap.add_argument('--M', type=int, default=10)
ap.add_argument('--L', type=float, default=1.0); ap.add_argument('--cl0', type=float, default=2.5)
ap.add_argument('--ds', type=float, default=0.05); ap.add_argument('--nsteps', type=int, default=300)
ap.add_argument('--amp_stop', type=float, default=1e5); ap.add_argument('--tag', type=str, default='arc')
args = ap.parse_args()
dev = 'cuda' if torch.cuda.is_available() else 'cpu'
cl0 = args.cl0; gamma = 1 / cl0
m = ipm1.IPM1(N=args.N, M=args.M, L=args.L, gamma=gamma, device=dev)
nw = solve.Newton(m, verbose=False)
b0 = torch.ones(args.N + 1, args.M, device=dev)
F0, fl0 = nw.residual_full(b0, cl0)
S0 = m.residual(b0, cl0, fl0); S0[0, :] = 0
s0 = (3 * cl0 - 1 - m.psi_xy0(fl0)).item()
log = open(f'{args.tag}.dat', 'w')
log.write("# eps cl max|b| b(inf)max smin ds tau_eps\n")
out, (b, cl, eps) = solve.arclength(nw, b0, cl0, 0.0, S0, s0, ds=args.ds, nsteps=args.nsteps, amp_stop=args.amp_stop, log=log)
np.savez(f'{args.tag}_end.npz', b=b.cpu().numpy(), cl=cl, eps=eps, gamma=gamma, N=args.N, M=args.M, L=args.L, p=m.p)
print("final eps", eps, "cl", cl)
