"""Natural continuation in eps of the identity-preserving homotopy with Levenberg-Marquardt solves (regularises the
near-free far-field directions). Grids given on the command line; saves the solution at selected eps values."""
import sys, time, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1, solve
dev = 'cuda'; base = ''
cl0 = 3.0
grids = [tuple(int(v) for v in g.split('x')) for g in sys.argv[1].split(',')] if len(sys.argv) > 1 else [(96, 24), (128, 32)]
deps0 = float(sys.argv[2]) if len(sys.argv) > 2 else 0.02
for (N, M) in grids:
    t0 = time.time(); deps = deps0
    m = ipm1.IPM1(N=N, M=M, L=1.0, gamma=1 / cl0, device=dev); nw = solve.Newton(m, verbose=False, chunk=1024)
    r = m.rad.rR[:, None]; th = m.ang.theta[None, :]
    s2 = r ** 2 / (m.L ** 2 + r ** 2) + 0 * th; one = torch.ones_like(s2)
    c1 = m.psi_xy0(m.fields(one)).item(); cs = m.psi_xy0(m.fields(s2)).item()
    b = one + (3 * cl0 - 1 - c1) / cs * s2; b[0, :] = 1.0; cl = cl0
    F0, fl0 = nw.residual_full(b, cl); E0 = m.residual(b, cl, fl0); S0 = E0.clone(); S0[0, :] = 0
    tag = f'lmc_cl3_N{N}M{M}'
    log = open(base + f'runs/{tag}.dat', 'w'); log.write("# eps |F|inf cl b(inf)max min_b iters time\n")
    eps = 0.0; lam = 1e-3
    while eps < 1.0 - 1e-12:
        eps = min(1.0, eps + deps)
        t1 = time.time()
        # Newton first (fast); LM if Newton fails
        bt, clt, info = nw.solve(b, cl, hom=(eps, S0, 0.0), tol=1e-10, maxit=25)
        method = 'newton'
        if not info['converged']:
            bt, clt, info = solve.levenberg_marquardt_hom(nw, b, cl, hom=(eps, S0, 0.0), lam=lam, maxit=150, tol=1e-10, verbose=False)
            method = 'LM'
        ok = info['converged']
        nrm = info.get('nrm_inf', info.get('nrm', float('nan')))
        binf = (m.rad.ext1_R @ bt).abs().max().item()
        msg = f"({N},{M}) eps={eps:.3f} {method:6s} converged={ok} |F|={nrm:.2e} c_l={clt:.8f} b(inf)max={binf:.1f} min b={bt[1:].min().item():.3g} ({time.time()-t1:.0f}s)"
        print(msg, flush=True); log.write(f"{eps:.4f} {nrm:.6e} {clt:.10f} {binf:.6e} {bt[1:].min().item():.6e} {len(info['hist'])} {time.time()-t1:.1f}\n"); log.flush()
        if not ok:
            print(f"({N},{M}): stopped at eps={eps:.3f} (|F|={nrm:.2e}); trying half step", flush=True)
            if deps > 0.0025:
                eps -= deps; deps *= 0.5; continue
            break
        b, cl = bt, clt
        if any(abs(eps - e) < 1e-6 for e in [0.3, 0.4, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]):
            np.savez(base + f'runs/{tag}_eps{eps:.3f}.npz', b=b.cpu().numpy(), cl=cl, eps=eps, gamma=m.gamma, N=N, M=M, L=m.L, p=m.p, beta=0.0)
    np.savez(base + f'runs/{tag}_last.npz', b=b.cpu().numpy(), cl=cl, eps=eps, gamma=m.gamma, N=N, M=M, L=m.L, p=m.p, beta=0.0)
    print(f"({N},{M}) done: final eps={eps:.4f} total {time.time()-t0:.0f}s", flush=True)
