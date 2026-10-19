# Location of the N_f and N_v maxima on a 2-10 band map (verifier, verifier). Usage: python3 band_nv.py tag...
import sys, numpy as np
for t in sys.argv[1:]:
    d = np.load('runs/audit/%s_resmap.npz' % t); r, th, R, Nf, Nv = d['r'], d['th'], d['R'], d['Nf'], d['Nv']
    ok = (th > 1e-6) & (th < np.pi / 2 - 1e-6); th, R, Nf, Nv = th[ok], R[:, ok], Nf[:, ok], Nv[:, ok]
    with np.errstate(all='ignore'):
        F = np.abs(R) / Nf; V = np.abs(R) / Nv
    print(t)
    for name, rm, tm in [('2-10 all', r > 0, th > 0), ('r 2-6', r < 6, th > 0), ('r 6-12 th<=0.6', r >= 6, th <= 0.6),
                         ('r 6-12 th>0.6', r >= 6, th > 0.6), ('th>1.4 (y axis)', r > 0, th > 1.4)]:
        sf = F[np.ix_(rm, tm)]; sv = V[np.ix_(rm, tm)]
        a = np.unravel_index(np.argmax(sf), sf.shape); b = np.unravel_index(np.argmax(sv), sv.shape)
        print('  %-16s N_f %.3e (r %.3f th %.4f)  N_v %.3e (r %.3f th %.4f)' % (name, sf.max(), r[rm][a[0]], th[tm][a[1]],
              sv.max(), r[rm][b[0]], th[tm][b[1]]))
