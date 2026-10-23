from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as s
R=Path('research/hydrostatic_axis_resonant_root_obstruction');V=R/'verification'
checks=[]
def ck(name,cond,evidence=''):
 checks.append(dict(name=name,passed=bool(cond),evidence=str(evidence)))
def zc(name,expr):ck(name,s.simplify(expr)==0,expr)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
prev=Path('research/hydrostatic_axis_zero_order_obstruction')
for f,count in [('CHECKS.json',2036),('REVIEW_CHECKS.json',33)]:
 a=json.loads((prev/'verification'/f).read_text());ck(f+'PASS',a['status']=='PASS');ck(f+'count',a['count']==len(a['checks'])==count);ck(f+'all',all(x['passed']for x in a['checks']));ck(f+'proof',a['proof_sha256']==sha(prev/'PROOF.md'))
t,z=s.symbols('t z',real=True);q=s.symbols('q',positive=True);d,n=s.symbols('d n',positive=True);w=1-t*t;Q=1+q*t*t;P=(q+1)/2
L=lambda f:s.expand(w*s.diff(f,t)+(q+1)*t*f)
A,B=s.symbols('A B',real=True)
zc('cubic remainder',s.rem(L(A*t**3+B*t),Q,t)+2*A*(q+1)/q**2)
zc('linear remainder',s.rem(L(t),Q,t))
zc('constant quotient remainder',s.rem(L((A*t**3+B*t)*Q),Q,t)+2*(q+1)*(B-A/q)/q)
zc('resonant squarefree remainder relation',w*s.diff(A*t**3+B*t,t)+2*(n+d/2)*t*(A*t**3+B*t)-(w*s.diff(A*t**3+B*t,t)+d*t*(A*t**3+B*t))-2*n*t*(A*t**3+B*t))
examples=[t,t**3,t**5,t*(t*t+2),t*(t*t+2)**2,t**3*(t*t+2),t*(t**4+t*t+1)**2,t*(t*t-2)**2,t**3*(t**4+1)**3,t*(t*t+2)**2*(t*t+3)**3,t*(t*t+s.Rational(1,7))**3*(t**4+2*t*t+3)]
for j,F in enumerate(examples):
 dd=s.degree(F,t);D=s.expand(w*s.diff(F,t)+dd*t*F);J=s.polys.polytools.terms_gcd(s.gcd(F,s.diff(F,t)))
 J=s.Poly(J,t).monic().as_expr();S=s.cancel(F/J);g=s.Poly(s.gcd(F,D),t).monic().as_expr()
 zc(f'{j} gcd agrees',g-J);zc(f'{j} J even',J.subs(t,-t)-J);zc(f'{j} S odd',S.subs(t,-t)+S);ck(f'{j} distinct parity',int(s.degree(S,t))%2==1);ck(f'{j} endpoint admissible',F.subs(t,1)!=0 and F.subs(t,-1)!=0)
 f=s.expand(F.subs(t,s.I*z)/s.I);zc(f'{j} imaginary real',s.im(f))
 zc(f'{j} Rolle derivative',s.diff(f,z)*(1+z*z)-dd*z*f-D.subs(t,s.I*z))
 ck(f'{j} denominator nonzero',D!=0)
 for nn in [1,2,5]:
  qq=2*nn+dd-1;QQ=1+qq*t*t;quot,rem=s.div(D,J,t);zc(f'{j}n{nn} quotient even',quot.subs(t,-t)-quot)
  if s.rem(QQ,quot,t)==0:
   ck(f'{j}n{nn} quotient degree',s.degree(quot,t)in[0,2])
   bb=s.cancel(F*QQ/D);ck(f'{j}n{nn} transport obstruction',s.rem(s.expand(w*s.diff(bb,t)+(qq+1)*t*bb),QQ,t)!=0)
# Arbitrary odd-degree polynomial families with D=1 or D=Q.
for dd in range(1,20,2):
 for nn in [1,2,5,11]:
  qq=s.Integer(2*nn+dd-1);QQ=1+qq*t*t
  for kind in ['constant','quadratic']:
   if kind=='quadratic' and dd==1:continue
   co={1:s.Integer(1)}
   for power in range(3,dd+1,2):
    target=qq if power==3 and kind=='quadratic'else s.Integer(0)
    co[power]=(target-(dd-power+2)*co[power-2])/power
   F=s.expand(sum(v*t**i for i,v in co.items()));D=s.expand(w*s.diff(F,t)+dd*t*F)
   zc(f'd{dd}n{nn}{kind} D',D-(1 if kind=='constant'else QQ))
   ck(f'd{dd}n{nn}{kind} degree',s.degree(F,t)==dd)
   ck(f'd{dd}n{nn}{kind} endpoint',F.subs(t,1)!=0)
   J=s.Poly(s.gcd(F,s.diff(F,t)),t).monic().as_expr();ck(f'd{dd}n{nn}{kind} squarefree',J==1)
   ck(f'd{dd}n{nn}{kind} imaginary no root',s.rem(F,QQ,t)!=0)
   bb=s.cancel(F*QQ/D);rr=s.rem(s.expand(w*s.diff(bb,t)+(qq+1)*t*bb),QQ,t)
   ck(f'd{dd}n{nn}{kind} remainder nonzero',rr!=0)
   if kind=='quadratic':zc(f'd{dd}n{nn}{kind} remainder exact',rr-s.rem(2*nn*t*F,QQ,t))
# Multiple roots can satisfy D/J=lambda Q, but a cubic squarefree quotient still fails.
for m in [1,3,5,7]:
 for k in [1,2,3,5]:
  for nn in [1,2,5]:
   dd=m+2*k;qq=s.Integer(2*nn+dd-1);BB=s.Rational(dd,m*qq-2*k);QQ=1+qq*t*t
   F=t**m*(t*t+BB)**k;J=t**(m-1)*(t*t+BB)**(k-1);S=t*(t*t+BB);D=s.expand(w*s.diff(F,t)+dd*t*F)
   zc(f'm{m}k{k}n{nn} D quotient',D-m*BB*J*QQ)
   zc(f'm{m}k{k}n{nn} gcd',s.Poly(s.gcd(F,s.diff(F,t)),t).monic().as_expr()-J)
   ck(f'm{m}k{k}n{nn} first imaginary root beyond Q',BB>1/qq)
   zc(f'm{m}k{k}n{nn} quotient obstruction',s.rem(s.expand(w*s.diff(S,t)+(qq+1)*t*S),QQ,t)+2*(qq+1)/qq**2)
# Degree conclusion uses both odd distinct-root count and nonconstant even gcd.
for ss in [5,7,9,11]:
 for jdeg in [2,4,6,8]:
  for nn in [1,2,3]:
   dd=ss+jdeg;pp=s.Rational(2*nn+dd,2);ck(f's{ss}j{jdeg}n{nn} necessary scope',dd>=7 and pp>=s.Rational(9,2) and pp.q==2)
out=dict(status='PASS'if all(x['passed']for x in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,proof_sha256=sha(R/'PROOF.md'),driver_sha256=sha(Path(__file__)),dependency_proof_sha256=sha(prev/'PROOF.md'),scope='Finite polynomial auxiliary axis data only; remaining repeated-root half-integers OPEN.')
(V/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status'],out['count'],flush=True)
for x in checks:
 if not x['passed']:print(x,flush=True)
if out['status']!='PASS':raise SystemExit(1)
