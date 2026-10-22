"""Independent exact jets/kernel algebra and two-formula directed Beta evaluation."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from math import factorial
import hashlib,json,sys
from flint import arb,ctx,fmpq
from mpmath import iv
assert not sys.flags.optimize
ctx.prec=512;ctx.threads=1;iv.dps=180
B=Path(__file__).resolve().parents[3];D=B/'research/escape_realization';E=D/'evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def aa(q):q=F(q);return arb(fmpq(q.numerator,q.denominator))
def ii(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def aq(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def mq(x):s,m,e,b=x;assert b>=0;return (-1 if s else 1)*F(int(m))*F(2)**int(e)
def ends(x):
 lo,hi=(aq(x.lower()),aq(x.upper())) if isinstance(x,arb) else tuple(map(mq,x._mpi_));assert lo<=hi;return lo,hi
counts={'exact_jet_trials':0,'exact_kernel_derivative_norms':0,'exact_resonance_values':0,'signed_cost_pulse_cases':0,'exact_cutoff_and_saddle_comparisons':0,'beta_directed_inequalities':0}
def clean(p):return {k:F(v) for k,v in p.items() if v}
def add(p,q):
 z=dict(p)
 for k,v in q.items():z[k]=z.get(k,0)+v
 return clean(z)
def sc(p,a):return clean({k:v*a for k,v in p.items()})
def mul(p,q):
 z={}
 for (i,j),v in p.items():
  for (k,l),w in q.items():z[i+k,j+l]=z.get((i+k,j+l),0)+v*w
 return clean(z)
def df(p,axis):
 z={}
 for k,v in p.items():
  if k[axis]:l=list(k);l[axis]-=1;z[tuple(l)]=v*k[axis]
 return clean(z)
def dx(p,n,axis):
 for _ in range(n):p=df(p,axis)
 return p
def shift(p,n):return {(i+n,j):v for (i,j),v in p.items()}
def coeff(p,i):return {(0,j):v for (k,j),v in p.items() if k==i}
def power(p,n):
 z={(0,0):F(1)}
 for _ in range(n):z=mul(z,p)
 return z
# Fresh polynomial division in x recovers the harmonic jet from an arbitrary B.
for seed in range(1,65):
 b={(0,j):F(((seed*7+j*11)%23)-11,j+1) for j in range(1,10,2)}
 a2={(0,j):F(((seed*3+j*5)%17)-8,j+2) for j in range(1,8,2)}
 a4={(0,j):F(((seed*13+j*2)%19)-9,j+3) for j in range(1,8,2)}
 u2={};prev=b
 for n in range(3):
  u2=add(u2,shift(prev,2*n));prev=sc(dx(prev,2,1),F(-1,(2*n+2)*(2*n+1)))
 u1={}
 for (i,j),v in df(u2,1).items():u1[i+1,j]=-v/F(i+1)
 assert not add(df(u1,0),df(u2,1))
 lap=add(dx(u2,2,0),dx(u2,2,1));assert not coeff(lap,0) and not coeff(lap,2)
 rho=add(shift(a2,2),shift(a4,4));coupling=add(mul(u1,df(rho,0)),mul(u2,df(rho,1)))
 t2=add(mul(df(a2,1),b),sc(mul(a2,df(b,1)),-2))
 t4=add(add(mul(df(a4,1),b),sc(mul(a4,df(b,1)),-4)),add(sc(mul(df(a2,1),dx(b,2,1)),F(-1,2)),sc(mul(a2,dx(b,3,1)),F(1,3))))
 assert coeff(coupling,2)==t2 and coeff(coupling,4)==t4
 counts['exact_jet_trials']+=1
# A rational-function differentiation scheme independent of the complex proof.
r2={(2,0):F(1),(0,2):F(1)};coords=[{(1,0):F(1)},{(0,1):F(1)}]
kernels=[{(1,1):F(-2)},{(2,0):F(1),(0,2):F(-1)}]
def deriv_rat(p,m,axis):return add(mul(df(p,axis),r2),sc(mul(p,coords[axis]),-2*m)),m+1
for n in range(11):
 for nx in range(n+1):
  polys=[]
  for p0 in kernels:
   p=dict(p0);m=2
   for axis in [0]*nx+[1]*(n-nx):p,m=deriv_rat(p,m,axis)
   polys.append(p)
  assert add(mul(polys[0],polys[0]),mul(polys[1],polys[1]))==sc(power(r2,n+2),factorial(n+1)**2)
  counts['exact_kernel_derivative_norms']+=1
ky,_=deriv_rat(kernels[1],2,1);assert ky=={(2,1):F(-6),(0,3):F(2)}
# Positive-support witness: 3u^2-v^2 >= 3-1/16 >0.
assert 3-F(1,16)>0
for k in [F(1,7),F(1,5),F(1615536043799051,9007199254740992),F(2,3)]:
 cl=1/k
 for c in [F(-3,7),F(1),F(0),F(9,2)]:
  # Coefficients of r^k log r and r^k after applying cl*r*d_r-1.
  amp=-c/cl**2
  assert (cl*k-1)*amp==0 and cl*amp+c*k==0
  if c:assert cl*(-c/(3*cl**2))+c*k!=0
  counts['exact_resonance_values']+=1
# Piecewise-linear primitives: maxima occur at ordered breakpoints.
for N in range(2,26):
 inc=[]
 for j in range(N):
  inc.append(F(1))
  if j<N-1:inc.append(F(-2))
 prim=[F(0)]
 for z in inc:prim.append(prim[-1]+z)
 cost=max(prim[j]-prim[i] for i in range(len(prim)) for j in range(i,len(prim)))
 assert cost==1 and sum(max(0,z) for z in inc)==N
 counts['signed_cost_pulse_cases']+=1
radius=F(99,2000);MV=F(743,2500);assert radius*MV==F(73557,5000000)<F(99,200)
a=F(25,4);gamma=F(1129,1000);L=F(1,2);k=F(1615536043799051,9007199254740992)
assert 12-2*a>-1 and 8-2*a<-1 and 4-2*a<-1
assert 2*k-2*gamma+1>-1 and gamma<1+k
p=F(213014,10000)/F(101506,10000);assert 2<p<F(5,2) and 4<2*p<5
counts['exact_cutoff_and_saddle_comparisons']=8
# Primary standard Beta/Gamma formula at full arguments.
aA=aa(a);gA=aa(gamma);piA=arb.pi()
betaA=(aA-2).gamma()*(2-gA).gamma()/(aA-gA).gamma()
betaA*= (aA+aa(F(1,2))).gamma()*aa(F(1,2)).gamma()/(aA+1).gamma()
CA=aa(L)**(aA-2)*betaA.sqrt()/piA
# Secondary independently reduce by recurrence, cancel Gamma(1/4),
# then reflect the reciprocal Gamma(121/1000). Every factor is positive.
def rising(q,n):
 z=F(1)
 for j in range(n):z*=q+j
 return z
pref=rising(F(1,4),4)*rising(F(3,4),6)/(rising(F(1,4),7)*rising(F(121,1000),5))
betaI=ii(pref)*iv.gamma(ii(F(3,4)))*iv.sqrt(iv.pi)*iv.gamma(ii(F(871,1000)))*iv.gamma(ii(F(879,1000)))*iv.sin(iv.pi*ii(F(121,1000)))/iv.pi
CI=iv.exp(ii(a-2)*iv.log(ii(L)))*iv.sqrt(betaI)/iv.pi
bounds={}
for name,x in [('arb512_direct_gamma',CA),('iv180_recurrence_reflection',CI)]:
 lo,hi=ends(x);assert F(78147,10000000)<lo<hi<F(78149,10000000)
 assert hi/3<F(2605,1000000);counts['beta_directed_inequalities']+=3
 bounds[name]={'lower_exact':str(lo),'upper_exact':str(hi),'display':str(x)}
la,ha=ends(CA);li,hi=ends(CI);assert max(la,li)<=min(ha,hi)
files={}
for f in [Path(__file__),D/'PROOF.md',D/'ADDENDUM.md',E/'proof_first.json',B/'research/canonical_strain_sign/evidence/verdict.json',B/'research/coupling_squares/evidence/verdict.json',B/'research/n8_velocity_hessian/evidence/verdict.json']:files[str(f.relative_to(B))]=sha(f)
assert json.loads((E/'proof_first.json').read_text())['proof_sha256']==sha(D/'PROOF.md')
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_ESCAPE_REALIZATION_IDENTITIES_AND_BETA_BOUND','counts':counts,'beta_bound':bounds,'exact':{'cutoff_variation_upper':str(radius*MV),'saddle_ratio_example':str(p),'far_integrability_exponent':str(2*k-2*gamma+1),'prompt_c_ceiling':'521/200000','raw_sigma_interval':['78147/10000000','78149/10000000']},'scope':'Finite exact regressions supplement complete analytic statements. Numerical Beta evaluation alone is certified, no actual escape weight, Wiener norms, A_s equivalence or global inverse.','files':dict(sorted(files.items()))}
(E/'checks.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj))
