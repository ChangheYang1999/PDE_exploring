from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
from exact_degree21 import *
from modular_gcd_certificate_285 import certify,add,mul
R=Path('research/degree21_grouped_moment_obstruction');checks=[];sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,b):checks.append(dict(name=n,passed=bool(b)))
for k,(D,A,B)in enumerate([(1,h+1,h*h+1),(h-21,(2*h+3)**2,3*h-4),((h-21)**12,h*h+2,5*h**3+7),(h**182*(h-21)**120,101*h+1,101*h*h+2)]):
 D=poly(D);A=poly(A);B=poly(B);c=certify(14*D*A,21*D*B,D);ck(str(k)+' exact division',c['exact_divisions_verified']);ck(str(k)+' degree preservation',c['leading_degrees_preserved']);p=c['prime'];a=[v%p for v in univ(prim(A))];b=[v%p for v in univ(prim(B))];ck(str(k)+' independent displayed Bezout',add(mul(c['s'],a,p),mul(c['t'],b,p),p)==[1])
 if k==3:ck('first prime degree drop skipped',p!=101)
for k,(F,G,D)in enumerate([((h+1)*(h+2),(h+1)*(h+3),1),(h+1,h+2,h+3)]):
 rejected=False
 try:certify(poly(F),poly(G),poly(D))
 except ArithmeticError:rejected=True
 ck('false target rejected'+str(k),rejected)
out=dict(status='PASS'if all(c['passed']for c in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,proof_sha256=sha(R/'GCD_MANUFACTURED_PROOF.md'),gcd_proof_sha256=sha(R/'GCD_CERTIFICATE_PROOF.md'),driver_sha256=sha(__file__),gcd_driver_sha256=sha('independent_code/modular_gcd_certificate_285.py'));(R/'verification/GCD_MANUFACTURED.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(checks));raise SystemExit(out['status']!='PASS')
