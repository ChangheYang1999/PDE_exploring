"""Independent exact identities and positive quadratures for result78."""
from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as s
import mpmath as mp
mp.mp.dps=60
checks=[]
x,y,eps=s.symbols('x y eps',real=True)
alpha,beta,B,L=s.symbols('alpha beta B L',positive=True)
I=1/(2*(s.sqrt(alpha)+s.sqrt(beta))**2)
q1=s.simplify((2*B*alpha**2*(I+2*alpha*s.diff(I,alpha)/3)).subs({alpha:L**-2,beta:1}))
q2=s.simplify((2*B*alpha*beta*(I+2*beta*s.diff(I,beta)/3)).subs({alpha:L**-2,beta:1}))
assert s.factor(q1-B*(1+3*L)/(3*L**2*(L+1)**3))==0
assert s.factor(q2-B*(L+3)/(3*(L+1)**3))==0
assert s.factor(q1+q2-B/(3*L**2))==0
checks += ['quartic_x_heat_coefficient','quartic_y_heat_coefficient','quartic_Poisson_sum']
t,a,b,e,u,v=s.symbols('t a b e u v',real=True)
rho=a*y-b*x*x*y-e*y**3
psi=-x*y+(t/s.Integer(6)+u)*x**3*y+(t/s.Integer(6)+v)*x*y**3
R=(2*x-s.diff(psi,y))*s.diff(rho,x)+(2*y+s.diff(psi,x))*s.diff(rho,y)-rho
R3=s.expand(R.subs({x:eps*x,y:eps*y})).coeff(eps,3)
assert s.expand(R3-((-6*b+a*(t/2+3*u))*x*x*y+(-2*e+a*(t/6+v))*y**3))==0
checks.append('full_cubic_transport')
th=s.symbols('theta',real=True)
for j,expect in [(0,s.Rational(5,8)*s.pi),(1,s.pi/8),(2,s.pi/8)]:
 assert s.integrate(s.cos(th)**(2*j)*s.sin(th)**(6-2*j),(th,0,2*s.pi))==expect
checks += ['angular_gram_y6','angular_gram_x2y4','angular_gram_x4y2']
cc=s.symbols('cc',positive=True);d=B/(cc*B+1)**2;tt=1-d;aa=B+4*tt
bx=tt+B/(cc*B)**2;ey=tt+B
cx=-6*bx+aa*(tt/2+3*q1.subs(L,cc*B));cy=-2*ey+aa*(tt/6+q2.subs(L,cc*B))
limits=[s.limit(z/B,B,s.oo) for z in (bx,ey,cx,cy)]
assert limits==[0,1,s.Rational(1,2),-s.Rational(11,6)]
Q=lambda z,w:z*z+2*z*w+5*w*w
assert s.factor(Q(limits[2],limits[3])/Q(limits[0],limits[1]))==s.Rational(137,45)
checks += ['large_B_four_coefficients','endpoint_137_over_45']
r=s.symbols('r',positive=True)
Hb=((s.Rational(2,7))*((1+r*r)**s.Rational(7,4)-1)-s.Rational(2,3)*((1+r*r)**s.Rational(3,4)-1))/r**4
assert s.simplify(r*s.diff(Hb,r)+4*Hb-(1+r*r)**s.Rational(-1,4))==0
assert s.series(Hb,r,0,4).removeO()==s.Rational(1,4)-r*r/24
checks += ['base_H_radial_equation','base_H_cubic_expansion']
z=s.symbols('z',real=True)
assert s.integrate((1+z*z)**-3,(z,-s.oo,s.oo))==3*s.pi/8
assert s.Rational(1,1000)/(s.Rational(3,8))==s.Rational(1,375)
checks += ['remote_denominator_constant','remote_lower_bound_constant']
gram=s.integrate((-b*s.cos(th)**2*s.sin(th)-e*s.sin(th)**3)*(u*s.cos(th)**2*s.sin(th)+v*s.sin(th)**3),(th,0,2*s.pi))
assert s.expand(gram-s.pi*(-(b+e)*u-(b+5*e)*v)/8)==0
assert s.expand(4*B**2-7*B-12-(4*(B-9)**2+65*(B-9)+249))==0
kernel=s.sin(th)**2*(4*s.sin(th)**2-3)
assert s.trigsimp(s.diff(s.cos(th)*s.sin(th)**3,th)+kernel)==0
assert s.integrate(kernel,(th,0,s.pi/2))==0
checks += ['mixed_cubic_Gram','strict_positive_polynomial','angular_strain_kernel_derivative','angular_strain_kernel_cancellation']
rows=[]
for mm in ['2.2','2.5','2.9','3','3.1','3.5','3.8']:
 m=mp.mpf(mm)
 # Positive log chart avoids loss in 1-exp(-s) and resolves both endpoints.
 def f(z):
  ss=mp.exp(z)
  return mp.exp((2-m)*z)*(-mp.expm1(-ss))**2
 cuts=[-mp.inf,-20,-5,0,3,10,mp.inf]
 # Evaluate the tails in the original s chart to avoid nested exp at infinity.
 val=mp.quad(lambda ss:ss**(1-m)*mp.expm1(-ss)**2,[0,mp.mpf('.25'),1,4,mp.inf])
 ref=2*mp.log(2) if m==3 else mp.gamma(4-m)*(mp.power(2,m-2)-2)/((m-3)*(m-2))
 rel=abs(val-ref)/ref
 # Tanh-sinh endpoint tails at m=2.2 or3.8 converge more slowly.
 assert rel<mp.mpf('1e-11'),(mm,rel)
 lower=4*mp.quad(lambda ss:ss**(3-m)*mp.exp(-2*ss),[mp.mpf('.5'),1,4,mp.inf])/ref
 assert lower>0
 rows.append({'m':mm,'J_quadrature':mp.nstr(val,45),'J_reference':mp.nstr(ref,45),'relative_error':mp.nstr(rel,18),'lower_R_squared':mp.nstr(lower,45)})
 if m==3: assert abs(lower-1/(mp.e*mp.log(2)))<mp.mpf('1e-50')
heat=[]
for lv in [1,4,37]:
 la=mp.mpf(lv);al=la**-2
 ix=mp.quad(lambda z:(1+4*al*z)**mp.mpf('-2.5')*(1+4*z)**mp.mpf('-1.5'),[0,1,la**2,mp.inf])
 iy=mp.quad(lambda z:(1+4*al*z)**mp.mpf('-1.5')*(1+4*z)**mp.mpf('-2.5'),[0,1,la**2,mp.inf])
 xx=2*al**2*ix;yy=2*al*iy
 ex=(1+3*la)/(3*la**2*(la+1)**3);ey=(la+3)/(3*(la+1)**3)
 assert abs(xx/ex-1)<mp.mpf('1e-50') and abs(yy/ey-1)<mp.mpf('1e-50')
 heat.append({'L':lv,'q1_per_B':mp.nstr(xx,45),'q2_per_B':mp.nstr(yy,45),'max_relative_error':mp.nstr(max(abs(xx/ex-1),abs(yy/ey-1)),18)})
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','exact_checks':checks,'J_positive_quadrature':rows,'quartic_heat_quadrature':heat,'scope':'Supporting exact algebra and60-digit positive quadratures. Dominated convergence, scope and all endpoint bounds are proved in PROOF.md; no samples certify a general profile.'}
p=Path('research/capped_weighted_limits/verification/checks.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
