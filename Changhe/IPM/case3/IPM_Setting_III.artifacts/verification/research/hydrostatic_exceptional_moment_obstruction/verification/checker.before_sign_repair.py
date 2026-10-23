from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,itertools
import sympy as s
R=Path('research/hydrostatic_exceptional_moment_obstruction');V=R/'verification';checks=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ck(name,value):checks.append(dict(name=name,passed=bool(value)))
def zero(name,expr):ck(name,s.cancel(s.expand(expr))==0)
x,u,v,t,z,a,b,d=s.symbols('x u v t z a b d');C=s.symbols('C',nonzero=True)
# Exact polynomial substitutions for arbitrary coefficient examples, n=1,2,4.
for m in [1,3,5,7,9,11,13]:
 for nn in [1,2,4]:
  P=s.Rational(2*nn+m,2);N=P-s.Rational(1,2);ss=1+x*x;q=1+2*P*x*x
  fs=[s.Integer((-1)**j*(j+2))for j in range((m+1)//2)]
  if sum(fs)==0:fs[0]+=1
  F=sum(fs[j]*t**(2*j+1)for j in range(len(fs)));psi=s.expand(sum(fs[j]*x**(2*j+1)*ss**((m-1)//2-j)for j in range(len(fs))))
  zero(f'{m},{nn} Yprime',s.diff(C*x*ss**N,x)-C*ss**(N-1)*q)
  ck(f'{m},{nn} exact degree',s.degree(psi,x)==m);zero(f'{m},{nn} leading',psi.coeff(x,m)-F.subs(t,1))
  zero(f'{m},{nn} at i',psi.subs(x,s.I)-fs[-1]*s.I**m);ck(f'{m},{nn} nonzero at i',psi.subs(x,s.I)!=0)
  # Avoid radicals: the square of the coordinate relation is rational.
  zero(f'{m},{nn} coordinate square',psi**2-(1+x*x)**m*s.expand(F**2).subs(t*t,x*x/(1+x*x)))
# Critical-condition reduction with arbitrary roots, independent polynomial expansion.
for e in range(5):
 roots=[s.Rational(-j-2,j+3)for j in range(e+1)];RR=x*s.prod(x*x-uk for uk in roots)
 for nn in [1,3]:
  m=2*e+3;P=s.Rational(2*nn+m,2);N=P-s.Rational(1,2);us=-1/(2*P)
  bracket=s.diff(RR,x)*(1+x*x)+2*(N-1-e)*x*RR
  remainder=s.rem(bracket,x*x-us,x)
  # beta R(beta) times the root sum gives half of beta times bracket.
  identity=(1+x*x)*(1+sum(2*x*x/(x*x-uk)for uk in roots))+2*(N-1-e)*x*x
  target=2*us*sum((1+uk)/(us-uk)for uk in roots)
  zero(f'e{e}n{nn} root sum reduction',identity.subs(x*x,us)-target)
  vk=[1/(1+uk)for uk in roots];zz=1/(1+us);pi=s.prod(v-w for w in vk)
  zero(f'e{e}n{nn} transformed derivative',sum((1+uk)/(us-uk)for uk in roots)+zz*s.diff(pi,v).subs(v,zz)/pi.subs(v,zz))
# Moment expansion, including residue at zero.
for count in range(1,6):
 roots=[s.Rational(j+2,j+3)for j in range(count)];weights=[s.Integer(2*j+2)for j in range(count)];aa=s.Integer(3)
 # u roots recovered from v roots.
 g=aa/u+sum(w/(u-(1/vk-1))for vk,w in zip(roots,weights))
 for ell in range(1,6):
  coeff=s.diff(g,u,ell-1).subs(u,-1)/s.factorial(ell-1)
  zero(f'moment {count},{ell}',coeff+aa+sum(w*vk**ell for vk,w in zip(roots,weights)))
# e=1 exact factorization, no solving or root approximation assumptions.
v1=(-a-2*d*z)/(b-d);v2=(a+2*b*z)/(b-d);mm=a+b+d
zero('e1 linear sum',v1+v2-2*z);zero('e1 first moment',a+b*v1+d*v2)
expr=s.factor((b-d)**2*((a+b*v1**2+d*v2**2)*z+mm*v1*v2))
factor=(a+(b+d)*z)*(a*mm-4*b*d*z*(z-1))
# Determine the displayed sign exactly rather than silently accepting proportionality.
zero('e1 displayed factorization',expr-factor)
# Completed square with arbitrary symbols.
S=-(a+b*x)/d;T=(a+b*x*x+d*S*S)/(2*d);pi=(v-x)*(v*v-S*v+T)
square=b*(b-d)/(2*d*d)*(x+(a+2*d*z)/b)**2+(1+2*d/b)*z*z+2*a*z/b+a/(2*d)+a*a/(2*b*d)
zero('e2 completed square',s.diff(pi,v).subs(v,z)-square)
zero('e2 first moment',a+b*x+d*S);zero('e2 second moment',a+b*x*x+d*(S*S-2*T))
for aa in [1,3,5]:
 for bb,dd in [(4,2),(6,2),(6,4),(10,2)]:
  for xx,zz in itertools.product([-10,-1,0,2,10],[s.Rational(101,100),s.Rational(7,6),2,10]):
   ck(f'square positive {aa},{bb},{dd},{xx},{zz}',square.subs({a:aa,b:bb,d:dd,x:xx,z:zz})>0)
# Newton formal-series coefficients independently expanded from the truncated log.
for e in range(1,8):
 for aa in [s.Rational(1,2),s.Rational(3,4),1,3]:
  log=sum(aa*t**ell/ell for ell in range(1,e+1));series=s.series(s.exp(log),t,0,e+1).removeO().expand()
  for ell in range(e+1):
   zero(f'equal e{e}a{aa}l{ell}',series.coeff(t,ell)-s.rf(aa,ell)/s.factorial(ell));ck(f'equal positive e{e}a{aa}l{ell}',series.coeff(t,ell)>0)
# Exhaustive positive integer multiplicity enumeration through degree9, independent of lead scan.
enumeration=[]
def partitions(total,length,lower=1):
 if length==0:
  if total==0:yield ()
  return
 for first in range(lower,total//length+1):
  for tail in partitions(total-first,length-1,first):yield(first,)+tail
for m in [5,7,9]:
 for e in range((m-3)//2+1):
  for aa in range(1,m,2):
   for mu in partitions((m-aa)//2,e+1):
    if e<=1:reason='e<=1'
    elif len(set(mu))==1:reason='equal'
    elif e==2 and mu[0]==mu[1]<mu[2]:reason='unique heavier'
    else:reason='OPEN'
    enumeration.append(dict(m=m,e=e,A0=aa,mu=mu,reason=reason));ck(f'enumeration {m},{e},{aa},{mu}',reason!='OPEN')
# Degree-nine specialization: manifestly positive discriminant-free formula.
zero('m9 pi prime',s.diff(pi,v).subs({v:z,a:1,b:4,d:2})-(3*z*z+(1+2*x)*z+x*x+x/2+s.Rational(3,8)))
# Hash dependency253 with its actual algebra/review gates.
dep=Path('research/hydrostatic_axis_zero_order_obstruction');ck('253 immutable proof',sha(dep/'PROOF.md')=='0ecb179f081fbc490fdc36fb16f459ffe9a1aa0fa38976c43b406b97b23b79b9')
for name in ['CHECKS.json','REVIEW_CHECKS.json']:
 data=json.loads((dep/'verification'/name).read_text());ck('253 '+name+' pass',data['status']=='PASS');ck('253 '+name+' all',all(q['passed']for q in data['checks']))
manifest=json.loads((V/'INPUTS.json').read_text());ck('lead frozen hash',sha(Path(manifest['frozen']))==manifest['sha256'])
out=dict(status='PASS'if all(q['passed']for q in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,enumeration=enumeration,proof_sha256=sha(R/'PROOF.md'),driver_sha256=sha(Path(__file__)),lead_notes_sha256=manifest['sha256'])
(V/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count']);print([q for q in checks if not q['passed']])
if out['status']!='PASS':raise SystemExit(1)
