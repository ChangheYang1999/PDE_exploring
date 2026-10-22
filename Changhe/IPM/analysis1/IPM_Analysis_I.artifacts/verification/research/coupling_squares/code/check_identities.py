"""Exact independent regression checks for the analytic coupling statements."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,itertools,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/coupling_squares';E=D/'evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def neg(a):return [[-x for x in r] for r in a]
def sub(a,b):return add(a,neg(b))
def mul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def scale(a,c):return [[x*c for x in r] for r in a]
def trans(a):return [list(r) for r in zip(*a)]
def comm(a,b):return sub(mul(a,b),mul(b,a))
def diag(v):return [[v[i] if i==j else F() for j in range(len(v))] for i in range(len(v))]
I=diag([F(1)]*3);zero=scale(I,0)
R=[diag([F(3,5),F(5,13),F(8,17)]),diag([F(4,5),F(12,13),F(15,17)])]
assert add(mul(R[0],R[0]),mul(R[1],R[1]))==I
# Multiplication coefficients need not commute with the Riesz multipliers.
a=[[F(v) for v in row] for row in [[1,2,0],[2,-1,1],[0,1,3]]]
c=[[F(v) for v in row] for row in [[2,0,1],[0,3,-1],[1,-1,2]]]
b=scale(I,20);BB=[[add(b,c),scale(a,F(-1,2))],[scale(a,F(-1,2)),b]]
T=sub(mul(a,mul(R[0],R[1])),mul(c,mul(R[0],R[0])));S=zero;C=zero;DD=zero
for i,j in itertools.product(range(2),repeat=2):
 S=add(S,mul(mul(R[i],BB[i][j]),R[j]));C=add(C,mul(comm(R[i],BB[i][j]),R[j]));DD=add(DD,comm(R[i],comm(R[j],BB[i][j])))
assert T==add(sub(b,S),C)
A=sub(b,T);assert DD==sub(add(A,trans(A)),scale(S,2))
assert add(T,trans(T))==sub(scale(sub(b,S),2),DD)
# Check PSD of the six-by-six B by strict row diagonal dominance.
block=[BB[0][0][i]+BB[0][1][i] for i in range(3)]+[BB[1][0][i]+BB[1][1][i] for i in range(3)]
assert all(block[i][i]>sum(abs(x) for j,x in enumerate(block[i]) if i!=j) for i in range(6))
# Rational unit-circle points allow exact squared frequency checks.
points=[]
for t in [F(-3),F(-1),F(-1,2),F(),F(1,3),F(1),F(4)]:points.append(((1-t*t)/(1+t*t),2*t/(1+t*t)))
checks=0
for n,k,r,s in itertools.product(points,points,[F(1,10),F(1),F(5)],[F(1,7),F(2),F(11)]):
 xi=[r*x for x in n];eta=[s*x for x in k];p=[x-y for x,y in zip(xi,eta)];p2=sum(x*x for x in p);dx=sum((x-y)**2 for x,y in zip(n,k))
 assert dx<=4 and dx*s*s<=4*p2 and dx*r*r<=4*p2
 assert dx*(1+s*s)<=4*(1+p2) and dx*(1+r*r)<=4*(1+p2)
 assert 1+r*r<=2*(1+p2)*(1+s*s)
 mn=[n[0]*n[1],-n[0]*n[0]];mk=[k[0]*k[1],-k[0]*k[0]];cross=n[0]*k[1]-n[1]*k[0]
 assert sum((x-y)**2 for x,y in zip(mn,mk))==cross*cross<=dx
 assert mn[0]**2+mn[1]**2==n[0]**2;checks+=8
# The source directional gap is established by exact box extrema, not sampling.
s=F(31,10);kappa=F(1687,500);lam=F(449,1000);corners=[]
for A,mu,g in itertools.product([F(10),F(51,5)],[F(99,100),F(101,100)],[F(29),F(30)]):
 slow=-1-A/2+(s-F(1,2))*mu;slope=s*(A-mu)-g
 assert slow<=-kappa and slope<=-lam
 corners.append({'A':str(A),'mu':str(mu),'g':str(g),'slow':str(slow),'slope':str(slope)})
assert max(F(x['slow']) for x in corners)==-kappa and max(F(x['slope']) for x in corners)==-lam
# Counterexample and scalar square completion, including endpoint regime.
quadchecks=0
for g,eps in [(F(29),F(1)),(F(29),F(58)),(F(29),F(70)),(lam,F(1,40))]:
 tstar=min(F(1),eps/(2*g));peak=-g*tstar*tstar+eps*tstar;target=eps*eps/(4*g) if eps<=2*g else eps-g;assert peak==target
 for t in [F(i,40) for i in range(41)]:assert -g*t*t+eps*t<=target;quadchecks+=1
assert F(1)>F(1,4*29) and F(29)-1>0
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_COUPLING_IDENTITIES_AND_SOURCE_BOX','counts':{'noncommuting_matrix_identities':4,'exact_frequency_inequalities':checks,'source_box_corners':8,'quadratic_cases':quadchecks},'directional_gap_exact':str(lam),'source_margin_exact':str(kappa),'corners':corners,'scope':'Exact regression checks complement the complete analytic proof. Finite checks are not substituted for universal inequalities or actual global coefficient norms.','files':{str(p.relative_to(B)):sha(p) for p in [Path(__file__),D/'PROOF.md',E/'proof_first.json']}}
(E/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['utc','status','counts','directional_gap_exact']}))
