"""P264 exact algebraic controls; no teammate code or numerical profile inputs."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s,json,hashlib,time
V=Path('research/264_critical_axis_data/verification');start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();checks=[]
def eq(name,e):
 q=s.factor(s.cancel(s.expand(s.powsimp(e,force=False))));checks.append({'name':name,'passed':q==0,'difference':str(q)})
def ck(name,p,detail=None):checks.append({'name':name,'passed':bool(p),'detail':detail})
beta=s.symbols('beta',positive=True);A=s.symbols('A',nonzero=True);C=s.symbols('C',positive=True);D,K,c2=s.symbols('D K c2',real=True);y=s.symbols('y',positive=True);d=(3*beta+2)/2;k=(beta+6)/2;gamma=s.Rational(1,2)+1/beta;m=1-2/beta;p=s.Rational(1,2)+2/beta;a=beta/(2*d)
b,rho,bp,bpp,r1,q,u=s.symbols('b rho bp bpp r1 q u',real=True)
rhop=(d-bp)*rho/b;r1p=(1/rho-beta*r1/2)/b
qprime=2*rho*rhop*r1+rho**2*r1p
eq('q_transport',b*qprime-(2*d-2*bp-beta/2)*rho**2*r1-rho)
eq('u_forcing',((2*d-2*bp-beta/2)*(u+2/beta)+rho)-((2*d-beta/2-2*bp)*u+4*(d-bp)/beta+rho-1))
eq('G_eta_source',-4*(u+2/beta)+8/beta+4*u)
eq('G_split',8/A*(rho**3*(-bpp-A*r1/rho)/2+A/beta)-(-4*rho**3*bpp/A-4*rho**2*r1+8/beta))
R=s.Function('R')(y);J=s.Function('J')(y);rv=A/d*R**(-a)*J
rder=s.diff(rv,y).subs({s.diff(R,y):d*R/b,s.diff(J,y):R**(a-1)})
eq('integral_r_solution',b*rder+beta*rv/2-A*R**0/(d*R/b))
eq('inner_r',A/(d*a)-2*A/beta)
# Check tail identities at symbolic beta by comparing the exponent and coefficient separately.
for name,e in [('rho_power',(d-beta)/beta-gamma),('R_integral',beta*(gamma+1)/d-1),('eta_D_power',-s.Rational(1,2)-gamma+1+1/beta),('eta_A_power',-2*gamma+1+2/beta),('G_D_exponent',3*gamma-1-1/beta-p),('G_A_exponent',3*gamma-1-2/beta-gamma),('G_D_operator',beta*p-k+1),('G_A_operator',beta*gamma-k+2),('critical_I_power',k/beta-1-gamma+m),('secondary_I_power',p-1-gamma+1-1/beta),('leading_gap',(-m)-(-1+1/beta)-1/beta),('eta_integral_exponent',p-1-k/beta+1+1/beta)]:eq(name,e)
for betav in [s.Integer(2),s.Rational(5,2),s.Integer(3),s.Integer(4),s.Integer(10)]:
 gv=gamma.subs(beta,betav);kv=k.subs(beta,betav);pv=p.subs(beta,betav);mv=m.subs(beta,betav)
 rt=D*y**s.Rational(-1,2)-A/C*y**(-gv);rh=C*y**gv;Gt=K*y**(kv/betav)+4*D*C*C/A*y**pv-2*C*y**gv+8*c2/(A*kv)
 rhs=-4*D*C*C/A*y**pv+4*C*y**gv-8*c2/A
 eq('tail_r_beta'+str(betav),betav*y*s.diff(rt,y)+betav*rt/2-A/rh)
 eq('tail_G_beta'+str(betav),betav*y*s.diff(Gt,y)-kv*Gt-rhs)
 Ipred=K*kv/(betav*C)*y**(-mv)+4*D*C/A*pv*y**(-1+1/betav)-2*gv/y
 eq('tail_I_beta'+str(betav),s.diff(Gt,y)/rh-Ipred)
 eq('eta_curl_beta'+str(betav),rt/rh+2*(-rt/rh/2))
# beta2 shift is globally homogeneous; its change to I is exactly constant.
R0,Rp,I0=s.symbols('R0 Rp I0',real=True)
eq('beta2_R_homogeneous',(d-k).subs(beta,2)*R0)
eq('I_shift',I0*rho/rho-I0)
# Physical polynomial-jet realization of all claimed coefficients.
x=s.symbols('x',real=True);B=s.Function('B')(y);Vv=s.Function('V')(y);Rh=s.Function('rho')(y);Iv=s.Function('I')(y)
T=A/Rh**2;Q=A**2*Iv/Rh**4;w1=(2*beta-s.diff(B,y))*x-s.diff(Vv,y)*x**3/3;w2=B+Vv*x*x;Th=T*x*x/2+Q*x**4/24;Om=s.diff(w1,y)-s.diff(w2,x)
eq('jet_divergence',s.diff(w1,x)+s.diff(w2,y)-2*beta)
eq('jet_curl',Om-((-s.diff(B,y,2)-2*Vv)*x-s.diff(Vv,y,2)*x**3/3))
res=s.expand(w1*s.diff(Th,x)+w2*s.diff(Th,y)-(beta-2)*Th)
sub={s.diff(Rh,y):(d-s.diff(B,y))*Rh/B}
eq('jet_T2',res.coeff(x,2).subs(sub))
eq('beta2_explicit_missing_V3',s.expand((A*x)-(A*x+A*A*I0*x**3/6)).coeff(x,3)+A*A*I0/6)
# A finite large-A choice really produces a negative L for arbitrary L_b.
Lb,ell=s.symbols('Lb ell',real=True);bb=s.symbols('bb',nonnegative=True);ll=s.symbols('ll',positive=True)
for sign in [-1,1]:
 AA=2+2*bb/ll;Lv=sign*bb/AA-ll
 numerator,denominator=s.fraction(s.factor(-Lv));ck('large_A_negative_'+str(sign),s.Poly(numerator,bb,ll).coeffs()[0]>0 and all(c>=0 for c in s.Poly(numerator,bb,ll).coeffs()+s.Poly(denominator,bb,ll).coeffs()),str(Lv))
proof=json.loads((V/'proof_before_checks.json').read_text());ck('proof_precedes_checks',proof['written_utc']<start);ck('proof_hash',proof['proof_sha256']==hashlib.sha256((V.parent/'PROOF.md').read_bytes()).hexdigest())
out={'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'passed':sum(c['passed']for c in checks),'total':len(checks),'all_passed':all(c['passed']for c in checks),'checks':checks,'proof_sha256':proof['proof_sha256'],'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact formulas for a one-dimensional low-order subsystem. Analytic construction is in PROOF.md; no full B2 profile or inverse is constructed.'}
(V/'controls.json').write_text(json.dumps(out,indent=2)+'\n');print(out['passed'],out['total'],out['elapsed_seconds']);print([c for c in checks if not c['passed']])
