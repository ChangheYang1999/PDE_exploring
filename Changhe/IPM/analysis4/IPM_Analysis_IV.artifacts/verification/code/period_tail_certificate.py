"""Remaining-response covers and exact boxes for certified long prefixes."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import argparse,gzip,json,sys,time
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,ctx
from gmpy2 import mpq
from pure_cartesian_ball import ball,refine_root
from compact_response_bounds import Response
from discrete_response_cover import cover,lower
from taylor_response_enclosure import enclose
from certified_initial_majorants import pack
from certified_prefix_majorant import PrefixMajorant,certificate
from adaptive_majorant_boxes import try_box
from resonance_block_majorant import clean
ROOT=Path('research/262_tail_response_prefix')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def put(path,obj):
 raw=json.dumps(clean(obj),separators=(',',':')).encode();data=gzip.compress(raw,mtime=0);path.write_bytes(data)
 return dict(path=str(path),sha256=sha256(data).hexdigest(),raw_sha256=sha256(raw).hexdigest())
def read(path):
 raw=path.read_bytes();return raw,json.loads(gzip.decompress(raw))
p=argparse.ArgumentParser();p.add_argument('--Q',type=int,required=True);args=p.parse_args();start=time.monotonic();ctx.prec=2048;Q=args.Q;assert Q in [7,8]
prefix=ROOT/f'verification/Q{Q}_root3_checks.json.gz';raw,d=read(prefix);assert d['all_checks_pass'];N=d['maximum_order'];assert N==(140 if Q==7 else 96);M=N//Q;K=max(M,2*Q+1)
obs=json.loads(Path(d['inputs'][0]['path']).read_bytes());b,I=refine_root(list(map(int,obs['primitive_coefficients'])),obs['real_roots'][2]['interval'],2112);r=Response(1,Q,b)
finite=[]
for k in range(M,K+8):
 v=r.full(k);assert lower(v)>0
 if k>=2*Q+1:assert v.overlaps(r.compact(ball(mpq(1,2*k-2))))
 finite.append(dict(k=k,enclosure=pack(v)))
limit=r.compact(arb(0));least=min([lower(limit)]+[abs(F(x['enclosure'][0])*F(2)**x['enclosure'][1])-F(x['enclosure'][2])*F(2)**x['enclosure'][3] for x in finite]);assert least>0
s=F(1)
while 2*s<least/2:s*=2
while s>=least/2:s/=2
cov=cover(r,K,s,interval_encloser=lambda lo,hi:enclose(r,lo,hi,degree=3),enclosure_metadata=dict(method='taylor',degree=3),point_split_width=8);s=F(cov['s']);cr=put(ROOT/f'verification/Q{Q}_tail_cover.json.gz',cov)
ns={x['n']:x for x in d['norms']};hs={x['n']:x for x in d['harmonics']};density=[F(ns[n]['density_bound']) for n in range(1,N+1)];harmonics=[F(0)]+[F(hs[n]['bound']) for n in range(2*Q,N,Q)]
delta=F(2,Q);L=F(3*Q*Q,4*(3*Q-1));kap=4*(2-delta+max(delta,1-delta))*(1-delta)/delta*F(N+1,N)
m=PrefixMajorant(1,Q,4,density,harmonics,s,L,kap);base=certificate(m,2);best=None;attempts=[]
for q in range(base['w_dyadic_exponent'],0,-1):
 result,attempt=try_box(m,q);attempts.append(attempt)
 if result is None:break
 best=result
assert best is not None
box=dict(h=1,Q=Q,B=4,N=N,M=M,K=K,s=s,L=L,kappa=kap,initial_density=density,initial_harmonics=harmonics,constant=m.constant,J=m.J,Y0=m.Y0,baseline=base,adaptive=best,attempts=attempts)
br=put(ROOT/f'verification/Q{Q}_tail_box.json.gz',box)
out=dict(checked_at_utc=stamp(),all_checks_pass=True,bits=2048,Q=Q,N=N,M=M,K=K,root_index=3,root_interval=I,s=s,finite=finite,limit=pack(limit),cover=cr,box=br,prefix=dict(path=str(prefix),sha256=sha256(raw).hexdigest()),q=best['q'],radius_exponent=F(best['q'],2),actual_elapsed_s=time.monotonic()-start)
put(ROOT/f'verification/Q{Q}_tail_checks.json.gz',out)
for name in ['period_tail_certificate.py','discrete_response_cover.py','taylor_response_enclosure.py','compact_response_bounds.py','certified_prefix_majorant.py','adaptive_majorant_boxes.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
print(json.dumps(clean({k:v for k,v in out.items() if k not in ['finite','limit','root_interval']})),flush=True)
