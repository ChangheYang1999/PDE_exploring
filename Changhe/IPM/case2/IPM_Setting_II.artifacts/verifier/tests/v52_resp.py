"""V52: central-difference responses from the runs of runs/v52_chain.sh / v52b_chain.sh. For each control pair (plus, minus, step):
dm1, d log Gt at selected exit angles (raw and minus the |cos| > 0.05 mean), d log G_axis(+-inf) (tests/v50_axis.py, median of
log h/k^2 - log 2 on t in [0, 9.5]) and d Delta_z, Delta_z = log G(-inf) - log G(+inf). Second differences against the base state
(runs/v47_nw3_p014N6R_s1.0) for the nonlinearity check. Usage: python3 tests/v52_resp.py"""
import json, os, numpy as np
R = 'runs/'
def load(tag, base=False):
    if base:
        st, gp, ax = R + 'v47_nw3_p014N6R_s1.0', R + 'v47_nw3_p014N6R_s1.0_gfixprof.npz', R + 'v50_axis_N6_nt256.log'
    else:
        st, gp, ax = R + 'v52_' + tag, R + 'v52_' + tag + '_gfixprof.npz', R + 'v52_' + tag + '_axis.log'
    if not (os.path.exists(gp) and os.path.exists(ax) and os.path.getsize(ax) > 0):
        return None
    if base:
        m1 = 0.496927
    else:
        s = [l for l in open(st + '.log') if l.startswith('SUMMARY')][0]
        m1 = json.loads(s[8:])['final']['m1']
    pr = np.load(gp); the = np.degrees(pr['the']); lg = pr['logGt']
    msk = np.abs(np.cos(pr['the'])) > 0.05
    a = [json.loads(l) for l in open(ax) if l.startswith('{')][0]['axis']
    return dict(m1=m1, the=the, lg=lg, mean=float(lg[msk].mean()), up=a['upper']['log_G_axis'], lo=a['lower']['log_G_axis'])
B = load('', base=True)
ANG = (0, 45, 80, 85, 88, 89, 91, 95, 180, 255, 260, 265, 268, 269, 271, 275, 300)
def at(S, d):
    return float(S['lg'][int(np.argmin(np.abs(S['the'] - d)))])
out = {}
for name, pl, mi, h in (('bl0.05', 'bl0.05_bu0', 'bl-0.05_bu0', 0.05), ('bu0.05', 'bl0_bu0.05', 'bl0_bu-0.05', 0.05),
                        ('bl0.2', 'bl0.2_bu0', 'bl-0.2_bu0', 0.2), ('p0.002', 'pP', 'pM', 0.002), ('a3_0.02', 'a3P', 'a3M', 0.02),
                        ('c0.05', 'cP', 'cM', 0.05)):
    P, M = load(pl), load(mi)
    if P is None or M is None:
        continue
    dz = lambda S: S['lo'] - S['up']
    r = dict(dm1=(P['m1'] - M['m1'])/(2*h), d2m1=(P['m1'] - 2*B['m1'] + M['m1'])/h**2,
             dlogG_up=(P['up'] - M['up'])/(2*h), dlogG_lo=(P['lo'] - M['lo'])/(2*h), dDz=(dz(P) - dz(M))/(2*h),
             d2Dz=(dz(P) - 2*dz(B) + dz(M))/h**2, dmean=(P['mean'] - M['mean'])/(2*h),
             dlogGt_raw={'%g' % d: round((at(P, d) - at(M, d))/(2*h), 4) for d in ANG},
             dlogGt_minus_mean={'%g' % d: round(((at(P, d) - P['mean']) - (at(M, d) - M['mean']))/(2*h), 4) for d in ANG},
             dup_mm=((P['up'] - P['mean']) - (M['up'] - M['mean']))/(2*h), dlo_mm=((P['lo'] - P['mean']) - (M['lo'] - M['mean']))/(2*h))
    out[name] = {k: (round(v, 5) if isinstance(v, float) else v) for k, v in r.items()}
print(json.dumps(dict(base=dict(m1=B['m1'], up=B['up'], lo=B['lo'], Dz=round(B['lo'] - B['up'], 4)), resp=out), indent=1))
# constrained derivative of Delta_z along a bump at fixed m1, compensated by p or by a_3
# (V52(d)) also the window-minus-mean values: axis limits (up, lo) and picks (89, 269), and the pick difference D = 269 - 89
for c in ('p0.002', 'a3_0.02', 'c0.05'):
    for bmp in ('bl0.05', 'bu0.05', 'bl0.2'):
        if c in out and bmp in out:
            k = out[bmp]['dm1']/out[c]['dm1']
            f = lambda g: g(out[bmp]) - k*g(out[c])
            print('constrained d/d%s at fixed m1 (compensator %s, step %.4f per unit bump): dDz %.4f  axis-mean (up %.4f, lo %.4f)  '
                  'picks-mean (89 %.4f, 269 %.4f)  dD_pick %.4f'
                  % (bmp, c, -k, f(lambda o: o['dDz']), f(lambda o: o['dup_mm']), f(lambda o: o['dlo_mm']),
                     f(lambda o: o['dlogGt_minus_mean']['89']), f(lambda o: o['dlogGt_minus_mean']['269']),
                     f(lambda o: o['dlogGt_minus_mean']['269'] - o['dlogGt_minus_mean']['89'])))
