"""Trace the forced sheet through the planted solution (see manufactured_test.py): forced solves at c_l near c_lm
starting from b_m (regridded), gauge beta_m; also forced solves exactly at c_lm from several starts."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'; N = int(sys.argv[1]); M = int(sys.argv[2]); a0m = float(sys.argv[3]); kap = float(sys.argv[4]); tag = sys.argv[5]
L = 1.0; log = open(f'runs/{tag}.log', 'a')
def P(msg): print(msg, flush=True); log.write(msg + "\n"); log.flush()
def b_m(mdl, gm):
    r = mdl.rad.rR[:, None]; th = mdl.ang.theta[None, :]; x2 = (r*torch.cos(th))**2
    return a0m*(1 + r**2/L**2)**((gm-1)/2)*(1 + kap*x2/(L**2 + r**2))/mdl.wR[:, None]
gm = 0.5
for it in range(40):
    mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=gm, device=dev); mdl.gauge = 'inf'
    c = mdl.psi_xy0(mdl.fields(b_m(mdl, gm))).item(); clm = 1 - c
    if abs(1/clm - gm) < 1e-13: break
    gm = 1/clm
mdl0 = ipm3.IPM3(N=N, M=M, L=L, gamma=1/clm, device=dev); mdl0.gauge = 'inf'; bm = b_m(mdl0, 1/clm)
beta_m = (mdl0.rad.ext1_R @ bm).mean().item()
def target_for(mdl): return mdl.residual(b_m(mdl, 1/clm), clm)
P(f"planted: c_lm={clm:.10f} a0m={a0m} beta_m={beta_m:.6f}")
# forced solves exactly at c_lm from several starts
r = mdl0.rad.rR[:, None]
starts = {'b_m exact': bm, 'b_m*1.1': bm*1.1, 'const': beta_m*torch.ones_like(bm), 'H1 ratio2 R0.3': beta_m + (2*beta_m - beta_m)/(1 + (r/0.3)**2)*torch.ones(1, M, device=dev),
          'H1 ratio4 R1': beta_m + (4*beta_m - beta_m)/(1 + (r/1.0)**2)*torch.ones(1, M, device=dev)}
tgt0 = target_for(mdl0)
for name, bg in starts.items():
    b, _, info = ipm3.newton(mdl0, bg, clm, gauge_value=beta_m, target=tgt0, maxit=80, tol=1e-12, verbose=False, log=log, mu=0.0, forced=True)
    sv = torch.linalg.svdvals(info['J'])
    P(f"  forced at c_lm from {name:16s}: |F|={info['nF']:.1e} it={len(info['hist'])} mu={info['mu']:+.3e} a0={b[0,0].item():.6f} max|b-b_m|={(b-bm).abs().max().item():.1e} smin={sv[-1].item():.1e}")
# sheet through the planted solution: continuation in c_l both ways from b_m
for direction in [+1, -1]:
    mdl_p, b_p, mu_p = mdl0, bm, 0.0
    for k in range(1, 9):
        cl = clm + direction*0.02*k
        mdlC = ipm3.IPM3(N=N, M=M, L=L, gamma=1/cl, device=dev); mdlC.gauge = 'inf'
        bg = ipm3.regrid(mdl_p, b_p, mdlC); bg = bg*(beta_m/(mdlC.rad.ext1_R @ bg).mean().item())
        b, _, info = ipm3.newton(mdlC, bg, cl, gauge_value=beta_m, target=target_for(mdlC), maxit=80, tol=1e-12, verbose=False, log=log, mu=mu_p, forced=True)
        sv = torch.linalg.svdvals(info['J'])
        P(f"  sheet through planted: cl={cl:.4f} mu={info['mu']:+.6f} a0={b[0,0].item():.6f} |F|={info['nF']:.1e} it={len(info['hist'])} smin={sv[-1].item():.1e}")
        if info['nF'] > 1e-8: break
        mdl_p, b_p, mu_p = mdlC, b, info['mu']
