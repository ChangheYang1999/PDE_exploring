"""Fourth-order interval Taylor evaluation; proof in research/interval_residual221."""
from fractions import Fraction as F
from math import factorial,comb
from dyadic_root220 import I,B,P,sixth_inverse,log as ilog,exp_negative as iexp

def pairs(n):return[(i,j)for k in range(n+1)for i in range(k+1)for j in [k-i]]
class Jet:
 __slots__=('n','c')
 def __init__(self,n,c):
  self.n=n;self.c={ij:I.of(c.get(ij,0))for ij in pairs(n)}
 @classmethod
 def const(cls,v,n=4):return cls(n,{(0,0):I.of(v)})
 @classmethod
 def var(cls,v,axis,n=4):return cls(n,{(0,0):I.of(v),(1,0)if axis==0 else(0,1):I.of(1)})
 def trunc(self,n):
  if n>self.n:raise ValueError('cannot raise available order')
  return Jet(n,self.c)
 def __add__(self,z):
  if not isinstance(z,Jet):z=Jet.const(z,self.n)
  n=min(self.n,z.n);return Jet(n,{ij:self.c[ij]+z.c[ij]for ij in pairs(n)})
 __radd__=__add__
 def __neg__(self):return Jet(self.n,{ij:-v for ij,v in self.c.items()})
 def __sub__(self,z):return self+-z
 def __rsub__(self,z):return -self+z
 def __mul__(self,z):
  if not isinstance(z,Jet):return Jet(self.n,{ij:v*z for ij,v in self.c.items()})
  n=min(self.n,z.n);out={}
  for i,j in pairs(n):out[i,j]=sum((self.c[a,b]*z.c[i-a,j-b]for a in range(i+1)for b in range(j+1)),I.of(0))
  return Jet(n,out)
 __rmul__=__mul__
 def compose(self,coeff):
  if len(coeff)!=self.n+1:raise ValueError('composition degree')
  v=Jet(self.n,{ij:z if ij!=(0,0)else I.of(0)for ij,z in self.c.items()});out=Jet.const(coeff[-1],self.n)
  for a in reversed(coeff[:-1]):out=out*v+a
  return out
 def reciprocal(self):
  a=self.c[0,0];return self.compose([(-1)**k*a**(-k-1)for k in range(self.n+1)])
 def __truediv__(self,z):return self*(z.reciprocal()if isinstance(z,Jet)else I.of(z).reciprocal())
 def __rtruediv__(self,z):return self.reciprocal()*z
 def __pow__(self,k):
  if not isinstance(k,int):raise TypeError('integer exponent')
  if k<0:return self.reciprocal()**(-k)
  out=Jet.const(1,self.n);a=self
  while k:
   if k&1:out=out*a
   a=a*a;k//=2
  return out
 def d(self,axis):
  if self.n<1:raise ValueError('no derivative available')
  return Jet(self.n-1,{(i,j):(i+1)*self.c[i+1,j]if axis==0 else(j+1)*self.c[i,j+1]for i,j in pairs(self.n-1)})
 def log(self):
  a=self.c[0,0];return self.compose([ilog(a)]+[F((-1)**(k-1),k)*a**(-k)for k in range(1,self.n+1)])
 def exp_negative(self):
  a=iexp(self.c[0,0]);return self.compose([a*F((-1)**k,factorial(k))for k in range(self.n+1)])
 def inv_sixth(self):
  a=self.c[0,0]
  if a.lo<B:raise ValueError('sixth inverse domain')
  q=I(sixth_inverse(F(a.hi,B)).lo,sixth_inverse(F(a.lo,B)).hi);cs=[q];bc=F(1)
  for k in range(1,self.n+1):bc*=F(-1,6)-k+1;bc/=k;cs.append(q*bc*a**(-k))
  return self.compose(cs)

def cheb_derivative_bound(n,k):
 if k==0:return 1
 return 0 if k>n else n*2**(k-1)*factorial(k-1)*comb(n+k-1,n-k)

def cheb_basis(z,count):
 """Unshifted T_n(z), enclosing derivatives for every constant base in z.c00."""
 a=z.c[0,0]
 if a.lo < -B or a.hi>B:raise ValueError('Chebyshev argument outside certified range')
 m=(a.lo+a.hi)//2;rho=F(max(m-a.lo,a.hi-m),B);degree=z.n
 # One-variable normalized Taylor coefficients at exact midpoint, order<=degree.
 values=[[I.of(1)]+[I.of(0)for _ in range(degree)]]
 if count>1:values.append([I(m)]+[I.of(int(k==1))for k in range(1,degree+1)])
 for n in range(2,count):
  prev,older=values[-1],values[-2]
  values.append([2*I(m)*prev[k]+(2*prev[k-1]if k else I.of(0))-older[k]for k in range(degree+1)])
 out=[]
 for n,row in enumerate(values):
  cs=[]
  for k,v in enumerate(row):
   rad=I.of(rho*F(cheb_derivative_bound(n,k+1),factorial(k)));cs.append(I(v.lo-rad.hi,v.hi+rad.hi))
  out.append(z.compose(cs))
 return out

def tensor(c,t,w):
 a=cheb_basis(2*t-1,len(c));b=cheb_basis(2*w-1,len(c[0]));out=Jet.const(0,min(t.n,w.n))
 for i,row in enumerate(c):out=out+a[i]*sum((b[j]*v for j,v in enumerate(row)),Jet.const(0,w.n))
 return out

class Field:
 def __init__(self,j):
  if F(j['beta'])!=3 or j['M']!=3 or F(j['alpha'])!=3:raise ValueError('only beta3 M3 alpha3')
  matrices=[j['outer']]+[p['coefficients']for p in j['patches']]
  if any(not isinstance(c,list)or not c or not isinstance(c[0],list)or not c[0]or any(not isinstance(row,list)or len(row)!=len(c[0])for row in c)for c in matrices):raise ValueError('nonempty rectangular coefficient matrices required')
  self.s=F(j['s']);self.a=F(j['a']);
  if self.a!=600:raise ValueError('this audit fixes amplitude parameter600')
  self.k=1-iexp(I.of(3));self.c=[[I.of(F(z))for z in row]for row in j['outer']];self.patches=[(F(p['R']),F(p['L']),[[I.of(F(z))for z in row]for row in p['coefficients']])for p in j['patches']]
  if self.s<=0 or any(min(R,L)<=0 for R,L,c in self.patches):raise ValueError('positive scales')
 def generating(self,x,eta,n=4):
  X,H=Jet.var(x,0,n),Jet.var(eta,1,n);E=1+X*X+(H/self.s)**6;q=E.inv_sixth();t=-(1-q*self.k).log()/3;w=(H/self.s)**2*q*q;v=tensor(self.c,t,w)
  for R,L,c in self.patches:
   u=X*X/(R*R+X*X);z=H*H/(R*R+H*H);v=v+((X*X+H*H)/(L*L)).exp_negative()*tensor(c,u,z)
  return X*H*q**(-2)*v
 def residual(self,x,eta):return physical(self.generating(x,eta),Jet.var(x,0),Jet.var(eta,1),self.a)

def abs_interval(z):
 if z.lo>=0:return z
 if z.hi<=0:return -z
 return I(0,max(-z.lo,z.hi))

def physical(G,X,H,amp=600):
 """Uses generating derivatives and physical chain rules with available orders."""
 gx,gh=G.d(0),G.d(1);A=gx.d(1);C=gx.d(0)
 if A.c[0,0].lo<=0:raise ValueError('Jacobian interval not positive')
 W1=(5*gh-H*gh.d(1))/A;W2=C*W1+A*H;U1=W1-3*X;U2=W2-3*gx
 dx=lambda z:z.d(0)-(C/A)*z.d(1);dy=lambda z:z.d(1)/A
 om=dy(U1)-dx(U2);ox=dx(om);oy=dy(om);tx=-amp*C/A;ty=amp/A;theta=amp*H
 val=lambda z:z.c[0,0]
 vals={k:val(v)for k,v in dict(x=X,y=gx,eta=H,A=A,C=C,W1=W1,W2=W2,U1=U1,U2=U2,Omega=om,Omega_x=ox,Omega_y=oy,Theta=theta,Theta_x=tx,Theta_y=ty).items()}
 f=vals;ts=[f['W1']*f['Omega_x'],f['W2']*f['Omega_y'],f['Omega'],-f['Theta_x']];gs=[f['U1']*f['Omega_x'],f['U2']*f['Omega_y'],3*(f['x']*f['Omega_x']+f['y']*f['Omega_y'])+f['Omega'],-f['Theta_x']];R=sum(ts,I.of(0));N=sum(map(abs_interval,ts),I.of(0));N2=sum(map(abs_interval,gs),I.of(0))
 xy=f['x']*f['y'];divided=None if xy.lo<=0<=xy.hi else R/xy
 vals.update(R=R,N=N,N2=N2,D=divided,R_Theta=f['W1']*f['Theta_x']+f['W2']*f['Theta_y']-f['Theta']);vals['prompt_ratio']=abs_interval(R)/N if N.lo>0 else None;vals['grouped_ratio']=abs_interval(R)/N2 if N2.lo>0 else None
 return vals
