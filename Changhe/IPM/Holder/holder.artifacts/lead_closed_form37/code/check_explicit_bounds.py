"""Independent interval evaluation of the explicit verifier-lane formulas.

Only local arithmetic is used.  The tail bound for each positive series is
proved in 02_upper_bounds/verification/CERTIFICATION.md.
"""
from datetime import datetime, timezone
from pathlib import Path
import json
from flint import arb, fmpq, ctx
import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
ctx.prec = 256
mp.mp.dps = 65
N = 120


def positive_integral(alpha, p):
    # int_0^(1/2) s^(alpha+1+2p) / sqrt(1-s^2) ds
    exponent = alpha + 2 + 2 * p
    coeff = arb(1)
    total = arb(0)
    for k in range(N):
        total += coeff * arb(2) ** (-(exponent + 2*k)) / (exponent + 2*k)
        coeff *= arb(2*k+1) / arb(2*k+2)
    tail = arb(4)/3 * arb(2) ** (-(exponent+2*N)) / (exponent+2*N)
    # [0, tail.upper()] with outward ball arithmetic.
    remainder = arb(tail.upper()/2, tail.upper()/2)
    return total + remainder


def evaluate(numerator, denominator):
    aq = fmpq(numerator, denominator)
    a = arb(aq)
    a1 = arb(2)**(a-1) / arb.pi().sqrt() * ((a+2)/2).gamma() / ((a+3)/2).gamma()
    a2 = arb(2)**(1+a/2) / (arb.pi()*(a+2))
    a3 = 3 * arb(2)**a / arb.pi() * (3*positive_integral(a,0)-4*positive_integral(a,1))
    shell_harmonic = (a3+a1)/2
    shell_antipodal = arb(2)**(a+1)/(3*arb.pi())
    assert shell_harmonic < shell_antipodal or shell_antipodal < shell_harmonic
    shell = shell_harmonic if shell_harmonic < shell_antipodal else shell_antipodal
    B = 2*a3/(1-a) + shell
    scale = (1-a)*B/(2*a2)
    F = 2*a2*scale**a/(a*(1-a))
    q = arb(2).sqrt()-1
    L = q**a*(4/(arb.pi()*a*(a+2))-arb(1)/4)
    vals = {'a1':a1,'a2':a2,'a3':a3,'shell_bound':shell,'B':B,'optimal_scale':scale,
            'upper_C':F,'upper_D':F+arb(1)/2,'lower_C_and_D':L,
            'alpha_upper':a*F,'alpha_lower':a*L}
    am = mp.mpf(numerator)/denominator
    a3m = 3/mp.pi*mp.quad(lambda t: mp.sin(3*t)*(2*mp.sin(t))**am,[0,mp.pi/6])
    # The decimal comparison is diagnostic only. The interval is certified by
    # exact series inequalities, independent of the floating quadrature.
    assert abs(mp.mpf(a3.mid().str(70,radius=False))-a3m) < mp.mpf('1e-60')
    return {'alpha':f'{numerator}/{denominator}',
            'intervals':{key:str(value) for key,value in vals.items()},
            'decimal_midpoints':{key:value.mid().str(18,radius=False) for key,value in vals.items()},
            'a3_quadrature_diagnostic':mp.nstr(a3m,63)}


def main():
    samples=[(1,1000),(1,100),(1,20),(1,10),(1,5),(3,10),(1,2),(3,4),(9,10),(99,100)]
    rows=[evaluate(n,d) for n,d in samples]
    out={'generated_utc':datetime.now(timezone.utc).isoformat(),
         'precision_bits':ctx.prec,'positive_series_terms':N,'rows':rows,
         'status':'Interval enclosures for the stated explicit formulas; not exact operator norms.'}
    (ROOT/'data/explicit_bounds_intervals.json').write_text(json.dumps(out,indent=2)+'\n')
    for row in rows:
        v=row['decimal_midpoints']
        print(row['alpha'],v['lower_C_and_D'],v['upper_C'],v['upper_D'])

if __name__=='__main__':
    main()
