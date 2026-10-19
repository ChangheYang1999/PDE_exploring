# Lead exploration: node and zero structure of a finite-p forward steady state (pforward.py output).
import sys, json, numpy as np
sys.path.insert(0, '.')
import pforward as PF, p0_forward as P1
d = np.load(sys.argv[1]); g, lr, th = d['g'], d['lr'], d['th']
args = json.loads(str(d['args'])); p = args['p']; l = 1 / p
r = np.exp(lr); Nr, Nth = g.shape
rhoD = (r ** p)[:, None] * g
wr, wt = PF.velocity_p(rhoD, lr, th, p)
ar = l + wr / r[:, None]; at = wt / r[:, None]
print('node matrix fits on rings:')
for k in [0, 2, 4, 8, 16, 32, 64]:
    M = PF.node_matrix(ar[k], at[k], th); ev = np.linalg.eigvalsh(0.5 * (M + M.T))
    print('  r=%.3g: M=[%.4f %.4f; %.4f %.4f], eig %.4f %.4f' % (r[k], M[0, 0], M[0, 1], M[1, 0], M[1, 1], ev[0], ev[1]))
# density along the x axis (th = 0 and pi): local exponent
j0 = 0; jpi = Nth // 2
print('local exponent of rho along x axis: d log rho / d log r')
for k in [2, 8, 16, 32, 48, 64, 96, 128]:
    e0 = (np.log(rhoD[k + 1, j0]) - np.log(rhoD[k - 1, j0])) / (lr[k + 1] - lr[k - 1])
    epi = (np.log(rhoD[k + 1, jpi]) - np.log(rhoD[k - 1, jpi])) / (lr[k + 1] - lr[k - 1])
    print('  r=%.3g: th=0 %.4f  th=pi %.4f  rho(r,0)=%.4g' % (r[k], e0, epi, rhoD[k, j0]))
# angular zero order near th = pi/2 and 3pi/2: fit g ~ C |th - th0|^n on the 3 nearest points
for rr in [0.01, 0.1, 1, 10, 100, 1000, 10000]:
    k = np.searchsorted(r, rr)
    out = []
    for th0 in [np.pi / 2, 3 * np.pi / 2]:
        j = int(round(th0 / (2 * np.pi) * Nth))
        jj = np.array([j + 1, j + 2, j + 4]); dt = th[jj] - th[j]
        gg = g[k, jj]
        n = np.polyfit(np.log(dt), np.log(np.maximum(gg, 1e-300)), 1)[0]
        out.append('th0=%.0f: g(th0)=%.2g order %.3f' % (np.degrees(th0), g[k, j], n))
    print('  r=%.3g: ' % r[k] + ' | '.join(out))
