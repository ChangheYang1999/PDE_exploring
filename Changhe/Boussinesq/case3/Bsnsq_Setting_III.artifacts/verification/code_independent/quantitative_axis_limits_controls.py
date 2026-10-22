"""P272 independent Cartesian, integrating factor and homogeneous jet controls."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s, json,hashlib,time
V=Path('research/272_quantitative_axis_ratio_limits/verification');started=datetime.now(timezone.utc).isoformat();tick=time.monotonic();checks=[]
def eq(n,e):
 z=s.factor(s.simplify(s.expand(e)));checks.append({'name':n,'passed':z==0,'difference':str(z)})
def ck(n,p,detail=None):checks.append({'name':n,'passed':bool(p),'detail':detail})
beta=s.symbols('beta',positive=True);A=s.symbols('A',nonzero=True);delta=s.symbols('delta',positive=True);d=(3*beta+2)/2;k=(beta+6)/2;g=s.Rational(1,2)+1/beta;m=1-2/beta
for n,e in [('rho_exponent',d/beta-1-g),('mu_exponent',beta/(2*beta)-s.Rational(1,2)),('r_integrand',s.Rational(1,2)-1-g+1+1/beta),('eta_exponent',-s.Rational(1,2)-g+1+1/beta),('P_exponent',3*g-1-k/beta),('I_prefactor',k/beta-1-g+m),('critical_error',-m-1/beta+1-1/beta),('T_exponent',m-2+2*g)]:eq(n,e)
ck('rho_inverse_cube_faster',s.simplify(3*g-(1+1/beta)).is_positive)
y=s.symbols('y',positive=True)
eq('R_integrable_error_primitive',s.diff(-y**(-delta)/delta,y)-y**(-1-delta))
eq('r_integrand_primitive',s.diff(-beta*y**(-1/beta),y)-y**(-1-1/beta))
epsilon=s.symbols('epsilon',positive=True)
eq('H_tail_primitive',s.diff(-y**(-epsilon)/epsilon,y)-y**(-1-epsilon))
# Exact algebra does not differentiate big O terms.
b,b1,b2,rho,r,h,R,G,I,c2=s.symbols('b b1 b2 rho r h R G I c2',nonzero=True)
rhop=(d-b1)*rho/b;rp=(A/rho-beta*r/2)/b;hp=k*h/b;Gp=rho*I
v,vp,Ip=s.symbols('v vp Ip');T=A/rho**2;Tp=-2*A*rhop/rho**3;D=A*A*I/rho**4;Dp=A*A*(Ip/rho**4-4*I*rhop/rho**5);eta=r/rho;etap=rp/rho-r*rhop/rho**2
for n,e in [('T2_equation',b*Tp+(3*beta+2-2*b1)*T),('V1_equation',b*etap+(2*beta+1-b1)*eta-T),('rho_b_integral_derivative',b*rhop+b1*rho-d*rho),('quartic_derivative',(b*Dp+(7*beta+2-4*b1)*D-8*vp*T+12*v*Tp)/T**2-b*Ip-(beta-2)*I+8*(3*rho*rho*rhop*v+rho**3*vp)/(A*rho)),('integral_cancellation',d-k-beta+2)]:eq(n,e)
Gsub=(d*R*I-8*(rho**3*v-c2)/A)/k
Hprime=A*(Gp/h-G*hp/h**2);P=rho**3/(b*h)
eq('H_exact_derivative',(Hprime-8*P*(v-c2/rho**3)).subs(G,Gsub).subs(R,b*rho/d))
eq('H_curl_form',(8*P*(v-c2/rho**3)+4*P*(b2+eta+2*c2/rho**3)).subs(v,-(b2+eta)/2))
H,Hprime=s.symbols('H Hprime');eq('ratio_extraction', (hp*H+h*Hprime)/(A*rho)-h/(A*b*rho)*(k*H+b*Hprime))
Ch,Cr,Hinf,alpha=s.symbols('Ch Cr Hinf alpha',nonzero=True);L=k*Ch*Hinf/(A*beta*Cr);eq('h_normalization_invariance',L.subs({Ch:alpha*Ch,Hinf:Hinf/alpha},simultaneous=True)-L)
# Independently regenerate Cartesian coefficients directly from polynomials.
x,yy=s.symbols('x yy',real=True);bf=s.Function('b')(yy);vf=s.Function('v')(yy);Tf=s.Function('T')(yy);Df=s.Function('D')(yy)
W1=(2*beta-s.diff(bf,yy))*x-s.diff(vf,yy)*x**3/3;W2=bf+vf*x*x;Th=Tf*x*x/2+Df*x**4/24;Om=s.diff(W1,yy)-s.diff(W2,x);et=-s.diff(bf,yy,2)-2*vf
RT=s.expand(W1*s.diff(Th,x)+W2*s.diff(Th,yy)-(beta-2)*Th);RO=s.expand(W1*s.diff(Om,x)+W2*s.diff(Om,yy)+Om-s.diff(Th,x))
eq('physical_divergence',s.diff(W1,x)+s.diff(W2,yy)-2*beta)
eq('physical_T2',2*RT.coeff(x,2)-bf*s.diff(Tf,yy)-(3*beta+2-2*s.diff(bf,yy))*Tf)
eq('physical_T4',24*RT.coeff(x,4)-bf*s.diff(Df,yy)-(7*beta+2-4*s.diff(bf,yy))*Df+8*s.diff(vf,yy)*Tf-12*vf*s.diff(Tf,yy))
eq('physical_V1',RO.coeff(x,1)-bf*s.diff(et,yy)-(2*beta+1-s.diff(bf,yy))*et+Tf)
# Exact shifted power tails from a distinct direct scalar ODE calculation.
y,z,C,Bcoef,Dcoef,K,c=s.symbols('y z C Bcoef Dcoef K c',positive=True);Rtail=beta*C*z**(g+1)/d;rhotail=C*z**g;rtail=Dcoef*z**(-s.Rational(1,2))-A/C*z**(-g);btail=beta*z
eq('tail_rho_b',rhotail*btail-d*Rtail)
eq('tail_r_ODE',btail*s.diff(rtail,z)+beta*rtail/2-A/rhotail)
Gtail=K*z**(k/beta)+4*Dcoef*C*C/A*z**(s.Rational(1,2)+2/beta)-2*C*z**g-8/(beta*k)
vtail=-rtail/(2*rhotail)
eq('tail_G_ODE',btail*s.diff(Gtail,z)-k*Gtail-8/A*(rhotail**3*vtail+A/beta))
Iexpected=k*K/(beta*C)*z**(-m)+4*Dcoef*C/A*(s.Rational(1,2)+2/beta)*z**(-1+1/beta)-2*g/z
eq('tail_I_exact',s.diff(Gtail,z)/rhotail-Iexpected)
for be in [s.Integer(2),s.Rational(5,2),s.Integer(3),s.Integer(10)]:
 mm=m.subs(beta,be);ck('error_margin_'+str(be),(-1+1/be)<-mm);ck('inverse_cube_margin_'+str(be),(3*g-1-1/beta).subs(beta,be)>0)
# General finite-order quotient and scaling, allowing zero numerator.
n=s.symbols('n',integer=True,positive=True)
eq('normalized_jet_power',m-2*n-n*(m-2)+(n-1)*m)
eq('rescaling_temperature_power',-(beta-2)/beta+2*n-(2*n-m))
q,a0,a1,b0,b1=s.symbols('q a0 a1 b0 b1',nonzero=True)
for order in range(1,7):
 ser=s.series((a0+q*a1)/(b0+q*b1)**order,q,0,2).removeO();eq('quotient_leading_'+str(order),ser.coeff(q,0)-a0/b0**order);eq('quotient_first_'+str(order),ser.coeff(q,1)-(a1/b0**order-order*a0*b1/b0**(order+1)))
 eq('reflection_factor_'+str(order),(-1)/(-1)**order-(-1)**(1-order))
# Homogeneous temperature manufactured outside the origin, independently differentiated.
x,y=s.symbols('x y',real=True);p=s.symbols('p',real=True);yy=s.symbols('yy',positive=True)
Th=x*x*(x*x+yy*yy)**((p-2)/2)+3*x**4*(x*x+yy*yy)**((p-4)/2)+5*x**6*(x*x+yy*yy)**((p-6)/2)
jetcoeff={1:s.Integer(2),2:12*(p+4),3:90*(p*p+6*p)}
for order,coeff in jetcoeff.items():
 derivative=s.diff(Th,x,2*order).subs(x,0)
 eq('homogeneous_cartesian_jet_'+str(order),derivative/yy**(p-2*order)-coeff)
 eq('homogeneous_ratio_power_'+str(order),s.powsimp((derivative/(2*yy**(p-2))**order)*yy**((order-1)*p),force=True)-coeff/2**order)
# Abstract negative-end reflection checked without assuming a physical realization.
w=s.symbols('w',real=True);bb=s.Function('b')(w);rr=s.Function('r')(w);rh=s.Function('rho')(w);vv=s.Function('v')(w);II=s.Function('I')(w);RR=s.Function('R')(w);GG=s.Function('G')(w);cc=s.symbols('cc');dy=lambda z:-s.diff(z,w)
for name,z in [('rho_b',rh*(-bb)-d*(-RR)+(rh*bb-d*RR)),('r_equation',(-bb)*dy(-rr)+beta*(-rr)/2-(-A)/rh+(bb*s.diff(rr,w)+beta*rr/2-A/rh)),('curl',(-rr)/rh+dy(dy(-bb))+2*(-vv)+(rr/rh+s.diff(bb,w,2)+2*vv)),('quartic',rh**3*(-vv)-(-cc)-(-A)/8*(d*(-RR)*(-II)-k*GG)+(rh**3*vv-cc-A/8*(d*RR*II-k*GG))),('G_primitive',dy(GG)-rh*(-II)+(s.diff(GG,w)-rh*II)),('R_primitive',dy(-RR)-rh-(s.diff(RR,w)-rh))]:eq('abstract_reflection_'+name,z)
# Every source dependency is independently frozen rather than imported as executable code.
for item in json.loads((V/'freeze.json').read_text())['inputs']:ck('input_hash_'+Path(item['snapshot']).name,hashlib.sha256(Path(item['snapshot']).read_bytes()).hexdigest()==item['sha256'])
pb=json.loads((V/'proof_before_checks.json').read_text());ph=hashlib.sha256((V.parent/'PROOF.md').read_bytes()).hexdigest();ck('proof_precedes_checks',pb['written_utc']<started);ck('original_proof_hash',pb['proof_sha256']==hashlib.sha256((V/'PROOF_before_editorials.md').read_bytes()).hexdigest());rev=json.loads((V/'editorial_revision.json').read_text());ck('current_proof_hash',rev['new_proof_sha256']==ph);ck('editorials_before_rerun',rev['utc']<started)
out={'started_utc':started,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'passed':sum(c['passed'] for c in checks),'total':len(checks),'all_passed':all(c['passed'] for c in checks),'checks':checks,'proof_sha256':ph,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact controls supplement an informal necessary-condition proof, with explicit class-A dependencies. No full B2 endpoint.'};(V/'controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['started_utc','ended_utc','elapsed_seconds','passed','total','all_passed']},indent=2));print('FAILED',[c for c in checks if not c['passed']])
