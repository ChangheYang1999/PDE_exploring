"""Independent Newton auditor: exact known polynomials at new nodes."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
from pathlib import Path
from fractions import Fraction as Q
import json,math,sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
import audit_coefficients as a
cases=0
for degree in range(8):
 for scale in (Q(1),Q(-7,3),Q(3,2**17)):
  coefficients=[scale*(i+1)*(-1)**i for i in range(degree+1)]+[Q(0)]*(7-degree)
  values=[sum((v*Q(j+1,9)**i for i,v in enumerate(coefficients)),Q(0)) for j in range(8)]
  for off,h in ((Q(0),Q(1)),(Q(1,2),Q(7,19)),(Q(3,11),Q(1,1000)),(Q(1),Q(59,8))):
   got=a.newton_coefficients(values,9*off-1,9/h)
   expected=[sum((coefficients[j]*math.comb(j,k)*off**(j-k)/h**k for j in range(k,8)),Q(0)) for k in range(8)]
   assert got==expected;cases+=8
knots=[Q(0)]*8+[Q(1)]*8;basis_checks=0
for j in range(1,9):
 z=Q(j,9);got=a.recursive_basis(knots,7,z);expected=[math.comb(7,i)*z**i*(1-z)**(7-i) for i in range(8)];assert got==expected;basis_checks+=8
faults=0
for bad in ('0x1.00000000000001p+0','nan','inf','-inf'):
 try:a.exact_hex(bad)
 except (AssertionError,ValueError,OverflowError):faults+=1
 else:raise AssertionError(bad)
result={'utc':a.utc(),'status':'PASS_DIAGNOSTIC_ONLY','exact_polynomial_coefficients':cases,'Bernstein_basis_values':basis_checks,'malformed_hex_rejected':faults,'source_sha256':a.sha(Path(__file__)),'auditor_sha256':a.sha(a.D/'code/audit_coefficients.py')};(a.E/'newton_manufactured.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
