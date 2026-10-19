"""Verifier scratch (shift 8): reading of the budget continuations 58 fxn16gb (row 54 fxn16g, c_l 5.5604082, continued 21500
iterations at its stored c_l) and 59 fxn24gb (row 55 fxn24g, c_l 5.5524653, the same) by SPEC v4.18 (G130):
"kept at twice the budget" if L2(59) and the whole-box N_f of 59 on both configurations (N11250 q384, N16875 q512) are above
58's; "not kept" if L2(59) is below L2(58); otherwise "the objective and the maxima disagree". Prints per row the L2 objective
(last check 'actual' of the GPU log) and its change over the last 1000 iterations, whole-box N_f (A5 and all columns), N_v
r <= 1000 (A5), N_v r > 1000 (A5), N_f within 0.5 of P, h(P) - 1, identity c_l, J (857 labels, eps 0.03 / 0.01), C at the
axis; ratios to F2 (seg3g) and 58/54, 59/55, 59/58. Usage: python3 scratch/read5859.py"""
import json, os
G = ''
D = 'runs/audit/'
cfgs = ['N11250_q384', 'N16875_q512']
rows = [('fxn16g', '54'), ('fxn24g', '55'), ('fxn16gb', '58'), ('fxn24gb', '59')]


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
    return dict(L2=ch[last], it=last, d1000=((ch[last] / ch[prev[-1]] - 1) if prev else float('nan')), done=done, ch=ch)


def aud(tag, c):
    f = D + '%s_%s_R7.652e6_a5.json' % (tag, c)
    if not os.path.exists(f): f = D + '%s_%s_R7.652e6.json' % (tag, c)
    if not os.path.exists(f): return None
    d = json.load(open(f)); r = {x['region']: x for x in d['residual']}
    w = r['all,ya>=0.006']
    return dict(wbA=w['flux_max'], wb=r['all']['flux_max'], r=w['flux_argmax_r'], th=w['flux_argmax_theta'],
                nv=r['r<=1000,ya>=0.006']['Nv_max'], far=r['r>1000,ya>=0.006']['Nv_max'], nP=r['|X-P|<0.5']['flux_max'],
                h=d['vcand']['hP'] - 1, cl=d['vcand']['c_l'], xs=d['vcand']['x_star'])


def jay(tag):
    f = D + '%s_N16875_q384_R7.652e6_jd2.json' % tag
    if not os.path.exists(f): return None
    s = json.load(open(f))['summary']['spread']; return s[5], s[6]


def cax(tag):
    f = 'runs/far1/%s_nt16384.json' % tag
    return json.load(open(f))['C_axis'] if os.path.exists(f) else None


F2 = dict(L=l2('seg3g'), a={c: aud('seg3g', c) for c in cfgs}, J=jay('seg3g'))
R = {}
for tag, k in rows:
    L = l2(tag); A = {c: aud(tag, c) for c in cfgs}; J = jay(tag); C = cax(tag); R[k] = (L, A, J, C)
    if L is None: print('== %s (%s): no GPU log' % (k, tag)); continue
    print('== %s %s  L2 %.6e (%.3f of F2) at %d its of this run, last 1000 its %+.3f%%, end %s' % (
        k, tag, L['L2'], L['L2'] / F2['L']['L2'], L['it'], 100 * L['d1000'], L['done']))
    for c in cfgs:
        a, b = A[c], F2['a'][c]
        if a is None: print('   %s: audit missing' % c); continue
        print('   %s wb A5 %.4e (%.3f F2) all %.4e at r %.4f th %.4f; Nv<=1000 %.3e (%.3f); Nv>1000 %.4e; nearP %.4e (%.3f); h(P)-1 %+.2e; c_l %.10f; x* %.7f' % (
            c, a['wbA'], a['wbA'] / b['wbA'], a['wb'], a['r'], a['th'], a['nv'], a['nv'] / b['nv'], a['far'], a['nP'], a['nP'] / b['nP'], a['h'], a['cl'], a['xs']))
    if J: print('   J eps 0.03 %.4e (%.3f F2), eps 0.01 %.4e (%.3f F2)' % (J[0], J[0] / F2['J'][0], J[1], J[1] / F2['J'][1]))
    if C is not None: print('   C at the axis %+.7f' % C)
for x, y in (('58', '54'), ('59', '55'), ('59', '58')):
    Lx, Ax, Jx, _ = R[x]; Ly, Ay, Jy, _ = R[y]
    if Lx is None or Ly is None: continue
    s = '%s/%s: L2 %.4f' % (x, y, Lx['L2'] / Ly['L2'])
    for c in cfgs:
        if Ax[c] and Ay[c]: s += '; %s wb A5 %.4f, all %.4f, nearP %.4f, Nv<=1000 %.4f' % (c, Ax[c]['wbA'] / Ay[c]['wbA'], Ax[c]['wb'] / Ay[c]['wb'], Ax[c]['nP'] / Ay[c]['nP'], Ax[c]['nv'] / Ay[c]['nv'])
    if Jx and Jy: s += '; J %.4f / %.4f' % (Jx[0] / Jy[0], Jx[1] / Jy[1])
    print(s)
L58, A58, _, _ = R['58']; L59, A59, _, _ = R['59']
if L58 and L59 and all(A58[c] and A59[c] for c in cfgs):
    up = L59['L2'] > L58['L2']; wbA = [A59[c]['wbA'] > A58[c]['wbA'] for c in cfgs]; wb = [A59[c]['wb'] > A58[c]['wb'] for c in cfgs]
    rd = 'kept at twice the budget' if (up and all(wbA)) else ('not kept' if L59['L2'] < L58['L2'] else 'the objective and the maxima disagree')
    print('READING (A5 whole box): %s  [L2(59) > L2(58) %s; wb A5 59 > 58 %s; wb all columns 59 > 58 %s]%s' % (
        rd, up, wbA, wb, '' if (L58['done'] and L59['done']) else ' PROVISIONAL (run not ended)'))
