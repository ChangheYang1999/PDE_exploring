"""Exact-source modal H² residual and Gaussian-Laguerre projection screen.

Arb Taylor coefficients and Acb polynomial convolutions resolve cancellation
before conversion to binary64.  Radial quadrature/projections remain FLOAT.
"""
import argparse,json,math,time
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime,timezone
from pathlib import Path
import numpy as np
from scipy.special import eval_genlaguerre,gammaln
from flint import arb,acb,acb_poly,arb_series
from fields013 import Evaluator,C,SOURCE_HASHES

E=None
SHIFT=164
def initialize(precision):
    global E
    E=Evaluator(precision,max_density_order=1,max_velocity_order=0)

def fourier_poly(modes,k):
    out=[acb(0)for _ in range(2*SHIFT+1)]
    for (kind,n),p in modes.items():
        a=p[k]
        if kind=='c':out[SHIFT+n]+=a/2;out[SHIFT-n]+=a/2
        else:out[SHIFT+n]+=acb(0,-a/2);out[SHIFT-n]+=acb(0,a/2)
    return acb_poly(out)

def residual_jets(r,degree=2):
    r=arb(r);fields=E.modes_taylor(r,degree)
    v1=dict(fields['u1',0,0]);v2=dict(fields['u2',0,0]);rr=arb_series([r,1],prec=degree+1)
    v1['c',1]=v1.get(('c',1),arb_series([],prec=degree+1))+arb(C)*rr
    v2['s',1]=v2.get(('s',1),arb_series([],prec=degree+1))+arb(C)*rr
    A=[fourier_poly(v1,k)for k in range(degree+1)];B=[fourier_poly(fields['rho',1,0],k)for k in range(degree+1)]
    D=[fourier_poly(v2,k)for k in range(degree+1)];F=[fourier_poly(fields['rho',0,1],k)for k in range(degree+1)]
    rho=[fourier_poly(fields['rho',0,0],k).left_shift(SHIFT)for k in range(degree+1)]
    return [sum((A[i]*B[k-i]+D[i]*F[k-i]for i in range(k+1)),acb_poly())-rho[k]for k in range(degree+1)]

def row(task):
    r,weight=task;r=float(r);jets=residual_jets(str(r),2)
    odd=list(range(1,2*SHIFT,2));f=[[],[],[]];error=0.
    for k in range(3):
        for n in odd:
            v=-2*jets[k][2*SHIFT+n].imag*math.factorial(k)
            f[k].append(float(v.mid()));error=max(error,float(v.rad()))
    f0,f1,f2=map(np.array,f);ns=np.array(odd)
    W=math.sqrt(1+4*r*r);Wp=4*r/W;Wpp=4/W-16*r*r/W**3
    weighted=W*f0;v=weighted-(W*f2+2*Wp*f1+Wpp*f0)-(W*f1+Wp*f0)/r+ns**2*weighted/r**2
    return {'r':r,'weight':float(weight),'F':f0.tolist(),'Fr':f1.tolist(),'Frr':f2.tolist(),'V':v.tolist(),'radial_roundoff':error}

def run(args):
    lo,hi=math.log(args.rmin),math.log(args.rmax);edges=np.linspace(lo,hi,math.ceil((hi-lo)/args.logstep)+1)
    x,w=np.polynomial.legendre.leggauss(args.order);tasks=[]
    for a,b in zip(edges[:-1],edges[1:]):
        ss=(a+b)/2+(b-a)/2*x;rr=np.exp(ss);ww=(b-a)/2*w*rr # dr weights
        tasks.extend(zip(rr,ww))
    start=time.monotonic();rows=[]
    with ProcessPoolExecutor(args.workers,initializer=initialize,initargs=(args.precision,))as pool:
        for result in pool.map(row,tasks,chunksize=1):
            rows.append(result)
            if len(rows)%64==0:print('rows',len(rows),'/',len(tasks),'seconds',time.monotonic()-start,flush=True)
    rr=np.array([r['r']for r in rows]);ww=np.array([r['weight']for r in rows]);VV=np.array([r['V']for r in rows]);ns=np.arange(1,2*SHIFT,2)
    energy=math.pi*np.sum(ww[:,None]*rr[:,None]*VV*VV,axis=0)
    widths=np.geomspace(args.width_min,args.width_max,args.width_count);best=[]
    for m in ns[ns<=args.max_angular]:
        vm=VV[:,int((m-1)/2)]
        for a in widths:
            s=rr*rr/a**2
            for k in range(args.max_radial+1):
                logc=.5*(math.log(2/math.pi)+gammaln(k+1)-gammaln(k+m+1))-(m+1)*math.log(a)
                profile=np.exp(logc+m*np.log(rr)-s/2)*eval_genlaguerre(k,int(m),s)
                c=float(math.pi*np.dot(ww*rr,vm*profile))
                best.append({'m':int(m),'k':k,'width':float(a),'c':c,'captured_H2_energy':c*c})
    best.sort(key=lambda r:r['captured_H2_energy'],reverse=True)
    out={'status':'FLOAT_RADIAL_QUADRATURE_ONLY','source_hashes':SOURCE_HASHES,'r_range':[args.rmin,args.rmax],'logstep':args.logstep,'order':args.order,'rows_count':len(rows),'modal_H2_energy':[{'m':int(m),'energy':float(v)}for m,v in zip(ns,energy)],'H2_norm_screen':float(np.sqrt(energy.sum())),'best_projections':best[:100],'elapsed_seconds':time.monotonic()-start,'finished_utc':datetime.now(timezone.utc).isoformat(),'rows':rows,'open_errors':['radial quadrature','origin/exterior tails','Gaussian projection norm and fractional residual tail']}
    args.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in ['rows','modal_H2_energy','best_projections']},indent=2),flush=True);print('top modes',sorted(out['modal_H2_energy'],key=lambda r:r['energy'],reverse=True)[:12],flush=True);print('best projections',best[:12],flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--rmin',type=float,default=1e-5);p.add_argument('--rmax',type=float,default=64);p.add_argument('--logstep',type=float,default=.3);p.add_argument('--order',type=int,default=16);p.add_argument('--workers',type=int,default=4);p.add_argument('--precision',type=int,default=384);p.add_argument('--width-min',type=float,default=.015);p.add_argument('--width-max',type=float,default=1);p.add_argument('--width-count',type=int,default=20);p.add_argument('--max-angular',type=int,default=81);p.add_argument('--max-radial',type=int,default=40);p.add_argument('--out',type=Path,required=True);run(p.parse_args())
