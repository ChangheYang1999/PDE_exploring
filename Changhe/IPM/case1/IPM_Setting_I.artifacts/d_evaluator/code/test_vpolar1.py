import numpy as np, sys
from scipy.special import gammainc
from vpolar import *
rho = lambda x,y: x**2*y*np.exp(-x**2-y**2)
for N in [200,400,800]:
    g = LogGrid(N, 1e-3, 12.0)
    Nt = 64
    th = 2*np.pi*np.arange(Nt)/Nt
    X = g.r[:,None]*np.cos(th)[None]; Y = g.r[:,None]*np.sin(th)[None]
    fm, bad, hi = modes_from_samples(rho(X,Y), 31)
    pm = psi_modes(g, fm, 30, tail_lo={1:(0.25,3),3:(0.25,3)})
    r = g.r
    p2ex = (1/8)*(r**2*np.exp(-r**2)/2 - r**-2*gammainc(3,r**2))
    p4ex = -(1/16)*r**-4*6*gammainc(4,r**2)
    c = center_c(g, fm[3], tail_lo=(0.25,3))
    rel = lambda a,b: np.abs(a-b).max()/np.abs(b).max()
    print(N, 'parity-bad %.1e'%bad, 'p2 relerr %.2e'%rel(pm[2][0],p2ex), 'p4 relerr %.2e'%rel(pm[4][0],p4ex),
          'p4 pointwise-rel %.2e'%(np.abs(pm[4][0]-p4ex)/np.abs(p4ex)).max(), 'c-1/8 %.2e'%(c-1/8))
