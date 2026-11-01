"""1024-bit replay with independent exact-polynomial prefix for delta=4/7."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import argparse,gzip,json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,ctx
from gmpy2 import mpq
from compact_response_bounds import Response
from pure_cartesian_ball import ball,refine_root
from certified_prefix_majorant import PrefixMajorant,direct_scalar
from certified_initial_majorants import endpoints
from unpack_dyadic4 import unpack
from taylor_response_enclosure import enclose
from resonance_block_majorant import clean
from four_sevenths_certificate import polynomial
ROOT=Path('research/239_four_sevenths_two_mode')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def read(row):
    raw=Path(row['path']).read_bytes();assert sha256(raw).hexdigest()==row['sha256']
    decoded=gzip.decompress(raw) if row['path'].endswith('.gz') else raw
    if row.get('raw_sha256'):assert sha256(decoded).hexdigest()==row['raw_sha256']
    return json.loads(decoded)
def low(v):
    m,e,r,re=v;return abs(F(m)*F(2)**e)-F(r)*F(2)**re

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--root',type=int,required=True);args=ap.parse_args()
    started=time.monotonic();ctx.prec=1024;index=args.root;p=ROOT/f'verification/root{index}_checks.json';raw=p.read_bytes();data=json.loads(raw)
    assert data['all_checks_pass'] and data['root_index']==index
    assert (data['h'],data['Q'],data['B'],data['N'],data['K'])==(2,7,4,7,8)
    s=F(data['s']);cov=read(data['coverage']);box=read(data['box']);obs=read(data['obstruction']);assert s>0 and F(cov['s'])==s
    exact=read(obs['prefix_polynomials']);assert exact['exact'] and exact['delta']=='4/7'
    b,I=refine_root(list(map(int,obs['primitive_coefficients'])),data['root_interval'],1080)
    assert arb(*unpack(data['root_ball'])).contains(b)
    r=Response(2,7,b);coefficients=0;independent_norms={}
    for family,fields,last in [('f',r.f,7),('g',r.g,6)]:
        for n in range(1,last+1):
            spec=exact['fields'][family][str(n)];assert fields[n].degree==mpq(spec['radial_exponent']);norm=arb(0)
            values={int(m):polynomial(c,b) for m,c in spec['sine_polynomials'].items()}
            for m in range(1,4*n+2,2 if family=='f' else 1):
                v=values.get(m,arb(0));assert fields[n].sine(m).overlaps(v),('exact_prefix',family,n,m)
                assert fields[n].coefficient(-m).overlaps(-v/2),('negative_prefix',family,n,m)
                coefficients+=2
                if m in values:norm+=abs(v)
            if family=='f':independent_norms[n]=norm
    assert [row['k'] for row in data['finite']]==list(range(1,17))
    for row in data['finite']:
        k=row['k'];value=r.full(k);assert abs(value)>ball(mpq(str(s))) and low(row['enclosure'])>s
        assert value.overlaps(arb(*unpack(row['enclosure'])))
        if k>=8:assert value.overlaps(r.compact(ball(mpq(1,4*k-2))))
    limit=r.compact(arb(0));assert abs(limit)>ball(mpq(str(s))) and limit.overlaps(arb(*unpack(data['limit'])))
    leaves=[];counts=dict(empty=0,singleton=0,interval=0);edge=F(1,30)
    assert F(cov['edge'])==edge and cov['K']==8 and cov['h']==2
    for row in cov['nodes']:
        address=row['address'];denominator=1<<len(address);numerator=int(address,2) if address else 0
        a=edge*numerator/denominator;b1=edge*(numerator+1)/denominator
        assert (F(row['a']),F(row['b']))==(a,b1)
        first=(1/b1+2)/4;lo=max(8,-(-first.numerator//first.denominator));hi=None
        if a:last=(1/a+2)/4;hi=last.numerator//last.denominator
        assert (row['lower'],row['upper'])==(lo,hi)
        status=row['status'];counts[status]+=1
        if status=='empty':assert hi is not None and hi<lo
        else:
            assert low(row['enclosure'])>s
            if status=='singleton':assert lo==hi==row['k'];value=r.compact(ball(mpq(1,4*lo-2)))
            else:assert status=='interval' and row['method']=='taylor' and row['degree']==2;value=enclose(r,a,b1,degree=2)
            assert value is not None and abs(value)>ball(mpq(str(s))) and value.overlaps(arb(*unpack(row['enclosure'])))
        leaves.append((a,b1))
    leaves.sort();assert leaves[0][0]==0 and leaves[-1][1]==edge and all(a[1]==b1[0] for a,b1 in zip(leaves,leaves[1:]))
    assert len(leaves)==cov['splits']+1 and counts==data['counts']
    assert len(box['initial_density'])==7 and box['initial_harmonics']==[]
    for n,row in enumerate(box['input_enclosures'],1):
        assert row['n']==n and F(row['bound'])==F(box['initial_density'][n-1])
        assert F(row['bound'])>n*endpoints(independent_norms[n])[1],('independent_norm_bound',n)
    L=F(147,80);kap=F(48,7);assert F(box['L'])==L and F(box['kappa'])==kap and F(box['s'])==s
    m=PrefixMajorant(2,7,4,list(map(F,box['initial_density'])),[],s,L,kap);direct_scalar(m,2)
    assert m.constant==list(map(F,box['constant'])) and m.J==[list(map(F,row)) for row in box['J']] and m.Y0==list(map(F,box['Y0']))
    q=box['adaptive']['q'];assert q==data['q'];bx=list(map(F,box['adaptive']['box']));image=m.transformed(F(1,2**q),bx)
    assert image==list(map(F,box['adaptive']['image'])) and all(y<=z and 0<=v<=z for y,z,v in zip(m.Y0,bx,image))
    out=dict(checked_at_utc=stamp(),all_checks_pass=True,root_index=index,h=2,Q=7,s=s,q=q,radius_exponent=F(q,4),amplitude_exponent=F(7,4),arithmetic_bits=1024,exact_prefix_coefficients=coefficients,finite_responses_recomputed=16,full_compact_comparisons=9,leaf_counts=counts,complete_partition_replayed=True,exact_box_replayed=True,exact_scalar_identities=42,independent_polynomial_norms_checked=True,receipt=dict(path=str(p),sha256=sha256(raw).hexdigest()),actual_elapsed_s=time.monotonic()-started)
    (ROOT/f'verification/root{index}_review.json').write_text(json.dumps(clean(out),indent=2)+'\n')
    (ROOT/'sources/four_sevenths_replay.py').write_bytes(Path('code/four_sevenths_replay.py').read_bytes())
    print(json.dumps(clean(out)),flush=True)
if __name__=='__main__':
    try:main()
    except Exception as exc:
        failure=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        (ROOT/'verification/replay_FAILURE.json').write_text(json.dumps(failure,indent=2)+'\n');print(json.dumps(failure),flush=True);raise SystemExit(1)
