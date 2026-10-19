"""Verifier scratch (shift 6): the angular row at fixed c_l (lead NOTES 4 of the c6h item: fxd1g 100, s2g 150, c6g 200, c6h 250)
on my audits. Quantities: whole-box N_f ('all'), near-P N_f (|X-P|<0.5), N_v for r <= 1000 (max over the five inner bands, and
'r<=1000,ya>=0.006'), N_v for r > 1000 ('1000<=r<=R', and 'r>1000,ya>=0.006'), 857-label J at eps 0.03 / 0.01.
For consecutive rows and each configuration both have: the change, and whether an increase exceeds the configuration spread
(max - min over the configurations of each of the two rows; the larger is used, the smaller printed too).
Usage: python3 row_read.py tag1 tag2 ... [-c N11250_q384,N16875_q512]"""
import sys, json, os
args = sys.argv[1:]
cfgs = ['N11250_q384', 'N16875_q512', 'N16875_q768', 'N22500_q384', 'N22500_q512']
if '-c' in args:
    i = args.index('-c'); cfgs = args[i + 1].split(','); args = args[:i] + args[i + 2:]
tags = args
inner = ['r<=0.1', '0.1<=r<=2', '2<=r<=10', '10<=r<=100', '100<=r<=1000']
Q = ['Nf_all', 'Nf_nearP', 'Nv_r<=1000', 'Nv_r<=1000_ya', 'Nv_r>1000', 'Nv_r>1000_ya']


def vals(t, c):
    f = 'runs/audit/%s_%s_R7.652e6.json' % (t, c)
    if not os.path.exists(f):
        return None
    R = {r['region']: r for r in json.load(open(f))['residual']}
    g = lambda k: R[k]['Nv_max'] if k in R else float('nan')
    return {'Nf_all': R['all']['flux_max'], 'Nf_nearP': R['|X-P|<0.5']['flux_max'],
            'Nv_r<=1000': max(R[k]['Nv_max'] for k in inner), 'Nv_r<=1000_ya': g('r<=1000,ya>=0.006'),
            'Nv_r>1000': R['1000<=r<=R']['Nv_max'], 'Nv_r>1000_ya': g('r>1000,ya>=0.006')}


V = {t: {c: vals(t, c) for c in cfgs} for t in tags}
J = {}
for t in tags:
    for inf in ('', '_clo'):
        f = 'runs/audit/%s_N16875_q384_R7.652e6%s_jd2.json' % (t, inf)
        if os.path.exists(f):
            s = json.load(open(f))['summary']; J[t] = (s['spread'][5], s['spread'][6]); break
for q in Q:
    print('== %s' % q)
    sp = {}
    for t in tags:
        xs = [V[t][c][q] for c in cfgs if V[t][c] and V[t][c][q] == V[t][c][q]]
        sp[t] = (max(xs) - min(xs)) if len(xs) > 1 else float('nan')
        print('  %-8s %s  spread %.2e' % (t, '  '.join('%s %.3e' % (c, V[t][c][q]) if V[t][c] else '%s -' % c for c in cfgs), sp[t]))
    for a, b in zip(tags, tags[1:]):
        ds = []
        for c in cfgs:
            if V[a][c] and V[b][c]:
                d = V[b][c][q] - V[a][c][q]; s = max(sp[a], sp[b])
                ds.append('%s %+.2e (ratio %.3f)%s' % (c, d, V[b][c][q] / V[a][c][q], ' INCREASE>spread' if d > s else ''))
        print('  %s -> %s: %s; spreads %.2e / %.2e' % (a, b, '; '.join(ds), sp[a], sp[b]))
print('== J (eps 0.03, 0.01)')
for t in tags:
    print('  %-8s %s' % (t, ('%.4e %.4e' % J[t]) if t in J else '-'))
for a, b in zip(tags, tags[1:]):
    if a in J and b in J:
        print('  %s -> %s: ratio %.3f %.3f' % (a, b, J[b][0] / J[a][0], J[b][1] / J[a][1]))
