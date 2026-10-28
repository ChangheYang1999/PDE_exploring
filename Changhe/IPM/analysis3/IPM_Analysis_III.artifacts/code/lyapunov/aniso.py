"""NUMERICAL: Lyapunov window for the anisotropic jet-compatible weight
   w = |cos th|^{-2a} |sin th|^{-2 b(t)} e^{mu(t)},  t = log r,
kappa_w = b0 + (1/2) V.grad log w. Requirement kappa_w - b_+ >= delta. Prints the feasible window for mu'(t)."""
import numpy as np, sys
d = np.load('field.npz'); t = d['t']; th = d['th']; r = np.exp(t)
cl = float(d['cl']); b0 = 1 + cl; A = 2*cl - 1; D = 4*cl - 1
rx, ry, V1, V2 = d['rho_x'], d['rho_y'], d['V1'], d['V2']
bp = (np.hypot(rx, ry) - ry) / 2
C, S = np.cos(th)[None, :], np.sin(th)[None, :]
q = (V1*C + V2*S) / r[:, None]                 # V.X/r^2
vth = (-V1*S + V2*C) / r[:, None]              # V_theta / r
a = float(sys.argv[1]) if len(sys.argv) > 1 else 3.5
bmax = float(sys.argv[2]) if len(sys.argv) > 2 else 1.2
tsw = float(sys.argv[3]) if len(sys.argv) > 3 else 0.0     # b switched off around t = tsw over width 2
dl = 0.5
sig = 0.5*(1 - np.tanh((t - tsw)/2.0)); b = bmax*sig; bpr = -bmax*0.25/np.cosh((t - tsw)/2.0)**2
# interior angles only (axes are limits); use th in (0, pi/2)
J = slice(1, -1)
Cj, Sj = C[:, J], S[:, J]
ang = (a*np.tan(th[J])[None, :]*vth[:, J]          # -(1/2)(-2a) V.grad log|cos| = a tan th vth  (V.grad log|cos| = -tan th vth)
       - b[:, None]/np.tan(th[J])[None, :]*vth[:, J]   # -(1/2) 2b V.grad log|sin| = -b cot th vth
       - bpr[:, None]*q[:, J]*np.log(Sj))             # -(1/2)(2 b'(t)) log|sin| * (V.grad t) , V.grad t = q
need = 2*(bp[:, J] - b0 - ang + dl)                  # mu' q >= need
qq = q[:, J]
lo = np.where(qq > 0, need/np.where(qq > 0, qq, 1), -np.inf).max(1)
hi = np.where(qq < 0, need/np.where(qq < 0, qq, 1), np.inf).min(1)
# where q ~ 0 the requirement is need <= 0
bad0 = ((np.abs(qq) < 1e-9) & (need > 0)).any(1)
feas = (lo <= hi) & ~bad0
print('a=%.3f bmax=%.3f tsw=%.2f  feasible at all t: %s  (infeasible count %d of %d)' % (a, bmax, tsw, feas.all(), (~feas).sum(), len(t)))
for rr in [1e-3, 1e-2, 0.1, 0.5, 1, 2, 4, 8, 8.6, 10, 15, 25, 50, 100, 1e3, 1e4, 1e5]:
    i = np.argmin(abs(r - rr)); print('r=%9.3g  lo=%8.3f  hi=%8.3f  b=%.3f' % (r[i], lo[i], hi[i], b[i]))
np.savez('aniso_window_a%.2f_b%.2f.npz' % (a, bmax), t=t, lo=lo, hi=hi, feas=feas)
