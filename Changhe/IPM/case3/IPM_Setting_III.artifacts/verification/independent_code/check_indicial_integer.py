"""Exact differentiation tests for nonpolynomial even-degree lattice modes."""
from fractions import Fraction as F
from datetime import datetime,timezone
from pathlib import Path
import json
from check_indicial_fourier import add,scale,deriv,mulcoord,iterate,lap,canonical
checks=[]
for A,m in [(F(2),0),(F(4,3),1),(F(6,5),2),(F(4),0),(F(2),1),(F(8,5),2)]:
 for n in range(3):
  d=(2*m+1)*A-2*m
  assert d.denominator==1 and d.numerator%2==0
  a0=(A-1)*((2*m+1)*A+2*n+3);s=d+2*m+2*n+1
  eta=iterate(iterate({(0,0,s/2):F(1)},0,2*m),1,2*n+1)
  chi=scale(iterate(iterate({(0,0,(s+2)/2):F(1)},0,2*m+1),1,2*n+1),-1/(s+2)**2)
  poisson=canonical(add(scale(lap(chi),-1),scale(deriv(eta,0),-1)))
  def defect(a):return canonical(add(scale(mulcoord(deriv(eta,0),0),A),mulcoord(deriv(eta,1),1),scale(eta,-1),scale(deriv(chi,0),a)))
  assert canonical(eta) and not poisson and not defect(a0) and defect(a0+1)
  assert all(k[2].denominator==2 for k in canonical(eta))
  checks.append({'A':str(A),'m':m,'n':n,'d':str(d),'a0':str(a0),'poisson_zero':True,'transport_zero':True,'negative_control_nonzero':True,'radial_powers_half_integral':True})
p=Path('research/indicial_integer/verification');p.mkdir(parents=True,exist_ok=True)
(p/'exact_examples.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'method':'Exact rational monomial differentiation and binomial reduction; no transform or shooting evaluator','checks':checks},indent=2)+'\n')
print(len(checks),'even-degree examples passed')
