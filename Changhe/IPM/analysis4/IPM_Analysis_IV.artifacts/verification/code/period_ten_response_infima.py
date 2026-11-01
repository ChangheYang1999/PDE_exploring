"""Global period-ten response infima by exact shifts and directed sign bounds."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import gzip,json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,fmpq,fmpq_poly,ctx
ROOT=Path('research/292_period_ten_response_infima')
BASE=Path('research/282_period_ten_symbolic_response/verification')

def now():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def ref(p):return dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size)
def read(p):return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_text())
def save(name,d):
 p=ROOT/'verification'/name;raw=json.dumps(d,separators=(',',':')).encode();p.write_bytes(gzip.compress(raw,mtime=0) if p.suffix=='.gz' else raw+b'\n')
def loadpoly(c):return fmpq_poly([fmpq(x) for x in c])
def abspoly(p,I):
 v=ev(p,I);assert v>0 or v<0,('sign unresolved',v)
 return (p,v,1) if v>0 else (-p,-v,-1)
def ev(p,I):
 y=arb(0)
 for x in reversed(list(p)):y=y*I+arb(x)
 return y
def main():
 start=time.monotonic();ctx.prec=1024
 prerequisite=read(BASE/'checks.json');assert prerequisite['all_checks_pass']
 gen=read(BASE/'reduced_generic.json.gz');small=read(BASE/'small_responses.json.gz');fac=read(BASE/'factors.json')
 rootsource=Path('research/281_period_ten_finite_algebra/verification/obstruction_checks.json');rd=read(rootsource);assert rd['all_checks_pass']
 N=[loadpoly(x) for x in gen['numerator_by_b_degree']];D=loadpoly(gen['denominator']);limit=loadpoly(fac['limit_coefficients'])
 assert len(N)==11 and D.degree()==109 and D[109]==1 and limit==fmpq_poly([p[109] for p in N])
 smalls={x['k']:loadpoly(x['coefficients']) for x in small['small']};assert set(smalls)==set(range(2,21))
 def fixed(k):
  if k in smalls:return smalls[k]
  d=D(k);assert d>0
  return fmpq_poly([p(k)/d for p in N])
 shifts={}
 def shifted(K):
  if K not in shifts:
   arg=fmpq_poly([K,1]);den=D(arg);cols=[p(arg) for p in N]
   assert den.degree()==109 and all(c>0 for c in den)
   shifts[K]=(cols,den)
  return shifts[K]
 rows=[]
 for i,rr in enumerate(rd['real_roots'],1):
  lo,hi=map(fmpq,rr['interval']);I=arb(lo).union(arb(hi))
  limpol,limvalue,tailsign=abspoly(limit,I)
  nc=[ev(fmpq_poly([col[j] for col in N]),I) for j in range(110)]
  dc=[arb(x) for x in D]
  def arbhorn(c,k):
   out=arb(0)
   for v in reversed(c):out=out*k+v
   return out
  samples={k:abs(ev(smalls[k],I)) if k<21 else abs(arbhorn(nc,k)/arbhorn(dc,k)) for k in range(2,3001)}
  samples[None]=limvalue
  targetk=min(samples,key=lambda k:float(samples[k].mid()))
  target,value,sign=abspoly(fixed(targetk),I) if targetk is not None else (limpol,limvalue,tailsign)
  if targetk is not None:assert limvalue>value
  trials=[]
  for K in [21,28,40,64,96,144,216,324,486,729,1094,1641,2462,3693]:
   if targetk is not None and K<=targetk:continue
   ns,ds=shifted(K);bounds=[];zeros=[];failed=[]
   for j in range(110):
    p=fmpq_poly([tailsign*col[j]-target[m]*ds[j] for m,col in enumerate(ns)])
    if not p:zeros.append(j);v=arb(0)
    else:
     v=ev(p,I)
     if not v>0:failed.append(j)
    bounds.append(dict(degree=j,exact_zero=not bool(p),enclosure=v.str(55)))
   trials.append(dict(K=K,failed_degrees=failed,zero_degrees=zeros))
   if not failed and not bounds[0]['exact_zero']:break
  else:raise AssertionError(('tail positivity not established',i,trials))
  assert zeros==([109] if targetk is None else [])
  finite=[]
  for k in range(2,K):
   p,v,s=abspoly(fixed(k),I)
   gap=ev(p-target,I)
   assert (k==targetk and p==target) or gap>0,('finite gap',i,k,gap)
   finite.append(dict(k=k,sign=s,modulus=v.str(55),gap=gap.str(55),candidate=(k==targetk)))
  row=dict(root_index=i,root_interval=rr['interval'],candidate_index=targetk,attained=targetk is not None,infimum=value.str(60),target_polynomial=[str(c) for c in target],tail_sign=tailsign,limit=ev(limit,I).str(60),K=K,tail_trials=trials,tail_coefficients=bounds,finite_checks=finite,proposal_sample_last_index=3000)
  rows.append(row);save('partial.json.gz',dict(rows=rows))
  print(json.dumps(dict(at=now(),root=i,K=K,candidate=targetk,infimum=value.str(30),elapsed_s=time.monotonic()-start)),flush=True)
 sources=[ref(BASE/name) for name in ['checks.json','reduced_generic.json.gz','small_responses.json.gz','factors.json']]+[ref(rootsource)]
 result=dict(at=now(),all_checks_pass=True,bits=ctx.prec,rows=rows,inputs=sources,actual_elapsed_s=time.monotonic()-start,scope='Exact global response infima at the fourteen fixed algebraic roots; not coefficient growth or sharp exterior radius.')
 save('checks.json.gz',result)
 for name in ['period_ten_response_infima.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
 print(json.dumps(dict(at=now(),complete=True,elapsed_s=result['actual_elapsed_s'])),flush=True)
if __name__=='__main__':
 try:main()
 except Exception as exc:
  d=dict(at=now(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(x.filename).name,line=x.lineno) for x in traceback.extract_tb(exc.__traceback__)])
  save('FAILURE.json',d);print(json.dumps(d),flush=True);raise SystemExit(1)
