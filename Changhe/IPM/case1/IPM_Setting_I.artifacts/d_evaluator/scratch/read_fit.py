"""Verifier scratch (shift 6): reading of a fit A against a base B on my audits (G89 / G90 template).
Per configuration (runs/audit/<A>_<cfg>_R7.652e6<sufA>.json and <B>_<cfg>_R7.652e6<sufB>.json): whole-box, near-P, 2-10,
10-100, r <= 1000 and r > 1000 (ya >= 0.006) N_f and N_v maxima with ratios A/B; the A4 two-sided test (2-10 and 10-100 N_f
ratios in [0.667, 1.5]); far bands (regions 'a<r<=b' in units of L) with N_v maxima and argmax; h(P) - 1, c_l.
Then the 857-label J spreads (eps 0.03, 0.01) and far1_ver C at the axis.
Usage: python3 read_fit.py A B sufA sufB jA jB   (suffixes '' allowed; jA / jB: jd2 file infixes such as '_clo' or '')"""
import sys, json, os, re
A, B = sys.argv[1], sys.argv[2]
sA, sB = (sys.argv[3] if len(sys.argv) > 3 else ''), (sys.argv[4] if len(sys.argv) > 4 else '')
jA, jB = (sys.argv[5] if len(sys.argv) > 5 else '_clo'), (sys.argv[6] if len(sys.argv) > 6 else '')
D = 'runs/audit/'
cfgs = ['N11250_q384', 'N16875_q512', 'N16875_q768', 'N22500_q384', 'N22500_q512']
keys = ['all', '|X-P|<0.5', '2<=r<=10', '10<=r<=100', '100<=r<=1000', 'r<=1000,ya>=0.006', 'r>1000,ya>=0.006']


def load(t, c, s):
    f = D + '%s_%s_R7.652e6%s.json' % (t, c, s)
    return json.load(open(f)) if os.path.exists(f) else None


def bands(d, L):
    out = {}
    for r in d['residual']:
        m = re.match(r'([0-9.e+]+)<r<=([0-9.e+inf]+)$', r['region'])
        if m:
            a = float(m.group(1)) / L; b = m.group(2); b = 'inf' if b == 'inf' else '%.0f' % (float(b) / L)
            out['%.0f-%s L' % (a, b)] = r
    return out


for c in cfgs:
    a, b = load(A, c, sA), load(B, c, sB)
    if a is None or b is None:
        print('%s: missing %s' % (c, ' '.join(x for x, y in ((A, a), (B, b)) if y is None))); continue
    L = 7.651424601381517
    ra = {r['region']: r for r in a['residual']}; rb = {r['region']: r for r in b['residual']}
    print('== %s  (%s%s against %s%s)' % (c, A, sA, B, sB))
    for k in keys:
        if k in ra and k in rb:
            x, y = ra[k], rb[k]
            print('  %-20s Nf %.3e / %.3e = %.3f   Nv %.3e / %.3e = %.3f   NvA at %.4g L th %.4f' % (
                k, x['flux_max'], y['flux_max'], x['flux_max'] / y['flux_max'], x['Nv_max'], y['Nv_max'],
                x['Nv_max'] / y['Nv_max'], x['Nv_argmax_r'] / L, x['Nv_argmax_theta']))
    r1 = ra['2<=r<=10']['flux_max'] / rb['2<=r<=10']['flux_max']; r2 = ra['10<=r<=100']['flux_max'] / rb['10<=r<=100']['flux_max']
    side = lambda q: 'in' if 0.667 <= q <= 1.5 else ('LOW' if q < 0.667 else 'HIGH')
    hA, hB = a['vcand']['hP'] - 1, b['vcand']['hP'] - 1
    print('  A4: 2-10 %.3f (%s), 10-100 %.3f (%s); h(P)-1 A %+.2e B %+.2e; c_l A %.10f B %.10f' % (
        r1, side(r1), r2, side(r2), hA, hB, a['vcand']['c_l'], b['vcand']['c_l']))
    ba, bb = bands(a, L), bands(b, L)
    for k in ba:
        x = ba[k]; y = bb.get(k)
        print('  band %-14s %s Nv %.3e at %.4g L th %.4f%s' % (k, '' if 'ya' not in x['region'] else '(ya)', x['Nv_max'],
              x['Nv_argmax_r'] / L, x['Nv_argmax_theta'], '' if y is None else '   B %.3e ratio %.3f' % (y['Nv_max'], x['Nv_max'] / y['Nv_max'])))
for t, j in ((A, jA), (B, jB)):
    f = D + '%s_N16875_q384_R7.652e6%s_jd2.json' % (t, j)
    if os.path.exists(f):
        s = json.load(open(f))['summary']; print('J %s: n %d  eps 0.03 %.4e  eps 0.01 %.4e' % (t, s['n'], s['spread'][5], s['spread'][6]))
    else:
        print('J %s: missing %s' % (t, f))
for t in (A, B):
    f = 'runs/far1/%s_nt16384.json' % t
    if os.path.exists(f):
        d = json.load(open(f)); print('far1 %s: C_axis %+.7f  C/(1+k) %+.7f  Vr_axis %+.6e' % (t, d['C_axis'], d['C_axis_over_1pk'], d['Vr_axis']))
