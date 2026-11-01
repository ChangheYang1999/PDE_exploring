"""Independent rational partition and 1024-bit response replay for sin17."""
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
from extremal_single_exact import ExactSingle,coefficient
from pure_cartesian_ball import ball
from certified_prefix_majorant import PrefixMajorant,direct_scalar
from unpack_dyadic4 import unpack
from taylor_response_enclosure import enclose
from resonance_block_majorant import clean
ROOT=Path('research/242_single_seventeen_six_thirteenths')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def read(row):
    raw=Path(row['path']).read_bytes();assert sha256(raw).hexdigest()==row['sha256'];decoded=gzip.decompress(raw) if row['path'].endswith('.gz') else raw
    if row.get('raw_sha256'):assert sha256(decoded).hexdigest()==row['raw_sha256']
    return json.loads(decoded)
def low(v):
    m,e,r,re=v;return abs(F(m)*F(2)**e)-F(r)*F(2)**re

def main():
    started=time.monotonic();ctx.prec=1024;p=ROOT/'verification/checks.json';raw=p.read_bytes();data=json.loads(raw);assert data['all_checks_pass']
    assert (data['h'],data['Q'],data['B'],data['N'],data['K'])==(3,13,18,13,40)
    s=F(data['s']);cover=read(data['coverage']);box=read(data['box']);probe=read(data['probe']);assert s>0 and F(cover['s'])==s
    assert [r['k'] for r in probe['rows']]==list(range(1,48)) and all(low(r['enclosure'])>s for r in probe['rows'])
    r=ExtremalResponse(3,13);exact=ExactSingle(3,13);exact.initialize();coefficients=0
    for f,g,last in [(r.f,exact.F,13),(r.g,exact.G,12)]:
        for n in range(1,last+1):
            assert f[n].degree==mpq(str(g[n].q)) and len(g[n].a)==1
            for m in range(-18*n-2,18*n+3):
                value=g[n].a[0][g[n].M+m] if g[n].M+m>=0 else 0
                assert f[n].coefficient(m).contains(ball(mpq(str(value)))),('exact_prefix',n,m)
                coefficients+=1
    for k in range(1,40):
        value=r.full(k);assert abs(value)>ball(mpq(str(s))) and value.overlaps(arb(*unpack(probe['rows'][k-1]['enclosure'])))
    leaves=[];counts=dict(empty=0,singleton=0,interval=0);edge=F(1,238);assert F(cover['edge'])==edge and cover['K']==40 and cover['h']==3
    for row in cover['nodes']:
        address=row['address'];denominator=1<<len(address);numerator=int(address,2) if address else 0
        a=edge*numerator/denominator;b=edge*(numerator+1)/denominator
        assert (F(row['a']),F(row['b']))==(a,b)
        first=(1/b+2)/6;lo=max(40,-(-first.numerator//first.denominator));hi=None
        if a:
            last=(1/a+2)/6;hi=last.numerator//last.denominator
        assert (row['lower'],row['upper'])==(lo,hi)
        status=row['status'];counts[status]+=1
        if status=='empty':assert hi is not None and hi<lo
        else:
            assert low(row['enclosure'])>s
            if status=='singleton':
                assert lo==hi==row['k'];value=r.compact(ball(mpq(1,6*lo-2)))
            else:
                assert status=='interval' and row['method']=='taylor' and row['degree']==5;value=enclose(r,a,b,degree=5)
            assert value is not None and abs(value)>ball(mpq(str(s))) and value.overlaps(arb(*unpack(row['enclosure'])))
        leaves.append((a,b))
    leaves.sort();assert leaves[0][0]==0 and leaves[-1][1]==edge and all(a[1]==b[0] for a,b in zip(leaves,leaves[1:]))
    assert len(leaves)==cover['splits']+1 and counts==data['counts']
    assert len(box['initial_density'])==13 and box['initial_harmonics']==[]
    for n,row in enumerate(box['input_enclosures'],1):
        assert row['n']==n
        norm=sum((abs(coefficient(exact.F[n],m)) for m in range(1,18*n,2)),0)
        assert F(row['bound'])==F(box['initial_density'][n-1]) and F(row['bound'])>n*F(str(norm))
    delta=F(6,13);L=F(507,152);kap=F(7938,169)
    assert F(box['L'])==L and F(box['kappa'])==kap and F(box['s'])==s
    m=PrefixMajorant(3,13,18,list(map(F,box['initial_density'])),[],s,L,kap);direct_scalar(m,2)
    assert m.constant==list(map(F,box['constant'])) and m.J==[list(map(F,row)) for row in box['J']] and m.Y0==list(map(F,box['Y0']))
    q=box['adaptive']['q'];assert q==data['q'];b=list(map(F,box['adaptive']['box']));image=m.transformed(F(1,2**q),b)
    assert image==list(map(F,box['adaptive']['image'])) and all(y<=z and 0<=v<=z for y,z,v in zip(m.Y0,b,image))
    out=dict(checked_at_utc=stamp(),all_checks_pass=True,h=3,Q=13,mode=17,s=s,q=q,radius_exponent=F(q,6),amplitude_exponent=F(13,6),arithmetic_bits=1024,exact_prefix_coefficients=coefficients,finite_responses_recomputed=39,leaf_counts=counts,complete_partition_replayed=True,exact_box_replayed=True,exact_scalar_identities=78,receipt=dict(path=str(p),sha256=sha256(raw).hexdigest()),actual_elapsed_s=time.monotonic()-started)
    (ROOT/'verification/review.json').write_text(json.dumps(clean(out),indent=2)+'\n')
    for name in ['single_seventeen_replay.py','extremal_single_exact.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    print(json.dumps(clean(out)),flush=True)
if __name__=='__main__':
    try:main()
    except Exception as exc:
        failure=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        (ROOT/'verification/replay_FAILURE.json').write_text(json.dumps(failure,indent=2)+'\n');print(json.dumps(failure),flush=True);raise SystemExit(1)
