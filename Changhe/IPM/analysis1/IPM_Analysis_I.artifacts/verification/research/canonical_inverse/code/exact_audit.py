"""Exact rational Cox-polynomial and Gaussian root/weight audit of the scalar run."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import sys,json,hashlib,time,bisect,resource
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,fmpq,fmpq_poly,fmpq_mat,ctx
from strain_arb import Data
BASE=Path(__file__).resolve().parents[3]
def fq(x):return fmpq(x.numerator,x.denominator)
def dyadic(x):
 m,e=x.man_exp();return fmpq(m)*fmpq(2)**int(e)
def encloses(a,q):return dyadic(a.lower())<=q<=dyadic(a.upper())
def exact_poly(d,a,b):
 mid=(a+b)/2;span=bisect.bisect_right(d.t,mid)-1
 # Cox basis recursion, not de Boor value recursion or truncated series.
 polys={span:fmpq_poly([1])}
 for degree in range(1,d.deg+1):
  nxt={}
  for i in range(span-degree,span+1):
   v=fmpq_poly()
   if i in polys and d.t[i+degree]!=d.t[i]:
    v+=fmpq_poly([fq(mid-d.t[i]),1])*polys[i]/fq(d.t[i+degree]-d.t[i])
   if i+1 in polys and d.t[i+degree+1]!=d.t[i+1]:
    v+=fmpq_poly([fq(d.t[i+degree+1]-mid),-1])*polys[i+1]/fq(d.t[i+degree+1]-d.t[i+1])
   nxt[i]=v
  polys=nxt
 basis=[polys[i] for i in range(span-d.deg,span+1)]
 assert sum(basis,fmpq_poly())==fmpq_poly([1])
 return span,fmpq_mat([[v[j] for v in basis] for j in range(d.deg+1)])
def legendre(n):
 p0=fmpq_poly([1]);p1=fmpq_poly([0,1])
 for j in range(1,n):p0,p1=p1,((2*j+1)*fmpq_poly([0,1])*p1-j*p0)/(j+1)
 return p1

def run():
 start=time.monotonic();resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));ctx.threads=1;ctx.cap=8;ctx.prec=160
 d=Data();raw=d.raw;nr=raw['integers']['degree'];nm=d.nm
 assert len(raw['z_hex'])==1+nm*nr+6 and len(raw['names'])==nm*nr+6
 assert raw['names']==[[m,j] for m in range(nm) for j in range(nr)]+[[-1,j] for j in range(6)]
 assert len(d.t)==nr+1+d.deg+1 and d.deg==7
 assert d.t[:8]==[F(0)]*8 and d.t[-8:]==[F(1)]*8
 assert all(d.t[i]<d.t[i+1] for i in range(7,len(d.t)-8))
 z=[fq(F.from_float(float.fromhex(v))) for v in raw['z_hex']]
 co=[[fmpq(0) for _ in range(nm)]]+[[z[1+m*nr+i] for m in range(nm)] for i in range(nr)]
 part=json.loads((BASE/'research/canonical_inverse/evidence/strain_arb_20_32_partition.json').read_text())
 count=0
 for cell,(left,right) in enumerate(part['q']):
  a,b=F(left),F(right);span,basis=exact_poly(d,a,b);exact=basis*fmpq_mat(co[span-d.deg:span+1])
  mid,rows=d.poly(a,b)
  assert encloses(mid,fq((a+b)/2))
  for j,row in enumerate(rows):
   for m in range(nm):
    assert encloses(row[0,m],exact[j,m]),('polynomial failure',cell,j,m)
    count+=1
  if (cell+1)%50==0:print(json.dumps({'stage':'polynomials','cells':cell+1,'coefficients':count,'seconds':time.monotonic()-start}),flush=True)
 # Exact sign changes establish all roots, without trusting the root algorithm.
 roots=[]
 for n in (20,32):
  ctx.prec=160;old=[arb.legendre_p_root(n,k,weight=True) for k in range(n)]
  p=legendre(n);dp=p.derivative();ctx.prec=320
  fine=[arb.legendre_p_root(n,k) for k in range(n)]
  for k,(x,(oldx,oldw)) in enumerate(zip(fine,old)):
   lo,hi=dyadic(x.lower()),dyadic(x.upper())
   assert -1<lo<hi<1 and p(lo)*p(hi)<0,('root sign',n,k)
   if k+1<n:assert dyadic(fine[k+1].upper())<lo
   assert oldx.contains(x),('node containment',n,k)
   derivative=arb(0)
   for j in range(dp.degree(),-1,-1):derivative=derivative*x+arb(dp[j].numerator)/arb(dp[j].denominator)
   weight=2/((1-x*x)*derivative**2)
   assert oldw.contains(weight),('weight containment',n,k,oldw,weight)
  roots.append({'degree':n,'disjoint_exact_sign_changes':n,'160_bit_nodes_and_weights_contain_certified_320_bit_intervals':True})
 out={'utc':datetime.now(timezone.utc).isoformat(),'input_sha256':d.sha,'audited_script_sha256':hashlib.sha256((Path(__file__).parent/'strain_arb.py').read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'input_layout_and_all_names':'PASS','exact_Cox_polynomial_coefficients_contained_in_Arb_series':count,'polynomial_cells':len(part['q']),'gaussian_audits':roots,'seconds':time.monotonic()-start,'status':'PASS'}
 (BASE/'research/canonical_inverse/evidence/exact_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
if __name__=='__main__':run()
