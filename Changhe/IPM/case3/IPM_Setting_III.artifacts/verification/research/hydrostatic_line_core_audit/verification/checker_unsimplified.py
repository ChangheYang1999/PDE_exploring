"""Result211: independent symbolic identities and controlled tail checks."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time
import sympy as S
import mpmath as mp
root=Path('research/hydrostatic_line_core_audit');out=root/'verification';t0=time.monotonic();rows=[]
def save():
 report=dict(utc=datetime.now(timezone.utc).isoformat(),seconds=time.monotonic()-t0,status='PASS'if rows and all(x['passed']for x in rows)else'FAILED',checks=rows,count=len(rows),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),proof_sha256=hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),scope='Algebra, exact counterexamples, elementary tail formulas and independent quadrature controls. General theorem proved in PROOF.md; no hydrostatic solution is numerically constructed.')
 (out/'CHECKS.json').write_text(json.dumps(report,indent=2)+'\n');return report

def check(name,value,detail=None):
 rows.append(dict(name=name,passed=bool(value),detail=str(detail)if detail is not None else None))
 if not value:save();raise AssertionError((name,detail))
def zero(name,e):check(name,S.simplify(e)==0,S.simplify(e))
g,G,a,b,v,gx=S.symbols('g G a b v gx',nonzero=True)
zero('line subtraction sign',(g-a*gx)/b-G/v-((g-G)/b-a*gx/b-G*(b-v)/(b*v)))
y,x,s,p,K,Q,T,D,m,B=S.symbols('y x s p K Q T D m B',positive=True)
gam,alpha=S.symbols('gamma alpha',real=True)
zero('weighted error antiderivative',S.diff(y**(gam-2)/(2-gam),y)+y**(gam-3))
zero('excluded power tail derivative',S.diff(y**(p-1+alpha)/(1-p-alpha),y)+y**(p-2+alpha))
zero('elementary uniform moment integral',S.integrate(s/(1+s)**(S.Rational(5,2)),(s,0,S.oo))-S.Rational(4,3))
for pp in [S.Rational(1,4),S.Rational(1,3),S.Rational(2,5),S.Rational(1,2),S.Rational(3,4)]:
 for gg in [pp,(1+pp)/2]:
  check(f'power comparison {pp} {gg}',0>gg-1-pp and pp>gg-1-pp and gg-2<pp-1)
 # Reference-power inverse is finite at lower end only after multiplication by t.
 zero(f'reference inverse {pp}',y**pp/pp+y**pp/(1-pp)-y**pp/(pp*(1-pp)))
F=S.Function('F');q=S.symbols('q',real=True)
expr=x**q*F(y/x);want=x**(q-2)*(q*(q-1)*F(y/x)-2*(q-1)*(y/x)*S.diff(F(s),s).subs(s,y/x)+(y/x)**2*S.diff(F(s),s,2).subs(s,y/x))
zero('homogeneous horizontal second derivative',S.diff(expr,x,2)-want)
A=Q/(p*(1-p));A2=K*A*p*p/(1-p)
zero('axis A2 normalization',A2-K*Q/((1-p)*((1-p)/p)))
for pp in [S.Rational(1,5),S.Rational(1,3),S.Rational(2,5)]:check(f'axis c>2 remainder ordering {pp}',3*pp-2<pp-1)
# A local Taylor computation of the optional degree-d curvature formula.
f=K*y**p+Q*x*x*y**(p-2)/2+T*x**4*y**(p-4)/24
V1=-Q*x*y**(p-1)/(1-p)-T*x**3*y**(p-3)/(6*(3-p))
V2=A*y**p+T*x*x*y**(p-2)/(2*(p-2)*(3-p))
calc=S.diff((V1*S.diff(f,x)+V2*S.diff(f,y))/D,x,2).subs({x:0,y:1})
want=(-(p+2)*Q*Q/(p*(1-p))+p*K*T/((p-2)*(3-p)))/D
zero('optional smooth inverse B identity',calc-want)
z=S.symbols('z');L=2*Q*z+(-2*Q**2+m/4)*z*z
zero('c2 exponential cancellation',S.expand(S.series(S.exp(L),z,0,3).removeO()).coeff(z,2)-m/4)
# General logarithmic case before the theorem forces B=0.
G0=K*S.sqrt(y)+2*K*Q+K*(B*S.log(y)+m+B)/(4*S.sqrt(y))
v0=2*y+4*Q*S.sqrt(y)+B*S.log(y)+m
# Leading residual coefficient at order y^-1/2 vanishes; work in z=1/sqrt(y).
res=S.expand(v0*S.diff(G0,y)-G0).subs(y,z**-2)
check('c2 logarithmic axis cancellation',S.limit(res/z,z,0,dir='+')==0)
# Non-solution control: it satisfies the exact center constraint at c=2.
f=y*S.exp(-x*x-y*y);v1=x*S.exp(-x*x-y*y);v2=S.sqrt(S.pi)*(x*x-S.Rational(1,2))*S.exp(-x*x)*S.erf(y)
zero('Gaussian inverse y derivative',S.diff(v1,y)-S.diff(f,x))
zero('Gaussian divergence',S.diff(v1,x)+S.diff(v2,y))
zero('Gaussian vertical inverse second derivative',S.diff(v2,y,2)+S.diff(f,x,2))
zero('Gaussian axis normalization',S.diff(f,y).subs({x:0,y:0})-1)
zero('Gaussian passes c2 center',2+S.diff(v2,y).subs({x:0,y:0})-1)
check('Gaussian different line constants',S.simplify(S.limit(v2,y,S.oo).subs(x,1)-S.limit(v2,y,S.oo).subs(x,0))!=0)
R=(2*x+v1)*S.diff(f,x)+(2*y+v2)*S.diff(f,y)-f
check('Gaussian nonzero transport residual',abs(float(R.subs({x:0,y:1}).evalf(30)))>S.Rational(1,10))
# Zero-degree trace has B=0 but nonzero matching constant.
F0=s/S.sqrt(1+s*s)+s/(2*(1+s*s)**S.Rational(3,2))
zero('zero curvature trace derivative',S.diff(F0,s)-S.Rational(3,2)*(1+s*s)**(-S.Rational(5,2)))
q0=2*s*S.diff(F0,s)+s*s*S.diff(F0,s,2)
zero('zero curvature trace B',S.limit(s*s*q0,s,S.oo))
zero('nonzero C0 despite B0',S.integrate(-s*s*S.Rational(3,2)*(1+s*s)**(-S.Rational(5,2)),(s,0,S.oo))+S.Rational(1,2))
mp.mp.dps=70
for qq in ['-0.2','-0.3333333333333333333333333333333333333333333333333','-0.5','-0.8']:
 qq=mp.mpf(qq)
 cur=lambda t:(qq-1)*t*(1+t*t)**((qq-5)/2)*(t*t+qq-2)
 exact=(qq-1)*(mp.beta(mp.mpf('2.5'),-qq/2)+(qq-2)*mp.beta(mp.mpf('1.5'),1-qq/2))/2
 # Compactify infinity with a Jacobi-like power substitution to avoid a slow tail.
 part=mp.quad(lambda t:t*cur(t),[0,1])
 tail=mp.quad(lambda w:(cur(w**(1/qq))/qq)*w**(2/qq-1),[1,0])
 value=part+tail;err=abs(value-exact)/(1+abs(exact))
 check(f'negative-degree ordinary moment {qq}',err<mp.mpf('1e-55'),mp.nstr(err,8))
for SS in [mp.mpf(10),mp.mpf(1000),mp.mpf('1e6')]:
 # F=s/sqrt(1+s²), B=-1; exact lower primitive t³+t-asinh(S).
 z=SS/mp.sqrt(1+SS*SS);lower=z**3+z-mp.asinh(SS)
 C=lower+mp.log(SS);check(f'log finite part S={SS}',abs(C-(2-mp.log(2)))<4/SS**2,mp.nstr(C,25))
 tail=SS*mp.quad(lambda w:((1/w)*(2-1/w**2)/(1+1/w**2)**mp.mpf('2.5'))/w**2,[0,1/SS])
 check(f'log upper-tail B S={SS}',abs(tail+1)<4/SS**2,mp.nstr(tail,25))
cur0=S.lambdify(s,q0,'mpmath')
C=mp.quad(lambda t:t*cur0(t),[0,1,mp.inf]);check('B0 nonzero C0 independent complete integral',abs(C+mp.mpf('.5'))<mp.mpf('1e-60'),mp.nstr(C,40))
for xx in [mp.mpf(2),mp.mpf(7)]:
 yy=mp.mpf('1e4');SS=yy/xx
 value=mp.quad(lambda t:t*cur0(t),[0,1,SS])+SS*mp.quad(cur0,[SS,mp.inf])
 check(f'B0 V2 tends to matching constant x={xx}',abs(value+mp.mpf('.5'))<10/SS**2,mp.nstr(value,25))
# All exact text inputs stay frozen; this does not replace the line-by-line proof audit.
for inp in json.loads((out/'INPUTS.json').read_text()):check('frozen input '+Path(inp['copy']).name,hashlib.sha256(Path(inp['copy']).read_bytes()).hexdigest()==inp['sha256'])
r=save();print(r['utc'],r['status'],r['count'],'seconds',r['seconds'])
