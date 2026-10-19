"""Verifier scratch (shift 6): parts of the c6g2 (step 45) reading not covered by read_fit.py (lead NOTES 21:10:51Z item 3).
(i) Far bands of c6g2 (suffix _rb45: 900 L-1000 L, 1000 L-9000 L, 9000 L-1e4 L, r > 1e4 L; k_self) against c6g's baselines
    (_rb44r 900 L-1000 L, _rb44 1000 L-9000 L and r > 1e4 L, _rb44s 9000 L-1e4 L; k_self), N_v maxima raw and with A5
    (ya >= 0.006), at N16875 q512 and N22500 q384; thresholds > 0.8 on some configuration / <= 0.5 on every one.
    C at the axis (far1_ver) ratio with the same thresholds.
(ii) Domain rows (closure convention, files without suffix) against c6g2 (formula convention): near-P N_f ratios on the
    common configurations, and J (dom _clo_jd2 against c6g2 _jd2, N16875 q384); [0.8, 1.25] -> the gain is that of the budget.
Usage: python3 c6g2_read.py [A=c6g2] [B=c6g]"""
import sys, json, os, re
A = sys.argv[1] if len(sys.argv) > 1 else 'c6g2'
B = sys.argv[2] if len(sys.argv) > 2 else 'c6g'
D = 'runs/audit/'


def bands(f):
    if not os.path.exists(f):
        return None
    d = json.load(open(f))
    L = float(d['vcand'].get('L', 7.651424601381517)) if 'vcand' in d else 7.651424601381517
    out = {}
    for r in d['residual']:
        m = re.match(r'([0-9.e+]+)<r<=([0-9.e+inf]+)(,ya>=0.006)?$', r['region'])
        if m:
            a = float(m.group(1)) / L; b = m.group(2); b = 'inf' if b == 'inf' else '%.0f' % (float(b) / L)
            out[('%.0f-%s' % (a, b), bool(m.group(3)))] = r
    return out


print('(i) far bands, N_v maxima, %s_rb45 against %s baselines' % (A, B))
for c in ('N16875_q512', 'N22500_q384'):
    a = bands(D + '%s_%s_R7.652e6_rb45.json' % (A, c))
    if a is None:
        print('  %s: %s _rb45 missing' % (c, A)); continue
    b = {}
    for s in ('_rb44r', '_rb44', '_rb44s'):
        x = bands(D + '%s_%s_R7.652e6%s.json' % (B, c, s))
        if x:
            for k, v in x.items():
                b.setdefault(k, v)
    for k in sorted(a, key=lambda k: (float(k[0].split('-')[0]), k[1])):
        x = a[k]; y = b.get(k)
        print('  %s %-11s %-4s A %.4e at %.5g L th %.4f   B %s' % (c, k[0] + ' L', 'A5' if k[1] else 'raw', x['Nv_max'],
              x['Nv_argmax_r'] / 7.651424601381517, x['Nv_argmax_theta'],
              '-' if y is None else '%.4e at %.5g L th %.4f  ratio %.4f' % (y['Nv_max'], y['Nv_argmax_r'] / 7.651424601381517,
                                                                      y['Nv_argmax_theta'], x['Nv_max'] / y['Nv_max'])))
fa, fb = 'runs/far1/%s_nt16384.json' % A, 'runs/far1/%s_nt16384.json' % B
if os.path.exists(fa) and os.path.exists(fb):
    x, y = json.load(open(fa)), json.load(open(fb))
    print('  C at the axis: %s %.6e  %s %.6e  ratio %.4f; V_r(pi/2) %.6f / %.6f; max |T1f - T1s| (0.05 < t < 1.4) %.3e / %.3e' % (
        A, x['C_axis'], B, y['C_axis'], x['C_axis'] / y['C_axis'], x['Vr_axis'], y['Vr_axis'], x['max_abs_diff_005_14'],
        y['max_abs_diff_005_14']))
print('(ii) domain rows against %s: near-P N_f and J' % A)
JA = D + '%s_N16875_q384_R7.652e6_jd2.json' % A
sJ = json.load(open(JA))['summary']['spread'] if os.path.exists(JA) else None
for t in ('dom90g', 'dom300g', 'dom9000g'):
    for c in ('N11250_q384', 'N16875_q512', 'N22500_q384'):
        fa, fb = D + '%s_%s_R7.652e6.json' % (t, c), D + '%s_%s_R7.652e6.json' % (A, c)
        if os.path.exists(fa) and os.path.exists(fb):
            x = {r['region']: r for r in json.load(open(fa))['residual']}['|X-P|<0.5']
            y = {r['region']: r for r in json.load(open(fb))['residual']}['|X-P|<0.5']
            q = x['flux_max'] / y['flux_max']
            print('  %-8s %s near-P N_f %.4e / %.4e = %.3f %s' % (t, c, x['flux_max'], y['flux_max'], q,
                                                                   'in [0.8, 1.25]' if 0.8 <= q <= 1.25 else 'outside'))
    fj = D + '%s_N16875_q384_R7.652e6_clo_jd2.json' % t
    if os.path.exists(fj) and sJ is not None:
        s = json.load(open(fj))['summary']['spread']
        print('  %-8s J eps 0.03 %.4e / %.4e = %.3f ; eps 0.01 %.4e / %.4e = %.3f' % (t, s[5], sJ[5], s[5] / sJ[5], s[6], sJ[6], s[6] / sJ[6]))
