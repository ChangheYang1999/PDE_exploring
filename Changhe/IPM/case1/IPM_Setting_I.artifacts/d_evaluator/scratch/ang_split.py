# Split the residual map R(r, theta) into angular bands n < ncut and n >= ncut (sin(n theta), n odd, on [0, pi/2])
# and report max |R_band|/N_f per region. Usage: python3 ang_split.py tag [ncut]
import sys, numpy as np
t = sys.argv[1]; ncut = int(sys.argv[2]) if len(sys.argv) > 2 else 195
d = np.load('runs/audit/%s_resmap.npz' % t); r = d['r']; th = d['th']
j1 = np.argmin(abs(th - np.pi/2)); T = th[:j1+1]; R = d['R'][:, :j1+1]; Nf = d['Nf'][:, :j1+1]
n = np.arange(1, 2*len(T), 2); S = np.sin(np.outer(T, n))
w = np.full(len(T), T[1]-T[0]); w[0] *= .5; w[-1] *= .5
C = (R*w) @ S * 4/np.pi
lo = C[:, n < ncut] @ S[:, n < ncut].T; hi = C[:, n >= ncut] @ S[:, n >= ncut].T
ok = (T > 1e-3) & (T < np.pi/2 - 1e-3); Ninv = np.where(Nf > 0, 1/np.where(Nf > 0, Nf, 1), 0)
print('%s: reconstruction error max %.1e (rel to max|R| %.1e)' % (t, abs(lo+hi-R)[:, ok].max(), abs(R).max()))
for (a, b, ta, tb) in [(6, 8.2, 0, .1), (6, 8.2, .1, 1.6), (8.2, 9.4, 0, .1), (8.2, 9.4, .1, .5), (8.2, 9.4, .5, 1.6), (9.4, 9.7, 0, 1.6), (9.7, 11, 0, 1.6), (11, 14, 0, 1.6)]:
    i = (r >= a) & (r < b); jj = ok & (T >= ta) & (T < tb)
    out = []
    for nm, F in [('all', R), ('n<%d' % ncut, lo), ('n>=%d' % ncut, hi)]:
        e = abs(F[np.ix_(i, jj)])*Ninv[np.ix_(i, jj)]; k = np.unravel_index(np.argmax(e), e.shape)
        out.append('%s %.2e (r %.3f th %.3f)' % (nm, e.max(), r[i][k[0]], T[jj][k[1]]))
    print('  r %4.1f-%4.1f th %.1f-%.1f: ' % (a, b, ta, tb) + '; '.join(out))
