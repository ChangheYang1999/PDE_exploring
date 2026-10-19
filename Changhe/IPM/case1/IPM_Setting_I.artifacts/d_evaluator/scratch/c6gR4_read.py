"""Verifier scratch (shift 7): c6gR4 (step 47) far bands, formula continued (suffix _frm47: 900 L-1000 L, 1000 L-9000 L,
9000 L-1e4 L, r > 1e4 L; k_self) against X3 = c6g baselines (_rb44r 900 L-1000 L, _rb44 1000 L-9000 L and r > 1e4 L, _rb44s
9000 L-1e4 L; k_self) and against dom9000g (_frm44), N_v maxima raw and with A5 (ya >= 0.006), at N16875 q512 and N22500 q384.
Thresholds (lead NOTES 18:04:24Z item 5, 00:21:41Z item 2): 1000 L-9000 L ratio in [0.8, 1.25] on both = "47 ~ c6g";
<= 0.5 on both = "falls"; otherwise stated.
Usage: python3 c6gR4_read.py"""
import json, os, re
D = 'runs/audit/'
LX = 7.651424601381517


def bands(f):
    if not os.path.exists(f):
        return None
    d = json.load(open(f))
    L = float(d['vcand'].get('L', LX)) if 'vcand' in d else LX
    out = {}
    for r in d['residual']:
        m = re.match(r'([0-9.e+]+)<r<=([0-9.e+inf]+)(,ya>=0.006)?$', r['region'])
        if m:
            a = float(m.group(1)) / L; b = m.group(2); b = 'inf' if b == 'inf' else '%.0f' % (float(b) / L)
            out[('%.0f-%s' % (a, b), bool(m.group(3)))] = r
    return out


for c in ('N16875_q512', 'N22500_q384'):
    a = bands(D + 'c6gR4_%s_R7.652e6_frm47.json' % c)
    if a is None:
        print('%s: c6gR4 _frm47 missing' % c); continue
    b = {}
    for s in ('_rb44r', '_rb44', '_rb44s'):
        x = bands(D + 'c6g_%s_R7.652e6%s.json' % (c, s))
        if x:
            for k, v in x.items():
                b.setdefault(k, v)
    g = bands(D + 'dom9000g_%s_R7.652e6_frm44.json' % c) or {}
    for k in sorted(a, key=lambda k: (float(k[0].split('-')[0]), k[1])):
        x = a[k]; y = b.get(k); z = g.get(k)
        print('%s %-11s %-4s R4 %.4e at %.5g L th %.4f | X3 %s | D9 %s' % (
            c, k[0] + ' L', 'A5' if k[1] else 'raw', x['Nv_max'], x['Nv_argmax_r'] / LX, x['Nv_argmax_theta'],
            '-' if y is None else '%.4e at %.5g L th %.4f R4/X3 %.4f' % (y['Nv_max'], y['Nv_argmax_r'] / LX, y['Nv_argmax_theta'],
                                                                        x['Nv_max'] / y['Nv_max']),
            '-' if z is None else '%.4e R4/D9 %.3f D9/X3 %s' % (z['Nv_max'], x['Nv_max'] / z['Nv_max'],
                                                                '-' if y is None else '%.4f' % (z['Nv_max'] / y['Nv_max']))))
