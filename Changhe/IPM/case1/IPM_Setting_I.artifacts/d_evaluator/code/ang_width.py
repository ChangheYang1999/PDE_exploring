import sys
import numpy as np
d = np.load(sys.argv[1])
r, ms, Fs, taus = d['r'], d['ms'], d['F'], d['tau']
th = np.linspace(0, np.pi / 2, 2001)
S = np.sin(np.outer(ms, th))
for i in [int(a) for a in sys.argv[2].split(',')]:
    print('tau %.3f' % taus[i])
    for rr in (3, 10, 30, 100, 300, 1000, 1e4):
        j = np.searchsorted(r, rr)
        f = Fs[i][:, j]
        rho = f @ S
        slope0 = (ms * f).sum()            # d rho/d theta at theta = 0
        mx = np.abs(rho).max()
        # width of the axis layer: first theta where rho reaches half its max
        k = np.argmax(np.abs(rho) >= 0.5 * mx)
        tail = np.abs(f[-len(ms) // 8:]).max() / np.abs(f).max()
        print('  r %8.3g  max|rho| %.3g at th %.1f deg; slope0/max %.3g; half-rise th %.2f deg; tail(top 1/8 of m)/max %.2e'
              % (r[j], mx, np.degrees(th[np.argmax(np.abs(rho))]), slope0 / mx, np.degrees(th[k]), tail))
