"""Exact independent radial angular and Cartesian jet checks."""
import sympy as S
import json
from pathlib import Path
r,theta,x,y,c,cl,A,b1,b2=S.symbols('r theta x y c cl A b1 b2',real=True)
h=r**3*(1+b1*r**2+b2*r**4)/4
T=-r**4/S.Integer(64)-b1*r**6/80-b2*r**8/96
harm7=S.expand((3*h*S.diff(T,r)-4*T*S.diff(h,r))/(2*r))
assert harm7.coeff(r,7)==b1/160
psi=c*x*y-x*y*(11*x*x+5*y*y)/48
rho=x*x*y
U=(-S.diff(psi,y),S.diff(psi,x))
R=S.expand((cl*x+U[0])*S.diff(rho,x)+(cl*y+U[1])*S.diff(rho,y)-rho)
expected=(3*cl-c-1)*x*x*y-S.Rational(11,48)*x**4*y+S.Rational(25,48)*x*x*y**3
assert S.expand(R-expected)==0
rho3=x*x*y;rho5=b1*rho3*(x*x+y*y)
U3=(U[0]+c*x,U[1]-c*y)
R5=S.expand(-A*x*S.diff(rho5,x)+(2*A+1)*y*S.diff(rho5,y)-rho5+U3[0]*S.diff(rho3,x)+U3[1]*S.diff(rho3,y))
eq1=R5.coeff(x,4).coeff(y,1);eq2=R5.coeff(x,2).coeff(y,3)
sol=S.solve([eq1,eq2],[A,b1],dict=True)
assert sol==[{A:S.Rational(11,3),b1:-S.Rational(1,32)}]
# Verify the fifth-degree field by Poisson, divergence and curl independently.
assert S.expand(-S.diff(psi,x,2)-S.diff(psi,y,2)-S.diff(rho,x))==0
assert S.expand(S.diff(U[0],x)+S.diff(U[1],y))==0
assert S.expand(S.diff(U[1],x)-S.diff(U[0],y)+S.diff(rho,x))==0
# The exact seventh angular product, with arbitrary radial mode data.
H,Hp,T0,Tp,S0,Sp=S.symbols('H Hp T0 Tp S0 Sp')
angular=-(2*S0*S.cos(2*theta)+4*T0*S.cos(4*theta))*Hp*(S.sin(theta)+S.sin(3*theta))
angular+=(Sp*S.sin(2*theta)+Tp*S.sin(4*theta))*H*(S.cos(theta)+3*S.cos(3*theta))
z=S.symbols('z',nonzero=True)
expr=S.expand(angular.rewrite(S.exp)).subs(S.exp(S.I*theta),z)
# Independent exponential expansion and Laurent coefficient extraction.
expr=S.expand(expr)
coef=S.simplify(2*S.I*expr.coeff(z,7))
assert S.simplify(coef-(3*H*Tp-4*T0*Hp)/2)==0
out={'degree5_residual':str(R5),'degree5_possible_parameters':[{str(k):str(v) for k,v in d.items()} for d in sol], 'degree7_sin7_coefficient':str(harm7.coeff(r,7)),'seventh_mode_identity':str(coef),'poisson_divergence_curl':'exact zero','status':'all assertions passed'}
p=Path(__file__).resolve().parents[1]/'verification'/'symbolic.json'
p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
