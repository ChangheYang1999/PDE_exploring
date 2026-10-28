from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as s
P,Q,S,B,dB,z=s.symbols('P Q S B dB z')
p1=-P/4-3*Q/4+5*S/2+(Q-10*S+B)*z+(8*S-B)*z**2
p2=P/4-Q/4+S/2+(Q-6*S)*z+(8*S-B)*z**2
rad=-(P-Q)*(2*z-1)/4+S*(8*z**2-8*z+1)/2
tan=(P+Q)/2-2*S+(4*S-B)*z
checks={}
checks['cartesian_component1']=p1-(rad-(1-z)*tan)
checks['cartesian_component2']=p2-(rad+z*tan)
def dt(f):
 return s.diff(f,P)*(-B)+s.diff(f,Q)*(-4*Q+B)+s.diff(f,S)*(-6*S+B)+s.diff(f,B)*dB
checks['divergence']=p1+p2+z*dt(p1)+(1-z)*dt(p2)+2*z*(1-z)*(s.diff(p1,z)-s.diff(p2,z))
v=P/4-Q/4+S/2
checks['axis_component2']=p2.subs(z,0)-v
checks['axis_component1']=p1.subs(z,0)+v+(Q-3*S)
b,bt,bth,cs,c=s.symbols('b bt btheta cos_sin c')
bx=2*b+z*bt-cs*bth
by=b+(1-z)*bt+cs*bth
checks['strain_cancellation']=-c*bx+c*by+c*(3*b+bt)/3-c*((s.Rational(4,3)-2*z)*bt+2*cs*bth)
x,y=s.symbols('x y',positive=True)
f=s.Function('f')
r=s.sqrt(x*x+y*y)
expr=x*x*y*f(s.log(r),s.atan(y/x))
args=(s.log(r),s.atan(y/x))
ff=f(*args)
ft=s.Subs(s.Derivative(f(s.Symbol('u'),args[1]),s.Symbol('u')),s.Symbol('u'),args[0])
# The derivative identities are checked by using the actual symbolic derivatives as placeholders.
actual_x=s.diff(expr,x)
actual_y=s.diff(expr,y)
f_t=s.diff(f(s.Symbol('u'),args[1]),s.Symbol('u')).subs(s.Symbol('u'),args[0])
f_th=s.diff(f(args[0],s.Symbol('u')),s.Symbol('u')).subs(s.Symbol('u'),args[1])
checks['background_gradient_x']=actual_x-x*y*(2*ff+x*x/r**2*f_t-x*y/r**2*f_th)
checks['background_gradient_y']=actual_y-x*x*(ff+y*y/r**2*f_t+x*y/r**2*f_th)
k=s.symbols('k')
checks['origin_weight_exponent']=8-s.Rational(17,2)+4-s.Rational(7,2)
checks['far_weight_exponent']=8-s.Rational(5,4)+2*(k-s.Rational(35,8))-2*(k-1)
res={name:str(s.simplify(expr)) for name,expr in checks.items()}
assert all(value=='0' for value in res.values()),res
out={'date_utc':datetime.now(timezone.utc).isoformat(),'checks':res,'status':'PASS'}
path=Path(__file__).resolve().parents[1]/'evidence'/'check.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
