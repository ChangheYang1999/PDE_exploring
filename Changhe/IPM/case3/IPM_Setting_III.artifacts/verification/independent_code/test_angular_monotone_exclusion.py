"""Exact supporting identities and transport countertests for result77."""
from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as s
x,y,theta,D,beta=s.symbols('x y theta D beta',real=True)
A=2*D+1
assert s.trigsimp(s.diff(s.cos(theta)*s.sin(theta)**3,theta)-s.sin(theta)*s.sin(3*theta))==0
assert s.integrate(s.cos(theta)**2*s.sin(theta)**4,(theta,0,s.pi/2))==s.pi/32
count=0;rows=[]
for k in range(1,21):
 t=s.symbols('t:'+str(k+1));aa=s.symbols('a')
 Q=sum(t[j]*x**(2*j)*y**(2*k-2*j)for j in range(k+1));H=-y*Q
 V=A*x*s.diff(H,x)+y*s.diff(H,y)-H
 residual=s.Poly(s.expand(s.diff(V,x,2)+s.diff(V,y,2)-aa*s.diff(H,x,2)),x,y)
 angular=s.Poly(s.expand(x*s.diff(Q,y)-y*s.diff(Q,x)),x,y)
 assert angular.coeff_monomial(x*y**(2*k-1))==2*(k*t[0]-t[1])
 for j in range(1,k+1):
  dj=2*j*A+2*(k-j);dp=2*(j-1)*A+2*(k-j+1)
  target=(2*j)*(2*j-1)*(aa-dj)*t[j]-(2*k-2*j+3)*(2*k-2*j+2)*dp*t[j-1]
  actual=residual.coeff_monomial(x**(2*j-2)*y**(2*k+1-2*j))
  assert s.expand(actual-target)==0,(k,j);count+=1
 for dd in [s.Rational(1,100),s.Rational(1,4),1,5,100]:
  for aval in [dd,2*dd,4*dd]:
   d1=(2*A+2*k-2).subs(D,dd)
   # If t0=-1, the j=1 compatibility would force t1>0, contradicting
   # the angular-sign requirement t1<=k*t0<0. All chosen a lie below d1.
   t1=-s.Rational((2*k+1)*(2*k)*(2*k),2)/(aval-d1)
   assert d1>aval and t1>0
   rows.append(dict(k=k,D=str(dd),a=str(aval),forced_t1=str(t1)))
a=8*D/(2+beta);b=-a;e=a*(beta-1)
defect=s.factor((a-2*A)*b-6*e)
assert s.factor(defect-a*(4*D+8-6*beta-a))==0
result=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',canonical_angular_identities=2,exact_recurrence_count=count,sign_counterchecks=len(rows),gaussian_transport_defect=str(defect),sign_samples=rows,
 scope='Exact angular strain weight, first angular coefficient, full leading PDE recurrences through degree41, and admissible canonical Gaussian nonprofile countertest. The all-degree and flat-germ arguments are proved in PROOF.md; finite checks do not prove a uniform theorem.')
p=Path('research/angular_monotone_exclusion/verification/checks.json');p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k!='sign_samples'},indent=2))
