"""Exact all-k response bounds and constructive majorant disk for Theorem T."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time,sys
sys.dont_write_bytecode=True
import sympy as sp
R=sp.Rational
b,k,t,z,W,U,V,E=sp.symbols('b k t z W U V E')
root=Path('research/120_tuned_explicit_radius')
start=time.monotonic()

def bounds(expr,lo,hi):
 p=sp.Poly(expr,b,domain=sp.QQ);lower=upper=R(0)
 for (j,),a in p.terms():
  lower+=a*(lo**j if a>=0 else hi**j)
  upper+=a*(hi**j if a>=0 else lo**j)
 return lower,upper

def qs(x):return str(x)

def main():
 source=Path('research/119_tuned_rational_series/verification')
 assert json.loads((source/'checks.json').read_text())['all_checks_passed']
 sig=json.loads((source/'sigma_symbolic_exact.json').read_text())
 num,den=map(sp.expand,sp.fraction(sp.sympify(sig['sigma'])))
 small=json.loads((source/'sigma_integer_exact.json').read_text())['rows']
 polynomial=176703765525000*b**6-222533688701250*b**5+96180432855375*b**4-20675598499400*b**3+2783057141280*b**2-243275209320*b+10532171936
 sturm=sp.sturm(polynomial,b)
 def variations(x):
  signs=[sp.sign(p.subs(b,x)) for p in sturm];signs=[s for s in signs if s]
  return sum(a!=c for a,c in zip(signs,signs[1:]))
 intervals=[(R(28066166273196640399,10**20),R(28066166273196640401,10**20)),(R(64635228988093464430,10**20),R(64635228988093464432,10**20))]
 # Since sigma=num/den<0 on the tail, -num-den/100000 must be positive.
 target=sp.Poly(sp.expand((-num-den/R(100000)).subs(k,t+7)),t)
 rows=[]
 for index,(lo,hi) in enumerate(intervals):
  assert variations(lo)-variations(hi)==1
  coefficients=[]
  for (power,),poly in target.terms():
   lower,upper=bounds(poly,lo,hi)
   assert lower>0,(index,power,str(lower))
   coefficients.append({'t_degree':power,'coefficient_polynomial':str(poly),'exact_lower_bound':qs(lower),'exact_upper_bound':qs(upper)})
  sr=[]
  for ref in small:
   n=ref['k']
   if n>6:continue
   s=sp.sympify(ref['sigma']);lower,upper=bounds(s,lo,hi)
   bound=lower if lower>0 else -upper
   assert bound>R(1,100000)
   sr.append({'k':n,'exact_lower':qs(lower),'exact_upper':qs(upper),'modulus_lower_bound':qs(bound)})
  rows.append({'root_index':index+1,'interval':[qs(lo),qs(hi)],'sturm_variations':[variations(lo),variations(hi)],'generic_positive_coefficients':coefficients,'small_responses':sr})
 # Both denominator factorizations have positive factors for k>=7.
 assert all(c>0 for c in sp.Poly(den.subs(k,t+7),t).all_coeffs())
 response={'checked_at_utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'uniform_modulus_bound':'1/100000','denominator_shifted_positive_coefficients':[str(v) for v in sp.Poly(den.subs(k,t+7),t).all_coeffs()],'rows':rows}
 (root/'verification/response_bound.json').write_text(json.dumps(response,indent=2)+'\n')
 a=2;kap=10;s=R(1,100000);d=60;e=3600;P=a*z+d*z*z+e*z**3
 phi=sp.Matrix([
 R(3,2)*kap*(d*d+2*a*e+2*d*e*z+e*e*z*z)+3*kap*P*W+R(3,2)*kap*z**4*W*W+kap*E*(P+z**4*W),
 R(3,2)*kap*(2*d*e+e*e*z)+3*kap*(a+d*z+e*z*z)*W+R(3,2)*kap*z**3*W*W+kap*z**3*E*W,
 R(3,2)*kap*(e*e+2*(d+e*z)*W+z*z*W*W)+kap*z*z*E*W+3*kap*a*U,
 kap/s*(3*e*W+R(3,2)*z*W*W+z*E*W+3*a*V+3*d*U)])
 Y=sp.Matrix([W,U,V,E]);J=phi.jacobian(Y).subs(z,0);c=phi.subs({z:0,W:0,U:0,V:0,E:0})
 assert J**4==sp.zeros(4)
 Q=sp.eye(4)+J+J**2+J**3;assert (sp.eye(4)-J)*Q==sp.eye(4)
 Y0=Q*c;psi=(phi-c-J*Y).applyfunc(lambda x:sp.cancel(x/z))
 for x in psi:
  assert all(v>=0 for v in sp.Poly(x,z,W,U,V,E).coeffs())
 M=2**55;z0=R(1,2**120)
 bound=Q*psi.subs({z:1,W:2*M,U:2*M,V:2*M,E:2*M})
 assert max(Y0)<=M and max(bound)*z0<=M
 assert list(Y0)==[270000,22680000,2041200000,19245600000000000]
 data={'checked_at_utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'a':a,'kappa':kap,'sigma_lower':str(s),'d':d,'e':e,'J':[[str(v) for v in J.row(i)] for i in range(4)],'Q':[[str(v) for v in Q.row(i)] for i in range(4)],'constant_solution':[str(v) for v in Y0],'M':str(M),'z0':str(z0),'Q_Psi_box_bound':[str(v) for v in bound],'maximum_bound_times_z0':str(max(bound)*z0),'supersolution_verified':True,'exterior_radius':'2^180 * abs(epsilon)^(3/2)','actual_elapsed_s':time.monotonic()-start}
 (root/'verification/majorant_disk.json').write_text(json.dumps(data,indent=2)+'\n')
 for p in [Path(__file__),source/'sigma_symbolic_exact.json',source/'sigma_integer_exact.json',source/'algebraic_roots.json',Path('research/119_tuned_rational_series/PROOF.md')]:
  (root/'sources'/(p.name if p.name!='PROOF.md' else 'abstract_theorem_PROOF.md')).write_bytes(p.read_bytes())
 files={str(p.relative_to(root)):{'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()} for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
 (root/'verification/MANIFEST.json').write_text(json.dumps({'all_checks_passed':True,'files':files},indent=2)+'\n')
 print(json.dumps({'all_checks_passed':True,'actual_elapsed_s':time.monotonic()-start,'root':str(root)}),flush=True)

if __name__=='__main__':
 try:main()
 except Exception as exc:
  print(json.dumps({'error_type':type(exc).__name__,'error':str(exc)}),flush=True)
  raise SystemExit(1)
