"""Amplitude continuation of the forced problem at fixed c_l: gauge b(inf) = beta, scan beta; report mu(beta), a0, c."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
N = int(sys.argv[1]); M = int(sys.argv[2]); L = float(sys.argv[3]); tag = sys.argv[4]
cl = float(sys.argv[5]); betas = [float(v) for v in sys.argv[6].split(',')]
log = open(f'runs/{tag}.log', 'a')
log.write(f"# beta scan N={N} M={M} L={L} cl={cl} betas={betas}  {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
gamma = 1/cl
mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=gamma, device=dev); mdl.gauge = 'inf'
b = betas[0]*torch.ones(N+1, M, device=dev); mu = 0.0
for beta in betas:
    t0 = time.time()
    mb = (mdl.rad.ext1_R @ b).mean().item(); b_try = b * (beta / (mb if abs(mb) > 1e-300 else 1e-300))
    b_new, _, info = ipm3.newton(mdl, b_try, cl, gauge_value=beta, maxit=80, tol=1e-12, verbose=False, log=log, mu=mu, forced=True)
    c = mdl.psi_xy0(info['flds']).item()
    sv = torch.linalg.svdvals(info['J'])
    a0 = b_new[0,0].item()
    msg = (f"cl={cl:.4f} beta={beta:8.4f}: mu={info['mu']:+.10f}  mu/beta^2={info['mu']/beta**2:+.6f}  a0={a0:.8f}  c={c:+.8f} (need {1-cl:+.4f}; cl-1+c={cl-1+c:+.6f})"
           f"  |F|={info['nF']:.2e} iters={len(info['hist'])}  smin(J)={sv[-1].item():.3e}  b range [{b_new.min().item():.4f},{b_new.max().item():.4f}]  {time.time()-t0:.1f}s")
    print(msg, flush=True); log.write(msg+"\n"); log.flush()
    if info['nF'] < 1e-8:
        b, mu = b_new, info['mu']
        torch.save(dict(b=b.cpu(), cl=cl, gamma=gamma, N=N, M=M, L=L, p=mdl.p, mu=mu, gauge='inf', beta=beta), f'runs/{tag}_beta{beta:.4f}.pt')
    else:
        print("  not converged; continuing from last converged state", flush=True)
