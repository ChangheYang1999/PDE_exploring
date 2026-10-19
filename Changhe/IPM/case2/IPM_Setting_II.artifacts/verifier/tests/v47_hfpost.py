"""V47: decomposition of the measured delta log Xi (runs/v47_hfsym_kK.npz) into re-timing (m1 delta T), orbit-geometry change
(delta log|u0|, from delta theta at r = e^tstop) and the delta m1 T term; windowed projections on cos(k th) per period."""
import sys, numpy as np
d = np.load(sys.argv[1]); k = int(d['k']); h = float(d['h']); th = d['the']; ne = len(th); m1 = float(d['m1']); dm1 = float(d['dm1'])
Q = d['Q']; T = d['T']; dT = (d['Tp'] - d['Tm'])/2
dlu0 = (np.log(np.abs(np.cos(d['th0p'] - np.pi))) - np.log(np.abs(np.cos(d['th0m'] - np.pi))))/2   # e1 = 180 deg (horizontal)
c = np.cos(k*th); per = ne//k
def proj(f, sl):
    return float((f[sl]*c[sl]).sum()/(h*(c[sl]**2).sum()))
print('k', k, 'm1', round(m1, 5), 'dm1/h', round(dm1/h, 4))
print('theta  Q   dT/pert_pred(1-e^-Q)  dT_meas  m1dT  dlog|u0|  dm1*T  dXi_meas  dXi_pred   dth0_amp(deg)')
for j in range(k):
    sl = slice(j*per, (j + 1)*per)
    if d['A0'][sl].min() < 1e-2: continue
    dth0 = (d['th0p'] - d['th0m'])/2
    print('%6.1f %5.2f %7.4f %7.4f %7.4f %8.4f %7.4f %7.4f %7.4f %8.4f' % (np.degrees(th[sl].mean()), Q[sl].mean(), (1 - np.exp(-Q[sl])).mean(),
          proj(dT, sl), proj(m1*dT, sl), proj(dlu0, sl), proj(dm1*T, sl), proj(d['dXi'], sl), (m1*(1 - np.exp(-Q[sl]))).mean(),
          np.degrees(proj(dth0, sl))))
