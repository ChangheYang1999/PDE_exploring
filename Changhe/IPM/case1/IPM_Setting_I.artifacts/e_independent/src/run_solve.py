"""First real solves: homotopy from b0 = 1 (a = w), c_l0, to the true equation, outer loop on gamma = 1/c_l."""
import sys, time, argparse, json, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1, solve

ap = argparse.ArgumentParser()
ap.add_argument('--N', type=int, default=64); ap.add_argument('--M', type=int, default=12)
ap.add_argument('--L', type=float, default=1.0); ap.add_argument('--cl0', type=float, default=1.5)
ap.add_argument('--neps', type=int, default=10); ap.add_argument('--outer', type=int, default=6)
ap.add_argument('--tag', type=str, default='first'); ap.add_argument('--init', type=str, default='')
ap.add_argument('--p', type=float, default=None)
args = ap.parse_args()
dev = 'cuda' if torch.cuda.is_available() else 'cpu'
t_start = time.time()
cl = args.cl0
b = None
for outer in range(args.outer):
    gamma = 1.0 / cl
    m = ipm1.IPM1(N=args.N, M=args.M, L=args.L, gamma=gamma, p=args.p, device=dev)
    nw = solve.Newton(m, verbose=False)
    if b is None:
        if args.init:
            d = np.load(args.init)
            # interpolate previous b (possibly different grid) onto this grid in (t, theta): use polynomial interp in t and exact in theta if same M
            bprev = torch.tensor(d['b'], device=dev)
            if bprev.shape == (args.N + 1, args.M):
                b = bprev
            else:
                raise SystemExit("init grid mismatch")
        else:
            b = torch.ones(args.N + 1, args.M, device=dev)
        eps_list = np.linspace(0, 1, args.neps + 1)[1:]
        b, cl, res, ok = solve.continuation(nw, b, cl, eps_list, tol=1e-11, maxit=40)
        print(f"[outer {outer}] gamma={gamma:.6f} continuation ok={ok} c_l={cl:.10f}", flush=True)
        if not ok:
            print("continuation failed; results:", res)
            break
    else:
        b, cl, info = nw.solve(b, cl, tol=1e-12, maxit=40)
        print(f"[outer {outer}] gamma={gamma:.6f} newton converged={info['converged']} c_l={cl:.10f} |F|={info['nrm']:.2e} its={len(info['hist'])-1}", flush=True)
    F, flds = nw.residual_full(b, cl)
    c = m.psi_xy0(flds).item()
    print(f"    identity: 3c_l-1 = {3*cl-1:.10f}, c = psi_xy(0) = {c:.10f}, 1/c_l = {1/cl:.6f} vs gamma {gamma:.6f};  b(inf) range "
          f"{(m.rad.ext1_R @ b).min().item():.4f}..{(m.rad.ext1_R @ b).max().item():.4f};  max|b| {b.abs().max().item():.3f}", flush=True)
    if abs(1.0 / cl - gamma) < 1e-10:
        break
np.savez(f'{args.tag}.npz', b=b.cpu().numpy(), cl=cl, gamma=1.0/cl, N=args.N, M=args.M, L=args.L, p=m.p)
print(f"saved runs/{args.tag}.npz  total {time.time()-t_start:.1f}s")
