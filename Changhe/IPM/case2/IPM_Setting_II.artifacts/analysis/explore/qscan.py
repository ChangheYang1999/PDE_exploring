"""Scan Q/(pi c^2) (scale invariant under the jet-preserving rescaling rho -> L^2 rho(X/L)) for test families.
A profile needs Q/(pi c^2) = 1 - 1/(2c) in (0,1) with c > 1/2 (I3 with Phi = sin 3th)."""
import numpy as np, sys
sys.path.insert(0, 'explore')
import dynres as D
from qdiag import Qfun
p0 = 0.6
G = D.Grid(-10, 12, 551, 256, p0); r = G.r[:,None]; X = r*G.cos; Y = r*G.sin
print("family poly: x^2 (1+a y)^2 (1+r^2)^{(p0-4)/2}, p0=0.6")
for a in [0.5, 1.0, 1.5, 2.0, 3.0, 5.0]:
    rho0 = X**2*(1+a*Y)**2*(1+r**2)**((p0-4)/2)
    Q, c, cm = Qfun(G, rho0/G.w, p0)
    k = Q/np.pi/c**2
    print(f"  a={a}: c={c:.5f} Q/pi={Q/np.pi:.5f} Q/(pi c^2)={k:.4f}  -> c needed {1/(2*(1-k)) if 0<k<1 else float('nan'):.4f}", flush=True)
print("family cross-pos: x^2 ((1+a y)^2 + e) (1+r^2)^{(p0-4)/2}/(1+e), p0=0.6, a=2")
for e in [0.0, 0.1, 0.3, 1.0]:
    a = 2.0
    rho0 = X**2*((1+a*Y)**2+e)*(1+r**2)**((p0-4)/2)/(1+e)
    Q, c, cm = Qfun(G, rho0/G.w, p0)
    k = Q/np.pi/c**2
    print(f"  e={e}: c={c:.5f} Q/pi={Q/np.pi:.5f} Q/(pi c^2)={k:.4f}", flush=True)
