"""Compare two residual maps (vresmap.py npz, same grid) near P: R/N_f on the window, maxima by sub-window, the theta
spectrum of R/N_f next to the x-axis. Usage: python3 cmp_resmap.py tagA tagB"""
import sys, warnings
import numpy as np
warnings.simplefilter('ignore')
T = sys.argv[1:3]
D = {t: np.load('runs/audit/%s_resmap.npz' % t) for t in T}
r, th = D[T[0]]['r'], D[T[0]]['th']
assert np.allclose(r, D[T[1]]['r']) and np.allclose(th, D[T[1]]['th'])
q = {t: np.where(D[t]['Nf'] > 0, D[t]['R'] / D[t]['Nf'], 0.0) for t in T}
xs = float(D[T[0]]['x_star'])
X, Y = r[:, None] * np.cos(th)[None, :], r[:, None] * np.sin(th)[None, :]
win = {'all': np.ones_like(X, bool), '|X-P|<0.5': np.hypot(X - xs, Y) < 0.5, '|X-P|<0.5, y<0.2': (np.hypot(X - xs, Y) < 0.5) & (Y < 0.2),
       '|X-P|<0.5, y>=0.2': (np.hypot(X - xs, Y) < 0.5) & (Y >= 0.2), 'y<0.2, x 6-8.1': (Y < 0.2) & (X > 6) & (X < 8.1),
       'y<0.2, x 8.1-8.6': (Y < 0.2) & (X >= 8.1) & (X < xs), 'y<0.2, x>x*': (Y < 0.2) & (X >= xs), 'y 0.2-1, |x-x*|<1': (Y >= 0.2) & (Y < 1) & (abs(X - xs) < 1),
       'y>=1': Y >= 1}
for k, m in win.items():
    s = []
    for t in T:
        a = np.abs(q[t]) * m; i, j = np.unravel_index(np.argmax(a), a.shape)
        s.append('%s %.3e at (x %.3f, y %.4f) rms %.2e' % (t, a[i, j], X[i, j], Y[i, j], np.sqrt(np.mean(q[t][m] ** 2))))
    print('%-20s %s | %s' % (k, s[0], s[1]))
# theta spectrum of q along rows next to the axis, theta <= 0.6 window: dominant frequency in theta (per radian)
for x0 in (7.0, 8.0, 8.3, 8.45, 8.6, 8.8):
    i = np.argmin(abs(r - x0)); s = []
    for t in T:
        v = q[t][i, 1:]; n = len(v); F = np.abs(np.fft.rfft(v * np.hanning(n))); fr = np.fft.rfftfreq(n, th[1] - th[0]) * 2 * np.pi
        k = np.argmax(F[1:]) + 1; s.append('%s peak omega %.0f amp %.2e, max|q| th<0.05 %.2e' % (t, fr[k], F[k] * 2 / n * 2, np.max(np.abs(v[th[1:] < 0.05]))))
    print('r %.3f: %s | %s' % (r[i], s[0], s[1]))
