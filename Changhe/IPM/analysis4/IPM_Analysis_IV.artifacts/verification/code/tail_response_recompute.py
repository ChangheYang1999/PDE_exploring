"""Higher-precision response recomputation for every accepted tail-cover leaf."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from hashlib import sha256
import argparse,gzip,json,sys,time
sys.dont_write_bytecode=True
from flint import arb,ctx
from gmpy2 import mpq
from compact_response_bounds import Response,ball,refine_root
from unpack_dyadic4 import unpack
from taylor_response_enclosure import enclose
ROOT=Path('research/223_tail_response_radii')
def one(index,K):
    started=time.monotonic();ctx.prec=1024
    source=ROOT/'verification'/f'root{index}_K{K}_checks.json';raw=source.read_bytes();r=json.loads(raw);assert r['all_checks_pass']
    partition=json.loads(gzip.decompress(Path(r['coverage']['path']).read_bytes()))
    assert sha256(Path(r['coverage']['path']).read_bytes()).hexdigest()==r['coverage']['sha256']
    roots=Path('research/200_three_fifths_tuning/verification/obstruction_checks.json');rawroots=roots.read_bytes();data=json.loads(rawroots)
    b,I=refine_root(data['primitive_coefficients'],data['real_roots'][index-1]['interval'],1088)
    response=Response(3,10,b);s=ball(mpq(r['s']));accepted=0
    for row in partition['nodes']:
        if row['status']!='accepted':continue
        a,b=map(mpq,[row['a'],row['b']])
        if row.get('method')=='singleton':
            assert row['lower']==row['upper']==row['k']
            value=response.compact(ball(mpq(1,6*row['k']-2)))
        elif row.get('method')=='taylor':
            assert row['degree']==2
            value=enclose(response,F(str(a)),F(str(b)),degree=2)
        else:
            assert 'method' not in row
            value=response.compact(ball(a).union(ball(b)))
        assert value is not None and abs(value)>s and value.overlaps(arb(*unpack(row['enclosure'])))
        accepted+=1
    full_checks=[]
    for k in [K,K+1,K+2,2*K]:
        value=response.full(k);compact=response.compact(ball(mpq(1,6*k-2)))
        assert value.overlaps(compact) and abs(value)>s
        full_checks.append(dict(k=k,value=value.str(35,radius=True)))
    out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,
        root_index=index,K=K,arithmetic_bits=1024,accepted_leaves_recomputed=accepted,full_compact_checks=full_checks,
        source=dict(path=str(source),sha256=sha256(raw).hexdigest()),root_source=dict(path=str(roots),sha256=sha256(rawroots).hexdigest()),
        actual_elapsed_s=time.monotonic()-started)
    (ROOT/'verification'/f'root{index}_K{K}_recomputed.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--roots',default='4');ap.add_argument('--K',type=int,default=30);a=ap.parse_args()
    for index in map(int,a.roots.split(',')):one(index,a.K)
    (ROOT/'sources/tail_response_recompute.py').write_bytes(Path(__file__).read_bytes())
