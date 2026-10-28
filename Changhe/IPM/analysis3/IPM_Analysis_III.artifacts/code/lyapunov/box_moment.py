"""NUMERICAL: variable-transport multiplier of the anisotropic local L^p moment on boxes Q_2R for the exact-join modal
trial (grid field.npz): kappa_w(X) = 2 c_l/p + 1 - a V_1/x - b V_2/y; also the inflow/outflow signs on the box
(V_1/x < 0, V_2/y > 0). Axis rows theta = 0, pi/2 excluded (limits taken by the neighbouring rows)."""
import numpy as np
d = np.load('field.npz'); t = d['t']; th = d['th'][1:-1]; r = np.exp(t); cl = float(d['cl']); A = 2*cl-1; D = 4*cl-1
X = r[:,None]*np.cos(th)[None,:]; Y = r[:,None]*np.sin(th)[None,:]
v1x = d['V1'][:,1:-1]/X; v2y = d['V2'][:,1:-1]/Y
for (p,a,b) in [(2,3.5,1.2),(2,4.25,0.0),(4,3.5,1.2),(1,3.5,1.2)]:
    k0 = 2*cl/p + 1 + a*A - b*D
    kw = 2*cl/p + 1 - a*v1x - b*v2y
    for R in [0.05,0.1,0.25,0.5,1.0]:
        sel = (np.abs(X) < 2*R) & (np.abs(Y) < 2*R)
        print('p=%g a=%.2f b=%.2f kappa0=%.4f R=%.2f inf kappa_w(Q_2R)=%.4f sup V1/x=%.3f inf V2/y=%.3f sup V2/y=%.3f'
              % (p,a,b,k0,R,kw[sel].min(),v1x[sel].max(),v2y[sel].min(),v2y[sel].max()))
