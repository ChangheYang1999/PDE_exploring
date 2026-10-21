"""Independent exact sixth-order source cancellation with arbitrary residuals."""
import sympy as S
from pathlib import Path
from datetime import datetime,timezone
import json,time
root=Path(__file__).resolve().parents[1]
t0=time.monotonic();x,y=S.symbols('x y');a=S.Function('a')(x,y);b=S.Function('b')(x,y);f=S.Function('f')(x,y)
n=6;dy=lambda u,k=1:S.diff(u,y,k);dx=lambda u:S.diff(u,x);D=lambda u:a*dx(u)+b*dy(u)
h=dy(f)/a;an=dy(a,n-1);K=dy(f,n)-h*an
F=(dy(a)*an/a-dy(a,n))*(dx(f)+b*h)-sum(S.binomial(n,k)*dy(a,k)*dx(dy(f,n-k)) for k in range(1,n))-sum(S.binomial(n,k)*dy(b,k)*dy(f,n+1-k) for k in range(2,n))+(dx(a)-(n-1)*dy(b))*h*an
E=D(f)-f;nu=dx(a)+dy(b)
check=S.cancel(S.expand(D(K)+(n*dy(b)-1)*K-F-dy(E,n)+(an/a)*dy(E)+dy(f)*dy(nu,n-1)))
assert check==0
out={'date':datetime.now(timezone.utc).isoformat(),'n':n,'identity_residual':str(check),'A_at_exception':2,'source_exponent':3,'required_alpha_threshold':-2,'ratio_bound_exponent':'alpha+2','seconds':time.monotonic()-t0,'scope':'General formal identity with arbitrary transport and divergence residuals; estimates remain the complete source-estimates/cone-endpoints argument'}
(root/'verification/source6.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
