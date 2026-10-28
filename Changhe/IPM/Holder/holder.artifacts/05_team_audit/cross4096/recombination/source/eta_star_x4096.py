"""Subtract the exact-radial saving eta*_a = J* p/4 + K* q/16 (Theorem 3.9 with the density of V206, accepted with values V210),
p = a(1-a), q = p(2-a)(3-a), from the interpolated cross4096 upper bounds for D (results/v168x4096.json, results/d36x4096.json),
and compare with the accepted V210 safe upper bounds (computed the same way from the cross2048 values).
Output: results/eta_star_x4096.json."""
from flint import arb, ctx
from decimal import Decimal, ROUND_CEILING
from fractions import Fraction as Q
from pathlib import Path
import json, hashlib
ctx.prec = 384
HERE = Path(__file__).resolve().parent
VER = Path('the verification work')
V210 = VER / '08_improved_upper_bounds/local_projection/strict_increment/larger_disks/exact_radial_density/numerical_values/accepted.json'
L43 = (arb(4) / 3).log()
Js = -arb(31) / 32 + arb(27) / 8 * L43
Ks = -arb(233) / 1024 + arb(405) / 512 * L43
assert Js > arb(1) / 512 and Ks > arb(1) / 49152
def eta(a):
    p = a * (1 - a); return Js * p / 4 + Ks * p * (2 - a) * (3 - a) / 16
def ar(x): q = Q(x); return arb(q.numerator) / q.denominator
def ceil10(x): return str(Decimal(x.upper().str(80, radius=False)).quantize(Decimal(10) ** -10, rounding=ROUND_CEILING))
acc = json.load(open(V210)); assert acc['verdict'] == 'CONFIRMED' and acc['ledger'] == 'V210'
v210 = {r['alpha']: r['safe_upper_D'] for r in acc['rows']}
r168 = json.load(open(HERE / 'results/v168x4096.json')); r36 = json.load(open(HERE / 'results/d36x4096.json'))
def rows(R):
    for k in ('rows', 'results'):
        if k in R: return R[k]
    raise KeyError(list(R))
base = {}
for r in rows(r168): base[r['alpha']] = r['pending_interpolated_D_upper']
for r in rows(r36): base[r['alpha']] = r['interpolated_D_upper']
out = []
for a in ['1/5', '3/10', '1/2', '3/4', '9/10', '99/100']:
    e = eta(ar(a)); D = ar(base[a]) - e
    new = ceil10(D)
    out.append(dict(alpha=a, interpolated_D_upper_x4096=base[a], eta_star_ball=str(e), D_upper_x4096_eta_star=new,
                    V210_safe_upper_D=v210[a], improvement=str(Decimal(v210[a]) - Decimal(new))))
    print(a, base[a], new, 'V210', v210[a], 'diff', Decimal(v210[a]) - Decimal(new))
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
json.dump(dict(rows=out, sources={str(V210): sha(V210), 'results/v168x4096.json': sha(HERE / 'results/v168x4096.json'),
               'results/d36x4096.json': sha(HERE / 'results/d36x4096.json')},
               verdict='Lead computation; awaiting verifier audit of the cross4096 certificate.'),
          open(HERE / 'results/eta_star_x4096.json', 'w'), indent=1)
