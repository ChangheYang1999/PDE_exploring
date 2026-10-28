# Collect certified upper and lower bounds (interval data) into one table.
# Upper bounds: upper interval endpoint, rounded up at 6 decimals. Lower bounds: lower endpoint, rounded down.
import json, re, math
from fractions import Fraction
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR
D = 'data/'
def parts(s):
    m = re.match(r'\[([-0-9.e]+) \+/- ([0-9.e-]+)\]', s)
    return Decimal(m.group(1)), Decimal(m.group(2))
def lo(s): c, r = parts(s); return c - r
def hi(s): c, r = parts(s); return c + r
up6 = lambda x: Decimal(x).quantize(Decimal('0.000001'), rounding=ROUND_CEILING)
dn6 = lambda x: Decimal(x).quantize(Decimal('0.000001'), rounding=ROUND_FLOOR)
ub = {r['alpha']: r['intervals'] for r in json.load(open(D+'explicit_bounds_intervals.json'))['rows']}
gate = {r['alpha']: r for r in json.load(open(D+'gated_lower_intervals.json'))['rows']}
cusp = {r['alpha']: r for r in json.load(open(D+'cusp_refinement_intervals.json'))['rows']}
hom = {r['alpha']: r for r in json.load(open(D+'homogeneous_lower_intervals.json'))['rows']}
poly = json.load(open(D+'structured_layercake_certificate_fine.json'))
C0 = 0.5 - (1 - math.log(2))/math.pi
print('| alpha | F(alpha) (upper, C) | G = F + 1/2 (upper, D) | best lower L(alpha) for C and D | witness | F/L (upper) | 2/(pi alpha) + C_0 |')
print('|---|---|---|---|---|---|---|')
for a in ub:
    al = float(Fraction(a))
    F = up6(hi(ub[a]['upper_C'])); G = up6(hi(ub[a]['upper_D']))
    cands = []
    if a in gate: q = Fraction(gate[a]['safe_decimal_lower_10_places']); cands.append((Decimal(q.numerator)/Decimal(q.denominator), 'gated'))
    if a in cusp: cands.append((lo(cusp[a]['C_and_D_lower_interval']), 'two-cusp L_2'))
    if a in hom: cands.append((lo(hom[a]['C_lower_interval']), 'degree-3 homogeneous'))
    if a == poly['alpha']: cands.append((Decimal(poly['safe_decimal_lower_10_places']), 'polygonal signed distance'))
    L, w = max(cands)
    L = dn6(L)
    ratio = (F/L).quantize(Decimal('0.0001'), rounding=ROUND_CEILING)
    print(f'| {a} | {F} | {G} | {L} | {w} | {ratio} | {2/(math.pi*al)+C0:.4f} |')
