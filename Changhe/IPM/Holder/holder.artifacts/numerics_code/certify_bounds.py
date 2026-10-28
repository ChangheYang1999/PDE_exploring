"""Independent arb recomputation of the verification work's explicit bounds F(alpha), L(alpha) (02_upper_bounds/PROOF.md,
03_lower_bounds/PROOF.md).  Closed forms used here (derived independently):
  a_1 = 2^alpha/pi * sqrt(pi) Gamma(1+alpha/2) / (2 Gamma((3+alpha)/2))
  a_2 = 2^(1+alpha/2) / (pi (alpha+2))
  a_3 = (3 2^alpha/pi) * (1/2) [ 3 B(1/4; alpha/2+1, 1/2) - 4 B(1/4; alpha/2+2, 1/2) ],  B(x;a,b) incomplete beta
  b = min((a_3+a_1)/2, 2^(alpha+1)/(3 pi)),  B = 2 a_3/(1-alpha) + b,  s = (1-alpha) B/(2 a_2),
  F = 2 a_2 s^alpha /(alpha (1-alpha)),   L = q^alpha (4/(pi alpha (alpha+2)) - 1/4), q = sqrt2 - 1.
Diagnostic: a_3 also by mpmath quadrature of the defining integral."""
from flint import arb, ctx, fmpq
import mpmath as mp, json, sys
ctx.prec = 200

def consts(alpha):
    al = arb(alpha)
    pi = arb.pi()
    a1 = arb(2)**al/pi*pi.sqrt()*(1 + al/2).gamma()/(2*((3 + al)/2).gamma())
    a2 = arb(2)**(1 + al/2)/(pi*(al + 2))
    B1 = arb(1)/4; half = arb(1)/2
    a3 = 3*arb(2)**al/pi*(3*B1.beta_lower(al/2 + 1, half) - 4*B1.beta_lower(al/2 + 2, half))/2
    b = arb.min((a3 + a1)/2, arb(2)**(al + 1)/(3*pi))
    B = 2*a3/(1 - al) + b
    s = (1 - al)*B/(2*a2)
    F = 2*a2*s**al/(al*(1 - al))
    q = arb(2).sqrt() - 1
    L = q**al*(4/(pi*al*(al + 2)) - arb(1)/4)
    return dict(a1=a1, a2=a2, a3=a3, b=b, B=B, s=s, F=F, L=L)

def a3_mp(alpha):
    mp.mp.dps = 40
    return 3/mp.pi*mp.quad(lambda t: mp.sin(3*t)*(2*mp.sin(t))**alpha, [0, mp.pi/6])

if __name__ == "__main__":
    ver = json.load(open('data/explicit_bounds_intervals.json'))
    alphas = [fmpq(1,1000), fmpq(1,100), fmpq(1,20), fmpq(1,10), fmpq(1,5), fmpq(3,10), fmpq(2,5), fmpq(1,2), fmpq(3,5), fmpq(7,10), fmpq(3,4), fmpq(4,5), fmpq(9,10), fmpq(99,100)]
    out = []
    print(f"{'alpha':>7} {'F (this lane)':>22} {'F (the verification work mid)':>18} {'L (this lane)':>22} {'L (the verification work mid)':>18}  a3 arb vs mpmath")
    vmap = {r['alpha']: r for r in ver['rows']}
    for a in alphas:
        c = consts(a)
        key = str(a)
        vF = vmap[key]['decimal_midpoints']['upper_C'] if key in vmap else '-'
        vL = vmap[key]['decimal_midpoints']['lower_C_and_D'] if key in vmap else '-'
        a3m = a3_mp(mp.mpf(int(a.p))/int(a.q))
        ok = c['a3'].contains(arb(str(a3m))) if False else abs(float(c['a3'].mid()) - float(a3m)) < 1e-30
        print(f"{key:>7} {c['F'].str(16):>22} {vF[:16]:>18} {c['L'].str(16):>22} {vL[:16]:>18}  {'ok' if ok else 'MISMATCH'} |a3-mp|={abs(float(c['a3'].mid())-float(a3m)):.1e}")
        out.append(dict(alpha=key, **{k: v.str(30, radius=True) for k, v in c.items()}))
    json.dump(dict(precision_bits=ctx.prec, note=__doc__, rows=out), open('../runs/certify_bounds.json' if False else 'runs/certify_bounds.json', 'w'), indent=1)
