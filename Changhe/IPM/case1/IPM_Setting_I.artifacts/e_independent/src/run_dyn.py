"""Dynamic rescaling in pseudo-time:  b_tau = -E[b, c_l(tau)],  c_l = (1 + c[b])/3  (keeps a(0)=1 exactly).
Implicit Euler on the full system (b, c_l): (I/dt + J) dz = -F  with the identity row kept as an algebraic constraint."""
import sys, time, argparse, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1, solve
ap = argparse.ArgumentParser()
ap.add_argument('--N', type=int, default=48); ap.add_argument('--M', type=int, default=10)
ap.add_argument('--L', type=float, default=1.0); ap.add_argument('--cl0', type=float, default=2.0)
ap.add_argument('--dt', type=float, default=0.05); ap.add_argument('--nsteps', type=int, default=400)
ap.add_argument('--tag', type=str, default='dyn'); ap.add_argument('--regamma', type=int, default=0)
args = ap.parse_args()
dev = 'cuda' if torch.cuda.is_available() else 'cpu'
cl = args.cl0; gamma = 1 / cl
m = ipm1.IPM1(N=args.N, M=args.M, L=args.L, gamma=gamma, device=dev)
nw = solve.Newton(m, verbose=False)
b = torch.ones(args.N + 1, args.M, device=dev)
n = nw.n
# initial c_l from the identity
F, fl = nw.residual_full(b, cl); cl = (1 + m.psi_xy0(fl).item()) / 3
log = open(f'{args.tag}.dat', 'w')
log.write("# tau cl |E|inf max|b| b(inf)max min_b\n")
tau = 0.0; dt = args.dt
for step in range(args.nsteps):
    F, fl = nw.residual_full(b, cl)
    E = F[:n]
    J = nw.jacobian(b, cl, fl)
    # implicit Euler for b rows (not for normalisation rows, not for identity row)
    A = J.clone()
    idx = torch.arange(args.M, n, device=dev)
    A[idx, idx] += 1.0 / dt
    dz = torch.linalg.solve(A, -F)
    b = b + dz[:n].reshape(args.N + 1, args.M); cl = cl + dz[n].item()
    tau += dt
    Fn, fln = nw.residual_full(b, cl)
    En = Fn[:n].abs().max().item()
    binf = (m.rad.ext1_R @ b)
    msg = f"tau={tau:8.3f} c_l={cl:.8f} |E|={En:.3e} max|b|={b.abs().max().item():.4g} b(inf)={binf.min().item():.4g}..{binf.max().item():.4g} min b={b.min().item():.4g}"
    if step % 10 == 0 or step == args.nsteps - 1:
        print(msg, flush=True)
    log.write(f"{tau:.4f} {cl:.10f} {En:.6e} {b.abs().max().item():.6e} {binf.abs().max().item():.6e} {b.min().item():.6e}\n"); log.flush()
    if not np.isfinite(En) or b.abs().max().item() > 1e8:
        print("diverged"); break
np.savez(f'{args.tag}_end.npz', b=b.cpu().numpy(), cl=cl, gamma=gamma, N=args.N, M=args.M, L=args.L, p=m.p)
