import numpy as np, time, sys
sys.path.insert(0, '.')
import manufactured as mf
import sympy as sp, mpmath as mp
from vmodal import Radial, ModalInverse
mp.mp.dps = 60
t0=time.time()
f, rho_s, psi_s = mf.lambdified(mf.DEFAULT_TERMS)
x,y = mf.x, mf.y
U1s = -sp.diff(psi_s,y); U2s = sp.diff(psi_s,x)
fm = {k: sp.lambdify((x,y), v, 'mpmath') for k,v in dict(rho=rho_s, psi=psi_s, U1=U1s, U2=U2s).items()}
pxy_s = sp.diff(psi_s, x, y)
fpxy = sp.lambdify((x,y), pxy_s, 'mpmath')
c_exact = fpxy(mp.mpf('1e-20'), mp.mpf('3e-20'))
a0_exact = sp.lambdify((x,y), sp.diff(rho_s,y), 'mpmath')(mp.mpf('1e-25'), mp.mpf('1e-25'))
print('exact a0 = %s  exact psi_xy(0) = %s' % (mp.nstr(a0_exact,15), mp.nstr(c_exact,15)))
def rho_fun(X, Y):
    # robust float evaluation: use lambdified numpy where r>1e-3, else mpmath
    out = f['rho'](X, Y)
    small = (X**2+Y**2) < 1e-6
    if small.any():
        idx = np.where(small)
        out = np.array(out, dtype=float)
        for i in zip(*idx):
            out[i] = float(fm['rho'](mp.mpf(X[i]), mp.mpf(Y[i])))
    return out
rng = np.random.default_rng(1)
for (tmin,tmax,npan,q,M) in [(np.log(1e-8), np.log(1e10), 300, 16, 32), (np.log(1e-8), np.log(1e14), 400, 16, 48), (np.log(1e-9), np.log(1e20), 600, 20, 64)]:
    rad = Radial(tmin, tmax, npan, q)
    inv = ModalInverse(rad, M)
    t0=time.time()
    out = inv.velocity_on_grid(rho_fun)
    tt = time.time()-t0
    s = inv.strain_at_origin(out['b'], out['P'], out['Q'])
    # compare on random subset of grid nodes with 1e-6<r<1e6
    r = rad.r.reshape(-1); sel = np.where((r>1e-6)&(r<1e6))[0]
    ii = rng.choice(sel, 300); jj = rng.integers(0, M, 300)
    errU = 0; errp = 0
    for i,j in zip(ii,jj):
        p_, k_ = divmod(i, q)
        rr = r[i]; th = inv.th[j]
        X = mp.mpf(rr)*mp.cos(th); Y = mp.mpf(rr)*mp.sin(th)
        sc = max(1.0, rr)**0.5
        e = max(abs(out['U1'][p_,k_,j]-float(fm['U1'](X,Y))), abs(out['U2'][p_,k_,j]-float(fm['U2'](X,Y))))/sc
        errU = max(errU, e)
        errp = max(errp, abs(out['psi'][p_,k_,j]-float(fm['psi'](X,Y)))/(sc*rr))
    print('grid', npan, q, M, 'time %.1fs'%tt, 'max|dU|/(1+r)^.5 = %.2e   max|dpsi|/(r(1+r)^.5) = %.2e' % (errU, errp))
    print('  a0 = %.14f  c_int = %.14f  c_lim = %.14f' % (s['a0'], s['c_int'], s['c_lim']))
