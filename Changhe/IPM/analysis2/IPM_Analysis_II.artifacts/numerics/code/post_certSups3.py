"""Frobenius recombination of the C2 cells from the saved scalar component upper bounds (verifier V094's method, recomputed independently):
|D^d rho|_F <= sqrt(sum_i C(d,i) b_(i,d-i)^2) with b the saved component uppers (binary64, taken as exact rationals), outward square root;
|D^d U|_F <= sqrt(sum over both components). Weighted by (1+4 r_hi^2)^0.4 (origin square: (1+8 r0^2)^0.4). Decimals rounded UP (checked).
Usage: post_certSups3.py in.jsonl out.json"""
import sys, json, math
from fractions import Fraction as Fr
from decimal import Decimal, ROUND_CEILING, getcontext
getcontext().prec = 50
rows = [json.loads(l) for l in open(sys.argv[1]) if l.strip()]
seen = set(); uniq = []
for r in rows:
    if r['status'] != 'ok' or (r['i'], r['k']) in seen: continue
    seen.add((r['i'], r['k'])); uniq.append(r)
def up_sqrt(q):            # Decimal upper bound of sqrt of a Fraction
    d = Decimal(q.numerator)/Decimal(q.denominator); s = d.sqrt()
    while s*s < d: s = s.next_plus()
    return s
def up_pow04(r_hi, square):   # upper bound of (1 + c r_hi^2)^0.4, c = 4 (disk) or 8 (origin square), via float with 3 ulps outward
    v = (1 + (8 if square else 4)*r_hi*r_hi)**0.4
    for _ in range(3): v = math.nextafter(v, math.inf)
    return v
res = {}
for d in (1, 2):
    for fld in ('rho', 'U'):
        best = Fr(0); bestw = Decimal(0); cell = None; cellw = None; nfin = 0
        for r in uniq:
            comps = []
            for i in range(d+1):
                names = ['rho_%d_%d' % (i, d-i)] if fld == 'rho' else ['U1_%d_%d' % (i, d-i), 'U2_%d_%d' % (i, d-i)]
                for nm in names:
                    v = r[nm]
                    if not (isinstance(v, (int, float)) and math.isfinite(v)): comps = None; break
                    comps.append((math.comb(d, i), Fr(v)))
                if comps is None: break
            if comps is None: continue
            nfin += 1
            q = sum(c*b*b for c, b in comps)
            w = Decimal(repr(up_pow04(r['r_hi'], r['r_lo'] == 0.0)))
            if q > best: best = q; cell = r
            s = up_sqrt(q)*w
            if s > bestw: bestw = s; cellw = r
        sb = up_sqrt(best)
        def pubup(x, sig=6):
            e = x.adjusted(); qq = Decimal(1).scaleb(e - sig + 1); c = x.quantize(qq, rounding=ROUND_CEILING)
            return str(c)
        key = 'D%d_%s' % (d, fld)
        res[key] = {'Frob_upper': pubup(sb), 'wFrob_upper': pubup(bestw), 'cells_with_finite_components': nfin, 'Frob_cell_r': [cell['r_lo'], cell['r_hi']], 'wFrob_cell_r': [cellw['r_lo'], cellw['r_hi']]}
        print('%s: |.|_F <= %s (cell r in [%g, %g]) ; weighted <= %s (cell r in [%g, %g]) ; cells %d of %d' % (key, pubup(sb), cell['r_lo'], cell['r_hi'], pubup(bestw), cellw['r_lo'], cellw['r_hi'], nfin, len(uniq)))
json.dump(res, open(sys.argv[2], 'w'), indent=1)
