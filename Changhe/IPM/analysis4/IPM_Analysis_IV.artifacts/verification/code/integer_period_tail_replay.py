"""Recompute and exactly replay integer-period tail-response certificates."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
import argparse, gzip, json, sys, time
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from gmpy2 import mpq
from flint import arb,ctx
from integer_period_prefix import inputs,constants
from compact_response_bounds import Response,ball,refine_root
from certified_prefix_majorant import PrefixMajorant
from unpack_dyadic4 import unpack
from resonance_block_majorant import clean
ROOT=Path('research/226_integer_period_tail_radii')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def lower(v):
    m,e,r,re=v;return abs(F(m)*F(2)**int(e))-F(r)*F(2)**int(re)
def ceil(x):return -((-x.numerator)//x.denominator)
def floor(x):return x.numerator//x.denominator
def hashed_read(r,compressed=False):
    raw=Path(r['path']).read_bytes();assert sha256(raw).hexdigest()==r['sha256']
    if compressed:
        raw=gzip.decompress(raw);assert sha256(raw).hexdigest()==r['raw_sha256']
    return json.loads(raw)
def one(Q,index):
    start=time.monotonic();ctx.prec=1024
    receipt=ROOT/'verification'/f'Q{Q}_root{index}_checks.json';raw=receipt.read_bytes();r=json.loads(raw)
    assert r['all_checks_pass'] and r['Q']==Q and r['root_index']==index
    old=hashed_read(r['prefix']);assert r['old_s']==old['s'] and r['old_q']==old['adaptive']['q']
    for item in r['root_inputs']:hashed_read(item)
    if r['status']=='no_improvement':
        out=dict(checked_at_utc=stamp(),all_checks_pass=True,Q=Q,root_index=index,status='old_certificate_retained',q=r['q'])
    else:
        assert r['status']=='tail_certified'
        M,N,K,s=r['M'],r['N'],r['K'],F(r['s']);assert N==M*Q and M>=2 and 2*K-2>=4*Q and K>=M and s>F(r['old_s'])
        coeff,intervals,_,_=inputs(Q);b,I=refine_root(coeff,intervals[index-1],1088);response=Response(1,Q,b)
        assert [x['k'] for x in r['finite']]==list(range(M,K))
        for row in r['finite']:
            assert lower(row['enclosure'])>s
            value=response.full(row['k']);assert value.overlaps(arb(*unpack(row['enclosure']))) and abs(value)>ball(mpq(str(s)))
        for row in r['probes']:
            if 'full' in row:
                k=row['k'];full=response.full(k);compact=response.compact(ball(mpq(1,2*k-2)))
                assert full.overlaps(compact) and full.overlaps(arb(*unpack(row['full'])))
        coverage=hashed_read(r['coverage'],True);edge=F(1,2*K-2)
        assert (coverage['K'],F(coverage['edge']),F(coverage['s']))==(K,edge,s)
        intervals=[];accepted=empty=0
        for row in coverage['nodes']:
            address=row['address'];den=2**len(address);num=int(address,2) if address else 0
            a=edge*F(num,den);b=edge*F(num+1,den);assert (a,b)==(F(row['a']),F(row['b']))
            lo=max(K,ceil((1/b+2)/2));hi=None if not a else floor((1/a+2)/2)
            assert (lo,hi)==(row['lower'],row['upper'])
            if row['status']=='empty':assert hi is not None and hi<lo;empty+=1
            else:
                assert row['status']=='accepted' and lower(row['enclosure'])>s
                value=response.compact(ball(mpq(str(a))).union(ball(mpq(str(b)))))
                assert value is not None and value.overlaps(arb(*unpack(row['enclosure']))) and abs(value)>ball(mpq(str(s)))
                accepted+=1
            intervals.append((a,b))
        intervals.sort();assert intervals[0][0]==0 and intervals[-1][1]==edge
        assert all(a[1]==b[0] for a,b in zip(intervals,intervals[1:])) and len(intervals)==coverage['splits']+1
        box=hashed_read(r['box'],True)
        d=list(map(F,box['initial_density']));e=list(map(F,box['initial_harmonics']));L,kap=constants(Q,N)
        assert d==list(map(F,old['initial_density'])) and e==list(map(F,old['initial_harmonics'])) and e[0]==0
        assert (box['h'],box['Q'],box['B'],box['N'],F(box['s']),F(box['L']),F(box['kappa']))==(1,Q,4,N,s,L,kap)
        model=PrefixMajorant(1,Q,4,d,e,s,L,kap)
        assert model.J==[list(map(F,row)) for row in box['J']] and model.Y0==list(map(F,box['Y0'])) and model.constant==list(map(F,box['constant']))
        best=box['adaptive'];q=best['q'];B=list(map(F,best['box']));image=model.transformed(F(1,2**q),B)
        assert q==r['q'] and image==list(map(F,best['image'])) and all(0<=v<=b and b>=y for v,b,y in zip(image,B,model.Y0))
        out=dict(checked_at_utc=stamp(),all_checks_pass=True,Q=Q,root_index=index,status='tail_and_box_verified',M=M,N=N,K=K,s=s,
            q=q,radius_exponent=F(q,2),accepted=accepted,empty=empty,leaves=len(intervals),
            finite_recomputed=len(r['finite']),compact_leaves_recomputed=accepted,exact_partition_replay=True,exact_box_replay=True)
    out.update(receipt=dict(path=str(receipt),sha256=sha256(raw).hexdigest()),actual_elapsed_s=time.monotonic()-start)
    (ROOT/'verification'/f'Q{Q}_root{index}_review.json').write_text(json.dumps(clean(out),indent=2)+'\n');print(json.dumps(clean(out)),flush=True)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--periods',default='4,5,6');ap.add_argument('--roots',default='1,2,3,4,5,6');a=ap.parse_args()
    for Q in map(int,a.periods.split(',')):
        for index in map(int,a.roots.split(',')):one(Q,index)
    (ROOT/'sources/integer_period_tail_replay.py').write_bytes(Path(__file__).read_bytes())
if __name__=='__main__':main()
