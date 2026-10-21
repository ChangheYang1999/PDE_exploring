# Quasi-homogeneity at A = 3, g = 5.5 with the rescaled representation v(mu^A s, mu y) = mu * [packet with
# lam = mu^(2-2A)] (tol 1e-30), Taylor terms of quasi-degree < 1+g subtracted (Beta integrals), then also the
# supercritical terms (1,5), (3,1), (1,7) with analytically continued Beta coefficients; predicted remainder O(mu^4).
import sys, json, numpy as np
sys.path.insert(0, 'code/frozen')
import vpacket as V
from frozen_checks_lib import taylor_coef, u0
A, g = 3.0, 5.5
out = []
for (s, y) in [(0.5, 0.5), (-0.3, 1.0), (1.0, 0.2)]:
    U0v = u0(A, g, s, y, 'g55')
    sub = {(j, k): taylor_coef(A, g, j, k) for (j, k) in [(1, 1), (1, 3)]}
    sup = {(j, k): taylor_coef(A, g, j, k) for (j, k) in [(1, 5), (3, 1), (1, 7)]}
    print('(s,y)=(%g,%g)  u0=%.12e  supercritical coefs %s' % (s, y, U0v, {k: '%.4e' % v for k, v in sup.items()}))
    rows = []
    for kk in range(0, 11):
        mu = 2.0**(-kk)
        P = V.Packet(A, g, lam=mu**(2-2*A), tol=1e-30)
        inner = P.eval(s, [y])[0][0]
        vv = mu*inner
        Ps = sum(c*mu**(A*j+k)*s**j*y**k for (j, k), c in sub.items())
        Vm = (vv - Ps)/mu**(1+g)
        Pp = sum(c*mu**(A*j+k-1-g)*s**j*y**k for (j, k), c in sup.items())
        rows.append(dict(mu=mu, V=Vm, dev=Vm-U0v, dev2=Vm-U0v-Pp))
        print('   mu=2^-%-2d V=%.12e  V-u0=%.3e   V-u0-supercrit=%.3e  (/mu^4 = %.3e)' % (kk, Vm, Vm-U0v, Vm-U0v-Pp, (Vm-U0v-Pp)/mu**4), flush=True)
    out.append(dict(s=s, y=y, u0=U0v, rows=rows))
json.dump(out, open('runs/frozen_scaling2.json', 'w'), indent=1)
