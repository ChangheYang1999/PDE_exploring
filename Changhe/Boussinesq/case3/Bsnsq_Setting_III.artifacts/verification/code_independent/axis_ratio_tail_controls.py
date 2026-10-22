"""Own exact controls for P258. No NUM or lead implementation imported."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s,json,hashlib,time
V=Path('research/258_axis_ratio_tail_restrictions/verification');start=datetime.now(timezone.utc).isoformat();tic=time.monotonic();checks=[]
def eq(n,e):
 z=s.factor(s.cancel(s.expand(e)));checks.append({'name':n,'passed':z==0,'difference':str(z)})
def pos(n,e,variables):
 num,den=s.fraction(s.factor(s.cancel(e)));pn=s.Poly(num,*variables);pd=s.Poly(den,*variables)
 a=pn.coeffs();b=pd.coeffs();good=all(t>=0 for t in a+b)and any(t>0 for t in a)and any(t>0 for t in b)
 checks.append({'name':n,'passed':bool(good),'positive_variables':[str(v)for v in variables],'numerator':str(pn.as_expr()),'denominator':str(pd.as_expr())})
y=s.symbols('y',positive=True);beta=s.symbols('beta',positive=True);A,L,C=s.symbols('A L C',real=True);q=s.symbols('q',real=True);d=(3*beta+2)/2;h=(beta+6)/2;gamma=s.Rational(1,2)+1/beta;m=1-2/beta
z,k=s.symbols('z k',positive=True);eps=k/(16*(1+beta*k));qs=-m+k
for name,e in [('epsilon_positive',eps),('integrable_mu_source',1/beta-2*eps),('p_below_one',k-2*eps),('eta_lower_order',qs+1-1/beta-4*eps),('weighted_integral_diverges',qs+gamma+1-eps),('coefficient_positive',(qs+m)/(gamma+1+qs))]:pos(name,e.subs(beta,2+z),(z,k))
eq('weighted_coefficient',d-h*(gamma+1)/(gamma+1+q)-d*(q+m)/(gamma+1+q))
eq('critical_coefficient_cancels',(d-h*(gamma+1)/(gamma+1+q)).subs(q,-m))
eq('h_relation',h/beta-(gamma+1-m))
eq('rho_exponent',d/beta-1-gamma)
# Integrating factor equation with fully independent symbolic functions.
b=s.Function('b')(y);rho=s.Function('rho')(y);rr=s.Function('r')(y);mu=s.Function('mu')(y)
left=s.diff(mu*rr,y).subs(s.diff(mu,y),beta*mu/(2*b));eq('mu_integrating_factor',left-mu/b*(b*s.diff(rr,y)+beta*rr/2))
# Exact half-axis power solutions, not profiles with the required smooth center.
rhop=y**gamma;Rp=y**(gamma+1)/(gamma+1);bp=beta*y;rp=C*y**(-s.Rational(1,2))-A*y**(-gamma);etap=rp/rhop
# powsimp is legitimate because y>0.
def peq(n,e):eq(n,s.powsimp(s.expand_power_exp(e),force=False))
peq('pure_power_axis_rho',s.diff(rhop*bp,y)-d*rhop)
peq('pure_power_first_vorticity_r',bp*s.diff(rp,y)+beta*rp/2-A/rhop)
peq('pure_power_eta_expansion',etap-C*y**(-1-1/beta)+A*y**(-1-2/beta))
H=y**(gamma+q+1)/(gamma+q+1)
peq('pure_power_weighted_integral',s.diff(H,y)-rhop*y**q)
peq('pure_power_weight_ratio',H-Rp*y**q*(gamma+1)/(gamma+1+q))
vp=A*L/8*(d*Rp*y**q-h*H)/rhop**3
peq('pure_power_v_coefficient',vp-A*L*d/8*(q+m)/(gamma+1+q)*Rp*y**q/rhop**3)
peq('pure_power_critical_v_zero',vp.subs(q,-m))
peq('pure_power_v_exponent',Rp*y**q/rhop**3-y**(q-2/beta)/(gamma+1))
# Primitive exactly covers p<1, including negative p.
p=s.symbols('p',real=True);Y=s.symbols('Y',positive=True)
F=y**(2-p)/((1-p)*(2-p))-y*Y**(1-p)/(1-p)+Y**(2-p)/(2-p)
peq('curvature_double_primitive',s.diff(F,y,2)-y**(-p));eq('curvature_initial_value',F.subs(y,Y));eq('curvature_initial_slope',s.diff(F,y).subs(y,Y))
for pv in[-3,-1,0,s.Rational(1,2),s.Rational(9,10)]:peq('curvature_p_'+str(pv),s.diff(F.subs(p,pv),y,2)-y**(-pv))
# Monotone comparison: early contribution C0 may have either sign.
R=s.symbols('R',positive=True);RY=s.symbols('RY',positive=True);K=s.symbols('K',positive=True);C0=s.symbols('C0',real=True)
upper=C0+K*(R-RY)
eq('monotone_comparison_remainder',d*R*K-h*upper-((beta-2)*R*K-h*C0+h*K*RY))
pos('monotone_gap_positive',(d-h).subs(beta,2+z),(z,))
# Exact positive/negative signed asymptotic coefficients on both sides of threshold.
for bv in[s.Rational(5,2),s.Integer(3),s.Integer(7)]:
 for kv in[s.Rational(1,7),s.Rational(3,2)]:
  ev=eps.subs({beta:bv,k:kv});qv=qs.subs({beta:bv,k:kv});pv=2/bv+2*ev-qv
  checks.append({'name':f'exponent_instance_beta{bv}_k{kv}','passed':bool(pv<1 and 2*ev<1/bv and 4*ev<qv+1-1/bv),'epsilon':str(ev),'q':str(qv),'p':str(pv)})
  for av,lv in[(2,3),(-2,3),(2,-3),(-2,-3)]:
   coeff=(A*L*d*(q+m)/(8*(gamma+1+q))).subs({beta:bv,A:av,L:lv,q:qv});checks.append({'name':f'sign_beta{bv}_k{kv}_A{av}_L{lv}','passed':bool(coeff*av*lv>0),'coefficient':str(coeff)})
out={'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tic,'passed':sum(t['passed']for t in checks),'total':len(checks),'checks':checks,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((V.parent/'PROOF.md').read_bytes()).hexdigest(),'scope':'Exact algebra and half-axis controls only. Analytic comparison proof is in PROOF.md. Pure powers do not supply a global B2 profile or settle critical attainability.'}
(V/'controls.json').write_text(json.dumps(out,indent=2)+'\n');print(out['passed'],out['total'],out['elapsed_seconds']);print([t for t in checks if not t['passed']])
