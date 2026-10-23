"""Independent algebra for result168. Does not import external checker code."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
import sympy as s
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time,resource
resource.setrlimit(resource.RLIMIT_AS,(1800*1024**2,1800*1024**2))
start=time.monotonic();x,y=s.symbols('x y',real=True);z=x*x+y*y;ell,a,b,d,P,T=s.symbols('ell a b d P T');checks=[]
def D(f):return -y*s.diff(f,x)+x*s.diff(f,y)
def E(f):return x*s.diff(f,x)+y*s.diff(f,y)
def lap(f):return s.diff(f,x,2)+s.diff(f,y,2)
def dot(v,f):return v[0]*s.diff(f,x)+v[1]*s.diff(f,y)
def velocity(psi):return [-s.diff(psi,y),s.diff(psi,x)]
def check(label,v):
 v=s.simplify(v);assert v==0,(label,v);checks.append(label)
# General differential identities on independent nonhomogeneous polynomials.
f=y*(a+2*x*x+3*y*y+5*x**4-7*x*x*y*y);psi=x*y*(-2+3*x*x-4*y*y+5*z*z);u=velocity(psi);C=[D(u[0])+u[1],D(u[1])-u[0]];W=[ell*x+u[0],ell*y+u[1]]
check('rotation commutator',D(dot(u,f))-dot(u,D(f))-dot(C,f))
check('rotation and dilation',D(E(f))-E(D(f)))
check('stream commutator component1',C[0]+s.diff(D(psi),y));check('stream commutator component2',C[1]-s.diff(D(psi),x))
check('rotation and Laplacian',lap(D(psi))-D(lap(psi)))
check('rotation and x derivative',D(s.diff(f,x))-s.diff(D(f),x)+s.diff(f,y))
q=s.cancel(f/(a*y));beta=s.cancel(u[1]/y);A=1-ell-beta;res=dot(W,f)-f;v=D(f);Q=D(q)
check('v equation including nonprofile residual',dot(W,v)-v+dot(C,f)-D(res))
check('q equation including nonprofile residual',dot(W,q)-A*q-res/(a*y))
check('Q equation including nonprofile residual',dot(W,Q)-A*Q+q*D(beta)+dot(C,q)-D(res/(a*y)))
check('angular product rule',v-a*(x*q+y*Q))
check('bounded-domain divergence identity',s.diff(W[0]*v*v/2,x)+s.diff(W[1]*v*v/2,y)-(ell+1)*v*v+v*dot(C,f)-v*D(res))
# Cubic coefficients with exact normalization, no use of the alleged relation.
rho=a*y+b*x*x*y+d*y**3;psi=(1-ell)*x*y+P*x**3*y+T*x*y**3;u=velocity(psi);R=s.Poly(s.expand(dot([ell*x+u[0],ell*y+u[1]],rho)-rho),x,y)
check('xxy transport',R.coeff_monomial(x*x*y)-(3*a*P+(4*ell-2)*b));check('yyy transport',R.coeff_monomial(y**3)-(a*T+2*d));check('Poisson cubic',lap(psi)+s.diff(rho,x)-(6*(P+T)+2*b)*x*y)
sol=s.solve([3*a*P+(4*ell-2)*b,a*T+2*d],(P,T));check('eliminated center identity',s.factor((6*(P+T)+2*b).subs(sol)*a/2)-(a*b-(4*ell-2)*b-6*d))
# Gaussian: independent symbolic radial potential, formal h checked before substitution.
t=s.symbols('t',positive=True);F=(1-s.exp(-t))/t;h=s.diff(F,t)
check('radial Poisson',t*s.diff(F,t,2)+2*s.diff(F,t)+s.exp(-t));check('h zero',s.limit(h,t,0)+s.Rational(1,2));check('hprime zero',s.limit(s.diff(h,t),t,0)-s.Rational(1,3))
H=s.Function('H');psi=2*x*y*H(z);u=velocity(psi);C=[D(u[0])+u[1],D(u[1])-u[0]];q=s.exp(-z);rho=4*y*q;beta=s.cancel(u[1]/y)
qforce=-q*D(beta)-dot(C,q);expected=8*x*y*s.exp(-z)*(s.diff(H(z),x)/(2*x)+2*H(z));check('Gaussian Q forcing',qforce-expected)
peak={x:s.sqrt(2)/2,y:s.sqrt(2)/2};subsH={H(1):h.subs(t,1),s.Subs(s.Derivative(H(t),t),t,1):s.diff(h,t).subs(t,1)}
# Evaluate with explicit h only after differentiating, to avoid a numerical or implicit derivative.
psi=2*x*y*h.subs(t,z);u=velocity(psi);C=[D(u[0])+u[1],D(u[1])-u[0]]
qforce=-q*D(s.cancel(u[1]/y))-dot(C,q);vforce=-dot(C,rho)
check('Gaussian Q peak',qforce.subs(peak)+4/s.exp(2));check('Gaussian v peak',vforce.subs(peak)-16*peak[x]/s.exp(1)*(-1+2/s.exp(1)))
check('Gaussian critical gradientx',s.diff(rho,x).subs({x:0,y:s.sqrt(2)/2}));check('Gaussian critical gradienty',s.diff(rho,y).subs({x:0,y:s.sqrt(2)/2}));assert rho.subs({x:0,y:s.sqrt(2)/2})!=0;checks.append('Gaussian is a nonprofile')
# Contact density and its exact pointwise values.
rho=y*s.exp(3*z)*(1-s.Rational(4,3)*z*y*y+s.Rational(4,5)*y**4);v=D(rho)
check('contact angular derivative',v-x*s.exp(3*z)*(1-4*x*x*y*y))
check('contact density',rho.subs(peak)-8*s.exp(3)/(15*s.sqrt(2)));check('contact radial density',E(rho).subs(peak)-28*s.exp(3)/(15*s.sqrt(2)));check('contact radial v',E(v).subs(peak)+4*s.exp(3)/s.sqrt(2));check('contact angular v',D(v).subs(peak))
check('first contact transport',s.Rational(2,7)*E(rho).subs(peak)-rho.subs(peak));check('first contact angular transport',s.Rational(2,7)*E(v).subs(peak)+s.Rational(30,49)*E(rho).subs(peak))
columns=[]
for n in [2,4,6]:
 phi=s.expand(s.im((x+s.I*y)**(n+1)))/(n+1);ps=s.diff(phi,x);check(f'harmonic potential {n}',lap(phi));check(f'stream derivative {n}',ps-s.expand(s.im((x+s.I*y)**n)))
 ur=-D(ps)/s.sqrt(z);column=[s.diff(ps,x,y).subs({x:0,y:0}),ur.subs(peak),D(ur).subs(peak)];columns.append(column)
 for j,val in enumerate([[2,0,4],[0,4,0],[0,0,-36]][[2,4,6].index(n)]):check(f'contact correction {n} column{j}',column[j]-val)
assert s.Matrix.hstack(*[s.Matrix(z)for z in columns]).det()==-288;checks.append('independent contact adjustment matrix invertible')
# Local two-source construction and flat-equilibrium matrix.
phi=-y*z/2;rho=-lap(phi);u=velocity(s.diff(phi,x));check('local primary density',rho-4*y);check('local primary residual',dot([2*x+u[0],2*y+u[1]],rho)-rho)
phi=6*x*y+3*(y*y-x*x);check('local remote zero density',lap(phi));u=velocity(s.diff(phi,x));check('remote source velocityx',u[0]+6);check('remote source velocityy',u[1]+6)
hh,kk,lamb=s.symbols('hh kk lamb');M=s.Matrix([[ell-hh,kk],[kk,ell+hh]]);check('flat equilibrium eigenvalue polynomial',(M-lamb*s.eye(2)).det()-((ell-lamb)**2-hh**2-kk**2))
root=Path('research/angular_contact_zero_regions');out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','checks':len(checks),'labels':checks,'elapsed_seconds':time.monotonic()-start,'max_rss_KiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'proof_sha256':hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact algebra and examples; flow claims separately proved in PROOF.md with explicit standard theorem dependencies; no endpoint.'}
(root/'verification/CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
