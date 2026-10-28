from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as s
x,y,e=s.symbols('x y e',real=True)
aa,bb=s.symbols('alpha beta',real=True)
def k1(x,y):return -x*y/(s.pi*(x*x+y*y)**2)
def k2(x,y):return (x*x-y*y)/(2*s.pi*(x*x+y*y)**2)
u=[]
for kernel in (k1,k2):
 f=0
 for sx in (-1,1):
  for sy in (-1,1):
   f+=sy*kernel(x-sx*2,y-sy*3)
 t=0
 for degree in (0,1,2,3):
  for i in range(degree+1):
   j=degree-i
   coeff=s.diff(f,x,i,y,j).subs({x:0,y:0})/(s.factorial(i)*s.factorial(j))
   t+=s.simplify(coeff)*x**i*y**j
 u.append(s.expand(t))
c=s.Rational(36,2197)/s.pi
checks={}
checks['kernel_linear_u1']=s.diff(u[0],x).subs({x:0,y:0})+c
checks['kernel_linear_u2']=s.diff(u[1],y).subs({x:0,y:0})-c
checks['kernel_divergence']=s.diff(u[0],x)+s.diff(u[1],y)
checks['kernel_parity_u1']=u[0].subs(x,-x)+u[0]
checks['kernel_parity_u2']=u[1].subs(y,-y)+u[1]
v03=s.expand(u[1]).coeff(y,3).subs(x,0)
rho=x*x*y*(1+aa*x*x+bb*y*y)
prod=u[0]*s.diff(rho,x)+u[1]*s.diff(rho,y)
r2=x*x+y*y
gamma=-c+(bb*c-5*v03)*r2-3*bb*v03*r2**2
diff=s.expand(prod-x*x*y*gamma)
deg5=s.expand(diff.subs({x:e*x,y:e*y})).coeff(e,5)
checks['outer_remainder_degree3']=s.expand(diff.subs({x:e*x,y:e*y})).coeff(e,3)
checks['outer_remainder_axis_factor']=s.expand(deg5).subs(x,0)
checks['outer_remainder_is_x4y']=s.rem(s.Poly(deg5,x,y),s.Poly(x**4*y,x,y)).as_expr()
# Directly audit the scalar exponents in the weighted double integrals.
a=s.Rational(17,4); eta=s.Rational(5,4); k=s.symbols('k'); q=s.symbols('density_exponent')
checks['local_scale']=(q+a-5)+3+(1-a)-(q-1)
checks['inner_near_dr']=0+(2*a+2)-2*a+1-3
checks['inner_far_dr']=2*(k-3)+(eta+2)-eta+1-(2*k-3)
checks['outer_near_dr']=10-2*a+1-s.Rational(5,2)
checks['outer_far_dr']=2*k+(eta-4)-eta+1-(2*k-3)
checks['outer_input_near_dr']=(2*a-9)-s.Rational(-1,2)
assert a>4 and a<s.Rational(9,2) and eta<2
result={name:str(s.simplify(value)) for name,value in checks.items()}
assert all(v=='0' for v in result.values()),result
out={'date_utc':datetime.now(timezone.utc).isoformat(),'checks':result,'point_source_cubic_velocity':[str(v) for v in u],'degree5_remainder':str(s.factor(deg5)),'status':'PASS','scope':'Algebraic checks and exact scaling exponents; functional estimates are proved in PROOF.md.'}
path=Path(__file__).resolve().parents[1]/'evidence'/'check.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
