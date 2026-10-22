"""Independent high-precision value-only mixed generating-function evaluator.

No lead/numerics code is imported. Physical derivatives use exact tensor FD
weights, rather than the lead's automatic Taylor jets.
"""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from math import factorial
import json,hashlib,time
import mpmath as mp

def mq(q):
 q=Q(q);return mp.mpf(q.numerator)/q.denominator

def chebs(x,n):
 if n==0:return []
 ans=[mp.mpf(1)]
 if n>1:ans.append(x)
 while len(ans)<n:ans.append(2*x*ans[-1]-ans[-2])
 return ans

class GeneratingFunction:
 def __init__(self,path):
  self.path=Path(path);d=json.loads(self.path.read_text());self.data=d
  self.beta=mq(d['beta']);self.a0=mq(d['a0']);assert self.beta>2
  self.a=mp.mpf('.5')-1/self.beta;self.C=[[mq(x) for x in row]for row in d['C']];self.D=[[mq(x) for x in row]for row in d['D']]
  self.calls=0;self.root_iterations=0;self.max_root_defect=mp.mpf(0)
 def radius(self,q,y):
  if q==0:return mp.sqrt(1+y*y)
  a=self.a;q2=q*q;yy=1+y*y
  lo=mp.mpf(0);hi=max(mp.log(2*q2)/(2*a),mp.log(2*yy)/2,mp.mpf(1))
  u=(lo+hi)/2
  for it in range(160):
   e=q2*mp.exp(-2*a*u);f=yy*mp.exp(-2*u);g=e+f-1;dg=-2*a*e-2*f
   if abs(g)<mp.eps*64:
    self.root_iterations+=it+1;self.max_root_defect=max(self.max_root_defect,abs(g));return mp.exp(u)
   if g>0:lo=u
   else:hi=u
   trial=u-g/dg;u=trial if lo<trial<hi else (lo+hi)/2
  raise ArithmeticError('Independent radius root failed')
 def __call__(self,q,y):
  self.calls+=1;R=self.radius(q,y);t=mp.exp(-mp.log(R)/self.beta);v=y/R
  tn=chebs(2*t-1,max(len(self.C),len(self.D)));nv=max([len(row)for row in self.C+self.D]+[0]);tv=chebs(v,nv)
  def val(coeff):return mp.fsum(tn[i]*mp.fsum(c*tv[j]for j,c in enumerate(row))for i,row in enumerate(coeff))
  p=val(self.C)
  if self.D:
   d=self.beta-3;factor=t**3*(mp.log(t)if d==0 else mp.expm1(d*mp.log(t))/d);p+=factor*val(self.D)
  return q*mp.exp((2-self.a)*mp.log(R))*p

@lru_cache(maxsize=4)
def fd_weights(n):
 assert n in[9,11,13];nodes=list(range(-(n//2),n//2+1));ans=[]
 for derivative in range(5):
  mat=[[Q(x)**power for x in nodes]+[Q(factorial(power)if power==derivative else 0)]for power in range(n)]
  for i in range(n):
   pivot=next(k for k in range(i,n)if mat[k][i]);mat[i],mat[pivot]=mat[pivot],mat[i];v=mat[i][i];mat[i]=[x/v for x in mat[i]]
   for k in range(n):
    if k==i:continue
    v=mat[k][i]
    if v:mat[k]=[x-v*y for x,y in zip(mat[k],mat[i])]
  w=[row[-1]for row in mat]
  for p in range(n):assert sum(wi*Q(x)**p for wi,x in zip(w,nodes))==(factorial(p)if p==derivative else 0)
  ans.append(w)
 return nodes,ans

def derivatives(fun,q,y,relative_step,n=9):
 nodes,w=fd_weights(n);hq=relative_step*max(1,abs(q));hy=relative_step*max(1,abs(y));wm=[[mq(x)for x in row]for row in w]
 values=[[fun(q+i*hq,y+j*hy)for j in nodes]for i in nodes];out={}
 for i in range(5):
  temp=[mp.fsum(wm[i][k]*values[k][l]for k in range(n))/hq**i for l in range(n)]
  for j in range(5-i):out[i,j]=mp.fsum(wm[j][l]*temp[l]for l in range(n))/hy**j
 return out

def physical(s,q,y,beta,a0):
 p=beta/2-1;mu=3*beta/2+1;J=s[1,1]
 if J<=0:return {'chart_valid':False,'J':J,'x':s[0,1]}
 unit=[(1,0),(0,1)]
 def inc(key,u):return key[0]+u[0],key[1]+u[1]
 def sj(key,u):return s[inc(key,u)]
 Ji=[sj((1,1),i)for i in unit];Jij=[[s[inc(inc((1,1),i),j)]for j in unit]for i in unit]
 A=s[0,2]/J;Ai=[(sj((0,2),u)-A*Ji[i])/J for i,u in enumerate(unit)]
 Aij=[[(s[inc(inc((0,2),u),v)]-Ai[i]*Ji[j]-Ai[j]*Ji[i]-A*Jij[i][j])/J for j,v in enumerate(unit)]for i,u in enumerate(unit)]
 def psi(i,j):return (2*beta-p*i-beta*j)*s[i,j]-p*q*s[i+1,j]-beta*y*s[i,j+1]
 B=1/J**2+A*A;C=-Ji[0]/J**3-Ai[1]+A*Ai[0]
 om=-(B*psi(2,0)-2*A*psi(1,1)+psi(0,2)+C*psi(1,0));omi=[]
 for i,u in enumerate(unit):
  bi=-2*Ji[i]/J**3+2*A*Ai[i];ci=-Jij[0][i]/J**3+3*Ji[0]*Ji[i]/J**4-Aij[1][i]+Ai[i]*Ai[0]+A*Aij[0][i]
  pi=lambda k,l:psi(k+u[0],l+u[1])
  omi.append(-(bi*psi(2,0)+B*pi(2,0)-2*Ai[i]*psi(1,1)-2*A*pi(1,1)+pi(0,2)+ci*psi(1,0)+C*pi(1,0)))
 V=(mu*s[1,0]-p*q*s[2,0])/J;W1=p*q*J+s[0,2]*V;omx=omi[0]/J;omy=omi[1]-A*omi[0];thx=2*a0*q/J
 residual=p*q*omi[0]+V*omi[1]+om-thx;normalizer=abs(W1*omx)+abs(V*omy)+abs(om)+abs(thx)
 ratio=abs(residual)/normalizer if normalizer else (mp.mpf(0)if residual==0 else mp.inf)
 return dict(chart_valid=True,x=s[0,1],y=y,q=q,J=J,eta=s[1,0],Psi=psi(0,0),Omega=om,Omega_q=omi[0],Omega_y=omi[1],W1=W1,W2=V,Theta_x=thx,residual=residual,normalizer=normalizer,ratio=ratio)

def strings(d):return {k:v if isinstance(v,bool)else mp.nstr(v,55)for k,v in d.items()}
