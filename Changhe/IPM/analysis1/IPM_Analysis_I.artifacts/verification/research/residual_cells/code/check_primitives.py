"""Checks Taylor bounds against independently solved forced ODEs and Bernstein identities."""
import os
os.environ['OMP_NUM_THREADS']='1';os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,hashlib,math
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from mpmath import iv
from flint import arb,ctx
from certify_cells import aa,ends,exp_poly,ode,mul,bernstein_matrix,ff
ctx.prec=384;iv.dps=100
B=Path(__file__).resolve().parents[3]
def iq(x):x=F(x);return iv.mpf(x.numerator)/x.denominator
def ii(x):a,b=ends(x);return iv.mpf([iq(a).a,iq(b).b])
def fi(v):sg,m,e,_=v;return (-1 if sg else 1)*F(int(m))*F(2)**int(e)
def ie(v):return tuple(map(fi,v._mpi_))
def peval(p,x):
 y=iv.mpf(0)
 for v in reversed(p):y=y*x+v
 return y
def tm_at(tm,z):
 p,r=tm;v=peval(list(map(ii,p)),iq(z));return v+iv.mpf([-iq(ff(r)).b,iq(ff(r)).b])
def contains(big,small):a,b=ie(big);c,d=ie(small);return a<=c<=d<=b
Q=16;h=F(1,1000);tc=F(3,7);P=[F(1),F(-7,2),F(3,11)];zpts=[F(-1),F(-7,13),F(0),F(5,7),F(1)]
count=0
for lam in (-522,-2,0,2,522):
 for gamma in (-2,4):
  y0=F(2,3);s=1 if lam<0 else -1
  # Q'(x)+(gamma-lambda)Q(x)=P(x), solved downward in exact rationals.
  if gamma!=lam:
   q=[F(0)]*len(P)
   for j in range(len(P)-1,-1,-1):q[j]=(P[j]-(j+1)*(q[j+1] if j+1<len(P) else 0))/(gamma-lam)
  G=exp_poly([aa(v*h**j) for j,v in enumerate(P)],gamma,aa(tc),aa(h),Q);Y=ode(aa(y0),lam,s,G,aa(h),Q)
  for z in zpts:
   x=iq(z*h)
   if gamma!=lam:truth=iv.exp(lam*x)*(iq(y0)-s*iv.exp(gamma*iq(tc))*iq(q[0]))+s*iv.exp(gamma*(iq(tc)+x))*peval(list(map(iq,q)),x)
   else:truth=iv.exp(lam*x)*(iq(y0)+s*iv.exp(gamma*iq(tc))*sum((iq(v/F(j+1))*x**(j+1) for j,v in enumerate(P)),iv.mpf(0)))
   assert contains(tm_at(Y,z),truth),(lam,gamma,str(z),str(tm_at(Y,z)),str(truth));count+=1
# Basis conversion checked by exact de Casteljau evaluation, no floating matrix identity.
mat,_=bernstein_matrix(Q);bernchecks=0
for ell in range(Q+1):
 b=[row[ell] for row in mat]
 for u in [F(0),F(1,17),F(2,5),F(1,2),F(16,17),F(1)]:
  v=b[:]
  for j in range(Q):v=[(1-u)*v[i]+u*v[i+1] for i in range(len(v)-1)]
  assert v[0]==(2*u-1)**ell;bernchecks+=1
# Independent exact functions test product remainder, including degree truncation.
A=exp_poly([arb(1),arb(-2),arb(3)],2,aa(tc),aa(h),Q);C=exp_poly([arb(-1),arb(5)],-3,aa(tc),aa(h),Q);AC=mul(A,C,Q)
for z in zpts:
 truth=iv.exp(-(iq(tc)+iq(h*z)))*(1-2*iq(z)+3*iq(z)**2)*(-1+5*iq(z));assert contains(tm_at(AC,z),truth);count+=1
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','ODE_and_product_checks':count,'exact_de_Casteljau_checks':bernchecks,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'implementation_sha256':hashlib.sha256((Path(__file__).parent/'certify_cells.py').read_bytes()).hexdigest()}
(B/'research/residual_cells/evidence/primitives.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
