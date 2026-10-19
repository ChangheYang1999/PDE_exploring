"""DMD of the frozen-c_l DR run C (linear phase): leading eigenvalues of the time-0.025 map on D_k = F_k - F0."""
import numpy as np, glob
z = np.load('runs/c1dr2/C_clfix_F0.npz'); F0, r, ms = z['F'], z['r'], z['ms']
fs = sorted(glob.glob('runs/c1dr2/C_clfix_snap0*.npz'))
S = [np.load(f) for f in fs]
tau = np.array([float(s['tau']) for s in S])
D = [s['F'] - F0 for s in S]
# weight: relative to the local profile scale |F0| summed over modes, so the far field does not dominate by size
wr = 1 / (np.abs(F0).max(0) + 1e-300)
X = np.array([(d * wr[None, :]).ravel() for d in D]).T
nrm = np.linalg.norm(X, axis=0)
print('tau', np.round(tau, 4))
print('norm growth per snap', np.round(nrm[1:] / nrm[:-1], 4))
dt = np.diff(tau).mean()
print('rate per unit tau', np.round(np.log(nrm[1:] / nrm[:-1]) / dt, 2))
for k0, k1 in ((0, 8), (2, 8), (0, 6), (3, 10)):
    Y = X[:, k0:k1]
    U, s, Vt = np.linalg.svd(Y[:, :-1], full_matrices=False)
    rk = (s > 1e-6 * s[0]).sum()
    U, s, Vt = U[:, :rk], s[:rk], Vt[:rk]
    At = U.T @ Y[:, 1:] @ Vt.T / s
    ev, W = np.linalg.eig(At)
    o = np.argsort(-np.abs(ev))
    lam = np.log(ev[o].astype(complex)) / dt
    print('snaps %d..%d rank %d  continuous eigenvalues:' % (k0, k1 - 1, rk), ' '.join('%.2f%+.2fi' % (l.real, l.imag) for l in lam[:5]))
# shape of the leading direction: last linear snapshot
k = 7
d = D[k]
prof_r = np.abs(d).max(0) / np.abs(F0).max(0)
for a, b in ((1e-3, 0.1), (0.1, 1), (1, 3), (3, 10), (10, 30), (30, 100), (100, 1e3), (1e3, 1e5)):
    sel = (r >= a) & (r < b)
    print('r in [%g, %g): max|D|/max|F0| = %.2e' % (a, b, prof_r[sel].max()))
am = np.abs(d).max(1)
print('mode m with max |D|:', ms[np.argsort(-am)[:6]], 'm>100 share %.1e' % (am[ms > 100].max() / am.max()))
