"""Independent strain moment of published forward states (g on a uniform log-r grid lr, rho = r^p g):
c = (1/pi) int rho r^-3 sin 3th dX = (1/pi) int int g e^{(p-1) t} sin 3th dt dth (Simpson in t, rectangle (spectral) in th)
+ tail beyond r_max with rho = r^p g(r_max, th): (1/pi) int g_last sin 3th dth * r_max^(p-1)/(1-p);
d = psi_xx(0)-moment (1/pi) int rho r^-3 cos 3th dX (b = psi_yy(0) = -psi_xx(0) up to sign convention: only |d| reported).
m1 = l - sqrt(c^2 + d^2). Inner part r < e^lr0 neglected (O(e^{(gamma-1) lr0}))."""
import sys, json, glob, math, numpy as np
from scipy.integrate import simpson
rows = []
for f in sys.argv[1:]:
    d = np.load(f)
    g, lr, th = d['g'], d['lr'], d['th']
    args = json.loads(str(d['args'])) if 'args' in d.files else {}
    p = float(args.get('p', 0.5)); l = 1/p
    w = np.exp((p - 1)*lr)[:, None]
    dth = 2*math.pi/len(th)
    S3 = simpson(g*w, x=lr, axis=0); 
    c = (np.sum(S3*np.sin(3*th))*dth + np.sum(g[-1]*np.sin(3*th))*dth*math.exp((p - 1)*lr[-1])/(1 - p))/math.pi
    dd = (np.sum(S3*np.cos(3*th))*dth + np.sum(g[-1]*np.cos(3*th))*dth*math.exp((p - 1)*lr[-1])/(1 - p))/math.pi
    m1 = l - math.hypot(c, dd)
    hist = d['hist'] if 'hist' in d.files else None
    rep = None
    if hist is not None:
        try:
            H = json.loads(str(hist)); last = H[-1]
            rep = last.get('m1', last.get('ring8', {}).get('m1'))
        except Exception:
            pass
    rows.append((f.split('/')[-1], p, args.get('kind'), args.get('par'), c, dd, m1, rep, g.shape))
    print('%-34s p %.2f %-9s par %-5s c %.5f d %+.1e m1(mine) %.5f  m1(reported) %s  grid %s' % rows[-1], flush=True)
