"""Verifier scratch (shift 6): c6g2 (step 45) against X3 = c6g, and c6h against c6g2, on my audits (cfg {}, formula global).
Five quantities of lead NOTES 15:14:26Z item 4, raw and with A5 (pi/2 - theta >= 0.006): whole-box N_f, N_f within 0.5 of P,
N_v r <= 1000 (max over the five inner bands), N_v r > 1000; positions of the maxima; h(P) - 1. J from the jd2 files.
Usage: python3 c6g2_tab.py [cfgs comma-separated] [tags comma-separated]"""
import sys, json, os
cfgs = (sys.argv[1] if len(sys.argv) > 1 else 'N11250_q384,N16875_q512,N16875_q768,N22500_q384,N22500_q512').split(',')
tags = (sys.argv[2] if len(sys.argv) > 2 else 'c6g,c6g2,c6h').split(',')
inner = ['r<=0.1', '0.1<=r<=2', '2<=r<=10', '10<=r<=100', '100<=r<=1000']


def q(t, c):
    f = 'runs/audit/%s_%s_R7.652e6.json' % (t, c)
    if not os.path.exists(f):
        return None
    d = json.load(open(f))
    R = {r['region']: r for r in d['residual']}
    fl = lambda r: (r['flux_max'], r['flux_argmax_r'], r['flux_argmax_theta'])
    nv = lambda r: (r['Nv_max'], r['Nv_argmax_r'], r['Nv_argmax_theta'])
    a5 = max(fl(R['r<=1000,ya>=0.006']), fl(R['r>1000,ya>=0.006']))
    return {'Nf_all': fl(R['all']), 'Nf_all_A5': a5, 'Nf_nearP': fl(R['|X-P|<0.5']),
            'Nv_le1000': max(nv(R[k]) for k in inner), 'Nv_le1000_A5': nv(R['r<=1000,ya>=0.006']),
            'Nv_gt1000': nv(R['1000<=r<=R']), 'Nv_gt1000_A5': nv(R['r>1000,ya>=0.006']),
            'hP-1': d['vcand']['hP'] - 1, 'c_l': d['vcand']['c_l']}


V = {t: {c: q(t, c) for c in cfgs} for t in tags}
for k in ['Nf_all', 'Nf_all_A5', 'Nf_nearP', 'Nv_le1000', 'Nv_le1000_A5', 'Nv_gt1000', 'Nv_gt1000_A5', 'hP-1']:
    print('== %s' % k)
    for c in cfgs:
        row = []
        for t in tags:
            v = V[t][c]
            if v is None:
                row.append('%-5s -' % t); continue
            x = v[k]
            row.append('%-5s %.4e' % (t, x) if k == 'hP-1' else '%-5s %.4e (r %.4g th %.4f)' % (t, x[0], x[1], x[2]))
        rat = []
        for a, b in zip(tags, tags[1:]):
            if V[a][c] and V[b][c] and k != 'hP-1':
                rat.append('%s/%s %.4f' % (b, a, V[b][c][k][0] / V[a][c][k][0]))
        print('  %-12s %s   %s' % (c, ' | '.join(row), '  '.join(rat)))
print('== J (857 labels; spread at eps 0.03 / 0.01)')
for t in tags:
    for f in ('runs/audit/%s_N16875_q384_R7.652e6_jd2.json' % t, 'runs/audit/%s_N16875_q512_R7.652e6_jd2.json' % t):
        if os.path.exists(f):
            s = json.load(open(f))['summary']['spread']
            print('  %-5s %s %.4e / %.4e' % (t, f.split('_')[1] + '_' + f.split('_')[2], s[5], s[6]))
