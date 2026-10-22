"""Independent exact physical-coordinate finite Taylor checks.
Polynomial dictionaries and Fraction arithmetic; no generating evaluator import.
All operations truncate by total degree. No formal-series convergence claim.
"""
from pathlib import Path
from fractions import Fraction as F
import datetime,json
out=Path('research/formal_local_jets/verification');out.mkdir(parents=True,exist_ok=True)
D=10

def add(*polys):
 q={}
 for p in polys:
  for m,v in p.items():q[m]=q.get(m,F(0))+v
 return {m:v for m,v in q.items() if v and sum(m)<=D}
def scale(p,c):return {m:v*c for m,v in p.items() if v*c}
def mul(p,q):
 a={}
 for (i,j),v in p.items():
  for (k,l),w in q.items():
   if i+j+k+l<=D:
    m=(i+k,j+l);a[m]=a.get(m,F(0))+v*w
 return {m:v for m,v in a.items() if v}
def power(p,n):
 q={(0,0):F(1)}
 for _ in range(n):q=mul(q,p)
 return q
def diff(p,axis):
 q={}
 for m,v in p.items():
  if m[axis]:
   mm=list(m);mm[axis]-=1;q[tuple(mm)]=v*m[axis]
 return q
def cut(p,n):return {m:v for m,v in p.items() if sum(m)<=n}
def homog(p,n):return {m:v for m,v in p.items() if sum(m)==n}
def compose_eta(p,eta):
 q={};powers={j:power(eta,j) for j in {m[1] for m in p}}
 for (i,j),v in p.items():q=add(q,mul({(i,0):v},powers[j]))
 return q
X={(1,0):F(1)};Y={(0,1):F(1)}
def physical(g,beta,a0):
 # Explicit formal reversion, independent of the mixed-coordinate differential operators.
 nonlinear=add(diff(g,0),scale(Y,-1));eta=Y.copy()
 for _ in range(D+1):eta=add(Y,scale(compose_eta(nonlinear,eta),-1))
 assert not cut(add(compose_eta(diff(g,0),eta),scale(Y,-1)),D)
 psi_mixed=add(scale(mul(X,diff(g,0)),beta),scale(mul(Y,diff(g,1)),beta-2),scale(g,-2*beta))
 psi=compose_eta(psi_mixed,eta);theta=scale(eta,a0)
 u1=scale(diff(psi,1),-1);u2=diff(psi,0)
 om=scale(add(diff(diff(psi,0),0),diff(diff(psi,1),1)),-1)
 w1=add(scale(X,beta),u1);w2=add(scale(Y,beta),u2)
 rt=add(mul(w1,diff(theta,0)),mul(w2,diff(theta,1)),scale(theta,-(beta-2)))
 ro=add(mul(w1,diff(om,0)),mul(w2,diff(om,1)),om,scale(diff(theta,0),-1))
 return dict(eta=eta,psi=psi,theta=theta,omega=om,rt=rt,ro=ro)
def expected_column(beta,a0,N,a):
 c=N-a;alpha=beta+2;b=beta-2;M=alpha*a+b*c;q={}
 if a>=3:q[(a-2,c)]=a*(a-1)*(a0-(M-2*beta)*(M-2*alpha+1))
 if c>=3:q[(a,c-2)]=-c*(c-1)*(M-2*beta)*(M-2*b+1)
 return {k:v for k,v in q.items() if v}
def solve(matrix,rhs):
 n=len(rhs);a=[list(row)+[rhs[i]] for i,row in enumerate(matrix)]
 for i in range(n):
  assert a[i][i]
  pivot=a[i][i];a[i]=[v/pivot for v in a[i]]
  for j in range(i+1,n):
   c=a[j][i]
   if c:a[j]=[a[j][k]-c*a[i][k] for k in range(n+1)]
 ans=[F(0)]*n
 for i in reversed(range(n)):ans[i]=a[i][-1]-sum(a[i][j]*ans[j] for j in range(i+1,n))
 return ans
records=[]
for beta,a0 in [(F(3),F(50)),(F(5,2),F(-9,2)),(F(7),F(756,11)),(F(3),F(108))]:
 g={(1,1):F(1)};stages=[]
 for N in [4,6,8]:
  # Degree N source modifies residual degree N-2, and every older jet stays fixed.
  base=physical(g,beta,a0);res=homog(base['ro'],N-2);cols=list(range(1,N,2));rows=[(a,N-2-a) for a in cols[:-1]]
  actual=[]
  for a in cols:
   test=physical(add(g,{(a,N-a):F(1)}),beta,a0)
   col=homog(add(test['ro'],scale(base['ro'],-1)),N-2)
   assert col==expected_column(beta,a0,N,a),(beta,a0,N,a,col,expected_column(beta,a0,N,a))
   assert not cut(add(test['ro'],scale(base['ro'],-1)),N-4)
   actual.append([col.get(row,F(0)) for row in rows])
  matrix=[[actual[j][i] for j in range(len(rows))] for i in range(len(rows))]
  assert all(matrix[i][j]==0 for i in range(len(rows)) for j in range(i))
  assert all(matrix[i][i]<0 for i in range(len(rows)))
  free={4:F(1,7),6:F(-2,11),8:F(3,13)}[N]
  rhs=[-res.get(row,F(0))-actual[-1][i]*free for i,row in enumerate(rows)]
  coefficients=solve(matrix,rhs)+[free]
  hn={(a,N-a):c for a,c in zip(cols,coefficients)};g=add(g,hn)
  check=physical(g,beta,a0)
  assert not cut(check['ro'],N-2),(beta,a0,N,cut(check['ro'],N-2))
  assert not cut(check['rt'],N-1)
  assert check['psi'].get((1,1))==-2 and check['theta'].get((0,1))==a0
  assert all(i%2==0 and j%2==1 for i,j in check['theta'])
  assert all(i%2==1 and j%2==1 for i,j in check['psi'])
  assert all(i%2==1 and j%2==1 for i,j in check['omega'])
  if N==4:assert check['omega'].get((1,1))==-6*a0*free/(2*beta+1)
  stages.append(dict(degree=N,monomials=[list(m) for m in hn],coefficients=[str(c) for c in hn.values()],diagonal=[str(matrix[i][i]) for i in range(len(rows))],residual_vanishes_through=N-2,temperature_vanishes_through=N-1,all_linear_columns_confirmed=True))
  print(json.dumps(dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),beta=str(beta),a0=str(a0),degree=N,event='exact_checks_passed')),flush=True)
 records.append(dict(beta=str(beta),a0=str(a0),stages=stages))
# Independently verify the displayed homogeneous linear operator symbolically.
import sympy as sp
x,y,bb,aa=sp.symbols('x y beta a0');alpha=bb+2;b=bb-2
L=lambda p:alpha*x*sp.diff(p,x)+b*y*sp.diff(p,y)
for N in [4,6,8,10,12]:
 for a in range(1,N,2):
  c=N-a;h=x**a*y**c;t=L(h)-2*bb*h;lap=sp.diff(t,x,2)+sp.diff(t,y,2)
  got=sp.expand(-L(lap)-lap+aa*sp.diff(h,x,2));M=alpha*a+b*c
  expect=0
  if a>=3:expect+=a*(a-1)*(aa-(M-2*bb)*(M-2*alpha+1))*x**(a-2)*y**c
  if c>=3:expect-=c*(c-1)*(M-2*bb)*(M-2*b+1)*x**a*y**(c-2)
  assert sp.expand(got-expect)==0
receipt=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),arithmetic='fractions.Fraction physical-coordinate polynomial operations; independent SymPy operator differentiation',cases=records,generic_symbolic_degrees=[4,6,8,10,12],all_passed=True,scope='Finite coefficients only; no convergence, local exact solution or full-plane claim')
(out/'exact_checks.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(dict(utc=receipt['utc'],all_passed=True,output=str(out/'exact_checks.json'))),flush=True)
