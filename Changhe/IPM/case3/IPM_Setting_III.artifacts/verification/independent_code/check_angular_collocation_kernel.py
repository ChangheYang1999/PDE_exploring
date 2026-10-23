"""Exact finite checks of the angular-sampling kernel proof."""
from pathlib import Path
from datetime import datetime,timezone
from math import comb
from fractions import Fraction as F
import hashlib,json,time
R=Path('research/angular_collocation_kernel_audit');V=R/'verification';checks=[];binds={};t=time.perf_counter()
def ck(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def trim(a):
 while len(a)>1 and a[-1]==0:a.pop()
 return a
def cheb(n):
 a=[1];b=[0,1]
 if n==0:return a
 for _ in range(1,n):
  c=[0]*(len(b)+1)
  for i,x in enumerate(b):c[i+1]+=2*x
  for i,x in enumerate(a):c[i]-=x
  a,b=b,trim(c)
 return b
def mul(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,u in enumerate(a):
  for j,v in enumerate(b):out[i+j]+=u*v
 return trim(out)
def power(a,k):
 out=[1]
 for _ in range(k):out=mul(out,a)
 return out
def val(c,z):
 s=F(0)
 for x in reversed(c):s=s*z+x
 return s
def cpow(x,y,n):
 a,b=F(1),F(0)
 for _ in range(n):a,b=a*x-b*y,a*y+b*x
 return a,b
for p in [__file__,R/'PROOF.md']:binds[str(p)]=sha(p)
for M in [1,2,3,4,5,7,8,16,24,32,40,48,56,64]:
 c=cheb(M);ck(str(M)+' degree and leading coefficient',len(c)==M+1 and c[-1]==2**(M-1))
 # Coefficient of y^(2k), with x=1, in (1+y^2)^M T_M((1-y^2)/(1+y^2)).
 co=[0]*(M+1)
 for j,a in enumerate(c):
  p=mul(power([1,-1],j),power([1,1],M-j))
  for k,b in enumerate(p):co[k]+=a*b
 ck(str(M)+' all coefficients independent binomial',co==[(-1)**k*comb(2*M,2*k)for k in range(M+1)])
 for x,y in [(F(1),F(0)),(F(0),F(1)),(F(3,5),F(4,5)),(F(-3,5),F(4,5)),(F(3,5),F(-4,5)),(F(2),F(7)),(F(-2),F(-7))]:
  r2=x*x+y*y;z=(x*x-y*y)/r2;expr=r2**M*val(c,z);direct=cpow(x,y,2*M)[0]
  ck(str((M,x,y))+' complex multiplication versus Chebyshev',expr==direct)
  ck(str((M,x,y))+' binomial parity',cpow(-x,y,2*M)[0]==direct and cpow(x,-y,2*M)[0]==direct)
 ck(str(M)+' exact nonzero y-axis polynomial',cpow(F(0),F(1),2*M)[0]==(-1)**M)
for p,h in binds.items():ck('stable '+p,sha(p)==h)
out=dict(status='PASS_EXACT_FINITE_FORMULA_CHECKS',utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.perf_counter()-t,count=len(checks),checks=checks,bindings=binds,scope='Finite integer/rational diagnostics only. General sampling statement proved in PROOF.md. No actual candidate residual or inverse evaluated; primary unresolved.')
(V/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count'],out['elapsed_seconds'])
