"""Sheet-uniqueness test: at fixed (c_l, beta) solve the forced problem from several H1-type initial guesses
b = beta + (a0g - beta)/(1 + (r/R)^2) and compare the converged (mu, a0)."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
N = int(sys.argv[1]); M = int(sys.argv[2]); L = 1.0; tag = sys.argv[3]
cls = [float(v) for v in sys.argv[4].split(',')]; beta = float(sys.argv[5])
log = open(f'runs/{tag}.log', 'a'); log.write(f"# multistart forced N={N} M={M} beta={beta} cls={cls} {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
for cl in cls:
    mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=1/cl, device=dev); mdl.gauge = 'inf'
    r = mdl.rad.rR[:, None]
    for a0g in [0.25*beta, beta, 4*beta, 16*beta, 64*beta]:
        for R in [0.1, 1.0, 10.0, 100.0]:
            bg = beta + (a0g - beta)/(1 + (r/R)**2) * torch.ones(1, M, device=dev)
            t0 = time.time()
            b, _, info = ipm3.newton(mdl, bg, cl, gauge_value=beta, maxit=80, tol=1e-12, verbose=False, log=log, mu=0.0, forced=True)
            c = mdl.psi_xy0(info['flds']).item()
            msg = f"cl={cl:.3f} beta={beta} guess a0g={a0g:8.3f} R={R:6.1f}: -> mu={info['mu']:+.8f} a0={b[0,0].item():.8f} c={c:+.8f} |F|={info['nF']:.1e} it={len(info['hist'])} {time.time()-t0:.1f}s"
            print(msg, flush=True); log.write(msg+"\n"); log.flush()
