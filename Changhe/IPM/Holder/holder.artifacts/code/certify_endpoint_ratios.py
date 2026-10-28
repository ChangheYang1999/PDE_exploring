"""Uniform endpoint ratio certificates from analytic bounds and Arb intervals."""
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,ctx
import json,hashlib
from check_explicit_bounds import positive_integral
ctx.prec=256

def coefficients(a):
    pi=arb.pi()
    a2=arb(2)**(1+a/2)/(pi*(a+2))
    a3=3*arb(2)**a/pi*(3*positive_integral(a,0)-4*positive_integral(a,1))
    # A valid bound at every alpha; avoiding a comparison of overlapping balls.
    b=arb(2)**(a+1)/(3*pi)
    scale=(2*a3+(1-a)*b)/(2*a2)
    return a2,scale

def safeupper(x):
    k=int((arb(x.upper())*10**10).ceil().unique_fmpz())
    return f'{k//10**10}.{k%10**10:010d}'

rows=[]
for end in ['0.005','0.01','0.02']:
    a=arb(0).union(arb(end));a2,s=coefficients(a)
    numerator=2*a2*s**a/(1-a)
    denominator=(arb(2).sqrt()-1)**a*(4/(arb.pi()*(a+2))-a/4)
    ratio=numerator/denominator
    rows.append(dict(endpoint='zero',range=f'0 < alpha <= {end}',ratio_interval=ratio.str(40,more=True),safe_upper=safeupper(ratio)))
for end in ['0.995','0.99','0.98']:
    a=arb(end).union(arb(1));a2,s=coefficients(a)
    numerator=2*a2*s**a/a
    denominator=(a+1)*(a+2)*arb(3).sqrt()/(8*arb.pi())+arb(2)**(1-a)*(1-a)/4
    ratio=numerator/denominator
    rows.append(dict(endpoint='one',range=f'{end} <= alpha < 1',ratio_interval=ratio.str(40,more=True),safe_upper=safeupper(ratio)))
out=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=ctx.prec,rows=rows,
         source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         dependency_sha256=hashlib.sha256(Path('code/check_explicit_bounds.py').read_bytes()).hexdigest(),
         conclusion='Uniform upper bounds for the stated theoretical upper/lower ratio on each entire exponent interval. No sampling argument is used.')
Path('data/endpoint_ratio_certificates.json').write_text(json.dumps(out,indent=2)+'\n')
for r in rows:print(r['range'],r['safe_upper'])
