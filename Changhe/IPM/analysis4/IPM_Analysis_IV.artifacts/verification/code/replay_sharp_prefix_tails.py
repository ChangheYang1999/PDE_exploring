"""Independent rational replay of the sharp tail certificates."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
import gzip,json,sys,time
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
ROOT=Path('research/187_sharp_prefix_tail_bounds')

def verify_max(d,m,Q,K,t,k,value):
    assert k>=K
    assert value==F(m+Q*k)**(d-1)*t**k
    # Ratios decrease for d>=2. The left neighbor is strictly smaller
    # unless the selected point is the left endpoint; right cannot grow.
    assert F(m+Q*(k+1))**(d-1)*t**(k+1)<=value
    if k>K: assert F(m+Q*(k-1))**(d-1)*t**(k-1)<value
    if d<=1: assert k==K

start=time.monotonic();summary=json.loads((ROOT/'verification/summary.json').read_text())
packed=(ROOT/'verification/checks.json.gz').read_bytes();raw=gzip.decompress(packed)
assert sha256(packed).hexdigest()==summary['archive_sha256']
assert sha256(raw).hexdigest()==summary['raw_sha256']
data=json.loads(raw);maxima=derivatives=0
for p in data['rows']:
    source=Path(p['path']).read_bytes();assert sha256(source).hexdigest()==p['sha256']
    boxdata=json.loads(source);box=list(map(F,boxdata.get('adaptive',boxdata)['box']))
    N,Q,h,B=p['N'],p['Q'],p['h'],p['B'];z,t,L=F(p['z']),F(p['t']),F(p['L'])
    assert t==z**Q*2**p['q'] and 0<t<1
    for row in p['rows']:
        J=row['J']
        for b in row['bounds']:
            d=b['d'];D=F(0)
            for r,item in enumerate(b['maxima'],1):
                m=N+r;K=max(0,-((m-J-1)//Q));assert item['m']==m and item['K']==K
                value=F(item['S']);verify_max(d,m,Q,K,t,item['k'],value);maxima+=1
                D+=box[Q+r-1]*z**m*value
            item=b['harmonic_maximum'];K=max(0,-((N-J-1)//Q));assert item['m']==N and item['K']==K
            value=F(item['S']);verify_max(d,N,Q,K,t,item['k'],value);maxima+=1
            E=box[Q-1]*z**N*value
            assert F(b['D'])==D and F(b['E'])==E
            for out in b['derivatives']:
                a,c=out['radial_Euler_order'],out['angular_order'];assert a+c==d
                density=max(F(2*h,Q),1-F(2*h,Q))**a*B**c*D
                stream=(2-F(2*h,Q))**a*B**c*(L*D+E)
                assert F(out['density_r_minus_1'])==density and F(out['stream_r_minus_2'])==stream
                assert F(out['density_primary'])==density/z and F(out['stream_primary'])==stream/z
                for key,x in [('density',density/z),('stream',stream/z)]:
                    k=out[key+'_primary_dyadic_strict'];assert F(2)**(k-1)<=x<F(2)**k
                derivatives+=1
# Test production search away from the very small ratios of the examples.
from sharp_prefix_tail_bounds import S
search_cases=0
for Q in [3,5,9]:
 for m in [1,19,36]:
  for K in [0,1,5]:
   for t in [F(1,512),F(3,7),F(1,2),F(99,100)]:
    for d in [0,1,2,3,7,12]:
     value,k=S(d,m,Q,K,t);verify_max(d,m,Q,K,t,k,value)
     # A direct finite search checks every candidate through the first decline;
     # the decreasing ratio proves no later revival.
     vals=[F(m+Q*j)**(d-1)*t**j for j in range(K,k+2)]
     assert value==max(vals) and k==K+vals.index(value)
     search_cases+=1
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_exact_checks_pass=True,profiles=len(data['rows']),maxima_checked=maxima,derivative_pairs_checked=derivatives,independent_search_cases=search_cases,source_raw_sha256=sha256(raw).hexdigest(),actual_elapsed_s=time.monotonic()-start)
(ROOT/'verification/replay.json').write_text(json.dumps(result,indent=2)+'\n')
(ROOT/'sources/replay_sharp_prefix_tails.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps(result))
