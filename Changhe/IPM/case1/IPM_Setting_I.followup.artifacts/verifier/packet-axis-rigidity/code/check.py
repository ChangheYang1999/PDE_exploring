"""Exact algebra plus finite-cutoff manufactured checks of the trace change of variables."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import hashlib,json,math
import numpy as np
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
if not __debug__:raise RuntimeError('Assertions required')
exact=[]
for A in [Q(6,5),Q(3,2),Q(2),Q(5,2),Q(3),Q(10)]:
 for g in [Q(1,3),Q(1),Q(4),Q(15,2)]:
  q=2*(A-1);eta=q/A;b=g/q
  for n in range(9):
   assert eta*(b+n)==(g+n*q)/A
   assert -2*(b+n)/A == (g+n*q)/A -2*b-2*n
   exact.append({'A':str(A),'g':str(g),'n':n,'mu':str(eta*(b+n)),'verdict':'PASS'})
remainder=[]
for b in range(1,6):
 for n in range(7):
  c=Q(math.prod(range(b,b+n+1)),math.factorial(n+1))
  for z in [Q(1,100),Q(1,10),Q(1,4),Q(1,3),Q(1,2)]:
   approx=sum((-1)**j*Q(math.prod(range(b,b+j)),math.factorial(j))*z**j for j in range(n+1))
   error=abs((1+z)**(-b)-approx)
   assert error<=c*z**(n+1)
   remainder.append({'b':b,'n':n,'z':str(z),'verdict':'PASS'})
nulls=[]
for N in range(7):
 t=[sp.Rational(j+2) for j in range(N+2)]
 mat=sp.Matrix([[sp.Integer(1) for _ in t]]+[[x**(-2-n)for x in t]for n in range(N)])
 ns=mat.nullspace();assert len(ns)==1
 v=ns[0];assert mat*v==sp.zeros(N+1,1)
 first=sum(v[j]*t[j]**(-2-N)for j in range(N+2));assert first!=0
 nulls.append({'cancelled_moments':N,'rank':mat.rank(),'first_nonzero':str(first),'coefficients':[str(x)for x in v],'scope':'Exact finite point-measure illustration only; smooth construction is proved by dimension in PROOF.md.'})
def integral(A,g,s,order,changed):
 u,w=np.polynomial.legendre.leggauss(order);rlo=.03;rhi=2.5
 q=2*(A-1);b=g/q;ans=0.
 for center,sign in [(1.1,1.),(1.9,-1.)]:
  t=center+.1*u;tw=.1*w*np.exp(-1/(1-u*u))*sign
  if not changed:
   r=rlo+(rhi-rlo)*(u+1)/2;rw=(rhi-rlo)*w/2
   z=s*t[:,None]*r[None,:]**A
   integrand=(-2*np.sin(z/2)**2)*(1+t[:,None]**2*r[None,:]**q)**(-b)/r[None,:]
   ans+=np.dot(tw,integrand@rw)
  else:
   lo=t*rlo**A;hi=t*rhi**A;k=lo[:,None]+(hi-lo)[:,None]*(u[None,:]+1)/2
   kw=(hi-lo)[:,None]*w[None,:]/2
   z=s*k
   integrand=(-2*np.sin(z/2)**2)*(1+k**(q/A)*t[:,None]**(2/A))**(-b)/(A*k)
   ans+=np.dot(tw,np.sum(integrand*kw,axis=1))
 return float(ans)
manufactured=[]
for A,g in [(1.2,1.),(1.5,4.),(2.,4.),(3.,1.)]:
 for s in [.2,1.1]:
  direct=integral(A,g,s,128,False);changed=integral(A,g,s,128,True)
  error=abs(direct-changed);assert error<2e-10*max(1,abs(direct))
  manufactured.append({'A':A,'g':g,'s':s,'direct_r_integral':direct,'changed_k_integral':changed,'absolute_difference':error,'scope':'Floating quadrature on finite [.03,2.5] radial interval; two equal-mass smooth bumps. Not an enclosure or full-plane result.'})
out={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','exponent_identities':exact,'exact_binomial_remainder_bounds':remainder,'finite_moment_illustrations':nulls,'manufactured_change_of_variable':manufactured,'pins':{str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in [ROOT/'PROOF.md',Path(__file__)]},'scope':'Exact identities and finite illustrations only. The standalone proof carries the infinite moment determinacy and regularity conclusions.'}
(ROOT/'verification/check.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS',len(exact),'exponent identities,',len(remainder),'rational Taylor remainder bounds,',len(nulls),'finite nullspaces,',len(manufactured),'manufactured coordinate checks; maxerror',max(x['absolute_difference']for x in manufactured))
