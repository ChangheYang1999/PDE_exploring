#!/usr/bin/env python3
"""Rigorous real-radial enclosures for Phi=R J^-0.1 psi_cubic.

Physical widtha=3/200. Heat substitutiont=z20; z∈[0,2].
Uniform Bernstein-ellipse Gaussian error plus real Arb nodes/weights.
"""
import argparse,json,time
from pathlib import Path
from fractions import Fraction as Q
from flint import arb,ctx


def aq(x):x=Q(x);return arb(x.numerator)/x.denominator


class CubicHeat:
 def __init__(self,width='3/200',rmax='31/100',nodes=768,bits=256):
  ctx.prec=bits;self.bits=bits;self.a=aq(width);self.rmax=aq(rmax);self.nodes=nodes
  a=self.a;a2=a*a;a4=a2*a2;rt2=arb(2).sqrt();b=arb(1)/25
  m=(arb(3)**2/25+b*b)**10 # .6²+.04², power10
  self.Dmin=a2-2*m;assert self.Dmin>0
  assert 20*(b/(arb(3)/5)).atan()<arb.pi()/2
  rho=b+(1+b*b).sqrt();w=self.rmax**2/(2*self.Dmin)
  M0=(a2/rt2*self.Dmin**(-arb(3)/2)*(1+arb(3)/4*w)
      +3*a4/(2*rt2)*self.Dmin**(-arb(5)/2)*(1+arb(5)/3*w+arb(35)/96*w*w))
  M2=(3*a2*self.rmax**2/(8*rt2)*self.Dmin**(-arb(5)/2)
      +15*a4*self.rmax**2/(16*rt2)*self.Dmin**(-arb(7)/2)*(1+arb(7)/24*w))
  M=M0 if M0>M2 else M2
  M*=m.exp()/(arb(21)/20).gamma()
  self.gauss_error=8*M*rho**(-2*nodes)/(1-1/rho)
  self.tail_error=(-arb(2)**20).exp()
  T=arb(2)**20;D=a2+2*T;wt=self.rmax**2/(2*D)
  # Positive real-argument majorants of the exact mode formulas, monotone for t>=T.
  tm0=a2/rt2*D**(-arb(3)/2)*(1+arb(3)/4*wt)+3*a4/(2*rt2)*D**(-arb(5)/2)*(1+arb(5)/3*wt+arb(35)/96*wt*wt)
  tm2=3*a2*self.rmax**2/(8*rt2)*D**(-arb(5)/2)+15*a4*self.rmax**2/(16*rt2)*D**(-arb(7)/2)*(1+arb(7)/24*wt)
  assert tm0<1 and tm2<1 and (arb(1)/20).gamma()>1
  self.error=(self.gauss_error+self.tail_error).abs_upper()
  self.prepared=[]
  for j in range(nodes):
   z,weight=arb.legendre_p_root(nodes,j,weight=True);z+=1;t=z**20;D=a2+2*t
   ww=weight*(-t).exp()/(arb(21)/20).gamma()
   c0a=-a2/rt2*D**(-arb(3)/2)*ww
   c0b=3*a4/(2*rt2)*D**(-arb(5)/2)*ww
   c2a=3*a2/(8*rt2)*D**(-arb(5)/2)*ww
   c2b=-15*a4/(16*rt2)*D**(-arb(7)/2)*ww
   self.prepared.append((-1/(2*D),c0a,c0b,c2a,c2b))
  self.metadata={'status':'RIGOROUS_UNIFORM_HEAT_VECTOR_ENCLOSURE','width':str(width),'rmax':str(rmax),'nodes':nodes,'bits':bits,'ellipse_semiminor':'1/25','ellipse_rho':rho.str(30),'Dmin':self.Dmin.str(30),'uniform_Gauss_error':self.gauss_error.str(60),'heat_tail_error':self.tail_error.str(20)}
 def modes(self,r):
  ctx.prec=self.bits;r=arb(r);assert r>=0 and r<=self.rmax
  rr=r*r;c0=arb(0);c2=arb(0)
  for fac,aa,bb,cc,dd in self.prepared:
   x=fac*rr
   c0+=aa*x.hypgeom_1f1(arb(3)/2,1)+bb*x.hypgeom_1f1(arb(5)/2,1)
   c2+=rr*(cc*x.hypgeom_1f1(arb(5)/2,3)+dd*x.hypgeom_1f1(arb(7)/2,3))
  c0+=arb(0,self.error);c2+=arb(0,self.error)
  return {('r1','s',2):c2,('r2','c',0):c0,('r2','c',2):-c2}


if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--nodes',type=int,default=768);ap.add_argument('--bits',type=int,default=256);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
 st=time.time();h=CubicHeat(nodes=args.nodes,bits=args.bits);print('prepared',time.time()-st,flush=True)
 rows=[]
 for r in ['0','.001','.015','.03','.1','.3']:
  tick=time.time();z=h.modes(r);rows.append({'r':r,'modes':{str(k):v.str(50)for k,v in z.items()},'seconds':time.time()-tick});print(r,rows[-1]['modes'],'seconds',rows[-1]['seconds'],flush=True)
 out={**h.metadata,'checks':rows,'elapsed_seconds':time.time()-st};args.output.write_text(json.dumps(out,indent=2)+'\n')
