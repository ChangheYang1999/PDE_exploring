"""Combine local, smooth cross-disk, middle-circle and exterior bounds."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
from flint import arb, ctx
from certify_far_circles import upper_decimal
import argparse, hashlib, json
ctx.prec = 192
ROOT = Path(__file__).resolve().parents[1]

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--middle', default='data/middle_circle_certificate_n512.json')
    p.add_argument('--cross', default='data/cross_disk_certificate.json')
    p.add_argument('--far', default='data/far_circle_certificate_fine.json')
    p.add_argument('--out', default='data/middle_composite_upper_n512.json')
    a = p.parse_args()
    mid = json.loads((ROOT/a.middle).read_text())
    cross = json.loads((ROOT/a.cross).read_text())
    far = json.loads((ROOT/a.far).read_text())
    m = mid['phase_intervals']
    assert cross['phase_intervals'] == far['phase_intervals'] == m
    cr = {Fraction(r['alpha']):r for r in cross['rows']}
    fr = {Fraction(r['alpha']):r for r in far['rows']}
    phase_factor = 1/(arb.pi()/(4*m)).cos()
    rows = []
    for r in mid['rows']:
        alpha = arb(r['alpha']); key = Fraction(r['alpha'])
        c = cr[key]; f = fr[key]
        assert len(r['middle_phase_intervals']) == len(c['cross_phase_intervals']) == len(f['far_phase_intervals']) == m+1
        values = [arb(x)+arb(y)+arb(z) for x,y,z in zip(r['middle_phase_intervals'],c['cross_phase_intervals'],f['far_phase_intervals'])]
        mx = values[0]
        for v in values[1:]: mx = arb.max(mx,v)
        remainder = mx*phase_factor
        a2 = arb(2)**(1+alpha/2)/(arb.pi()*(alpha+2))
        A = ((alpha+2)/2).gamma()/(2*arb.pi().sqrt()*((alpha+3)/2).gamma())
        nearC = 2*a2*arb(2)**(-alpha)/alpha
        nearD = 2*A*arb(2)**(-alpha)/alpha+arb(1)/2
        C = nearC+remainder; D = nearD+remainder
        rows.append(dict(alpha=r['alpha'],regular_plus_far_grid=[v.str(40,more=True) for v in values],phase_uniform_regular_plus_far=remainder.str(40,more=True),near_C=nearC.str(40,more=True),near_D=nearD.str(40,more=True),upper_C=C.str(40,more=True),upper_D=D.str(40,more=True),safe_upper_C=upper_decimal(C),safe_upper_D=upper_decimal(D)))
    result = dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=ctx.prec,phase_intervals=m,method='Local circles, four-point smooth cross-disk remainders, exact rational transports on truncated middle and exterior circles',rows=rows,input_sha256={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in [a.middle,a.cross,a.far]},source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (ROOT/a.out).write_text(json.dumps(result,indent=2)+'\n')
    for r in rows: print(r['alpha'],r['safe_upper_C'],r['safe_upper_D'])
if __name__ == '__main__':
    main()
