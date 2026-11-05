#!/usr/bin/env python3
"""FLOAT Gaussian partition screen of actual stream Wiener moments.

Actual radial point values use Arb. Gauss discretization, finite radius and
partition tails are UNCONTROLLED. This is not an upper certificate.
"""
import argparse
from collections import defaultdict
import json, math
from pathlib import Path
import sys,time
import numpy as np
from flint import arb,arb_series,ctx
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'coercivity_residual'))
from fields013 import Evaluator,derivative_series

def add(out,key,value):
    kind,n=key
    if n<0:n=-n;value=-value if kind=='s' else value
    if n==0 and kind=='s':return
    key=kind,n
    out[key]=out.get(key,0)+value

def coordinate(modes,rr,axis):
    out={}
    for (kind,n),p in modes.items():
        v=rr*p/2
        if axis=='x':
            add(out,(kind,n+1),v);add(out,(kind,n-1),v)
        elif kind=='c':
            add(out,('s',n+1),v);add(out,('s',n-1),-v)
        else:
            add(out,('c',n-1),v);add(out,('c',n+1),-v)
    return out

class Pricing:
    def __init__(self,precision=384,jmax=12,degree=7):
        self.e=Evaluator(precision,0,0);self.degree=degree;self.jmax=jmax
    def stream(self,r):
        degree=self.degree
        ps=self.e.potential_series(r,degree+2)
        rr=arb_series([r,1],prec=degree+1)
        rp=[rr**(-b) for b in range(3)];out={}
        for (kind,n),p in ps.items():
            i,j=(1,1) if kind=='c' else (1,0)
            pd=[p,p.derivative(),p.derivative().derivative()]
            for (a,b,N,t),v in derivative_series(kind,n,i,j).items():
                add(out,(t,N),arb(v)*pd[a]*rp[b])
        assert all(p.prec>=degree+1 for p in out.values())
        return rr,out
    def densities(self,r):
        rr,psi=self.stream(r)
        coords=[psi,coordinate(psi,rr,'x'),coordinate(psi,rr,'y')]
        coords.extend([coordinate(coords[1],rr,'x'),coordinate(coords[1],rr,'y'),coordinate(coords[2],rr,'y')])
        cuts=[arb_series([1],prec=self.degree+1),(-(rr*rr)).exp()]
        for j in range(self.jmax+1):
            R=arb(2)**j
            cuts.append((-(rr*rr)/(4*R*R)).exp()-(-(rr*rr)/(R*R)).exp())
        result=np.zeros((len(cuts),6,8))
        for ci,cut in enumerate(cuts):
            for ai,modes in enumerate(coords):
                for (kind,n),p in modes.items():
                    f=cut*p;angular=2*arb.pi() if n==0 else arb.pi()
                    for order in range(4):
                        # python-flint signed balls containing zero may return
                        # NaN for **2; multiplication has correct enclosure.
                        e0=f[0]*f[0]
                        e1=f[1]*f[1]+arb(n*n)*f[0]*f[0]/(r*r)
                        assert e0.is_finite() and e1.is_finite()
                        result[ci,ai,2*order]+=float((angular*r*e0).mid())
                        result[ci,ai,2*order+1]+=float((angular*r*e1).mid())
                        if order<3:f=f.derivative().derivative()+f.derivative()/rr-arb(n*n)*f/(rr*rr)
        assert np.isfinite(result).all()
        return result

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--nodes',type=int,default=96)
    ap.add_argument('--loglo',type=float,default=-7);ap.add_argument('--loghi',type=float,default=11)
    ap.add_argument('--jmax',type=int,default=12);ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();tick=time.monotonic();pr=Pricing(jmax=args.jmax)
    z,w=np.polynomial.legendre.leggauss(args.nodes)
    ys=(args.loghi+args.loglo)/2+(args.loghi-args.loglo)*z/2
    ws=w*(args.loghi-args.loglo)/2
    sums=np.zeros((args.jmax+3,6,8))
    points=[]
    for i,(y,ww) in enumerate(zip(ys,ws)):
        r=float(np.exp(y));den=pr.densities(arb(r));sums+=ww*r*den
        points.append({'r':r,'energies':den.tolist()})
        if (i+1)%4==0:print('point',i+1,'of',args.nodes,'seconds',round(time.monotonic()-tick,2),flush=True)
    # Integral-normalized Fourier moments by Cauchy-Schwarz with (lambda²+r²)^-2.
    mom=np.zeros((args.jmax+3,6,6))
    for m in range(6):
        mom[:,:,m]=np.sqrt((np.sqrt(np.maximum(sums[:,:,m]*sums[:,:,m+2],0))+sums[:,:,m+1])/(2*np.pi))
    fractional=mom[:,:,4]**.9*mom[:,:,5]**.1
    totals=mom[1:].sum(axis=0);frac=fractional[1:].sum(axis=0)
    partition_totals=totals.copy();partition_fractional=frac.copy()
    # For m>3+|alpha|-gamma all three global physical norms are finite.
    # Use their tighter unwindowed estimates only in this proved range.
    orders=[0,1,1,2,2,2]
    for ai,order in enumerate(orders):
        for m in range(6):
            if m>=3+order:totals[ai,m]=min(totals[ai,m],mom[0,ai,m])
        if order<=1:frac[ai]=min(frac[ai],fractional[0,ai])
    D=np.zeros((3,3));D[0,0]=2*(totals[0,4]+frac[0])
    for i in range(2):D[i+1,0]=D[0,i+1]=2*(20*(totals[0,3]+frac[0])+2*(totals[i+1,4]+frac[i+1]))
    for i in range(2):
        for j in range(2):
            ij=3 if i==j==0 else 5 if i==j==1 else 4
            D[i+1,j+1]=4*(60*(totals[0,2]+frac[0])+20*(totals[i+1,3]+frac[i+1]+totals[j+1,3]+frac[j+1])+2*(totals[ij,4]+frac[ij]))
    out={'status':'FLOAT_SCREEN_NOT_A_CERTIFICATE','uncontrolled':['Gauss discretization','origin tail','radius exterior','Gaussian partition tail'],
         'nodes':args.nodes,'log_interval':[args.loglo,args.loghi],'jmax':args.jmax,
         'physical_energies':sums.tolist(),'integer_moments_by_piece':mom.tolist(),
         'piece_zero':'unwindowed diagnostic; only eligible globally finite moments are used',
         'partition_integer_moment_totals':partition_totals.tolist(),'partition_fractional_4p1_totals':partition_fractional.tolist(),
         'fractional_4p1_by_piece':fractional.tolist(),'integer_moment_totals':totals.tolist(),'fractional_4p1_totals':frac.tolist(),
         'weighted_Schur_matrix':D.tolist(),'weighted_Schur_norm':float(np.linalg.norm(D,2)),
         'row_sum_bound':float(max(D.sum(axis=1))),'seconds':time.monotonic()-tick,'points':points}
    args.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['points','physical_energies','integer_moments_by_piece','fractional_4p1_by_piece']},indent=2))
if __name__=='__main__':main()
