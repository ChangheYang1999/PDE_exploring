from pathlib import Path
from datetime import datetime,timezone
from math import factorial,prod
import sympy as S
import time,json,itertools
start=time.monotonic();root=Path('research/195_interior_zero_arc_examples/verification');checks=[]
x,y=S.symbols('x y',real=True);h=S.Function('h')(x);t=S.Function('t')(y)
def ck(label,z):
 assert S.simplify(z)==0,(label,z);checks.append(label)
for tag,W,T,om in [('graph',S.Matrix([0,4*y-h]),h,S.diff(h,x)),('vertical',S.Matrix([4*x,0]),t,S.Integer(0))]:
 ck(tag+' div',S.diff(W[0],x)+S.diff(W[1],y)-4);ck(tag+' curl',S.diff(W[1],x)-S.diff(W[0],y)+om)
 ck(tag+' T',W.dot(S.Matrix([S.diff(T,x),S.diff(T,y)])));ck(tag+' V',W.dot(S.Matrix([S.diff(om,x),S.diff(om,y)]))+om-S.diff(T,x))
 U=W-2*S.Matrix([x,y]);ck(tag+' U first derivative',S.diff(U[0],x)-(-2 if tag=='graph' else 2))
a=S.symbols('a',nonzero=True);co=S.symbols('c0:6');F=sum(co[k]*x**(2*k)for k in range(6));hh=a*x*x+F-F.subs(x,0)-S.diff(F,x,2).subs(x,0)*x*x/2
HH=S.integrate(hh,x);psi=2*x*y-HH;UU=S.Matrix([-S.diff(psi,y),S.diff(psi,x)]);WW=2*S.Matrix([x,y])+UU;oo=S.diff(hh,x)
for label,z in [('h even',hh.subs(x,-x)-hh),('omega odd',oo.subs(x,-x)+oo),('psi odd',psi.subs(x,-x)+psi),('center h',hh.subs(x,0)),('center a',S.diff(hh,x,2).subs(x,0)-2*a),('center b',S.diff(oo,x).subs(x,0)-2*a),('strain',S.diff(psi,x,y)-2),('Poisson',-S.diff(psi,x,2)-S.diff(psi,y,2)-oo)]:ck(label,z)
for i in range(2):
 ck('center W'+str(i),WW[i].subs({x:0,y:0}))
 for j,z in enumerate([x,y]):ck('center DW'+str((i,j)),S.diff(WW[i],z).subs({x:0,y:0})-S.diag(0,4)[i,j])
for m in range(2,6):ck('high jet'+str(m),S.diff(hh,x,2*m).subs(x,0)-S.diff(F,x,2*m).subs(x,0))
# Exhaust all ordered positive compositions through n=12.
composition_checks=0;merge_checks=0
for n in range(1,13):
 for mask in range(1<<(n-1)):
  cuts=[0]+[j for j in range(1,n)if mask&(1<<(j-1))]+[n];parts=[cuts[j+1]-cuts[j]for j in range(len(cuts)-1)];k=len(parts)
  assert factorial(k)*prod(factorial(j)for j in parts)<=factorial(n);composition_checks+=1
  assert prod(factorial(j+1)for j in parts)<=factorial(n+1);merge_checks+=1
# Formal inverse coefficients computed recursively, compared with finite Lagrange identity.
z=S.symbols('z');lagrange=[]
for coeff in [(2,1,-1,2),(-3,2,1,-1),(S.Rational(1,2),-2,3,1)]:
 ff=sum(c*z**(i+1)for i,c in enumerate(coeff));gg=S.Integer(0)
 for n in range(1,9):
  bn=S.symbols('bn');trial=gg+bn*z**n;eq=S.expand(sum(c*trial**(i+1)for i,c in enumerate(coeff))).coeff(z,n)-(1 if n==1 else 0);value=S.solve(eq,bn)[0];gg+=value*z**n
  q=S.expand(ff/(coeff[0]*z)-1)
  rhs=S.Rational(1,n)*S.sympify(coeff[0])**(-n)*S.series((1+q)**(-n),z,0,n).removeO().coeff(z,n-1)
  ck('Lagrange'+str((coeff,n)),value-rhs);lagrange.append(str(value))
J,m,L=S.symbols('J m L');ck('complete square',-J*J+2*m*J*L-(m*m*L*L-(J-m*L)**2))
# Wrong movement direction is explicitly refuted with exact parts (2,3)->(1,4).
assert S.Rational(factorial(5),factorial(1)*factorial(4))/S.Rational(factorial(5),factorial(2)*factorial(3))==S.Rational(2,4)
out={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'symbolic_checks':len(checks),'composition_checks':composition_checks,'inverse_factorial_checks':merge_checks,'lagrange_checks_in_symbolic_total':len(lagrange),'algebraic_wrong_movement_counterexample':1,'elapsed_seconds':time.monotonic()-start,'scope':'Exact finite controls; infinite smoothness and non-Gevrey claims proved in PROOF.md, not inferred from controls.'};(root/'controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
