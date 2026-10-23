from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from collections import Counter
import json,hashlib,math
import sympy as s
R=Path('research/single_exceptional_multiplicity');V=R/'verification';checks=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(name,yes,evidence=None): checks.append(dict(name=name,passed=bool(yes),evidence=evidence))
def zero(name,expr):
 z=s.cancel(expr);ck(name,z==0,str(z) if z!=0 else None)
for f in json.loads((V/'INPUTS.json').read_text())['files']:ck('frozen '+Path(f['frozen']).name,sha(f['frozen'])==f['sha256'])
for filename,count in [('dependency258_CHECKS.json',724),('dependency258_REVIEW_CHECKS.json',53)]:
 g=json.loads((V/filename).read_text());ck(filename+' status/count',g['status']=='PASS' and g['count']==count and all(x['passed'] for x in g['checks']))
g=json.loads((V/'dependency258_CHECKS.json').read_text());ck('258 proof binding',g['proof_sha256']==sha(V/'dependency258_PROOF.md'))
A,mu,nu,m,n,z,a,u,v=s.symbols('A mu nu m n z a u v')
D=m+2*n;zz=D/(D-1);T=A*D-m
av=zz*(1+2*(nu-mu)/T)
zero('exceptional node solves weighted zero',A/(zz-1)+2*(nu-mu)/(zz-av)-m/zz)
zero('T decomposition',T-((A-1)*m+2*A*n))
zero('single transformed partial fraction',1/(1/z-1-(1/v-1))-(z-z*z/(z-v)))
zero('zero-pole transformed partial fraction',1/(1/z-1)-(z-z*z/(z-1)))
# Exact finite-series coefficients from two separately implemented recurrences.
def newton_coeff(power,e):
 c=[Q(1)]
 for j in range(1,e+1):c.append(-sum(power[k-1]*c[j-k] for k in range(1,j+1))/j)
 return c
def binomial_coeff(h,a,e):
 c=[Q(1)]
 for j in range(1,e+1):c.append(c[-1]*(h+j-1)*a/j)
 return c
for AA in [1,3,7]:
 for mm in [1,2,5]:
  for gap in [1,3]:
   for aa in [Q(3,2),Q(7,3)]:
    e=8; powers=[-Q(AA,2*mm)-Q(gap,mm)*aa**l for l in range(1,e+1)]
    c=newton_coeff(powers,e);b=binomial_coeff(Q(AA,2*mm),Q(1),e);d=binomial_coeff(Q(gap,mm),aa,e)
    conv=[sum(b[j]*d[k-j] for j in range(k+1))for k in range(e+1)]
    for k in range(e+1):ck(f'series A{AA} mu{mm} gap{gap} a{aa} coefficient{k}',c[k]==conv[k] and c[k]>0)
    for ee in [1,2,4,8]:
     for zz0 in [Q(1),Q(109,108),Q(3,2)]:ck(f'derivative positive {AA},{mm},{gap},{aa},{ee},{zz0}',sum((ee+1-j)*c[j]*zz0**(ee-j)for j in range(ee+1))>0)
# Enumerate partitions independently of all external scan code.
def partitions(total,length,maximum=None):
 if length==0:
  if total==0:yield ()
  return
 if total<length:return
 if maximum is None:maximum=total
 for k in range(min(maximum,total-length+1),0,-1):
  for tail in partitions(total-k,length-1,k):yield (k,)+tail

def reason(AA,parts):
 hist=Counter(parts)
 if len(hist)==1:return 'equal'
 # Exactly one exceptional node and all remaining weights equal.
 if len(hist)==2:
  for nu0,num in hist.items():
   if num==1:
    common=next(x for x in hist if x!=nu0)
    if nu0>common:return 'higher'
    if AA>1:return 'lower-A'
    if common-nu0<=1:return 'lower-gap'
 if all(count==1 for count in hist.values()):return 'all-real-M2'
 return 'OPEN'
rows={};survivors={}
for degree in [5,7,9,11,13]:
 result=[]
 for ee in range(2,(degree-3)//2+1):
  for AA in range(1,degree-2*(ee+1)+1,2):
   for pp in partitions((degree-AA)//2,ee+1):
    ck(f'degree accounting {degree},{ee},{AA},{pp}',AA+2*sum(pp)==degree and len(pp)==ee+1 and list(pp)==sorted(pp,reverse=True))
    result.append(dict(e=ee,A=AA,mu=list(pp),reason=reason(AA,pp)))
 rows[str(degree)]=result;survivors[str(degree)]=[r for r in result if r['reason']=='OPEN']
 ck(f'all excluded degree{degree}',not survivors[str(degree)] if degree<13 else survivors[str(degree)]==[dict(e=3,A=1,mu=[2,2,1,1],reason='OPEN')])
expect11={(2,1,(3,1,1)),(2,1,(2,2,1)),(2,3,(2,1,1)),(3,1,(2,1,1,1))}
expect13={(2,1,(4,1,1)),(2,1,(3,2,1)),(2,3,(3,1,1)),(2,3,(2,2,1)),(2,5,(2,1,1)),(3,1,(3,1,1,1)),(3,1,(2,2,1,1)),(3,3,(2,1,1,1)),(4,1,(2,1,1,1,1))}
for mm,expected in [(11,expect11),(13,expect13)]:ck(f'exact unequal degree{mm} list',{(r['e'],r['A'],tuple(r['mu']))for r in rows[str(mm)]if r['reason']!='equal'}==expected)
# Counterconfiguration: rational function arithmetic, no numerical root test.
config=json.loads((V/'noninteger_configuration.json').read_text());t=s.symbols('t');f=sum(s.Integer(co)*t**j for j,co in enumerate(config['polynomial_ascending']));fp=s.Poly(s.diff(f,t),t)
ck('f derivative strictly positive on nonnegative axis',all(q>0 for q in fp.all_coeffs()) and fp.eval(0)>0)
ck('f left endpoint',f.subs(t,1)==-8964)
ck('f right endpoint',f.subs(t,s.Rational(1001,1000))==s.Rational(19356647401164749,10**12))
ck('weights and degree',config['A0']+2*sum(config['multiplicities'])==config['m']==107)
DD=107+2*t;zz=DD/(DD-1);aa=s.cancel(zz*(1-13/t));bb=-(1+18*aa)/88;cc=s.cancel(bb**2+(1+18*aa**2)/88);prod=s.cancel(bb**2+cc)
pp=(v-aa)*((v-bb)**2+cc)
zero('counter M1',1+18*aa+88*bb)
zero('counter M2',1+18*aa**2+88*(bb**2-cc))
zero('counter derivative exact quartic factor',s.diff(pp,v).subs(v,zz)-9*f/(3872*t*t*(t+53)**2))
zero('counter exceptional zero ratio',zz/(zz-aa)-t/13)
zero('counter weighted zero identity after pi prime vanishes',1/(zz-1)-26/(zz-aa)-107/zz)
M3=1+18*aa**3+88*(bb**3-3*bb*cc)
def modulo(name,expr):
 num,den=s.fraction(s.cancel(expr));rem=s.rem(s.Poly(num,t),s.Poly(f,t));ck(name,rem.is_zero,str(rem.as_expr())if not rem.is_zero else None)
 return s.factor(den)
dens={}
dens['moment3']=str(modulo('counter M3 z=107 product modulo f',M3*zz-107*aa*prod))
u1=s.cancel(1/aa-1);usum=s.cancel(2*bb/prod-2);uprod=s.cancel(1-2*bb/prod+1/prod);quad=u*u-usum*u+uprod
# Numerator over u*(u-u1)*quad from residue weights 1,18,44,44.
numg=(u-u1)*quad+18*u*quad+44*u*(u-u1)*(2*u-usum)
target=107*(1+u)**2*(u+1/DD)
for j in range(4):dens[f'g-coefficient{j}']=str(modulo(f'counter g numerator coefficient{j}',s.Poly(s.cancel(numg-target),u).nth(j)))
# Rational endpoint manufactures substantiate all strict inequalities used for eta.
for tt in [s.Rational(1),s.Rational(2001,2000),s.Rational(1001,1000)]:
 vals={k:s.cancel(q.subs(t,tt))for k,q in [('a',aa),('b',bb),('c2',cc),('z',zz),('u1',u1),('uprod',uprod)]}
 ck(f'counter node sign at {tt}',vals['a']<0 and vals['c2']>0 and vals['z']>1 and vals['u1']<-1)
 ck(f'counter gap at {tt}',13>tt)
 ck(f'counter continuous interval at {tt}',vals['z']<=s.Rational(109,108))
lo,hi=s.Rational(1),s.Rational(1001,1000)
for j in range(60):
 mid=(lo+hi)/2
 if f.subs(t,mid)<0:lo=mid
 else:hi=mid
ck('exact eta isolating refinement',f.subs(t,lo)<0<f.subs(t,hi) and 1<lo<hi<s.Rational(1001,1000))
(V/'ENUMERATION.json').write_text(json.dumps(dict(rows=rows,survivors=survivors),indent=2)+'\n')
(V/'COUNTERCONFIGURATION_CHECK.json').write_text(json.dumps(dict(polynomial=str(f),eta_interval=[str(lo),str(hi)],eta_decimal=[str(s.N(lo,25)),str(s.N(hi,25))],cleared_denominators=dens),indent=2)+'\n')
out=dict(status='PASS'if all(c['passed']for c in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,proof_sha256=sha(R/'PROOF.md'),driver_sha256=sha(Path(__file__)),input_sha256=sha(V/'INPUTS.json'),configuration_sha256=sha(V/'noninteger_configuration.json'))
(V/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count']);print([q for q in checks if not q['passed']]);raise SystemExit(out['status']!='PASS')
