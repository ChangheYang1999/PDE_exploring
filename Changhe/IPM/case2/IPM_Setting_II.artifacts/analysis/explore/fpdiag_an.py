# Lead exploration: analyse fpdiag output: response of log|Xi|^2 to datum perturbations, on the x-even modes.
import sys
import numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE
d = np.load(sys.argv[1]); N = int(sys.argv[2]) if len(sys.argv) > 2 else 6; cut = 0.05
logA, logAn, m1, a = d['logA'], d['logAn'], d['m1'], d['a']
nA = logA.shape[1]; th = 2 * np.pi * np.arange(nA) / nA
w = np.abs(np.cos(th)) > cut
X = np.vstack([np.ones(nA), FE.basis(th, N)]).T[w]
proj = lambda f: np.linalg.lstsq(X, f[w], rcond=None)[0][1:]
L0 = 2 * m1[0] * logAn[0]
print('base m1 %.5f' % m1[0])
np.set_printoptions(precision=4, suppress=True, linewidth=160)
for j in range(1, len(m1)):
    da = a[j] - a[0]; h = np.max(np.abs(da)); k = int(np.argmax(np.abs(da)))
    dL = 2 * m1[j] * logAn[j] - L0          # delta log |Xi|^2
    dLt = dL - 2 * (m1[j] - m1[0]) * logAn[0] * 0  # (same; kept for clarity)
    print('mode %d (h %.3f): dm1/da = %.4f ; DT column (dlog|Xi|^2 / da on modes) =' % (k + 1, h, (m1[j] - m1[0]) / h), proj(dL) / h)
    print('        residual of fit (rms, /h): %.4f' % (np.sqrt(np.mean((dL[w] - X @ np.linalg.lstsq(X, dL[w], rcond=None)[0]) ** 2)) / h))
