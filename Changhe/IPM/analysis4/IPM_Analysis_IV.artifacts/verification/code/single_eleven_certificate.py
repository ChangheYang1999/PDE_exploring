"""Complete integer-tail response cover and explicit prefix majorant for sin(11 theta)."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import gzip,json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,ctx
from gmpy2 import mpq
from single_eleven_probe import HighModeResponse,ROOT
from pure_cartesian_ball import ball
from three_fifths_response_bounds import exact_lower
from certified_initial_majorants import pack,endpoints,round_up
from certified_prefix_majorant import PrefixMajorant,certificate
from adaptive_majorant_boxes import try_box
from resonance_block_majorant import clean
from discrete_response_cover import cover
from discrete_cover_checks import check as check_discrete
from taylor_response_enclosure import enclose

def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def put(path,data):
    raw=json.dumps(clean(data),separators=(',',':')).encode()
    encoded=gzip.compress(raw,compresslevel=6,mtime=0) if path.suffix=='.gz' else raw+b'\n'
    path.write_bytes(encoded)
    return dict(path=str(path),sha256=sha256(encoded).hexdigest(),raw_sha256=sha256(raw).hexdigest())
def lower(d):
    m,e,r,re=d;return abs(F(m)*F(2)**e)-F(r)*F(2)**re
def ceil(x):return -((-x.numerator)//x.denominator)
def floor(x):return x.numerator//x.denominator

def main():
    start=time.monotonic();check_discrete();ctx.prec=768;probe_path=ROOT/'verification/probe.json';raw=probe_path.read_bytes();probe=json.loads(raw)
    assert probe['all_checks_pass'] and probe['all_separated'] and len(probe['rows'])==40
    assert [r['k'] for r in probe['rows']]==list(range(1,41))
    least=min([lower(r['enclosure']) for r in probe['rows']]+[lower(probe['limit'])]);assert least>0
    s=F(1)
    while s>=least/4:s/=2
    response=HighModeResponse();K=28;edge=F(1,4*K-2);stack=[(F(0),edge,'')];nodes=[];splits=0;adjustments=[]
    # Point samples only select a conservative target. The complete cover below proves it.
    sampled=[]
    for k in [28,40,60,100,200,500,1000,10000,1000000]:
        v=response.compact(ball(mpq(1,4*k-2)));assert v is not None and exact_lower(v)>0
        sampled.append(dict(k=k,enclosure=pack(v)))
        while s>=exact_lower(v)/4:s/=2
    for left,right in zip(sampled,sampled[1:]):
        def sign(row):return 1 if F(row['enclosure'][0])>0 else -1
        if sign(left)==sign(right):continue
        a,b=left['k'],right['k'];sa=sign(left)
        while b-a>1:
            k=(a+b)//2;v=response.compact(ball(mpq(1,4*k-2)));assert exact_lower(v)>0
            while s>=exact_lower(v)/4:s/=2
            sampled.append(dict(k=k,enclosure=pack(v)))
            if (1 if v>0 else -1)==sa:a=k
            else:b=k
    print(json.dumps(dict(time=stamp(),stage='cover_start',s=str(s),K=K)),flush=True)
    covering=cover(response,K,s,progress=lambda data:put(ROOT/'verification/cover_partial.json.gz',data),
        interval_encloser=lambda a,b:enclose(response,a,b,degree=2),
        enclosure_metadata=dict(method='taylor',degree=2),point_split_width=8)
    nodes=covering['nodes'];splits=covering['splits'];s=F(covering['s']);adjustments+=covering['adjustments']
    cov=put(ROOT/'verification/cover.json.gz',covering)
    initial=[];d=[]
    for n in range(1,10):
        v=response.f[n].norm();bound=round_up(n*endpoints(v)[1]);assert bound>0 and bound>n*endpoints(v)[1]
        d.append(bound);initial.append(dict(n=n,enclosure=pack(v),bound=bound))
    L=F(243,104);delta=F(4,9);kappa=12*(2-delta+max(delta,1-delta))*(1-delta)/delta*F(10,9)
    m=PrefixMajorant(2,9,12,d,[],s,L,kappa);base=certificate(m,2);q=base['w_dyadic_exponent'];chosen=None
    for j in range(q,max(0,q-100),-1):
        item,record=try_box(m,j)
        if item is None:break
        chosen=dict(q=j,box=item['box'],image=item['image'],iterations=record['iterations'])
    assert chosen is not None
    box=put(ROOT/'verification/box.json.gz',dict(h=2,Q=9,B=12,N=9,s=s,L=L,kappa=kappa,initial_density=d,initial_harmonics=[],input_enclosures=initial,constant=m.constant,J=m.J,Y0=m.Y0,baseline=base,adaptive=chosen))
    result=dict(checked_at_utc=stamp(),all_checks_pass=True,mode=11,delta='4/9',h=2,Q=9,B=12,N=9,K=K,s=s,
        target_adjustments=adjustments,extra_samples=sampled,finite_checked=list(range(1,28)),probe=dict(path=str(probe_path),sha256=sha256(raw).hexdigest()),
        coverage=cov,accepted=sum(n['status'] in ('interval','singleton') for n in nodes),interval=sum(n['status']=='interval' for n in nodes),singleton=sum(n['status']=='singleton' for n in nodes),empty=sum(n['status']=='empty' for n in nodes),leaves=len(nodes),
        box=box,q=chosen['q'],radius_exponent=F(chosen['q'],4),amplitude_exponent=F(9,4),arithmetic_bits=768,actual_elapsed_s=time.monotonic()-start)
    put(ROOT/'verification/checks.json',result)
    for name in ['single_eleven_certificate.py','single_eleven_probe.py','compact_response_bounds.py','pure_cartesian_ball.py','certified_prefix_majorant.py','adaptive_majorant_boxes.py','discrete_response_cover.py','taylor_response_enclosure.py']:
        (ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    partial=ROOT/'verification/cover_partial.json.gz'
    if partial.exists():partial.unlink()
    print(json.dumps(clean(result)),flush=True)
if __name__=='__main__':
    try:main()
    except Exception as exc:
        failure=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        (ROOT/'verification/certificate_FAILURE.json').write_text(json.dumps(failure,indent=2)+'\n');print(json.dumps(failure),flush=True);raise SystemExit(1)
