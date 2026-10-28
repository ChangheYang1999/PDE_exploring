from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import ast,hashlib,json,math
from flint import arb,fmpq,ctx
ctx.prec=192
p=Path(__file__).resolve().parents[1]
snap=p/'code_snapshot'
# Isolated exact function definitions: no imports of pipeline drivers or data loads.
ns={'fmpq':fmpq}
def extract(filename,names):
 tree=ast.parse((snap/filename).read_text())
 nodes=[]
 for n in tree.body:
  if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id in {'MU_KNOTS','MU_VALS'} for t in n.targets): nodes.append(n)
  if isinstance(n,ast.FunctionDef) and n.name in names: nodes.append(n)
 exec(compile(ast.Module(body=nodes,type_ignores=[]),filename,'exec'),ns)
extract('section_l2.py',{'mu_prime_at','mu_at','angular_matrix'})
extract('margin.py',{'mu_prime_values_on'})
knots=[Q(3,2),Q(7,4),Q(3),Q(4),Q(5),Q(6),Q(7),Q(8),Q(9),Q(10)]
slopes=[Q(i,16) for i in (4,17,28,27,25,18,4,-10,-17,-19,-20)]
def mu_ref(t):
 if t<=0:return t/4
 b=[Q(0)]+[k for k in knots if k<t]+[t]
 out=Q(0)
 for a,z in zip(b,b[1:]):
  n=sum(k<=a for k in knots)
  out+=(z-a)*slopes[n]
 return out
for v in [Q(-100),Q(0),Q(3,2),Q(13,8),Q(7,4),Q(2),Q(3),Q(5),Q(19,2),Q(10),Q(12)]:
 assert Q(str(ns['mu_at'](fmpq(v.numerator,v.denominator))))==mu_ref(v)
for j,k in enumerate(knots):
 got={Q(str(x)) for x in ns['mu_prime_values_on'](fmpq(k.numerator,k.denominator),fmpq(k.numerator,k.denominator))}
 assert got=={slopes[j],slopes[j+1]}
# Real Fourier product: Phi_m=(sin(theta)+sin(3theta))*cos(2m theta)/4.
# Its sine coefficients are exact rationals; orthogonality gives Gram/pi.
def phi(m):
 d={}
 for n in (1,3):
  for l in (n+2*m,n-2*m):
   if l:
    d[abs(l)]=d.get(abs(l),Q(0))+Q(1 if l>0 else -1,8)
 return {n:c for n,c in d.items() if c}
gram=ns['angular_matrix'](8)
for m in range(8):
 for n in range(8):
  expected=sum(c*phi(n).get(j,Q(0)) for j,c in phi(m).items())
  assert Q(str(gram[m][n]))==expected
# Interval squaring and quantitative conversion counterexamples.
r=arb(0,1)
bad=(r*r+r*r).sqrt()
assert str(bad)=='nan'
assert str(r**2)=='nan'
a=arb(1)/2;b=a+arb(2)**-55
assert b>a and float(a.upper())==float(b.upper())==0.5
chosen=b if float(b.upper())>float(a.upper()) else a
assert chosen<b
small=arb(2)**-1200
assert small>0 and float(small.upper())==0
v=arb(1)+arb(2)**-54
assert arb(float(v.upper()))<v
# Final multiplicative inflation cannot rescue a squared underflow.
z=math.ldexp(1.,-600)
assert z>0 and z*z==0 and z*z*(1+1e-8)==0
# Outward endpoint conversion repairs these scalar examples.
for x in [v,b,small,-v]:
 assert arb(math.nextafter(float(x.upper()),math.inf))>=x.upper()
 assert arb(math.nextafter(float(x.lower()),-math.inf))<=x.lower()
# Missing velocity term for rho=r^3 sin(29theta): coefficients of r^-3 (-x,y).grad rho.
l=29
missing={l+2:Q(l-3,2),l-2:-Q(l+3,2)}
assert missing=={31:Q(13),27:Q(-16)}
assert all((n-1)//2>11 for n in missing)
res={'date':datetime.now(timezone.utc).isoformat(),'result':'PASS','scope':'exact weight and angular Gram checks; installed-Arb and IEEE-float counterexamples; exact omitted-mode identity',
 'interval_gradient_result':str(bad),'row_max_selected':str(chosen),'row_max_required':str(b),'float_underflow_example':'2^-1200 -> 0',
 'missing_velocity_modes':{str(n):str(c) for n,c in missing.items()},
 'files':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(snap.glob('*.py'))}}
(p/'evidence/check.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({k:v for k,v in res.items() if k!='files'},indent=2))
