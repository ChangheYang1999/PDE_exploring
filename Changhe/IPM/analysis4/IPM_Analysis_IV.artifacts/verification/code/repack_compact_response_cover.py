"""Recompute existing interval leaves and retain exact dyadic balls."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time,sys
sys.dont_write_bytecode=True
from gmpy2 import mpq
from flint import arb,ctx
from pure_cartesian_ball import ball
from compact_response_bounds import Response

def pack(v):
    m,e=v.mid().man_exp();r,re=v.rad().man_exp()
    return [str(m),int(e),str(r),int(re)]

def run():
    ctx.prec=512;start=time.monotonic();root=Path('research/149_compact_response_certificates');out=root/'verification';data=json.loads((out/'checks.json').read_text());rows=[]
    for row in data['rows']:
        index=row['root_index'];src=out/('root'+str(index)+'_coverage.json');cover=json.loads(src.read_text());s=mpq(row['s']);lo,hi=map(mpq,row['root_interval']);b=ball(lo).union(ball(hi));response=Response(2,9,b);checked=0
        for node in cover['nodes']:
            if node['status']=='accepted':
                a,b=map(mpq,[node['a'],node['b']]);v=response.compact(ball(a).union(ball(b)))
                assert v is not None and abs(v)>ball(s)
                assert arb(node['response']).contains(v),('printed_enclosure',index,node['address'])
                node['response_exact_dyadic']=pack(v);checked+=1
                if checked%200==0:print(json.dumps(dict(root=index,checked=checked,target=cover['accepted'],elapsed_s=time.monotonic()-start)),flush=True)
        cover['original_sha256']=sha256(src.read_bytes()).hexdigest();cover['exact_repack_checked_at_utc']=datetime.now(timezone.utc).isoformat(timespec='seconds');cover['exact_repack_precision_bits']=512
        dest=out/('root'+str(index)+'_coverage_exact.json');dest.write_text(json.dumps(cover,indent=2)+'\n');rows.append(dict(root_index=index,accepted_recomputed=checked,all_lower_bounds_pass=True,path=str(dest.relative_to(root)),sha256=sha256(dest.read_bytes()).hexdigest()))
        print(json.dumps(dict(root=index,accepted_recomputed=checked,all_lower_bounds_pass=True,elapsed_s=time.monotonic()-start)),flush=True)
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,rows=rows,actual_elapsed_s=time.monotonic()-start,reason='Arb display formatting of wide intervals may replace a signed interval by a symmetric enclosure containing zero. Exact midpoint/radius dyadics preserve the certified positive distance.')
    (out/'exact_repack_checks.json').write_text(json.dumps(result,indent=2)+'\n');(root/'sources/repack_compact_response_cover.py').write_bytes(Path('code/repack_compact_response_cover.py').read_bytes())
if __name__=='__main__':
    try:run()
    except Exception as exc:
        import traceback
        fail=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        Path('research/149_compact_response_certificates/verification/exact_repack_FAILURE.json').write_text(json.dumps(fail,indent=2)+'\n');print(json.dumps(fail),flush=True);raise SystemExit(1)
