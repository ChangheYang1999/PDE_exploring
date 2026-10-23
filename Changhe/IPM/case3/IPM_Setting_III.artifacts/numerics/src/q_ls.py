"""Driver for the least-squares Q representation (src/ipm3ql.py).
  forced  cl N M gK Lf1,Lf2,... tag           forced continuation in the forcing width Lf (grid L = 1) at fixed c_l, gauge gK
  release start.pt tag [N M]                   unforced release (mu = 0, c_l free, deflated centre row) from a saved forced state,
                                               optionally regridded to N x M
Every converged state is saved as runs/<tag>_Lf<Lf>.pt (forced) or runs/<tag>.pt (release)."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3, ipm3s, ipm3q, ipm3ql
torch.set_default_dtype(torch.float64); dev = 'cuda'
now = lambda: time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def report(q, u, cl, mu, info, label, log):
    beta = q.beta_full(u); flds = info['flds']; c = q.psi_xy0(flds).item(); a0 = beta[0, 0].item()
    K, Lcan = q.K_of_state(beta, cl); og = ipm3ql.between_node(q, beta, cl, flds, mu if mu is not None else 0.0)
    S = info['S']; tail = ipm3ql.cheb_tail(q, u); keep = S >= 1e-13 * S[0]; nnull = int((~keep).sum().item()); smin_eff = S[keep][-1].item()
    m = (f"{label}: |F|max={info['nF']:.1e} |F|2={info['nF2']:.1e} its={info['its']} smin={smin_eff:.1e} (above cutoff; {nnull} invisible directions) smax={S[0].item():.1e} "
         f"cl={cl:.10f} mu={mu if mu is None else f'{mu:+.10f}'} a0={a0:.10f} c={c:+.10f} Delta={cl+c-1:+.3e} K={K:.6f} Lcan={Lcan:.5g} "
         f"cheb-tail(mode0,1)={tail[0]:.1e},{tail[1]:.1e} between-node |R|/Nf=[{og[0]:.1e} {og[1]:.1e} {og[2]:.1e} {og[3]:.1e}]")
    print(m, flush=True); log.write(m + "\n"); log.flush()
    return beta


mode = sys.argv[1]
if mode == 'forced':
    cl = float(sys.argv[2]); N = int(sys.argv[3]); M = int(sys.argv[4]); gK = float(sys.argv[5])
    Lfs = [float(v) for v in sys.argv[6].split(',')]; tag = sys.argv[7]
    Lgrid = float(sys.argv[9]) if len(sys.argv) > 9 else 1.0          # outer map scale (domain test; default 1)
    log = open(f'runs/{tag}.log', 'a'); log.write(f"# q_ls forced cl={cl} {N}x{M} gK={gK} Lfs={Lfs} L={Lgrid} {now()}\n")
    q = ipm3ql.IPM3QL(N=N, M=M, L=Lgrid, gamma=1 / cl, device=dev, Lf=Lfs[0])
    if len(sys.argv) > 8 and sys.argv[8] != '-':
        st = torch.load(sys.argv[8]); qo = ipm3ql.IPM3QL(N=st['N'], M=st['M'], L=st.get('L', 1.0), gamma=1 / cl, device=dev)
        u = q.beta_to_u(ipm3s.regrid_s(qo, st['beta'].to(dev), q)); mu = st['mu']
    else:
        beta0 = torch.zeros(N + 1, M, device=dev); beta0[:, 0] = gK; u = q.beta_to_u(beta0); mu = 0.0
    for Lf in Lfs:
        q.Lf = Lf; t0 = time.time()
        u2, _, mu2, info = q.gn(u, cl, gK, mu=mu, forced=True, maxit=40, log=log)
        beta = report(q, u2, cl, mu2, info, f"QL forced {N}x{M} cl={cl} gK={gK} Lf={Lf} L={Lgrid} ({time.time()-t0:.0f}s)", log)
        torch.save(dict(beta=beta.cpu(), u=u2.cpu(), cl=cl, mu=mu2, gamma=1 / cl, N=N, M=M, L=Lgrid, Lf=Lf, gK=gK, p=q.p, rep='QL'), f'runs/{tag}_Lf{Lf:g}.pt')
        if info['nF'] < 1e-6:
            u, mu = u2, mu2
        else:
            print(f"  not converged at Lf={Lf}; stopping the continuation", flush=True); break
elif mode == 'release':
    start = sys.argv[2]; tag = sys.argv[3]; st = torch.load(start)
    N = int(sys.argv[4]) if len(sys.argv) > 4 else st['N']; M = int(sys.argv[5]) if len(sys.argv) > 5 else st['M']
    cl0 = st['cl']; gK = st['gK']
    log = open(f'runs/{tag}.log', 'a'); log.write(f"# q_ls release from {start} at {N}x{M} {now()}\n")
    qo = ipm3ql.IPM3QL(N=st['N'], M=st['M'], L=1.0, gamma=1 / cl0, device=dev, Lf=st['Lf'])
    q = ipm3ql.IPM3QL(N=N, M=M, L=1.0, gamma=1 / cl0, device=dev, Lf=st['Lf'], centre='identity')
    beta0 = st['beta'].to(dev) if (N, M) == (st['N'], st['M']) else ipm3s.regrid_s(qo, st['beta'].to(dev), q)
    u = q.beta_to_u(beta0)
    # (i) the forced residual of the start on this grid (is the start resolved?)
    F0, _, _ = q.system(u, cl0, gK, mu=st['mu'], forced=True)
    log.write(f"  start: forced |F|max on {N}x{M} = {F0.abs().max().item():.2e}, |F|2 = {F0.norm().item():.2e}, mu = {st['mu']:.8f}, Delta0 = {st['mu']/beta0[0,0].item():+.4e}\n")
    t0 = time.time()
    u2, cl2, _, info = q.gn(u, cl0, gK, mu=None, forced=False, maxit=60, log=log)
    report(q, u2, cl2, None, info, f"QL release {N}x{M} from {start} (start cl={cl0}, Delta0={st['mu']/beta0[0,0].item():+.3e}; {time.time()-t0:.0f}s)", log)
    beta = q.beta_full(u2)
    torch.save(dict(beta=beta.cpu(), u=u2.cpu(), cl=cl2, mu=None, gamma=1 / cl2, N=N, M=M, L=1.0, Lf=st['Lf'], gK=gK, p=q.p, rep='QL', hist=info['hist']), f'runs/{tag}.pt')
