"""V100 aux: jumps of the panel-Lagrange interpolant of g = rho / r^p across panel edges, relative to the ring max of g and to the
local value; top 6 edges, and the same for log g where g > 1e-3 ring max. CPU, numpy only. Usage: python3 tests/v100_rhojump.py OWN.npz [ppu]"""
import sys, math, json, numpy as np
sys.path.insert(0, 'code')
from charsolve import lagrange_eval
fn = sys.argv[1]; d = np.load(fn, allow_pickle=True); args = json.loads(str(d['args'])); p = float(d['p'])
ppu = int(args['ppu']); tmin, tmax = float(args['tmin']), float(args['tmax']); q = 8
r = d['r']; th = d['th']; g = d['rho']/r[:, None]**p; deg = np.degrees(th)
edges = np.concatenate([[0.0], np.exp(np.linspace(tmin, tmax, int(round((tmax - tmin)*ppu)) + 1))])
xg = np.polynomial.legendre.leggauss(q)[0]; Lm = lagrange_eval(xg, 1.0); Lp = lagrange_eval(xg, -1.0)
rows = []
for e in range(2, len(edges) - 1):
    l = Lm @ g[(e - 1)*q:e*q]; rr = Lp @ g[e*q:(e + 1)*q]; gm = max(np.abs(l).max(), np.abs(rr).max())
    ok = (np.abs(l) > 1e-3*gm) & (np.abs(rr) > 1e-3*gm) & (l > 0) & (rr > 0)
    jl = np.where(ok, np.abs(np.log(np.where(ok, l, 1)/np.where(ok, rr, 1))), 0.0); j = int(np.argmax(jl))
    rows.append((float(np.abs(l - rr).max()/gm), float(jl.max()), round(math.log(edges[e]), 3), round(float(deg[j]), 2),
                 [float('%.4g' % l[j]), float('%.4g' % rr[j])], float('%.3g' % (l[j]/gm))))
rows.sort(key=lambda x: -x[1])
print(json.dumps(dict(state=fn.split('/')[-1], top_by_logjump=[[float('%.3g' % x[0]), float('%.3g' % x[1])] + list(x[2:]) for x in rows[:6]])))
