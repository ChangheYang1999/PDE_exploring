"""Fresh symbolic Green integration and exact disk quadratic-energy computation."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from math import factorial
import hashlib,json,sys
import sympy as s
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/nonlinear_x_obstruction'
def check(v,t):
 if not v:raise ValueError(t)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def rat(v):v=s.Rational(v);return str(v.p)+'/'+str(v.q)
x,y,r,t,z,A,eps,a=s.symbols('x y r t z A eps a',real=True);R=x*x+y*y;H=s.expand(x*x*y*(1-R)**6);psi=0;ext=0;rows=[]
chi=(1-z)**6;src={2:s.expand(r*r*chi.subs(z,r*r)+r**4*s.diff(chi,z).subs(z,r*r)/2),4:s.expand(r**4*s.diff(chi,z).subs(z,r*r)/4)}
for n in [2,4]:
 f=src[n];low=s.integrate(t**(n+1)*f.subs(r,t),(t,0,r));up=s.integrate(t**(1-n)*f.subs(r,t),(t,r,1));inn=s.expand((r**(-n)*low+r**n*up)/(2*n));coef=s.integrate(t**(n+1)*f.subs(r,t),(t,0,1))/(2*n);ang=s.im(s.expand((x+s.I*y)**n))
 for (j,),c in s.Poly(inn,r).terms():
  check(j>=n and (j-n)%2==0,'regular Cartesian power');psi+=c*R**((j-n)//2)*ang
 ext+=coef*ang/R**n
 check(s.expand(-(s.diff(inn,r,2)+s.diff(inn,r)/r-n*n*inn/r**2)-f)==0,'unit Green ODE')
 rows.append({'mode':n,'inner':{str(j):rat(c) for (j,),c in s.Poly(inn,r).terms()},'exterior':rat(coef)})
psi=s.expand(psi);U=[-s.diff(psi,y),s.diff(psi,x)];Q=s.expand(sum(u*s.diff(H,j) for u,j in zip(U,[x,y])));grad=[s.diff(Q,j) for j in [x,y]]
check(s.Poly(Q,x,y).coeff_monomial(x*x*y)==-s.Rational(1,56),'nonzero cubic coefficient')
check(all(sum(mon)>=3 for mon,c in s.Poly(Q,x,y).terms()),'no lower quadratic term')
check(s.expand(-(s.diff(psi,x,2)+s.diff(psi,y,2))-s.diff(H,x))==0,'Cartesian Poisson')
expected=-x*y/(2016*R**2)-x*y*(x*x-y*y)/(3360*R**4);check(s.cancel(ext-expected)==0,'rational exterior')
diagonal=s.factor(s.diff(ext,x,y).subs({x:A,y:A}));check(diagonal==-1/(2688*A**4),'diagonal strain')
translated=s.simplify(4*a/eps*diagonal.subs(A,4/eps));check(translated==-a*eps**3/172032,'four-packet strain')
g=s.expand(-s.Rational(56,3)*(x*x*y*(1-R)**6-x*x*y*(1-R/4)**6));check(s.Poly(g,x,y).coeff_monomial(x*x*y)==0,'g center zero');check(s.Poly(g,x,y).coeff_monomial(x**4*y)==84 and s.Poly(g,x,y).coeff_monomial(x*x*y**3)==84,'g leading degree5')
check(-s.Rational(56,3)*(s.Rational(1,56)-s.Rational(4,56))==1,'g strain one')
energy=s.expand(sum(v*v for v in grad));moment=F(0);terms=0
for (i,j),c in s.Poly(energy,x,y).terms():
 if i%2 or j%2:continue
 alpha,beta=i//2,j//2;order=alpha+beta;disk=F(factorial(2*alpha)*factorial(2*beta),4**order*factorial(alpha)*factorial(beta)*factorial(order)*(order+1))*F(1,2)**(2*order+2);moment+=F(int(c.p),int(c.q))*disk;terms+=1
check(moment>0,'strict positive patch gradient integral')
def coefficients(p):return [{'powers':list(mon),'coefficient':rat(c)} for mon,c in s.Poly(s.expand(p),x,y).terms()]
prior=json.loads((B/'research/graph_center_norm/evidence/verdict.json').read_text());pins={}
for name,h in prior['files'].items():check(sha(B/name)==h,'unit theorem pin');pins[name]=h
for pth in [D/'PROOF.md',D/'evidence/proof_first.json',Path(__file__),B/'research/graph_center_norm/evidence/verdict.json']:pins[str(pth.relative_to(B))]=sha(pth)
check(json.loads((D/'evidence/proof_first.json').read_text())['proof_sha256']==sha(D/'PROOF.md'),'proof first')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_FRESH_GREEN_QUADRATIC_POLYNOMIAL_AND_EXACT_DISK_ENERGY','radial_modes':rows,'cartesian':{'H':coefficients(H),'psi':coefficients(psi),'U1':coefficients(U[0]),'U2':coefficients(U[1]),'Q_H':coefficients(Q),'Q_x':coefficients(grad[0]),'Q_y':coefficients(grad[1])},'Q_H_cubic_coefficient':'-1/56','diagonal_strain_coefficient':'-1/2688','four_packet_strain_coefficient':'-1/172032','g_J':'0/1','g_Sigma':'1/1','g_leading_radial_factor':'84/1','disk_radius':'1/2','gradient_energy_over_pi':str(moment),'gradient_energy_polynomial_terms_integrated':terms,'files':pins,'scope':'Exact finite unit arithmetic for the explicit concentration theorem. No actual nonlinear closing constant, graph-norm obstruction or PDE endpoint.'}
p=D/'evidence/compute.json';check(not p.exists(),'immutable');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['utc','status','Q_H_cubic_coefficient','four_packet_strain_coefficient','gradient_energy_over_pi','gradient_energy_polynomial_terms_integrated']}))
