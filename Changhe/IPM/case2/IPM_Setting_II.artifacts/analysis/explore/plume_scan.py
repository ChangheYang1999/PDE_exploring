"""Plume-head test densities (lead, 2026-10-17): rho = x^2 (1+r^2)^{(p0-2)/2} * sig, sig = (1 - tanh((y - y0 -
alpha sqrt(1+x^2))/delta))/2, i.e. density removed above a curve over the centre (a 'dead zone' above the light
column, cf. structure_v1 section 10).  Reports c, kappa = Q/(pi c^2) and the profile requirement
kappa = 2(1-p)/(2-p) (moment law + c = 1/p - 1/2; kappa is scale invariant, p is the growth exponent)."""
import numpy as np, sys
sys.path.insert(0, 'explore')
import dynres as D, qdiag as QD
p0 = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
G = D.Grid(-10, 12, 551, 256, p0); r = G.r[:,None]; X = r*G.cos; Y = r*G.sin
tgt = 2*(1-p0)/(2-p0)
print(f"p0={p0} target kappa={tgt:.4f}", flush=True)
for sgn in [1, -1]:
  for y0 in [0.5, 1.0, 2.0, 4.0]:
    for al in [0.0, 0.5, 1.0, 2.0]:
        delta = 0.3
        sig = 0.5*(1 - np.tanh((sgn*Y - y0 - al*np.sqrt(1+X**2))/delta))
        rho0 = X**2*(1+r**2)**((p0-2)/2)*sig
        Q, c, cm = QD.Qfun(G, rho0/G.w, p0)
        k = Q/np.pi/c**2
        print(f"{'above' if sgn>0 else 'below'} y0={y0} alpha={al}: c={c:.4f} kappa={k:.4f} (target {tgt:.4f})", flush=True)
