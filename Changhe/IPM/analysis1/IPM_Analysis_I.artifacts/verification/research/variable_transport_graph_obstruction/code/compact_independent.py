from pathlib import Path
from fractions import Fraction as F
import sys
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[3];P=R/'research/variable_transport_graph_obstruction';E=P/'evidence';sys.path.insert(0,str(R/'research/full_derivative_norm_bound_v2/code'));import protocol as p
start=p.now();a=p.load(E/'compact_check.json');assert a['proof_sha256']==p.sha(P/'COMPACT_VELOCITY_PROOF.md')=='1079a79a6995ed608fc21d60e221c90a3e9d253ca3fc6574456d0b3752d63342'
# Laurent differential polynomials after factoring x^beta exp(t Phi), t=i*n.
# Keys: x-power,y-power,b_z-order,b_y-order,A-power,D-power,beta-power,t-power.
Z=(0,)*8

def mon(**kw):
 names=['x','y','bz','by','A','D','beta','t'];return {tuple(kw.get(n,0) for n in names):F(1)}
def add(*qs):
 out={}
 for q in qs:
  for t,v in q.items():out[t]=out.get(t,F())+v
 return {t:v for t,v in out.items() if v}
def scale(q,c):return {t:v*F(c) for t,v in q.items() if v*c}
def shift(q,**kw):
 names=['x','y','bz','by','A','D','beta','t'];delta=tuple(kw.get(n,0) for n in names);return {tuple(i+j for i,j in zip(t,delta)):v for t,v in q.items()}
def dx(q):
 out={}
 for key,value in q.items():
  term={key:value}
  out=add(out,scale(shift(term,x=-1),key[0]),shift(term,x=-1,beta=1),shift(term,x=-1,D=1,t=1),shift(term,x=-1,bz=1))
 return out
def dy(q):
 out={}
 for key,value in q.items():
  term={key:value}
  out=add(out,scale(shift(term,y=-1),key[1]),shift(term,y=-1,A=1,t=1),shift(term,by=1))
 return out
base=mon();xx=dx(dx(base));yy=dy(dy(base));lap=add(xx,yy)
B0=add(mon(x=-2,bz=2),scale(mon(x=-2,beta=1,bz=1),2),scale(mon(x=-2,bz=1),-1),mon(x=-2,beta=2),scale(mon(x=-2,beta=1),-1),mon(by=2))
B1=add(scale(mon(x=-2,D=1,bz=1),2),scale(mon(x=-2,D=1,beta=1),2),scale(mon(x=-2,D=1),-1),scale(mon(y=-1,A=1,by=1),2),scale(mon(y=-2,A=1),-1))
Rphi=add(mon(x=-2,D=2),mon(y=-2,A=2));assert lap==add(B0,shift(B1,t=1),shift(Rphi,t=2))
u1=scale(dx(dy(base)),-1);u2=xx
# Change t^2=-n^2; removing the t^2 index gives the leading n^2 terms.
def n2(q):return {t[:-1]+(0,):-v for t,v in q.items() if t[-1]==2}
assert n2(scale(lap,-1))==Rphi
assert n2(u1)==mon(x=-1,y=-1,A=1,D=1)
assert n2(u2)==scale(mon(x=-2,D=2),-1)
assert not add(dx(u1),dy(u2))
assert add(dx(u2),scale(dy(u1),-1))==dx(lap)
assert dx(dy(base))==dy(dx(base))
h=scale(lap,-1);Th=add(scale(shift(dx(h),x=1,A=1),-1),shift(dy(h),y=1,D=1),scale(h,-1));assert max(k[-1] for k in h)==2 and max(k[-1] for k in Th)==2
checks=['complete_Laurent_Laplacian','positive_density_phase_square','velocity1_leading_coefficient','velocity2_leading_coefficient','full_divergence_identity','full_curl_identity','mixed_derivative_commutation','frozen_differentiation_does_not_raise_phase_degree']
out={'start_utc':start,'utc':p.now(),'status':'PASS_INDEPENDENT_LAURENT_DIFFERENTIAL_POLYNOMIAL_COMPACT_CHECKS','proof_sha256':p.sha(P/'COMPACT_VELOCITY_PROOF.md'),'code_sha256':p.sha(Path(__file__)),'primary_sha256':p.sha(E/'compact_check.json'),'exact_checks':checks,'polynomial_term_counts':{'Laplacian':len(lap),'velocity1':len(u1),'velocity2':len(u2),'density':len(h),'frozen_image':len(Th)},'scope':'No Sympy, no input formulas from primary. The primitive product/chain rules generate the full Cartesian jets. Analytic function-space conclusions remain proof claims.'};p.write(E/'compact_independent.json',out);print(out)
