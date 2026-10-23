"""Result175 manufactures. Independent symbolic algebra and scalar quadrature."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,math,time
import sympy as S
import mpmath as mp
from scipy.integrate import quad
root=Path('research/anisotropic_weighted_hessian/verification');root.mkdir(parents=True,exist_ok=True)
start=time.monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','proof_sha256':hashlib.sha256(Path('research/anisotropic_weighted_hessian/PROOF.md').read_bytes()).hexdigest(),'symbolic':[],'quadratures':[]}
def save(): (root/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
def check(name,v):
 z=S.simplify(S.expand(v));assert z==0,(name,z);out['symbolic'].append(name)
x,y,p,ell,eps=S.symbols('x y p ell eps',real=True)
a,b=S.symbols('a b',positive=True)
J=S.pi/(2*a*b*(a+b))
check('radial-angular-strain',((J+(b*b+1)/(2*b)*S.diff(J,b))*2*a/S.pi).subs(b,1)+1/(1+a)**2)
u=S.symbols('u',positive=True)
check('first-radial-antiderivative',S.diff((1+u*u)**p/(2*p),u)-u*(1+u*u)**(p-1))
check('second-radial-antiderivative',S.diff((1+u*u)**p/(2*p)-(1+u*u)**(p-1)/(2*(p-1)),u)-u**3*(1+u*u)**(p-2))
g=y*(1+x*x+y*y)**p;v1=x*(1+x*x+y*y)**p
check('radial-hydrostatic-vertical',S.diff(v1,y)-S.diff(g,x))
check('radial-center',-S.diff(v1,x).subs({x:0,y:0})+1)
B,E,D,F,c=S.symbols('B E D F c');gp=y+B*x*x*y+E*y**3;ph=c*x*y+D*x**3*y+F*x*y**3
R=S.expand(((ell*x-S.diff(ph,y))*S.diff(gp,x)+(ell*y+S.diff(ph,x))*S.diff(gp,y)-gp).subs(c,1-ell))
check('profile-cubic-xxy',R.coeff(x,2).coeff(y,1)-((4*ell-2)*B+3*D))
check('profile-cubic-yyy',R.coeff(x,0).coeff(y,3)-(2*E+F))
po=S.expand(-S.diff(ph,y,2)-eps*S.diff(ph,x,2)-S.diff(gp,x))
check('anisotropic-cubic-poisson',po.coeff(x,1).coeff(y,1)-(-6*eps*D-6*F-2*B))
check('eliminated-cubic',(-6*eps*D-6*F-2*B).subs({D:-(4*ell-2)*B/3,F:-2*E})+2*((1-eps*(4*ell-2))*B-6*E))
# Non-profile diagnostic for the growing radial input, gamma=.5, ell2.
check('radial-not-profile-jet',((1-eps*(4*ell-2))*B-6*E).subs({eps:0,ell:2,B:-S.Rational(1,4),E:-S.Rational(1,4)})-S.Rational(5,4))
save()
for ep in [100.,1.,1e-2,1e-4,1e-8,1e-12]:
 aa=math.sqrt(ep)
 # z=a tan(t) removes the narrow pole before applying scalar quadrature.
 def ff(t):
  z=aa*math.tan(t);return (z*z-1)/(1+z*z)**2
 cuts=sorted(set([0.,math.pi/4,math.pi/2]+[math.atan(10.**j/aa) for j in range(-4,5)]))
 pairs=[quad(ff,l,r,epsabs=2e-14,epsrel=2e-13,limit=300) for l,r in zip(cuts[:-1],cuts[1:])]
 val=sum(v for v,e in pairs);err=sum(e for v,e in pairs)
 val*=2/math.pi;err*=2/math.pi;exact=-1/(1+aa)**2
 with mp.workdps(60):
  ea=mp.sqrt(mp.mpf(ep));f=lambda t:(ea*ea*mp.tan(t)**2-1)/(1+ea*ea*mp.tan(t)**2)**2
  ref=2/mp.pi*mp.quad(f,[0,mp.atan(1/ea),mp.pi/2])
 assert abs(val-exact)<1e-10*max(1,abs(exact)) and abs(float(ref)-exact)<2e-15
 out['quadratures'].append({'epsilon':ep,'scipy_strain':val,'exact_strain':exact,'mp60_strain':mp.nstr(ref,50),'integration_breakpoints':cuts,'estimated_error':err,'absolute_error':abs(val-exact)});save()
out.update(status='PASS',finished_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,symbolic_count=len(out['symbolic']));save();print(json.dumps({'status':'PASS','symbolic':len(out['symbolic']),'quadratures':len(out['quadratures']),'elapsed_seconds':out['elapsed_seconds']}))
