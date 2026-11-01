"""Directed longer Q7/Q8 prefixes with exact resonance-block supersolutions."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import argparse,gzip,json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from gmpy2 import mpq
from flint import arb,ctx
from pure_cartesian_ball import Tuning,sine,refine_root,ball
from compact_response_bounds import Response
from certified_initial_majorants import pack,endpoints,round_up
from certified_prefix_majorant import PrefixMajorant,certificate
from adaptive_majorant_boxes import try_box
from resonance_block_majorant import clean
ROOT=Path('research/261_period_seven_eight_prefixes')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def put(path,obj):
 raw=json.dumps(clean(obj),separators=(',',':')).encode();data=gzip.compress(raw,mtime=0) if path.suffix=='.gz' else raw+b'\n';path.write_bytes(data)
 return dict(path=str(path),sha256=sha256(data).hexdigest(),raw_sha256=sha256(raw).hexdigest())
def load_receipt(row):
 raw=Path(row['path']).read_bytes();assert sha256(raw).hexdigest()==row['sha256'];decoded=gzip.decompress(raw) if row['path'].endswith('.gz') else raw
 if row.get('raw_sha256'):assert sha256(decoded).hexdigest()==row['raw_sha256']
 return json.loads(decoded)
def polynomial(c,b):
 v=arb(0)
 for a in reversed(c):v=v*b+ball(mpq(a))
 return v

def one(Q,index,N,bits):
 start=time.monotonic();ctx.prec=bits;ball.cache_clear();folder=Path('research', '253_period_seven_tuning' if Q==7 else '256_period_eight_tuning')
 op=folder/'verification/obstruction_checks.json';ob=op.read_bytes();obs=json.loads(ob);assert obs['all_checks_pass'];exact=load_receipt(obs['prefix_polynomials'])
 rp=folder/f'verification/root{index}_review.json';rr=rp.read_bytes();review=json.loads(rr);assert review['all_checks_pass'];s=F(review['s'])
 b,I=refine_root(list(map(int,obs['primitive_coefficients'])),obs['real_roots'][index-1]['interval'],bits+64)
 response=Response(1,Q,b);solver=Tuning(1,Q,4);f={1:sine(solver.p(1),1,arb(1))+sine(solver.p(1),3,b)};g={1:solver.poisson(f[1],1)}
 harmonics=[];norms=[];d={};e={Q:F(0)};cases=[];prefix_count=0;low_response_checks=0
 base=dict(Q=Q,h=1,B=4,root_index=index,bits=bits,root_interval=I,root_ball=pack(b),s=s,inputs=[dict(path=str(p),sha256=sha256(raw).hexdigest()) for p,raw in [(op,ob),(rp,rr)]],exact_prefix=obs['prefix_polynomials'])
 for n in range(1,N+1):
  if n>1:
   fn=solver.order(n,f,g)
   if solver.resonant(n):
    obstruction=fn.sine(solver.frequency(n)-1);assert obstruction.contains(0)
    f[n]=fn.project(4*n-1,1,solver.counts,zero_mode=solver.frequency(n)-1)
    zero=solver.continuation(n,f,g,arb(0));sigma=response.full(n//Q);assert not sigma.contains(0) and abs(sigma)>ball(mpq(str(s)))
    if n==2*Q:
     oneR=solver.continuation(n,f,g,arb(1));assert sigma.overlaps(oneR-zero);low_response_checks+=1
    H=-zero/sigma;g[n]=solver.poisson(f[n],n,H);eb=round_up(n*endpoints(abs(H))[1]);e[n]=eb
    harmonics.append(dict(n=n,H=pack(H),sigma=pack(sigma),obstruction=pack(obstruction),bound=eb))
    print(json.dumps(dict(at=stamp(),Q=Q,root=index,n=n,stage='tuned',actual_elapsed_s=time.monotonic()-start)),flush=True)
   else:f[n]=fn;g[n]=solver.poisson(fn,n)
  for label,series in [('f',f),('g',g)]:
   if str(n) in exact['fields'][label]:
    expected=exact['fields'][label][str(n)]['sine_polynomials']
    for m in range(1 if label=='f' else 2,4*n+(0 if label=='f' else 1),2):
     old=polynomial(expected.get(str(m),['0']),b);assert series[n].sine(m).overlaps(old),('prefix',Q,index,label,n,m);prefix_count+=1
  fnorm=f[n].norm();gnorm=g[n].norm();assert fnorm>0 and gnorm>0
  bound=round_up(n*endpoints(fnorm)[1]);d[n]=bound;norms.append(dict(n=n,F=pack(fnorm),G=pack(gnorm),density_bound=bound))
  if n>=2*Q and n%(2*Q)==0:
   L=F(3*Q*Q,4*(3*Q-1));delta=F(2,Q);kap=4*(2-delta+max(delta,1-delta))*(1-delta)/delta*F(n+1,n)
   m=PrefixMajorant(1,Q,4,[d[j] for j in range(1,n+1)],[e[j] for j in range(Q,n,Q)],s,L,kap);initial=certificate(m,2);best=None;attempts=[]
   for q in range(initial['w_dyadic_exponent'],0,-1):
    candidate,attempt=try_box(m,q);attempts.append(attempt)
    if candidate is None:break
    best=candidate
   assert best is not None
   box=dict(h=1,Q=Q,B=4,N=n,s=s,L=L,kappa=kap,initial_density=m.d[1:],initial_harmonics=m.e,constant=m.constant,J=m.J,Y0=m.Y0,baseline=initial,adaptive=best,attempts=attempts)
   br=put(ROOT/f'verification/Q{Q}_root{index}_N{n}_box.json.gz',box);q=best['q']
   cases.append(dict(N=n,q=q,radius_exponent=F(q,2),box=br))
   out=dict(base,checked_at_utc=stamp(),all_checks_pass=True,maximum_order=n,cases=cases,norms=norms,harmonics=harmonics,counts=solver.counts,exact_prefix_comparisons=prefix_count,direct_response_checks=low_response_checks,actual_elapsed_s=time.monotonic()-start)
   receipt=put(ROOT/f'verification/Q{Q}_root{index}_checks.json.gz',out)
   print(json.dumps(clean(dict(at=stamp(),Q=Q,root=index,N=n,q=q,radius_exponent=F(q,2),receipt=receipt,actual_elapsed_s=time.monotonic()-start))),flush=True)
 for name in ['period_high_prefix.py','pure_cartesian_ball.py','compact_response_bounds.py','certified_prefix_majorant.py','adaptive_majorant_boxes.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
 return cases

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--Q',type=int,required=True);ap.add_argument('--root',type=int,required=True);ap.add_argument('--N',type=int,required=True);ap.add_argument('--bits',type=int,default=1536);a=ap.parse_args();assert a.Q in [7,8] and 1<=a.root<=10 and a.N%(2*a.Q)==0
 try:one(a.Q,a.root,a.N,a.bits)
 except Exception as exc:
  out=dict(checked_at_utc=stamp(),Q=a.Q,root_index=a.root,error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
  put(ROOT/f'verification/Q{a.Q}_root{a.root}_FAILURE.json',out);print(json.dumps(out),flush=True);raise SystemExit(1)
if __name__=='__main__':main()
