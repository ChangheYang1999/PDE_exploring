"""Summarise paired-ray check results: python3 src/ray_table.py runs/ray/c6d_full_A.json [B.json [C.json ...]]
Prints, per region, the maximum of |U_ray - U_lead|, |dU|/|U|, and the residual impact |dU . grad rho| / D against the lead's export,
and the mutual differences between configurations (the ray method's own convergence)."""
import sys, json, numpy as np

def load(p):
    d = json.load(open(p)); rows = d['rows']
    X = np.array([[r['x'], r['y']] for r in rows]); U = np.array([r['U_ray'] for r in rows]); Ul = np.array([r['U_lead'] for r in rows])
    g = np.array([[r['rho_x'], r['rho_y']] for r in rows]); D = np.array([r['D'] for r in rows]); res = np.array([r['res_lead'] for r in rows])
    return d, X, U, Ul, g, D, res

def region(X, xs):
    r = np.hypot(X[:, 0], X[:, 1]); dP = np.hypot(X[:, 0] - xs, X[:, 1])
    out = []
    for i in range(len(X)):
        if dP[i] < 0.5: out.append('P<0.5')
        elif dP[i] < 2.5: out.append('P 0.5-2.5')
        elif r[i] < 0.5: out.append('r=0.1')
        elif r[i] < 5: out.append('r=1')
        elif r[i] < 50: out.append('r=20')
        elif r[i] < 200: out.append('r=100')
        else: out.append('r=300')
    return np.array(out)

paths = sys.argv[1:]
data = [load(p) for p in paths]
d0, X, U0, Ul, g, D, res = data[0]
reg = region(X, d0['xstar'])
print('targets %d; x* %.6f; c_l %.8f' % (len(X), d0['xstar'], d0['c_l']))
print('%-10s %3s | %-9s %-9s %-9s | %-9s' % ('region', 'n', 'max|dU|', 'max rel', 'max imp', 'lead|R|/D'))
for rg in ['P<0.5', 'P 0.5-2.5', 'r=0.1', 'r=1', 'r=20', 'r=100', 'r=300']:
    m = reg == rg
    if not m.any(): continue
    dU = U0[m] - Ul[m]; rel = np.hypot(dU[:, 0], dU[:, 1]) / np.hypot(Ul[m, 0], Ul[m, 1])
    imp = np.abs(dU[:, 0] * g[m, 0] + dU[:, 1] * g[m, 1]) / np.where(D[m] > 0, D[m], np.inf)
    print('%-10s %3d | %-9.2e %-9.2e %-9.2e | %-9.2e' % (rg, m.sum(), np.abs(dU).max(), rel.max(), imp.max(), (np.abs(res[m]) / np.where(D[m] > 0, D[m], np.inf)).max()))
dU = U0 - Ul; imp = np.abs(dU[:, 0] * g[:, 0] + dU[:, 1] * g[:, 1]) / np.where(D > 0, D, np.inf)
print('ALL: max|dU| %.3e, max rel %.3e, max impact %.3e, median impact %.3e' % (np.abs(dU).max(), (np.hypot(dU[:, 0], dU[:, 1]) / np.hypot(Ul[:, 0], Ul[:, 1])).max(), imp.max(), np.median(imp)))
for k in range(1, len(data)):
    dk = data[k]; assert np.allclose(dk[1], X)
    dd = dk[2] - U0; impk = np.abs(dd[:, 0] * g[:, 0] + dd[:, 1] * g[:, 1]) / np.where(D > 0, D, np.inf)
    print('config %d vs config 0: max|U_k - U_0| = %.3e (rel %.3e), max impact of the difference %.3e, median %.3e' % (
        k, np.abs(dd).max(), (np.hypot(dd[:, 0], dd[:, 1]) / np.hypot(Ul[:, 0], Ul[:, 1])).max(), impk.max(), np.median(impk)))
    dUk = dk[2] - Ul; impl = np.abs(dUk[:, 0] * g[:, 0] + dUk[:, 1] * g[:, 1]) / np.where(D > 0, D, np.inf)
    print('   config %d vs lead: max|dU| %.3e, max impact %.3e, median impact %.3e' % (k, np.abs(dUk).max(), impl.max(), np.median(impl)))
# worst targets of config 0
j = np.argsort(-imp)[:6]
print('worst residual impacts (config 0): ' + '; '.join('(%.3f,%.3f) %.1e' % (X[i, 0], X[i, 1], imp[i]) for i in j))
