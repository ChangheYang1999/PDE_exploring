from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
x=s.symbols('x',positive=True); A=s.symbols('A',positive=True); beta=s.symbols('beta',positive=True);w=s.Function('w')(x);v=s.Function('v')(x)
checks=[]
def add(name,z):
 z=s.simplify(z);assert z==0,(name,z);checks.append({'name':name,'residual':str(z)})
eta_prime=s.diff(s.log(1+v/w),x)-A*(1/(w+v)-1/w)
add('normalized logarithmic derivative',eta_prime-((s.diff(w+v,x)-A)/(w+v)-(s.diff(w,x)-A)/w))
add('finite-part leading prefactor',(beta-1)*A**(1-beta)/3*(-A**(beta-2)/2)-(1-beta)/(6*A))
add('twice integrated weight',s.diff(x**(-6-beta),x,2)-(6+beta)*(7+beta)*x**(-8-beta))
l=s.symbols('lambda',positive=True);g=s.Function('g')(x)
add('exact tail Q scaling',(s.diff(l*g,x)-s.diff(w,x,2))/(2*(l*g)**3)-(l**(-2)*s.diff(g,x)/(2*g**3)-l**(-3)*s.diff(w,x,2)/(2*g**3)))
# Real positive m and g avoid unrequested complex-power transformations.
m=s.symbols('m',positive=True);G=s.symbols('G',positive=True)
add('exact positive tail W scaling',(m/l)**(beta-2)/(l*G)-l**(1-beta)*m**(beta-2)/G)
for b in (s.Rational(1,5),s.Rational(1,2),s.Rational(3,4)):
 for i in range(3):
  n=6-i
  c=sum((-1)**k*s.binomial(n,k)/(b+k+1) for k in range(n+1))/s.factorial(n)
  add(f'Taylor integral constant beta={b} i={i}',c-1/s.prod(b+k for k in range(1,8-i)))
  assert c>0
out={'utc':datetime.now(timezone.utc).isoformat(),'checks':checks,'verdict':'PASS','scope':'Exact algebraic identities only. The uniform estimates and limiting arguments require the complete informal proof and independent review; these computations do not certify a PDE profile.','pins':{'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
(ROOT/'verification/symbolic_checks.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS',len(checks),out['utc'])
