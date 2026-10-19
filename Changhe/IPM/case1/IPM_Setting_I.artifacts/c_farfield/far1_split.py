import sys, numpy as np
sys.path.insert(0, '.')
# usage: python3 far1_split.py [coef_shape.npz [export_fields.npz]] (defaults: the candidate and its export)
SHAPE = sys.argv[1] if len(sys.argv) > 1 else 'c6g_shape.npz'
EXPORT = sys.argv[2] if len(sys.argv) > 2 else 'c6gx_fields.npz'
from far1 import run, Trial
P = SHAPE
o, (th, Th0, Th1f, Th1e) = run(P, verbose=False)
k = o['k']; L = o['L']; cl = o['c_l']; N = len(th)
z = np.load(EXPORT, mmap_mode='r')
r = np.array(z['r']); tq = np.array(z['theta'])
sel = slice(0, N//4+1)
I = lambda f, x: np.interp(x, th[sel], f[sel])
for jt in [len(tq)-3, len(tq)-10, 450, 300, 150]:
    t0 = tq[jt]
    T0 = I(Th0, t0); T1f = I(Th1f, t0); T1e = I(Th1e, t0)
    print('theta %.5f  Th0 %.4e  (1-c_l)Th1f %+.6e  (c_l-1)Th1e %+.6e' % (t0, T0, (1-cl)*T1f, (cl-1)*T1e))
    for rr in [300*L, 1000*L, 3000*L, 6000*L]:
        i = np.argmin(np.abs(r-rr)); R = r[i]
        x, y = R*np.cos(t0), R*np.sin(t0)
        rho = z['rho'][i, jt]; rx = z['rho_x'][i, jt]; ry = z['rho_y'][i, jt]
        u1 = z['U1'][i, jt]; u2 = z['U2'][i, jt]
        A = cl*(x*rx+y*ry)-rho; B = u1*rx+u2*ry
        sc = R**(2*k-1)*T0
        print('   r/L %5.0f  rho/(r^k Th0) %.8f  A/sc %+.6e  B/sc %+.6e  (A+B)/sc %+.3e  res/den %+.3e' % (R/L, rho/(R**k*T0), A/sc, B/sc, (A+B)/sc, z['residual'][i, jt]/z['denominator'][i, jt]))
