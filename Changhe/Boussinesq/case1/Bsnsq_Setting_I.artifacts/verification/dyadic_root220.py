"""Outward integer arithmetic for exact beta3 implicit-coordinate brackets.
Proof: research/implicit_root220/PROOF.md. No fitting or mpmath code used.
"""
from fractions import Fraction as F
from math import factorial
P=400;B=1<<P

def floor_rat(q):q=F(q);return(q.numerator*B)//q.denominator
def ceil_rat(q):q=F(q);return -((-q.numerator*B)//q.denominator)
class I:
 __slots__=('lo','hi')
 def __init__(self,lo,hi=None):
  self.lo=int(lo);self.hi=int(lo if hi is None else hi)
  if self.lo>self.hi:raise ArithmeticError('reversed interval')
 @staticmethod
 def of(q):return q if isinstance(q,I)else I(floor_rat(q),ceil_rat(q))
 def __add__(self,z):z=I.of(z);return I(self.lo+z.lo,self.hi+z.hi)
 __radd__=__add__
 def __neg__(self):return I(-self.hi,-self.lo)
 def __sub__(self,z):return self+-I.of(z)
 def __rsub__(self,z):return I.of(z)+-self
 def __mul__(self,z):
  z=I.of(z);v=[self.lo*z.lo,self.lo*z.hi,self.hi*z.lo,self.hi*z.hi];return I(min(v)//B,-((-max(v))//B))
 __rmul__=__mul__
 def reciprocal(self):
  if self.lo<=0<=self.hi:raise ArithmeticError('zero denominator')
  return I((B*B)//self.hi,-((-B*B)//self.lo))
 def __truediv__(self,z):return self*I.of(z).reciprocal()
 def __rtruediv__(self,z):return I.of(z)*self.reciprocal()
 def __pow__(self,n):
  if not isinstance(n,int):raise TypeError('integer exponent required')
  if n<0:return self.reciprocal()**(-n)
  result=I.of(1);a=self
  while n:
   if n&1:result=result*a
   a=a*a;n//=2
  return result
 def dump(self):return{'lo':str(self.lo),'hi':str(self.hi),'denominator_power':P}
 def contains(self,q):q=F(q);return self.lo*q.denominator<=q.numerator*B<=self.hi*q.denominator
 def width(self):return F(self.hi-self.lo,B)

def sixth_inverse(E):
 E=F(E)
 if E<1:raise ValueError('E must be >=1')
 n,d=E.numerator,E.denominator;target=d*(B**6);lo,hi=0,B
 while lo+1<hi:
  m=(lo+hi)//2
  if n*m**6<=target:lo=m
  else:hi=m
 if n*hi**6==target:lo=hi
 if not(n*lo**6<=target<=n*hi**6):raise ArithmeticError('sixth root bracket')
 return I(lo,hi)

def log_series(a,N=200):
 """a is exact rational in [0,1/3]; log((1+a)/(1-a))."""
 a=F(a)
 if not 0<=a<=F(1,3):raise ValueError('log range')
 q=I.of(a);step=q*q;power=q;out=I.of(0)
 for n in range(N):out=out+power*F(2,2*n+1);power=power*step
 tail=F(2,1)*F(1,3)**(2*N+1)/(F(2*N+1)*(1-F(1,9)))
 return I(out.lo,out.hi+ceil_rat(tail))
_LOG2=None

def scalar_log(z):
 global _LOG2
 z=F(z)
 if z<=0:raise ValueError('positive log argument')
 if _LOG2 is None:_LOG2=log_series(F(1,3))
 j=0;v=z
 while v<1:v*=2;j-=1
 while v>=2:v/=2;j+=1
 return log_series((v-1)/(v+1))+j*_LOG2

def log(z):
 z=I.of(z)
 if z.lo<=0:raise ValueError('log interval domain')
 return I(scalar_log(F(z.lo,B)).lo,scalar_log(F(z.hi,B)).hi)

def scalar_exp_negative(z,N=160):
 z=F(z)
 if z<0:raise ValueError('nonnegative exp argument required')
 if not z:return I.of(1)
 if z>=P:return I(0,1)
 j=0;u=z
 while u>F(1,2):u/=2;j+=1
 q=-I.of(u);power=I.of(1);out=power
 for n in range(1,N+1):power=power*q/n;out=out+power
 tail=F(2,(2**(N+1))*factorial(N+1));pad=ceil_rat(tail);out=I(out.lo-pad,out.hi+pad)
 if out.lo<0:out=I(0,out.hi)
 for _ in range(j):out=out*out
 return out

def exp_negative(z):
 z=I.of(z)
 if z.lo<0:raise ValueError('negative exp argument interval')
 return I(scalar_exp_negative(F(z.hi,B)).lo,scalar_exp_negative(F(z.lo,B)).hi)

def cheb(z,n):
 if n<1:raise ValueError('empty polynomial')
 a=[I.of(1)];d=[I.of(0)]
 if n>1:a.append(2*z-1);d.append(I.of(2))
 for _ in range(2,n):a.append(2*(2*z-1)*a[-1]-a[-2]);d.append(4*a[-2]+2*(2*z-1)*d[-1]-d[-2])
 return a,d

def polynomial(c,t,w):
 tx,dx=cheb(t,len(c));tw,dw=cheb(w,len(c[0]));v=I.of(0);vt=I.of(0);vw=I.of(0)
 for i,row in enumerate(c):
  vv=I.of(0);ww=I.of(0)
  for j,a in enumerate(row):vv=vv+a*tw[j];ww=ww+a*dw[j]
  v=v+tx[i]*vv;vt=vt+dx[i]*vv;vw=vw+tx[i]*ww
 return v,vt,vw

class Field:
 def __init__(self,data):
  if F(data['beta'])!=3 or data['M']!=3 or F(data['alpha'])!=3:raise ValueError('beta3 alpha3 M3 only')
  self.s=F(data['s']);self.a=F(data['a']);self.k=1-exp_negative(I.of(3))
  if self.s<=0 or not self.a:raise ValueError('s/a')
  def rows(c):
   if not c or not c[0]or any(len(v)!=len(c[0])for v in c):raise ValueError('coefficient layout')
   return[[I.of(F(v))for v in row]for row in c]
  self.c=rows(data['outer']);self.patches=[]
  for p in data['patches']:
   R,L=F(p['R']),F(p['L'])
   if min(R,L)<=0:raise ValueError('patch domain')
   self.patches.append((R,L,rows(p['coefficients'])))
 def gx(self,x,eta,diagnostics=False):
  x,eta=F(x),F(eta);E=1+x*x+(eta/self.s)**6;q=sixth_inverse(E);X,H=I.of(x),I.of(eta)
  den=1-self.k*q;t=-log(den)/3;w=(eta/self.s)**2*q**2
  qx=-X*q**7/3;tx=self.k*qx/(3*den);wx=2*(eta/self.s)**2*q*qx
  val,pt,pw=polynomial(self.c,t,w);vx=pt*tx+pw*wx
  for R,L,c in self.patches:
   u=x*x/(R*R+x*x);v=eta*eta/(R*R+eta*eta);ux=2*x*R*R/(R*R+x*x)**2
   co,cu,_=polynomial(c,I.of(u),I.of(v));en=exp_negative(I.of((x*x+eta*eta)/(L*L)))
   val=val+en*co;vx=vx+en*(cu*ux-2*x*co/(L*L))
  out=H*((q**-2+F(2,3)*x*x*q**4)*val+X*q**-2*vx)
  if diagnostics:return out,{'E':str(E),'q':q.dump(),'t':t.dump(),'w':w.dump(),'F':val.dump(),'Fx':vx.dump()}
  return out
