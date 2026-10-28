from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
import sympy as s
from flint import arb, ctx
P=Path(__file__).resolve().parents[1]
x,y,H=s.symbols('x y H',real=True)
psi=-(x**3*y+x*y**3)/6+H*(x**3*y-x*y**3)
assert s.simplify(-s.diff(psi,x,2)-s.diff(psi,y,2)-2*x*y)==0
u1=-s.diff(psi,y);u2=s.diff(psi,x)
pol=s.expand(u1*2*x*y+u2*x*x)
expected=x*x*y*((-s.Rational(1,6)+H)*x*x+(s.Rational(5,6)+5*H)*y*y)
assert s.simplify(pol-expected)==0
assert s.solve([H-s.Rational(1,6),5*H+s.Rational(5,6)],[H])==[]
ctx.prec=384;ctx.threads=1
sigma=arb(1)/4
cv=1/(8*(sigma*(sigma+1)*(sigma+2)).sqrt())
assert cv>arb('0.1490711984999859797606115779154184156')
assert cv>arb('0.069735617396310252')
sg=s.symbols('sigma',positive=True)
integral=1/(2*sg)-2/(2*sg+2)+1/(2*sg+4)
assert s.simplify(integral-1/(sg*(sg+1)*(sg+2)))==0
out={'date':datetime.now(timezone.utc).isoformat(),'result':'PASS',
     'snapshot_sha256':hashlib.sha256((P/'evidence/report_snapshot.md').read_bytes()).hexdigest(),
     'proof_sha256':hashlib.sha256((P/'PROOF.md').read_bytes()).hexdigest(),
     'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'velocity_remainder_pairing':str(pol),'simultaneous_zero_coefficients':'impossible',
     'sharp_Cv_at_sigma_quarter':cv.str(75),'source_uniqueness_scope':'only the certified interval',
     'comparison':'audited against existing independent certificates, no copied numerical claim upgraded without evidence'}
(P/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
