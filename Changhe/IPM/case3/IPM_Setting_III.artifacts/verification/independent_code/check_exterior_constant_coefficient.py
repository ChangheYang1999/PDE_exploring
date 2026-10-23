"""Exact countertests for the exterior constant-coefficient audit.

The proof is in research/exterior_constant_coefficient_audit/PROOF.md.
No producer code is imported. These finite tests support, not replace, it.
"""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
from math import comb
import hashlib,json,time
start=time.monotonic();checks=[]
def add(p,q):
 out=p.copy()
 for k,v in q.items():out[k]=out.get(k,F(0))+v
 return {k:v for k,v in out.items()if v}
def scale(p,c):return {k:v*c for k,v in p.items()if v*c}
def monomial(p,dx,dy):return {(i+dx,j+dy):v for(i,j),v in p.items()}
def diff(p,axis):
 out={}
 for(i,j),v in p.items():
  n=(i,j)[axis]
  if n:out[(i-(axis==0),j-(axis==1))]=v*n
 return out
def radial_diff(poly,beta,axis):
 # d(poly*(x^2+y^2)^beta)=newpoly*(x^2+y^2)^(beta-1).
 d=diff(poly,axis)
 return add(add(monomial(d,2,0),monomial(d,0,2)),
            scale(monomial(poly,axis==0,axis==1),2*beta))
def rank(rows):
 a=[list(r)for r in rows];n=len(a);m=len(a[0]);r=0
 for j in range(m):
  pivot=next((k for k in range(r,n)if a[k][j]),None)
  if pivot is None:continue
  a[r],a[pivot]=a[pivot],a[r];v=a[r][j];a[r]=[x/v for x in a[r]]
  for k in range(r+1,n):
   v=a[k][j]
   if v:a[k]=[x-v*y for x,y in zip(a[k],a[r])]
  r+=1
  if r==n:break
 return r
def verify(label,condition,**data):
 if not condition:raise AssertionError((label,data))
 checks.append(dict(test=label,**data))
for p in [F(1,3),F(1,2),F(2,3)]:
 beta=(p-1)/2
 for m in range(10):
  polys=[]
  for nx in range(m+1):
   poly={(0,1):F(1)};b=beta
   for axis in [0]*nx+[1]*(m-nx):poly=radial_diff(poly,b,axis);b-=1
   reverse={(0,1):F(1)};b=beta
   for axis in [1]*(m-nx)+[0]*nx:reverse=radial_diff(reverse,b,axis);b-=1
   verify('commuting derivatives of noninteger homogeneous field',poly==reverse,p=str(p),order=m,x_order=nx)
   polys.append(poly)
  degrees=[(i,m+1-i)for i in range(m+2)]
  mat=[[q.get(d,F(0))for q in polys]for d in degrees]
  verify('no homogeneous annihilator of sampled order',rank(mat)==m+1,p=str(p),order=m,rank=rank(mat))
 lap=add(radial_diff(radial_diff({(0,1):F(1)},beta,0),beta-1,0),radial_diff(radial_diff({(0,1):F(1)},beta,1),beta-1,1))
 expected={(2,1):p*p-1,(0,3):p*p-1}
 verify('polar Laplacian coefficient independently recovered',lap==expected,p=str(p))
 for m in range(10):
  # Scaling a test function supplies R^(p+2-j), so the smallest
  # differential order survives division by its own power.
  for j in range(m,10):
   verify('rescaled exponent and noninteger point-support degree',
     (p+2-j)-(p+2-m)==m-j and (p-m+2).denominator!=1,p=str(p),m=m,j=j)
  for k in range(8):
   b=p+2+k;M=m+k+5
   verify('two tails of differentiated dyadic series',b>0 and b-M<0,p=str(p),derivative=k,decay=M)
# Separate polynomial tests of the ridge annihilator and integer exception.
def multiply(p,q):
 out={}
 for(i,j),v in p.items():
  for(k,l),w in q.items():out[(i+k,j+l)]=out.get((i+k,j+l),F(0))+v*w
 return {k:v for k,v in out.items()if v}
def power(p,n):
 out={(0,0):F(1)}
 for _ in range(n):out=multiply(out,p)
 return out
def directional(p,v):return add(scale(diff(p,0),v[0]),scale(diff(p,1),v[1]))
ls=[(1,2),(2,-1),(3,1)]
for n in range(1,9):
 poly={}
 for j,l in enumerate(ls):poly=add(poly,power({(1,0):F(l[0]),(0,1):F(l[1]),(0,0):F(j-1)},n+j))
 for l in ls:poly=directional(poly,(-l[1],l[0]))
 verify('commuting product annihilates finite ridge sum',not poly,degree=n)
for n in range(8):
 poly={(n,0):F(1)}
 for _ in range(n+1):poly=diff(poly,0)
 verify('integer homogeneous polynomial exception',not poly,degree=n)
for A in [(1,2,3,4),(0,1,-1,0),(2,0,1,3)]:
 a,b,c,d=map(F,A);det=a*d-b*c
 verify('fixed linear maps preserve nonzero rays and central reflection',det!=0 and a*(-1)+b*(-2)==-(a+2*b),matrix=A,determinant=str(det))
root=Path('research/exterior_constant_coefficient_audit/verification')
result=dict(utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,status='PASS',count=len(checks),checks=checks,
 code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),proof_sha256=hashlib.sha256((root.parent/'PROOF.md').read_bytes()).hexdigest(),
 scope='Finite exact countertests and algebra checks. General exclusion follows from the written distributional proof, not from finite orders tested.')
(root/'CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k]for k in ['utc','elapsed_seconds','status','count']}))
