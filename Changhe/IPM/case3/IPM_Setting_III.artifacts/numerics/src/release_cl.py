"""Start the unforced coupled (gamma = 1/c_l) Newton from a saved forced state; gauge 'inf' at that state's beta."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
start = sys.argv[1]; tag = sys.argv[2]
st = torch.load(start)
log = open(f'runs/{tag}.log', 'a')
log.write(f"# release c_l from {start}  {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
N, M, L = st['N'], st['M'], st['L']
mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=st['gamma'], p=st['p'], device=dev, couple_gamma=True); mdl.gauge = 'inf'
b = st['b'].to(dev); cl = st['cl']; beta = st.get('beta', (mdl.rad.ext1_R @ b).mean().item())
F0, _, _ = mdl.system(b, cl, gauge_value=beta)
print(f"start: cl={cl} beta={beta} mu_forced={st.get('mu')} |F_unforced|={F0.abs().max().item():.3e}")
b, cl, info = ipm3.newton(mdl, b, cl, gauge_value=beta, maxit=60, tol=1e-12, verbose=True, log=log)
c = mdl.psi_xy0(info['flds']).item()
sv = torch.linalg.svdvals(info['J'])
msg = f"RESULT {start}: cl={cl:.12f} c={c:.12f} cl+c-1={cl+c-1:.2e} a0={b[0,0].item():.10f} b(inf)={(mdl.rad.ext1_R @ b).mean().item():.6f} |F|={info['nF']:.2e} iters={len(info['hist'])} smin(J)={sv[-1].item():.3e} s[-2]={sv[-2].item():.3e} b range [{b.min().item():.4f},{b.max().item():.4f}]"
print(msg); log.write(msg+"\n")
torch.save(dict(b=b.cpu(), cl=cl, gamma=mdl.gamma, N=N, M=M, L=L, p=mdl.p), f'runs/{tag}.pt')
