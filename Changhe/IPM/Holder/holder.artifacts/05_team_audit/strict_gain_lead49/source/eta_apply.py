"""Strict-increment savings (V195: radial density J, symmetric concavity, fourth moment, cutoff form) applied to
the accepted D upper endpoints. Section 3 theorems use the projection decomposition of radius 1/2 at |x-y|=1 (s=1/2):
saving p J s^2 + q K s^4. Theorem 5.7 J_D at rational rho<=1/3 uses the cutoff form
p[J rho^2 - rho^4/(512(1-rho)^2)] + q[K rho^4 - rho^6/(49152(1-rho)^2)].  p=a(1-a), q=p(2-a)(3-a).
New upper = old upper endpoint - lower endpoint of the saving, rounded up at 10 decimals."""
import json, hashlib
from fractions import Fraction
from decimal import Decimal, ROUND_CEILING, getcontext
from flint import arb, ctx
ctx.prec = 256; getcontext().prec = 80
R = ''
L = arb(4) / 3; L = L.log()
J = arb(653) / 288 - arb(63) / 8 * L
K = arb(56627) / 138240 - arb(729) / 512 * L
assert J > 0 and K > 0
def fr(x): x = Fraction(x); return arb(x.numerator) / x.denominator
def lowdec(x):  # exact rational lower bound of an arb
    return Fraction(Decimal(arb(x.lower()).str(60, radius=False)))
def up10(q): return (Decimal(q.numerator) / Decimal(q.denominator)).quantize(Decimal('1e-10'), rounding=ROUND_CEILING)
def sec3(a):
    a = fr(a); p = a * (1 - a); q = p * (2 - a) * (3 - a); s = arb(1) / 2
    return p * J * s**2 + q * K * s**4
def cut(a, rho):
    a = fr(a); r = fr(rho); p = a * (1 - a); q = p * (2 - a) * (3 - a)
    assert r <= arb(1) / 3
    return p * (J * r**2 - r**4 / (512 * (1 - r)**2)) + q * (K * r**4 - r**6 / (49152 * (1 - r)**2))
src = {}
out = []
V190 = R + '05_team_audit/cross2048/recombination/verification/accepted.json'
d = json.load(open(V190)); assert d['verdict'] == 'CONFIRMED' and d['ledger'] == 'V190'; src[V190] = hashlib.sha256(open(V190, 'rb').read()).hexdigest()
for x in d['rows']:
    old = Fraction(Decimal(x['safe_upper_D'])); e = sec3(x['alpha']); el = lowdec(e)
    out.append(dict(alpha=x['alpha'], source='V190 cross2048 Thm 3.6 + 3.8', old_upper_D=x['safe_upper_D'], saving=e.str(15), new_upper_D=str(up10(old - el))))
CC = R + 'data/circle_composite_upper_n768.json'
d = json.load(open(CC)); src[CC] = hashlib.sha256(open(CC, 'rb').read()).hexdigest()
for x in d['rows']:
    if x['alpha'] not in ('1/20', '1/10'): continue
    old = Fraction(Decimal(x['safe_upper_D'])); e = sec3(x['alpha']); el = lowdec(e)
    out.append(dict(alpha=x['alpha'], source='exterior circles Thm 3.5 (n768)', old_upper_D=x['safe_upper_D'], saving=e.str(15), new_upper_D=str(up10(old - el))))
RC = R + '08_improved_upper_bounds/explicit_second_term/verification/rational_cutoffs.json'
d = json.load(open(RC)); src[RC] = hashlib.sha256(open(RC, 'rb').read()).hexdigest()
for x in d['rows']:
    if x['alpha'] not in ('1/1000', '1/100'): continue
    b = x['bounds']['J_D']; old = Fraction(b['upper']); e = cut(x['alpha'], b['rho']); el = lowdec(e)
    out.append(dict(alpha=x['alpha'], source='J_D Thm 5.7(ii), rho=' + b['rho'], old_upper_D=str(up10(old)), saving=e.str(15), new_upper_D=str(up10(old - el))))
for o in out: print(o)
json.dump(dict(J=J.str(30), K=K.str(30), rows=out, inputs_sha256=src,
               code_sha256=hashlib.sha256(open(__file__, 'rb').read()).hexdigest()), open('eta_apply.json', 'w'), indent=1)
