# Lead: half-disc model of the strain moment. dc/dlr of the state (m1mom formula) against (14/(15 pi)) (G_up - G_lo) r with
# G_up / G_lo = median rho/x^2 over |cos th| > 0.5 in the upper / lower half-plane at each radius. Usage: python3 cmodel.py s.npz ...
import sys, numpy as np
for f in sys.argv[1:]:
    s = np.load(f); g, lr, th, p = s['g'], s['lr'], s['th'], float(s['p']); r = np.exp(lr)
    up = np.sin(th) > 0; sel = np.abs(np.cos(th)) > 0.5
    rho = (r ** p)[:, None] * g; x2 = (r[:, None] * np.cos(th)[None, :]) ** 2
    q = rho / np.maximum(x2, 1e-300)
    Gu = np.median(np.where(sel & up, q, np.nan), axis=1) if False else np.array([np.median(q[i][sel & up]) for i in range(len(lr))])
    Gl = np.array([np.median(q[i][sel & ~up]) for i in range(len(lr))])
    w = np.exp((p - 1) * lr)[:, None] * g * np.sin(3 * th)[None, :]
    net = 2 * w.mean(axis=1)                      # d c / d lr
    model = 14 / (15 * np.pi) * (Gu - Gl) * r     # half-disc model, d c / d lr
    print(f)
    for lo, hi in [(-14.1, -12), (-12, -10), (-10, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 10.1)]:
        m = (lr >= lo) & (lr <= hi)
        print('  %6.1f..%5.1f  c_band %+.3f  model %+.3f  log(Gl/Gu) mid %+.3f' % (lo, hi, np.trapz(net[m], lr[m]), np.trapz(model[m], lr[m]), np.log(Gl[m][len(Gl[m])//2] / Gu[m][len(Gu[m])//2])))
