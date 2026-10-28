"""Byproducts of a cert_M covering (JSON lines of cert_M.py) evaluated EXACTLY (Fractions) from the stored outward-rounded endpoints:
 (B2)  A = [[rho_y, -rho_x/2], [-rho_x/2, 0]] >= -(1/20) I  <=>  rho_x^2 <= rho_y/5 + 1/100   (given rho_y >= -1/10; proof: lambda_min(A) =
       (rho_y - sqrt(rho_y^2 + rho_x^2))/2 >= -1/20  <=>  sqrt(rho_y^2 + rho_x^2) <= rho_y + 1/10  <=>  rho_x^2 <= rho_y/5 + 1/100 when rho_y + 1/10 >= 0).
       Per cell the test uses max |rho_x| over the enclosure and the lower bound of rho_y: sufficient on the cell.
 (symDU) lambda_max(sym DU) = sqrt(DU11^2 + ((DU12 + DU21)/2)^2) because tr DU = 0 (U divergence free: DU11 = -psi_xy = -DU22 exactly);
       per cell: sqrt(max|DU11|^2 + max|(DU12+DU21)/2|^2) with the maxima over the enclosures (a bound, since both DU11 and DU22 enclosures are rigorous:
       we use max over both |DU11| and |DU22| to be safe).
 (rho_y) positivity of rho_y on the cells.
 Far field (r >= R): from farfield_M_cert json: |rho_x| <= B_rho_x r^(gamma-1) <= B_rho_x R^(gamma-1) (gamma < 1), rho_y >= c r^(gamma-1) > 0 for all r >= R.
 Directed rounding: the far-field numbers are evaluated in arb (128 bits) and compared as rationals; printed decimals are rounded in the safe direction.
 Coverage/row audit: rows with status != ok or split are counted and reported; the coverage of the depth-0 cells by accepted leaves is checked as in post_certM.py.
Usage: post_certM_B2.py cells.jsonl farfield.json cl out.json
"""
import sys, json, math
from fractions import Fraction as Fr
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR
from collections import defaultdict
from flint import arb, ctx

def dn(x, d=6):
    """decimal string rounded DOWN (safe for lower bounds / margins)"""
    q = Decimal(1).scaleb(-d); return str(Decimal(Fr(x).numerator)/Decimal(Fr(x).denominator)).__class__(Decimal(Fr(x).numerator)/Decimal(Fr(x).denominator)).quantize(q, rounding=ROUND_FLOOR) if False else format((Decimal(Fr(x).numerator)/Decimal(Fr(x).denominator)).quantize(q, rounding=ROUND_FLOOR), 'f')
def up(x, d=6):
    """decimal string rounded UP (safe for upper bounds)"""
    q = Decimal(1).scaleb(-d); return format((Decimal(Fr(x).numerator)/Decimal(Fr(x).denominator)).quantize(q, rounding=ROUND_CEILING), 'f')

def main(path, ffpath, cl, out_json):
    cl = Fr(cl); gamma = 1/cl
    rows = [json.loads(l) for l in open(path) if l.strip()]
    origin = [r for r in rows if 'origin_box_h' in r]
    allcells = [r for r in rows if 'origin_box_h' not in r]
    cells = [r for r in allcells if r['status'] == 'ok' and not r.get('split')]
    nbad = sum(1 for r in allcells if r['status'] != 'ok'); nsplit = sum(1 for r in allcells if r.get('split'))
    cov = defaultdict(float)
    for r in cells: cov[(r['i'], r['k'])] += (math.log(r['r_hi']) - math.log(r['r_lo']))*(r['t_hi'] - r['t_lo'])
    top = {(r['i'], r['k']): (math.log(r['r_hi']) - math.log(r['r_lo']))*(r['t_hi'] - r['t_lo']) for r in allcells if r['depth'] == 0}
    uncovered = [k for k, v in top.items() if abs(cov.get(k, 0) - v) > 1e-9*v]
    print('rows: %d cells (%d accepted leaves, %d split parents, %d non-ok), %d origin boxes; depth-0 cells %d, not covered by accepted leaves: %d' % (len(allcells), len(cells), nsplit, nbad, len(origin), len(top), len(uncovered)))
    def F(x): return Fr(x)
    res = {}
    # (B2)
    worst = None; nfail = 0; fails = []
    for r in cells + origin:
        rxm = max(abs(F(r['rho_x_lo'])), abs(F(r['rho_x_hi'])))
        m = F(r['rho_y_lo'])/5 + Fr(1, 100) - rxm*rxm
        if worst is None or m < worst[0]: worst = (m, r)
        if m <= 0:
            nfail += 1; fails.append(r)
    w = worst[1]
    loc = ('origin h=%g' % w['origin_box_h']) if 'origin_box_h' in w else ('r in [%g, %g], theta in [%.4f, %.4f]' % (w['r_lo'], w['r_hi'], w['t_lo'], w['t_hi']))
    print('(B2) test rho_x^2 <= rho_y/5 + 1/100 on %d cells + %d origin boxes: failing cells %d; smallest margin >= %s (exact rational, printed rounded down) at %s' % (len(cells), len(origin), nfail, dn(worst[0], 7), loc))
    res['B2'] = {'n_cells': len(cells), 'n_origin': len(origin), 'n_fail': nfail, 'min_margin': float(worst[0]), 'worst_cell': {k: w[k] for k in ('r_lo', 'r_hi', 't_lo', 't_hi') if k in w},
                 'fail_cells': [{k: r[k] for k in ('r_lo', 'r_hi', 't_lo', 't_hi', 'rho_x_lo', 'rho_x_hi', 'rho_y_lo', 'rho_y_hi') if k in r} for r in fails[:200]]}
    # exact lambda_min(A) lower bound per cell (diagnostic, float): (rho_y_lo - sqrt(rho_y_hi^2 + rxm^2))/2 is the crude one; the sharp one from the scalar test:
    # lambda_min(A) >= -(1/2) * rxm^2 / (rho_y_lo + sqrt(rho_y_lo^2 + rxm^2))  (monotone in rho_y for fixed rxm; valid when rho_y_lo >= 0)
    lamA = []
    for r in cells + origin:
        rxm = max(abs(r['rho_x_lo']), abs(r['rho_x_hi'])); ry = r['rho_y_lo']
        if ry >= 0: lamA.append(((-0.5*rxm*rxm/(ry + math.hypot(ry, rxm))) if (ry > 0 or rxm > 0) else 0.0, r))
        else: lamA.append(((ry - math.hypot(max(abs(r['rho_y_lo']), abs(r['rho_y_hi'])), rxm))/2, r))
    la, lr = min(lamA, key=lambda t: t[0])
    print('lambda_min(A) >= %.6f on the covered region (FLOAT evaluation of the per-cell sharp formula; the exact (B2) test above is the certificate) at r in [%g, %g]' % (la, lr.get('r_lo', 0), lr.get('r_hi', lr.get('origin_box_h', 0))))
    res['lambda_min_A_float'] = la
    # sym DU
    best = 0; bw = None
    for r in cells + origin:
        d = max(abs(F(r['DU11_lo'])), abs(F(r['DU11_hi'])), abs(F(r['DU22_lo'])), abs(F(r['DU22_hi'])))
        s = max(abs(F(r['DU12_lo']) + F(r['DU21_lo'])), abs(F(r['DU12_hi']) + F(r['DU21_hi'])), abs(F(r['DU12_lo']) + F(r['DU21_hi'])), abs(F(r['DU12_hi']) + F(r['DU21_lo'])))/2
        v = d*d + s*s
        if v > best: best = v; bw = r
    sq = math.nextafter(math.sqrt(float(best)), math.inf)*(1 + 2**-50) if best > 0 else 0.0
    assert Fr(sq)*Fr(sq) >= best, 'sqrt upper bound failed the exact check'
    if bw is None: bw = cells[0]
    print('||sym DU||_2 = lambda_max(sym DU) <= %s on the covered region (sqrt of the exact max of DU11^2 + s^2, rounded up, checked exactly: sq^2 >= max; 17/20 = 0.85) at r in [%g, %g]' % (up(sq, 6), bw.get('r_lo', 0), bw.get('r_hi', bw.get('origin_box_h', 0))))
    res['symDU_upper'] = sq
    # rho_y positivity
    mr = min(cells + origin, key=lambda r: r['rho_y_lo'])
    print('min over cells of the rho_y lower bound: %.6g at r in [%g, %g]' % (mr['rho_y_lo'], mr.get('r_lo', 0), mr.get('r_hi', mr.get('origin_box_h', 0))))
    res['rho_y_min_lower'] = mr['rho_y_lo']
    # far field (arb 128 bits, outward; the file keys are str(float(R)))
    ff = json.load(open(ffpath)); Rk = max(ff, key=lambda k: float(k)); R = float(Rk); e = ff[Rk]
    ctx.prec = 128
    g1 = arb(gamma.numerator)/gamma.denominator - 1          # gamma - 1 < 0
    def hi(v): return Fr(math.nextafter(float(v.upper()), math.inf))
    pw = arb(R)**g1
    B = e['bounds_coef_r^(gamma-1)']
    rx_hi = hi(arb(B['rho_x'])*pw)                            # |rho_x| <= rx_hi for all r >= R
    margin_ff = Fr(1, 100) - rx_hi*rx_hi                       # (B2) margin for r >= R (rho_y > 0 there)
    du11_hi = hi(arb(B['DU11'])*pw); s_hi = hi((arb(B['DU12']) + arb(B['DU21']))/2*pw)
    symdu_ff = hi((arb(float(du11_hi))**2 + arb(float(s_hi))**2).sqrt())
    ryc = e['rho_y_coef_lower']
    assert ryc > 0 and margin_ff > 0
    print('far field r >= %g: |rho_x| <= %s for all r >= R (B r^(gamma-1) decreasing), rho_y >= %s r^(gamma-1) > 0: (B2) margin >= 1/100 - rho_x^2 >= %s; |DU11| <= %s, |(DU12+DU21)/2| <= %s -> ||sym DU|| <= %s  (arb 128 bits, outward, printed in the safe direction)' % (
        R, up(rx_hi, 6), dn(Fr(ryc), 4), dn(margin_ff, 7), up(du11_hi, 6), up(s_hi, 6), up(symdu_ff, 6)))
    res['farfield'] = {'R': R, 'rho_x_max_upper': float(rx_hi), 'rho_y_coef_lower': ryc, 'B2_margin_lower': float(margin_ff), 'symDU_upper': float(symdu_ff)}
    res['rows'] = {'cells': len(allcells), 'accepted': len(cells), 'split': nsplit, 'non_ok': nbad, 'origin_boxes': len(origin), 'depth0': len(top), 'uncovered_depth0': len(uncovered)}
    json.dump(res, open(out_json, 'w'), indent=1)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
