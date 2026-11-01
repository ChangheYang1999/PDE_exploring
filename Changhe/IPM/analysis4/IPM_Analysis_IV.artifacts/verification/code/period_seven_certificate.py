"""Independent all-index response covers and prefix boxes at delta2/7."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import argparse,gzip,json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,ctx
from gmpy2 import mpq
from compact_response_bounds import Response
from pure_cartesian_ball import ball,refine_root
from discrete_response_cover import cover,lower
from taylor_response_enclosure import enclose
from certified_initial_majorants import pack,endpoints,round_up
from certified_prefix_majorant import PrefixMajorant,certificate
from adaptive_majorant_boxes import try_box
from resonance_block_majorant import clean
ROOT=Path('research/253_period_seven_tuning')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def put(path,obj):
 raw=json.dumps(clean(obj),separators=(',',':')).encode();saved=gzip.compress(raw,mtime=0) if path.suffix=='.gz' else raw
 path.write_bytes(saved);return dict(path=str(path),sha256=sha256(saved).hexdigest(),raw_sha256=sha256(raw).hexdigest())
def polynomial(coeff,b):
 result=arb(0)
 for a in reversed(coeff):result=result*b+ball(mpq(a))
 return result

def extend_prefix(response):
 for n in range(7,15):
  if n>7:
   value=response.solver.order(n,response.f,response.g)
   if n==14:
    obstruction=value.sine(1);assert obstruction.contains(0)
    value=value.project(4*n-1,1,response.solver.counts,zero_mode=1)
   response.f[n]=value
  if n<14:response.g[n]=response.solver.poisson(response.f[n],n)
 return obstruction

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--root',type=int,required=True);args=ap.parse_args()
 started=time.monotonic();ctx.prec=768;index=args.root;assert 1<=index<=10
 src=ROOT/'verification/obstruction_checks.json';raw=src.read_bytes();data=json.loads(raw);assert data['all_checks_pass'] and data['obstruction_exactly_matches']
 b,I=refine_root(list(map(int,data['primitive_coefficients'])),data['real_roots'][index-1]['interval'],832)
 response=Response(1,7,b);finite=[]
 for k in range(2,23):
  value=response.full(k);assert lower(value)>0,('finite_response',index,k,str(value))
  if k>=15:assert value.overlaps(response.compact(ball(mpq(1,2*k-2)))),('full_compact',index,k)
  finite.append(dict(k=k,enclosure=pack(value),display=value.str(40,radius=True)))
 limit=response.compact(arb(0));assert lower(limit)>0
 least=min([abs(F(m)*F(2)**e)-F(r)*F(2)**re for m,e,r,re in [row['enclosure'] for row in finite]]+[lower(limit)])
 s=F(1)
 while 2*s<least/4:s*=2
 while s>=least/4:s/=2
 print(json.dumps(clean(dict(stage='finite_responses',root=index,s=s,limit=limit.str(35,radius=True),checked_at_utc=stamp()))),flush=True)
 cov=cover(response,15,s,progress=lambda d:put(ROOT/f'verification/root{index}_cover_partial.json.gz',d),interval_encloser=lambda a,b:enclose(response,a,b,degree=3),enclosure_metadata=dict(method='taylor',degree=3),point_split_width=8)
 s=F(cov['s']);cv=put(ROOT/f'verification/root{index}_cover.json.gz',cov)
 obstruction=extend_prefix(response);density=[];initial=[]
 for n in range(1,15):
  norm=response.f[n].norm();d=round_up(n*endpoints(norm)[1]);assert d>n*endpoints(norm)[1]
  density.append(d);initial.append(dict(n=n,enclosure=pack(norm),bound=d))
 L=F(147,80);kap=F(1275,49);m=PrefixMajorant(1,7,4,density,[F(0)],s,L,kap);base=certificate(m,2);best=None
 for q in range(base['w_dyadic_exponent'],max(0,base['w_dyadic_exponent']-100),-1):
  found,record=try_box(m,q)
  if found is None:break
  best=dict(q=q,box=found['box'],image=found['image'],iterations=record['iterations'])
 assert best is not None
 bx=put(ROOT/f'verification/root{index}_box.json.gz',dict(h=1,Q=7,B=4,N=14,s=s,L=L,kappa=kap,input_enclosures=initial,initial_density=density,initial_harmonics=[F(0)],constant=m.constant,J=m.J,Y0=m.Y0,baseline=base,adaptive=best))
 out=dict(checked_at_utc=stamp(),all_checks_pass=True,root_index=index,root_interval=I,root_ball=pack(b),h=1,Q=7,B=4,N=14,K=15,s=s,q=best['q'],radius_exponent=F(best['q'],2),amplitude_exponent=F(7,2),arithmetic_bits=768,finite=finite,limit=pack(limit),first_obstruction=pack(obstruction),full_compact_comparisons=8,coverage=cv,box=bx,counts={status:sum(n['status']==status for n in cov['nodes']) for status in ['empty','singleton','interval']},obstruction=dict(path=str(src),sha256=sha256(raw).hexdigest()),actual_elapsed_s=time.monotonic()-started)
 put(ROOT/f'verification/root{index}_checks.json',out)
 for name in ['period_seven_certificate.py','discrete_response_cover.py','compact_response_bounds.py','pure_cartesian_ball.py','certified_prefix_majorant.py','adaptive_majorant_boxes.py','taylor_response_enclosure.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
 partial=ROOT/f'verification/root{index}_cover_partial.json.gz'
 if partial.exists():partial.unlink()
 print(json.dumps(clean({k:v for k,v in out.items() if k not in ['finite','root_ball','root_interval','limit','first_obstruction']})),flush=True)
if __name__=='__main__':
 try:main()
 except Exception as exc:
  out=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
  put(ROOT/'verification/response_FAILURE.json',out);print(json.dumps(out),flush=True);raise SystemExit(1)
