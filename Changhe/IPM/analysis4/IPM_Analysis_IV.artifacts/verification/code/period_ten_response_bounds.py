"""Uniform Q10 response bounds by exact shifts and directed Horner tests."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import gzip,json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,fmpq,fmpq_poly,ctx
from certified_initial_majorants import endpoints
ROOT=Path('research/285_period_ten_response_bounds')
BASE=Path('research/282_period_ten_symbolic_response/verification')
def now():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def ref(p):return dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest())
def read(p):return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())
def save(name,d):
 raw=json.dumps(d,separators=(',',':')).encode();p=ROOT/'verification'/name;p.write_bytes(gzip.compress(raw,mtime=0) if p.suffix=='.gz' else raw+b'\n')
def poly(c):return fmpq_poly([fmpq(x) for x in c])
def ev(p,I):
 y=arb(0)
 for c in reversed(list(p)):y=y*I+arb(c)
 return y
def power_below(x):
 assert x>0
 e=x.numerator.bit_length()-x.denominator.bit_length();v=F(2)**e
 if v>x:e-=1;v/=2
 assert v<=x<2*v
 return v,e

def main():
 start=time.monotonic();ctx.prec=1024
 checks=read(BASE/'checks.json');assert checks['all_checks_pass']
 gen=read(BASE/'reduced_generic.json.gz');small=read(BASE/'small_responses.json.gz');fac=read(BASE/'factors.json')
 rootpath=Path('research/281_period_ten_finite_algebra/verification/obstruction_checks.json');rd=read(rootpath);assert rd['all_checks_pass'] and len(rd['real_roots'])==14
 N=list(map(poly,gen['numerator_by_b_degree']));D=poly(gen['denominator']);limit=poly(fac['limit_coefficients']);d=D.degree()
 assert len(N)==11 and all(p.degree()<=d for p in N) and D[d]==1 and limit==fmpq_poly([p[d] for p in N])
 smalls={r['k']:poly(r['coefficients']) for r in small['small']};assert set(smalls)==set(range(2,21))
 def fixed(k):
  if k in smalls:return smalls[k]
  den=D(k);assert den>0
  return fmpq_poly([p(k)/den for p in N])
 shifts={}
 def shifted(K):
  if K not in shifts:
   a=fmpq_poly([K,1]);den=D(a);assert all(c>0 for c in den)
   shifts[K]=([p(a) for p in N],den)
  return shifts[K]
 rows=[]
 for i,r in enumerate(rd['real_roots'],1):
  lo,hi=map(fmpq,r['interval']);I=arb(lo).union(arb(hi));lv=ev(limit,I);assert lv>0 or lv<0;e=1 if lv>0 else -1
  minimum=endpoints(abs(lv))[0];argmin='limit';nc=[ev(fmpq_poly([p[j] for p in N]),I) for j in range(d+1)];dc=[arb(c) for c in D]
  def horn(c,k):
   a=arb(0)
   for v in reversed(c):a=a*k+v
   return a
  for k in range(2,3001):
   v=abs(ev(smalls[k],I)) if k<21 else abs(horn(nc,k)/horn(dc,k));lower=endpoints(v)[0];assert lower>0
   if lower<minimum:minimum=lower;argmin=k
  target,exponent=power_below(minimum*F(9,10));trials=[];accepted=False
  for reduction in range(12):
   s=target/F(2)**reduction
   for K in [21,28,40,64,96,144,216,324,486,729,1094,1641,2462,3693]:
    ns,ds=shifted(K);bounds=[];failed=[]
    for j in range(d+1):
     p=fmpq_poly([e*c[j]-(fmpq(s.numerator,s.denominator)*ds[j] if m==0 else 0) for m,c in enumerate(ns)])
     v=ev(p,I);ok=(not p) or v>=0
     if not ok or (j==0 and not v>0):failed.append(j)
     bounds.append(dict(degree=j,exact_zero=not bool(p),enclosure=v.str(50)))
    trials.append(dict(K=K,s=str(s),failed_degrees=failed))
    if not failed:accepted=True;break
   if accepted:break
  assert accepted,('no tail bound',i,trials)
  finite=[]
  for k in range(2,K):
   v=ev(fixed(k),I);assert v>0 or v<0;sign=1 if v>0 else -1;gap=sign*v-arb(fmpq(s.numerator,s.denominator));assert gap>0,('finite bound',i,k,gap)
   finite.append(dict(k=k,sign=sign,modulus=abs(v).str(50),gap=gap.str(50)))
  row=dict(root_index=i,root_interval=r['interval'],s=str(s),s_power=exponent-reduction,tail_sign=e,K=K,denominator_degree=d,proposal_minimum_index=argmin,proposal_minimum_lower=str(minimum),limit=lv.str(50),trials=trials,tail_coefficients=bounds,finite_checks=finite)
  rows.append(row);save('partial.json.gz',dict(rows=rows));print(json.dumps(dict(at=now(),root=i,s=str(s),K=K,proposal_argmin=argmin,elapsed_s=time.monotonic()-start)),flush=True)
 inputs=[ref(BASE/name) for name in ['checks.json','reduced_generic.json.gz','small_responses.json.gz','factors.json']]+[ref(rootpath)]
 out=dict(at=now(),all_checks_pass=True,Q=10,bits=1024,rows=rows,inputs=inputs,actual_elapsed_s=time.monotonic()-start,scope='Uniform lower bounds; sampled minima are proposals, not certified global infima.')
 save('checks.json.gz',out);(ROOT/'sources/period_ten_response_bounds.py').write_bytes(Path(__file__).read_bytes());print(json.dumps(dict(at=now(),complete=True,elapsed_s=out['actual_elapsed_s'])),flush=True)
if __name__=='__main__':
 try:main()
 except Exception as exc:
  d=dict(at=now(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(x.filename).name,line=x.lineno) for x in traceback.extract_tb(exc.__traceback__)]);save('FAILURE.json',d);print(json.dumps(d),flush=True);raise SystemExit(1)
