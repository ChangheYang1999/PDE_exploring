"""Certified tail-only response lower bounds and exact prefix majorants."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import argparse,gzip,json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from gmpy2 import mpq
from flint import arb,ctx
from compact_response_bounds import Response,ball,refine_root
from three_fifths_response_bounds import exact_lower,ceil,floor
from certified_initial_majorants import pack
from certified_prefix_majorant import PrefixMajorant,certificate
from adaptive_majorant_boxes import try_box
from resonance_block_majorant import clean
from discrete_response_cover import cover as discrete_cover
from taylor_response_enclosure import enclose
ROOT=Path('research/223_tail_response_radii')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def put(path,obj):
    raw=json.dumps(clean(obj),separators=(',',':')).encode()
    path.write_bytes(gzip.compress(raw,compresslevel=6,mtime=0) if path.suffix=='.gz' else raw+b'\n')
    return dict(path=str(path),sha256=sha256(path.read_bytes()).hexdigest(),raw_sha256=sha256(raw).hexdigest())
def cover(response,s,K,progress=None):
    data=discrete_cover(response,K,s,progress=progress,
        interval_encloser=lambda a,b:enclose(response,a,b,degree=2),
        enclosure_metadata=dict(method='taylor',degree=2),point_split_width=8)
    for row in data['nodes']:
        if row['status']=='interval':row['status']='accepted'
        elif row['status']=='singleton':row.update(status='accepted',method='singleton')
    return data,None

def one(index,K):
    started=time.monotonic();ctx.prec=768
    op=Path('research/200_three_fifths_tuning/verification/obstruction_checks.json');o=json.loads(op.read_text());assert o['all_checks_pass']
    b,I=refine_root(o['primitive_coefficients'],o['real_roots'][index-1]['interval'],832)
    response=Response(3,10,b);finite=[];least=None
    for k in list(range(K,K+21))+[2*K,4*K,10*K]:
        v=response.compact(ball(mpq(1,6*k-2)));assert v is not None and exact_lower(v)>0
        finite.append(dict(k=k,enclosure=pack(v),display=v.str(32,radius=True)))
        least=exact_lower(v) if least is None else min(least,exact_lower(v))
    limit=response.compact(arb(0));assert limit is not None and exact_lower(limit)>0;least=min(least,exact_lower(limit))
    s=F(1)
    while s>=least/4:s/=2
    attempts=[]
    while True:
        print(json.dumps(dict(root=index,K=K,stage='cover',s=str(s),time=stamp())),flush=True)
        data,fail=cover(response,s,K,progress=lambda v:put(ROOT/'verification'/f'root{index}_K{K}_partial.json.gz',v))
        if data is not None:break
        attempts.append(dict(s=str(s),failure=fail));s/=2
        assert len(attempts)<20
    s=F(data['s'])
    coverage=put(ROOT/'verification'/f'root{index}_K{K}_cover.json.gz',data)
    old=Path(f'research/220_high_prefix_three_fifths_radii/verification/root{index}_checks.json');r=json.loads(old.read_text());assert r['all_checks_pass']
    inp=r['inputs'];raw=Path(inp['path']).read_bytes();assert sha256(raw).hexdigest()==inp['sha256'];unpacked=gzip.decompress(raw);assert sha256(unpacked).hexdigest()==inp['raw_sha256'];src=json.loads(unpacked)
    db={v['n']:F(v['bound']) for v in src['density']};eb={v['n']:F(v['bound']) for v in src['harmonics']};N=10*K
    m=PrefixMajorant(3,10,4,[db[n] for n in range(1,N+1)],[eb[n] for n in range(10,N,10)],s,F(75,29),F(16,3)*F(N+1,N))
    result=certificate(m,2);q=result['w_dyadic_exponent'];best,a=try_box(m,q);assert best;box_attempts=[a]
    while q>1:
        found,a=try_box(m,q-1);box_attempts.append(a)
        if found is None:break
        q-=1;best=found
    result.update(adaptive=best,adaptive_attempts=box_attempts,root_index=index,K=K,inputs=inp,tail_response_receipt=coverage)
    box=put(ROOT/'verification'/f'root{index}_K{K}_box.json.gz',result)
    out=dict(checked_at_utc=stamp(),all_checks_pass=True,root_index=index,K=K,N=N,s=s,previous_global_s=src['s'],root_interval=I,limiting_response=pack(limit),samples=finite,failed_attempts=attempts,coverage=coverage,box=box,q=q,radius_exponent=F(q,6),actual_elapsed_s=time.monotonic()-started)
    put(ROOT/'verification'/f'root{index}_K{K}_checks.json',out)
    print(json.dumps(clean({k:v for k,v in out.items() if k not in ['samples','root_interval','limiting_response']})),flush=True)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--roots',default='4,1,2,3');ap.add_argument('--K',type=int,default=30);a=ap.parse_args();assert a.K>=7
    for index in map(int,a.roots.split(',')):one(index,a.K)
    for name in ['tail_response_radii.py','compact_response_bounds.py','three_fifths_response_bounds.py','pure_cartesian_ball.py','certified_prefix_majorant.py','adaptive_majorant_boxes.py','discrete_response_cover.py','taylor_response_enclosure.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
if __name__=='__main__':
    try:main()
    except Exception as exc:
        d=dict(checked_at_utc=stamp(),type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        put(ROOT/'verification/FAILURE.json',d);print(json.dumps(d),flush=True);raise SystemExit(1)
