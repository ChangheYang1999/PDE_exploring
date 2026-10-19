"""V52(e): dependence of the constrained (fixed m1) response of the up/down asymmetry on where it is read. For pick pairs
(90 - d, 270 - d) deg of the exit tracer profile (tests/v43_gfix.py) and for the axis limits (tests/v50_axis.py), the central
differences of D(d) = log Gt(270 - d) - log Gt(90 - d) per unit control, and the constrained derivative along a bump at fixed m1,
X_b - (dm1/db)/(dm1/dc) X_c, for the compensators c = p, a_3, cmode. Reuses load() of tests/v52_resp.py. Usage: python3 tests/v52e_pickdep.py"""
import json, sys, numpy as np
sys.argv = sys.argv[:1]
src = open('tests/v52_resp.py').read()
exec(src[:src.index('B = load')])
DEL = (20, 10, 5, 3, 2, 1, 0.5)
def at(S, d):
    return float(S['lg'][int(np.argmin(np.abs(S['the'] - d)))])
def D(S, d):
    return at(S, 270 - d) - at(S, 90 - d)
C = {}
for name, pl, mi, h in (('bl', 'bl0.05_bu0', 'bl-0.05_bu0', 0.05), ('bu', 'bl0_bu0.05', 'bl0_bu-0.05', 0.05),
                        ('p', 'pP', 'pM', 0.002), ('a3', 'a3P', 'a3M', 0.02), ('c', 'cP', 'cM', 0.05)):
    P, M = load(pl), load(mi)
    r = dict(dm1=(P['m1'] - M['m1'])/(2*h), axis=((P['lo'] - P['up']) - (M['lo'] - M['up']))/(2*h))
    for d in DEL:
        r['%g' % d] = (D(P, d) - D(M, d))/(2*h)
    C[name] = r
    print('%-3s dm1 %+.4f  axis %+.4f  ' % (name, r['dm1'], r['axis']) + '  '.join('d%g %+.4f' % (d, r['%g' % d]) for d in DEL))
for b in ('bl', 'bu'):
    for c in ('p', 'a3', 'c'):
        s = C[b]['dm1']/C[c]['dm1']
        print('constrained %s | %-2s: axis %+.4f  ' % (b, c, C[b]['axis'] - s*C[c]['axis']) +
              '  '.join('d%g %+.4f' % (d, C[b]['%g' % d] - s*C[c]['%g' % d]) for d in DEL))
for c in ('a3', 'c'):
    s = C['p']['dm1']/C[c]['dm1']
    print('constrained p  | %-2s: axis %+.4f  ' % (c, C['p']['axis'] - s*C[c]['axis']) +
          '  '.join('d%g %+.4f' % (d, C['p']['%g' % d] - s*C[c]['%g' % d]) for d in DEL))
