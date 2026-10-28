"""Decay constants of the lead's (W1) list (S1_CLOSURE: delta = 2/5): sup_X r^delta |D rho|_F, sup_X r^(delta-1) |U|, sup_X r^delta |DU|_F, from the stored cell
enclosures of the cert_M coverings (inner 0.005 <= r <= 10066.9 and far 10^4 <= r <= 1.00888e6), the near-origin Taylor constants of C3-131 for r <= 0.005 (for the
|U| term, whose weight is singular at 0), and the exterior sector coefficient bounds for r >= 10^6 (farfield_Mk_cert json, field 'coef': |f| <= B_f r^(gamma-1) for
D rho and DU, |U_i| <= B_Ui r^gamma). Exact rational arithmetic on the outward-rounded endpoints; powers of r in arb (128 bits), outward; printed rounded up.
Per polar cell: r^delta |Drho| <= r_hi^delta sqrt(max|rho_x|^2 + max|rho_y|^2); r^(delta-1) |U| <= r_lo^(delta-1) sqrt(max|U1|^2 + max|U2|^2); r^delta |DU|_F <=
r_hi^delta sqrt(sum_ij max|DU_ij|^2). Origin square [-h, h]^2 (r <= sqrt2 h): the two delta-weighted terms with r_hi = sqrt2 h; the |U| term from C3-131:
|U| <= (c_l - 1) r + sqrt2 * 0.283275 r^3 on r <= 0.05, so r^(delta-1)|U| <= (c_l - 1) r^delta + 0.4007 r^(2 + delta) is increasing and bounded by its value at r = sqrt2 h.
Exterior r >= R: r^delta B r^(gamma-1) = B r^(gamma - 1 + delta) with gamma - 1 + delta < 0, decreasing, so bounded by the value at R; same for B_U r^(gamma + delta - 1).
NOT covered here: the r^(1+delta)|D^2 rho| part of the first (W1) constant and the |D^2 u| constant (second derivatives are not in these cell files).
Usage: post_certM_decay.py inner.jsonl far.jsonl farfield_Mk.json cl R_exterior out.json
"""
import sys, json, math
from fractions import Fraction as Fr
from decimal import Decimal, ROUND_CEILING
from flint import arb, ctx

def up(x, d=5):
    q = Decimal(1).scaleb(-d); return format((Decimal(Fr(x).numerator)/Decimal(Fr(x).denominator)).quantize(q, rounding=ROUND_CEILING), 'f')
def hi(v): return Fr(math.nextafter(float(v.upper()), math.inf))
def ar(fr): return arb(fr.numerator)/fr.denominator
def sqrt_up(fr):
    r = math.nextafter(math.sqrt(float(fr)), math.inf)*(1 + 2**-50); assert Fr(r)*Fr(r) >= fr; return Fr(r)

def main(inner, far, ffjson, cl, R, out_json):
    ctx.prec = 128
    cl = Fr(cl); gamma = 1/cl; delta = Fr(2, 5)
    rows = [json.loads(l) for f in (inner, far) for l in open(f) if l.strip()]
    cells = [r for r in rows if 'origin_box_h' not in r and r['status'] == 'ok' and not r.get('split')]
    origin = [r for r in rows if 'origin_box_h' in r]
    def mx(r, k): return max(abs(Fr(r[k+'_lo'])), abs(Fr(r[k+'_hi'])))
    best = {'Drho': (Fr(0), None), 'U': (Fr(0), None), 'DU': (Fr(0), None)}
    for r in cells:
        rlo = Fr(r['r_lo']); rhi = Fr(r['r_hi'])
        w_hi = hi(ar(rhi)**ar(delta)); w_lo = hi(ar(rlo)**ar(delta - 1))
        drho = w_hi*sqrt_up(mx(r, 'rho_x')**2 + mx(r, 'rho_y')**2)
        u = w_lo*sqrt_up(mx(r, 'U1')**2 + mx(r, 'U2')**2)
        du = w_hi*sqrt_up(sum(mx(r, k)**2 for k in ('DU11', 'DU12', 'DU21', 'DU22')))
        for key, v in (('Drho', drho), ('U', u), ('DU', du)):
            if v > best[key][0]: best[key] = (v, r)
    # origin square: smallest h only (the covering of cells starts at r = h)
    h = min(Fr(o['origin_box_h']) for o in origin); o = [x for x in origin if Fr(x['origin_box_h']) == h][0]
    rmax = hi(ar(h)*arb(2).sqrt())
    w_hi = hi(ar(rmax)**ar(delta))
    drho0 = w_hi*sqrt_up(mx(o, 'rho_x')**2 + mx(o, 'rho_y')**2); du0 = w_hi*sqrt_up(sum(mx(o, k)**2 for k in ('DU11', 'DU12', 'DU21', 'DU22')))
    u0 = hi(ar(cl - 1)*ar(rmax)**ar(delta) + arb(2).sqrt()*arb(0.283275)*ar(rmax)**ar(2 + delta))      # C3-131: |U_i - DU(0)X_i| <= 0.283275 r^3 on r <= 0.05 (both components)
    # exterior
    ff = json.load(open(ffjson)); e = ff[str(float(R))]; B = {k: Fr(v) for k, v in e['coef'].items()}
    Rr = ar(Fr(R)); pw = hi(Rr**ar(gamma - 1 + delta)); pwu = hi(Rr**ar(gamma + delta - 1))
    drho_ext = pw*sqrt_up(B['rho_x']**2 + B['rho_y']**2); u_ext = pwu*sqrt_up(B['U1']**2 + B['U2']**2); du_ext = pw*sqrt_up(sum(B[k]**2 for k in ('DU11', 'DU12', 'DU21', 'DU22')))
    res = {}
    for key, name, o0, ext, target in (('Drho', 'sup r^(2/5) |D rho|_F', drho0, drho_ext, '152 (together with r^(7/5)|D^2 rho|)'), ('U', 'sup r^(-3/5) |U|', u0, u_ext, '18'), ('DU', 'sup r^(2/5) |DU|_F', du0, du_ext, '18')):
        v, r = best[key]; tot = max(v, o0, ext)
        print('%s <= %s on R^2  [cells %s at r in [%g, %g] theta in [%.3f, %.3f]; origin square r <= %s: %s; exterior r >= %g: %s]  target %s' % (name, up(tot), up(v), r['r_lo'], r['r_hi'], r['t_lo'], r['t_hi'], up(rmax, 6), up(o0), R, up(ext), target))
        res[key] = {'name': name, 'global_upper': up(tot), 'cells_upper': up(v), 'cell': {k: r[k] for k in ('r_lo', 'r_hi', 't_lo', 't_hi')}, 'origin_upper': up(o0), 'exterior_upper': up(ext), 'R': R}
    res['n_cells'] = len(cells); res['delta'] = '2/5'; res['note'] = 'second-derivative decay constants not covered'
    json.dump(res, open(out_json, 'w'), indent=1)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], float(sys.argv[5]), sys.argv[6])
