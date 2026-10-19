"""Reduce vchar_dense output (G69 (e)): spread of J by label subset and family; resolution in theta0."""
import json, sys, numpy as np
for f in sys.argv[1:]:
    d = json.load(open(f)); rows = d['rows']; eps = d['summary']['eps_P']
    fam = np.array([r['fam'] for r in rows]); th = np.array([r['theta0'] for r in rows])
    J = np.array([r['J'] for r in rows], float); dt = np.array([r['dtol'] for r in rows]); rmin = np.array([r['rmin'] for r in rows])
    yc = np.array([r['ycross'] for r in rows], float)
    print(f.split('/')[-1], 'n', len(rows), 'max dtol %.1e' % np.nanmax(dt), 'min rmin %.2e' % rmin.min(), 'NaN J(.01) %d' % np.isnan(J[:, 6]).sum())
    A = fam == 'A'
    def sp(m, i):
        v = J[m, i]; return np.nanmax(v) - np.nanmin(v)
    nA = A.sum()
    for step in (32, 16, 8, 4, 2, 1):
        if nA < 100 and step > 4: continue
        m = np.zeros(len(rows), bool); idx = np.nonzero(A)[0][::step]; m[idx] = True
        print('  A every %2d (%3d): J.1 %.3e J.03 %.3e J.01 %.3e' % (step, m.sum(), sp(m, 4), sp(m, 5), sp(m, 6)))
    for name, m in (('A', A), ('B', fam == 'B'), ('C', fam == 'C'), ('all', np.ones(len(rows), bool))):
        if m.sum() == 0: continue
        print('  %-3s (%3d): J.03 %.3e .. %.3e spread %.3e | J.01 %.3e .. %.3e spread %.3e' % (
            name, m.sum(), np.nanmin(J[m, 5]), np.nanmax(J[m, 5]), sp(m, 5), np.nanmin(J[m, 6]), np.nanmax(J[m, 6]), sp(m, 6)))
    i5 = np.nanargmax(J[:, 5]); j5 = np.nanargmin(J[:, 5])
    print('  J.03 max at %s %.6f (rmin %.3g, ycross %.3g); min at %s %.6f (rmin %.3g, ycross %.3g)' % (
        fam[i5], th[i5], rmin[i5], yc[i5], fam[j5], th[j5], rmin[j5], yc[j5]))
    # theta0 bins for family A: spread inside each bin
    if nA > 100:
        tA = th[A]; JA = J[A, 5]
        for lo, hi in ((0.0, 0.5), (0.5, 1.0), (1.0, 1.35), (1.35, 1.45), (1.45, 1.6)):
            m = (tA >= lo) & (tA < hi)
            if m.sum(): print('    theta0 [%.2f, %.2f): n %3d J.03 %.3e .. %.3e, median neighbour |dJ| %.1e' % (
                lo, hi, m.sum(), JA[m].min(), JA[m].max(), np.median(np.abs(np.diff(JA[m])))))
