from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
x,A,b=s.symbols('x A b',positive=True)
w=s.Function('w')(x);g=s.Function('g')(x);G=s.Function('G')(x)
r1=w*s.diff(g,x)-(s.diff(w,x)-A)*g
Q=(s.diff(g,x)-s.diff(w,x,2))/(2*g**3);F=g**4*s.diff(Q,x)/3
m=-w/g
logH=(3+b)*s.diff(g,x)/g-b*s.diff(w,x)/w
r3=w*s.diff(G,x)-(3*s.diff(w,x)-3*A-A*b)*G-F
checks={}
def zero(name,expr):
 v=s.factor(expr);assert v==0,(name,v);checks[name]='0'
zero('m_prime',s.diff(m,x)+A/g-r1/g**2)
zero('log_H_prime',logH-(3*s.diff(w,x)-3*A-A*b)/w-(3+b)*r1/(w*g))
zero('quotient_residual',s.diff(G,x)-G*logH-(F+r3-(3+b)*r1*G/g)/w)
zero('forcing',F-(-((s.diff(g,x)-s.diff(w,x,2))/2)*s.diff(g,x)+s.diff((s.diff(g,x)-s.diff(w,x,2))/2,x)*g/3))
# Divide the integration-by-parts identity by m^(b-2)/(3A^b), leaving a rational expression.
ql=s.symbols('Q_L')
zero('ibp_sign',-s.diff(Q,x)*m+(b-1)*A*(Q-ql)/g-(b-1)*(Q-ql)*r1/g**2-(-s.diff(Q,x)*m-(b-1)*(Q-ql)*s.diff(m,x)))
ww=-4*x*(1-x*x)/(1+x*x);gg=x*x*(1+x*x/s.Integer(10))/(1+x*x);GG=x*x/(1+x*x)**2
rr=s.factor(ww*s.diff(gg,x)-(s.diff(ww,x)-4)*gg)
assert rr!=0 and s.limit(rr/x**4,x,0)!=0 and rr.subs(x,1)==0
zero('manufactured_first_residual',rr+s.Rational(4,5)*x**4*(1-x*x)/(1+x*x)**2)
obj={'date':datetime.now(timezone.utc).isoformat(),'checks':checks,'manufactured_r1':str(rr),'center_r1_x4':str(s.limit(rr/x**4,x,0)),'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),'verdict':'CONFIRMED_EXACT_ALGEBRA'}
(ROOT/'verification/check.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
