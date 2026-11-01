"""Exact total-budget tail maxima and concrete certified evaluations."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
import gzip, json, sys, time
sys.dont_write_bytecode = True
sys.set_int_max_str_digits(0)
from explicit_prefix_tail_bounds import one, A
from resonance_block_majorant import clean
ROOT = Path('research/187_sharp_prefix_tail_bounds')


def S(d, m, Q, K, t):
    assert d >= 0 and m > 0 and Q > 0 and K >= 0 and 0 < t < 1
    def ratio(k): return t * F(m + Q*(k+1), m + Q*k)**(d-1)
    if d <= 1 or ratio(K) <= 1:
        k = K
    else:
        lo, hi = K, max(K+1, 1)
        while ratio(hi) > 1:
            lo, hi = hi, 2*hi+1
        while hi-lo > 1:
            mid = (lo+hi)//2
            if ratio(mid) > 1: lo = mid
            else: hi = mid
        k = hi
    return F(m + Q*k)**(d-1)*t**k, k


def dyadic_strict(x):
    assert x > 0
    k = x.numerator.bit_length()-x.denominator.bit_length()
    while F(2)**k <= x: k += 1
    while F(2)**(k-1) > x: k -= 1
    return k


def main():
    start = time.monotonic()
    paths = [
        'research/176_other_certified_prefixes/verification/two_mode4_N36_box.json',
        'research/176_other_certified_prefixes/verification/candidate1_N27_box.json',
        'research/174_adaptive_majorant_boxes/verification/prefix_N90_sharp.json',
        'research/182_period_five_prefix_radii/verification/root5_N50.json',
        'research/186_period_six_prefix_radii/verification/root6_N60.json',
    ]
    results = []
    for name in paths:
        path = Path(name)
        data = json.loads(path.read_text())
        old = one(path, data)
        N,Q,h = old['N'],old['Q'],old['h']
        z,t = old['z'],old['t']
        box = list(map(F, data.get('adaptive',data)['box']))
        B,L,delta = data['B'],F(data['L']),F(2*h,Q)
        rows = []
        for prev in old['rows']:
            J=prev['J']; bounds=[]
            for d in range(4):
                D=F(0); maxima=[]
                for r in range(1,Q+1):
                    m=N+r;K=max(0,(J+1-m+Q-1)//Q)
                    s,k=S(d,m,Q,K,t)
                    D += box[Q+r-1]*z**m*s
                    maxima.append(dict(m=m,K=K,k=k,S=s))
                K=max(0,(J+1-N+Q-1)//Q)
                s,k=S(d,N,Q,K,t)
                E=box[Q-1]*z**N*s
                assert D<=prev['bounds'][d]['D'] and E<=prev['bounds'][d]['E']
                derivatives=[]
                for a in range(d+1):
                    b=d-a
                    density=max(delta,1-delta)**a*B**b*D
                    stream=(2-delta)**a*B**b*(L*D+E)
                    derivatives.append(dict(radial_Euler_order=a,angular_order=b,
                        density_r_minus_1=density,stream_r_minus_2=stream,
                        density_primary=density/z,stream_primary=stream/z,
                        density_primary_dyadic_strict=dyadic_strict(density/z),
                        stream_primary_dyadic_strict=dyadic_strict(stream/z)))
                bounds.append(dict(d=d,D=D,E=E,maxima=maxima,harmonic_maximum=dict(m=N,K=K,k=k,S=s),derivatives=derivatives))
            rows.append(dict(J=J,bounds=bounds))
        results.append(dict(path=name,sha256=sha256(path.read_bytes()).hexdigest(),prefix_source=old['prefix_source'],N=N,Q=Q,h=h,B=B,L=L,q=old['q'],z=z,t=t,radius_dyadic_exponent=old['radius_dyadic_exponent'],rows=rows))
    data=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_exact_checks_pass=True,scope='Unit leading amplitude. Primary density and stream weights are r^(-gamma) and r^(-1-gamma); all bounds hold on the whole closed exterior at the stated radius.',rows=results,actual_elapsed_s=time.monotonic()-start)
    raw=(json.dumps(clean(data),indent=2)+'\n').encode();packed=gzip.compress(raw,mtime=0)
    (ROOT/'verification/checks.json.gz').write_bytes(packed)
    summary=dict(checked_at_utc=data['checked_at_utc'],profiles=len(results),raw_sha256=sha256(raw).hexdigest(),raw_bytes=len(raw),archive_sha256=sha256(packed).hexdigest(),archive_bytes=len(packed),actual_elapsed_s=data['actual_elapsed_s'])
    (ROOT/'verification/summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    for source in ['sharp_prefix_tail_bounds.py','explicit_prefix_tail_bounds.py','certified_prefix_majorant.py','resonance_block_majorant.py']:
        (ROOT/'sources'/source).write_bytes(Path('code',source).read_bytes())
    print(json.dumps(summary))
    for row in results:
        print(row['path'], 'R exponent',row['radius_dyadic_exponent'],'J',row['N'],[(x['d'],x['derivatives'][0]['density_primary_dyadic_strict'],x['derivatives'][0]['stream_primary_dyadic_strict']) for x in row['rows'][0]['bounds']])

if __name__=='__main__':main()
