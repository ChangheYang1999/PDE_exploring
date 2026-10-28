"""Post-process data/certM_088.jsonl: global certified lower bound of lambda_min(M), coverage check, near-origin constants (N4),
rho_y positivity, K_bar positivity, and a summary JSON. Also reports the worst cells and the remainders."""
import sys, os, json, math
import numpy as np
from collections import defaultdict

def main(path, farfield_json, cl, a0, out_json, Rmax_boxes=1e4):
    rows = [json.loads(l) for l in open(path) if l.strip()]
    origin = [r for r in rows if 'origin_box_h' in r]
    cells = [r for r in rows if 'origin_box_h' not in r]
    accepted = [r for r in cells if r['status'] == 'ok' and not r.get('split')]
    errors = [r for r in cells if r['status'] != 'ok']
    print('rows %d, origin boxes %d, cells %d (accepted %d, split %d, errors %d)' % (len(rows), len(origin), len(cells), len(accepted), sum(1 for r in cells if r.get('split')), len(errors)))
    # coverage: the accepted cells must cover every depth-0 cell exactly (children cover parents); check per depth-0 cell that area is covered
    cov = defaultdict(float)
    for r in accepted: cov[(r['i'], r['k'])] += (math.log(r['r_hi']) - math.log(r['r_lo']))*(r['t_hi'] - r['t_lo'])
    top = {(r['i'], r['k']): (math.log(r['r_hi']) - math.log(r['r_lo']))*(r['t_hi'] - r['t_lo']) for r in cells if r['depth'] == 0}
    bad = [k for k, v in top.items() if abs(cov.get(k, 0) - v) > 1e-9*v]
    print('depth-0 cells: %d; cells whose accepted descendants do not cover them: %d' % (len(top), len(bad)))
    r_lo_all = min(r['r_lo'] for r in cells); r_hi_all = max(r['r_hi'] for r in cells)
    print('radial range of cells: [%g, %g]; angular range [%g, %g]' % (r_lo_all, r_hi_all, min(r['t_lo'] for r in cells), max(r['t_hi'] for r in cells)))
    lam_cells = min(r['lam_min_lo'] for r in accepted)
    worst = min(accepted, key=lambda r: r['lam_min_lo'])
    print('min over accepted cells of lambda_min lower bound: %.9f at r in [%g, %g], theta in [%.4f, %.4f] (depth %d)' % (lam_cells, worst['r_lo'], worst['r_hi'], worst['t_lo'], worst['t_hi'], worst['depth']))
    for o in origin: print('origin box h=%g: lambda_min >= %.9f' % (o['origin_box_h'], o['lam_min_lo']))
    ff = json.load(open(farfield_json))
    lam_far = ff[str(float(Rmax_boxes))]['lambda_min_lower_bound'] if str(float(Rmax_boxes)) in ff else ff['10000.0']['lambda_min_lower_bound']
    print('far field r >= %g: lambda_min >= %.6f' % (Rmax_boxes, lam_far))
    orig_h = min(o['origin_box_h'] for o in origin if o['origin_box_h'] >= r_lo_all) if any(o['origin_box_h'] >= r_lo_all for o in origin) else None
    orig_ok = [o['lam_min_lo'] for o in origin if o['origin_box_h'] >= r_lo_all]
    lam_origin = max(orig_ok) if orig_ok else float('inf')      # a covering that starts away from 0 (far extension) has no origin square to use
    m0 = min(lam_cells, lam_origin, lam_far) - 1e-9
    print(('GLOBAL' if orig_ok else 'ON THE COVERED RADII [%g, %g] AND BEYOND %g' % (r_lo_all, r_hi_all, Rmax_boxes)) + ': inf lambda_min(M(X)) >= %.9f  (origin square half-width %s: %s; cells: %.9f; far field: %.6f; minus 1e-9 float slack)' % (m0, orig_h, ('%.9f' % lam_origin) if orig_ok else 'none', lam_cells, lam_far))
    # positivity of rho_y and of M22 - (cl+2)
    print('min over cells of rho_y lower bound: %.6g (at r in [%g,%g])' % (min(r['rho_y_lo'] for r in accepted), *[(r['r_lo'], r['r_hi']) for r in [min(accepted, key=lambda r: r['rho_y_lo'])]][0]))
    print('min over cells of M22-(cl+2) lower bound: %.6g' % min(r['M22_minus_cl2_lo'] for r in accepted))
    # K_bar positivity away from the x-axis: cells with t_lo > 0
    Kneg = [r for r in accepted if r['t_lo'] > 1e-12 and r['K_lo'] <= 0]
    print('cells with t_lo > 0 and K_bar lower bound <= 0: %d (of %d); smallest r among them: %s' % (len(Kneg), sum(1 for r in accepted if r['t_lo'] > 1e-12), min((r['r_lo'] for r in Kneg), default=None)))
    # global sup of lambda_max(sym DU) over cells (cross-check of the verifier's 17/20): sym DU = [[DU11, (DU12+DU21)/2],[., DU22]]
    def lmax_symDU(r):
        a = max(abs(r['DU11_lo']), abs(r['DU11_hi'])); d = max(abs(r['DU22_lo']), abs(r['DU22_hi']))
        b = max(abs(r['DU12_lo'] + r['DU21_lo']), abs(r['DU12_hi'] + r['DU21_hi']), abs(r['DU12_lo'] + r['DU21_hi']), abs(r['DU12_hi'] + r['DU21_lo']))/2
        return max(a, d) + b        # crude: lambda_max <= max diagonal magnitude + |offdiag|
    print('cells: max over cells of a bound for ||sym DU||_2 (max|diag| + |offdiag|): %.5f' % max(lmax_symDU(r) for r in accepted))
    # min eigenvalue of A = [[rho_y, -rho_x/2],[-rho_x/2, 0]] over cells: lambda_min(A) = (rho_y - sqrt(rho_y^2 + rho_x^2))/2 >= (rho_y_lo - sqrt(rho_y_hi^2 + rho_x_max^2))/2
    def lminA(r):
        rxm = max(abs(r['rho_x_lo']), abs(r['rho_x_hi'])); return (r['rho_y_lo'] - math.sqrt(max(r['rho_y_hi'], abs(r['rho_y_lo']))**2 + rxm**2))/2
    wa = min(accepted, key=lminA)
    print('cells: min over cells of lambda_min(A) lower bound: %.6f at r in [%g,%g] theta in [%.3f,%.3f] (verifier: A >= -1/20 I?)' % (lminA(wa), wa['r_lo'], wa['r_hi'], wa['t_lo'], wa['t_hi']))
    # near-origin constants N4 on disks r <= r0 (cells with r_hi <= r0, plus the origin square of half-width h0 <= r0/sqrt2 ... we report cells only, with the origin box separately)
    out = {'m0': m0, 'lambda_cells': lam_cells, 'lambda_origin': lam_origin, 'lambda_far': lam_far, 'origin_half_width': orig_h, 'n_accepted_cells': len(accepted), 'errors': len(errors), 'uncovered': len(bad)}
    DU0 = {'DU11': cl - 1, 'DU22': 1 - cl, 'DU12': 0.0, 'DU21': 0.0}
    from fractions import Fraction as Fr
    from decimal import Decimal, ROUND_CEILING
    def up(x, d=5):
        q = Decimal(1).scaleb(-d); return format((Decimal(Fr(x).numerator)/Decimal(Fr(x).denominator)).quantize(q, rounding=ROUND_CEILING), 'f')
    CLF = Fr(cl); A0F = Fr(a0)
    for r0 in (0.05, 0.1, 0.2, 0.5, 1.0):
        sel = [r for r in accepted if r['r_hi'] <= r0*(1 + 1e-12)]
        if not sel: continue
        r_end = max(Fr(r['r_hi']) for r in sel); rmin = min(Fr(r['r_lo']) for r in sel)
        # exact rational constants from the stored outward-rounded endpoints (sup over the cell divided by r_lo^power is valid on the cell)
        c_rhoy = max(max(abs(Fr(r['rho_y_lo']) - A0F), abs(Fr(r['rho_y_hi']) - A0F))/Fr(r['r_lo'])**2 for r in sel)
        c_rhox = max(max(abs(Fr(r['rho_x_lo'])), abs(Fr(r['rho_x_hi'])))/Fr(r['r_lo'])**2 for r in sel)
        DU0F = {'DU11': CLF - 1, 'DU22': 1 - CLF, 'DU12': Fr(0), 'DU21': Fr(0)}
        c_DU = max(max(max(abs(Fr(r[k+'_lo']) - DU0F[k]), abs(Fr(r[k+'_hi']) - DU0F[k])) for k in DU0F)/Fr(r['r_lo'])**2 for r in sel)
        print('N4 on the union of the cells with r_hi <= %g, i.e. on %r <= r <= %r (exact binary64 endpoints of the covered union; a0, c_l as given): |rho_y - a0| <= %s r^2 ; |rho_x| <= %s r^2 ; |DU - DU(0)| (max entry) <= %s r^2   [exact rationals of the stored endpoints, printed rounded up]' % (r0, float(rmin), float(r_end), up(c_rhoy), up(c_rhox), up(c_DU)))
        out['N4_r0_%g' % r0] = {'r_min': float(rmin), 'r_end_actual': float(r_end), 'r_end_actual_repr': repr(float(r_end)), 'c_rho_y_upper': up(c_rhoy), 'c_rho_x_upper': up(c_rhox), 'c_DU_upper': up(c_DU),
                                'note': 'valid on r_min <= r <= r_end_actual (union of accepted cells with r_hi <= r0); the inputs a0 and cl are the binary64 arguments'}
    json.dump(out, open(out_json, 'w'), indent=1)

if __name__ == '__main__':
    # usage: post_certM.py cells.jsonl farfield.json summary.json [cl a0]   (defaults: state 88; state 131: 1.810319210199998 10.300294891831177)
    cl = float(sys.argv[4]) if len(sys.argv) > 4 else 1.8085383949271123
    a0 = float(sys.argv[5]) if len(sys.argv) > 5 else 10.29757491765872
    main(sys.argv[1], sys.argv[2], cl, a0, sys.argv[3])
