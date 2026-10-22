"""Independent physical-coordinate controls for P257; no lead/NUM code execution."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s,json,hashlib,time
V=Path('research/257_nonzero_axis_ratio_limit/verification');t0=time.monotonic();start=datetime.now(timezone.utc).isoformat();checks=[]
x,y=s.symbols('x y',real=True);beta,A,c2=s.symbols('beta A c2',nonzero=True);alpha=(beta-2)/2;d=(3*beta+2)/2;h=(beta+6)/2
rho=s.Function('rho')(y);R=s.Function('R')(y);I=s.Function('I')(y);v=s.Function('v')(y);T=s.Function('T')(y);Q=s.Function('Q')(y);b=s.Function('b')(y)
def check(n,e):
 z=s.factor(s.cancel(s.expand(e)));checks.append({'name':n,'passed':z==0,'difference':str(z)})
def positive(n,e,z):
 p=s.Poly(s.factor(e).subs(beta,2+z).cancel(),z)if s.denom(s.factor(e).subs(beta,2+z).cancel())==1 else None
 # Record denominator and test positive-coefficient numerator/denominator separately.
 num,den=s.fraction(s.factor(e).subs(beta,2+z).cancel());pn=s.Poly(num,z);pd=s.Poly(den,z)
 good=all(a>=0 for a in pn.all_coeffs()+pd.all_coeffs())and any(a>0 for a in pn.all_coeffs())and any(a>0 for a in pd.all_coeffs());checks.append({'name':n,'passed':bool(good),'positive_parameter':str(z),'numerator':str(pn.as_expr()),'denominator':str(pd.as_expr())})
def RD(e):return s.expand(e).subs(s.diff(R,y),rho)
w=2*beta-s.diff(b,y);W1=w*x-s.diff(v,y)*x**3/3;W2=b+v*x**2;theta=T*x**2/2+Q*x**4/24;omega=s.diff(W1,y)-s.diff(W2,x)
rt=s.expand(W1*s.diff(theta,x)+W2*s.diff(theta,y)-(beta-2)*theta);rv=s.expand(W1*s.diff(omega,x)+W2*s.diff(omega,y)+omega-s.diff(theta,x))
check('divergence',s.diff(W1,x)+s.diff(W2,y)-2*beta)
axisT=b*s.diff(T,y)+(3*beta+2-2*s.diff(b,y))*T
check('thermal_x2_factor',rt.coeff(x,2)-axisT/2)
axis4=4*w*Q-8*T*s.diff(v,y)+b*s.diff(Q,y)+12*v*s.diff(T,y)-(beta-2)*Q
check('thermal_x4_factor',rt.coeff(x,4)-axis4/24)
eta=-s.diff(b,y,2)-2*v
check('negative_curl_x',omega.coeff(x,1)-eta)
check('vorticity_x_ODE',rv.coeff(x,1)-(b*s.diff(eta,y)+(2*beta+1-s.diff(b,y))*eta-T))
bs=d*R/rho;ws=2*beta-s.diff(bs,y);Ts=A/rho**2;Qs=A**2*I/rho**4
check('axis_rho_identity',RD(bs*s.diff(Ts,y)+(3*beta+2-2*s.diff(bs,y))*Ts))
check('axis_alpha',RD(ws-bs*s.diff(rho,y)/rho-alpha))
formula=s.diff(rho**3*v,y)-A/8*((beta-2)*rho*I+d*R*s.diff(I,y))
raw4=4*ws*Qs-8*Ts*s.diff(v,y)+bs*s.diff(Qs,y)+12*v*s.diff(Ts,y)-(beta-2)*Qs
check('thermal_integrating_factor',RD(raw4+8*A/rho**5*formula))
J=s.Function('J')(y);m=c2+A/8*(d*R*I-h*J)
check('integrated_identity_derivative',RD(s.diff(m,y)).subs(s.diff(J,y),rho*I)-A/8*((beta-2)*rho*I+d*R*s.diff(I,y)))
rr=s.Function('r')(y);etas=rr/rho
axisv=bs*s.diff(etas,y)+(2*beta+1-s.diff(bs,y))*etas-Ts
check('vorticity_r_integrating_factor',RD(rho*axisv-(bs*s.diff(rr,y)+beta*rr/2-A/rho)))
check('d_minus_h',d-h-(beta-2));check('center_eta',beta/2*(2*A/beta)-A)
gamma=s.Rational(1,2)+1/beta;eps=(beta-2)/(12*beta);p=2/beta+2*eps;z=s.symbols('z',positive=True)
for name,expr in [('gamma_positive',gamma),('gamma_lt1',1-gamma),('epsilon_positive',eps),('exponent_gap',gamma-2/beta-3*eps),('p_positive',p),('p_lt1',1-p)]:positive(name,expr,z)
check('lower_growth_exponent',1-2*gamma+2/beta);check('ratio_R_power',d/beta-1-gamma)
# Verify the exact twice-integrated kernel, including its endpoint data.
pp=s.symbols('p',positive=True);Y=s.symbols('Y',positive=True);yy=s.symbols('yy',positive=True)
F=yy**(2-pp)/((1-pp)*(2-pp))-yy*Y**(1-pp)/(1-pp)+Y**(2-pp)/(2-pp)
check('double_integral_second_derivative',s.diff(F,yy,2)-yy**(-pp));check('double_integral_value',F.subs(yy,Y));check('double_integral_first_derivative',s.diff(F,yy).subs(yy,Y))
# Manufactured nonconstant rho/I, with exact integrated v; independently evaluate physical coefficients.
u0,u1,u2=s.symbols('u0 u1 u2');rm=1+y**2;Rm=y+y**3/3;Im=u0+u1*y+u2*y**2;Jm=s.integrate(rm*Im,y);bm=d*Rm/rm;vm=(c2+A/8*(d*Rm*Im-h*Jm))/rm**3;Tm=A/rm**2;Qm=A**2*Im/rm**4
for av in [s.Integer(2),s.Integer(-3)]:
 for bv in [s.Integer(3),s.Rational(5,2)]:
  repl={A:av,beta:bv,u0:1,u1:-2,u2:3,c2:-1};tm=(Tm*x**2/2+Qm*x**4/24).subs(repl);w1=((2*beta-s.diff(bm,y))*x-s.diff(vm,y)*x**3/3).subs(repl);w2=(bm+vm*x**2).subs(repl)
  residual=s.expand(w1*s.diff(tm,x)+w2*s.diff(tm,y)-(bv-2)*tm)
  for n in[2,4]:check(f'manufactured_A{av}_beta{bv}_thermal_x{n}',residual.coeff(x,n))
# The low-order equations can hold exactly with I=0. This explicit polynomial field
# fails sublinearity and is not a prompt-admissible profile.
w1=alpha*x;w2=d*y-A*x**2/beta;om=2*A*x/beta;th=A*x**2/2
check('polynomial_manufacture_div',s.diff(w1,x)+s.diff(w2,y)-2*beta);check('polynomial_manufacture_curl',s.diff(w1,y)-s.diff(w2,x)-om)
check('polynomial_manufacture_thermal',w1*s.diff(th,x)+w2*s.diff(th,y)-(beta-2)*th);check('polynomial_manufacture_vorticity',w1*s.diff(om,x)+w2*s.diff(om,y)+om-s.diff(th,x))
check('manufacture_sublinearity_defect',s.diff(w2,y)-beta-(beta/2+1))
# Explicit parity-preserving y reflection on general polynomial test fields.
f=x*(1+2*y+x**2+y**3);g=y+2*x**2*(1+y)+y**3;tt=x**2*(3+y+x**2*(1-y));oo=s.diff(f,y)-s.diff(g,x)
reflect=lambda e:e.subs(y,-y)
fn=reflect(f);gn=-reflect(g);tn=-reflect(tt);on=-reflect(oo)
check('reflection_div',s.diff(fn,x)+s.diff(gn,y)-reflect(s.diff(f,x)+s.diff(g,y)))
check('reflection_curl',s.diff(fn,y)-s.diff(gn,x)-on)
check('reflection_thermal',fn*s.diff(tn,x)+gn*s.diff(tn,y)-(beta-2)*tn+reflect(f*s.diff(tt,x)+g*s.diff(tt,y)-(beta-2)*tt))
check('reflection_vorticity',fn*s.diff(on,x)+gn*s.diff(on,y)+on-s.diff(tn,x)+reflect(f*s.diff(oo,x)+g*s.diff(oo,y)+oo-s.diff(tt,x)))
check('reflection_A',s.diff(tn,x,2).subs({x:0,y:0})+s.diff(tt,x,2).subs({x:0,y:0}))
it=s.diff(tt,x,4).subs(x,0)/s.diff(tt,x,2).subs(x,0)**2;itn=s.diff(tn,x,4).subs(x,0)/s.diff(tn,x,2).subs(x,0)**2;check('reflection_ratio',itn+reflect(it))
out={'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-t0,'passed':sum(c['passed']for c in checks),'total':len(checks),'checks':checks,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((V.parent/'PROOF.md').read_bytes()).hexdigest(),'scope':'Exact identities and manufactured polynomial/rational tests; analytic asymptotic contradiction is proved in PROOF.md, not inferred from samples.'}
(V/'controls.json').write_text(json.dumps(out,indent=2)+'\n');print(out['passed'],out['total'],out['elapsed_seconds']);print('failed',[c for c in checks if not c['passed']])
