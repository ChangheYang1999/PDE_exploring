"""Method B (vquad) vs exact U for rho = x^2 y e^{-r^2}, and vs method A (vpolar) for the growing field
rho = x^2 y (1+r^2)^{(k-3)/2}, k = 0.6."""
import numpy as np, torch, time
import sympy as sp, mpmath as mp
from vquad import disc_velocity, tail_coeffs, tail_velocity
from vpolar import LogGrid
from vresid import evaluate
mp.mp.dps = 40
rs = sp.symbols('r', positive=True); s = rs**2
p2 = (sp.exp(-s)*(s**2+s+1)-1)/(8*s); p4 = (sp.exp(-s)*(s**3+3*s**2+6*s+6)-6)/(16*s**2)
fp = {n: (sp.lambdify(rs, p, 'mpmath'), sp.lambdify(rs, sp.diff(p, rs), 'mpmath')) for n, p in ((2, p2), (4, p4))}
def Uexact(X):
    r = np.hypot(X[:,0], X[:,1]); t = np.arctan2(X[:,1], X[:,0])
    P = {n: (np.array([float(fp[n][0](mp.mpf(x))) for x in r]), np.array([float(fp[n][1](mp.mpf(x))) for x in r])) for n in (2,4)}
    psr = P[2][1]*np.sin(2*t) + P[4][1]*np.sin(4*t); pst = 2*P[2][0]*np.cos(2*t) + 4*P[4][0]*np.cos(4*t)
    Ur, Ut = -pst/r, psr
    return np.stack([np.cos(t)*Ur - np.sin(t)*Ut, np.sin(t)*Ur + np.cos(t)*Ut], 1)
rng = np.random.default_rng(1)
Xt = np.concatenate([rng.uniform(-3, 3, (60, 2)), np.array([[0.01, 0.02], [1.0, 0.0], [0.0, 1.0], [2.5, 2.5]])])
F1 = lambda x, y: (2*x*y - 2*x**3*y)*torch.exp(-(x**2+y**2))
Ue = Uexact(Xt)
for nphi, npan in ((128, 24), (256, 48), (512, 64)):
    t0 = time.time(); Ub = disc_velocity(F1, Xt, 12.0, nphi=nphi, npan=npan)
    print(f"decaying: nphi={nphi} npan={npan}: max|U_B - U_exact| = {np.abs(Ub-Ue).max():.2e} (max|U|={np.abs(Ue).max():.2e}) {time.time()-t0:.1f}s")
# growing field
k = 0.6
def F2(x, y):
    r2 = x**2 + y**2
    return (2*x*y*(1+r2)**((k-3)/2) + x**2*y*(k-3)*x*(1+r2)**((k-5)/2))
rhof = lambda x, y: x**2*y*(1+x**2+y**2)**((k-3)/2)
N, Nt = 2400, 64
g = LogGrid(N, 1e-3, 1e5); th = 2*np.pi*np.arange(Nt)/Nt
r = g.r; X = r[:,None]*np.cos(th); Y = r[:,None]*np.sin(th)
ev = evaluate(rhof(X, Y), g, th, c_l=1.5, k_far=k)
print('method A c =', ev.c, 'exact', 1/(4*(1-k)))
# compare at targets on grid points of method A
idx_r = [np.argmin(abs(r - v)) for v in (0.05, 0.3, 1.0, 2.0, 5.0, 10.0)]
pts = [(j, i) for j in idx_r for i in (1, 5, 9, 14)]
XA = np.array([[X[j,i], Y[j,i]] for j, i in pts])
UA = np.array([[np.cos(th[i])*ev.Ur[j,i] - np.sin(th[i])*ev.Ut[j,i], np.sin(th[i])*ev.Ur[j,i] + np.cos(th[i])*ev.Ut[j,i]] for j, i in pts])
for RB, RF in ((50.0, 1e5), (100.0, 1e5), (200.0, 1e5)):
    t0 = time.time()
    Ud = disc_velocity(F2, XA, RB, nphi=512, npan=64)
    T = tail_coeffs(F2, RB, RF, 40, k)
    Ut_ = tail_velocity(T, XA)
    UB = Ud + Ut_
    print(f"growing: RB={RB}: max|U_B - U_A| = {np.abs(UB-UA).max():.2e}, max|U_A|={np.abs(UA).max():.2e}, tail max {np.abs(Ut_).max():.2e}  {time.time()-t0:.1f}s")
