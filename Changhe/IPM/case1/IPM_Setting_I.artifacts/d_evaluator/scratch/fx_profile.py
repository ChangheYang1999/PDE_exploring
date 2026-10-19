"""Verifier scratch (shift 7): the fixed-c_l profile on 375 x m <= 150 at equal budget (lead NOTES 2026-10-19T00:25:51Z), on my
audits: rows fxn16g (d = -1.6e-2; lead NOTES 03:13:52Z), fxn8g (d = -8e-3), fxn4g (-4e-3; lead NOTES 01:07:09Z), fxm2g (-2e-3), s2g (X2, -1e-3), seg3g (F2, free, 0), fxu2g (+2e-3), fxu3g (+3e-3), fxv24g (+2.4e-2) as far as they
exist. Per row: L2 objective (last check 'actual' of the GPU chain log) and its change over the last 1000 iterations; per
configuration (N11250 q384, N16875 q512; for seg3g and s2g the _a5 re-audits): whole-box N_f with A5 ('all,ya>=0.006') and all columns ('all'), N_v r <= 1000 (A5),
N_f within 0.5 of P, h(P) - 1, identity c_l; 857-label J (eps 0.03, 0.01; no closure); far1_ver C at the axis. Ratios against
F2 and the 00:25:51Z reading: (a) L2 within 30 percent of F2's, whole-box N_f (A5) within 30 percent on each configuration,
|h(P) - 1| <= 1e-6; (b) flattened (|change| < 2 percent over the last 1000 iterations) and near-P N_f >= 2 x F2's on each
configuration; (c) otherwise. Usage: python3 fx_profile.py"""
import json, os
G = ''
D = 'runs/audit/'
rows = [('fxn24g', -2.4e-2), ('fxn16g', -1.6e-2), ('fxn8g', -8e-3), ('fxn4g', -4e-3), ('fxm2g', -2e-3), ('s2g', -1e-3), ('seg3g', 0.0), ('fxu2g', 2e-3), ('fxu3g', 3e-3), ('fxv24g', 2.4e-2)]
cfgs = ['N11250_q384', 'N16875_q512']


def l2(tag):
    f = G + tag + '/' + tag + '.log'
    if not os.path.exists(f): return None
    ch = {}; done = False; inner = 2500
    for l in open(f):
        if not l.startswith('{'): continue
        o = json.loads(l)
        if o.get('event') == 'check': ch[inner * (o['outer'] - 1) + o['it']] = o['actual']
        if o.get('event') == 'end': done = True
    if not ch: return None
    last = max(ch); prev = [k for k in sorted(ch) if k <= last - 1000]
    return ch[last], last, ((ch[last] / ch[prev[-1]] - 1) if prev else float('nan')), done


def aud(tag, c):
    f = D + '%s_%s_R7.652e6_a5.json' % (tag, c)
    if not os.path.exists(f): f = D + '%s_%s_R7.652e6.json' % (tag, c)
    if not os.path.exists(f): return None
    d = json.load(open(f)); r = {x['region']: x for x in d['residual']}
    return dict(wbA=r['all,ya>=0.006']['flux_max'], wb=r['all']['flux_max'], nv=r['r<=1000,ya>=0.006']['Nv_max'],
                nP=r['|X-P|<0.5']['flux_max'], h=d['vcand']['hP'] - 1, cl=d['vcand']['c_l'])


def jay(tag):
    f = D + '%s_N16875_q384_R7.652e6_jd2.json' % tag
    if not os.path.exists(f): return None
    s = json.load(open(f))['summary']['spread']; return s[5], s[6]


def cax(tag):
    f = 'runs/far1/%s_nt16384.json' % tag
    return json.load(open(f))['C_axis'] if os.path.exists(f) else None


ref = {'L2': l2('seg3g'), 'J': jay('seg3g'), 'a': {c: aud('seg3g', c) for c in cfgs}}
for tag, dd in rows:
    L = l2(tag)
    if L is None: print('%-7s %+.1e: no chain log' % (tag, dd)); continue
    q = L[0] / ref['L2'][0]
    print('== %-7s d %+.1e  L2 %.6e (%.3f of F2) at %d its, last 1000 its %+.3f%%, end %s' % (tag, dd, L[0], q, L[1], 100 * L[2], L[3]))
    okA = abs(q - 1) <= 0.3; okB = abs(L[2]) < 0.02; nb = []; hmax = 0.0; have = True
    for c in cfgs:
        a, b = aud(tag, c), ref['a'][c]
        if a is None: print('   %s: audit missing' % c); have = False; continue
        rw = a['wbA'] / b['wbA']; rp = a['nP'] / b['nP']; hmax = max(hmax, abs(a['h']))
        okA = okA and abs(rw - 1) <= 0.3; nb.append(rp >= 2)
        print('   %s  wholebox A5 %.4e (%.3f)  all %.4e (%.3f)  Nv r<=1000 A5 %.3e (%.3f)  near P %.4e (%.3f)  h(P)-1 %+.2e  c_l %.10f' % (
            c, a['wbA'], rw, a['wb'], a['wb'] / b['wb'], a['nv'], a['nv'] / b['nv'], a['nP'], rp, a['h'], a['cl']))
    j = jay(tag)
    if j: print('   J eps 0.03 %.4e (%.3f)  eps 0.01 %.4e (%.3f)' % (j[0], j[0] / ref['J'][0], j[1], j[1] / ref['J'][1]))
    C = cax(tag)
    if C is not None: print('   C at the axis %+.7f' % C)
    if tag == 'seg3g' or not have: continue
    okA = okA and hmax <= 1e-6
    rd = '(a) not determined at this level' if okA else ('(b) excluded at this level' if (okB and all(nb)) else
                                                         '(c) undecided at the 375 x m <= 150 level after its iterations')
    if not L[3]: rd += ' (PROVISIONAL: run not ended)'
    print('   reading: %s  [L2 %s, |h(P)-1| max %.2e, flattened %s, near P >= 2 x F2 %s]' % (rd, abs(q - 1) <= 0.3, hmax, okB, nb))
