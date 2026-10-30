"""Exact triangular origin projection and an independent whole-plane size bound."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
from math import factorial
from hashlib import sha256
from datetime import datetime,timezone
import json,sys,time
from flint import arb,ctx
import jets as J
sys.set_int_max_str_digits(0);ctx.prec=512
b=Path(__file__).resolve().parents[1];s=b/'source';start=time.monotonic()
hashof=lambda p:sha256(p.read_bytes()).hexdigest()
for name,h in json.loads((s/'MANIFEST.json').read_text()).items():assert hashof(s/name)==h
raw=json.loads((s/'canonical007.json').read_text());previous=json.loads((s/'constraint_result.json').read_text())
c=J.c;p=J.p0;assert Q(raw['cl'])==c
coeff={tuple(map(int,k)):Q(v) for k,v in zip(raw['order'],raw['coefficients'])}
phi={}
for (j,m,k),v in coeff.items():
 if k<=4:phi=J.add(phi,J.scale(J.canonical_jet(j,m,k),v))
pairs=[(2,1),(0,3),(3,1),(1,3),(0,4)]
etas=[];members=[]
for a,z in pairs:
 l=a+z;M={(a,z):Q(1)}
 etas.append(J.add(*(J.scale(J.mul(M,J.radial(k)),J.binomial(p-l-2,k)) for k in range(5-l))))
 members.append(next(x['membership'] for x in previous['directions'] if (x['a'],x['b'])==(a,z)))
keys=[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]
def extract(ph):
 f=J.residual(ph);return [f.get(k,Q(0)) for k in keys]
def project(ph):
 R,U,W=J.fields(ph);a=R.get((0,0),Q(0));assert W.get((0,0),Q(0))==1-c
 assert a-4*c+2 and a-8*c+4
 f=extract(ph);alpha=-f[1]/(24*(a-4*c+2));beta=f[2]/240
 ph1=J.add(ph,J.scale(etas[0],alpha),J.scale(etas[1],beta));g=extract(ph1);assert g[:3]==[0,0,0]
 gamma=-g[3]/(60*(a-8*c+4));delta=g[4]/(480*c);epsilon=(g[5]+12*(a-4)*delta)/1344
 ts=[alpha,beta,gamma,delta,epsilon]
 ph2=J.add(ph,*(J.scale(e,t) for e,t in zip(etas,ts)));assert extract(ph2)==[0]*6
 return ph2,ts,g
patched,ts,intermediate=project(phi)
assert project(patched)[1]==[0]*5
assert [J.fields(patched)[i].get((0,0),Q(0)) for i in range(3)]==[J.fields(phi)[i].get((0,0),Q(0)) for i in range(3)]
# Reconstruct the correction in exact canonical coordinates and check all tail rows.
changes=defaultdict(Q)
for t,entries in zip(ts,members):
 for row in entries:
  m=int(row['m'])
  for w,v in row['polynomial'].items():changes[0,m,m+int(w)]+=t*Q(v)
changes={k:v for k,v in changes.items() if v}
for key in changes:assert key in coeff
ph3={}
for key,v in {k:coeff[k]+changes.get(k,Q(0)) for k in coeff}.items():
 j,m,k=key
 if k<=4:ph3=J.add(ph3,J.scale(J.canonical_jet(j,m,k),v))
assert ph3==patched and extract(ph3)==[0]*6
for m in set(k[1] for k in changes):
 vals=[(k,v) for (j,n,k),v in changes.items() if n==m]
 assert sum((v for k,v in vals),Q(0))==0
 assert sum(((p-k)*v for k,v in vals),Q(0))==0
# Cartesian polynomial differentiation for the independent size bound.
def add(*ps):
 out=defaultdict(Q)
 for poly in ps:
  for key,value in poly.items():out[key]+=value
 return {k:v for k,v in out.items() if v}
def scale(poly,v):return {k:x*v for k,x in poly.items() if x*v}
def shift(poly,axis,n=1):
 out={}
 for k,v in poly.items():j=list(k);j[axis]+=n;out[tuple(j)]=v
 return out
def diff(poly,axis):
 out={}
 for k,v in poly.items():
  if k[axis]:j=list(k);j[axis]-=1;out[tuple(j)]=v*k[axis]
 return out
def D(poly,q,axis):
 derivative=diff(poly,axis)
 return add(derivative,shift(derivative,0,2),shift(derivative,1,2),scale(shift(poly,axis),2*q))
def density(a,z):
 l=a+z;q=p-l-2;M={(2*a,2*z):Q(1)}
 lap=add(D(D(M,q,0),q-1,0),D(D(M,q,1),q-1,1))
 return scale(D(lap,q-2,1),-1),2*l+7-1/c
def moment(u,v,A):
 ans=Q(factorial(2*u)*factorial(2*v),4**(u+v)*factorial(u)*factorial(v))
 for k in range(1,u+v+2):assert A-k>0;ans/=A-k
 return ans
def rationalnorm(H,A):
 val=Q(0)
 for (a,z),x in H.items():
  for (aa,zz),y in H.items():
   assert (a+aa)%2==0 and (z+zz)%2==0
   val+=x*y*moment((a+aa)//2,(z+zz)//2,A)
 assert val>0;return val
def ball(q):return arb(q.numerator)/arb(q.denominator)
ns=[];bound=arb(0)
for pair,t in zip(pairs,ts):
 H,A=density(*pair);n=rationalnorm(H,A);bb=(arb.pi()*ball(n)).sqrt();bound+=ball(abs(t))*bb
 ns.append({'pair':list(pair),'squared_L2_over_pi':str(n),'L2_ball':bb.str(55)})
assert bound<arb('1e-10')
parameters=[{'pair':list(pair),'coefficient':str(t),'coefficient_ball':ball(t).str(55)} for pair,t in zip(pairs,ts)]
par={'format':'exact rational Taylor correction, unregistered algebraic artifact','source_canonical_sha256':hashof(s/'canonical007.json'),'c':str(c),'parameters':parameters,'canonical_changes':[{'index':list(k),'coefficient':str(v)} for k,v in sorted(changes.items())]}
with (b/'verification/parameters.json').open('x') as f:json.dump(par,f,indent=2);f.write('\n')
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'initial_residual_balls':[ball(x).str(50) for x in extract(phi)],'intermediate_residual_balls':[ball(x).str(50) for x in intermediate],'final_six_residual_coefficients':['0']*6,'a0_strain_preserved':True,'all_tail_rows_preserved':True,'canonical_reconstruction_matches':True,'idempotence_exact':True,'parameters_file_sha256':hashof(b/'verification/parameters.json'),'direction_norms':ns,'density_L2_upper_bound_ball':bound.str(65),'strict_density_L2_upper_bound':'1e-10','code_sha256':hashof(Path(__file__)),'jets_sha256':hashof(Path(__file__).with_name('jets.py')),'proof_sha256':hashof(b/'PROOF.md'),'source_manifest_sha256':hashof(s/'MANIFEST.json'),'status':'Exact checks pass locally; OPEN independent Opus theorem and numerical-lane reproduction. Not a published candidate or an existence proof.'}
with (b/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in out.items() if k!='direction_norms'},indent=2))
print('parameter balls',[x['coefficient_ball'] for x in parameters])
print('direction norm balls',[x['L2_ball'] for x in ns])
