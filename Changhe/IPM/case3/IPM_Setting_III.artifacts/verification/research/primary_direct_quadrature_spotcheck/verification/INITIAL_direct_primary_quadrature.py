from fractions import Fraction as F
import mpmath as mp

def number(v):
 if isinstance(v,dict):v=F(int(v['numerator']),int(v['denominator']))
 if isinstance(v,F):return mp.mpf(v.numerator)/v.denominator
 return mp.mpf(v)

class DirectField:
 def __init__(self,d):
  self.alpha=number(d['alpha']);self.L=number(d['length']);self.ell=number(d['cl']);self.co=[[number(v)for v in row]for row in d['chebyshev_coefficients']];self.M=len(self.co)
 def density_modes(self,s):
  q=s*s/(self.L*self.L+s*s);w=(1+s*s/(self.L*self.L))**(-self.alpha);t=1-2*w
  N=max(map(len,self.co));T=[mp.mpf(1)];D=[mp.mpf(0)]
  if N>1:T.append(t);D.append(mp.mpf(1))
  for j in range(1,N-1):T.append(2*t*T[-1]-T[-2]);D.append(2*T[-2]+2*t*D[-1]-D[-2])
  gs=[];bs=[];power=mp.mpf(1)
  for k,co in enumerate(self.co):
   p=mp.fsum(c*T[j]for j,c in enumerate(co));dp=mp.fsum(c*D[j]for j,c in enumerate(co));fac=power*w
   gs.append(fac*p);bs.append(fac*((2*k*(1-q)-2*self.alpha*q)*p+4*self.alpha*q*w*dp));power*=q
  gs.append(mp.mpf(0));bs.append(mp.mpf(0))
  A=[gs[0]-gs[1]/2];B=[bs[0]-bs[1]/2]
  for k in range(1,self.M):A.append((gs[k]-gs[k+1])/2);B.append((bs[k]-bs[k+1])/2)
  return A,B
 def source(self,s):
  A,B=self.density_modes(s);A.append(mp.mpf(0));B.append(mp.mpf(0))
  return [((-2*k)*A[k]+B[k]+(2*k+4)*A[k+1]+B[k+1])/2 for k in range(self.M)]
 def local(self,x,y):
  r=mp.hypot(x,y);th=mp.atan2(y,x);A,B=self.density_modes(r)
  val=r*mp.fsum(a*mp.sin((2*k+1)*th)for k,a in enumerate(A));dr=mp.fsum((a+b)*mp.sin((2*k+1)*th)for k,(a,b)in enumerate(zip(A,B)));dt=mp.fsum((2*k+1)*a*mp.cos((2*k+1)*th)for k,a in enumerate(A))
  return val,(x*dr-y*dt)/r,(y*dr+x*dt)/r
 def direct_density(self,x,y):
  q=(x+mp.j*y)**2/(self.L*self.L+x*x+y*y);w=(1+(x*x+y*y)/(self.L*self.L))**(-self.alpha);t=1-2*w
  return y*w*mp.fsum(mp.re(q**k)*mp.fsum(c*mp.chebyt(j,t)for j,c in enumerate(co))for k,co in enumerate(self.co))
 def inverse(self,x,y,nodes,weights):
  r=mp.hypot(x,y);th=mp.atan2(y,x);P=[mp.mpf(0)]*self.M;Q=[mp.mpf(0)]*self.M
  for zz,ww in zip(nodes,weights):
   v=(number(float(zz))+1)/2;wt=number(float(ww))/2;inside=self.source(r*v);outside=self.source(r/v**5)
   for j,(a,b)in enumerate(zip(inside,outside),1):P[j-1]+=wt*v**(2*j+1)*a;Q[j-1]+=wt*5*v**(10*(j-1)-1)*b
  ps=r*r*mp.fsum((p+q)*mp.sin(2*j*th)/(4*j)for j,(p,q)in enumerate(zip(P,Q),1));ur=-r*mp.fsum((p+q)*mp.cos(2*j*th)/2 for j,(p,q)in enumerate(zip(P,Q),1));ut=r*mp.fsum((q-p)*mp.sin(2*j*th)/2 for j,(p,q)in enumerate(zip(P,Q),1))
  return ps,(x*ur-y*ut)/r,(y*ur+x*ut)/r
