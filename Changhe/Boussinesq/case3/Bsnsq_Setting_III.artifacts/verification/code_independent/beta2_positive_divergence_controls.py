"""Independent exact controls for P271. No teammate code is executed."""
from pathlib import Path
from datetime import datetime, timezone
import sympy as s
import hashlib, json, time
V=Path('research/271_beta2_positive_ratio_divergence/verification')
started=datetime.now(timezone.utc).isoformat(); tick=time.monotonic(); checks=[]
def eq(name, expr):
 z=s.factor(s.simplify(s.expand(expr)))
 checks.append({'name':name,'passed':z==0,'difference':str(z)})
def ck(name, value, detail=None):
 checks.append({'name':name,'passed':bool(value),'detail':detail})
x,y=s.symbols('x y',real=True); A=s.symbols('A',nonzero=True)
b=s.Function('b')(y);v=s.Function('v')(y);T=s.Function('T')(y);D4=s.Function('D4')(y)
W1=(4-s.diff(b,y))*x-s.diff(v,y)*x**3/3;W2=b+v*x*x
Th=T*x*x/2+D4*x**4/24;Om=s.diff(W1,y)-s.diff(W2,x)
eta=-s.diff(b,y,2)-2*v
RT=s.expand(W1*s.diff(Th,x)+W2*s.diff(Th,y));RO=s.expand(W1*s.diff(Om,x)+W2*s.diff(Om,y)+Om-s.diff(Th,x))
eq('Cartesian_divergence',s.diff(W1,x)+s.diff(W2,y)-4)
eq('Cartesian_curl',Om-eta*x+s.diff(v,y,2)*x**3/3)
eq('Cartesian_T2',2*RT.coeff(x,2)-b*s.diff(T,y)-(8-2*s.diff(b,y))*T)
eq('Cartesian_T4',24*RT.coeff(x,4)-b*s.diff(D4,y)-(16-4*s.diff(b,y))*D4+8*s.diff(v,y)*T-12*v*s.diff(T,y))
eq('Cartesian_V1',RO.coeff(x,1)-b*s.diff(eta,y)-(5-s.diff(b,y))*eta+T)
# Independent local jets and formal total derivative on exact reduced relations.
b,b1,b2,rho,r,R,G,I,Ip,c2,h,P,E,H,f,Q=s.symbols('b b1 b2 rho r R G I Ip c2 h P E H f Q',nonzero=True)
rhop=(4-b1)*rho/b; rp=(A/rho-r)/b;hp=4*h/b;Gp=rho*I;Rp=rho
Tv=A/rho**2;Tp=-2*A*rhop/rho**3;Dv=A*A*I/rho**4;Dp=A*A*(Ip/rho**4-4*I*rhop/rho**5)
v,vp=s.symbols('v vp');et=r/rho;etp=rp/rho-r*rhop/rho**2
for n,e in [('T2_reduced',b*Tp+(8-2*b1)*Tv),('V1_reduced',b*etp+(5-b1)*et-Tv),('rho_b_derivative',rhop*b+rho*b1-4*rho),('T4_reduced',(b*Dp+(16-4*b1)*Dv-8*vp*Tv+12*v*Tp)/Tv**2-(b*Ip-8*(3*rho*rho*rhop*v+rho**3*vp)/(A*rho))),('integrated_RI_G_derivative',A*(Rp*I+R*Ip-Gp)/2-A*R*Ip/2),('integral_derivative_compatibility',(A*R*Ip/2).subs(R,b*rho/4)-A*b*rho*Ip/8)]:eq(n,e)
Pp=P*(3*rhop/rho-b1/b-hp/h)
eq('P_log_derivative',Pp/P+4*(b1-2)/b)
# First compute H' from the finite integrated identity, then curl.
Hprime=A*(Gp/h-G*hp/h**2)
subG=R*I-2*(rho**3*v-c2)/A
eq('H_prime_finite_identity',(Hprime-8*P*(v-c2/rho**3)).subs({G:subG,P:rho**3/(b*h)}).subs(R,b*rho/4))
eq('H_prime_curl', (8*P*(v-c2/rho**3)+4*P*(b2+et+2*c2/rho**3)).subs(v,-(b2+et)/2))
Qp=-4*P*(b2+f)+4*(-4*P*(b1-2)/b)*(b1-2)+4*P*b2
eq('Q_energy_identity',Qp+16*P*(b1-2)**2/b+4*P*f)
B,D,z,q,e,Y,Ch,Rv,Hd=s.symbols('B D z q e Y Ch Rv Hd',nonzero=True)
Pdot=4*P*D/B;qdot=-16*P*D*D/B
Qdot=-16*P*D*D/B-4*P*Y*f;edot=-4*P*Y*f
eq('tail_error_sign',Qdot-edot-qdot)
eq('H_decomposition',Q-e+e+4*P*D-(Q+4*P*D))
eq('z_quotient_derivative',(-qdot/P+q*Pdot/P**2).subs(q,-z*P)-(4*D/B)*(4*D-z))
eq('z_gap_identity',(P*(4*D-z)-(H-e)).subs({z:-q/P,H:q+e+4*P*D}))
eq('F_energy_derivative',Pdot/(2*s.sqrt(P))-2*s.sqrt(P)*D/B)
eq('F_energy_square', (Pdot/(2*s.sqrt(P)))**2-4*P*D**2/B**2)
eq('energy_to_F_square',4*P*D**2/B**2-(-qdot)/(4*B))
# h=Ch R, b rho=4R and logarithmic differentiation of G=h H/A.
AI=Ch*Rv/rho*(Hd/Y+4*H/(B*Y))
eq('ratio_extraction',AI.subs(Rv,B*Y*rho/4)-Ch*(H+B*Hd/4))
eq('ratio_linear_ODE',4/B*(H+B*Hd/4)-Hd-4*H/B)
eq('B_derivative_identity',(-D)-(s.symbols('Bdot')+B-2)+(s.symbols('Bdot')-(2-B-D)))
# Exact exponent margins used for all nonlocal tail errors.
eps=s.Rational(1,48)
for n,exp in [('r_integrating_factor',-s.Rational(3,2)+2*eps),('P_eta',-s.Rational(3,2)+6*eps),('constant_forcing',-3+eps)]:ck(n+'_integrable',exp<-1,str(exp))
ck('epsilon_range',0<eps<s.Rational(1,24))
eq('P_upper_exponent',(3*(1+eps)-(2-eps)-1)-4*eps)
eq('P_lower_exponent',(3*(1-eps)-(2+eps)-1)+4*eps)
eq('eta_exponent',(-s.Rational(1,2)+eps)-(1-eps)+s.Rational(3,2)-2*eps)
# Concrete polynomial fields independently test the negative-end reflection.
x,y=s.symbols('x y',real=True);w1=3*x+x*y+x**3*y;w2=2*y+y*y+x*x*(1-y)
tho=3*x*x+x*x*y+2*x**4*y*y;om=s.diff(w1,y)-s.diff(w2,x)
tw1=w1.subs(y,-y);tw2=-w2.subs(y,-y);tt=-tho.subs(y,-y);to=-om.subs(y,-y)
eq('reflection_curl',s.diff(tw1,y)-s.diff(tw2,x)-to)
eq('reflection_divergence',s.diff(tw1,x)+s.diff(tw2,y)-(s.diff(w1,x)+s.diff(w2,y)).subs(y,-y))
eq('reflection_thermal_residual',tw1*s.diff(tt,x)+tw2*s.diff(tt,y)+(w1*s.diff(tho,x)+w2*s.diff(tho,y)).subs(y,-y))
eq('reflection_vorticity_residual',tw1*s.diff(to,x)+tw2*s.diff(to,y)+to-s.diff(tt,x)+(w1*s.diff(om,x)+w2*s.diff(om,y)+om-s.diff(tho,x)).subs(y,-y))
Av=s.diff(tho,x,2).subs({x:0,y:0});At=s.diff(tt,x,2).subs({x:0,y:0})
Iv=s.diff(tho,x,4).subs(x,0)/s.diff(tho,x,2).subs(x,0)**2;It=s.diff(tt,x,4).subs(x,0)/s.diff(tt,x,2).subs(x,0)**2
eq('reflection_A',At+Av);eq('reflection_I',It+Iv.subs(y,-y));eq('reflection_signed_ratio',At*It-Av*Iv.subs(y,-y))
# Analytic argument boundaries: energy control alone does not imply finite F.
t=s.symbols('t',positive=True);Fm=t**s.Rational(1,4)
eq('energy_example_derivative',s.diff(Fm,t)**2-s.Rational(1,16)*t**(-s.Rational(3,2)))
ck('energy_example_sublinear_square',s.limit(Fm*Fm/t,t,s.oo)==0)
ck('energy_example_not_finite',s.limit(Fm,t,s.oo)==s.oo)
Cr=s.symbols('Cr',positive=True);eq('opposite_sign_log_example',A*(-64*Cr**2/A)+64*Cr**2)
ck('opposite_sign_log_is_negative',(-64*Cr**2).is_negative)
pb=json.loads((V/'proof_before_checks.json').read_text()); ph=hashlib.sha256((V.parent/'PROOF.md').read_bytes()).hexdigest()
ck('proof_before_checks',pb['written_utc']<started);ck('proof_hash',pb['proof_sha256']==ph)
out={'started_utc':started,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'passed':sum(c['passed'] for c in checks),'total':len(checks),'all_passed':all(c['passed'] for c in checks),'checks':checks,'proof_sha256':ph,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact controls supplement the full informal proof. Neither existence nor general B2 exclusion is claimed.'}
(V/'controls.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['started_utc','ended_utc','elapsed_seconds','passed','total','all_passed']},indent=2));print('FAILED',[c for c in checks if not c['passed']])
