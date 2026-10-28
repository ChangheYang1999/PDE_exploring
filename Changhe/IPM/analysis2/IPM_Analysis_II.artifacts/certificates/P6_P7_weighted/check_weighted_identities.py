from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json
import sympy as s
x,y,R,c,b=s.symbols('x y R c b', real=True)
q=x*x+y*y
K=s.Matrix([-x*y/(s.pi*q*q),(x*x-y*y)/(2*s.pi*q*q)])
J=K.jacobian([x,y])
assert s.simplify(J.T*J-s.eye(2)/(s.pi**2*q**3))==s.zeros(2)
Hnorm=sum(s.diff(K[i],z,w)**2 for i in range(2) for z in (x,y) for w in (x,y))
assert s.simplify(Hnorm-36/(s.pi**2*q**4))==0
t=q/(R*R+q)
b0=-b*c*t
db0=s.diff(b0,x,2)+s.diff(b0,y,2)
assert s.simplify(db0+4*b*c*R**2*(R**2-q)/(R**2+q)**3)==0
u=s.symbols('u',real=True)
poly=-4*u**3+6*u*u-u
ucrit=(3+s.sqrt(6))/6
assert s.simplify(poly.subs(u,ucrit)-s.Rational(1,2)-2*s.sqrt(6)/9)==0
assert s.Rational(99,40)**2>6
assert Q(19,5)-Q(11,10)*Q(37,20)>Q(2,5)
assert 1-Q(31,100)*Q(37,20)>Q(2,5)
assert Q(9,2)*4096*64**3<2**33
assert 64*2**35+2**10<2**42
assert 9000*2*2**16<2**31
assert 24*(2**47+2**36)<2**53
# epsilon=2/5 > 1/4; 2^(-1/4)<7/8 follows from 2>(8/7)^4.
assert Q(8,7)**4<2
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'kernel_JtJ':'I/(pi^2*r^6)','kernel_Hessian_Frobenius_squared':'36/(pi^2*r^8)','radial_laplacian_identity':True,'radial_polynomial_maximum':'1/2+2*sqrt(6)/9 < 21/20','dyadic_constant_inequalities':True,'localization_input_bound':4,'localization_output_bound':6,'commutator_constant':2**53}
Path(__file__).with_name('weighted_identity_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
