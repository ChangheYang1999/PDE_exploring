"""Verifier scratch (shift 7; lead NOTES 2026-10-19T04:02:23Z item 2): for each fit with audits on N11250 q384 and N16875 q512,
the location of the whole-box N_f maximum (A5 region 'all,ya>=0.006'): r, theta, the distance to P = (x*, 0), and whether it
equals the maximum within 0.5 of P; and, for the rows given on the command line, the comparison with X3 = c6g on the same
configuration (whole-box N_f, within 0.5 of P, N_v r <= 1000 (A5), far band N_v r > 1000 (A5), J at N16875 q384 eps 0.03 / 0.01).
Usage: python3 wb_loc.py [tag ...]"""
import json, os, sys, math
D = 'runs/audit/'
cfgs = ['N11250_q384', 'N16875_q512']
allt = ['c6g', 'c6gF', 's2g', 'seg3g', 'fxn24g', 'fxn16g', 'fxn8g', 'fxn4g', 'fxm2g', 'fxu2g', 'fxu3g', 'fxv24g', 'nst24g', 'nsn8g']


def aud(tag, c):
    f = D + '%s_%s_R7.652e6_a5.json' % (tag, c)
    if not os.path.exists(f): f = D + '%s_%s_R7.652e6.json' % (tag, c)
    if not os.path.exists(f): return None
    d = json.load(open(f)); r = {x['region']: x for x in d['residual']}
    if 'all,ya>=0.006' not in r: return None
    w = r['all,ya>=0.006']; xs = d['vcand']['x_star']
    rr, th = w['flux_argmax_r'], w['flux_argmax_theta']
    dist = math.hypot(rr * math.cos(th) - xs, rr * math.sin(th))
    return dict(wb=w['flux_max'], r=rr, th=th, dist=dist, nP=r['|X-P|<0.5']['flux_max'], n2=r['|X-P|<2']['flux_max'],
                nv=r['r<=1000,ya>=0.006']['Nv_max'], far=r['r>1000,ya>=0.006']['Nv_max'], xs=xs)


def jay(tag):
    f = D + '%s_N16875_q384_R7.652e6_jd2.json' % tag
    if not os.path.exists(f): return None
    s = json.load(open(f))['summary']['spread']; return s[5], s[6]


print('Whole-box N_f (A5) maximum: value, r, theta, |X - P|, = max within 0.5 of P?, = max within 2 of P?')
for t in allt:
    for c in cfgs:
        a = aud(t, c)
        if a is None: continue
        print('%-7s %s  %.4e  r %9.4f  theta %.4f  |X-P| %8.4f  inP0.5 %-5s inP2 %-5s  (x* %.7f)' % (
            t, c, a['wb'], a['r'], a['th'], a['dist'], a['wb'] == a['nP'], a['wb'] == a['n2'], a['xs']))
X = {c: aud('c6g', c) for c in cfgs}; JX = jay('c6g')
for t in sys.argv[1:]:
    print('== %s against X3 = c6g (same configuration)' % t)
    for c in cfgs:
        a = aud(t, c)
        if a is None: print('   %s missing' % c); continue
        x = X[c]
        print('   %s  wholebox %.4e (%.3f)  near P %.4e (%.3f)  Nv r<=1000 %.3e (%.3f)  far Nv r>1000 %.3e (%.3f)' % (
            c, a['wb'], a['wb'] / x['wb'], a['nP'], a['nP'] / x['nP'], a['nv'], a['nv'] / x['nv'], a['far'], a['far'] / x['far']))
    j = jay(t)
    if j: print('   J eps 0.03 %.4e (%.3f)  eps 0.01 %.4e (%.3f)' % (j[0], j[0] / JX[0], j[1], j[1] / JX[1]))
