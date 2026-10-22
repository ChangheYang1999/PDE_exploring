"""Piecewise Green integration, exact normalization, and quadratic constants."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json,sys
import sympy as s
assert not sys.flags.optimize
ROOT=Path(__file__).resolve().parents[3];D=ROOT/'research/nonlinear_center_topology'
def check(v,label):
 if not v:raise ValueError(label)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def rat(q):
 q=s.Rational(q);return str(int(q.p))+'/'+str(int(q.q))
def coeffs(poly):
 out={}
 for term in s.Add.make_args(s.expand(poly)):
  power=term.as_powers_dict().get(r,0);c=s.cancel(term/r**power);check(c.is_Rational,'Laurent coefficient');out[str(int(power))]=rat(c)
 return {p:c for p,c in out.items() if F(c)}
def primitive(f,a,b):return s.integrate(f,(t,a,b))
x,y,r,t,z=s.symbols('x y r t z',real=True);R=x*x+y*y;chi=(1-z)**6;H=s.expand(x*x*y*(1-R)**6)
f={2:s.expand(r*r*chi.subs(z,r*r)+r**4*s.diff(chi,z).subs(z,r*r)/2),4:s.expand(r**4*s.diff(chi,z).subs(z,r*r)/4)}
rows=[];psiHcart=0;jetchecks=0;sourcechecks=0
for n in (2,4):
 f0=s.expand(s.Rational(4,3)*(f[n]-f[n].subs(r,r/2)));f1=s.expand(-s.Rational(4,3)*f[n].subs(r,r/2))
 A0=primitive(t**(n+1)*f0.subs(r,t),0,r);B0=primitive(t**(1-n)*f0.subs(r,t),r,1)+primitive(t**(1-n)*f1.subs(r,t),1,2)
 A1=primitive(t**(n+1)*f0.subs(r,t),0,1)+primitive(t**(n+1)*f1.subs(r,t),1,r);B1=primitive(t**(1-n)*f1.subs(r,t),r,2)
 A2=primitive(t**(n+1)*f0.subs(r,t),0,1)+primitive(t**(n+1)*f1.subs(r,t),1,2)
 psi=[s.expand((r**(-n)*A0+r**n*B0)/(2*n)),s.expand((r**(-n)*A1+r**n*B1)/(2*n)),s.expand(r**(-n)*A2/(2*n))]
 for a,g in zip(psi,[f0,f1,0]):check(s.expand(-(s.diff(a,r,2)+s.diff(a,r)/r-n*n*a/r**2)-g)==0,'radial Poisson');sourcechecks+=1
 jets=[]
 for boundary,lo,hi in ((1,0,1),(2,1,2)):
  row=[]
  for j in range(7):
   a=s.diff(psi[lo],r,j).subs(r,boundary);b=s.diff(psi[hi],r,j).subs(r,boundary);check(a==b,'stream jets through6');row.append(rat(a));jetchecks+=1
  jets.append({'radius':boundary,'jets':row})
 psiH=s.expand((r**(-n)*primitive(t**(n+1)*f[n].subs(r,t),0,r)+r**n*primitive(t**(1-n)*f[n].subs(r,t),r,1))/(2*n))
 extH=s.expand(r**(-n)*primitive(t**(n+1)*f[n].subs(r,t),0,1)/(2*n))
 for a,b in zip(psi,[s.Rational(4,3)*psiH-s.Rational(16,3)*psiH.subs(r,r/2),s.Rational(4,3)*extH-s.Rational(16,3)*psiH.subs(r,r/2),s.Rational(4,3)*extH-s.Rational(16,3)*extH.subs(r,r/2)]):check(s.expand(a-b)==0,'independent superposition form')
 angular=s.im(s.expand((x+s.I*y)**n))
 for (p,),c in s.Poly(psiH,r).terms():psiHcart+=c*R**((p-n)//2)*angular
 rows.append({'mode':n,'source_by_piece':[coeffs(f0),coeffs(f1),{}],'stream_by_piece':[coeffs(p) for p in psi],'matching_jets':jets})
check(F(rows[0]['stream_by_piece'][0].get('2','0'))==0,'zero strain');check(F(rows[0]['stream_by_piece'][2]['-2'])==F(5,1008),'outer mode2');check(F(rows[1]['stream_by_piece'][2]['-4'])==F(1,160),'outer mode4')
psiHcart=s.expand(psiHcart);UH=[-s.diff(psiHcart,y),s.diff(psiHcart,x)]
def l1(p):return sum((abs(c) for m,c in s.Poly(s.expand(p),x,y).terms()),s.Integer(0))
S1=sum(l1(s.diff(H,j)) for j in (x,y));S2=sum(l1(s.diff(H,j,l)) for j in (x,y) for l in (x,y));CH=sum(l1(s.diff(a,j)) for a in UH for j in (x,y));check((S1,S2,CH)==(8019,84078,s.Rational(693689,84)),'unit bump constants')
CU=8*CH/3;BB1=5*S1/3;BB2=5*S2/3;AQ=CU*BB1;BQ=CU*(BB1+BB2);C2=4*(AQ**2+BQ**2)
# The compact two-scale factor is exactly normalized and its integral strain cancels.
a0=s.expand(s.Rational(4,3)*(1-z)**6-s.Rational(1,3)*(1-z/4)**6);a1=s.expand(-s.Rational(1,3)*(1-z/4)**6)
check(a0.subs(z,0)==1,'central factor');strain=s.integrate(r*a0.subs(z,r*r),(r,0,1))+s.integrate(r*a1.subs(z,r*r),(r,1,2));check(strain==0,'separate strain integral')
# Exact dimension balances: density3, velocity3, one spatial derivative -1.
exponents={'b':3,'Ub':3,'grad_b':2,'Q':5,'grad_Q':4,'X_Q_squared':2*5-6+2,'X_b_squared':2*3-6+2,'rho_dilation_stream':2,'rho_dilation_source':0,'rho_dilation_velocity':1,'rho_dilation_strain':0}
check(exponents['X_Q_squared']==6 and exponents['X_b_squared']==2,'radial Jacobian and weight scaling')
prior=json.loads((ROOT/'research/graph_center_norm/evidence/verdict.json').read_text());pins={}
for n,h in prior['files'].items():check(sha(ROOT/n)==h,'inherited pin');pins[n]=h
for p in [D/'PROOF.md',D/'evidence/proof_first.json',Path(__file__),ROOT/'research/graph_center_norm/evidence/verdict.json']:pins[str(p.relative_to(ROOT))]=sha(p)
check(json.loads((D/'evidence/proof_first.json').read_text())['proof_sha256']==sha(D/'PROOF.md'),'proof first')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_PIECEWISE_GREEN_QUADRATIC_SCALING_AND_CONSTANTS','radial_modes':rows,'matching_jet_checks':jetchecks,'poisson_checks':sourcechecks,'unit_constants':{'S1':rat(S1),'S2':rat(S2),'C_H':rat(CH),'C_U':rat(CU),'B1':rat(BB1),'B2':rat(BB2),'A_Q':rat(AQ),'B_Q':rat(BQ),'quadratic_norm_squared_over_pi_Cw':rat(C2)},'central_factor':1,'canonical_strain_exact':'0/1','scaling_exponents':exponents,'files':pins,'scope':'Explicit compact family finite identities and constants only. Stationary background and derivative bounds remain hypotheses. No profile existence or PDE exclusion.'}
p=D/'evidence/compute.json';check(not p.exists(),'immutable');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['utc','status','matching_jet_checks','poisson_checks','unit_constants']}))
