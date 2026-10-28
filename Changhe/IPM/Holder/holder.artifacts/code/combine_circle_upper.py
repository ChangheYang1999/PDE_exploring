"""Combine independently audited local, compact-region and exterior bounds."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from flint import arb,ctx
import argparse,json,hashlib
ctx.prec=192
ROOT=Path(__file__).resolve().parents[1]
def safeupper(x,n=10):
    k=int((arb(x.upper())*10**n).ceil().unique_fmpz())
    return f'{k//10**n}.{k%10**n:0{n}d}'
def main():
    p=argparse.ArgumentParser()
    p.add_argument('--regular',default='data/reflection_orbit_certificate_v2_fine.json')
    p.add_argument('--far',default='data/far_circle_certificate_fine.json')
    p.add_argument('--out',default='data/circle_composite_upper_fine.json')
    a=p.parse_args();reg=json.loads((ROOT/a.regular).read_text());far=json.loads((ROOT/a.far).read_text())
    assert reg['version']==2
    m=reg['phase_intervals'];assert far['phase_intervals']==m
    phases=1/(arb.pi()/(4*m)).cos();fr={Fraction(r['alpha']):r for r in far['rows']}
    rows=[]
    for r in reg['rows']:
        alpha=arb(r['alpha']);f=fr[Fraction(r['alpha'])]
        assert len(r['regular_grid'])==len(f['far_phase_intervals'])==m+1
        values=[arb(x)+arb(y) for x,y in zip(r['regular_grid'],f['far_phase_intervals'])]
        mx=values[0]
        for v in values[1:]:mx=arb.max(mx,v)
        regularfar=mx*phases
        A=((alpha+2)/2).gamma()/(2*arb.pi().sqrt()*((alpha+3)/2).gamma())
        nearC=arb(r['near']);nearD=2*A*arb(2)**(-alpha)/alpha+arb(1)/2
        C=nearC+regularfar;D=nearD+regularfar
        assert C.is_finite() and D.is_finite()
        rows.append(dict(alpha=r['alpha'],regular_plus_far_grid=[v.str(36,more=True) for v in values],
                         phase_uniform_regular_plus_far=regularfar.str(36,more=True),
                         near_C=nearC.str(36,more=True),near_D=nearD.str(36,more=True),
                         upper_C=C.str(36,more=True),upper_D=D.str(36,more=True),
                         safe_upper_C=safeupper(C),safe_upper_D=safeupper(D)))
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=ctx.prec,phase_intervals=m,
             method='Local circles, reflection orbits in the compact remainder, exact rational transports on exterior circles',
             rows=rows,input_sha256={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in [a.regular,a.far]},
             source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (ROOT/a.out).write_text(json.dumps(out,indent=2)+'\n')
    for r in rows:print(r['alpha'],r['safe_upper_C'],r['safe_upper_D'])
if __name__=='__main__':main()
