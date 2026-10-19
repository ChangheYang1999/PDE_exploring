"""Verifier scratch: parts of the third-order residual R3 of code/far2_ver.py (same construction), and the four series terms
at given radii in L. Usage: python3 far2_parts.py shape.npz nt"""
import sys
import numpy as np
sys.path.insert(0, 'code')
from far2_ver import jets
d = np.load(sys.argv[1], allow_pickle=True); nt = int(sys.argv[2])
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
parts = {}
for o1 in V:
    for o2 in orders:
        o = (o1[0] + o2[0] + 1, o1[1] + o2[1])
        if o == (3, 0):
            parts['U%s.grad A%s' % (o1, o2)] = a[o2] * V[o1][0] * A[o2] + V[o1][1] * dA[o2]
parts['(c_l a - 1) A3'] = (cl * a[(3, 0)] - 1) * A[(3, 0)]
for tw in (1.56811, 0.81819):
    i = int(round(tw / (2 * np.pi) * nt))
    s = sum(p[i] for p in parts.values())
    print('theta %.5f  R3/A0 %+.6e' % (t[i], s / T0[i]))
    for kk, p in parts.items():
        print('   %-26s %+.6e' % (kk, p[i] / T0[i]))
q = dict(q1=0.01582165901, q2=-88.78237, qh=782.1024, q3=1.190005e5)
for rl in (3000, 4700, 4858, 9500, 3e4):
    r = rl * L; de = r ** (k - 1)
    tt = (q['q1'] * de, q['q2'] * de ** 2, q['qh'] * r ** -2, q['q3'] * de ** 3)
    print('r %7g L  q1 d %+.4e  q2 d^2 %+.4e  qh r^-2 %+.4e  q3 d^3 %+.4e  sum %+.4e  (q1+q2 %+.3e)' % (rl, *tt, sum(tt), tt[0] + tt[1]))
