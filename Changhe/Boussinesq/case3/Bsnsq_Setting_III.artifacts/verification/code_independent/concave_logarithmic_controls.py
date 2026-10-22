"""P270 exact algebra and asymptotic-exponent controls, independent of team code."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s,json,hashlib,time
V=Path('research/270_concave_logarithmic_axis_tails/verification');start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();checks=[]
def eq(n,e):
 z=s.factor(s.powsimp(s.simplify(s.expand(e)),force=True));checks.append({'name':n,'passed':z==0,'difference':str(z)})
def ck(n,p,detail=None):checks.append({'name':n,'passed':bool(p),'detail':detail})
beta,A,a,C,Cr,Ch,y,t,c=s.symbols('beta A a C Cr Ch y t c',positive=True);d=(3*beta+2)/2;k=(beta+6)/2;g=s.Rational(1,2)+1/beta;m=1-2/beta;ar=beta/(2*d)
for n,e in [('d_beta_gamma',d/beta-g-1),('3d_k_4beta',3*d-k-4*beta),('rho_gamma',d/beta-1-g),('r_integral_y_exponent',(ar-1)*d/beta+1+1/beta),('r_power',-ar*d/beta+s.Rational(1,2)),('r_log',ar*d*a/beta-a/2),('I_power',(k/d-1)*d/beta+m),('I_log',-(k/d-1)*d*a/beta-m*a),('P_y_cancellation',(3-k/d)*d/beta-4),('P_log',(3-k/d)*(-d*a/beta)+4*a),('u_integral_y',(2*g-s.Rational(1,2))-(1+k/beta)+1+1/beta),('u_integral_log',-2*d*a/beta+a/2+k*a/beta-(-2+1/beta)*a),('quartic_coefficient',d-k-beta+2)]:eq(n,e)
z=s.symbols('z');mu=(d-beta)/(beta*a);c0=s.symbols('c0',real=True);c_tail=1/mu-c0
bp=beta+(d-beta)/(1+mu*(s.log(y)-c0));eq('tail_bp',bp-beta-beta*a/(s.log(y)+c_tail));eq('tail_bpp',s.diff(bp,y)+beta*a/(y*(s.log(y)+c_tail)**2))
Hy=y/(s.log(y)+c);eq('tail_primitive_derivative',s.diff(Hy,y)-1/(s.log(y)+c)+1/(s.log(y)+c)**2)
q=s.symbols('q',real=True);B=beta*(1+a*z+q*z*z);inv=s.series(d/B,z,0,3).removeO();eq('inverse_first_order',inv.coeff(z,1)+d*a/beta);eq('inverse_constant',inv.coeff(z,0)-d/beta)
# Exact jet identities, with no asymptotic differentiation.
b,b1,b2,rho,r=s.symbols('b b1 b2 rho r',nonzero=True);rh1=(d-b1)*rho/b;r1=(A/rho-beta*r/2)/b;T=A/rho**2;Tp=-2*A*rh1/rho**3;eta=r/rho;etap=r1/rho-r*rh1/rho**2
for n,e in [('T2_exact',b*Tp+(3*beta+2-2*b1)*T),('V1_exact',b*etap+(2*beta+1-b1)*eta-T),('rho_b_exact',rh1*b+rho*b1-d*rho)]:eq(n,e)
runit=s.symbols('runit');runitp=(1/rho-beta*runit/2)/b;u=rho*rho*runit-2/beta;up=2*rho*rh1*runit+rho*rho*runitp;eq('u_positive_forcing_identity',b*up-(2*d-beta/2-2*b1)*u-4*(d-b1)/beta-rho+1)
P,h,R,J,Jdot=s.symbols('P h R J Jdot',nonzero=True);eq('P_log_derivative',3*rh1/rho-b1/b-k/b+4*(b1-beta)/b);eq('I_exact_extraction',h/rho*(Jdot/y+k*J/b)-h/(b*rho)*((b/y)*Jdot+k*J))
# Weighted primitives used to prove the Gb coefficient is finite.
powr=4*a+2;primitive=-t**(-4*a-1)/(4*a+1);eq('Gb_integrable_primitive',s.diff(primitive,t)-t**(-powr))
# Fixed-A dilation from arbitrary functions at the base coordinate.
lam=s.symbols('lam',positive=True);w=s.symbols('w',real=True);bf=s.Function('b')(w);rf=s.Function('rho')(w);Rfun=s.Function('R')(w);rfun=s.Function('r1')(w);gb=s.Function('Gb')(w);ge=s.Function('Ge')(w);dy=lambda f:s.diff(f,w)/lam
bl=lam*bf;rl=rf;Rll=lam*Rfun;rr=A*rfun;et=A*rfun/rf;vl=-(s.diff(bf,w,2)/lam+et)/2;Gl=gb/(A*lam)+ge;Il=dy(Gl)/rf
for n,e in [('scaled_rho',bl*dy(rl)-(d-dy(bl))*rl-(bf*s.diff(rf,w)-(d-s.diff(bf,w))*rf)),('scaled_R',dy(Rll)-s.diff(Rfun,w)),('scaled_r',bl*dy(rr)+beta*rr/2-A/rf-A*(bf*s.diff(rfun,w)+beta*rfun/2-1/rf)),('scaled_curl',-dy(dy(bl))-2*vl-et),('scaled_G',bl*dy(Gl)-k*Gl-((bf*s.diff(gb,w)-k*gb)/(A*lam)+bf*s.diff(ge,w)-k*ge)),('scaled_force',8/A*(rf**3*vl+A/beta)-(-4*rf**3*s.diff(bf,w,2)/(A*lam)-4*rf**2*rfun+8/beta)),('scaled_I',Il-s.diff(gb,w)/(rf*A*lam**2)-s.diff(ge,w)/(rf*lam)),('scaled_limit_Ib',m-2-(m-1-1)),('scaled_limit_Ie',m-1-(m-1))]:eq(n,e)
Lb,absLe=s.symbols('Lb absLe',positive=True);threshold=Lb/(A*absLe)
for f in [s.Rational(1,3),s.Rational(1,2),s.Integer(2),s.Integer(3)]:
 bracket=Lb/(A*f*threshold)-absLe;eq('threshold_identity_'+str(f),bracket-absLe*(1/f-1));ck('threshold_sign_'+str(f),s.sign(bracket)==(1 if f<1 else -1))
# Independent Cartesian coefficient generator.
x,yy=s.symbols('x yy',real=True);bf=s.Function('b')(yy);rf=s.Function('rho')(yy);vf=s.Function('v')(yy);If=s.Function('I')(yy);Tf=A/rf**2;Q4=Tf**2*If;W1=(2*beta-s.diff(bf,yy))*x-s.diff(vf,yy)*x**3/3;W2=bf+vf*x*x;Th=Tf*x*x/2+Q4*x**4/24;Om=s.diff(W1,yy)-s.diff(W2,x)
eq('physical_divergence',s.diff(W1,x)+s.diff(W2,yy)-2*beta);eq('physical_curl',Om-((-s.diff(bf,yy,2)-2*vf)*x-s.diff(vf,yy,2)*x**3/3));RT=s.expand(W1*s.diff(Th,x)+W2*s.diff(Th,yy)-(beta-2)*Th);eq('physical_T2',RT.coeff(x,2).subs(s.diff(rf,yy),(d-s.diff(bf,yy))*rf/bf));reduced=bf*s.diff(If,yy)+(beta-2)*If-8*s.diff(rf**3*vf,yy)/(A*rf);eq('physical_T4',(24*RT.coeff(x,4)/Tf**2-reduced).subs(s.diff(rf,yy),(d-s.diff(bf,yy))*rf/bf));eq('non_sublinear_axis_horizontal_line',W2.subs({bf:0,vf:-A/beta})+A*x*x/beta)
# Strict parameter margins and prescription ell=ma at representative exact beta.
ell=s.symbols('ell',positive=True)
for be in [s.Rational(201,100),s.Rational(5,2),s.Integer(3),s.Integer(10)]:
 mm=m.subs(beta,be);ck('m_positive_'+str(be),mm>0);eq('ell_prescription_'+str(be),mm*(ell/mm)-ell);ck('r_integral_margin_'+str(be),1/be>0)
ck('a_positive_assumed',a.is_positive);ck('Gb_integrability_margin',(4*a+1).is_positive)
pb=json.loads((V/'proof_before_checks.json').read_text());ck('proof_precedes_checks',pb['written_utc']<start);ck('original_proof_hash',pb['proof_sha256']==hashlib.sha256((V/'PROOF_before_editorials.md').read_bytes()).hexdigest());rev=json.loads((V/'editorial_revision.json').read_text());ck('revised_proof_hash',rev['new_proof_sha256']==hashlib.sha256((V.parent/'PROOF.md').read_bytes()).hexdigest());ck('editorial_revision_precedes_rerun',rev['utc']<start)
out={'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'passed':sum(z['passed']for z in checks),'total':len(checks),'all_passed':all(z['passed']for z in checks),'checks':checks,'original_proof_sha256':pb['proof_sha256'],'proof_sha256':rev['new_proof_sha256'],'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact algebra supplements the complete low-order theorem. No certified numerical or full B2 existence claim.'};(V/'controls.json').write_text(json.dumps(out,indent=2)+'\n');print(out['passed'],out['total'],out['elapsed_seconds']);print('FAILED',[r for r in checks if not r['passed']])
