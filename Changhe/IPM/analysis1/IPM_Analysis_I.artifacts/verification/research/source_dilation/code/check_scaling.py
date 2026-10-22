"""Exact and directed independent checks for the analytic dilation corollary."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from datetime import datetime,timezone
import hashlib,json,math,sys
from flint import arb,ctx,fmpq
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/source_dilation';E=D/'evidence'
ctx.prec=512;iv.dps=180
counts=Counter()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def fa(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def fi(t):s,m,e,_=t;return (-1 if s else 1)*F(int(m))*F(2)**int(e)
def endpoints(x):
 if isinstance(x,arb):assert x.is_finite();return fa(x.lower()),fa(x.upper())
 return fi(x._mpi_[0]),fi(x._mpi_[1])
def qa(v):v=F(v);return arb(fmpq(v.numerator,v.denominator))
def qi(v):v=F(v);return iv.mpf(v.numerator)/v.denominator
def iroot(n,k):
 assert n>=0 and k>=1
 if n<2:return n
 x=1<<((n.bit_length()+k-1)//k)
 while True:
  y=((k-1)*x+n//x**(k-1))//k
  if y>=x:break
  x=y
 while (x+1)**k<=n:x+=1
 while x**k>n:x-=1
 assert x**k<=n<(x+1)**k
 return x
def rational_power(v,p,bits=768):
 v,p=F(v),F(p);assert v>0 and p>0
 n,d=(v**p.numerator).as_integer_ratio();scale=1<<bits;k=p.denominator
 root=iroot(n*scale**k//d,k)
 assert root**k*d<=n*scale**k<(root+1)**k*d
 counts['integer_root_cross_multiplications']+=2
 return F(root,scale),F(root+1,scale)
def atan_box(inv,N=400):
 x=F(1,inv);s=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(N)),F())
 nxt=(-1)**N*x**(2*N+1)/F(2*N+1)
 return min(s,s+nxt),max(s,s+nxt)
p5,p239=atan_box(5),atan_box(239);PI=(16*p5[0]-4*p239[1],16*p5[1]-4*p239[0])
assert PI[0]>3 and PI[1]<F(22,7)
# Machin identity: tan(4atan(1/5)-atan(1/239))=1 and angle in(0,pi/2).
def tanadd(a,b):return (a+b)/(1-a*b)
z=F(1,5);z2=tanadd(z,z);z4=tanadd(z2,z2);assert tanadd(z4,-F(1,239))==1
counts['exact_Machin_tangent_identity']=1
for eng,Q,pi in [('arb',qa,arb.pi()),('iv',qi,iv.pi)]:
 lo,hi=endpoints(pi);assert lo<=PI[0]<=PI[1]<=hi;counts['independent_pi_containments']+=1

def padded(x):
 lo,hi=endpoints(x);pad=(1+max(abs(lo),abs(hi)))*F(2)**-400
 return lo-pad,hi+pad

def root_direct(s,ell):
 # Original Fourier profile is1 on2/3<=|xi|<=5/4. Scale ell and use(2).
 h0=F(1)+ell*ell*F(4,9);h1=F(1)+ell*ell*F(25,16)
 a0,a1=rational_power(h0,s+1),rational_power(h1,s+1)
 fac=ell**-4/(s+1)
 return PI[0]*fac*(a1[0]-a0[1]),PI[1]*fac*(a1[1]-a0[0])
rows=[]
for s in map(F,('61/20','153/50','31/10')):
 for ell in map(F,('1','33/2000','1/100','7/2000')):
  # Arb: direct norm of the explicitly rescaled Fourier annulus.
  lo=1+qa(ell*ell*F(4,9));hi=1+qa(ell*ell*F(25,16))
  ar=arb.pi()*qa(ell**-4)/(qa(s+1))*(hi**qa(s+1)-lo**qa(s+1))
  # iv: N_(1/ell) norm times ell^(2s-2), derived before changing eta.
  low=qi(ell**-2+F(4,9));high=qi(ell**-2+F(25,16))
  other=qi(ell)**qi(2*s-2)*iv.pi/qi(s+1)*(high**qi(s+1)-low**qi(s+1))
  exact=root_direct(s,ell);boxes={'arb':padded(ar),'iv':padded(other)}
  for eng,(a,b) in boxes.items():assert 0<a<=exact[0]<=exact[1]<=b,(eng,s,ell);counts['fresh_integer_norm_containments']+=1
  rows.append({'s':str(s),'ell':str(ell),'squared_Hs_Dell_bounds':{e:list(map(str,v)) for e,v in boxes.items()},'independent_rational_root_box':list(map(str,exact))})
# At integer r=2, the Fourier Wiener annulus moments are exact rationals times1.
for ell in map(F,('1','33/2000','1/100','7/2000')):
 for r in (0,2,4):
  j=1+F(r,2);a,b=F(2,3),F(5,4)
  direct=ell**-2*((1+ell*ell*b*b)**j-(1+ell*ell*a*a)**j)/(r+2)
  expanded=sum((F(math.comb(r//2,k))*ell**(2*k)*(b**(2*k+2)-a**(2*k+2))/F(2*k+2) for k in range(r//2+1)),F())
  assert direct==expanded;counts['independent_Wiener_polynomial_integrals']+=1
# Fourier homogeneous symbols under isotropic and anisotropic dilation.
for a in range(-7,8):
 for b in range(-7,8):
  if not a and not b:continue
  xi,eta=F(a),F(b);den=xi*xi+eta*eta;symbols=(xi*xi/den,xi*eta/den,-xi*xi/den)
  for ell in map(F,('33/2000','1/100','7/2000')):
   x,y=xi/ell,eta/ell;dd=x*x+y*y
   assert symbols==(x*x/dd,x*y/dd,-x*x/dd);counts['homogeneous_symbol_checks']+=3
assert F(1)/(1+F(1,4))==F(4,5)!=F(1,2)
counts['anisotropic_symbol_counterexample']=1
# Dilation norms at integer orders by independent binomial expansion.
for ell in map(F,('1','33/2000','1/100','7/2000')):
 for xi2 in map(F,('0','1','3/2','10000')):
  assert ell**-2*(1+ell*ell*xi2)**4==sum((F(math.comb(4,j))*ell**(2*j-2)*xi2**j for j in range(5)),F())
  counts['integer_H4_scaling_identities']+=1
files={}
for name in ('source_semigroup','source_order_family'):
 p=B/'research'/name/'evidence/verdict.json';v=json.loads(p.read_text());assert v['status'].startswith('CONFIRMED');files[str(p.relative_to(B))]=sha(p)
 for f,h in v['files'].items():assert sha(B/f)==h,f;counts['dependency_hash_checks']+=1
for p in [D/'PROOF.md',E/'proof_first.json',Path(__file__)]:files[str(p.relative_to(B))]=sha(p)
assert sha(D/'PROOF.md')==json.loads((E/'proof_first.json').read_text())['proof_sha256']
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_AND_TWO_ENGINE_DILATION_CHECKS','counts':dict(counts),'annulus_examples':rows,'scope':'Analytic auxiliary-operator dilation and norm identities. Fourier-annulus examples are not actual coefficients. No trial R or inverse number evaluated.','files':files}
(E/'checks.json').write_text(json.dumps(out,indent=2)+'\n');(E/'review_summary.json').write_text(json.dumps({k:v for k,v in out.items() if k!='annulus_examples'},indent=2)+'\n')
print(json.dumps({'utc':out['utc'],'status':out['status'],'counts':dict(counts)},indent=2))
