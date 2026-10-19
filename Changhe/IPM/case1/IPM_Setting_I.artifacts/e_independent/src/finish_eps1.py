"""From a homotopy end point near eps = 1 (or any start), solve the TRUE equations (no homotopy) by Newton with the identity
row; optionally first continue in eps from eps_end to 1 (identity-preserving). Saves runs/<tag>.npz and runs analysis."""
import sys, argparse, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1, solve, diag
ap = argparse.ArgumentParser(); ap.add_argument('--start', required=True); ap.add_argument('--tag', required=True)
ap.add_argument('--neps', type=int, default=20); ap.add_argument('--regamma', type=int, default=1)
args = ap.parse_args(); dev = 'cuda'; base = ''
d = np.load(base + args.start)
beta = float(d['beta']) if 'beta' in d else 0.0
m = ipm1.IPM1(N=int(d['N']), M=int(d['M']), L=float(d['L']), gamma=float(d['gamma']), p=float(d['p']), device=dev, beta=beta)
b = torch.tensor(d['b'], device=dev); cl = float(d['cl']); eps0 = float(d['eps']) if 'eps' in d else 1.0
nw = solve.Newton(m, verbose=True)
if eps0 < 1.0 - 1e-9:
    # identity-preserving continuation from eps0 to 1 using the start's own true residual as the homotopy source
    F0, fl0 = nw.residual_full(b, cl); E0 = m.residual(b, cl, fl0); S0 = E0.clone() / (1 - eps0); S0[0, :] = 0
    for eps in np.linspace(eps0, 1.0, args.neps + 1)[1:]:
        b, cl, info = nw.solve(b, cl, hom=(eps, S0, 0.0), tol=1e-11, maxit=40)
        print(f"[finish] eps={eps:.5f} converged={info['converged']} c_l={cl:.10f} |F|={info['nrm']:.2e}", flush=True)
        if not info['converged']:
            break
b, cl, info = nw.solve(b, cl, tol=1e-12, maxit=40)
print(f"[finish] TRUE problem: converged={info['converged']} c_l={cl:.12f} |F|={info['nrm']:.3e} 1/c_l={1/cl:.8f} gamma_grid={m.gamma:.8f}", flush=True)
np.savez(base + f'runs/{args.tag}.npz', b=b.cpu().numpy(), cl=cl, gamma=m.gamma, N=m.N, M=m.M, L=m.L, p=m.p, beta=beta, converged=info['converged'], Finf=info['nrm'])
