"""Tail-only response bounds for already certified integer-period prefixes."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
import argparse, gzip, json, sys, time, traceback
sys.dont_write_bytecode = True
sys.set_int_max_str_digits(0)
from gmpy2 import mpq
from flint import arb, ctx
from integer_period_prefix import inputs, constants
from compact_response_bounds import Response, ball, refine_root
from three_fifths_response_bounds import exact_lower, ceil, floor
from certified_initial_majorants import pack
from certified_prefix_majorant import PrefixMajorant, certificate
from adaptive_majorant_boxes import try_box
from resonance_block_majorant import clean
ROOT = Path('research/226_integer_period_tail_radii')
TOPICS = {4:'178_period_four_prefix_radii', 5:'182_period_five_prefix_radii', 6:'186_period_six_prefix_radii'}
def stamp(): return datetime.now(timezone.utc).isoformat(timespec='seconds')
def put(path, obj):
    raw = json.dumps(clean(obj), separators=(',', ':')).encode()
    data = gzip.compress(raw, compresslevel=6, mtime=0) if path.suffix == '.gz' else raw + b'\n'
    path.write_bytes(data)
    return dict(path=str(path), sha256=sha256(data).hexdigest(), raw_sha256=sha256(raw).hexdigest())
def cover(response, target, K):
    edge=F(1, 2*K-2); stack=[(F(0), edge, '')]; nodes=[]; splits=0
    while stack:
        a,b,address=stack.pop(); lo=max(K,ceil((1/b+2)/2)); hi=None if not a else floor((1/a+2)/2)
        row=dict(a=a,b=b,address=address,lower=lo,upper=hi)
        if hi is not None and hi<lo:
            row['status']='empty'; nodes.append(row)
        else:
            value=response.compact(ball(mpq(str(a))).union(ball(mpq(str(b)))))
            if value is not None and exact_lower(value)>target:
                row.update(status='accepted',enclosure=pack(value));nodes.append(row)
            else:
                if len(address)>=65 or len(nodes)+splits>30000:
                    return None,dict(reason='unresolved',address=address,leaves=len(nodes),splits=splits)
                mid=(a+b)/2;stack.extend([(mid,b,address+'1'),(a,mid,address+'0')]);splits+=1
    return dict(K=K,edge=edge,s=target,nodes=nodes,splits=splits),None

def one(Q,index):
    start=time.monotonic();ctx.prec=768;N=10*Q;M=10;K=max(M,ceil(F(4*Q+2,2)))
    oldpath=Path('research',TOPICS[Q],'verification',f'root{index}_N{N}.json')
    raw=oldpath.read_bytes();old=json.loads(raw)
    assert (old['h'],old['Q'],old['B'],old['N'])==(1,Q,4,N)
    old_s=F(old['s']);old_q=old['adaptive']['q'];L,kap=constants(Q,N)
    assert (L,kap)==(F(old['L']),F(old['kappa']))
    d=list(map(F,old['initial_density']));e=list(map(F,old['initial_harmonics']))
    assert len(d)==N and len(e)==M-1 and e[0]==0
    coeff,intervals,lowers,paths=inputs(Q)
    b,I=refine_root(coeff,intervals[index-1],832);response=Response(1,Q,b)
    finite=[];probes=[];least=None
    for k in range(M,K):
        v=response.full(k);assert exact_lower(v)>0
        finite.append(dict(k=k,enclosure=pack(v)));least=exact_lower(v) if least is None else min(least,exact_lower(v))
    for k in sorted(set(list(range(K,K+11))+[2*K,4*K,10*K])):
        v=response.compact(ball(mpq(1,2*k-2)));assert v is not None and exact_lower(v)>0
        row=dict(k=k,enclosure=pack(v))
        if k<K+3:
            full=response.full(k);assert full.overlaps(v);row['full']=pack(full)
        probes.append(row);least=exact_lower(v) if least is None else min(least,exact_lower(v))
    limit=response.compact(arb(0));assert limit is not None and exact_lower(limit)>0
    least=min(least,exact_lower(limit));target=F(1)
    while target>=least/4:target/=2
    while 2*target<least/4:target*=2
    prefix=dict(path=str(oldpath),sha256=sha256(raw).hexdigest())
    root_inputs=[dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest()) for p in paths]
    base=dict(Q=Q,root_index=index,N=N,M=M,K=K,old_s=old_s,old_q=old_q,root_interval=I,
        prefix=prefix,root_inputs=root_inputs,finite=finite,probes=probes,limit=pack(limit))
    attempts=[];data=None
    while target>old_s:
        print(json.dumps(clean(dict(Q=Q,root=index,K=K,stage='cover',s=target,utc=stamp()))),flush=True)
        data,fail=cover(response,target,K)
        if data is not None:break
        attempts.append(dict(s=target,failure=fail));target/=2
    if data is None:
        base.update(checked_at_utc=stamp(),all_checks_pass=True,status='no_improvement',s=old_s,q=old_q,
            proposed_s=target,failed_attempts=attempts,actual_elapsed_s=time.monotonic()-start)
        put(ROOT/'verification'/f'Q{Q}_root{index}_checks.json',base)
        print(json.dumps(clean({k:base[k] for k in ['Q','root_index','status','s','q','actual_elapsed_s']})),flush=True)
        return
    coverage=put(ROOT/'verification'/f'Q{Q}_root{index}_cover.json.gz',data)
    model=PrefixMajorant(1,Q,4,d,e,target,L,kap);result=certificate(model,2)
    q=result['w_dyadic_exponent'];best,record=try_box(model,q);assert best;box_attempts=[record]
    while q>1:
        new,record=try_box(model,q-1);box_attempts.append(record)
        if new is None:break
        best=new;q-=1
    result.update(adaptive=best,adaptive_attempts=box_attempts,prefix=prefix,coverage=coverage)
    box=put(ROOT/'verification'/f'Q{Q}_root{index}_box.json.gz',result)
    base.update(checked_at_utc=stamp(),all_checks_pass=True,status='tail_certified',s=target,q=q,
        radius_exponent=F(q,2),coverage=coverage,box=box,failed_attempts=attempts,actual_elapsed_s=time.monotonic()-start)
    put(ROOT/'verification'/f'Q{Q}_root{index}_checks.json',base)
    print(json.dumps(clean({k:base[k] for k in ['Q','root_index','status','s','q','radius_exponent','actual_elapsed_s']})),flush=True)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--periods',default='4,5,6');ap.add_argument('--roots',default='1,2,3,4,5,6');a=ap.parse_args()
    for Q in map(int,a.periods.split(',')):
        assert Q in TOPICS
        for index in map(int,a.roots.split(',')):one(Q,index)
    for name in ['integer_period_tail_radii.py','integer_period_prefix.py','compact_response_bounds.py','pure_cartesian_ball.py','certified_prefix_majorant.py','adaptive_majorant_boxes.py']:
        (ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
if __name__=='__main__':
    try:main()
    except Exception as exc:
        row=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        put(ROOT/'verification/FAILURE.json',row);print(json.dumps(row),flush=True);raise SystemExit(1)
