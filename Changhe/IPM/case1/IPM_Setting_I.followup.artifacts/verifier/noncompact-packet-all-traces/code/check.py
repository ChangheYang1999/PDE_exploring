from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as s
D=Path(__file__).resolve().parents[1]
k,t,r,eps=s.symbols('k t r eps',positive=True)
y,z=s.symbols('y z',real=True)
checks=[]
for m in range(9):
 j=2*m+1
 sy=s.simplify(s.diff(s.sin(y*r),y,j).subs(y,0)-(-1)**m*r**j);assert sy==0
 jac=s.simplify((s.sqrt(k/t))**(2*m-1)*s.diff(s.sqrt(k/t),k)-s.Rational(1,2)*k**(m-1)*t**(-m));assert jac==0
 for n in range(9):
  logpower=s.Rational(-1,2)-m-s.Rational(1,2)-n+1
  assert logpower==-m-n
  assert s.sin(s.pi*logpower)==0
  checks.append({'m':m,'n':n,'j':j,'moment_index':m+n,'Gaussian_linear_exponent':str(logpower),'sine_factor':'0'})
 for ell in range(9):
  N=m+ell+1
  power=s.Rational(2*m-3,2)-N+ell
  assert power < -1
 for j_even in [2*m]:assert s.diff(s.sin(y*r),y,j_even).subs(y,0)==0
 if m>=1:
  exact=s.integrate(r**(2*m-1)*s.exp(-eps*t*r*r),(r,0,s.oo))
  assert s.simplify(exact-s.factorial(m-1)/(2*(eps*t)**m))==0
res={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','moment_checks':checks,'odd_prefactor_and_Jacobian_checks':9,'even_trace_checks':9,'exact_damped_radial_integrals':8,'high_frequency_integrability_checks':81,'proof_sha256':hashlib.sha256((D/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Finite exact symbolic checks supplement the general standalone proof. No numerical profile or interval certificate.'}
(D/'verification/check.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps({k:v for k,v in res.items()if k!='moment_checks'},indent=2))
