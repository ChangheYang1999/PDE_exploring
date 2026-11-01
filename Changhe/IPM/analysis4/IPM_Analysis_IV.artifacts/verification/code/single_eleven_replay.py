"""Independent exact partition and box replay, with higher-precision response checks."""
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
from high_harmonic_tuning import Chain,coefficient
from certified_prefix_majorant import PrefixMajorant
from unpack_dyadic4 import unpack
from resonance_block_majorant import clean
from taylor_response_enclosure import enclose

def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def read(row):
    raw=Path(row['path']).read_bytes();assert sha256(raw).hexdigest()==row['sha256']
    decoded=gzip.decompress(raw) if row['path'].endswith('.gz') else raw
    if row.get('raw_sha256'):assert sha256(decoded).hexdigest()==row['raw_sha256']
    return json.loads(decoded)
def low(v):
    m,e,r,re=v;return abs(F(m)*F(2)**e)-F(r)*F(2)**re
def upper(v):
    m,e,r,re=v;return F(m)*F(2)**e+F(r)*F(2)**re
def ceil(x):return -((-x.numerator)//x.denominator)
def floor(x):return x.numerator//x.denominator

def main():
    start=time.monotonic();ctx.prec=1024;receipt=ROOT/'verification/checks.json';raw=receipt.read_bytes();d=json.loads(raw);assert d['all_checks_pass'];s=F(d['s'])
    probe=read(d['probe']);cover=read(d['coverage']);box=read(d['box']);K=28;edge=F(1,110)
    assert (d['h'],d['Q'],d['B'],d['N'],d['K'])==(2,9,12,9,28)
    assert cover['K']==K and F(cover['s'])==s and F(cover['edge'])==edge
    assert len(probe['rows'])==40 and all(low(row['enclosure'])>s for row in probe['rows'])
    response=HighModeResponse();chain=Chain(11);chain.initialize();exact_low=0
    for fields,ref,last in [(response.f,chain.F,9),(response.g,chain.G,8)]:
        for n in range(1,last+1):
            actual=fields[n];exact=ref[n]
            assert len(exact.a)==1 and actual.degree==mpq(str(exact.q))
            for m in range(-12*n-2,12*n+3):
                q=exact.a[0][exact.M+m] if exact.M+m>=0 else 0
                assert actual.coefficient(m).contains(ball(mpq(str(q)))), ('low_coefficient',n,m)
                exact_low+=1
    finite=[]
    for k in range(1,28):
        v=response.full(k);assert abs(v)>ball(mpq(str(s))) and v.overlaps(arb(*unpack(probe['rows'][k-1]['enclosure'])))
        finite.append(dict(k=k,display=v.str(30,radius=True)))
    print(json.dumps(dict(time=stamp(),stage='finite_replayed',count=len(finite),exact_low_coefficient_checks=exact_low)),flush=True)
    leaves=[];accepted=empty=0
    for row in cover['nodes']:
        bits=row['address'];den=2**len(bits);num=int(bits,2) if bits else 0;a,b=edge*F(num,den),edge*F(num+1,den)
        assert (a,b)==(F(row['a']),F(row['b']))
        lo=max(K,ceil((1/b+2)/4));hi=None if not a else floor((1/a+2)/4)
        assert (lo,hi)==(row['lower'],row['upper'])
        if row['status']=='empty':assert hi is not None and hi<lo;empty+=1
        else:
            assert row['status'] in ('interval','singleton') and low(row['enclosure'])>s
            if row['status']=='singleton':
                assert lo==hi==row['k']
                value=response.compact(ball(mpq(1,4*lo-2)))
            else:
                assert row['method']=='taylor' and row['degree']==2
                value=enclose(response,a,b,degree=2)
            assert value is not None and abs(value)>ball(mpq(str(s))) and value.overlaps(arb(*unpack(row['enclosure'])))
            accepted+=1
        leaves.append((a,b))
        if len(leaves)%250==0:print(json.dumps(dict(time=stamp(),stage='leaf_replay',leaves=len(leaves),accepted=accepted,empty=empty)),flush=True)
    leaves.sort();assert leaves[0][0]==0 and leaves[-1][1]==edge
    assert all(a[1]==b[0] for a,b in zip(leaves,leaves[1:])) and len(leaves)==cover['splits']+1
    assert all((n==i['n'] and F(i['bound'])>n*upper(i['enclosure'])) for n,i in enumerate(box['input_enclosures'],1))
    assert box['initial_harmonics']==[] and len(box['initial_density'])==9
    for row in box['input_enclosures']:
        n=row['n'];norm=sum((abs(coefficient(chain.F[n],m)) for m in range(1,12*n,2)),0)
        assert F(row['bound'])>n*F(str(norm))
    delta=F(4,9);kap=12*(2-delta+max(delta,1-delta))*(1-delta)/delta*F(10,9)
    assert F(box['kappa'])==kap and F(box['L'])==F(243,104)
    m=PrefixMajorant(2,9,12,list(map(F,box['initial_density'])),[],s,F(243,104),kap)
    assert m.constant==list(map(F,box['constant'])) and m.J==[list(map(F,row)) for row in box['J']] and m.Y0==list(map(F,box['Y0']))
    q=box['adaptive']['q'];b=list(map(F,box['adaptive']['box']));image=m.transformed(F(1,2**q),b)
    assert image==list(map(F,box['adaptive']['image'])) and all(y<=z and 0<=v<=z for y,z,v in zip(m.Y0,b,image))
    result=dict(checked_at_utc=stamp(),all_checks_pass=True,mode=11,delta='4/9',s=s,K=K,N=9,q=q,radius_exponent=F(q,4),arithmetic_bits=1024,
        exact_low_coefficient_checks=exact_low,finite_responses_recomputed=len(finite),accepted_leaves_recomputed=accepted,empty_leaves_replayed=empty,
        complete_partition_replayed=True,exact_initial_norms_verified=True,exact_box_replayed=True,receipt=dict(path=str(receipt),sha256=sha256(raw).hexdigest()),actual_elapsed_s=time.monotonic()-start)
    (ROOT/'verification/review.json').write_text(json.dumps(clean(result),indent=2)+'\n')
    (ROOT/'sources/single_eleven_replay.py').write_bytes(Path(__file__).read_bytes());print(json.dumps(clean(result)),flush=True)
if __name__=='__main__':
    try:main()
    except Exception as exc:
        failure=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        (ROOT/'verification/replay_FAILURE.json').write_text(json.dumps(failure,indent=2)+'\n');print(json.dumps(failure),flush=True);raise SystemExit(1)
