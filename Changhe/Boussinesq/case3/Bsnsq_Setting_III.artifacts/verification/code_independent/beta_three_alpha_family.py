"""Exploratory exact third-source alpha on sign-compatible angular families.
This is a calculation, not yet a theorem about exact profiles.
"""
from pathlib import Path
from datetime import datetime,timezone
import sympy as S,json,time
start=time.monotonic();z=S.symbols('z',nonzero=True);a,b,h,d=S.symbols('a b h d',real=True)
c=(z+1/z)/2;t=(z-1/z)/(2*S.I)
def deriv(f):return S.expand(S.I*z*S.diff(f,z))
def inv(f,k):
 ans=0
 for term in S.Add.make_args(S.expand(f)):
  n=int(term.as_powers_dict().get(z,0));ans+=term/(n*n-k*k)
 return S.expand(ans)
s=S.Rational(1,3);m=s;k0=2-s;k1=2-2*s
A0=S.expand(c*(a+b*t));H0=S.expand(c*c*(h+d*t));F0=inv(A0,k0)
A1=S.expand(k0*F0*deriv(A0)+s*deriv(F0)*A0-m*c*H0+t*deriv(H0))
H1=S.expand(k0*F0*deriv(H0)-m*deriv(F0)*H0);F1=inv(A1,k1)
A2=S.expand((k0*F0*deriv(A1)+2*s*deriv(F0)*A1+k1*F1*deriv(A0)+s*deriv(F1)*A0-(m-s)*c*H1+t*deriv(H1))/2)
alpha=S.factor(A2.coeff(z,1)+A2.coeff(z,-1))
out={'created_utc':datetime.now(timezone.utc).isoformat(),'alpha':str(alpha),'A0':'cos(theta)*(a+b*sin(theta))','H0':'cos(theta)^2*(h+d*sin(theta))','alpha_b_zero':str(S.factor(alpha.subs(b,0))),'alpha_d_zero':str(S.factor(alpha.subs(d,0))),'zero_d_bzero':str(S.solve(alpha.subs(b,0),d)),'elapsed_seconds':time.monotonic()-start,'scope':'Exploratory exact angular identities, not global profiles.'}
Path('research/91_beta_three_logarithmic_tail/verification/exploratory_alpha_family.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
