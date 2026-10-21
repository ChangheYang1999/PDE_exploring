from pathlib import Path
from datetime import datetime,timezone
import sympy as s,json,time
start=time.time();u,A,L=s.symbols('u A L',positive=True)
D=lambda f:s.diff(f,u)/L
w=-A*L*u*(1-u*u)/(1+u*u);g=L*L*u*u/(1+u*u);h=A+1-D(w)
a2=(D(g)-D(D(w)))/2;b3=-D(a2)/3;F3=s.factor(-a2*D(g)-b3*g)
expected=-u*u*((6*A+3*L*L)*u*u+5*L*L-30*A)/(3*(1+u*u)**4)
S=6*A*(4*A-3)/(8*A-1)
checks={'forcing':str(s.factor(F3-expected)), 'beta_recurrence_ratio':str(s.factor((-2-1/A)/(-2+1/A)-(2*A+1)/(2*A-1))), 'bracket':str(s.factor(5*L*L-30*A+(6*A+3*L*L)*(2*A+1)/(2*A-1)-2*(8*A-1)*(L*L-S)/(2*A-1))), 'source_w_prime':str(s.factor(D(w).subs(u,1)-A)), 'source_h':str(s.factor(h.subs(u,1)-1))}
assert all(t=='0' for t in checks.values())
out={'date':datetime.now(timezone.utc).isoformat(),'checks':checks,'seconds':time.time()-start}
(Path(__file__).resolve().parents[1]/'verification'/'general_b3.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
