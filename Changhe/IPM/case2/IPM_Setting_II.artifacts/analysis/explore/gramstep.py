# Lead: Newton step for the fpnloc residual in the Gram (L2) metric: r = L^T c (G = X^T X / N = L L^T), m1 weight wm.
# Usage: python3 gramstep.py log J.npz K ws wm [line]
import sys, json
import numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE
logf, Jf, K = sys.argv[1], sys.argv[2], int(sys.argv[3]); ws = [float(v) for v in sys.argv[4].split(',')]; wm = float(sys.argv[5])
line = int(sys.argv[6]) if len(sys.argv) > 6 else 0
def basis(t):
    out = [FE.basis(t, K)] if K > 0 else []
    s = np.sin(t)
    for w in ws: out.append(np.exp(-(1 - s) / w)[None, :])
    for w in ws: out.append(np.exp(-(1 + s) / w)[None, :])
    return np.vstack(out)
thA = 2 * np.pi * np.arange(2048) / 2048
w = np.abs(np.cos(thA)) > 0.02
X = np.vstack([np.ones_like(thA), basis(thA)]).T[w]
# residual coefficients exclude the constant: project out the constant from the basis columns
Xc = X[:, 1:] - X[:, 1:].mean(0)
G = Xc.T @ Xc / len(Xc); L = np.linalg.cholesky(G)
recs = [json.loads(l) for l in open(logf)]
rec = [r for r in recs if 'R' in r][line]
R = np.array(rec['R']); J = np.load(Jf)['J']
nb = len(R) - 1
T = np.zeros((nb + 1, nb + 1)); T[:nb, :nb] = L.T; T[nb, nb] = wm / float(rec.get('wm', 1.0) if 'wm' in rec else 1.0)
Rg = T @ R; Jg = T @ J
print('normR coef', np.linalg.norm(R).round(4), 'normR gram', np.linalg.norm(Rg).round(4), 'L2 in-span', np.linalg.norm(Rg[:nb]).round(4))
print('sv gram', np.linalg.svd(Jg, compute_uv=False).round(4))
dz = np.linalg.lstsq(Jg, -Rg, rcond=1e-8)[0]
print('dz gram', dz.round(3))
dzc = np.linalg.lstsq(J, -R, rcond=1e-8)[0]
print('dz coef', dzc.round(3))
print('predicted dm1 gram', (J[nb] @ dz).round(4), 'coef', (J[nb] @ dzc).round(4))
