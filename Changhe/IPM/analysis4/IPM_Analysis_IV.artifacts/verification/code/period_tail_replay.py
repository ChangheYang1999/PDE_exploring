"""Higher-precision complete response-tail replay and exact scalar check."""
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
from taylor_response_enclosure import Jet
from certified_prefix_majorant import PrefixMajorant,direct_scalar
from period_polar_prefix_replay import unpack,upper
from resonance_block_majorant import clean
ROOT=Path('research/262_tail_response_prefix')
def read(path):
 raw=path.read_bytes();return raw,json.loads(gzip.decompress(raw))
def receipt(row):
 raw,d=read(Path(row['path']));assert sha256(raw).hexdigest()==row['sha256']
 if row.get('raw_sha256'):assert sha256(gzip.decompress(raw)).hexdigest()==row['raw_sha256']
 return d
p=argparse.ArgumentParser();p.add_argument('--Q',type=int,required=True);a=p.parse_args();Q=a.Q;start=time.monotonic();ctx.prec=3072
path=ROOT/f'verification/Q{Q}_tail_checks.json.gz';raw,d=read(path);assert d['all_checks_pass'] and d['Q']==Q;N=d['N'];M=d['M'];K=d['K'];assert N==M*Q and K==max(M,2*Q+1);s=F(d['s'])
prefix=receipt(d['prefix']);cover=receipt(d['cover']);box=receipt(d['box']);obs=json.loads(Path(prefix['inputs'][0]['path']).read_bytes())
polar=ROOT/f'verification/Q{Q}_root3_polar_replay.json.gz';pr,pd=read(polar);assert pd['all_checks_pass'] and pd['maximum_order']==N and pd['source']==d['prefix']
b,I=refine_root(list(map(int,obs['primitive_coefficients'])),obs['real_roots'][2]['interval'],3136);r=Response(1,Q,b)
assert [x['k'] for x in d['finite']]==list(range(M,K+8))
for row in d['finite']:
 k=row['k'];v=r.full(k);assert abs(v)>ball(mpq(str(s))) and v.overlaps(unpack(row['enclosure']))
 if k>=2*Q+1:assert v.overlaps(r.compact(ball(mpq(1,2*k-2))))
limit=r.compact(arb(0));assert abs(limit)>ball(mpq(str(s))) and limit.overlaps(unpack(d['limit']))
edge=F(1,2*K-2);assert F(cover['edge'])==edge and F(cover['s'])==s and cover['K']==K;parts=[];counts=dict(empty=0,singleton=0,interval=0)
for row in cover['nodes']:
 address=row['address'];den=1<<len(address);num=int(address,2) if address else 0;lo=edge*num/den;hi=edge*(num+1)/den;assert (lo,hi)==(F(row['a']),F(row['b']))
 x=(1/hi+2)/2;first=max(K,-(-x.numerator//x.denominator));last=None
 if lo:x=(1/lo+2)/2;last=x.numerator//x.denominator
 assert (first,last)==(row['lower'],row['upper']);status=row['status'];counts[status]+=1
 if status=='empty':assert last is not None and last<first
 else:
  if status=='singleton':assert first==last==row['k'];v=r.compact(ball(mpq(1,2*first-2)))
  else:
   assert status=='interval' and row['degree']==3
   mid=(lo+hi)/2;rad=(hi-lo)/2;iv=ball(mpq(str(lo))).union(ball(mpq(str(hi))));center=r.compact(Jet([ball(mpq(str(mid))),arb(1)],3));whole=r.compact(Jet([iv,arb(1)],3));x=ball(mpq(str(-rad))).union(ball(mpq(str(rad))))
   v=center.c[0]+center.c[1]*x+center.c[2]*(x*x)+whole.c[3]*(x*x*x)
  assert v is not None and abs(v)>ball(mpq(str(s))) and v.overlaps(unpack(row['enclosure']))
 parts.append((lo,hi))
parts.sort();assert parts[0][0]==0 and parts[-1][1]==edge and all(x[1]==y[0] for x,y in zip(parts,parts[1:]));assert len(parts)==cover['splits']+1
ns={x['n']:x for x in pd['norms']};hs={x['n']:x for x in pd['harmonics']};density=list(map(F,box['initial_density']));harmonics=list(map(F,box['initial_harmonics']));assert len(density)==N and len(harmonics)==M-1 and harmonics[0]==0
for n,bound in enumerate(density,1):assert bound>n*upper(unpack(ns[n]['F']))
for k,bound in enumerate(harmonics[1:],2):assert bound>k*Q*upper(abs(unpack(hs[k*Q]['H'])))
delta=F(2,Q);L=F(3*Q*Q,4*(3*Q-1));kap=4*(2-delta+max(delta,1-delta))*(1-delta)/delta*F(N+1,N);assert F(box['s'])==s and F(box['L'])==L and F(box['kappa'])==kap
m=PrefixMajorant(1,Q,4,density,harmonics,s,L,kap);direct_scalar(m,2);assert m.J==[list(map(F,x)) for x in box['J']] and m.constant==list(map(F,box['constant'])) and m.Y0==list(map(F,box['Y0']))
v=list(map(F,box['adaptive']['box']));q=box['adaptive']['q'];im=m.transformed(F(1,2**q),v);assert q==d['q'] and im==list(map(F,box['adaptive']['image'])) and all(y<=b and 0<=z<=b for y,b,z in zip(m.Y0,v,im))
out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,Q=Q,root_index=3,N=N,M=M,K=K,s=s,q=q,radius_exponent=F(q,2),finite_responses=len(d['finite']),leaf_counts=counts,complete_partition=True,scalar_identities=6*Q,source=dict(path=str(path),sha256=sha256(raw).hexdigest()),polar_replay=dict(path=str(polar),sha256=sha256(pr).hexdigest()),actual_elapsed_s=time.monotonic()-start)
(ROOT/f'verification/Q{Q}_tail_review.json').write_text(json.dumps(clean(out),indent=2)+'\n');(ROOT/'sources/period_tail_replay.py').write_bytes(Path(__file__).read_bytes());print(json.dumps(clean(out)),flush=True)
