"""Verifier scratch (shift 6): maxima of |R| / N_f on the vresmap windows of scratch/phase_scan.sh (and the unshifted
maps if given): near P (|X - P| < 0.5), the lobe (r 8.5-9.0, theta 0.12-0.30), and the window with ya >= 0.006.
Usage: python3 phase_read.py map.npz ..."""
import sys
import numpy as np
for f in sys.argv[1:]:
    d = np.load(f)
    r, th, R, Nf = d['r'], d['th'], d['R'], d['Nf']
    q = np.where(Nf > 0, np.abs(R) / np.where(Nf > 0, Nf, 1), 0.0)
    X, Y = r[:, None] * np.cos(th)[None, :], r[:, None] * np.sin(th)[None, :]
    P = float(d['x_star'])
    out = []
    for lab, m in (('nearP', (X - P) ** 2 + Y ** 2 < 0.25),
                   ('lobe', (r[:, None] >= 8.5) & (r[:, None] <= 9.0) & (th[None, :] >= 0.12) & (th[None, :] <= 0.30)),
                   ('window', np.ones_like(q, bool))):
        qq = np.where(m, q, -1)
        i, j = np.unravel_index(np.argmax(qq), q.shape)
        out.append('%s %.4e (r %.4f th %.4f)' % (lab, q[i, j], r[i], th[j]))
    print(f.split('/')[-1], ' r[0] %.6f dlnr %.3e' % (r[0], np.log(r[1] / r[0])), ' | '.join(out))
