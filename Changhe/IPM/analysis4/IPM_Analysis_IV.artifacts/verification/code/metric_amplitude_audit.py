"""Exact polynomial leading coefficient and analytic-pole Fourier audit."""
from pathlib import Path
from fractions import Fraction
from hashlib import sha256
from datetime import datetime,timezone
import json,time
from flint import fmpq as Q
from rational_scan_audit import compute


def main():
    start=time.monotonic();src=Path('research/42_real_profile_prime_obstruction/verification/polynomial_checks.json');data=json.loads(src.read_text());rows=[]
    for row in data['results']:
        if row['family']!='variable_first':continue
        p,a=row['prime'],row['a'];co=[Q(x) for x in row['kappa_coefficients']]
        reference=compute(Fraction(a,p),{1:'1'},p)
        assert len(co)==p+1 and co[-1]==Q(reference['kappa_exact']) and co[-1]
        rows.append(dict(p=p,a=a,degree=p,leading_coefficient=str(co[-1]),independent_single_sine=str(reference['kappa_exact']),match=True))
    # Laurent algebra for the residue bracket, independent of its sine projection formula.
    pole=[]
    from cartesian_verify import C,I,Q as MQ
    def add(d,k,v):d[k]=d.get(k,C())+v
    def mul(a,b):
        d={}
        for k,v in a.items():
            for m,w in b.items():add(d,k+m,v*w)
        return d
    for j in [1,2,3,7]:
        gamma=Q(3,7);x=Q(2,3)
        amplitudes={1:x,3:Q(-1,5),5:Q(7,11),4*j+1:Q(1,13)}
        f={};fp={}
        for m,v in amplitudes.items():
            # Standard complex Fourier sine coefficients; derivative multiplies by i*m.
            f[m]=-I*MQ(str(v))/2;f[-m]=I*MQ(str(v))/2
            fp[m]=C(MQ(str(v))*m/2);fp[-m]=C(MQ(str(v))*m/2)
        sin={2*j:-I/2,-2*j:I/2};cos={2*j:C(MQ(str(gamma))/2),-2*j:C(MQ(str(gamma))/2)}
        bracket=mul(sin,fp)
        for k,v in mul(cos,f).items():add(bracket,k,v)
        actual=2*bracket[2*j+1].im*(-1)
        expected=((1+gamma)*amplitudes[1]-(4*j+1-gamma)*amplitudes.get(4*j+1,Q(0)))/2
        assert str(Fraction(actual))==str(Fraction(str(expected)))
        pole.append(dict(j=j,gamma=str(gamma),amplitude=str(expected),exact_fourier_match=True))
    out=dict(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),polynomial_cases=rows,pole_cases=pole,
      actual_elapsed_s=time.monotonic()-start,source=str(src),source_sha256=sha256(src.read_bytes()).hexdigest(),code_sha256=sha256(Path(__file__).read_bytes()).hexdigest())
    Path('research/52_metric_amplitude_divergence/verification/checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(polynomial_cases=len(rows),pole_cases=len(pole),elapsed_s=out['actual_elapsed_s'])))

if __name__=='__main__':main()
