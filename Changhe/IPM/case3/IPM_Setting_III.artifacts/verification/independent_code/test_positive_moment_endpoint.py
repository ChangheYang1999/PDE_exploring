from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from math import factorial
import json
import sympy as s
x,y,m=s.symbols('x y m',real=True);z=x*x+y*y
fm=y*z**(1-m)/(4*(m-1)*(m-2))
assert s.simplify(s.diff(fm,x,2)+s.diff(fm,y,2)-y*z**(-m))==0
assert s.simplify(s.diff(fm,x,2)-y*z**(-m)*(2*m*x*x/z-1)/(2*(m-2)))==0
n,A,a,T=s.symbols('n A a T')
expr=a*((n+3)*T-1)-(n-1)*(n-A+(n+3)*(A-1)*T)
assert s.expand(expr-((a-(n-1)*(A-1))*((n+3)*T-1)-(n-1)**2))==0
def moment(j,k):
 # Integral cos^(2j)sin^(2k) divided by pi.
 return F(2*factorial(2*j)*factorial(2*k),4**(j+k)*factorial(j)*factorial(k)*factorial(j+k))
cases=[]
for K in range(1,17):
 n=2*K+1
 for A in [F(6,5),F(2),F(3),F(9),F(11),F(37)]:
  for a in [F(-76),F(2),F(13),(n-1)*A,(n-1)*A+1,(n-1)*A+9]:
   e=[n-1+2*j*(A-1)for j in range(K+1)]
   cc=[F(0)]*K+[F(1)]
   for j in range(K-1,-1,-1):cc[j]=-F((2*j+2)*(2*j+1))*(e[j+1]-a)*cc[j+1]/((n-2*j)*(n-2*j-1)*e[j])
   C=sum((c*moment(j,K-j+1)for j,c in enumerate(cc)),F(0))
   M=sum((c*moment(j+1,K-j+1)for j,c in enumerate(cc)),F(0))
   assert (a-(n-1)*(A-1))*((n+3)*M-C)==(n-1)**2*C
   if all(c>=0 for c in cc):
    assert C>0 and 0<M<C
    assert a<(n-1)*(A-n) or a>(n-1)*(A-1)+F((n-1)**2,n+2)
   cases.append(dict(n=n,A=str(A),a=str(a),C_over_pi=str(C),moment_over_pi=str(M)))
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',symbolic_checks=3,rational_leading_cases=len(cases),cases=cases,scope='Exact algebra supporting the standalone conditional first-moment proof. Boundary estimates are justified in PROOF.md, not by finite tests.')
Path('research/positive_moment_endpoint/verification/checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='cases'},indent=2))
