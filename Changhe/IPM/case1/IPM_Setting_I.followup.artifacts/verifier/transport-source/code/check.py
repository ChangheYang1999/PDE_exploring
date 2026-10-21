import sympy as S
import json
from pathlib import Path
s,v,A,q,r=S.symbols('s v A q r', nonzero=True)
F=S.Function('F')(s,v)
J=1+S.diff(F,s,v)
a=(A*(s+S.diff(F,v))-v*S.diff(F,v,2))/J
b=J*v+S.diff(F,s,2)*a
Ds=lambda h:S.diff(h,s)-S.diff(F,s,2)/J*S.diff(h,v)
Dy=lambda h:S.diff(h,v)/J
out={'transport':str(S.simplify(-a*S.diff(F,s,2)/J+b/J-v)),
     'divergence':str(S.simplify(Ds(a)+Dy(b)-(A+1)))}
F0=r**(1-q)*v**5/(q-1)
fs=lambda h:-S.diff(h,r)
j0=1+fs(S.diff(F0,v))
a0=(A*(-r+S.diff(F0,v))-v*S.diff(F0,v,2))/j0
b0=j0*v+fs(fs(F0))*a0
y0=v+fs(F0)
out['inner_a']=str(S.simplify((a0+A*r).subs(A,4/q)))
out['inner_b']=str(S.simplify((b0-y0).subs(A,4/q)))
assert all(x=='0' for x in out.values()),out
path=Path(__file__).resolve().parents[1]/'verification'/'identities.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
