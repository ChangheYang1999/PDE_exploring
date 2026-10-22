"""Exact matrix identities and two interval systems for explicit example parameters."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,sys
from flint import arb,ctx,fmpq
from mpmath import iv
assert not sys.flags.optimize
ctx.prec=512;ctx.threads=1;iv.dps=180
B=Path(__file__).resolve().parents[3];D=B/'research/semigroup_implication';E=D/'evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def matmul(x,y):return [[sum(x[i][k]*y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def add(x,y):return [[x[i][j]+y[i][j] for j in range(2)] for i in range(2)]
def scale(c,x):return [[c*v for v in row] for row in x]
def qa(x):x=F(x);return arb(fmpq(x.numerator,x.denominator))
def qi(x):x=F(x);return iv.mpf(x.numerator)/x.denominator
def ends(v):
 if isinstance(v,arb):
  assert v.is_finite()
  def cv(z):m,e=z.man_exp();return F(int(m))*F(2)**int(e)
  return cv(v.lower()),cv(v.upper())
 def cv(z):s,m,e,bc=z;assert bc>=0;return F((-1 if s else 1)*int(m))*F(2)**int(e)
 return tuple(map(cv,v._mpi_))
I=[[F(1),F(0)],[F(0),F(1)]];Q=[[F(1),F(0)],[F(0),F(0)]];Z=scale(0,I)
identities=0;cases=0;intervals=0;exact_cases=[]
for a in [F(1,4),F(1),F(7,3),F(10)]:
 for b in [F(-7,3),F(1,2),F(5)]:
  L=[[-a,b],[F(0),F(0)]];C=scale(-1/a,Q)
  assert matmul(L,L)==scale(-a,L);identities+=1
  assert matmul(L,C)==Q and matmul(C,matmul(L,Q))==Q;identities+=2
  # For formal q the polynomial identity L(I+(1-q)L/a)=qL
  assert add(L,scale(1/a,matmul(L,L)))==Z and scale(-1/a,matmul(L,L))==L;identities+=2
  assert matmul(L,Q)==scale(-a,Q);identities+=1
  # Semigroup product on q1,q2; polynomial coefficient comparison in (1-q).
  # (I+cL)(I+dL)=I+(c+d-a*c*d)L and c(q1*q2)=c+d-a*c*d.
  for q1,q2 in [(F(1,3),F(2,5)),(F(4,7),F(8,9))]:
   c=(1-q1)/a;d=(1-q2)/a
   assert c+d-a*c*d==(1-q1*q2)/a;identities+=1
   assert matmul(add(I,scale(c,L)),add(I,scale(d,L)))==add(I,scale((1-q1*q2)/a,L));identities+=1
  for t in [F(1,10),F(1),F(5)]:
   for tag,q,exp in [('arb',qa,lambda x:x.exp()),('iv',qi,iv.exp)]:
    e=exp(-q(a)*q(t));l,u=ends(e);assert 0<l<=u<1
    off=q(b)*(1-e)/q(a);lo,hi=ends(off);assert (lo>0 if b>0 else hi<0)
    # Exact finite integral plus an exponential remainder gives the inverse coefficient.
    partial=-(1-e)/q(a);tail=-e/q(a);s=partial+tail;sl,su=ends(s);assert sl<=-1/a<=su
    intervals+=3
  exact_cases.append({'a':str(a),'b':str(b),'inverse_on_N':str(-1/a),'decay_K':'1','decay_lambda':str(a),'full_generator_determinant':'0'})
  cases+=1
assert cases==12 and identities==120 and intervals==216
# Explicit shifted support has symmetric difference of measure 2 min(t,1), hence cannot agree up to a scalar.
supports=[]
for t in [F(1,10),F(1,2),F(1),F(2)]:
 inter=max(F(0),min(F(1),F(1)-t)-max(F(0),-t));diff=2-2*inter
 assert diff==2*min(t,F(1))>0;supports.append({'t':str(t),'symmetric_difference_measure':str(diff)})
files={str(p.relative_to(B)):sha(p) for p in [D/'PROOF.md',D/'ADDENDUM.md',Path(__file__)]}
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_SEMIGROUP_REGRESSIONS','counts':{'rational_matrix_parameter_cases':cases,'exact_matrix_and_parameter_identities':identities,'directed_interval_inequalities':intervals,'translated_support_checks':len(supports)},'matrix_cases':exact_cases,'shifted_support_examples':supports,'scope':'Exact regression examples for the proved analytic semigroup implication. Not a computational proof of the Banach theorem or an IPM decay estimate.','files':files}
(E/'checks.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({k:v for k,v in obj.items() if k not in ['files','matrix_cases','shifted_support_examples']}))
