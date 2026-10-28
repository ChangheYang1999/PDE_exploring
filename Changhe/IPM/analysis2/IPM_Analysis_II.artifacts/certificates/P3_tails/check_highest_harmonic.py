from pathlib import Path
import sympy as s
from datetime import datetime,timezone
import json
q,n,r=s.symbols('q n r', positive=True)
w=s.Function('w')(q)
H=(n+2)*w+q*s.diff(w,q)
B=r**(n+2)*w.subs(q,r*r)
A=-4*r**(n+1)*H.subs(q,r*r)
coefficient=s.expand((-(n+2)*B*s.diff(A,r)+(n+1)*s.diff(B,r)*A)/(2*r))
Q=(n+2)*w*(q*s.diff(w,q,2)+2*s.diff(w,q))-(n+1)*q*s.diff(w,q)**2
identity=s.simplify(coefficient-4*r**(2*n+3)*Q.subs(q,r*r))
assert identity==0
u=s.Function('u')(q)
transformed=s.factor(Q.subs(w,u**(n+2)).doit())
expected=(n+2)**2*u**(2*n+3)*(q*s.diff(u,q,2)+2*s.diff(u,q))
assert s.simplify(transformed-expected)==0
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
'highest_harmonic_difference':str(identity),'positive_w_substitution_difference':'0',
'negative_w_case':'Q is quadratic in w,w derivatives, so unchanged by w -> -w',
'assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
