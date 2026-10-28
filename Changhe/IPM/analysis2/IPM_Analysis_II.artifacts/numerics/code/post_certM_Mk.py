"""Hypotheses (B4), (B5), (B6) of S1_CLOSURE section 3 evaluated from the stored cell enclosures of a cert_M covering (arb interval arithmetic on the
outward-rounded endpoints; the cell's x, y ranges from the polar cell with arb cos/sin of the exact rational angles, enlarged outward):
  (B4) M_1 = I - sym DU + A >= (9/10) I,
  (B5) M_2 = (1 + c_l + V.grad log omega) I - 2 sym DV + A >= (1/2) I,
  (B6) M_3 = (1 + c_l + V.grad log omega) I - 3 sym DV + A >= -(5/4) I,
with A = [[rho_y, -rho_x/2], [-rho_x/2, 0]], V = c_l X + U, DV = c_l I + DU, omega = (1 + 4 r^2)^(2/5), so
V.grad log omega = (16/5) (V.X)/(1 + 4 r^2), V.X = c_l r^2 + x U1 + y U2.
Per cell every field is an arb ball covering its enclosure; lambda_min of the symmetric 2x2 matrix [[a, b], [b, d]] is (a + d)/2 - sqrt(((a - d)/2)^2 + b^2),
evaluated in arb; a cell PASSES when the lower endpoint exceeds the target. Failing cells are listed (they need re-enclosure on sub-boxes; not done here).
Far field: not treated here (the hypotheses at infinity: M_1 -> I, M_2 -> (1 + c_l + (16/5) c_l/4 - 2 c_l) I = (1 - c_l + (4/5) c_l) I = (1 - c_l/5) I = 0.638 I,
M_3 -> (1 - c_l + (4/5)c_l - c_l) I = (1 - (6/5) c_l) I = -1.17 I; the certificate here is for the covered region 0 <= r <= 10066.9 only).
Usage: post_certM_Mk.py cells.jsonl cl out.json
"""
import sys, json, math
from fractions import Fraction as Fr
from flint import arb, ctx

def ball(lo, hi):
    lo = arb(lo); hi = arb(hi)
    return arb.union(lo, hi) if hasattr(arb, 'union') else (lo + hi)/2 + arb(0, (float(hi - lo)/2)*(1 + 2**-40))

def lam_min(a, b, d):
    """rigorous LOWER bound (binary64, rounded down) of lambda_min([[a, b], [b, d]]) over the balls a, b, d: (a + d)/2 - sqrt(((a - d)/2)^2 + b^2);
    the discriminant ball may straddle 0 when a - d and b do (arb squares of such balls contain negative numbers), so its square root is taken at the
    nonnegative upper endpoint."""
    half = (a - d)/2
    disc = half*half + b*b
    du = float(disc.upper()); du = du if du > 0 else 0.0
    root_hi = math.nextafter(float(arb(du).sqrt().upper()), math.inf)
    return math.nextafter(float(((a + d)/2).lower()), -math.inf) - root_hi

def main(path, cl, out_json):
    ctx.prec = 128
    cl = Fr(cl); CL = arb(cl.numerator)/cl.denominator
    rows = [json.loads(l) for l in open(path) if l.strip()]
    cells = [r for r in rows if 'origin_box_h' not in r and r['status'] == 'ok' and not r.get('split')]
    origin = [r for r in rows if 'origin_box_h' in r]
    targets = {'B4': Fr(9, 10), 'B5': Fr(1, 2), 'B6': Fr(-5, 4)}
    worst = {k: None for k in targets}; fails = {k: [] for k in targets}
    def enc(r, key): return ball(r[key+'_lo'], r[key+'_hi'])
    def xy_ranges(r):
        if 'origin_box_h' in r:
            h = arb(r['origin_box_h'])*(1 + arb(2)**-30)
            return arb(0, float(h)), arb(0, float(h))      # x, y in [-h, h] (first-quadrant parity makes this fine)
        tl = arb(Fr(r['t_lo']).numerator)/Fr(r['t_lo']).denominator; th = arb(Fr(r['t_hi']).numerator)/Fr(r['t_hi']).denominator
        rl = arb(Fr(r['r_lo']).numerator)/Fr(r['r_lo']).denominator; rh = arb(Fr(r['r_hi']).numerator)/Fr(r['r_hi']).denominator
        xlo = rl*th.cos() if r['t_hi'] < math.pi/2 else arb(0); xhi = rh*tl.cos()
        ylo = rl*tl.sin() if r['t_lo'] > 0 else arb(0); yhi = rh*th.sin()
        xlo = xlo.lower() if float(xlo.lower()) > 0 else arb(0); ylo = ylo.lower() if float(ylo.lower()) > 0 else arb(0)
        return arb.union(arb(xlo), arb(xhi.upper())), arb.union(arb(ylo), arb(yhi.upper()))
    n = 0
    for r in cells + origin:
        n += 1
        DU11, DU12, DU21, DU22 = enc(r, 'DU11'), enc(r, 'DU12'), enc(r, 'DU21'), enc(r, 'DU22')
        rx, ry = enc(r, 'rho_x'), enc(r, 'rho_y'); U1, U2 = enc(r, 'U1'), enc(r, 'U2')
        x, y = xy_ranges(r)
        s = (DU12 + DU21)/2
        # (B4)
        l4 = lam_min(1 - DU11 + ry, -s - rx/2, 1 - DU22)
        # weighted ones
        # radial range of the box: r2 in [r_lo^2, r_hi^2] for a polar cell, [0, 2h^2] for the origin square; f(r2) = r2/(1 + 4 r2) is increasing,
        # so c_l f(r2) is enclosed by its values at the endpoints (no interval dependency); the small term (x U1 + y U2)/(1 + 4 r2) uses the balls.
        if 'origin_box_h' in r:
            r2lo = arb(0); r2hi = 2*arb(r['origin_box_h'])**2*(1 + arb(2)**-30)
        else:
            r2lo = (arb(Fr(r['r_lo']).numerator)/Fr(r['r_lo']).denominator)**2; r2hi = (arb(Fr(r['r_hi']).numerator)/Fr(r['r_hi']).denominator)**2
        r2 = arb.union(arb(r2lo.lower()), arb(r2hi.upper()))
        f_lo = r2lo/(1 + 4*r2lo); f_hi = r2hi/(1 + 4*r2hi)
        fr = arb.union(arb(f_lo.lower()), arb(f_hi.upper()))
        w = (arb(16)/5)*(CL*fr + (x*U1 + y*U2)/(1 + 4*r2))
        base = 1 + CL + w
        l5 = lam_min(base - 2*(CL + DU11) + ry, -2*s - rx/2, base - 2*(CL + DU22))
        l6 = lam_min(base - 3*(CL + DU11) + ry, -3*s - rx/2, base - 3*(CL + DU22))
        for k, lm in (('B4', l4), ('B5', l5), ('B6', l6)):
            lo = Fr(math.nextafter(lm, -math.inf))
            if worst[k] is None or lo < worst[k][0]: worst[k] = (lo, r)
            if lo <= targets[k]: fails[k].append((float(lo), r))
    res = {}
    for k in targets:
        lo, r = worst[k]
        loc = ('origin h=%g' % r['origin_box_h']) if 'origin_box_h' in r else ('r in [%g, %g], theta in [%.4f, %.4f]' % (r['r_lo'], r['r_hi'], r['t_lo'], r['t_hi']))
        print('%s target %s: boxes %d, failing %d, worst lower bound %.6f at %s' % (k, targets[k], n, len(fails[k]), float(lo), loc))
        fl = sorted(fails[k], key=lambda t: t[0])
        if fl:
            rs = [t[1] for t in fl if 'origin_box_h' not in t[1]]
            if rs: print('   failing cells: r from %g to %g, theta from %.3f to %.3f; worst margin %.3g' % (min(c['r_lo'] for c in rs), max(c['r_hi'] for c in rs), min(c['t_lo'] for c in rs), max(c['t_hi'] for c in rs), fl[0][0] - float(targets[k])))
        res[k] = {'target': str(targets[k]), 'n_boxes': n, 'n_fail': len(fails[k]), 'worst_lower': float(lo), 'worst_cell': {kk: r[kk] for kk in ('r_lo', 'r_hi', 't_lo', 't_hi', 'origin_box_h') if kk in r},
                  'fail_cells': [{kk: c[kk] for kk in ('i', 'k', 'depth', 'r_lo', 'r_hi', 't_lo', 't_hi') if kk in c} | {'lower': v} for v, c in fl[:5000]]}
    json.dump(res, open(out_json, 'w'), indent=1)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
