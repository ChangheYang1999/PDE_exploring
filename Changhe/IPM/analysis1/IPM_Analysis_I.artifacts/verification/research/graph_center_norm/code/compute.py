from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json,sys
import sympy as s
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/graph_center_norm'
def check(q,label):
 if not q:raise ValueError(label)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def rat(x):x=s.Rational(x);return str(int(x.p))+'/'+str(int(x.q))
x,y,r,t,z=s.symbols('x y r t z',real=True);R=x*x+y*y;chi=(1-z)**6;H=s.expand(x*x*y*(1-R)**6)
f2=s.expand(r*r*chi.subs(z,r*r)+r**4*s.diff(chi,z).subs(z,r*r)/2);f4=s.expand(r**4*s.diff(chi,z).subs(z,r*r)/4)
source=s.expand(s.expand(f2/r**2).subs(r*r,R)*2*x*y+s.expand(f4/r**4).subs(r*r,R)*4*x*y*(x*x-y*y));check(s.expand(source-s.diff(H,x))==0,'Cartesian source reconstructed')
rows=[];psicart=0;match=0
for n,f in ((2,f2),(4,f4)):
 A=s.integrate(t**(n+1)*f.subs(r,t),(t,0,r));Bint=s.integrate(t**(1-n)*f.subs(r,t),(t,r,1));psi=s.expand((r**(-n)*A+r**n*Bint)/(2*n));exterior=s.integrate(t**(n+1)*f.subs(r,t),(t,0,1))/(2*n)*r**(-n)
 check(s.simplify(-(s.diff(psi,r,2)+s.diff(psi,r)/r-n*n*psi/r**2)-f)==0,'radial Poisson')
 endpoint=[]
 for j in range(7):
  a=s.diff(psi,r,j).subs(r,1);b=s.diff(exterior,r,j).subs(r,1);check(a==b,'matching derivative through6');endpoint.append(rat(a));match+=1
 angular=s.im(s.expand((x+s.I*y)**n));polynomial=0
 for (degree,),coeff in s.Poly(psi,r).terms():
  check(degree>=n and (degree-n)%2==0,'Cartesian polynomial parity');polynomial+=coeff*R**((degree-n)//2)*angular
 psicart+=polynomial
 rows.append({'stream_mode':n,'source_coefficients':{str(p[0]):rat(c) for p,c in s.Poly(f,r).terms()},'inner_stream_coefficients':{str(p[0]):rat(c) for p,c in s.Poly(psi,r).terms()},'exterior_stream_coefficient':rat(s.expand(exterior*r**n)),'matching_jets_0_through_6':endpoint})
psicart=s.expand(psicart);U=[-s.diff(psicart,y),s.diff(psicart,x)];check(s.expand(-s.diff(psicart,x,2)-s.diff(psicart,y,2)-s.diff(H,x))==0,'Cartesian Poisson');check(s.expand(s.diff(U[0],x)+s.diff(U[1],y))==0,'divergence');check(s.expand(s.diff(U[1],x)-s.diff(U[0],y)+s.diff(H,x))==0,'curl');check(all(q.subs({x:0,y:0})==0 for q in U),'velocity origin')
strain=s.diff(psicart,x,y).subs({x:0,y:0});beta=s.integrate(r*(1-r*r)**6,(r,0,1))/4;check(strain==beta==s.Rational(1,56),'strain independent moment')
def l1(poly):return sum((abs(c) for mon,c in s.Poly(s.expand(poly),x,y).terms()),s.Integer(0))
S0=l1(H);S1=sum(l1(s.diff(H,q)) for q in (x,y));S2=sum(l1(s.diff(H,q,v)) for q in (x,y) for v in (x,y));DU=sum(l1(s.diff(q,v)) for q in U for v in (x,y));outside0=sum(row['stream_mode']*abs(s.Rational(row['exterior_stream_coefficient'])) for row in rows);outside1=sum(row['stream_mode']*(row['stream_mode']+1)*abs(s.Rational(row['exterior_stream_coefficient'])) for row in rows);C_H=max(DU,outside0,outside1)
polys={'H':H,'psi_inner':psicart,'U1_inner':U[0],'U2_inner':U[1]};export={name:[{'x_power':mon[0],'y_power':mon[1],'coefficient':rat(c)} for mon,c in s.Poly(poly,x,y).terms()] for name,poly in polys.items()}
alpha=s.symbols('alpha',positive=True);exponents={'G_center':s.expand(2*(2+alpha)-6+1),'G_far':s.Integer(-2),'Q_inner':s.expand(2*(2+alpha)-6+1),'Q_middle':s.expand(2*(alpha-2)-6+1),'Q_far':s.Integer(-10)}
check(exponents['G_center']==2*alpha-1 and exponents['Q_middle']==2*alpha-9,'radial exponents');check(s.expand(12+(2*alpha-9)+1)==4+2*alpha,'middle delta exponent')
pins={str(p.relative_to(D.parents[1])):sha(p) for p in (D/'PROOF.md',D/'evidence/proof_first.json',Path(__file__))};check(json.loads((D/'evidence/proof_first.json').read_text())['proof_sha256']==sha(D/'PROOF.md'),'proof first')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_SYMBOLIC_CARTESIAN_SOURCE_GREEN_INTEGRALS_AND_GRAPH_NORM_SCALING','radial_modes':rows,'cartesian_polynomials':export,'matching_jet_checks':match,'strain_exact':rat(strain),'rank_one_coefficient_exact':rat(strain/3),'polynomial_abs_coefficient_constants':{'H0':rat(S0),'H1':rat(S1),'H2':rat(S2),'DU_inner':rat(DU),'U_outer':rat(outside0),'DU_outer':rat(outside1),'C_H':rat(C_H)},'radial_integrand_exponents':{key:str(value) for key,value in exponents.items()},'files':pins,'scope':'Exact fixed compact bump and exponent checks. Background constants, exact kernel membership and actual inverse remain hypotheses; no numerical matrix or PDE endpoint.'};p=D/'evidence/compute.json';check(not p.exists(),'immutable');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'modes':[{k:r[k] for k in ('stream_mode','exterior_stream_coefficient')} for r in rows],'strain':out['strain_exact'],'constants':out['polynomial_abs_coefficient_constants']}))
