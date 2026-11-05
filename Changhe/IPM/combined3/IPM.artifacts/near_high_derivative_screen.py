#!/usr/bin/env python3
"""FLOAT radial quadrature of actual high near-coefficient derivative norms.

Purpose: choose a better Fourier-tail derivative order than inherited m=6.
Fields at each radius are enclosed by exact-source Arb power series; the
outer Gauss quadrature and all reported norms/tails are explicitly FLOAT.
"""
import argparse
from datetime import datetime, timezone
from hashlib import sha256
import json
import math
from pathlib import Path
import sys
import time

sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'coercivity_residual'))
import numpy as np
from scipy.special import roots_legendre
from flint import arb,arb_series,ctx
from fields013 import Evaluator, derivative_series, rational_arb, C, SOURCE_HASHES

def coefficient_modes(e,r,degree):
    ps=e.potential_series(r,degree+2)
    rr=arb_series([r,1],prec=degree+1)
    powers={b:rr**(-b) for b in range(3)}
    udot={}
    for (kind,n),pol in ps.items():
        di,dj=(1,1) if kind=='c' else (1,0)
        for (a,b,N,t),v in derivative_series(kind,n,di,dj).items():
            if N==0:continue
            pp=pol
            for _ in range(a):pp=pp.derivative()
            # udotX=-d_theta psi, psi=chi_xy for base and phi_x for correction.
            dest=('s',N) if t=='c' else ('c',N)
            factor=v*N*(1 if t=='c' else -1)
            value=arb(factor)*pp*powers[b]
            udot[dest]=udot.get(dest,arb_series([],prec=degree+1))+value
    ell=arb(8).log()/(2*arb.pi().sqrt())
    cut=((rr/arb(8).sqrt()).log()/ell).erfc()/2
    core=rational_arb(C)/(1+4*rr*rr)
    an={k:cut*4*p/(1+4*rr*rr) for k,p in udot.items()}
    an['c',0]=an.get(('c',0),arb_series([],prec=degree+1))-cut*core
    ar=dict(an);ar['c',0]+=core
    return an,ar

def radial_norm_squares(modes,r,maximum):
    rr=arb_series([r,1],prec=maximum+1);inv=rr**(-1);inv2=rr**(-2)
    norms={m:arb(0) for m in range(maximum+1)}
    for (kind,n),p in modes.items():
        angular=2*arb.pi() if n==0 else arb.pi()
        current=p
        for k in range(maximum//2+1):
            v=current[0]
            norms[2*k]+=angular*v*v
            if 2*k+1<=maximum:
                norms[2*k+1]+=angular*(current[1]**2+(arb(n)/r)**2*v*v)
            if 2*k+2<=maximum:
                current=current.derivative().derivative()+inv*current.derivative()-n*n*inv2*current
    return {m:float(v.mid()) for m,v in norms.items()}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--nodes',type=int,default=256)
    ap.add_argument('--maximum',type=int,default=16);ap.add_argument('--bits',type=int,default=512)
    ap.add_argument('--log-rmin',type=float,default=-10.);ap.add_argument('--log-rmax',type=float,default=6.)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();ctx.prec=args.bits
    e=Evaluator(args.bits,max_density_order=-1,max_velocity_order=-1)
    xs,ws=roots_legendre(args.nodes);half=(args.log_rmax-args.log_rmin)/2;mid=(args.log_rmax+args.log_rmin)/2
    totals={'an':np.zeros(args.maximum+1),'ar':np.zeros(args.maximum+1)}
    rows=[];start=time.monotonic()
    for j,(x,w) in enumerate(zip(xs,ws)):
        t=mid+half*x;r=float(np.exp(t))
        an,ar=coefficient_modes(e,arb(str(r)),args.maximum)
        item={'r':r,'weight_log':float(w*half)}
        for name,modes in [('an',an),('ar',ar)]:
            d=radial_norm_squares(modes,arb(str(r)),args.maximum)
            vals=np.array([d[k] for k in range(args.maximum+1)])
            totals[name]+=float(w*half)*r*r*vals
            item[name]=vals.tolist()
        rows.append(item)
        if (j+1)%16==0:
            args.output.with_suffix('.checkpoint.float.json').write_text(json.dumps({'status':'FLOAT_PARTIAL_NOT_CERTIFICATE','nodes_completed':j+1,'rows':rows},indent=2)+'\n')
            print('nodes',j+1,'of',args.nodes,'seconds',time.monotonic()-start,flush=True)
    norms={name:np.sqrt(v).tolist() for name,v in totals.items()}
    tails=[];q=2.1
    for mu in [40,48,56,60,64,68,72]:
        for m in range(4,args.maximum+1):
            if m<=q+1:continue
            dm=norms['ar'][m]
            tail=lambda v: v**(q-m+1)*dm/math.sqrt(4*math.pi*(m-q-1))
            tails.append({'mu':mu,'order':m,'D_m_ar':dm,'tail_B_ar':(4/3)**q*tail(3*mu/4)+(8/mu)**q*tail(mu/2)})
    result={'status':'FLOAT_NOT_CERTIFICATE','source_hashes':SOURCE_HASHES,'program_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'nodes':args.nodes,'maximum_order':args.maximum,'bits_at_point_fields':args.bits,
        'log_radial_range':[args.log_rmin,args.log_rmax],'D_m':norms,'tail_screens':tails,
        'best_tail_by_mu':{str(mu):min([r for r in tails if r['mu']==mu],key=lambda z:z['tail_B_ar']) for mu in [40,48,56,60,64,68,72]},
        'elapsed_seconds':time.monotonic()-start,'finished_utc':datetime.now(timezone.utc).isoformat(),
        'warning':'Radial quadrature/truncation and arithmetic after point-field enclosure are not certified.'}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['tail_screens']},indent=2),flush=True)

if __name__=='__main__':main()
