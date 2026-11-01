"""Exact rational-endpoint replay of every Q10 lower-bound inequality."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import gzip,json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import fmpq,fmpq_poly
ROOT=Path('research/285_period_ten_response_bounds')
BASE=Path('research/282_period_ten_symbolic_response/verification')
def now():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def ref(p):return dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest())
def read(p):return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())
def poly(c):return fmpq_poly([fmpq(v) for v in c])
def ev(p,I):
 a=b=F(0);lo,hi=I
 for c in reversed(list(p)):
  ends=(a*lo,a*hi,b*lo,b*hi);v=F(str(c));a,b=min(ends)+v,max(ends)+v
 return a,b

def main():
 start=time.monotonic();source=ROOT/'verification/checks.json.gz';data=read(source);assert data['all_checks_pass'] and data['Q']==10 and len(data['rows'])==14
 for r in data['inputs']:assert ref(Path(r['path']))['sha256']==r['sha256']
 gen=read(BASE/'reduced_generic.json.gz');N=list(map(poly,gen['numerator_by_b_degree']));D=poly(gen['denominator']);d=D.degree()
 smalls={r['k']:poly(r['coefficients']) for r in read(BASE/'small_responses.json.gz')['small']};roots=read(Path('research/281_period_ten_finite_algebra/verification/obstruction_checks.json'))['real_roots'];shifts={};rows=[]
 for row,root in zip(data['rows'],roots):
  assert row['root_interval']==root['interval'];I=tuple(map(F,row['root_interval']));s=F(row['s']);assert s>0 and s==F(2)**row['s_power'];K=row['K'];e=row['tail_sign'];assert e in [-1,1] and K>=21
  if K not in shifts:
   arg=fmpq_poly([K,1]);shifts[K]=([p(arg) for p in N],D(arg))
  ns,ds=shifts[K];assert ds.degree()==d and all(v>0 for v in ds)
  positive=zero=0;least=None
  for j in range(d+1):
   p=fmpq_poly([e*c[j]-(fmpq(s.numerator,s.denominator)*ds[j] if m==0 else 0) for m,c in enumerate(ns)])
   lo,hi=ev(p,I)
   if not p:zero+=1;assert j!=0
   else:assert lo>=0 and (j!=0 or lo>0),('tail',row['root_index'],j);positive+=1;least=lo if least is None else min(lo,least)
  assert len(row['finite_checks'])==K-2
  for item,k in zip(row['finite_checks'],range(2,K)):
   assert item['k']==k and item['sign'] in [-1,1]
   if k<21:p=smalls[k]
   else:
    den=D(k);assert den>0;p=fmpq_poly([c(k)/den for c in N])
   lo,hi=ev(item['sign']*p,I);assert lo>s,('finite',row['root_index'],k)
  result=dict(root_index=row['root_index'],s=str(s),K=K,positive_tail_coefficients=positive,zero_tail_coefficients=zero,positive_denominator_coefficients=d+1,finite_comparisons=K-2,least_tail_coefficient_lower=str(least));rows.append(result)
  print(json.dumps(dict(at=now(),root=row['root_index'],s=str(s),K=K,elapsed_s=time.monotonic()-start)),flush=True)
 out=dict(checked_at_utc=now(),all_checks_pass=True,method='Exact Fraction endpoint Horner arithmetic; exact fmpq polynomial shifts reconstructed from source.',rows=rows,source=ref(source),inputs=data['inputs'],actual_elapsed_s=time.monotonic()-start)
 raw=json.dumps(out,separators=(',',':')).encode();(ROOT/'verification/replay.json.gz').write_bytes(gzip.compress(raw,mtime=0));(ROOT/'sources/period_ten_response_bounds_replay.py').write_bytes(Path(__file__).read_bytes());print(json.dumps(dict(at=now(),complete=True,elapsed_s=out['actual_elapsed_s'])),flush=True)
if __name__=='__main__':
 try:main()
 except Exception as exc:
  d=dict(at=now(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(x.filename).name,line=x.lineno) for x in traceback.extract_tb(exc.__traceback__)]);(ROOT/'verification/replay_FAILURE.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d),flush=True);raise SystemExit(1)
