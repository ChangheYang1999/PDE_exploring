"""Valley state at c_l ~ 1.5, beta = 16, N = 96, M = 24 with a NON-default map power p (lead's request: does the measured
centre exponent move with p?).  Start from the saved default-p state, regrid, free-c_l Newton, then Chebyshev tail."""
import sys, math, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'; pfac = float(sys.argv[1]); tag = sys.argv[2]
st = torch.load('runs/res_cl1.5_N96M24.pt'); N, M, L = st['N'], st['M'], st['L']
mo = ipm3.IPM3(N=N, M=M, L=L, gamma=st['gamma'], p=st['p'], device=dev)
p_new = st['p']*pfac
mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=st['gamma'], p=p_new, device=dev, couple_gamma=True); mdl.gauge = 'inf'
b = ipm3.regrid(mo, st['b'].to(dev), mdl); cl = st['cl']; beta = (mdl.rad.ext1_R @ b).mean().item()
log = open(f'runs/{tag}.log', 'a')
b, cl, info = ipm3.newton(mdl, b, cl, gauge_value=beta, maxit=150, tol=1e-12, verbose=False, log=log)
bhat = mdl.ang.to_coef(b, 'EE'); t = mdl.rad.tR_np; V = np.cos(np.outer(np.arccos(t), np.arange(N+1)))
ck = np.linalg.lstsq(V, bhat[:,0].cpu().numpy(), rcond=None)[0]; n = np.arange(N+1); tail = slice(N//2, N-2); s0 = ((-1.0)**n*ck)[tail]
sl = np.polyfit(np.log(n[tail]), np.log(np.abs(s0)+1e-300), 1)[0]
rr = np.logspace(-4, -1, 7); tt = mdl.rad.t_of_r(rr); P = torch.tensor(ipm3.interp_matrix(mdl.rad.tR_np, tt, mdl.rad.wR_np), device=dev); bk = (P @ bhat).cpu().numpy()
a0 = b[0,0].item(); ls0 = np.diff(np.log(np.abs(bk[:,0]-a0)))/np.diff(np.log(rr))
print(f"p = {p_new:.4f} (default {st['p']:.4f}): |F|={info['nF']:.1e} cl={cl:.8f} a0={a0:.6f} tail sign-frac(+)={(s0>0).mean():.2f} slope={sl:+.2f} -> d-1 ~ {(-sl-1)/2:.2f}; near-0 slopes of b0-a0: {np.array2string(ls0, precision=2)}", flush=True)
