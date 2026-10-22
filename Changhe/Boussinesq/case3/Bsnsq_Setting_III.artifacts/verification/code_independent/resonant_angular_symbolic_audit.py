"""Exact independent checks for packet67; no production solver code."""
from pathlib import Path
from datetime import datetime,timezone
import json,time,hashlib
import sympy as s
start=time.monotonic()
r=s.symbols('r',positive=True);theta=s.symbols('theta',real=True)
k=s.symbols('k',integer=True,positive=True);alpha,beta,kappa=s.symbols('alpha beta kappa',nonzero=True)
q=s.Function('q')(theta);g=s.Function('g')(theta);gamma=k*alpha
H=s.Matrix([r**alpha*q,r**gamma*(g+kappa/beta*q**k*s.log(r))])
det=s.det(s.Matrix.hstack(H.diff(r),H.diff(theta)))
want=r**(alpha+gamma-1)*(alpha*q*s.diff(g,theta)-gamma*s.diff(q,theta)*g-kappa/beta*q**k*s.diff(q,theta))
checks={'polar_jacobian':s.simplify(det-want)}
qp=s.diff(q,theta);gp=(1+gamma*qp*g+kappa/beta*q**k*qp)/(alpha*q)
checks['quotient_equation']=s.simplify(s.diff(g/q**k,theta).subs(s.diff(g,theta),gp)-1/(alpha*q**(k+1))-kappa/(alpha*beta)*qp/q)
# On the right half-plane q>0; logarithmic derivatives are the same for log|q| elsewhere.
ghat=g-kappa/(alpha*beta)*q**k*s.log(q)
checks['corrected_quotient']=s.simplify(s.diff(ghat/q**k,theta).subs(s.diff(g,theta),gp)-1/(alpha*q**(k+1)))
t=s.symbols('t',real=True);x,y,lam=s.symbols('x y lam',nonzero=True)
xt=s.exp(lam*t)*x;yt=s.exp(k*lam*t)*(y+kappa*t*x**k)
checks['triangular_flow_y']=s.simplify(s.diff(yt,t)-k*lam*yt-kappa*xt**k)
bval=2*(k+1)/(k-3);lv=(bval-2)/2;mv=(3*bval+2)/2
checks['beta_resonance']=s.simplify(mv-k*lv)
checks['area_exponent']=s.simplify((lv+mv)/bval-2)
z,a,b,c=s.symbols('z a b c',nonzero=True)
Q=a*z+b*z**3+c*z**5
res=s.expand(s.series((z/Q)**5,z,0,5).removeO()).coeff(z,4)
checks['k4_residue']=s.simplify(res-(15*b*b/a**7-5*c/a**6))
q3,q5=s.symbols('q3 q5')
checks['k4_derivatives']=s.simplify(-beta*res.subs({b:q3/6,c:q5/120})-beta*(q5/(24*a**6)-5*q3*q3/(12*a**7)))
# A finite smooth Taylor jet, without analyticity, has no residue after differentiating.
for order in [4,6,8,10]:
 B=s.symbols('B0:'+str(order+2));poly=sum(B[j]*z**j for j in range(order+2))
 checks['derivative_residue_k'+str(order)]=s.expand(s.diff(poly/z**order,z)).coeff(z,-1)
assert all(v==0 for v in checks.values()),checks
root=Path('research/67_resonant_angular_tail/verification')
out={'written_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'sympy_version':s.__version__,'checks':{n:str(v) for n,v in checks.items()},'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact algebra only; complete smooth proof and global endpoint arguments are in PROOF.md. No PDE candidate or existence assertion.'}
(root/'symbolic.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
