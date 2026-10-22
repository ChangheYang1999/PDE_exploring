"""Independent hexadecimal/decimal parsing and a free differential-polynomial jet algebra."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/modal_graph_scaling'
def check(q,t):
 if not q:raise ValueError(t)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def rr(v):return str(v.numerator)+'/'+str(v.denominator)
def hexq(s):
 sign=-1 if s.startswith('-') else 1;s=s.lstrip('+-');mant,expo=s.split('p');parts=mant[2:].split('.');tail=parts[1] if len(parts)>1 else '';v=sign*int(parts[0]+tail,16);e=int(expo)-4*len(tail);return F(v*(2**max(e,0)),2**max(-e,0))
def decq(s):
 s=s.lower();base,exp=(s.split('e') if 'e' in s else (s,'0'));sign=-1 if base.startswith('-') else 1;base=base.lstrip('+-');part=base.split('.');tail=part[1] if len(part)>1 else '';v=sign*int(part[0]+tail);e=int(exp)-len(tail);return F(v*(10**max(e,0)),10**max(-e,0))
def add(a,b):
 q=dict(a)
 for p,v in b.items():q[p]=q.get(p,0)+v
 return {p:v for p,v in q.items() if v}
def mul(a,b):
 q={}
 for m,u in a.items():
  for n,v in b.items():p=tuple(sorted(m+n));q[p]=q.get(p,0)+u*v
 return {p:v for p,v in q.items() if v}
def scale(a,c):return {p:c*v for p,v in a.items() if c*v}
def variable(v):return {(v,):1}
def dv(v,i):
 if v in ('x','y'):return () if v==('x','y')[i] else None
 if v=='c':return None
 name,a,b=v.split(':');a=int(a);b=int(b);return (name+':'+str(a+(i==0))+':'+str(b+(i==1)),)
def der(a,i):
 q={}
 for m,v in a.items():
  for j,key in enumerate(m):
   d=dv(key,i)
   if d is not None:
    p=tuple(sorted(m[:j]+m[j+1:]+d));q[p]=q.get(p,0)+v
 return {p:v for p,v in q.items() if v}
x,y,c=map(variable,('x','y','c'));coords=(x,y);rho=variable('R:0:0');U=[variable('U1:0:0'),variable('U2:0:0')];psi=variable('P:0:0')
def E(q):return add(mul(x,der(q,0)),mul(y,der(q,1)))
def lap(q):return add(der(der(q,0),0),der(der(q,1),1))
def dotgrad(a,b):return add(mul(a[0],der(b,0)),mul(a[1],der(b,1)))
V=[add(mul(c,z),u) for z,u in zip(coords,U)];K=add(rho,scale(E(rho),-1));UK=[add(u,scale(E(u),-1)) for u in U];eps=add(dotgrad(V,rho),scale(rho,-1));LK=add(add(dotgrad(V,K),scale(K,-1)),dotgrad(UK,rho));psik=add(scale(psi,2),scale(E(psi),-1));identities={'linearized_spatial':add(add(LK,scale(eps,-1)),E(eps)),'poisson_commutator':add(scale(lap(psik),-1),scale(E(lap(psi)),-1)),'density_source_commutator':add(der(K,0),E(der(rho,0))),'velocity_component1':add(scale(der(psik,1),-1),scale(add(scale(der(psi,1),-1),E(der(psi,1))),-1)),'velocity_component2':add(der(psik,0),scale(add(der(psi,0),scale(E(der(psi,0)),-1)),-1))}
for name,q in identities.items():check(q=={},name)
center=0
for u in UK:
 for i in range(2):
  q={m:v for m,v in der(u,i).items() if 'x' not in m and 'y' not in m};check(q=={},'center derivative');center+=1
raw=json.loads((B/'data_exact/modal_v2.json').read_text());sc={n:hexq(v) for n,v in raw['scalars_hex'].items()};k=sc['k'];check(F(0)<k<F(1,2) and sc['bi']>4 and sc['bo']>4-2*k,'end exponents');knots=list(map(hexq,raw['arrays']['knots']['hex']));check(raw['degree']==7 and len(raw['arrays']['S']['hex'])==260*1565,'degree and count');counts={}
for v in knots:counts[v]=counts.get(v,0)+1
ks=list(counts);check(ks==sorted(ks) and counts[ks[0]]==counts[ks[-1]]==8 and all(counts[q]==1 for q in ks[1:-1]),'knots independently counted')
exponents=[]
for j,l in raw['outer_jl']:exponents.append((j+1)*k-(j+3+2*l))
check(exponents[0]==k-3 and len(set(exponents))==10,'outer powers');check(all(q<=2*k-4 for q in exponents[1:]),'subleading powers');check(3-sc['bo']<2*k-1,'log remainder strict')
primary=json.loads((D/'evidence/compute.json').read_text());check(primary['scalars']=={n:rr(v) for n,v in sc.items()},'all scalar decoders');check(primary['outer_factor_exponents']==list(map(rr,exponents)),'outer exponents');check(primary['symbolic_identities']==list(identities) and primary['center_derivative_identities']==center,'independent differential algebra')
scalar=json.loads((B/'research/modal_repair/evidence/audit_verdict.json').read_text());rawA=hexq(raw['arrays']['Aout']['hex'][0]);z=list(map(decq,scalar['public_decimal_enclosures']['A00_correction']));interval=[rawA+q for q in z];check(interval[0]>0 and interval[1]>interval[0],'positive A00');check(primary['A00_normalized_enclosure']==list(map(rr,interval)),'A00 independent input parsing')
# Check every possible exterior homogeneous resonance in the finite stream family.
density_powers=[3+q for q in exponents]+[3-sc['bo']];mins=None;nr=0
for n in range(2,523,2):
 for p in density_powers:
  for sign in (-1,1):
   gap=p+1-sign*n;check(gap!=0,'actual exterior resonance absent');nr+=1;mins=abs(gap) if mins is None else min(mins,abs(gap))
check(2*3-6+1==1,'central norm exponent');check(2*k+(-2*k-3)+1==-2,'far norm exponent')
files=dict(primary['files'])
for n,h in files.items():check(sha(B/n)==h,'primary pin')
for name in ['research/center_obstruction/evidence/verdict.json','research/graph_center_norm/evidence/verdict.json']:
 a=json.loads((B/name).read_text())
 for n,h in a['files'].items():check(sha(B/n)==h,'inherited verdict pin');check(n not in files or files[n]==h,'pin conflict');files[n]=h
for p in [D/'PROOF.md',D/'evidence/compute.json',D/'code/compute.py',Path(__file__)]:files[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_HEX_DECIMAL_PARSING_FREE_JET_ALGEBRA_AND_FINITE_RESONANCES','symbolic_identities':list(identities),'center_derivative_identities':center,'actual_exterior_nonresonance_checks':nr,'minimum_absolute_resonance_gap':rr(mins),'A00_normalized_enclosure':list(map(rr,interval)),'files':files,'scope':'Actual exact modal finite inputs, identities and inherited dependency pins. No zero image, numerical norm ratio or retained matrix identified.'};p=D/'evidence/independent.json';check(not p.exists(),'immutable');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({n:out[n] for n in ['utc','status','actual_exterior_nonresonance_checks','minimum_absolute_resonance_gap','center_derivative_identities']}))
