# Lead: convert a verifier exit-map state (code/fwdstat.py output: rho on Gauss-Legendre panels in r, q nodes per
# panel, edges [0, exp(linspace(tmin, tmax, P+1))], args json with p, par, tmin, tmax, ppu) to the lead npz format on the
# uniform grid lr = -14 .. 10, dlr 1/30, by the same panel Lagrange interpolation in r that the verifier uses.
# Usage: python3 fromver.py in.npz out.npz [q=8]
import sys, json, numpy as np
d = np.load(sys.argv[1], allow_pickle=True); a = json.loads(str(d['args']))
q = 8
for s in sys.argv[3:]:
    k, v = s.split('='); q = int(v)
rho, r, th = d['rho'], d['r'], d['th']; p = float(a['p']); tmin, tmax = float(a['tmin']), float(a['tmax']); ppu = float(a['ppu'])
P = int(round((tmax - tmin) * ppu)); edges = np.concatenate([[0.0], np.exp(np.linspace(tmin, tmax, P + 1))])
assert len(r) == (len(edges) - 1) * q, (len(r), len(edges), q)
xg = np.polynomial.legendre.leggauss(q)[0]
def lag(x):
    w = np.ones((len(x), q))
    for j in range(q):
        for m in range(q):
            if m != j:
                w[:, j] *= (x - xg[m]) / (xg[j] - xg[m])
    return w
lr = np.linspace(-14.0, 10.0, 721); ru = np.exp(lr)
k = np.clip(np.searchsorted(edges, ru, side='right') - 1, 1, len(edges) - 2)
A, B = edges[k], edges[k + 1]; x = 2 * (ru - A) / (B - A) - 1
W = lag(x)
rhou = np.einsum('ij,ijt->it', W, rho.reshape(len(edges) - 1, q, -1)[k])
g = rhou / (ru ** p)[:, None]
par = np.array([float(v) for v in a['par'].split(':')])
# check: nodes of a panel reproduce themselves
kk = len(edges) // 2; rr = r[kk * q:(kk + 1) * q]; xx = 2 * (rr - edges[kk]) / (edges[kk + 1] - edges[kk]) - 1
err = float(np.abs(lag(xx) @ rho[kk * q:(kk + 1) * q] - rho[kk * q:(kk + 1) * q]).max())
np.savez(sys.argv[2], g=g, lr=lr, th=th, x=par, p=p, m1=float('nan'))
print(json.dumps(dict(K=len(par), p=p, par=a['par'], Nth=len(th), self_interp_err=err, gmin=float(g.min()), g_top_rel=float(np.abs(g[-1] - g[-1].mean()).max()))))
