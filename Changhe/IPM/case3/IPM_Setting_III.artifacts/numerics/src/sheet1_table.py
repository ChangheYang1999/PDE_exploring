"""Converged table of mu(c_l, beta) on sheet 1 (continued from b = const) at a given resolution, with smin, a0, c,
Delta = c_l + c - 1, K, Lcan and the between-node residual of the forced equation."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
N = int(sys.argv[1]); M = int(sys.argv[2]); tag = sys.argv[3]
cls = [float(v) for v in sys.argv[4].split(',')]; betas = [float(v) for v in sys.argv[5].split(',')]; L = 1.0
log = open(f'runs/{tag}.log', 'a'); log.write(f"# sheet1 table N={N} M={M} cls={cls} betas={betas} {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
for cl in cls:
    mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=1/cl, device=dev); mdl.gauge = 'inf'
    b = None; mu = 0.0
    for beta in betas:
        bg = beta*torch.ones(N+1, M, device=dev) if b is None else b*(beta/(mdl.rad.ext1_R @ b).mean().item())
        b2, _, info = ipm3.newton(mdl, bg, cl, gauge_value=beta, maxit=100, tol=1e-12, verbose=False, log=log, mu=mu, forced=True)
        c = mdl.psi_xy0(info['flds']).item(); a0 = b2[0,0].item(); sv = torch.linalg.svdvals(info['J'])
        bhat = mdl.ang.to_coef(b2, 'EE'); bK = ((mdl.rad.ext1_R @ bhat)[0]*torch.cos(math.pi*torch.arange(M, device=dev, dtype=torch.float64))).sum().item()
        K = bK; Lcan = (K/a0)**(cl/(cl-1)) if K/a0 > 0 else float('nan')
        tR = mdl.rad.tR_np; tm = 0.5*(tR[:-1]+tR[1:]); th = mdl.ang.theta_np; thm = 0.5*(th[:-1]+th[1:])
        rm = mdl.rad.rmap(torch.tensor(tm)).numpy(); RR, TT = np.meshgrid(rm, thm, indexing='ij')
        ev = mdl.evaluate(b2, cl, info['flds'], RR, TT); tt = mdl.rad.t_of_r(RR); phi = mdl.rad.one_minus_s2_of_t(torch.tensor(tt)).numpy()**2
        q = (np.abs(ev['R'] - info['mu']*ev['y']*phi)/ev['Nf']).max()
        msg = f"cl={cl:6.3f} beta={beta:7.3f}: mu={info['mu']:+.10f} Delta={cl+c-1:+.8f} a0={a0:.8f} c={c:+.8f} K={K:.6f} Lcan={Lcan:.5g} |F|={info['nF']:.1e} it={len(info['hist'])} smin={sv[-1].item():.1e} offgrid|R_forced|/Nf={q:.1e}"
        print(msg, flush=True); log.write(msg+"\n"); log.flush()
        if info['nF'] < 1e-8: b, mu = b2, info['mu']
