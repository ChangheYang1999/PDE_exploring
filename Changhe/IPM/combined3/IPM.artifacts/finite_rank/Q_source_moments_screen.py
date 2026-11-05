#!/usr/bin/env python3
"""FLOAT radial quadrature of Candidate013 tame-source coefficient constants.

Exact-source Arb point fields are used. The outer Gauss quadrature, radial
truncation, and inferred suprema are not certificates.
"""
import argparse,json,sys,time,math,hashlib
from pathlib import Path
import numpy as np
from scipy.special import roots_legendre
from flint import arb,arb_series,ctx
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'coercivity_residual'))
sys.path.insert(0,str(HERE.parent/'operator_theory'))
from fields013 import Evaluator
from Ctr_wiener_moment_screen import coordinate

def norms(modes,r,maximum=4):
    rr=arb_series([r,1],prec=maximum+1);inv=rr**-1;inv2=inv*inv
    vals=[arb(0) for _ in range(maximum+1)]
    for (kind,n),f in modes.items():
        angular=2*arb.pi() if n==0 else arb.pi()
        cur=f
        for k in range(maximum//2+1):
            vals[2*k]+=angular*cur[0]*cur[0]
            if 2*k+1<=maximum:
                vals[2*k+1]+=angular*(cur[1]*cur[1]+(n/r)**2*cur[0]*cur[0])
            if 2*k+2<=maximum:
                cur=cur.derivative().derivative()+inv*cur.derivative()-n*n*inv2*cur
    assert all(v.is_finite() for v in vals)
    return np.array([float(v.mid()) for v in vals])

def constant(sig):
    return .5/(math.sqrt(math.cos(math.pi*sig/2))*(1-sig)**((1-sig)/4)*(1+sig)**((1+sig)/4))

def moment(D,m,sig):
    return constant(sig)*D[m]**((1-sig)/2)*D[m+2]**((1+sig)/2)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--nodes',type=int,default=128)
    ap.add_argument('--bits',type=int,default=512);ap.add_argument('--loglo',type=float,default=-12)
    ap.add_argument('--loghi',type=float,default=12);ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();ctx.prec=args.bits
    e=Evaluator(args.bits,max_density_order=2,max_velocity_order=-1)
    z,w=roots_legendre(args.nodes);ys=(args.loghi+args.loglo)/2+(args.loghi-args.loglo)*z/2
    ws=w*(args.loghi-args.loglo)/2
    total_b=np.zeros(5);total_xb=np.zeros(5);rows=[];H1=0;st=time.time()
    for j,(y,ww) in enumerate(zip(ys,ws)):
        rf=float(np.exp(y));r=arb(str(rf));md=e.modes_taylor(r,degree=4)
        rr=arb_series([r,1],prec=5);b=[md['rho',1,0],md['rho',0,1]]
        nb=sum((norms(mm,r) for mm in b),np.zeros(5))
        nxb=sum((norms(coordinate(mm,rr,ax),r) for mm in b for ax in ['x','y']),np.zeros(5))
        total_b+=ww*rf*rf*nb;total_xb+=ww*rf*rf*nxb
        # An angular l1 majorant at this sampled radius, not a supremum certificate.
        h=[]
        for ij in [(2,0),(1,1),(0,2)]:
            h.append(sum(float(abs(v[0]).upper()) for v in md['rho',*ij].values()))
        Hsample=math.sqrt(1+4*rf*rf)*math.sqrt(h[0]**2+2*h[1]**2+h[2]**2)
        H1=max(H1,Hsample)
        rows.append({'r':rf,'H1_angular_l1_at_point':Hsample,'b_radial_energy':nb.tolist(),'xb_radial_energy':nxb.tolist()})
        if (j+1)%8==0:
            args.output.with_suffix('.checkpoint.float.json').write_text(json.dumps({'status':'FLOAT_PARTIAL_NOT_CERTIFICATE','completed':j+1,'rows':rows},indent=2)+'\n')
            print('point',j+1,'of',args.nodes,'seconds',round(time.time()-st,2),flush=True)
    Db=np.sqrt(total_b);Dxb=np.sqrt(total_xb)
    A={}
    for sig in [0,.1]:
        A[str(2+sig)]=moment(Db,2,sig)+2*moment(Dxb,2,sig)+4*moment(Db,1,sig)
    ratio=3.813e-7/.387
    parts=[2.1*H1*ratio**(1/2.1),1.155*A['2']*ratio**(1-.1/2.1),1.155*A['2.1']*ratio]
    out={'status':'FLOAT_SCREEN_NOT_A_CERTIFICATE','nodes':args.nodes,'bits_at_point_values':args.bits,'log_radial_interval':[args.loglo,args.loghi],'D_b':Db.tolist(),'D_xb':Dxb.tolist(),'H1_sampled_angular_l1_majorant':H1,'A_s':A,'test_R_over_M':ratio,'tame_rate_parts':parts,'tame_rate_sum':sum(parts),'elapsed_seconds':time.time()-st,'warning':'Radial quadrature and truncation uncontrolled; sampled supremum is not a uniform bound. No energy closure or existence claimed.','rows':rows,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    args.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2),flush=True)

if __name__=='__main__':main()
