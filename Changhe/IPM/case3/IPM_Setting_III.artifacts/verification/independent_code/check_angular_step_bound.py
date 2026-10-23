from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import math,json,hashlib,sys
import mpmath as mp
if sys.flags.optimize:raise RuntimeError('optimized Python refused')
ROOT=Path('verification')
if Path.cwd().resolve()!=ROOT:raise RuntimeError('wrong lane')
R=ROOT/'research/angular_step_error_bound';V=R/'verification';checks=[];records=[]
def test(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError(n)
def mf(z):
 q=F(z);return mp.mpf(q.numerator)/q.denominator
for n in range(13):
 for x in [F(0),F(1),F(-2),F(3,7)]:
  for h in [F(1,3),F(1,100),F(2)]:
   left=((x+h)**n-(x-h)**n)/(2*h)-(n*x**(n-1)if n else 0)
   right=F(0)
   if n>=3:
    for k in range(n-2):
     if k%2==0:right+=F(h*h*n*(n-1)*(n-2),4)*math.comb(n-3,k)*x**(n-3-k)*h**k*F(4,(k+1)*(k+2)*(k+3))
   test('exact Peano monomial '+str((n,str(x),str(h))),left==right)
# Exact Gaussian moments stored as pairs a+b*sqrt(pi).
I={0:(F(0),F(1,2)),1:(F(1,2),F(0))}
for n in range(2,6):I[n]=tuple(F(n-1,2)*v for v in I[n-2])
a=tuple(2*sum(F(math.comb(2,k))*I[k+1][j]for k in range(3))for j in range(2));b=tuple(sum(F(math.comb(4,k))*I[k+1][j]for k in range(5))for j in range(2))
test('exact Gaussian quadratic coefficient',a==(F(2),F(1)))
test('exact Gaussian quartic remainder constant',b==(F(9,2),F(5,2)))
test('explicit fourth derivative constant',1216*F(9,4)**5==F(1121931,16))
previous={}
for digits in [72,108]:
 with mp.workdps(digits):
  for pp in ['.1','.5','.9']:
   p=mp.mpf(pp)
   for yy in ['.001','1','3','100']:
    y=mp.mpf(yy);direct=mp.quad(lambda s:s*(1+s)**(p-2),[0,y])+y*(1+y)**(p-1)/(1-p);want=((1+y)**p-1)/(p*(1-p))
    test('kernel primitive '+str((digits,pp,yy)),abs(direct-want)<=mp.mpf('1e-60')*max(1,abs(want)),str(abs(direct-want)))
  for ee in ['.1','.01','.0001','.000001','.00000001']:
   e=mp.mpf(ee);a=1+e*e;b=2*e*e;J=mp.sqrt(mp.pi)/(2*mp.sqrt(a))*mp.exp(b*b/(4*a))*mp.erfc(b/(2*mp.sqrt(a)));closed=-mp.exp(-e*e)/a+(b/a)*mp.exp(-e*e)*J
   integral=-2*mp.quad(lambda s:s*mp.exp(-s*s-e*e*(1+s)**2),[0,1,4,mp.inf]);leading=2+mp.sqrt(mp.pi);remainder=closed+1-leading*e*e;bound=(9+5*mp.sqrt(mp.pi))/2*e**4
   test('independent Gaussian closed-integral '+str((digits,ee)),abs(closed-integral)<mp.mpf('1e-65'))
   test('Gaussian analytic remainder inequality '+str((digits,ee)),-bound<=remainder<=0)
   # Coarse proven global M, with p=.5 and epsilon0=.25, gives an independent sufficient error bound.
   M=mf(F(1121931,16));K=M/(6*mp.mpf('.75')**mp.mpf('3.5'))
   test('Gaussian global lemma strain bound '+str((digits,ee)),abs(closed+1)<=2*K*e*e)
   row=dict(digits=digits,epsilon=ee,strain=mp.nstr(closed,digits),quadratic_scaled_change=mp.nstr((closed+1)/(e*e),digits),remainder=mp.nstr(remainder,digits),remainder_bound=mp.nstr(bound,digits));records.append(row)
   if digits==72:previous[ee]=row
   else:test('Gaussian72/108 agreement '+ee,abs(mp.mpf(previous[ee]['strain'])-closed)<mp.mpf('1e-68'))
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
bindings={str(Path(p).resolve()):sha(p)for p in [__file__,R/'PROOF.md']}
d=dict(status='PASS_STEP_BOUND_SYMBOLIC_AND_GAUSSIAN_CHECKS_REVIEW_PENDING',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,records=records,scope='Proof checked by exact polynomial identities and finite Gaussian diagnostics; general theorem depends on PROOF.md hypotheses; no candidate-specific numeric enclosure.')
(V/'CHECKS.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps({k:d[k]for k in ['status','utc','count']},indent=2))
