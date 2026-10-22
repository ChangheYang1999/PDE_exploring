"""Independent exact Cartesian check of packet92, after its informal proof."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as S,json,time,hashlib
namespace={}
source=Path('code_independent/check_third_tail_cartesian.py').read_text().split('cases=[]',1)[0]
exec(compile(source,'own_cartesian_definitions','exec'),namespace)
x,y,R,z=[namespace[n] for n in ['x','y','R','z']]
dx,dy,dot,velocity,curl,circle,invert,cart_stream,is_zero=[namespace[n] for n in ['dx','dy','dot','velocity','curl','circle','invert','cart_stream','is_zero']]
start=time.monotonic();a,h,d=S.symbols('a h d',real=True);p=-9*a/16;k0=S.Rational(5,3);k1=S.Rational(4,3)
psi0=p*x*R**S.Rational(2,3);th0=x*x*R**S.Rational(-5,3)*(h+d*y/R)
u0=velocity(psi0);om0=curl(psi0);om1=S.expand(dot(u0,om0)-dx(th0));th1=dot(u0,th0)
A1=circle(om1);F1=invert(A1,k1);psi1=cart_stream(F1,k1);u1=velocity(psi1)
om2=S.expand((dot(u0,om1)+dot(u1,om0)-dx(th1))/2);A2=circle(om2)
alpha=S.factor(A2.coeff(z,1)+A2.coeff(z,-1));c=(z+1/z)/2;t=(z-1/z)/(2*S.I)
sin2=2*c*t;cos3=4*c**3-3*c;sin4=4*c*t*(1-2*t*t);Q=9*a*a/16-d/3
A1_want=S.expand(Q*sin2-3*h*c/4+5*h*cos3/12+d*sin4/3)
F1_want=S.expand(9*Q*sin2/20+27*h*c/28+3*h*cos3/52+3*d*sin4/128)
H1_want=S.expand(p*(-3*h*c*c*t-3*d*c*c*t*t+S.Rational(5,3)*d*c**4))
checks={'omega0_negative_curl':is_zero(circle(om0)-a*c),'A1_cartesian':is_zero(A1-A1_want),'F1_cartesian':is_zero(F1-F1_want),'H1_cartesian':is_zero(circle(th1)-H1_want),'u1_negative_curl':is_zero(circle(curl(psi1))-A1),'u0_divergence':is_zero(circle(dx(u0[0])+dy(u0[1]))),'alpha_exact':S.factor(alpha+3*a*(27*a*a-41*d)/320)==0,'alpha_sine_first_zero':S.expand(A2.coeff(z,1)-A2.coeff(z,-1))==0,'alpha_mean_zero':S.expand(A2).coeff(z,0)==0}
examples=[]
for dv,expected in [(S.Rational(0),S.Rational(-81,320)),(S.Rational(27,41),S.Rational(0)),(S.Rational(4,5),S.Rational(87,1600))]:
 av=S.factor(alpha.subs({a:1,h:1,d:dv}));assert av==expected
 examples.append({'a':'1','h':'1','d':str(dv),'alpha':str(av),'H0_over_cos_squared_positive_lower_bound':str(1-abs(dv))})
assert all(checks.values()),checks
out={'created_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'checks':checks,'examples':examples,'alpha_exact':str(alpha),'all_pass':True,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact symbolic Cartesian calculation on exterior homogeneous data, not global B2 profiles.'}
Path('research/92_beta_three_resonance_not_forced_by_sign/verification/cartesian_exact_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
