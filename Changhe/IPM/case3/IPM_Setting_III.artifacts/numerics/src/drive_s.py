"""Driver for the smooth-centre representation (ipm3s).
 modes:
   forced  N M L tag gaugeK cl1,cl2,...   : fixed c_l, solve (beta, mu) with forcing; report mu(c_l), a0, c, K, Lcan
   free    N M L tag gaugeK cl0 [start.pt]: c_l free (unforced), from beta_0 = gaugeK const or a saved state
   betascan N M L tag cl  g1,g2,...        : fixed c_l forced, scan the gauge value (far-field y-axis amplitude)
"""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import ipm3, ipm3s
torch.set_default_dtype(torch.float64)
dev = 'cuda'
mode = sys.argv[1]; N = int(sys.argv[2]); M = int(sys.argv[3]); L = float(sys.argv[4]); tag = sys.argv[5]
log = open(f'runs/{tag}.log', 'a')
def stamp(): return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
def report(mdl, beta, cl, info, extra=""):
    c = mdl.psi_xy0(info['flds']).item(); K, Lcan = mdl.K_of_state(beta, cl)
    sv = torch.linalg.svdvals(info['J']); a0 = beta[0,0].item()
    # between-node residual
    tR = mdl.rad.tR_np; tm = 0.5*(tR[:-1] + tR[1:]); th = mdl.ang.theta_np; thm = 0.5*(th[:-1] + th[1:])
    rm = mdl.rad.rmap_np(tm); RR, TT = np.meshgrid(rm, thm, indexing='ij')
    ev = mdl.evaluate(beta, cl, info['flds'], RR, TT); q = np.abs(ev['R'])/ev['Nf']
    og = [q[(RR>=lo)&(RR<hi)].max() if ((RR>=lo)&(RR<hi)).sum() else float('nan') for lo,hi in [(0,1),(1,100),(100,1e4),(1e4,1e30)]]
    msg = (f"{extra} cl={cl:.12f} c={c:+.12f} cl+c-1={cl+c-1:+.2e} a0={a0:.10f} K={K:.6f} Lcan={Lcan:.5g} |F|={info['nF']:.2e} iters={len(info['hist'])} "
           f"smin={sv[-1].item():.2e} s[-2]={sv[-2].item():.2e} offgrid|R|/Nf [r<1,1-1e2,1e2-1e4,>1e4]= {og[0]:.1e} {og[1]:.1e} {og[2]:.1e} {og[3]:.1e}"
           + (f" mu={info['mu']:+.10f}" if info.get('mu') is not None else ""))
    print(msg, flush=True); log.write(msg + "\n"); log.flush()
    return msg
if mode == 'forced':
    gK = float(sys.argv[6]); cls = [float(v) for v in sys.argv[7].split(',')]
    log.write(f"# {stamp()} SCR forced scan N={N} M={M} L={L} gaugeK={gK} cls={cls}\n")
    for cl in cls:
        mdl = ipm3s.IPM3S(N=N, M=M, L=L, gamma=1/cl, device=dev)
        beta = torch.zeros(N+1, M, device=dev); beta[:, 0] = gK
        beta, _, info = ipm3.newton(mdl, beta, cl, gauge_value=gK, maxit=80, tol=1e-12, verbose=False, log=log, mu=0.0, forced=True)
        report(mdl, beta, cl, info, extra=f"[forced gK={gK}]")
        torch.save(dict(beta=beta.cpu(), cl=cl, gamma=1/cl, N=N, M=M, L=L, p=mdl.p, mu=info['mu'], gK=gK, rep='SCR'), f'runs/{tag}_cl{cl:.4f}.pt')
elif mode == 'free':
    gK = float(sys.argv[6]); cl = float(sys.argv[7]); start = sys.argv[8] if len(sys.argv) > 8 else None
    log.write(f"# {stamp()} SCR free-c_l solve N={N} M={M} L={L} gaugeK={gK} cl0={cl} start={start}\n")
    mdl = ipm3s.IPM3S(N=N, M=M, L=L, gamma=1/cl, device=dev, couple_gamma=True)
    if start is None:
        beta = torch.zeros(N+1, M, device=dev); beta[:, 0] = gK
    else:
        st = torch.load(start); mo = ipm3s.IPM3S(N=st['N'], M=st['M'], L=st['L'], gamma=st['gamma'], p=st['p'], device=dev)
        beta = ipm3s.regrid_s(mo, st['beta'].to(dev), mdl); cl = st['cl']
    for outer in range(4):
        beta, cl, info = ipm3.newton(mdl, beta, cl, gauge_value=gK, maxit=80, tol=1e-12, verbose=True, log=log)
        report(mdl, beta, cl, info, extra=f"[free outer {outer} p={mdl.p:.6f}]")
        if info['nF'] > 1e-8 or abs(mdl.p - 1/(1-1/cl)) < 1e-8: break
        mdl_new = ipm3s.IPM3S(N=N, M=M, L=L, gamma=1/cl, device=dev, couple_gamma=True)
        beta = ipm3s.regrid_s(mdl, beta, mdl_new); mdl = mdl_new
    torch.save(dict(beta=beta.cpu(), cl=cl, gamma=1/cl, N=N, M=M, L=L, p=mdl.p, gK=gK, rep='SCR'), f'runs/{tag}.pt')
elif mode == 'betascan':
    cl = float(sys.argv[6]); gs = [float(v) for v in sys.argv[7].split(',')]
    log.write(f"# {stamp()} SCR beta scan N={N} M={M} L={L} cl={cl} gauge values {gs}\n")
    mdl = ipm3s.IPM3S(N=N, M=M, L=L, gamma=1/cl, device=dev)
    beta = torch.zeros(N+1, M, device=dev); beta[:, 0] = gs[0]; mu = 0.0
    for gK in gs:
        bt = beta * (gK / mdl.gauge_row(beta, 0.0).item())
        bnew, _, info = ipm3.newton(mdl, bt, cl, gauge_value=gK, maxit=80, tol=1e-12, verbose=False, log=log, mu=mu, forced=True)
        report(mdl, bnew, cl, info, extra=f"[betascan cl={cl} gK={gK}]")
        if info['nF'] < 1e-8:
            beta, mu = bnew, info['mu']
            torch.save(dict(beta=beta.cpu(), cl=cl, gamma=1/cl, N=N, M=M, L=L, p=mdl.p, mu=mu, gK=gK, rep='SCR'), f'runs/{tag}_g{gK:.4f}.pt')
