"""Independent all-plane strain, exploratory Gaussian quadrature, no error certificate."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import argparse, json, time
from datetime import datetime,timezone
import numpy as np
from scipy.interpolate import BSpline
from x3_independent import X3,BASE

def run(nq,nt):
    x=X3();start=time.monotonic()
    v,w=np.polynomial.legendre.leggauss(nq)
    knots=np.unique(x.t)
    q=((knots[:-1,None]+knots[1:,None])/2+(knots[1:]-knots[:-1])[:,None]*v/2).ravel()
    qw=((knots[1:]-knots[:-1])[:,None]*w/2).ravel()
    a,aw=np.polynomial.legendre.leggauss(nt)
    theta=(a+1)*np.pi/4
    kernel=(np.pi/4)*aw*np.cos(theta)**2*np.sin(theta)*np.sin(3*theta)
    total=np.longdouble(0)
    for off in range(0,len(q),128):
        S=x.compact(q[off:off+128],theta)
        val=np.exp(S)@kernel
        total+=np.sum(qw[off:off+128]*val,dtype=np.longdouble)
    c=float(total*4*x.L*x.L/(np.pi*(1-x.k)))
    return dict(utc=datetime.now(timezone.utc).isoformat(),method='own de Boor; composite Gauss per exact knot span; compact all-plane density integral',certified=False,nq=nq,nt=nt,radial_points=len(q),c=c,canonical_cl=(1+c)/3,held_cl=1/x.k,normalization_defect=3/x.k-1-c,seconds=time.monotonic()-start)

def checks():
    x=X3();q=np.r_[0,np.linspace(0,1,37),np.unique(x.t)]
    own=x.deboor(q,x.t,x.co,x.spline_order)
    lib=BSpline(x.t,x.co,x.spline_order)(q)
    err=float(np.max(np.abs(own-lib)))
    own_d=x.deboor(q,x.t[1:-1],x.dco,x.spline_order-1)
    lib_d=BSpline(x.t,x.co,x.spline_order)(q,nu=1)
    derr=float(np.max(np.abs(own_d-lib_d)))
    ans={'utc':datetime.now(timezone.utc).isoformat(),'max_deboor_difference_scipy':err,'max_derivative_difference_scipy':derr,'max_spline_coefficient':float(np.max(np.abs(x.co))),'origin_spline_exact_zero':bool(np.all(own[0]==0)),'noncertified_check':True}
    print(json.dumps(ans),flush=True)
    assert err<1e-11 and derr<1e-7

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--nq',type=int);ap.add_argument('--nt',type=int);a=ap.parse_args()
    checks()
    configurations=[(a.nq,a.nt)] if a.nq else [(8,256),(12,384),(16,512),(24,768)]
    for nq,nt in configurations:print(json.dumps(run(nq,nt)),flush=True)
