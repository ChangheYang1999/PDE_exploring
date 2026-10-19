#!/usr/bin/env python3
"""Right singular vectors of the x-odd block J_oo from parity-free Jacobian files (merged as in tests/pfwd_par_svd.py); writes pertfiles for mode=nsolve.
usage: python3 tests/pfwd_par_svec.py out_prefix J1.npz [J2.npz ...]   -> out_prefix_svec1.npz (smallest), _svec2.npz, ... (keys v [Ko], cols [names], s)"""
import sys, json, numpy as np
out = sys.argv[1]; files = sys.argv[2:]
d = np.load(files[0], allow_pickle=True); J = d['J'].copy(); rows = [str(r) for r in d['row_names']]
for fn in files[1:]:
    d2 = np.load(fn, allow_pickle=True); J2 = d2['J']; assert J2.shape == J.shape
    for j in range(J.shape[1]):
        if not np.all(np.isfinite(J[:, j])) and np.all(np.isfinite(J2[:, j])): J[:, j] = J2[:, j]
K = sum(1 for r in rows if r.startswith('a')); Ko = sum(1 for r in rows if r.startswith('b')); nz = 2 if 'G_up' in rows else 0
odd_rows = np.array([r.startswith('b') or r in ('M_up', 'M_dn', 'psi_yy0', 'G_up', 'G_dn') for r in rows]); odd_cols = np.array([False] * K + [True] * Ko + [True] * nz + [False])
names = ['a%d' % (j + 1) for j in range(K)] + ['b%d' % (j + 1) for j in range(Ko)] + (['t1', 't2'] if nz else []) + ['p']
oc = [j for j in range(J.shape[1]) if odd_cols[j] and np.all(np.isfinite(J[:, j]))]
Joo = J[odd_rows][:, oc]; U, S, Vt = np.linalg.svd(Joo, full_matrices=False)
print('J_oo', Joo.shape, 'columns', [names[j] for j in oc]); print('singular values', ' '.join('%.4g' % v for v in S))
for k in range(min(4, len(S))):
    v = Vt[-1 - k]; s = S[-1 - k]
    if v[np.argmax(np.abs(v))] < 0: v = -v
    print('svec%d s=%.4g :' % (k + 1, s), ' '.join('%s %+.3f' % (names[oc[i]], v[i]) for i in range(len(oc))))
    np.savez('%s_svec%d.npz' % (out, k + 1), v=v, cols=np.array([names[j] for j in oc]), s=s, files=np.array(files))
print('written', out + '_svec{1..%d}.npz' % min(4, len(S)))
