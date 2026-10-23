"""Converge valley (unforced, c_l free) states from saved starts with many Newton iterations, then report the
Chebyshev-tail exponent of beta_0, a0, c_l, K, Lcan and the between-node residual (data for the indicial comparison)."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'; tag = sys.argv[1]; files = sys.argv[2:]
log = open(f'runs/{tag}.log', 'a'); log.write(f"# valley converge {files} {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
for f in files:
    st = torch.load(f); N, M, L = st['N'], st['M'], st['L']
    mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=st['gamma'], p=st['p'], device=dev, couple_gamma=True); mdl.gauge = 'inf'
    b = st['b'].to(dev); cl = st['cl']; beta = (mdl.rad.ext1_R @ b).mean().item()
    t0 = time.time()
    for rnd in range(3):
        b, cl, info = ipm3.newton(mdl, b, cl, gauge_value=beta, maxit=150, tol=1e-12, verbose=False, log=log)
        if info['nF'] < 1e-11: break
        mdl_new = ipm3.IPM3(N=N, M=M, L=L, gamma=1/cl, device=dev, couple_gamma=True); mdl_new.gauge = 'inf'
        b = ipm3.regrid(mdl, b, mdl_new); mdl = mdl_new
    c = mdl.psi_xy0(info['flds']).item(); a0 = b[0,0].item()
    bhat = mdl.ang.to_coef(b, 'EE'); bK = ((mdl.rad.ext1_R @ bhat)[0]*torch.cos(math.pi*torch.arange(M, device=dev, dtype=torch.float64))).sum().item()
    K = L**(1-1/cl)*bK; Lcan = (K/a0)**(cl/(cl-1)) if K/a0 > 0 else float('nan')
    t = mdl.rad.tR_np; V = np.cos(np.outer(np.arccos(t), np.arange(N+1))); ck = np.linalg.lstsq(V, bhat[:,0].cpu().numpy(), rcond=None)[0]
    n = np.arange(N+1); tail = slice(N//2, N-2); s0 = ((-1.0)**n*ck)[tail]; sl = np.polyfit(np.log(n[tail]), np.log(np.abs(s0)+1e-300), 1)[0]
    tR = mdl.rad.tR_np; tm = 0.5*(tR[:-1]+tR[1:]); th = mdl.ang.theta_np; thm = 0.5*(th[:-1]+th[1:])
    rm = mdl.rad.rmap(torch.tensor(tm)).numpy(); RR, TT = np.meshgrid(rm, thm, indexing='ij')
    ev = mdl.evaluate(b, cl, info['flds'], RR, TT); q = (np.abs(ev['R'])/ev['Nf']).max()
    msg = (f"{f}: N={N} M={M} -> cl={cl:.10f} c={c:+.10f} cl+c-1={cl+c-1:+.1e} a0={a0:.8f} A={2*cl-1:.4f} K={K:.5f} Lcan={Lcan:.4g} |F|={info['nF']:.1e} "
           f"offgrid|R|/Nf={q:.1e} tail: sign-frac(+)={(s0>0).mean():.2f} slope={sl:+.2f} -> d-1~{(-sl-1)/2:.2f} |c_N/2|={abs(ck[N//2]):.1e} |c_N-3|={abs(ck[N-3]):.1e} {time.time()-t0:.0f}s")
    print(msg, flush=True); log.write(msg+"\n"); log.flush()
    torch.save(dict(b=b.cpu(), cl=cl, gamma=mdl.gamma, N=N, M=M, L=L, p=mdl.p), f'runs/{tag}_{f.split("/")[-1]}')
