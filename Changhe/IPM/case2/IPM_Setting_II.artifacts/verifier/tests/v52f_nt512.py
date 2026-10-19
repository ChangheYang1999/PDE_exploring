"""V52(e): nt 512 repeat of tests/v52e_pickdep.py on the runs of runs/v52n_chain.sh (bl, a3, cmode, p) and runs/v54_chain.sh (bu).
Same quantities: dm1, the axis Delta_z = log G(-inf) - log G(+inf) and the pick asymmetry D(d) = log Gt(270 - d) - log Gt(90 - d), central
differences per unit control and the constrained derivatives X_b - (dm1/db)/(dm1/dc) X_c at fixed m1. Pairs whose runs are missing are
skipped. Usage: python3 tests/v52f_nt512.py"""
import json, os, numpy as np
R = 'runs/v52n_'
def load(tag):
    st, gp, ax = R + tag, R + tag + '_gfixprof.npz', R + tag + '_axis.log'
    if not all(os.path.exists(f) and os.path.getsize(f) > 0 for f in (st + '.log', gp, ax)):
        return None
    s = [l for l in open(st + '.log') if l.startswith('SUMMARY')]
    a = [json.loads(l) for l in open(ax) if l.startswith('{')]
    if not s or not a:
        return None
    pr = np.load(gp)
    return dict(m1=json.loads(s[0][8:])['final']['m1'], the=np.degrees(pr['the']), lg=pr['logGt'],
                up=a[0]['axis']['upper']['log_G_axis'], lo=a[0]['axis']['lower']['log_G_axis'])
DEL = (20, 10, 5, 3, 2, 1, 0.5)
def at(S, d):
    return float(S['lg'][int(np.argmin(np.abs(S['the'] - d)))])
def D(S, d):
    return at(S, 270 - d) - at(S, 90 - d)
C = {}
for name, pl, mi, h in (('bl', 'bl0.05', 'bl-0.05', 0.05), ('bu', 'bl0_bu0.05', 'bl0_bu-0.05', 0.05),
                        ('p', 'pP', 'pM', 0.002), ('a3', 'a3P', 'a3M', 0.02), ('c', 'cP', 'cM', 0.05)):
    P, M = load(pl), load(mi)
    if P is None or M is None:
        print('%-3s missing (%s %s)' % (name, P is not None, M is not None))
        continue
    r = dict(dm1=(P['m1'] - M['m1'])/(2*h), axis=((P['lo'] - P['up']) - (M['lo'] - M['up']))/(2*h),
             m1P=P['m1'], m1M=M['m1'], DzP=P['lo'] - P['up'], DzM=M['lo'] - M['up'])
    for d in DEL:
        r['%g' % d] = (D(P, d) - D(M, d))/(2*h)
    C[name] = r
    print('%-3s m1 %.6f / %.6f  dm1 %+.4f  Dz %.4f / %.4f  axis %+.4f  ' % (name, r['m1P'], r['m1M'], r['dm1'], r['DzP'], r['DzM'], r['axis'])
          + '  '.join('d%g %+.4f' % (d, r['%g' % d]) for d in DEL))
for b, comps in (('bl', ('p', 'a3', 'c')), ('bu', ('p', 'a3', 'c')), ('p', ('a3', 'c'))):
    for c in comps:
        if b in C and c in C:
            s = C[b]['dm1']/C[c]['dm1']
            print('constrained %s | %-2s: axis %+.4f  ' % (b, c, C[b]['axis'] - s*C[c]['axis']) +
                  '  '.join('d%g %+.4f' % (d, C[b]['%g' % d] - s*C[c]['%g' % d]) for d in DEL))
