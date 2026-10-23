from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as S
import mpmath as mp
root=Path('research/hydrostatic_axis_audit/verification');checks=[]
def ck(name,x):
 ok=bool(x);checks.append(dict(name=name,passed=ok));assert ok,name
y,x,e,c=S.symbols('y x e c',real=True);v=S.Function('v')(y);G=S.Function('G')(y)
h1=c-S.diff(v,y);g2=-S.diff(v,y,2)/2
b2=((4*c-1-2*S.diff(v,y))*S.diff(v,y,2)+v*S.diff(v,y,3))/(2*S.diff(G,y))
ck('formal_b2_coefficient',S.simplify(2*(c+h1)*g2+v*S.diff(g2,y)+S.diff(G,y)*b2-g2)==0)
h3=-S.diff(b2,y)/3;g4=-S.diff(b2,y,2)/12
ck('formal_h3_relation',S.simplify(S.diff(b2,y)+3*h3)==0)
ck('formal_g4_relation',S.simplify(S.diff(h3,y)-4*g4)==0)
w=c*y-(c-1)*S.atan(y)
ck('arctan_vprime',S.simplify(S.diff(w,y)-(c-(c-1)/(1+y*y)))==0)
ck('arctan_vsecond',S.simplify(S.diff(w,y,2)-2*(c-1)*y/(1+y*y)**2)==0)
ck('arctan_cubic',S.limit((w-y)/y**3,y,0)==(c-1)/3)
ck('arctan_integrand_slope',S.limit((1/w-1/y)/y,y,0)==-(c-1)/3)
R=S.symbols('R',positive=True);prim=-(1-y/R)*S.diff(v,y)-v/R
ck('finite_radius_integrand',S.simplify(S.diff(prim,y)+(1-y/R)*S.diff(v,y,2))==0)
g=S.Function('g')(x,y);h=S.Function('h')(x,y);u=S.Function('u')(x,y);z=S.Function('z')(x,y)
gp=g+e*u;hp=h+e*z
F=c-S.diff((gp-(c*x+hp)*S.diff(hp,y))/S.diff(gp,y),y)
b=(g-(c*x+h)*S.diff(h,y))/S.diff(g,y)
want=-S.diff((u-S.diff(h,y)*z-(c*x+h)*S.diff(z,y)-b*S.diff(u,y))/S.diff(g,y),y)
ck('exact_full_linearization',S.simplify(S.diff(F,e).subs(e,0)-want)==0)
a=S.Function('a')(y);q=S.Function('q')(y);H=S.Function('H')(y);b=S.Function('b')(y);uu=S.Function('u')(y);zz=S.Function('z')(y)
L=-S.diff((uu-H*zz-a*S.diff(zz,y)-b*S.diff(uu,y))/q,y)
L0=S.expand(L).subs({H:0,S.diff(H,y):0,a:0,S.diff(a,y):0})
coef2=b/q;coef1=S.diff(b/q,y)-1/q;coef0=S.diff(q,y)/q**2
ck('axis_no_z_terms',not L0.has(zz,S.diff(zz,y),S.diff(zz,y,2)))
ck('axis_u_coefficients',S.simplify(L0-(coef2*S.diff(uu,y,2)+coef1*S.diff(uu,y)+coef0*uu))==0)
eta,lam=S.symbols('eta lam',real=True);B,Q,Q1,B1=S.symbols('B Q Q1 B1',real=True)
f2=B/Q;f1=B1/Q-B*Q1/Q**2-1/Q;f0=Q1/Q**2
A=S.Matrix([[0,S.I*eta],[-f2*eta**2+S.I*f1*eta+f0,0]])
ck('frozen_characteristic_polynomial',S.simplify((lam*S.eye(2)-A).det()-(lam**2+S.I*f2*eta**3+f1*eta**2-S.I*f0*eta))==0)
s,D=S.symbols('s D',positive=True);Fv,Fp=S.symbols('F Fp')
axisexpr=2*s*(c+D*Fv)*Fp+(c-D*Fv-2*D*s*Fp)*Fv-Fv
ck('elliptical_axis_ODE',S.expand(axisexpr.subs(D,c-1)-(2*c*s*Fp-(c-1)*Fv*(Fv-1)))==0)
nu,k=S.symbols('nu k',positive=True);ff=1/(1-k*s**nu)
ck('elliptical_explicit_solution',S.simplify(s*S.diff(ff,s)-nu*ff*(ff-1))==0)
la,mu=S.symbols('lambda mu',positive=True);ck('hydrostatic_scaling_V1',S.simplify(la**2/mu*mu/la-la)==0);ck('hydrostatic_scaling_V2',S.simplify(la**2/mu*mu**2/la**2-mu)==0)
ck('hydrostatic_scaling_slope',S.simplify(la**2/mu/mu-(la/mu)**2)==0)
mp_rows=[]
with mp.workdps(60):
 for C in [mp.mpf('1.5'),mp.mpf(2),mp.mpf(3)]:
  VV=lambda t:C*t-(C-1)*mp.atan(t)
  for Y in [mp.mpf('.1'),mp.mpf(1),mp.mpf(10)]:
   curvature=lambda t:-2*(C-1)*t/(1+t*t)**2
   I=mp.quad(lambda t:(1-t/Y)*curvature(t),[0,Y]);rhs=1-VV(Y)/Y
   ck(f'axis_integral_c{C}_R{Y}',abs(I-rhs)<mp.mpf('1e-55'))
   mp_rows.append(dict(c=str(C),R=str(Y),integral=str(I),rhs=str(rhs)))
 for sign in [-1,1]:
  freq=sign*mp.mpf(10)**6;f2=mp.mpf(3)/2;f1=mp.mpf(-1)/3;f0=mp.mpf(1)/7
  lam0=mp.sqrt(-1j*f2*freq**3-f1*freq**2+1j*f0*freq)
  target=mp.sqrt(f2/2)*abs(freq)**mp.mpf('1.5')
  ck(f'frozen_high_frequency_sign{sign}',abs(abs(lam0.real)/target-1)<mp.mpf('1e-6'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',checks=checks,MP_checks=mp_rows,code_sha256=sha(Path(__file__)),proof_sha256=sha(root.parent/'PROOF.md'),source_sha256={p.name:sha(p)for p in root.iterdir()if p.is_file()},repairs=['Do not preserve real analyticity under arbitrary nonzero supported smooth perturbations.','State smooth formal axis data in the all-order recurrence.','Do not claim a vanishes only on the axis or that frozen ill-posedness forces a unique global construction method.','Stronger axis tail is automatic under stated bounds; F(0) may be defined by continuity.'],endpoint='UNRESOLVED')
(root/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='MP_checks'}))
