"""Independent check of the closed form of a referee for Q(rho_a) = int rho W.grad(r^-3 sin 3th),
rho_a = x^2 (1 + a y)^2 e^{-r^2}, claimed Q/pi = 3a^4/512 + (51 log2/32 - 265/256) a^2 + 3 log2/8 - 21/64, c = a/4.
Velocity from my polar inverse (code/polar_inverse.py); also via the Cartesian Ewald evaluator for c and W."""
import numpy as np, sys
sys.path.insert(0, 'code')
from polar_inverse import PolarGrid
edges = np.concatenate([[0.0], np.geomspace(1e-4, 0.2, 14), np.linspace(0.25, 7, 40), np.geomspace(7.5, 1e3, 10)])
for q in (16, 24):
    G = PolarGrid(edges, q, 128)
    dth = 2*np.pi/G.nt
    integ = lambda F: np.sum(G.w[:, None]*dth*G.R*F)
    for a in (0.0, 0.5, 1.0, 2.0):
        X, Y = G.X, G.Y
        rho = X**2*(1 + a*Y)**2*np.exp(-(X**2 + Y**2))
        W1, W2 = G.velocity(rho)
        c = integ(rho*np.sin(3*G.T)/G.R**3)/np.pi
        b = integ(rho*np.cos(3*G.T)/G.R**3)/np.pi
        m = 3; Phi = np.sin(3*G.T); dPhi = 3*np.cos(3*G.T)
        gr = -m*G.R**(-m-1)*Phi; gt = G.R**(-m-1)*dPhi
        cs, sn = np.cos(G.T), np.sin(G.T)
        gx = cs*gr - sn*gt; gy = sn*gr + cs*gt
        Q = integ(rho*(W1*gx + W2*gy))
        Qc = np.pi*(3*a**4/512 + (51*np.log(2)/32 - 265/256)*a**2 + 3*np.log(2)/8 - 21/64)
        print(f'q={q} a={a}: c={c:.15f} (a/4={a/4}), psi_xx(0)={b:.2e}, Q={Q:.15f}, closed form {Qc:.15f}, diff {Q-Qc:.1e}')
