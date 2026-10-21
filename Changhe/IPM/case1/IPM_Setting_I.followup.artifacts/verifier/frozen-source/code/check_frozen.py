"""Fresh pointwise/distributional frozen potential check from y derivatives."""
import json
from pathlib import Path
import sympy as S
s,y,A=S.symbols('s y A',real=True)
R2=s*s+y*y
t=S.symbols("t",positive=True)
def reduce(expr):
    return S.factor(S.simplify(S.powsimp(expr.subs(R2,t),force=True)).subs(t,R2))
rows=[]
for label,f,phi,g in [
 ('V',R2**((A-1)/2),R2**((A+1)/2)/(A+1)**2,A*A-1),
 ('Q',s*R2**((2*A-3)/2),s*R2**((2*A-1)/2)/((2*A-1)*(2*A+1)),(A-1)*(2*A+1))]:
 lap=reduce(S.diff(phi,s,2)+S.diff(phi,y,2)-f)
 ode=reduce(A*s*S.diff(f,s)+y*S.diff(f,y)-g*S.diff(phi,s,2))
 assert lap==0 and ode==0
 # v_y=f, so coefficient v_y^(j-1)/j! is G_j.
 coefficients={str(j):str(S.simplify(S.diff(f,y,j-1).subs(y,0)/S.factorial(j))) for j in (3,5)}
 rows.append({'family':label,'potential_laplacian_y_residual':str(lap),'frozen_equation_y_residual':str(ode),'G':coefficients})
r=S.symbols('r',positive=True)
f=s*S.sqrt(R2)
cone=S.simplify(S.diff(f,y,3).subs(s,-r))
assert S.simplify(cone-3*r**3*y/(r*r+y*y)**S.Rational(5,2))==0
out={'checks':rows,'Q2_fourth_derivative_at_minus_r':str(cone),'samples':[]}
for label,av in [('V',S.Rational(5,2)),('Q',S.Rational(7,4)),('Q',S.Integer(2))]:
 f=R2**((av-1)/2) if label=='V' else s*R2**((2*av-3)/2)
 zs={str(j):str(S.simplify(r**((j-1)/av)*S.diff(f,y,j-1).subs({s:-r,y:0})/S.factorial(j))) for j in (3,5)}
 out['samples'].append({'family':label,'A':str(av),'Z':zs})
print(json.dumps(out,indent=2))
Path('verifier/frozen-source/verification/symbolic.json').write_text(json.dumps(out,indent=2)+'\n')
