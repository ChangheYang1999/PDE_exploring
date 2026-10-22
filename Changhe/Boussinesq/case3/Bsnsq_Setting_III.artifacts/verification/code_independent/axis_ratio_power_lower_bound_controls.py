"""P261: exact physical, energy and all-parameter threshold controls.
Independent code; no lead, NUM or referee imports or execution.
"""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s,json,hashlib,time
V=Path('research/261_axis_ratio_power_lower_bound/verification');start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();checks=[]
def eq(n,e):
 q=s.factor(s.cancel(s.expand(e)));checks.append({'name':n,'passed':q==0,'difference':str(q)})
def ck(n,b,detail=None):checks.append({'name':n,'passed':bool(b),'detail':detail})
y=s.symbols('y',positive=True);x=s.symbols('x',real=True);beta,delta=s.symbols('beta delta',positive=True);z=s.symbols('z',nonnegative=True);A=s.symbols('A',nonzero=True);c2=s.symbols('c2',real=True)
d=(3*beta+2)/2;h=(beta+6)/2;gamma=s.Rational(1,2)+1/beta;m=1-2/beta;k=1+h/d;eps=delta/(128*beta*(1+beta*delta));power=delta-m
# Positivity certificates apply on beta=2+z, z>=0, delta>0, including z=0.
def positive(name,e):
 n0,d0=s.fraction(s.cancel(e.subs(beta,z+2)));pn=s.Poly(n0,z,delta);pd=s.Poly(d0,z,delta)
 good=all(c>=0 for c in pn.coeffs()+pd.coeffs()) and any(mon[0]==0 and c>0 for mon,c in pn.terms()) and any(mon[0]==0 and c>0 for mon,c in pd.terms())
 ck(name,good,{'domain':'z=beta-2>=0, delta>0','numerator':str(pn.as_expr()),'denominator':str(pd.as_expr())})
for name,expr in [
 ('eps_positive',eps),('eps_lt_delta_over256',delta/256-eps),('eps_lt_inverse128beta2',1/(128*beta**2)-eps),
 ('mu_integrable',1/beta-2*eps),('M_eta_integrable',1/beta-(6+k)*eps),('N_integrable',h/beta-(1+k)*eps),
 ('weighted_source_growth',delta-(1-h/d)*eps),('curvature_growth',delta-2*eps),
 ('lead_exponent_gap',delta-6*eps),('lead_integrable',1/beta-6*eps),('pointwise_integral_grows',power+gamma+1-eps),
 ('pointwise_weight_constant_positive',1+power/(gamma+1))]:positive(name,expr)
for name,e in [('3d_h',3*d-h-4*beta),('rho_growth',d/beta-1-gamma),('weighted_growth',(gamma+1)*(1-h/d)-m),('M_power',4*gamma-k*(gamma+1)),('N_power',gamma-k*(gamma+1)+1+h/beta),('curvature_power',power+2-2*gamma-delta),('lead_P_power',3*gamma-1-h/beta),('lead_Phi_power',power+gamma+1-h/beta-delta),('comparison_L',1+power/(gamma+1)-(gamma+1+power)/(gamma+1))]:eq(name,e)
eq('k_interval_identity',2-k-2*(beta-2)/(3*beta+2))
rho=s.Function('rho')(y);R=s.Function('R')(y);b=s.Function('b')(y);I=s.Function('I')(y);G=s.Function('G')(y);v=s.Function('v')(y);eta=s.Function('eta')(y)
T=A/rho**2;Q=A**2*I/rho**4
W1=(2*beta-s.diff(b,y))*x-s.diff(v,y)*x**3/3;W2=b+v*x**2;Theta=T*x**2/2+Q*x**4/24
curl=s.diff(W1,y)-s.diff(W2,x);eq('negative_curl_linear',s.expand(curl).coeff(x,1)+s.diff(b,y,2)+2*v)
thermal=s.expand(W1*s.diff(Theta,x)+W2*s.diff(Theta,y)-(beta-2)*Theta)
bp=d-d*R*s.diff(rho,y)/rho**2
expr=s.simplify(24*thermal.coeff(x,4).subs(s.diff(b,y),bp).subs(b,d*R/rho))
vp=s.solve(expr,s.diff(v,y))[0]
eq('physical_quartic_integrated_derivative',rho**3*vp+3*rho**2*s.diff(rho,y)*v-A/8*((d-h)*rho*I+d*R*s.diff(I,y)))
Omega=eta*x;vort=s.expand(W1*s.diff(Omega,x)+W2*s.diff(Omega,y)+Omega-s.diff(Theta,x));eq('physical_vorticity_linear',vort.coeff(x,1)-(b*s.diff(eta,y)+(2*beta+1-s.diff(b,y))*eta-T))
eq('rho_r_linear_coefficient',2*beta+1-s.diff(b,y)-(d-s.diff(b,y))-beta/2)
M=s.Function('M')(y);N=s.Function('N')(y);E=s.diff(b,y)-beta
logM=(4*(d-s.diff(b,y))-k*d)/b;eq('M_logderivative',logM+4*E/b)
# Scaled G derivative and exact energy, retaining arbitrary b''.
JG=s.diff(G*R**(-h/d),y).subs({s.diff(G,y):rho*I,s.diff(R,y):rho})
vval=(c2+A/8*(d*R*I-h*G))/rho**3
eq('scaled_G_identity',s.powsimp(JG-8/(A*d)*rho*R**(-k)*(rho**3*vval-c2),force=False))
prod=s.diff(M*E,y).subs(s.diff(M,y),-4*M*E/b)
eq('energy_identity',(-M*s.diff(b,y,2)-M*eta-2*c2*N)+prod+4*M*E**2/b+M*eta+2*c2*N)
eq('division_power',s.powsimp(y**power*R**(1-h/d)/(rho**4*R**(-k))-y**power*R**2/rho**4,force=False))
eq('pointwise_weight_derivative',(s.diff(R*y**power,y).subs(s.diff(R,y),rho))/(rho*y**power)-(1+power*R/(y*rho)))
# Exact normalization between two genuinely different presentations of the energy.
C=s.symbols('C',positive=True);Mv=rho**4*R**(-k);P=rho**3/((d*R/rho)*C*R**(h/d))
eq('lead_P_equals_M_over_dC',s.powsimp(P-Mv/(d*C),force=False))
Qlead=A*G/(C*R**(h/d))+4*P*E;Sown=A*d*G*R**(-h/d)/4+Mv*E
eq('lead_Q_equals_scaled_S',s.powsimp(Qlead-4*Sown/(d*C),force=False))
# Boundary beta=2 is not omitted by the positivity certificate.
for name,e,expected in [('m',m,0),('h_over_d',h/d,1),('k',k,2),('gamma',gamma,1),('Npower',-1-h/beta,-3)]:eq('beta2_'+name,e.subs(beta,2)-expected)
eq('beta2_constant_I_invisible',(d-h).subs(beta,2))
# Signed polynomial reflection, independent of any asymptotic approximation.
u=s.symbols('u',real=True);rh=1+u**2;ip=1-3*u+2*u**4;RR=s.integrate(rh,(u,0,y));GG=s.integrate(rh*ip,(u,0,y));rn=s.integrate(rh.subs(u,-u),(u,0,y));gn=s.integrate(-rh.subs(u,-u)*ip.subs(u,-u),(u,0,y))
eq('negative_end_R',rn+RR.subs(y,-y));eq('negative_end_G',gn-GG.subs(y,-y));eq('negative_end_mean',-A*gn/rn-A*GG.subs(y,-y)/RR.subs(y,-y));eq('negative_end_pointwise',(-A)*(-ip.subs(u,-u))-A*ip.subs(u,-u))
# Manufacture product identity including beta2 and b' very different from beta.
for bv in [s.Integer(2),s.Rational(5,2),s.Integer(3),s.Integer(12)]:
 for q in [s.Rational(1,2),s.Integer(1),s.Integer(2)]:
  bm=q*y;mm=y**(4*(bv-q)/q);ee=q-bv
  eq(f'product_manufacture_beta{bv}_slope{q}',s.diff(mm*ee,y)+4*mm*ee**2/bm)
proof=json.loads((V/'proof_before_checks.json').read_text());ck('proof_precedes_checks',proof['written_utc']<start);ck('proof_hash',hashlib.sha256((V.parent/'PROOF.md').read_bytes()).hexdigest()==proof['sha256'])
for it in json.loads((V/'freeze.json').read_text())['inputs']:ck('input_hash_'+Path(it['snapshot']).name,hashlib.sha256(Path(it['snapshot']).read_bytes()).hexdigest()==it['sha256'])
out={'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'passed':sum(c['passed']for c in checks),'total':len(checks),'all_passed':all(c['passed']for c in checks),'checks':checks,'proof_sha256':proof['sha256'],'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact algebra and parameter-inequality controls; complete analysis in PROOF.md. No global profile manufacture or existence claim.'}
(V/'controls.json').write_text(json.dumps(out,indent=2)+'\n');print(out['passed'],out['total'],out['elapsed_seconds']);print('FAILURES',[c for c in checks if not c['passed']])
