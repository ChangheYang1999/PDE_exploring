"""Corrected post-processing of data/certSups_*.jsonl (after the verifier's V083 audit):
 - per field, the set of certified cells = cells whose bound is finite; report the exact saved maximum and a ROUNDED-UP decimal (never rounded down);
 - origin square [-r0, r0]^2: the stored weighted bounds used omega(r0) = (1+4 r0^2)^0.4 (inscribed disk); for the full square the weight maximum is
   (1+8 r0^2)^0.4, so the weighted bounds of that cell are multiplied by ((1+8r0^2)/(1+4r0^2))^0.4 rounded up (the stored value is w(r0) * Frob-bound);
 - counts of nonfinite cells per field and the radial range fully certified from r0 upward.
Usage: post_certSups2.py in.jsonl out.json"""
import sys, json, math
from decimal import Decimal, ROUND_CEILING
rows = [json.loads(l) for l in open(sys.argv[1]) if l.strip()]
ok = [r for r in rows if r['status'] == 'ok']
seen = set(); uniq = []
for r in ok:
    key = (r['i'], r['k'])
    if key in seen: continue
    seen.add(key); uniq.append(r)
print('rows %d, ok %d, distinct cells %d' % (len(rows), len(ok), len(uniq)))
def finite(v): return isinstance(v, (int, float)) and not (math.isnan(v) or math.isinf(v))
def round_up(v, sig=6):
    if v == 0: return 0.0
    d = Decimal(repr(v)); e = d.adjusted(); q = Decimal(1).scaleb(e - sig + 1)
    return float(d.quantize(q, rounding=ROUND_CEILING))
keys = [k for k in uniq[0] if k.startswith(('Frob_', 'wFrob_', 'rho_', 'U1_', 'U2_'))]
origin = [r for r in uniq if r['r_lo'] == 0.0]
assert len(origin) == 1; r0 = origin[0]['r_hi']
ratio = ((1 + 8*r0*r0)/(1 + 4*r0*r0))**0.4; ratio_up = math.nextafter(ratio, math.inf)
out = {'r0': r0, 'origin_square_weight_ratio_applied': ratio_up}
for k in keys:
    vals = []
    for r in uniq:
        v = r[k]
        if not finite(v): continue
        if r['r_lo'] == 0.0 and k.startswith('wFrob'): v = v*ratio_up; v = math.nextafter(v, math.inf)
        vals.append((v, r))
    bad = [r for r in uniq if not finite(r[k])]
    if not vals: continue
    vmax, rmax = max(vals, key=lambda t: t[0])
    # fully certified from r0 up to:
    bad_r = sorted(r['r_lo'] for r in bad); upto = bad_r[0] if bad_r else max(r['r_hi'] for r in uniq)
    bad_min = min((r['r_lo'] for r in bad), default=None); bad_max = max((r['r_hi'] for r in bad), default=None)
    out[k] = {'saved_max_upper': vmax, 'rounded_up_6sig': round_up(vmax), 'cell_r': [rmax['r_lo'], rmax['r_hi']], 'cell_theta': [rmax['t_lo'], rmax['t_hi']],
              'n_certified_cells': len(vals), 'n_nonfinite_cells': len(bad), 'nonfinite_r_range': [bad_min, bad_max] if bad else None, 'fully_certified_r_upto': upto}
    if k.startswith(('Frob', 'wFrob')):
        print('%-14s saved max %.12g -> rounded up %.6g ; certified cells %d, nonfinite %d (r in %s); fully certified for r <= %.4g ; max at r in [%g, %g]' % (k, vmax, round_up(vmax), len(vals), len(bad), out[k]['nonfinite_r_range'], upto, rmax['r_lo'], rmax['r_hi']))
print('component sups (rounded up):', {k: v['rounded_up_6sig'] for k, v in out.items() if isinstance(v, dict) and not k.startswith(('Frob', 'wFrob'))})
json.dump(out, open(sys.argv[2], 'w'), indent=1)
