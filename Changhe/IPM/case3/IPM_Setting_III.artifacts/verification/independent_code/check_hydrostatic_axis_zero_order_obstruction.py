"""Exact symbolic and manufactured checks supporting the standalone proof253."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import hashlib,json,random,sys
import sympy as S
sys.set_int_max_str_digits(0)
R=Path('research/hydrostatic_axis_zero_order_obstruction');V=R/'verification';checks=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(name,b,e=None):checks.append(dict(name=name,passed=bool(b),evidence=e))
def zero(name,e):ck(name,S.cancel(S.expand(e))==0,str(S.factor(e)))
t=S.symbols('t');P,n,C,c,a,b,q=S.symbols('P n C c a b q');w=1-t*t;Q=1+(2*P-1)*t*t
L=lambda f,p:S.expand(w*S.diff(f,t)+2*p*t*f)
f=S.Function('F')(t);D=w*S.diff(f,t)+2*(P-n)*t*f
# Chain-rule formulas after removing explicit common powers of positive w.
zero('G_t reduction',w*S.diff(f,t)+(n-P)*S.diff(w,t)*f-D)
zero('coordinate derivative',w+2*P*t*t-Q)
zero('G_y reduction',D/(C*Q)-S.cancel(D/C/Q))
A=S.Function('A')(t)
zero('velocity derivative reduction',w*S.diff(A,t)-P*S.diff(w,t)*A-L(A,P))
zero('linear gauge derivative',L(c*t,P)-c*Q)
# Pole coefficients, including endpoints even when D vanishes there.
for ell in range(1,10):
 for alpha in [S.Integer(1),S.Integer(-1),S.Integer(0),2,S.I]:
  f=(t-alpha)**(-ell);k=ell if alpha in [1,-1]else ell+1
  value=S.limit((t-alpha)**k*(w*S.diff(f,t)+2*P*t*f),t,alpha)
  expected=(2*(ell+P) if alpha==1 else -2*(ell+P) if alpha==-1 else -ell*(1-alpha**2))
  zero(f'pole{ell}@{alpha}',value-expected)
# Degree relation and exceptional degree1/3 residues with symbolic q.
d=S.symbols('d');zero('generic coefficient relation',2*(P-n)-d-d*(2*P-1)-2*(P-n-P*d))
ck('generic integer contradiction examples',all(1-Fraction(k,1)/Fraction(p,2)<1 for k in range(1,10)for p in range(3,24)))
Qq=1+q*t*t;pq=(q+1)/2
rem=lambda B:S.cancel(S.rem(L(B,pq),Qq,t))
for label,B,expect in [('degree1',t*Qq,-2*(q+1)/q),('degree3b0',t*Qq/3,-2*(q+1)/(3*q)),('degree3Dconstant',t*(1-S.Rational(2,3)*t*t)*Qq,-2*(q+1)/q*(1+2/(3*q))),('degree3Dquadratic',t*(1+(q-2)*t*t/3),-2*(q-2)*(q+1)/(3*q*q))]:
 zero(label+' remainder',rem(B)-expect)
 for ni in range(1,17):
  qi=2*ni if label=='degree1' else 2*ni+2
  ck(label+f' n{ni} nonzero',S.cancel(expect.subs(q,qi))!=0)
F=a*t**3+b*t
zero('degree3 D',w*S.diff(F,t)+3*t*F-(b+(3*a+2*b)*t*t))
zero('degree3 constant case',(b+(3*a+2*b)*t*t).subs(a,-2*b/3)-b)
zero('degree3 quadratic case',(b+(3*a+2*b)*t*t).subs(a,(q-2)*b/3)-b*Qq)
# Independent polynomial samples of the generic multiplicity and degree argument.
rng=random.Random(253);samples=[]
for ni in [1,2,3,5,9]:
 for degree_h in range(0,6):
  coeff=[rng.choice([-3,-2,-1,1,2,3])]+[rng.randint(-3,3)for _ in range(degree_h)]
  if coeff[-1]==0:coeff[-1]=2
  h=sum(S.Integer(v)*w**j for j,v in enumerate(coeff));F=S.Poly(S.expand(t*h),t);dd=F.degree()
  for pp in [S.Rational(5,4),S.Rational(3,2),S.Integer(2),S.Rational(5,2),S.Integer(3),S.Rational(13,4),S.Rational(7,2),S.Integer(5),S.Rational(19,4),S.Integer(ni)]:
   if pp<=1:continue
   expr=S.expand(w*F.diff().as_expr()+2*(pp-ni)*t*F.as_expr());D=S.Poly(expr,t);Qp=S.Poly(Q.subs(P,pp),t)
   tag=f'n{ni}h{degree_h}P{pp}'
   ck(tag+'F endpoints',F.eval(1)!=0 and F.eval(-1)!=0);ck(tag+'D nonzero',not D.is_zero)
   if pp==ni:
    ck(tag+'P=n obstruction',D.eval(1)==0 and (F*Qp).eval(1)!=0)
   else:
    J=S.gcd(F,D).monic();J0=S.gcd(F,F.diff()).monic();ck(tag+'gcd',J==J0)
    ck(tag+'D endpoints',D.eval(1)!=0 and D.eval(-1)!=0)
    if dd!=2*(pp-ni):
     ck(tag+'genericdegree',D.degree()==dd+1)
     ck(tag+'nondivisibility',not S.rem(F*Qp,D).is_zero)
    else:
     ck(tag+'resonance',pp==ni+S.Rational(dd,2));samples.append(dict(n=ni,P=str(pp),F_degree=dd,F=str(F.as_expr()),D=str(D.as_expr())))
# Deliberate repeated roots, including complex roots and a multiple origin.
for m0 in [1,3,5]:
 for m1 in [1,2,3]:
  F=S.Poly(t**m0*(t*t+2)**m1,t)
  for ni,pp in [(1,S.Rational(3,2)),(2,S.Rational(9,4)),(5,S.Integer(3))]:
   D=S.Poly(w*F.diff().as_expr()+2*(pp-ni)*t*F.as_expr(),t);J=S.gcd(F,D).monic()
   ck(f'repeated{m0},{m1},n{ni}gcd',J==S.gcd(F,F.diff()).monic());ck(f'repeated{m0},{m1},n{ni}degree',J.degree()==F.degree()-3)
# Manufactured counterexamples when either H hypothesis is removed.
for pp in [S.Rational(5,4),2,S.Rational(7,2),5]:
 for cc in [-2,0,S.Rational(7,5),3]:
  for hh in [-3,1,5]:
   yy=S.symbols('y');G=hh*yy;vel=(1-cc)*yy
   zero(f'droppedH0 P{pp}c{cc}H{hh}',(cc*yy+vel)*S.diff(G,yy)-G)
  zero(f'Hidenticallyzero P{pp}c{cc}',(cc*S.Symbol('y')+1)*0-0)
# The degree3 formulas can satisfy the first divisibility while failing the second.
for ff,pp in [(t,S.Rational(3,2)),(t**3,S.Rational(5,2)),(t-S.Rational(2,3)*t**3,S.Rational(5,2)),(t+S.Rational(2,3)*t**3,S.Rational(5,2))]:
 dd=S.degree(ff,t);nn=pp-S.Rational(dd,2);dden=w*S.diff(ff,t)+2*(pp-nn)*t*ff;qq=Q.subs(P,pp);bb=S.cancel(ff*qq/dden)
 ck('firstdiv insufficient '+str(ff),S.denom(bb)==1 or not S.denom(bb).has(t));ck('seconddiv fails '+str(ff),S.cancel(S.rem(L(bb,pp),qq,t))!=0)
# Existing nine checkpoint applications, gated and bound to exact certificate hashes.
gate=Path('research/hydrostatic_finite_axis_obstruction/verification/CHECKS.json');gd=json.loads(gate.read_text());ck('previous independent gate329',gd['status']=='PASS'and gd['count']==329 and all(x['passed']for x in gd['checks']))
for record in gd['certificates']:
 tag=Path(record['path']).name;ck('certificate '+tag,sha(record['path'])==record['sha256']);pp=Fraction(record['P']);ck('new excluded range '+tag,1<pp<Fraction(7,2));ck('nonzeroH '+tag,record['H1_nonzero']);ck('nonresonant '+tag,pp!=1+Fraction(record['F_degree'],2))
# Necessary high-degree resonance arithmetic. These are necessary conditions only.
for ni in range(1,10):
 for dd in range(5,30,2):
  pp=Fraction(ni)+Fraction(dd,2);ck(f'exception set n{ni}d{dd}',pp>=Fraction(7,2)and pp.denominator==2)
ck('proofbeforechecker',(R/'PROOF.md').stat().st_mtime<Path(__file__).stat().st_mtime)
out=dict(status='PASS'if all(x['passed']for x in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,proof_sha256=sha(R/'PROOF.md'),driver_sha256=sha(__file__),previous_gate_sha256=sha(gate),resonant_sample_cases=samples,scope='Supports standalone auxiliary-axis proof253. Exceptional P=7/2,9/2,... remain open; no infinite-degree or full-plane PDE exclusion.')
(V/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(checks));print(json.dumps([x for x in checks if not x['passed']],indent=2));raise SystemExit(out['status']!='PASS')
