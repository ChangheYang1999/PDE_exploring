"""Strict global response-minimum check using the prior complete integer cover."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import gzip,json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,ctx
from gmpy2 import mpq
from extremal_single_probe import ExtremalResponse
from pure_cartesian_ball import ball
from taylor_response_enclosure import enclose
from certified_initial_majorants import pack,endpoints
from certified_prefix_majorant import PrefixMajorant,certificate,direct_scalar
from adaptive_majorant_boxes import try_box
from unpack_dyadic4 import unpack
from resonance_block_majorant import clean
ROOT=Path('research/255_seventeen_exact_minimum')
OLD=Path('research/242_single_seventeen_six_thirteenths')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def read(row):
 raw=Path(row['path']).read_bytes();assert sha256(raw).hexdigest()==row['sha256'];d=gzip.decompress(raw) if row['path'].endswith('.gz') else raw
 if row.get('raw_sha256'):assert sha256(d).hexdigest()==row['raw_sha256']
 return json.loads(d)
def put(path,data):
 raw=json.dumps(clean(data),separators=(',',':')).encode();raw=gzip.compress(raw,mtime=0) if path.suffix=='.gz' else raw;path.write_bytes(raw)
 return dict(path=str(path),sha256=sha256(raw).hexdigest())
def main():
 start=time.monotonic();ctx.prec=1536
 rp=OLD/'verification/review.json';review=json.loads(rp.read_text());assert review['all_checks_pass']
 data=read(review['receipt']);cov=read(data['coverage']);oldbox=read(data['box']);probe=read(data['probe'])
 r=ExtremalResponse(3,13);target=abs(r.compact(ball(mpq(1,14278))));U=endpoints(target)[1];s=F(277,10**14);assert endpoints(target)[0]>s
 finite=[]
 for k in range(1,40):
  value=r.full(k);assert abs(value)>ball(mpq(str(U)));assert value.overlaps(arb(*unpack(probe['rows'][k-1]['enclosure'])))
  finite.append(dict(k=k,enclosure=pack(value)))
 leaves=[];partition=[];target_leaves=0;edge=F(1,238)
 for i,row in enumerate(cov['nodes']):
  address=row['address'];den=1<<len(address);num=int(address,2) if address else 0;a=edge*num/den;b=edge*(num+1)/den
  assert (a,b)==(F(row['a']),F(row['b']));x=(1/b+2)/6;lo=max(40,-(-x.numerator//x.denominator));hi=None
  if a:y=(1/a+2)/6;hi=y.numerator//y.denominator
  assert (lo,hi)==(row['lower'],row['upper']);status=row['status'];new=dict(row)
  if status=='empty':assert hi is not None and hi<lo
  else:
   if status=='singleton':assert lo==hi==row['k'];value=r.compact(ball(mpq(1,6*lo-2)))
   else:assert status=='interval' and row['degree']==5;value=enclose(r,a,b,degree=5)
   assert value is not None and value.overlaps(arb(*unpack(row['enclosure'])))
   if status=='singleton' and lo==2380:
    assert abs(value).overlaps(target);target_leaves+=1
   else:assert abs(value)>ball(mpq(str(U))),('minimum_gap',lo,hi,str(value),str(U))
   new['recomputed_enclosure']=pack(value)
  leaves.append(new);partition.append((a,b))
  print(json.dumps(dict(at=stamp(),stage='leaf',completed=i+1,total=len(cov['nodes']),actual_elapsed_s=time.monotonic()-start)),flush=True)
 partition.sort();assert target_leaves==1 and partition[0][0]==0 and partition[-1][1]==edge and all(x[1]==y[0] for x,y in zip(partition,partition[1:]));assert len(leaves)==cov['splits']+1
 m=PrefixMajorant(3,13,18,list(map(F,oldbox['initial_density'])),[],s,F(507,152),F(7938,169));direct_scalar(m,2);base=certificate(m,2);best=None
 for q in range(base['w_dyadic_exponent'],max(0,base['w_dyadic_exponent']-120),-1):
  found,record=try_box(m,q)
  if found is None:break
  best=dict(q=q,box=found['box'],image=found['image'],iterations=record['iterations'])
 assert best is not None
 box=dict(h=3,Q=13,B=18,N=13,s=s,L=F(507,152),kappa=F(7938,169),initial_density=oldbox['initial_density'],initial_harmonics=[],constant=m.constant,J=m.J,Y0=m.Y0,baseline=base,adaptive=best)
 receipt=put(ROOT/'verification/box.json.gz',box)
 out=dict(checked_at_utc=stamp(),all_checks_pass=True,bits=1536,minimizing_index=2380,target=pack(target),target_display=target.str(55,radius=True),target_upper=U,s=s,finite=finite,leaves=leaves,box=receipt,q=best['q'],radius_exponent=F(best['q'],6),amplitude_exponent=F(13,6),exact_scalar_identities=78,prior_review=dict(path=str(rp),sha256=sha256(rp.read_bytes()).hexdigest()),prior_coverage=data['coverage'],actual_elapsed_s=time.monotonic()-start)
 put(ROOT/'verification/checks.json.gz',out)
 for n in ['seventeen_minimum.py','taylor_response_enclosure.py','extremal_single_probe.py','compact_response_bounds.py','adaptive_majorant_boxes.py']:(ROOT/'sources'/n).write_bytes(Path('code',n).read_bytes())
 print(json.dumps(clean({k:v for k,v in out.items() if k not in ['leaves','finite','target_upper','target']})),flush=True)
if __name__=='__main__':
 try:main()
 except Exception as exc:
  out=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)]);put(ROOT/'verification/FAILURE.json',out);print(json.dumps(out),flush=True);raise SystemExit(1)
