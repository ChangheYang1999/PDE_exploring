from pathlib import Path
from datetime import datetime,timezone
import sympy as z,json
s,y=z.symbols('s y',positive=True);A=z.symbols('A',positive=True);C=z.symbols('C');R=s*s+y*y
u1v=s*R**((A-1)/2)/(A+1);u1q=(2*A*s*s+y*y)*R**((2*A-3)/2)/((2*A-1)*(2*A+1))
checks={
 'V_velocity':z.simplify(z.diff(R**((A+1)/2)/(A+1)**2,s)-u1v),
 'Q_velocity':z.simplify(z.diff(s*R**((2*A-1)/2)/((2*A-1)*(2*A+1)),s)-u1q),
 'V_U2_singular_multiplier':z.simplify((1-A*A)/(A*A-1)+1),
 'Q_U2_singular_multiplier':z.simplify((1-A*(2*A-1))/((A-1)*(2*A+1))+1),
 'V_h_singular':z.simplify(u1v*C*A*s**(A-1)-C*s**A*R**((A-1)/2)+C*s**A*R**((A-1)/2)/(A+1)),
 'Q_h_singular':z.simplify(u1q*C*(2*A-1)*s**(2*A-2)-C*s**(2*A-1)*s*R**((2*A-3)/2)-C*s**(2*A-2)*(y*y-s*s)*R**((2*A-3)/2)/(2*A+1)),
 'Q2_log_h':z.simplify(-z.Rational(3,2)*s*s*u1q.subs(A,2)+z.Rational(1,2)*s**3*s*z.sqrt(R)+s*s*(y*y-s*s)*z.sqrt(R)/10)}
sigma=y**(2*A-1)/((A-1)*(2*A-1)*(2*A+1));checks['curve_equation']=z.simplify(y*z.diff(sigma,y)-A*sigma-u1q.subs(s,0))
assert all(v==0 for v in checks.values()),checks
out={'date':datetime.now(timezone.utc).isoformat(),'all_pass':True,'identities':{k:str(v) for k,v in checks.items()},'scope':'local algebra; C3 correction obstruction proved separately in PROOF.md','particular_curve_coefficients':{'A7/4':str(z.simplify(sigma/y**(2*A-1)).subs(A,z.Rational(7,4))),'A2':str(z.simplify(sigma/y**(2*A-1)).subs(A,2))}}
root=Path(__file__).resolve().parents[1];(root/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
