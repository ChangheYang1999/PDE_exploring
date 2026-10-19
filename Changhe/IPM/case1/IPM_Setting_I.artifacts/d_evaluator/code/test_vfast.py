import numpy as np, time
from vpolar import LogGrid, modes_from_samples, psi_modes, center_c
from vfast import FastInverse
k = 0.6
g = LogGrid(1200, 1e-4, 1e4); Nt = 64; th = 2*np.pi*np.arange(Nt)/Nt
r = g.r; X = r[:,None]*np.cos(th); Y = r[:,None]*np.sin(th)
rho = X**2*Y*(1+X**2+Y**2)**((k-3)/2)
fm, bad, top = modes_from_samples(rho, 31)
th_hi = {m: (f[-1]/r[-1]**k, k) for m, f in fm.items()}
th_lo = {m: (f[0]/r[0]**max(m,3), max(m,3)) for m, f in fm.items()}
t0=time.time(); pm = psi_modes(g, fm, 30, th_hi, th_lo); c1 = center_c(g, fm[3], th_hi[3], th_lo[3]); t1=time.time()
F = np.array([fm[m] for m in range(1, 32, 2)])
fi = FastInverse(g, 30); t2=time.time()
p, dp, c2 = fi.solve(F, (F[:, -1]/r[-1]**k, k), (F[:,0], np.array([max(2*i+1,3) for i in range(16)])))
t3=time.time()
print('slow', t1-t0, 's; setup', t2-t1, 's; fast solve', t3-t2, 's')
print('c', c1, c2, 'exact', 1/(4*(1-k)))
print('max diff p', max(np.abs(p[a]-pm[n][0]).max() for a, n in enumerate(range(2,31,2))), 'dp', max(np.abs(dp[a]-pm[n][1]).max() for a, n in enumerate(range(2,31,2))))
