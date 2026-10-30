"""Constraint-rank reproduction using squared-coordinate polynomial jets."""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
from math import comb
from collections import defaultdict
import json,sys,time
from flint import fmpq_mat,arb,ctx
sys.set_int_max_str_digits(0)
base=Path(__file__).resolve().parents[1];src=base/'source';start=time.monotonic();ctx.prec=768
hashof=lambda p:sha256(p.read_bytes()).hexdigest()
for name,rec in json.loads((src/'MANIFEST.json').read_text()).items():assert hashof(src/name)==rec['sha256']
raw=json.loads((src/'candidate007.json').read_text());can=json.loads((src/'canonical007.json').read_text());peer=json.loads((src/'N4_result.json').read_text())
c=Q(can['cl']);delta=1-1/c;p0=(3+1/c)/2
assert c==Q(4076476460239181,2251799813685248)
def add(*ps):
 out=defaultdict(Q)
 for p in ps:
  for k,v in p.items():out[k]+=v
 return {k:v for k,v in out.items() if v}
def scale(p,v):return {k:x*v for k,x in p.items() if x*v}
def mul(p,q,degree=4):
 out=defaultdict(Q)
 for (a,b),v in p.items():
  for (d,e),w in q.items():
   if a+b+d+e<=degree:out[a+d,b+e]+=v*w
 return {k:v for k,v in out.items() if v}
def diff(p,axis):
 out={}
 for k,v in p.items():
  if k[axis]:
   j=list(k);j[axis]-=1;out[tuple(j)]=v*k[axis]
 return out
def dx(p):return diff(p,0)
def dy(p):return diff(p,1)
X={(1,0):Q(1)};Y={(0,1):Q(1)}
def binomial(x,n):
 out=Q(1)
 for j in range(n):out*= (x-j)/(j+1)
 return out
def radial(n):return {(i,n-i):Q(comb(n,i)) for i in range(n+1)}
def harmonic(m):return {(m-j,j):Q((-1)**j*comb(2*m,2*j)) for j in range(m+1)}
def canonical_jet(j,m,k):
 if k>4:return {}
 assert k>=m>=0
 p=p0-j*delta/2
 return add(*(scale(mul(harmonic(m),radial(k-m+l)),binomial(p-k,l)) for l in range(5-k)))
def fields(phi):
 xy=dx(dy(phi));xxy=dx(xy);xyy=dy(xy);yyy=dy(dy(dy(phi)))
 R=add(scale(xy,-4),scale(dy(dy(phi)),-12),scale(mul(X,xxy),-8),scale(mul(Y,yyy),-8))
 U=add(scale(xy,-4),scale(mul(Y,xyy),-8));W=add(scale(xy,4),scale(mul(X,xxy),8))
 return R,U,W
def residual(phi):
 R,U,W=fields(phi)
 return add(scale(mul(X,mul(add({(0,0):c},U),dx(R)),2),2),scale(mul(Y,mul(add({(0,0):c},W),dy(R)),2),2),mul(add({(0,0):c-1},W),R,2))
def linear(phi,eta):
 R,U,W=fields(phi);h,u,w=fields(eta)
 return add(scale(mul(X,add(mul(u,dx(R)),mul(add({(0,0):c},U),dx(h))),2),2),scale(mul(Y,add(mul(w,dy(R)),mul(add({(0,0):c},W),dy(h))),2),2),mul(w,R,2),mul(add({(0,0):c-1},W),h,2))
phi={}
for (j,m,k),cf in zip(can['order'],can['coefficients']):
 if int(k)<=4:phi=add(phi,scale(canonical_jet(int(j),int(m),int(k)),Q(cf)))
R,U,W=fields(phi);a0=R.get((0,0),Q(0));strain=W.get((0,0),Q(0))
assert a0==Q(can['a0'])==Q(peer['a0_exact'])
assert strain==1-c==Q(peer['strain_exact'])
assert U.get((0,0),0)==c-1
keys=[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]
rf=residual(phi);taylor=[rf.get(k,Q(0)) for k in keys]
assert taylor==list(map(Q,peer['Taylor_residual_exact']))
assert taylor[0]==0 and all(v!=0 for v in taylor[1:])
factors=[a0-4*c+2,a0-8*c+4];assert factors[0]>0 and factors[1]<0
# Tail functionals from independent explicit shifted-Legendre coefficients.
groups=defaultdict(list)
def polynomial(spec):
 if spec[0]=='mono':return {int(spec[1]):Q(1)}
 assert spec[0]=='leg';w,n=int(spec[1]),int(spec[2])
 return {w+k:Q((-1)**(n-k)*comb(n,k)*comb(n+k,k)) for k in range(n+1)}
for i,g in enumerate(raw['generators']):groups[int(g['j']),int(g['m'])].append((i,g,polynomial(g['spec'])))
tail=[]
for (j,m),rows in sorted(groups.items()):
 vals=[]
 for i,g,p in rows:
  l0=sum(p.values(),Q(0));l1=(p0-j*delta/2-m)*l0-sum((k*v for k,v in p.items()),Q(0));assert l0==1
  vals.append((i,l0,l1))
 x=vals[0];count=1;det=x[1]
 if j<=2:
  y=next(y for y in vals if x[1]*y[2]-x[2]*y[1]);count=2;det=x[1]*y[2]-x[2]*y[1]
 tail.append({'j':j,'m':m,'rank':count,'minor':str(det)})
assert len(tail)==360 and sum(x['rank'] for x in tail)==420
columns=[];directions=[]
for a,b in [(1,1),(2,1),(0,3),(3,1),(1,3),(0,4)]:
 l=a+b;M={(a,b):Q(1)}
 eta=add(*(scale(mul(M,radial(q)),binomial(p0-l-2,q)) for q in range(5-l)))
 # Exact angular decomposition uses a small rational matrix only.
 basis=[mul(harmonic(m),radial(l-m)) for m in range(l+1)]
 mat=fmpq_mat([[str(basis[m].get((i,l-i),Q(0))) for m in range(l+1)] for i in range(l+1)])
 rhs=fmpq_mat([[int(i==a)] for i in range(l+1)]);sol=mat.solve(rhs)
 weights=[Q(str(sol[m,0])) for m in range(l+1)]
 assert add(*(scale(basis[m],weights[m]) for m in range(l+1)))==M
 eta2={};membership=[]
 for m,q in enumerate(weights):
  if not q:continue
  pol={l-m:q,l-m+1:-2*q,l-m+2:q}
  assert sum(pol.values())==0 and sum(k*v for k,v in pol.items())==0
  mono={int(g['spec'][1]) for i,g,p in groups[0,m] if g['spec'][0]=='mono'}
  assert set(pol)<=mono
  membership.append({'m':m,'polynomial':{str(k):str(v) for k,v in pol.items()}})
  for w,z in pol.items():eta2=add(eta2,scale(canonical_jet(0,m,m+w),z))
 assert eta2==eta
 col=[fields(eta)[2].get((0,0),Q(0))]+[linear(phi,eta).get(k,Q(0)) for k in keys[1:]]
 match=next(x for x in peer['directions'] if x['a']==a and x['b']==b)
 assert col==[Q(match['strain'])]+list(map(Q,match['Taylor_differential']))
 columns.append(col);directions.append({'a':a,'b':b,'membership':membership,'column':[str(v) for v in col]})
matrix=fmpq_mat([[str(columns[j][i]) for j in range(6)] for i in range(6)])
det=Q(str(matrix.det()));formula=4*24*factors[0]*(-240)*60*factors[1]*(-480*c)*(-1344)
assert det==formula==Q(peer['determinant_exact']) and det!=0
assert [peer[k] for k in ['linear_constraint_rank','full_constraint_rank','constrained_potential_tangent_dimension','constrained_generator_tangent_dimension']]==[421,426,1496,2556]
def ball(q):return (arb(q.numerator)/arb(q.denominator)).str(65)
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'tail_rank':420,'linear_rank':421,'full_differential_rank':426,'potential_tangent_dimension':1496,'coefficient_tangent_dimension':2556,'a0_exact':str(a0),'a0_ball':ball(a0),'nonzero_factors_exact':list(map(str,factors)),'nonzero_factor_balls':list(map(ball,factors)),'Taylor_coefficients_exact':list(map(str,taylor)),'Taylor_coefficient_balls':list(map(ball,taylor)),'Taylor_constant_exact_zero':True,'five_other_Taylor_coefficients_exact_nonzero':True,'determinant_exact':str(det),'tail_minor_witnesses':tail,'directions':directions,'proof_sha256':hashof(base/'PROOF.md'),'code_sha256':hashof(Path(__file__)),'source_manifest_sha256':hashof(src/'MANIFEST.json'),'status':'CONFIRMED exact constraint rank and Taylor non-feasibility; no PDE Jacobian rank or inverse conclusion.'}
with (base/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in out.items() if k in ['utc','elapsed_seconds','tail_rank','linear_rank','full_differential_rank','potential_tangent_dimension','coefficient_tangent_dimension','a0_ball','nonzero_factor_balls','Taylor_coefficient_balls','status']},indent=2))
