"""V115: report (version of 11:04Z) Section 4.14(f) check. Gbar R = (G_+(R) + G_-(R)) R / 2 with G_+- = median of rho/x^2 over the ring
r = R, |cos th| > 1/2, upper / lower half-plane, on own exit-map states. Values at R = e^t, t = -13..-10, by linear
interpolation in t of the ring medians (the ring medians are taken on the stored radial nodes). Usage: python3 v115_gbar.py A.npz ..."""
import sys, numpy as np
for fn in sys.argv[1:]:
    d = np.load(fn, allow_pickle=True); R = d['rho']; r = d['r']; th = d['th']; t = np.log(r)
    up = np.sin(th) > 0; sel = np.abs(np.cos(th)) > 0.5
    x2 = (r[:, None]*np.cos(th)[None, :])**2
    Gp = np.array([np.median((R[i]/x2[i])[sel & up]) for i in range(len(r))])
    Gm = np.array([np.median((R[i]/x2[i])[sel & ~up]) for i in range(len(r))])
    o = np.argsort(t)
    out = []
    for tt in (-13, -12, -11, -10):
        gp = np.interp(tt, t[o], Gp[o]); gm = np.interp(tt, t[o], Gm[o])
        out.append('t %d Gbar R %.3f (G+ %.4g G- %.4g)' % (tt, 0.5*(gp + gm)*np.exp(tt), gp, gm))
    print(fn, 'tmin %.2f' % t.min()); print('  ' + '; '.join(out))
