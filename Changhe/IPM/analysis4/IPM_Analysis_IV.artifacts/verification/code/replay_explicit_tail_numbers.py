"""Independent exact rational replay of the retained derivative-tail examples."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from hashlib import sha256
import gzip,json,sys,time
sys.set_int_max_str_digits(0)
ROOT=Path('research/184_explicit_prefix_tail_bounds')
def series_bound(d,m,Q,K,t):
    u=1-t;a=m+Q*K
    if d==0:return t**K/(a*u)
    if d==1:return t**K/u
    if d==2:return t**K*(a*u+Q*t)/u**2
    return t**K*(a*a*u*u+Q*(2*a+Q)*t*u+2*Q*Q*t*t)/u**3
start=time.monotonic();packed=(ROOT/'verification/checks.json.gz').read_bytes();raw=gzip.decompress(packed);data=json.loads(raw);summary=json.loads((ROOT/'verification/summary.json').read_text());assert sha256(raw).hexdigest()==summary['raw_sha256'] and sha256(packed).hexdigest()==summary['archive_sha256'];assert data['all_exact_checks_pass'] and data['symbolic_identity_checks']==3
scalars=derivatives=0
for profile in data['rows']:
    p=Path(profile['path']);assert sha256(p.read_bytes()).hexdigest()==profile['sha256'];source=json.loads(p.read_text());a=source.get('adaptive',source);box=list(map(F,a['box']));Q,h,N=profile['Q'],profile['h'],profile['N'];B=source['B'];delta=F(2*h,Q);z=F(profile['z']);t=F(profile['t']);assert 0<t<1 and t==z**Q*2**profile['q'];L=F(source['L'])
    if profile['prefix_source']:
        p=Path(profile['prefix_source']['path']);assert sha256(p.read_bytes()).hexdigest()==profile['prefix_source']['sha256']
    assert [row['J'] for row in profile['rows']]==[N,N+Q,N+2*Q]
    for row in profile['rows']:
        J=row['J']
        for bnd in row['bounds']:
            d=bnd['total_derivative_order'];D=F(0)
            for r in range(1,Q+1):
                m=N+r;K=max(0,-(-(J+1-m)//Q));D+=box[Q+r-1]*z**m*series_bound(d,m,Q,K,t)
            K=max(0,-(-(J+1-N)//Q));E=box[Q-1]*z**N*series_bound(d,N,Q,K,t)
            assert D==F(bnd['D']) and E==F(bnd['E']) and D>=0 and E>=0;scalars+=1
            for der in bnd['derivatives']:
                a,b=der['radial_Euler_order'],der['angular_order'];assert a+b==d
                assert F(der['density_weighted_bound'])==max(delta,1-delta)**a*B**b*D
                assert F(der['stream_weighted_bound'])==(2-delta)**a*B**b*(L*D+E);derivatives+=1
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_exact_replay_checks_pass=True,profiles=len(data['rows']),scalar_bound_pairs=scalars,derivative_bound_pairs=derivatives,actual_elapsed_s=time.monotonic()-start,input_raw_sha256=sha256(raw).hexdigest(),scope='Arithmetic replay only. The standalone analytic argument still awaits independent lead review.')
(ROOT/'verification/independent_replay.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
