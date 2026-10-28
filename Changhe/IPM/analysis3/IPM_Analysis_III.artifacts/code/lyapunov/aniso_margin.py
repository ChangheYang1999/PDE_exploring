"""NUMERICAL margin m(X) = kappa_w(X) - b_+(X) for w = |cos th|^{-2a}|sin th|^{-2b(t)} e^{mu(t)} with the mu' of aniso_mu.py."""
import numpy as np
d = np.load('field.npz'); t = d['t']; th = d['th']; r = np.exp(t)
cl = float(d['cl']); b0 = 1 + cl
rx, ry, V1, V2 = d['rho_x'], d['rho_y'], d['V1'], d['V2']
bp = (np.hypot(rx, ry) - ry) / 2
C, S = np.cos(th)[None, :], np.sin(th)[None, :]
q = (V1*C + V2*S) / r[:, None]; vth = (-V1*S + V2*C) / r[:, None]
a, bmax, tsw = 3.5, 1.2, 0.0
b = bmax*0.5*(1 - np.tanh((t - tsw)/2.0)); bpr = -bmax*0.25/np.cosh((t - tsw)/2.0)**2
mup = np.load('aniso_mup.npy')
J = slice(1, -1)
kap = (b0 + 0.5*mup[:, None]*q[:, J] + a*np.tan(th[J])[None, :]*vth[:, J]
       - b[:, None]/np.tan(th[J])[None, :]*vth[:, J] - bpr[:, None]*q[:, J]*np.log(S[:, J]))
m = kap - bp[:, J]
i, j = np.unravel_index(m.argmin(), m.shape)
print('min margin %.4f at r=%.4g th=%.4f (kappa %.3f, b+ %.3f)' % (m.min(), r[i], th[J][j], kap[i, j], bp[i, J][j]))
for lab, sl in [('r<0.1', r < 0.1), ('0.1<r<5', (r > 0.1) & (r < 5)), ('5<r<60', (r > 5) & (r < 60)), ('r>60', r > 60)]:
    print('%10s min margin %.4f' % (lab, m[sl].min()))
print('near y-axis (last interior angle) min %.4f; near x-axis (first) min %.4f' % (m[:, -1].min(), m[:, 0].min()))
np.savez('aniso_margin.npz', t=t, th=th[J], m=m)
