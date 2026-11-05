#!/usr/bin/env python3
"""Certified Gram majorants for smooth algebraic S1 multipole test functions.

phi_l=r^l sin(l theta)*(L²+r²)^(-(l+tau)/2), l odd,tau>2.
The functions need not be Schwartz: WJ^q phi_l belongs toL2, so the finite-rank
low-order pairing follows by smooth cutoff approximation in weightedH3.
"""
import argparse,json,math
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
from flint import arb,ctx


def aq(q):q=Q(q);return arb(q.numerator)/q.denominator

def clean(p):return {k:v for k,v in p.items()if v}
def put(out,key,v):
 p,nu,n,kind=key
 if n<0:n=-n;v=-v if kind=='s' else v
 if kind=='s' and n==0:return
 key=p,nu,n,kind;out[key]=out.get(key,Q(0))+v


def diff(poly,axis):
 out={}
 for (p,nu,n,kind),v in poly.items():
  # homogeneous derivative of r^p trig(n theta)
  if axis==0:
   put(out,(p-1,nu,n+1,kind),v*(p-n)/2);put(out,(p-1,nu,n-1,kind),v*(p+n)/2)
  elif kind=='s':
   put(out,(p-1,nu,n-1,'c'),v*(p+n)/2);put(out,(p-1,nu,n+1,'c'),v*(n-p)/2)
  else:
   put(out,(p-1,nu,n+1,'s'),v*(p-n)/2);put(out,(p-1,nu,n-1,'s'),-v*(p+n)/2)
  # radial derivative of (L²+r²)^-nu multiplied by cos/sin theta
  vv=-nu*v
  if axis==0:
   put(out,(p+1,nu+1,n+1,kind),vv);put(out,(p+1,nu+1,n-1,kind),vv)
  elif kind=='s':
   put(out,(p+1,nu+1,n-1,'c'),vv);put(out,(p+1,nu+1,n+1,'c'),-vv)
  else:
   put(out,(p+1,nu+1,n+1,'s'),vv);put(out,(p+1,nu+1,n-1,'s'),vv)
 return clean(out)


def coordinate(poly,axis):
 out={}
 for (p,nu,n,kind),v in poly.items():
  if axis==0:
   put(out,(p+1,nu,n+1,kind),v/2);put(out,(p+1,nu,n-1,kind),v/2)
  elif kind=='s':
   put(out,(p+1,nu,n-1,'c'),v/2);put(out,(p+1,nu,n+1,'c'),-v/2)
  else:
   put(out,(p+1,nu,n+1,'s'),v/2);put(out,(p+1,nu,n-1,'s'),v/2)
 return clean(out)


class Integrals:
 def __init__(self,L):self.L=Q(L)
 @lru_cache(None)
 def radial(self,p,nu):
  A=Q(p+2,2);assert A>0 and nu-A>0,(p,nu,A)
  return aq(self.L)**aq(p+2-2*nu)*aq(A).gamma()*aq(nu-A).gamma()/(2*aq(nu).gamma())
 def inner(self,f,g):
  z=arb(0)
  for (p,nu,n,kind),v in f.items():
   for (pp,nunu,nn,kk),vv in g.items():
    if nn!=n or kk!=kind:continue
    z+=aq(v*vv)*arb.pi()*(2 if n==0 else 1)*self.radial(p+pp,nu+nunu)
  return z
 def H3sq(self,f):
  z=arb(0)
  for d in range(4):
   for i in range(d+1):
    g=f
    for axis in [0]*i+[1]*(d-i):g=diff(g,axis)
    z+=math.comb(3,d)*math.comb(d,i)*self.inner(g,g)
  return z


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--L',default='32');ap.add_argument('--tau',default=None);ap.add_argument('--max-mode',type=int,default=23);ap.add_argument('--bits',type=int,default=256);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
 ctx.prec=args.bits;c=Q(4076476460239181,2251799813685248);gamma=1-1/c;tau=Q(args.tau)if args.tau else 2+gamma;assert tau>2
 I=Integrals(args.L);q=Q(21,10);rows=[]
 for l in range(1,args.max_mode+1,2):
  phi={(l,(l+tau)/2,l,'s'):Q(1)}
  H=I.H3sq(phi);X=sum((I.H3sq(coordinate(phi,j)) for j in range(2)),arb(0))
  Bup=(1+8*aq(q)**2)*H+8*X
  rows.append({'l':l,'L2_norm_squared':I.inner(phi,phi).str(60),'H3_norm_squared':H.str(60),'coordinate_H3_sum':X.str(60),'Bqq_diagonal_upper':Bup.str(60)})
 out={'status':'RIGOROUS_PSD_GRAM_MAJORANT','q':str(q),'gamma':str(gamma),'tau':str(tau),'L':args.L,'basis':'phi_l=r^l sin(l theta)*(L²+r²)^(-(l+tau)/2), l odd','B_bound':'Bqq <= diagonal(Bqq_diagonal_upper), since rotations make all distinct-l cross entries exactly zero','proof':'Bqq(phi)<= (1+8q²)||J³phi||²+8 sum_j||J³(x_j phi)||²; polar derivatives rational, radial pairings exact beta integrals','rows':rows,'bits':args.bits,'warning':'No profile-dependent finite-rank A or operator-tail bound is asserted by this Gram computation alone.'}
 args.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
