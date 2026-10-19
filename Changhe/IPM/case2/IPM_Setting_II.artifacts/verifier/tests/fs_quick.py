import sys, time, math, json, numpy as np, torch
sys.path.insert(0, 'code')
from fwdstat import FwdStat
t0 = time.time()
F = FwdStat(0.5, lambda th: np.cos(th)**2, tmin=-8, tmax=8, ppu=3, q=8, nt=64, dti=0.02, nstep=400)
rho = F.initial()
for k in range(40):
    rn, info = F.T_partial(rho, dT=4.0, nstep=100)
    err = float(((rn - rho)/F.R**F.p).abs().max())
    rho = rn
    nd = F.node(rho)
    print(k, 'err %.3e c %.6f m1 %.6f minalpha %.4f  t %.1f' % (err, nd['c'], nd['m1'], info['minalpha'], time.time()-t0), flush=True)
