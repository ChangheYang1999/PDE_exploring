"""P266 exact controls for logarithmic critical-axis manufacture.
Independently entered physical coefficient equations, differential algebra,
asymptotic exponents, and the explicit full-plane failure. No teammate code.
"""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s,json,hashlib,time
V=Path('research/266_logarithmic_critical_axis_data/verification');start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();checks=[]
def eq(name,e):
 q=s.factor(s.trigsimp(s.cancel(s.expand(e))));checks.append({'name':name,'passed':q==0,'difference':str(q)})
def ck(name,p,detail=None):checks.append({'name':name,'passed':bool(p),'detail':detail})
beta=s.symbols('beta',positive=True);A=s.symbols('A',nonzero=True);a=s.symbols('a',positive=True);d=(3*beta+2)/2;k=(beta+6)/2;m=1-2/beta;g=s.Rational(1,2)+1/beta;ar=beta/(2*d);p=2*a*a;ell=a*a*(2-m/2)
e=s.symbols('e');eq('reciprocal_cubic_remainder',1/(1+e)-(1-e+e*e-e**3/(1+e)))
t=s.symbols('t',positive=True);ep=a*s.sin(t)/s.sqrt(t);E=beta*(ep+s.diff(ep,t));Ed=s.diff(E,t)
Epred=beta*a*((s.sin(t)+s.cos(t))/s.sqrt(t)-s.sin(t)/(2*t**s.Rational(3,2)))
Edpred=beta*a*((s.cos(t)-s.sin(t))/s.sqrt(t)-(s.sin(t)/2+s.cos(t))/t**s.Rational(3,2)+3*s.sin(t)/(4*t**s.Rational(5,2)))
eq('E_exact',E-Epred);eq('Edot_exact',Ed-Edpred)
rem=beta**2*a**2*(-(s.sin(t)+s.cos(t))*s.sin(t)/t**2+s.sin(t)**2/(4*t**3))
eq('square_exact_remainder',E**2-beta**2*a**2*(1+s.sin(2*t))/t-rem)
eq('sine_square_mean',ep**2-a*a*(1-s.cos(2*t))/(2*t))
for name,expr in [('d_over_beta',d/beta-g-1),('3d_k',3*d-k-4*beta),('k_d',k-d+beta-2),('r_integral_y_power',d/beta*(ar-1)+1+1/beta),('r_y_power',-ar*d/beta+s.Rational(1,2)),('r_log_power',-ar*d*a*a/(2*beta)+a*a/4),('eta_y_power',-s.Rational(1,2)-g+1+1/beta),('eta_log_power',-a*a/4-d*a*a/(2*beta)+a*a*(1+1/(2*beta))),('P_R_exponent',3-k/d-4*beta/d),('P_y_cancellation',(d/beta)*(3-k/d)-4),('P_log_power',d*a*a/(2*beta)*(3-k/d)-p),('H_square_coefficient',16*beta*a*a/p-8*beta),('I_y_power',(k/d-1)*d/beta+m),('I_log_power',(k/d-1)*d*a*a/(2*beta)+p-ell),('ell_simpler',ell-d*a*a/beta),('coefficient_Cr_power',4*beta/d+(k-d)/d-2)]:eq(name,expr)
Cr,Ch=s.symbols('Cr Ch',positive=True);P0=d**3*Cr**(4*beta/d)/(Ch*beta**4)
Lraw=-8*beta*k*Ch*P0*Cr**((k-d)/d)/(A*d)
# Check coefficient separately from its already checked common Cr exponent.
eq('L_coefficient',-8*beta*k*Ch*d**3/(Ch*beta**4*A*d)+8*k*d*d/(A*beta**3))
eq('beta2_L',(-8*k*d*d/beta**3).subs(beta,2)+64);eq('beta2_ell',ell.subs(beta,2)-p);eq('beta2_m',m.subs(beta,2))
z=s.symbols('z',nonnegative=True)
for name,expr in [('ell_positive',ell),('r_integrability_margin',1/beta),('rho_constant_forcing_integrable',3*g-1),('P_positive_log_power',p),('ell_choice_denominator',2-m/2)]:
 num,den=s.fraction(s.cancel(expr.subs(beta,z+2)));np=s.Poly(num,z,a);dp=s.Poly(den,z,a);ck(name,all(v>=0 for v in np.coeffs()+dp.coeffs()) and any(v>0 for v in np.coeffs()) and any(v>0 for v in dp.coeffs()),{'numerator':str(num),'denominator':str(den),'domain':'z>=0,a>0'})
# Exact differential algebra for the energy identity, with independent symbols.
b,rho,bp,bpp,h,R,G,I,P,H,ef=s.symbols('b rho bp bpp h R G I P H ef');rhop=(d-bp)*rho/b;hp=k*h/b;Pexpr=rho**3/(b*h)
Pprime=s.diff(Pexpr,rho)*rhop+s.diff(Pexpr,b)*bp+s.diff(Pexpr,h)*hp
eq('P_energy_derivative',Pprime+4*Pexpr*(bp-beta)/b)
Hp=A*rho*I/h-k*H/b;vexpr=s.symbols('c2')/rho**3+A*(d*R*I-k*G)/(8*rho**3)
eq('v_from_Hprime',(2*vexpr-2*s.symbols('c2')/rho**3-Hp/(4*Pexpr)).subs({H:A*G/h,R:b*rho/d}))
Ev=s.symbols('Ev');Pp=-4*P*Ev/b;Hpp=-4*P*(bpp+ef)
eq('Q_square_identity',Hpp+4*Pp*Ev+4*P*bpp+16*P*Ev**2/b+4*P*ef)
B,y=s.symbols('B y',nonzero=True);Edot,yf=s.symbols('Edot yf');eq('log_time_energy',(-16*P*Ev**2/b-4*P*ef)*y-(-16*P*Ev**2/(b/y)-4*P*y*ef))
Hdot=s.symbols('Hdot');Gprime=hp*H/A+h*Hdot/(A*y)
eq('I_extraction',Gprime/rho-h/(A*b*rho)*((b/y)*Hdot+k*H))
# The last prefactor identity is checked after rho=dR/b.
eq('I_leading_prefactor',(Pexpr*h/(d*R)-d*d*R*R/b**4).subs(rho,d*R/b))
# Formal trigonometric differential algebra also checks E for exact rational phases.
S,C,Z=s.symbols('S C Z');dt=lambda f:s.diff(f,S)*C-s.diff(f,C)*S-s.diff(f,Z)*Z**3/2
eps=a*Z*S;Er=beta*(eps+dt(eps));Edr=dt(Er)
for be in [s.Integer(2),s.Rational(5,2),s.Integer(3),s.Integer(10)]:
 for sign in [-1,1]:
  vals={beta:be,a:s.Rational(3,2),S:sign*s.Rational(3,5),C:s.Rational(4,5),Z:s.Rational(1,20)}
  expected=be*s.Rational(3,2)*((vals[S]+vals[C])*vals[Z]-vals[S]*vals[Z]**3/2)
  eq('rational_E_'+str((be,sign)),Er.subs(vals)-expected)
  ck('literal_A_L_negative_'+str((be,sign)),(-8*k*d*d/beta**3).subs(beta,be)<0)
# Direct physical coefficient and exact off-axis failure.
y=s.symbols('y',real=True);x=s.symbols('x',real=True);bf=s.Function('b')(y);rf=s.Function('rho')(y);vf=s.Function('v')(y);If=s.Function('I')(y)
Tf=A/rf**2;Q4=Tf**2*If;W1=(2*beta-s.diff(bf,y))*x-s.diff(vf,y)*x**3/3;W2=bf+vf*x*x;Th=Tf*x*x/2+Q4*x**4/24;Om=s.diff(W1,y)-s.diff(W2,x)
eq('physical_divergence',s.diff(W1,x)+s.diff(W2,y)-2*beta)
eq('physical_curl',Om-((-s.diff(bf,y,2)-2*vf)*x-s.diff(vf,y,2)*x**3/3))
RT=s.expand(W1*s.diff(Th,x)+W2*s.diff(Th,y)-(beta-2)*Th)
eq('physical_T2',RT.coeff(x,2).subs(s.diff(rf,y),(d-s.diff(bf,y))*rf/bf))
eq('physical_T4_form',24*RT.coeff(x,4)-(bf*s.diff(Q4,y)+(7*beta+2-4*s.diff(bf,y))*Q4-8*s.diff(vf,y)*Tf+12*vf*s.diff(Tf,y)))
reduced=bf*s.diff(If,y)+(beta-2)*If-8*s.diff(rf**3*vf,y)/(A*rf)
eq('physical_T4_reduction',(24*RT.coeff(x,4)/Tf**2-reduced).subs(s.diff(rf,y),(d-s.diff(bf,y))*rf/bf))
eq('origin_curl_v',-2*(-A/beta)-2*A/beta);eq('off_axis_quadratic',W2.subs({bf:0,vf:-A/beta})+A*x*x/beta)
ck('off_axis_growth_nonzero',s.simplify(-A/beta)!=0)
proof=json.loads((V/'proof_before_checks.json').read_text());ck('proof_precedes_controls',proof['written_utc']<start);ck('proof_hash',proof['proof_sha256']==hashlib.sha256((V.parent/'PROOF.md').read_bytes()).hexdigest())
result={'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'passed':sum(r['passed']for r in checks),'total':len(checks),'all_passed':all(r['passed']for r in checks),'checks':checks,'proof_sha256':proof['proof_sha256'],'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact algebraic controls for the complete analytic low-order construction, not a B2 profile or a numerical existence argument.'};(V/'controls.json').write_text(json.dumps(result,indent=2)+'\n');print(result['passed'],result['total'],result['elapsed_seconds']);print('FAILED',[r for r in checks if not r['passed']])
