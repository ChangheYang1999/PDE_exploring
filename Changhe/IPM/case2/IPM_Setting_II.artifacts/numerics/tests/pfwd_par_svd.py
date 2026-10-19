"""Singular values of the x-odd block J_oo and cross-block norms from a parity-free Jacobian file (code/pfwd_parity.py mode=lincol / jodd / search).
Usage: python3 tests/pfwd_par_svd.py J1.npz [J2.npz ... merged] [cmp=other_J.npz for a column-by-column comparison]"""
import sys, json, numpy as np
files = [a for a in sys.argv[1:] if not a.startswith('cmp=')]; cmp = [a[4:] for a in sys.argv[1:] if a.startswith('cmp=')]
d = np.load(files[0], allow_pickle=True); J = d['J'].copy(); rows = list(d['row_names']); recs = json.loads(str(d['recs'])) if 'recs' in d.files else []
for fn in files[1:]:                                                      # merge further files (columns that are NaN in the first file)
    d2 = np.load(fn, allow_pickle=True); J2 = d2['J']; assert J2.shape == J.shape, (fn, J2.shape, J.shape)
    for j in range(J.shape[1]):
        if not np.all(np.isfinite(J[:, j])) and np.all(np.isfinite(J2[:, j])): J[:, j] = J2[:, j]
    recs += json.loads(str(d2['recs'])) if 'recs' in d2.files else []
K = sum(1 for r in rows if r.startswith('a')); Ko = sum(1 for r in rows if r.startswith('b')); nz = 2 if 'G_up' in rows else 0
odd_rows = np.array([r.startswith('b') or r in ('M_up', 'M_dn', 'psi_yy0', 'G_up', 'G_dn') for r in rows]); odd_cols = np.array([False] * K + [True] * Ko + [True] * nz + [False])
have = np.all(np.isfinite(J), axis=0)
print('columns available:', int(have.sum()), 'of', J.shape[1]); names = ['a%d' % (j + 1) for j in range(K)] + ['b%d' % (j + 1) for j in range(Ko)] + (['t1', 't2'] if nz else []) + ['p']
oc = [j for j in range(J.shape[1]) if odd_cols[j] and have[j]]
if oc:
    Joo = J[odd_rows][:, oc]; Jeo = J[~odd_rows][:, oc]
    sv = np.linalg.svd(Joo, compute_uv=False)
    print('J_oo shape', Joo.shape, 'singular values', ' '.join('%.4g' % v for v in sv))
    print('cross block (even rows, odd cols) Frobenius %.4g  vs  odd block Frobenius %.4g' % (np.linalg.norm(Jeo), np.linalg.norm(Joo)))
    print('per-column: name |col_odd| |col_even| (rows: 16 odd LSQ | M_up M_dn | psi_yy0 | G_up G_dn contributions)')
    for j in oc:
        c = J[:, j]; co = c[odd_rows]
        extra = ('  G %9.4g %9.4g' % (c[rows.index('G_up')], c[rows.index('G_dn')])) if nz else ''
        print('  %-4s %9.4g %9.4g   lsq_odd %9.4g  M %9.4g %9.4g  psi_yy %9.4g%s' % (names[j], np.linalg.norm(co), np.linalg.norm(c[~odd_rows]), np.linalg.norm(co[:Ko]), c[rows.index('M_up')], c[rows.index('M_dn')], c[rows.index('psi_yy0')], extra))
    if Joo.shape[1] == Ko + nz:
        U, S, Vt = np.linalg.svd(Joo, full_matrices=False)
        print('smallest right singular vector (datum direction):', ' '.join('%s %.3f' % (names[oc[i]], Vt[-1, i]) for i in np.argsort(-np.abs(Vt[-1]))[:6]))
        print('largest  right singular vector:', ' '.join('%s %.3f' % (names[oc[i]], Vt[0, i]) for i in np.argsort(-np.abs(Vt[0]))[:6]))
for r in recs:
    if 'gmres_resid' in r:
        print('  col %s gmres k %d Hess resid %.4g  TRUE resid %s  H_sv min %.4g max %.4g  dF_odd %.4g dF_even %.4g  defect of linear state %s  smooth %s eps %s' % (names[r['col']], r['gmres_k'], r['gmres_resid'][-1], ('%.3g' % r['resid_true']) if 'resid_true' in r else 'n/a', r['H_sv'][-1], r['H_sv'][0], r['dF_odd'], r['dF_even'], ['%.3g' % v for v in r['defect_of_linear_state']], r.get('smooth'), r.get('eps_rel')))
for fn in cmp:
    d2 = np.load(fn, allow_pickle=True); J2 = d2['J']; print('comparison with', fn)
    for j in range(J.shape[1]):
        if np.all(np.isfinite(J[:, j])) and np.all(np.isfinite(J2[:, j])):
            dcol = J[:, j] - J2[:, j]
            print('  compare %s: |diff| %.4g (odd %.4g) vs |col| %.4g (odd %.4g)' % (names[j], np.linalg.norm(dcol), np.linalg.norm(dcol[odd_rows]), np.linalg.norm(J[:, j]), np.linalg.norm(J[odd_rows, j])))
