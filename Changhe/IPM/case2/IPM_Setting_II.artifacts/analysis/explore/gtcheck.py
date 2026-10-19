# Lead exploration (2026-10-17): G and Gt = A/|Xi|^2 of a saved forward state (no evolution).
# Usage: python3 gtcheck.py state.npz p A_kind [par]   (A_kind: cos2 | cosk par | xeven a1,a2,.. | sin3 b  (cos^2 exp(-b sin 3th)))
import sys, json
import numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE
st = np.load(sys.argv[1]); p = float(sys.argv[2]); kind = sys.argv[3]; par = sys.argv[4] if len(sys.argv) > 4 else ''
if kind == 'cos2':
    Af = lambda t: np.cos(t) ** 2
elif kind == 'cosk':
    Af = lambda t: np.abs(np.cos(t)) ** float(par)
elif kind == 'sin3':
    Af = lambda t: np.cos(t) ** 2 * np.exp(-float(par) * np.sin(3 * t))
else:
    a = np.array([float(v) for v in par.split(',')]); Af = FE.datum_fn(a, len(a))
g = st['g']
if g.shape[0] != len(st['lr']):
    g = g.T
ng = FE.node_and_G(p, Af, g, st['lr'], st['th'])
th = ng['thA']; A = ng['A']; m1 = ng['m1']
lG = ng['logG']; lGt = np.log(np.maximum(A, 1e-300)) - 2 * m1 * ng['logAn']
out = dict(m1=m1, m2=ng['m2'])
for name, lg in (('G', lG), ('Gt', lGt)):
    for cut in (0.5, 0.1, 0.01):
        sel = (np.abs(np.cos(th)) > cut) & np.isfinite(lg)
        v = np.exp(lg[sel] - lg[sel].mean())
        out['%s_ratio_cos>%g' % (name, cut)] = float(v.max() / v.min())
    sel = (np.abs(np.cos(th)) > 0.1) & np.isfinite(lg)
    out[name + '_rel_std_cos>0.1'] = float(np.std(np.exp(lg[sel] - lg[sel].mean())) / np.mean(np.exp(lg[sel] - lg[sel].mean())))
idx = [int(round(k * len(th) / 16)) for k in range(9)]
out['deg'] = [round(float(np.degrees(th[i])), 1) for i in idx]
out['Gt_rel'] = [round(float(np.exp(lGt[i] - lGt[0])), 4) for i in idx]
out['G_rel'] = [round(float(np.exp(lG[i] - lG[0])), 4) for i in idx]
print(json.dumps(out))
