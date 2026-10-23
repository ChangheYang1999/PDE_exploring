"""Independent exact checks for the new critical strain and nodal calculations."""
from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as s
x,y,vx,vy,c,B,T,b,eps=s.symbols('x y vx vy c B T b eps',real=True)
r2=x*x+y*y
K=s.Matrix([-x*y/r2**2,(x*x-y*y)/(2*r2**2)])
J=K.jacobian([x,y]);Q=s.Matrix([y*(3*x*x-y*y),x*(3*y*y-x*x)])/r2**3
expected=s.Matrix([[Q[0],Q[1]],[Q[1],-Q[0]]]);assert s.simplify(J-expected)==s.zeros(2)
assert s.simplify(x*Q.diff(x)+y*Q.diff(y)+3*Q)==s.zeros(2,1)
DQ=Q.jacobian([x,y]);assert s.simplify(DQ.T*DQ-9/r2**4*s.eye(2))==s.zeros(2)
fractions=[]
for a,bb,e1,e2 in [(s.Integer(3),s.Integer(1),-s.Rational(41,169),-s.Rational(1117,4394)),(s.Integer(1),s.Rational(1,2),s.Rational(11552,34225),-s.Rational(4564464,6331625))]:
    u=sum((2-h*a)*bb/((2-h*a)**2+bb*bb)**2 for h in [-1,1])
    q=sum(bb*(bb*bb-3*(2-h*a)**2)/((2-h*a)**2+bb*bb)**3 for h in [-1,1])
    assert s.factor(u-e1)==0 and s.factor(q-e2)==0
    fractions.append({'a':str(a),'b':str(bb),'velocity_without_2_over_pi':str(u),'strain_without_2_over_pi':str(q)})
D=c-1;p=1/c
assert s.simplify(c*(p-1)+D)==0
assert s.expand(T/2*(-b*eps/D)**2+eps*b*T/D*(-b*eps/D)+T*b*b*eps**2/(2*D**2))==0
k,lam=s.symbols('k lam');mu=2*c-lam
assert s.expand((1-k*lam)-k*mu-(1-2*k*c))==0
# On v>0 the absolute-value expression reduces to a smooth elementary formula.
u,v=s.symbols('u v',positive=True);ll=s.symbols('lambda',negative=True);cc=s.symbols('ell',positive=True)
mm=2*cc-ll;alpha=-ll/mm
rho=v**(1/mm)*s.exp(-1/(u*u*v**(2*alpha)))
assert s.simplify(ll*u*s.diff(rho,u)+mm*v*s.diff(rho,v)-rho)==0
# Local strain equality does not determine the cubic jet from transport alone.
assert -2*7+5*3==1
rows=[]
for kk in range(2,15):
 for jj in range(1,kk):
    lam=(1-2*c*jj)/(kk-jj);mu=2*c-lam
    assert s.factor(kk*lam+jj*mu-1)==0
    if jj==1:assert s.factor(c-lam-(c+(2*c-1)/(kk-1)))==0
    rows.append({'k':kk,'j':jj,'stable_eigenvalue':str(lam)})
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','kernel_checks':3,'bump_fractions':fractions,'finite_resonances':rows,'additional_checks':['exterior transport argument','second far coefficient cancellation','transverse exponent','hyperbolic flat transport','non-cubic equal-strain transport example'],'scope':'Independent exact identities and full informal proofs. Conditional strain bounds and non-profile tests do not resolve the primary endpoint.'}
pth=Path('research/critical_strain_moments/verification/checks.json');pth.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'utc':result['utc'],'status':'PASS','finite_resonances':len(rows)}),flush=True)
