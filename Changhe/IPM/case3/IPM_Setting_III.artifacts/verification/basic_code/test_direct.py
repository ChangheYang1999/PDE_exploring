import numpy as np, time, sys
sys.path.insert(0,'.')
import manufactured as mf, sympy as sp, mpmath as mp
from vdirect import DirectVelocity
mp.mp.dps=60
f, rho_s, psi_s = mf.lambdified(mf.DEFAULT_TERMS)
x,y=mf.x,mf.y
fm = {k: sp.lambdify((x,y), v, 'mpmath') for k,v in dict(U1=-sp.diff(psi_s,y), U2=sp.diff(psi_s,x)).items()}
def rho_fun(X,Y):
    X=np.asarray(X,float); Y=np.asarray(Y,float)
    with np.errstate(all='ignore'):
        out = np.array(f['rho'](X,Y), dtype=float)
    bad = ~np.isfinite(out)
    if bad.any():
        for i in zip(*np.where(bad)):
            out[i] = float(mp.re(sp.lambdify((x,y), rho_s, 'mpmath')(mp.mpf(X[i]), mp.mpf(Y[i]))))
    return out
for (H,q,Nth,tmax) in [(0.1,12,512,np.log(1e8)), (0.05,16,1024,np.log(1e12))]:
    t0=time.time()
    dv = DirectVelocity(rho_fun, H=H, q=q, Nth=Nth, tmax=tmax)
    print('setup %.1fs grid %d x %d'%(time.time()-t0, len(dv.r), Nth))
    for (X1,X2) in [(0.3,0.2),(1.0,0.0),(0.0,1.0),(2.0,-1.5),(10.,7.),(100.,3.),(0.01,0.02)]:
        t0=time.time()
        U1,U2,parts = dv.U(X1,X2, return_parts=True)
        e1 = float(fm['U1'](mp.mpf(X1),mp.mpf(X2))); e2=float(fm['U2'](mp.mpf(X1),mp.mpf(X2)))
        print('  X=(%g,%g): U=(%.12e, %.12e) exact (%.12e, %.12e) err (%.1e, %.1e) tail (%.1e,%.1e) %.1fs'%(X1,X2,U1,U2,e1,e2,U1-e1,U2-e2,parts['tail'][0],parts['tail'][1],time.time()-t0))
