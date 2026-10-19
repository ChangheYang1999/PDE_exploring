# Strip and near-P maxima of |R|/N_f and |R|/N_v from resmap files (verifier, verifier). Usage: python3 strip_nv.py tag...
import sys, numpy as np
for t in sys.argv[1:]:
    d = np.load('runs/audit/%s_resmap.npz' % t); r, th, R, Nf, Nv = d['r'], d['th'], d['R'], d['Nf'], d['Nv']
    xs = float(d['x_star'])
    with np.errstate(all='ignore'):
        F = np.where(Nf > 0, np.abs(R) / Nf, 0.0); V = np.where(Nv > 0, np.abs(R) / Nv, 0.0)
    out = []
    for name, rm, tm in [('strip r 7.9-8.6 th<=0.08', (r >= 7.9) & (r <= 8.6), th <= 0.08),
                         ('right r 8.6-9.4 th<=0.08', (r > 8.6) & (r <= 9.4), th <= 0.08),
                         ('r 8.2-9.4 th 0.08-0.5', (r >= 8.2) & (r <= 9.4), (th > 0.08) & (th <= 0.5)),
                         ('r 6-12, th 0-0.6', (r >= 6) & (r <= 12), th <= 0.6)]:
        sf = F[np.ix_(rm, tm)]; sv = V[np.ix_(rm, tm)]
        a = np.unravel_index(np.argmax(sf), sf.shape); b = np.unravel_index(np.argmax(sv), sv.shape)
        out.append('%-26s N_f %.3e (r %.3f th %.4f)  N_v %.3e (r %.3f th %.4f)' % (name, sf.max(), r[rm][a[0]], th[tm][a[1]],
                   sv.max(), r[rm][b[0]], th[tm][b[1]]))
    print(t, 'x* %.6f' % xs); print('  ' + '\n  '.join(out))
