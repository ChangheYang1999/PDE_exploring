import numpy as np, time
from vpolar import LogGrid, modes_from_samples, psi_modes
k = 0.18
g = LogGrid(1500, 1e-4, 3e3); Nt = 128; th = 2*np.pi*np.arange(Nt)/Nt
r = g.r; X = r[:,None]*np.cos(th); Y = r[:,None]*np.sin(th)
rho = X**2*Y*(1+X**2+Y**2)**((k-3)/2)*(1+0.3*np.cos(3*th))
fm, bad, top = modes_from_samples(rho, 63)
th_hi = {m: (f[-1]/r[-1]**k, k) for m, f in fm.items()}
th_lo = {m: (f[0]/r[0]**max(m,3), max(m,3)) for m, f in fm.items()}
t0 = time.time(); a = psi_modes(g, fm, 64, th_hi, th_lo, slow=True); t1 = time.time()
b = psi_modes(g, fm, 64, th_hi, th_lo); t2 = time.time()
sc = max(np.abs(a[n][0]).max() for n in a); scd = max(np.abs(a[n][1]).max() for n in a)
print('slow %.1f s fast %.2f s' % (t1 - t0, t2 - t1))
print('max |dp|/scale %.2e  |d dp|/scale %.2e' % (max(np.abs(a[n][0]-b[n][0]).max() for n in a)/sc, max(np.abs(a[n][1]-b[n][1]).max() for n in a)/scd))
