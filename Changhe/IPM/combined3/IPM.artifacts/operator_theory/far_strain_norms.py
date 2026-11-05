#!/usr/bin/env python3
"""Actual-source far-strain radial norms. Initial Gauss screen is FLOAT only.

Point evaluations use Arb. The --screen quadrature has no discretization/tail
certificate and is labeled accordingly. All outputs are new combined3 files.
"""
import argparse
from collections import defaultdict
import json
from pathlib import Path
import sys
import time
import numpy as np
from flint import arb,arb_series,ctx

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'coercivity_residual'))
from fields013 import Evaluator

class FarStrain:
    def __init__(self,precision=384,strain_scale='1'):
        self.e=Evaluator(precision,0,1)
        self.precision=precision
        self.strain_scale=arb(strain_scale)
        assert self.strain_scale>0
    def strain_series(self,r,degree=4):
        m=self.e.modes_taylor(arb(r),degree=degree)
        rr=arb_series([arb(r),1],prec=degree+1)
        ell=arb(8).log()/(2*arb.pi().sqrt())
        # 1-chi = erfc(-log(r/sqrt8)/ell)/2, avoiding subtraction.
        farcut=(-((rr/(self.strain_scale*arb(8).sqrt())).log()/ell)).erfc()/2
        out=[]
        xx={k:farcut*p for k,p in m['u1',1,0].items()}
        keys=m['u1',0,1].keys()|m['u2',1,0].keys()
        xy={k:farcut*(m['u1',0,1].get(k,arb_series([],prec=degree+1))+m['u2',1,0].get(k,arb_series([],prec=degree+1)))/2 for k in keys}
        # div u=0 => S22=-S11, so both independent entries carry factor two.
        assert all(f.prec>=degree+1 for modes in [xx,xy] for f in modes.values())
        return rr,[xx,xy]
    @staticmethod
    def lap(f,rr,n):
        return f.derivative().derivative()+f.derivative()/rr-arb(n*n)*f/(rr*rr)
    def densities(self,r):
        r=arb(r);rr,entries=self.strain_series(r)
        values=[arb(0),arb(0),arb(0)]
        for modes in entries:
            for (kind,n),f in modes.items():
                if kind=='s' and n==0:continue
                angular=2*arb.pi() if n==0 else arb.pi()
                assert f.prec>=5
                lf=self.lap(f,rr,n);llf=self.lap(lf,rr,n)
                assert lf.prec>=3 and llf.prec>=1
                vals=[lf[0]**2,lf[1]**2+arb(n*n)*lf[0]**2/(r*r),llf[0]**2]
                for j in range(3):values[j]+=2*angular*r*vals[j]
        return values

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--screen',action='store_true')
    ap.add_argument('--nodes',type=int,default=96);ap.add_argument('--loglo',type=float,default=-2)
    ap.add_argument('--loghi',type=float,default=6);ap.add_argument('--precision',type=int,default=384)
    ap.add_argument('--output',type=Path);ap.add_argument('--point',default=None)
    ap.add_argument('--strain-scale',default='1')
    args=ap.parse_args();tick=time.monotonic();fs=FarStrain(args.precision,args.strain_scale)
    if args.point:
        ds=fs.densities(args.point);print(json.dumps({'r':args.point,'densities_arb':[str(v) for v in ds],'status':'POINT_EVALUATION_ONLY'},indent=2));return
    assert args.screen
    z,w=np.polynomial.legendre.leggauss(args.nodes);ys=(args.loghi+args.loglo)/2+(args.loghi-args.loglo)*z/2
    ws=w*(args.loghi-args.loglo)/2
    sums=np.zeros(3);largest_rad=0.
    points=[]
    for i,(y,ww) in enumerate(zip(ys,ws)):
        r=float(np.exp(y));vs=fs.densities(arb(r));vals=np.array([float(v.mid()) for v in vs])
        largest_rad=max(largest_rad,max(float(v.rad()) for v in vs))
        sums+=ww*r*vals
        points.append({'r':r,'density_mid':[float(v.mid()) for v in vs],'density_arb':[str(v) for v in vs]})
        if (i+1)%8==0:print('progress',i+1,'of',args.nodes,'elapsed',round(time.monotonic()-tick,2),flush=True)
    d=np.sqrt(sums);moment=float(np.sqrt((d[0]*d[2]+d[1]**2)/(2*np.pi)))
    out={'status':'FLOAT_GAUSS_SCREEN_NOT_A_CERTIFICATE','nodes':args.nodes,'log_interval':[args.loglo,args.loghi],
         'strain_scale':args.strain_scale,
         'D2_D3_D4_screen':d.tolist(),'M2_majorant_screen':moment,'TIS_p_damping_price_screen':21/20*moment,
         'point_interval_max_radius':largest_rad,'uncontrolled_errors':['quadrature discretization','origin tail','exterior tail'],
         'elapsed_seconds':time.monotonic()-tick,'points':points}
    if args.output:args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='points'},indent=2))
if __name__=='__main__':main()
