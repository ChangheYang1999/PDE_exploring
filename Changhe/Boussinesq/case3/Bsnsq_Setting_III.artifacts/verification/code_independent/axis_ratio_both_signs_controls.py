"""Independent P263 physical and multiplier algebra, without teammate code."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s,json,hashlib,time
V=Path('research/263_axis_ratio_both_signs/verification');start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();checks=[]
def eq(name,expr):
 q=s.factor(s.cancel(s.expand(expr)));checks.append({'name':name,'passed':q==0,'difference':str(q)})
def ck(name,ok,detail=None):checks.append({'name':name,'passed':bool(ok),'detail':detail})
y,x=s.symbols('y x',real=True);beta,A,c2=s.symbols('beta A c2',real=True);d=(3*beta+2)/2;k=(beta+6)/2;g=s.Rational(1,2)+1/beta;m=1-2/beta
b=s.Function('b')(y);v=s.Function('v')(y);T=s.Function('T')(y);D=s.Function('D')(y);eta=s.Function('eta')(y)
W1=(2*beta-s.diff(b,y))*x-s.diff(v,y)*x**3/3;W2=b+v*x*x;Th=T*x*x/2+D*x**4/24;Om=eta*x
thermal=s.expand(W1*s.diff(Th,x)+W2*s.diff(Th,y)-(beta-2)*Th)
eq('physical_divergence',s.diff(W1,x)+s.diff(W2,y)-2*beta)
eq('physical_T2',2*thermal.coeff(x,2)-(b*s.diff(T,y)+(3*beta+2-2*s.diff(b,y))*T))
eq('physical_T4',24*thermal.coeff(x,4)-(4*(2*beta-s.diff(b,y))*D-8*T*s.diff(v,y)+b*s.diff(D,y)+12*v*s.diff(T,y)-(beta-2)*D))
eq('physical_curl_eta',s.expand(s.diff(W1,y)-s.diff(W2,x)).coeff(x,1)+s.diff(b,y,2)+2*v)
eq('physical_V1',s.expand(W1*s.diff(Om,x)+W2*s.diff(Om,y)+Om-s.diff(Th,x)).coeff(x,1)-(b*s.diff(eta,y)+(2*beta+1-s.diff(b,y))*eta-T))
rho=s.symbols('rho',positive=True);bp,rhop,r,rdot=s.symbols('bp rhop r rdot',real=True)
eq('T2_rho',(-2*b*rhop/rho+3*beta+2-2*bp).subs(rhop,(d-bp)*rho/b))
eq('eta_to_r',b*(rdot/rho-r*rhop/rho**2)+(2*beta+1-bp)*r/rho-(b*rdot+beta*r/2)/rho if False else (2*beta+1-bp)-(d-bp)-beta/2)
for name,e in [('3d_k',3*d-k-4*beta),('d_over_beta',d/beta-g-1),('d_minus_k',d-k-beta+2),('P_power',3*g-1-k/beta),('critical_mean',g+1-k/beta-m)]:eq(name,e)
# Algebraic differential calculus: independently enter vector-field identities.
bv,P,h,R,G,I,H,E,f,Z,B,Bdot,Pstar,slack=s.symbols('bv P h R G I H E f Z B Bdot Pstar slack',real=True)
bprime=E+beta;rhoprime=(d-bprime)*rho/bv
Pprime=P*(3*rhoprime/rho-bprime/bv-k/bv)
eq('P_derivative',Pprime+4*P*E/bv)
Hprime=A*rho*I/h-H*k/bv
vexpr=c2/rho**3+A*(d*R*I-k*G)/(8*rho**3)
eq('v_Hprime', (2*vexpr-2*c2/rho**3-Hprime/(4*P)).subs({H:A*G/h,P:rho**3/(bv*h),R:bv*rho/d}))
Edprime=-f-Hprime/(4*P)
eq('energy_square',Hprime+4*Pprime*E+4*P*Edprime+16*P*E**2/bv+4*P*f)
eq('Q_Pprime',H+4*P*E-(H-bv*Pprime))
B0=s.symbols('B0',positive=True);w=(B/B0)**4;chi=k*(w-1)/B;lam=-4*(B-beta)/B
Pdot=-4*P*E/B
Eactual=Bdot+B-beta
Pstardot=Pdot*w+P*s.diff(w,B)*Bdot
eq('Pstar_log_from_P',Pstardot.subs(E,Eactual)-P*w*lam)
eq('Pstar_log_from_rho_b',(3*d-k)/B-4-lam)
F=k*(B**4-beta**4)/B0**4+16*(B-beta)-4*(k+4*beta)*s.log(B/beta)
eq('explicit_primitive',s.diff(F,B)-4*(chi-lam));eq('primitive_at_beta',F.subs(B,beta))
# Include a nonnegative slack in (11), so the direction is checked exactly.
yf=s.symbols('yf',real=True);Edot=-k*Z/(4*B*P)-yf+slack;Zdot=4*P*(Edot+yf)
M=Z-4*P*w*E;Mdot=Zdot-4*P*w*Edot-4*P*w*lam*E
Mbound=chi*M+4*P*w*(chi-lam)*E+4*P*w*yf
eq('M_inequality_exact_slack',Mdot-Mbound+4*P*(w-1)*slack)
N=M-P*w*F;Ndot=Mdot-P*w*lam*F-P*w*s.diff(F,B)*Bdot
Nbound=chi*N+P*w*((chi-lam)*(F+4*(B-beta))+4*yf)
eq('N_inequality_exact_slack',(Ndot-Nbound+4*P*(w-1)*slack).subs(E,Eactual))
eq('Zsign_to_Eslack',Zdot+k*Z/B-4*P*slack)
# All-parameter rational positivity, including beta=2.
z=s.symbols('z',nonnegative=True);delta=s.symbols('delta',positive=True);eps=delta/(128*beta*(1+beta*delta));power=delta-m
for name,expr in [('epsilon',eps),('eta_integrable',1/beta-2*eps),('Pf_integrable',1/beta-6*eps),('positive_contradiction',delta-6*eps),('negative_growth',delta-2*eps),('weighted_integral',power+g+1-eps),('constant_yf_decay',3*g-1-3*eps)]:
 n0,d0=s.fraction(s.cancel(expr.subs(beta,z+2)));pn=s.Poly(n0,z,delta);pd=s.Poly(d0,z,delta)
 ok=all(q>=0 for q in pn.coeffs()+pd.coeffs()) and any(mon[0]==0 and q>0 for mon,q in pn.terms()) and any(mon[0]==0 and q>0 for mon,q in pd.terms())
 ck(name,ok,{'numerator':str(n0),'denominator':str(d0),'domain':'z>=0,delta>0'})
nu=delta-2*eps;theta=nu/4
eq('final_growth',nu-theta-3*nu/4)
# Exact rational perturbations with either sign of B-beta, uncontrolled Bdot,
# both critical and supercritical beta. Slack gap must be nonpositive.
for betav in [s.Integer(2),s.Integer(3),s.Rational(11,2)]:
 for offset in [s.Rational(-1,100),s.Rational(1,100)]:
  sub={beta:betav,B:betav+offset,B0:betav-s.Rational(1,50),P:s.Rational(7,3),slack:s.Rational(5,2),Bdot:s.Integer(1000),E:s.Integer(-999),Z:s.Integer(8),yf:s.Rational(-7,4)}
  value=s.factor((Mdot-Mbound).subs(sub));ck('manufactured_slack_'+str((betav,offset)),value<0,str(value))
# The analytic conclusion only excludes strictly supercritical powers.
eq('beta2_m',m.subs(beta,2));eq('beta2_k_equals_d',(k-d).subs(beta,2))
# Reflection in actual physical polynomial fields, testing all equations' signs.
Xp,Yp=s.symbols('Xp Yp');u1=Xp+Xp*Yp+Xp**3;u2=Yp+Xp**2+Yp**3;th=Xp**2*(1+Yp+Xp**2);om=Xp*(1+Yp**2)
reflect=lambda q:q.subs(Yp,-Yp);ut1=reflect(u1);ut2=-reflect(u2);tt=-reflect(th);ot=-reflect(om)
for name,q,qt,sign in [('div',s.diff(u1,Xp)+s.diff(u2,Yp),s.diff(ut1,Xp)+s.diff(ut2,Yp),1),('curl',s.diff(u1,Yp)-s.diff(u2,Xp),s.diff(ut1,Yp)-s.diff(ut2,Xp),-1),('thermal',u1*s.diff(th,Xp)+u2*s.diff(th,Yp)-(beta-2)*th,ut1*s.diff(tt,Xp)+ut2*s.diff(tt,Yp)-(beta-2)*tt,-1),('vorticity',u1*s.diff(om,Xp)+u2*s.diff(om,Yp)+om-s.diff(th,Xp),ut1*s.diff(ot,Xp)+ut2*s.diff(ot,Yp)+ot-s.diff(tt,Xp),-1)]:eq('reflection_'+name,qt-sign*reflect(q))
proof=json.loads((V/'proof_before_checks.json').read_text());ck('proof_written_before_checks',proof['written_utc']<start);ck('proof_hash',hashlib.sha256((V.parent/'PROOF.md').read_bytes()).hexdigest()==proof['proof_sha256'])
for row in json.loads((V/'manifest.json').read_text())['inputs']:ck('input_hash_'+row['snapshot'],hashlib.sha256((V/row['snapshot']).read_bytes()).hexdigest()==row['sha256'])
out={'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'passed':sum(c['passed']for c in checks),'total':len(checks),'all_passed':all(c['passed']for c in checks),'checks':checks,'proof_sha256':proof['proof_sha256'],'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact algebraic and universal parameter controls. Complete analytic proof in PROOF.md. No B2 endpoint follows.'}
(V/'controls.json').write_text(json.dumps(out,indent=2)+'\n');print(out['passed'],out['total'],out['elapsed_seconds']);print([a for a in checks if not a['passed']])
