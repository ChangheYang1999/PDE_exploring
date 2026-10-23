"""Exact polynomial primitive and independent multiprecision radial inversion.
Proof: research/hydrostatic_axis_primitive/PROOF.md. No producer imports.
"""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
import gmpy2
import mpmath as mp
from functools import lru_cache
from fractions import Fraction
Q=gmpy2.mpq

def exact(v):
 if isinstance(v,Q):return v
 if isinstance(v,Fraction):return Q(v.numerator,v.denominator)
 n,d=float(v).as_integer_ratio();return Q(n,d)

def add(a,b):
 out=[Q(0)]*max(len(a),len(b))
 for i,v in enumerate(a):out[i]+=v
 for i,v in enumerate(b):out[i]+=v
 return out

def linear(a,c0,c1):
 out=[Q(0)]*(len(a)+1)
 for n,v in enumerate(a):
  out[n]+=c0*v
  if n==0:out[1]+=c1*v
  else:out[n-1]+=c1*v/2;out[n+1]+=c1*v/2
 return out

def scale(a,c):return[c*v for v in a]
def endpoint(a,sign):return sum((v*sign**n for n,v in enumerate(a)),Q(0))
def integral(a):
 out=[Q(0)]*(len(a)+1)
 for n,v in enumerate(a):
  if n==0:out[1]+=v
  elif n==1:out[2]+=v/4
  else:out[n+1]+=v/(2*(n+1));out[n-1]-=v/(2*(n-1))
 out[0]-=endpoint(out,-1)
 return out

def derivative(a):
 if len(a)<2:return[Q(0)]
 out=[Q(0)]*(len(a)-1)
 # T_n'=n U_{n-1}; U_even=1+2(T2+...), U_odd=2(T1+...).
 for n,v in enumerate(a[1:],1):
  for j in range(n-1,-1,-2):out[j]+=n*v*(1 if j==0 else 2)
 return out

def equal(a,b):return all(v==0 for v in add(a,scale(b,-1)))

def primitive(coeff,P):
 P=exact(P);H=[Q(0)];D=[Q(0)]
 for k,row in enumerate(coeff):
  p=list(map(exact,row))
  for j in range(k):p=linear(p,Q(1,2),Q(1,2))
  H=add(H,scale(linear(p,Q(1,2),Q(-1,2)),(-1)**k))
  if k:
   z=list(map(exact,row))
   for j in range(k-1):z=linear(z,Q(1,2),Q(1,2))
   z=linear(z,(1+2*P)/2,(2*P-1)/2)
   D=add(D,scale(z,k*k*(-1)**k))
 J=integral(D);K=add(scale(H,-1),J);K[0]-=endpoint(J,1)
 a=endpoint(list(map(exact,coeff[0])),-1);cH=-a-endpoint(J,1)
 assert equal(derivative(J),D)
 assert endpoint(J,-1)==0 and endpoint(K,1)==0 and endpoint(K,-1)==cH
 return dict(H=H,D=D,J=J,K=K,cH=cH,a=a)

def mnum(v):
 v=exact(v);return mp.mpf(int(v.numerator))/int(v.denominator)

def evaluate(a,t):
 b1=mp.mpf(0);b2=mp.mpf(0)
 for v in a[:0:-1]:b0=v+2*t*b1-b2;b2,b1=b1,b0
 return a[0]+t*b1-b2

class AxisPrimitive:
 def __init__(self,polys,P,L,c):
  self.P=mnum(P);self.L=mnum(L);self.c=mnum(c)
  for name in ['H','J','K']:setattr(self,name,[mnum(v)for v in polys[name]])
  self.Ht=[mnum(v)for v in derivative(polys['H'])]
  self.cH=mnum(polys['cH']);self.a=mnum(polys['a'])
 def coordinate(self,y):
  y=abs(y)
  if not y:return mp.mpf(-1)
  target=mp.log(y/self.L)+self.P*mp.log(2)
  z=2*target if target<0 else target/self.P
  for iteration in range(100):
   if z>0:
    em=mp.exp(-z);lpe=z+mp.log1p(em);s=1/(1+em)
   else:
    ep=mp.exp(z);lpe=mp.log1p(ep);s=ep/(1+ep)
   f=z/2+(self.P-mp.mpf('.5'))*lpe-target
   step=f/(mp.mpf('.5')+(self.P-mp.mpf('.5'))*s)
   z-=step
   if abs(step)<mp.eps*16*(1+abs(z)):break
  else:raise ArithmeticError('Independent logit radial inversion failed')
  if z>0:return 1-2/(1+mp.exp(z))
  ez=mp.exp(z);return (ez-1)/(ez+1)
 def axis_jet(self,y):
  t=self.coordinate(y);s=(1+t)/2;w=(1-t)/2;qq=w+2*self.P*s
  hz=4*s*w/qq*evaluate(self.Ht,t);h=evaluate(self.H,t)
  return y*h,h+hz
 def k(self,y):return evaluate(self.K,self.coordinate(y))
 def v2(self,y,order):
  sign=-1 if y<0 else 1;y=abs(y)
  if not y:return mp.mpf(0)
  cuts=[mp.mpf(0),y]
  v=mp.mpf('0.001953125')
  while v<y:cuts.append(v);v*=2
  cuts=sorted(cuts);nodes,weights=rule(order,mp.mp.dps)
  total=mp.mpf(0)
  for lo,hi in zip(cuts[:-1],cuts[1:]):
   mid=(hi+lo)/2;half=(hi-lo)/2
   total+=half*mp.fsum(weights[j]*self.k(mid+half*nodes[j])for j in range(order))
  return sign*total
 def residual(self,y,order):
  g,gy=self.axis_jet(y);v2=self.v2(y,order);v=self.c*y+v2;R=v*gy-g
  nf=abs(v*gy)+abs(g);nv=abs(g)+abs(y*gy)+abs(v2*gy)
  return dict(g=g,gy=gy,V2=v2,dV2_dy=self.k(y),R=R,Nf=nf,Nv=nv,R_Nf=abs(R)/nf if nf else None,R_Nv=abs(R)/nv if nv else None)

@lru_cache(None)
def rule(order,dps):
 with mp.workdps(dps):
  nodes,weights=mp.gauss_quadrature(order,'legendre')
  return tuple(nodes),tuple(weights)
