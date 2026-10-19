"""V59(c): constrained (fixed m1) responses of the pick asymmetry D(d) = log Gt(270 - d) - log Gt(90 - d) at the tracer inner stops
t_s = -9 and -12 (tests/v59_tstop.py profiles runs/v52n_{tag}_v59tstop.npz), next to the axis-law values of V52(e)
(runs/v52n_{tag}_axis.log). Same pairs and constrained form X_b - (dm1/db)/(dm1/dc) X_c as tests/v52f_nt512.py.
Usage: python3 tests/v59c_resp.py"""
import json, os, numpy as np
R = 'runs/v52n_'
def load(tag):
    st, pr, ax = R + tag + '.log', R + tag + '_v59tstop.npz', R + tag + '_axis.log'
    if not all(os.path.exists(f) and os.path.getsize(f) > 0 for f in (st, pr, ax)):
        return None
    s = [l for l in open(st) if l.startswith('SUMMARY')]; a = [json.loads(l) for l in open(ax) if l.startswith('{')]
    z = np.load(pr)
    return dict(m1=json.loads(s[0][8:])['final']['m1'], deg=z['deg'], lg={ts: z['lg%g' % ts] for ts in (-9, -12)},
                Dz=a[0]['axis']['lower']['log_G_axis'] - a[0]['axis']['upper']['log_G_axis'])
DEL = (5, 3, 2, 1, 0.5, 0.09)
def D(S, ts, d):
    i = lambda x: int(np.argmin(np.abs(S['deg'] - x)))
    return float(S['lg'][ts][i(270 - d)] - S['lg'][ts][i(90 - d)])
C = {}
for name, pl, mi, h in (('bl', 'bl0.05', 'bl-0.05', 0.05), ('bu', 'bl0_bu0.05', 'bl0_bu-0.05', 0.05),
                        ('p', 'pP', 'pM', 0.002), ('a3', 'a3P', 'a3M', 0.02), ('c', 'cP', 'cM', 0.05)):
    P, M = load(pl), load(mi)
    if P is None or M is None:
        print('%-3s missing' % name); continue
    r = dict(dm1=(P['m1'] - M['m1'])/(2*h), axis=(P['Dz'] - M['Dz'])/(2*h))
    for ts in (-9, -12):
        for d in DEL:
            r[(ts, d)] = (D(P, ts, d) - D(M, ts, d))/(2*h)
    C[name] = r
    for ts in (-9, -12):
        print('%-3s t_s %3d  dm1 %+.4f  axis %+.4f  ' % (name, ts, r['dm1'], r['axis']) + '  '.join('d%g %+.4f' % (d, r[(ts, d)]) for d in DEL))
for b, comps in (('bl', ('p', 'a3', 'c')), ('bu', ('p', 'a3', 'c')), ('p', ('a3', 'c'))):
    for c in comps:
        if b in C and c in C:
            s = C[b]['dm1']/C[c]['dm1']
            for ts in (-9, -12):
                print('constrained %s | %-2s t_s %3d: axis %+.4f  ' % (b, c, ts, C[b]['axis'] - s*C[c]['axis']) +
                      '  '.join('d%g %+.4f' % (d, C[b][(ts, d)] - s*C[c][(ts, d)]) for d in DEL))
