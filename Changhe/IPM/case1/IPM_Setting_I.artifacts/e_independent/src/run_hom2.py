"""Identity-preserving homotopy: start b0 = 1 + A s2(r) with A such that c_l0 = (1 + c[b0])/3; E rows perturbed only."""
import sys, time, argparse, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1, solve
ap = argparse.ArgumentParser()
ap.add_argument('--N', type=int, default=48); ap.add_argument('--M', type=int, default=10)
ap.add_argument('--L', type=float, default=1.0); ap.add_argument('--cl0', type=float, default=2.0)
ap.add_argument('--neps', type=int, default=80); ap.add_argument('--tag', type=str, default='hom2')
ap.add_argument('--arc', type=int, default=1); ap.add_argument('--shape', type=str, default='s2')
args = ap.parse_args()
dev = 'cuda'
cl0 = args.cl0; gamma = 1 / cl0
m = ipm1.IPM1(N=args.N, M=args.M, L=args.L, gamma=gamma, device=dev)
nw = solve.Newton(m, verbose=False)
r = m.rad.rR[:, None]; th = m.ang.theta[None, :]
s2 = r ** 2 / (m.L ** 2 + r ** 2) + 0 * th
shape = {'s2': s2, 's2cos': s2 * (1 + torch.cos(2 * th)) / 2, 's2sin': s2 * (1 - torch.cos(2 * th)) / 2, 's1': (r / (m.L + r)) + 0 * th}[args.shape]
one = torch.ones_like(s2)
c1 = m.psi_xy0(m.fields(one)).item(); cs = m.psi_xy0(m.fields(shape)).item()
A = (3 * cl0 - 1 - c1) / cs
b0 = one + A * shape; b0[0, :] = 1.0
F0, fl0 = nw.residual_full(b0, cl0)
print(f"start: c_l0={cl0} gamma={gamma:.4f}  c[1]={c1:.5f} c[shape]={cs:.5f} -> A={A:.4f}; identity residual {F0[-1].item():.2e}; max|E0|={F0[:-1].abs().max().item():.3e}", flush=True)
eps_list = np.linspace(0, 1, args.neps + 1)[1:]
b, cl, res, ok = solve.continuation(nw, b0, cl0, eps_list, tol=1e-10, maxit=30, verbose=True, keep_identity=True)
print(f"natural continuation ok={ok}; reached eps={max([e for (e,c,cv,nr) in res if cv], default=0):.4f}  c_l={cl:.8f}", flush=True)
np.savez(f'{args.tag}_nat.npz', b=b.cpu().numpy(), cl=cl, gamma=gamma, N=args.N, M=args.M, L=args.L, p=m.p, eps=max([e for (e,c,cv,nr) in res if cv], default=0))
if not ok and args.arc:
    E0 = m.residual(b0, cl0, fl0); S0 = E0.clone(); S0[0, :] = 0
    log = open(f'{args.tag}_arc.dat', 'w')
    out, (b, cl, eps) = solve.arclength(nw, b0, cl0, 0.0, S0, 0.0, ds=0.05, nsteps=400, amp_stop=1e5, log=log, verbose=True)
    np.savez(f'{args.tag}_arc_end.npz', b=b.cpu().numpy(), cl=cl, eps=eps, gamma=gamma, N=args.N, M=args.M, L=args.L, p=m.p)
    print("arclength final eps", eps, "cl", cl)
