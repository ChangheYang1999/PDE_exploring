"""Verifier scratch (shift 6): for each shape, at theta 1.56811 (next to the y-axis) the far-field series coefficients of
code/far2_ver.py and, per order j = 1, 2, 3, |R_j| / max(|pure part|, |velocity part|) with pure = (c_l a_j - 1) A_j and
velocity = sum of U.grad terms of order j (the lead's 19:34:02Z item 1 ratio), and the series sum at 4858 L.
Usage: python3 far2_rel.py nt label=shape.npz ..."""
import sys
import numpy as np
sys.path.insert(0, 'code')
from far2_ver import jets, main as far2
nt = int(sys.argv[1])
for arg in sys.argv[2:]:
    lab, path = arg.split('=')
    d = np.load(path, allow_pickle=True)
    t = 2 * np.pi * np.arange(nt) / nt
    J = jets(d, t); k, L = J['k'], J['L']; cl = 1 / k
    n = np.fft.rfftfreq(nt, 1.0 / nt)
    D = lambda f: np.fft.irfft(1j * n * np.fft.rfft(f), nt)
    l1, l2, l3 = J['lam'][1:]; lh = J['lamh']; T0 = J['T0']
    orders = [(0, 0), (1, 0), (2, 0), (0, 1), (3, 0)]
    a = {o: k + o[0] * (k - 1) - 2 * o[1] for o in orders}
    A = {(0, 0): T0, (1, 0): T0 * l1, (2, 0): T0 * (l2 + l1 ** 2 / 2), (0, 1): T0 * lh, (3, 0): T0 * (l3 + l1 * l2 + l1 ** 3 / 6)}
    dA = {o: D(A[o]) for o in orders}
    V = {}
    for o in [(0, 0), (1, 0), (2, 0)]:
        g = a[o] * np.cos(t) * A[o] - np.sin(t) * dA[o]
        Fh = np.fft.rfft(g) / (n ** 2 - (a[o] + 1) ** 2)
        V[o] = (-np.fft.irfft(1j * n * Fh, nt), (a[o] + 1) * np.fft.irfft(Fh, nt))
    UG = {o: np.zeros(nt) for o in orders}
    for o1 in V:
        for o2 in orders:
            o = (o1[0] + o2[0] + 1, o1[1] + o2[1])
            if o in UG:
                UG[o] = UG[o] + a[o2] * V[o1][0] * A[o2] + V[o1][1] * dA[o2]
    i = int(round(1.56811 / (2 * np.pi) * nt))
    rel = []
    for o in [(1, 0), (2, 0), (3, 0)]:
        pure = (cl * a[o] - 1) * A[o][i]; vel = UG[o][i]
        rel.append(abs(pure + vel) / max(abs(pure), abs(vel)))
    out, prof = far2(path, nt, (1.56811,))
    row = out['rows'][0]
    r = 4858 * L; de = r ** (k - 1)
    s = row['q1'] * de + row['q2'] * de ** 2 + row['qh'] * r ** -2 + row['q3'] * de ** 3
    print('%-4s theta %.5f q1 %.6e q2 %.5f qh %.4f q3 %.6e  rel %.3e %.4f %.4f  sum4858 %.4e  (k %.12f L %.9f)' % (
        lab, row['theta'], row['q1'], row['q2'], row['qh'], row['q3'], *rel, s, k, L))
