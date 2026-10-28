"""An independent exact Gaussian integral check of the gradient coupling identity."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as S,json
x,y=S.symbols('x y',real=True)
def D(p,z):return S.diff(p,z)-2*z*p
p=(1+x*x)*y
f=-D(D(p,x),x)-D(D(p,y),y)
u=[-D(D(p,x),y),D(D(p,x),x)]
rho=y+y**3+x*x*y;v=1+x*x+2*y*y
b=[v*S.diff(rho,z) for z in (x,y)]
df=[D(f,z) for z in (x,y)]
lhs=-sum(b[j]*D(u[j],z)*df[i] for i,z in enumerate((x,y)) for j in range(2))
rhs=v*(S.diff(rho,y)*df[0]**2-S.diff(rho,x)*df[0]*df[1])+S.Rational(1,2)*(S.diff(b[0],x,y)-S.diff(b[1],x,2))*f*f+sum(f*S.diff(b[j],z)*D(u[j],z) for z in (x,y) for j in range(2))
def gauss(p):
 total=0
 for (i,j),a in S.Poly(S.expand(p),x,y).terms():
  if i%2 or j%2:continue
  total+=a*S.factorial2(i-1)*S.factorial2(j-1)/S.Integer(4)**((i+j)//2)
 return S.factor(total)
l=gauss(lhs);r=gauss(rhs);assert l==r
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'test_potential':'(1+x^2)y exp(-r^2)','test_density':'y+y^3+x^2 y','weight_squared':'1+x^2+2y^2','lhs_divided_by_pi_over_two':str(l),'rhs_divided_by_pi_over_two':str(r),'verdict':'CONFIRMED exact rational equality'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
