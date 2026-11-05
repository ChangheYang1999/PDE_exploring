"""Local residual projections for the full-matrix Riesz dual estimate.

For normalized S1 Gaussians psi_a=sqrt(2)*y/(sqrt(pi)*a²)*exp(-r²/2a²),
Phi_a=R J^(-1/10)psi_a and H=J^(21/10)(WF), one has exactly
<RH,Phi_a>=<WF,(1-Delta)psi_a>.  The last integral needs only F's
sine-one mode; no pointwise substitution for a Riesz transform is made.
"""
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime,timezone
from pathlib import Path
import argparse,json,math,time
import numpy as np
from flint import arb
from fields013 import Evaluator,C,SOURCE_HASHES

E=None
def sine_coefficient(kind,n,typ,m,target):
    """Exact coefficient of sin(target*theta) in one product of trig modes."""
    if kind==typ:return 0
    # sin(n)*cos(m) = [sin(n+m)+sin(n-m)]/2.
    if kind=='c':n,m=m,n
    out=0
    for nn in [n+m,n-m]:
        if nn==target:out+=.5
        if nn==-target:out-=.5
    return out

def sine_product(A,B,target=1,absolute=False):
    out=arb(0)
    for (kind,n),a in A.items():
        for (typ,m),b in B.items():
            if kind==typ or (abs(n-m)!=target and n+m!=target):continue
            coeff=sine_coefficient(kind,n,typ,m,target)
            if coeff:out+=(abs(coeff)if absolute else coeff)*a*b
    return out

def residual_mode(modes,r,target=1):
    rx,ry=modes['rho',1,0],modes['rho',0,1]
    u1,u2=modes['u1',0,0],modes['u2',0,0]
    dil=sine_product({('c',1):arb(1)},rx,target)+sine_product({('s',1):arb(1)},ry,target)
    return arb(C)*r*dil+sine_product(u1,rx,target)+sine_product(u2,ry,target)-modes['rho',0,0].get(('s',target),arb(0))

def initialize(precision):
    global E
    E=Evaluator(precision,max_density_order=1,max_velocity_order=0)

def row(r):
    modes=E.modes_at(str(r));f=residual_mode(modes,arb(str(r)))
    return float(r),float(f.mid()),float(f.rad())

def float_run(args):
    xx,ww=np.polynomial.legendre.leggauss(args.order);r=(xx+1)*args.radius/2;weights=ww*args.radius/2
    tick=time.monotonic()
    with ProcessPoolExecutor(args.workers,initializer=initialize,initargs=(args.precision,))as pool:
        rows=list(pool.map(row,r,chunksize=1))
    fv=np.array([rr[1]for rr in rows]);widths=[float(a)for a in args.widths.split(',')]
    cs=[]
    for a in widths:
        test=math.sqrt(2*math.pi)/a**2*np.sqrt(1+4*r*r)*r*r*np.exp(-r*r/(2*a*a))*(1+4/a**2-r*r/a**4)
        cs.append(float(np.dot(weights,fv*test)))
    out={'status':'FLOAT_QUADRATURE_ONLY','source_hashes':SOURCE_HASHES,'precision':args.precision,'order':args.order,'integration_radius':args.radius,'widths':widths,'c_values':cs,'max_radial_roundoff':max(rr[2]for rr in rows),'elapsed_seconds':time.monotonic()-tick,'finished_utc':datetime.now(timezone.utc).isoformat(),'rows':rows,'open_errors':['quadrature discretization','omitted radial tails','whole-matrix inverse Gram enclosure']}
    args.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='rows'},indent=2),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--order',type=int,default=512);p.add_argument('--radius',type=float,default=3.2);p.add_argument('--widths',default='.1,.2,.4');p.add_argument('--workers',type=int,default=2);p.add_argument('--precision',type=int,default=384);p.add_argument('--out',type=Path,required=True);float_run(p.parse_args())
