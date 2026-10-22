"""P268 independent exact controls; no teammate code imports or execution."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s,json,hashlib,time
V=Path('research/268_critical_axis_both_signs/verification');start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();checks=[]
def eq(n,e):
 q=s.factor(s.powsimp(s.simplify(s.expand(e)),force=True));checks.append({'name':n,'passed':q==0,'difference':str(q)})
def ck(n,p,detail=None):checks.append({'name':n,'passed':bool(p),'detail':detail})
beta,A,C,D,z,lam=s.symbols('beta A C D z lam',positive=True);d=(3*beta+2)/2;k=(beta+6)/2;g=s.Rational(1,2)+1/beta;m=1-2/beta;ar=beta/(2*d);c2=-A/beta
for n,e in [('density_power',d/beta-1-g),('vorticity_damping',2*beta+1-d-beta/2),('quartic_damping',d-k-beta+2),('thermal_2',2*d-3*beta-2),('power1_eigenvalue',beta*(s.Rational(1,2)+2/beta)-k+1),('power2_eigenvalue',beta*g-k+2),('I_power',k/beta-1-g+m),('first_error_power',s.Rational(1,2)+2/beta-1-g+1-1/beta),('shift_error_margin',(-1+1/beta)-(-m-1)-(1-1/beta)),('Ge_integrability',(s.Rational(1,2)+2/beta)-1-k/beta+1+1/beta)]:eq(n,e)
y0=s.symbols('y0',positive=True);b=beta*z;rho=C*z**g;R=beta*C*z**(g+1)/d;r=D*z**(-s.Rational(1,2))-A/C*z**(-g);eta=r/rho;v=-eta/2;T=A/rho**2;K=s.symbols('K');p1=s.Rational(1,2)+2/beta
G=K*z**(k/beta)+4*D*C*C/A*z**p1-2*C*z**g-8/(beta*k)
I=k*K/(beta*C)*z**(-m)+4*D*C/A*p1*z**(-1+1/beta)-2*g/z
for n,e in [('R_prime',s.diff(R,z)-rho),('rho_b',rho*b-d*R),('r_transport',b*s.diff(r,z)+beta*r/2-A/rho),('eta_transport',b*s.diff(eta,z)+(beta+1)*eta-T),('thermal2_tail',b*s.diff(T,z)+(beta+2)*T),('G_ode',b*s.diff(G,z)-k*G-8/A*(rho**3*v-c2)),('I_derivative',s.diff(G,z)/rho-I),('quartic_integral',rho**3*v-c2-A/8*(d*R*I-k*G)),('quartic_differential',b*s.diff(I,z)+(beta-2)*I-8*s.diff(rho**3*v,z)/(A*rho))]:eq(n,e)
# Re-derive the positive forcing identity from independent first-order jets.
b0,bp,rh,rr=s.symbols('b0 bp rh rr',nonzero=True);rhp=(d-bp)*rh/b0;rrp=(1/rh-beta*rr/2)/b0;u=rh**2*rr-2/beta;up=2*rh*rhp*rr+rh**2*rrp
rhs=(2*d-beta/2-2*bp)*u+4*(d-bp)/beta+rh-1
eq('u_ode',b0*up-rhs);eq('Ge_force',(-4*rh**2*rr+8/beta)+4*u)
h,Gb,Ge,Gbp,Gep,bpp=s.symbols('h Gb Ge Gbp Gep bpp');hp=k*h/b0
eq('Gb_integrating_factor',b0*h*(Gbp/h-Gb*hp/h**2)-(b0*Gbp-k*Gb))
eq('G_split_force',(-4*rh**3*bpp)/A+(-4*rh**2*rr+8/beta)-8/A*(rh**3*(-bpp-A*rr/rh)/2+A/beta))
# Dilation checked directly on arbitrary jets. q is the base coordinate, not y.
y=s.symbols('y',real=True);q=s.symbols('q',real=True);bf=s.Function('b')(q);rf=s.Function('rho')(q);Rf=s.Function('R')(q);r1=s.Function('r1')(q);e1=r1/rf;gb=s.Function('Gb')(q);ge=s.Function('Ge')(q)
bl=lam*bf;rl=rf;Rll=lam*Rf;rll=A*r1;vl=-(s.diff(bf,q,2)/lam+A*e1)/2;Gl=gb/(A*lam)+ge;Il=s.diff(Gl,q)/(lam*rf)
dy=lambda f:s.diff(f,q)/lam
eq('scaled_density_equation',bl*dy(rl)-(d-dy(bl))*rl-(bf*s.diff(rf,q)-(d-s.diff(bf,q))*rf))
eq('scaled_R_equation',dy(Rll)-s.diff(Rf,q))
eq('scaled_r_equation',bl*dy(rll)+beta*rll/2-A/rf-A*(bf*s.diff(r1,q)+beta*r1/2-1/rf))
eq('scaled_curl',-dy(dy(bl))-2*vl-A*e1)
eq('scaled_G_equation',bl*dy(Gl)-k*Gl-((bf*s.diff(gb,q)-k*gb)/(A*lam)+bf*s.diff(ge,q)-k*ge))
eq('scaled_force',8/A*(rf**3*vl+A/beta)-(-4*rf**3*s.diff(bf,q,2)/(A*lam)-4*rf**2*r1+8/beta))
eq('scaled_I',Il-s.diff(gb,q)/(rf*A*lam**2)-s.diff(ge,q)/(rf*lam))
eq('scaled_limit_Ib_exponent',m-2-(m-1-1));eq('scaled_limit_Ie_exponent',m-1-(m-1))
eq('beta2_homogeneous',d.subs(beta,2)-k.subs(beta,2));eq('beta2_m',m.subs(beta,2))
# Positive thresholds, exact sample arithmetic as controls for the choice, not proofs of signs.
Lb,Le,Ac=s.symbols('Lb Le Ac',positive=True);threshold=Lb/(Ac*Le)
for factor in [s.Rational(1,4),s.Rational(1,2),s.Integer(2),s.Integer(4)]:
 bracket=Lb/(Ac*factor*threshold)-Le
 eq('threshold_bracket_'+str(factor),bracket-Le*(1/factor-1));ck('threshold_sign_'+str(factor),s.sign(bracket)==(1 if factor<1 else -1))
# Physical coefficients independently differentiated in Cartesian coordinates.
x=s.symbols('x',real=True);bf=s.Function('b')(y);rf=s.Function('rho')(y);vf=s.Function('v')(y);If=s.Function('I')(y);Tf=A/rf**2;Q4=Tf**2*If
W1=(2*beta-s.diff(bf,y))*x-s.diff(vf,y)*x**3/3;W2=bf+vf*x*x;Th=Tf*x*x/2+Q4*x**4/24;Om=s.diff(W1,y)-s.diff(W2,x)
eq('divergence',s.diff(W1,x)+s.diff(W2,y)-2*beta)
eq('curl',Om-((-s.diff(bf,y,2)-2*vf)*x-s.diff(vf,y,2)*x**3/3))
RT=s.expand(W1*s.diff(Th,x)+W2*s.diff(Th,y)-(beta-2)*Th)
eq('thermal2_physical',RT.coeff(x,2).subs(s.diff(rf,y),(d-s.diff(bf,y))*rf/bf))
eq('thermal4_physical_form',24*RT.coeff(x,4)-(bf*s.diff(Q4,y)+(7*beta+2-4*s.diff(bf,y))*Q4-8*s.diff(vf,y)*Tf+12*vf*s.diff(Tf,y)))
reduced=bf*s.diff(If,y)+(beta-2)*If-8*s.diff(rf**3*vf,y)/(A*rf)
eq('thermal4_physical_reduction',(24*RT.coeff(x,4)/Tf**2-reduced).subs(s.diff(rf,y),(d-s.diff(bf,y))*rf/bf))
eq('center_a0_b0',2*A/beta-4*(A/2)/beta)
eq('non_sublinear_vertical',W2.subs({bf:0,vf:-A/beta})+A*x*x/beta)
# Strict scalar margins used in the analytic improper integral and shift arguments.
z0=s.symbols('z0',nonnegative=True)
for n,e in [('d_minus_beta',d-beta),('alpha_positive',ar),('tail_gap1',k/beta-p1),('tail_gap2',k/beta-g),('shift_margin',1-1/beta),('integral_margin',1/beta)]:
 num,den=s.fraction(s.cancel(e.subs(beta,z0+2)));coeff=s.Poly(num,z0).all_coeffs()+s.Poly(den,z0).all_coeffs();ck(n,all(c>=0 for c in coeff)and num.subs(z0,0)>0 and den.subs(z0,0)>0,str(e))
pb=json.loads((V/'proof_before_checks.json').read_text());ck('proof_precedes_checks',pb['written_utc']<start);ck('proof_hash',pb['proof_sha256']==hashlib.sha256((V.parent/'PROOF.md').read_bytes()).hexdigest())
out={'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'passed':sum(c['passed']for c in checks),'total':len(checks),'all_passed':all(c['passed']for c in checks),'checks':checks,'proof_sha256':pb['proof_sha256'],'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact algebra supplement to the complete low-order concave-transport proof. No full-profile or certified numerical existence claim.'};(V/'controls.json').write_text(json.dumps(out,indent=2)+'\n');print(out['passed'],out['total'],out['elapsed_seconds']);print('FAILED',[r for r in checks if not r['passed']])
