"""Compare two genfn states sampled by gphys.py on the SAME physical polar grid: relative differences of Theta, Omega, U1, U2 by radius
bin (max |diff| / max |field| in the bin), and each state's max |R_Omega|/N_Omega by bin. Usage: compare_phys.py A.npz B.npz"""
import sys, numpy as np
A = np.load(sys.argv[1]); B = np.load(sys.argv[2])
assert np.allclose(A['r'], B['r']) and np.allclose(A['phi'], B['phi']), 'grids differ'
nr, nph = len(A['r']), len(A['phi']); R = np.repeat(A['r'], nph)
edges = [0, 0.01, 0.1, 1, 10, 100, 1e4, 1e6, np.inf]
print('a0: %.4f vs %.4f (rel diff %.2e)' % (float(A['a0']), float(B['a0']), abs(float(A['a0']) - float(B['a0'])) / abs(float(A['a0']))))
print('%-14s' % 'bin' + ''.join('%12s' % k for k in ['Theta', 'Omega', 'U1', 'U2', 'Psi']) + '%14s%14s' % ('maxR/N A', 'maxR/N B'))
for lo, hi in zip(edges[:-1], edges[1:]):
    m = (R >= lo) & (R < hi)
    if not m.any(): continue
    row = '%-14s' % ('[%g, %g)' % (lo, hi))
    for k in ['Theta', 'Omega', 'U1', 'U2', 'Psi']:
        a, b = A[k][m], B[k][m]
        row += '%12.2e' % (np.abs(a - b).max() / np.abs(a).max())
    qa = (np.abs(A['R_Omega']) / A['N_Omega'])[m]; qb = (np.abs(B['R_Omega']) / B['N_Omega'])[m]
    row += '%14.2e%14.2e' % (qa.max(), qb.max())
    print(row)
# location of the maxima
for name, D in [('A', A), ('B', B)]:
    q = np.abs(D['R_Omega']) / D['N_Omega']; i = int(np.argmax(q)); print('%s: max R/N %.3e at r %.3g phi %.1f deg' % (name, q[i], np.hypot(D['X'][i], D['Y'][i]), np.degrees(np.arctan2(D['Y'][i], D['X'][i]))))
