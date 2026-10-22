"""Lead 17:14Z (beta = 2): J(x,y)/(xy) near O (r = 0.05, 0.1, 0.2; angles) vs predicted lower bound 3|a0|/40, and
Omega - lambda y vs 3 a0 x y / 20, with J = Omega + lambda int_0^inf e^{-3s} W2(Phi_s X) ds, lambda = Theta_x/W2."""
import sys, numpy as np
sys.path.insert(0, 'code')
from lm_solve import load_state
from charcheck import build, evalW
from jdiag import J_at
for path in sys.argv[1:]:
    d = load_state(path); B = build(d, rmin=1e-5, rmax=1e8, nr=6000); beta = B['beta']
    a0 = evalW(B, np.array([1e-4]), np.array([1e-4]), need_fields=True)['a'][0]
    print(f"=== {path}: beta={beta}, a0={a0:.5f}; bound 3|a0|/40 = {3*abs(a0)/40:.5f}; 3 a0/20 = {3*a0/20:.5f}")
    th = np.array([0.3, 0.7, 1.0, 1.3])
    for r0 in [0.05, 0.1, 0.2, 0.5]:
        X0 = r0 * np.cos(th); Y0 = r0 * np.sin(th)
        J, Om, lam, I, traj = J_at(B, X0, Y0, smax=18.0, dt=0.004)
        print(f"  r = {r0}: J/(xy) = " + " ".join(f"{v:+.5f}" for v in J / (X0 * Y0)) + "   (Omega - lambda y)/(xy) = " + " ".join(f"{v:+.5f}" for v in (Om - lam * Y0) / (X0 * Y0)) + "   lambda = " + " ".join(f"{v:+.3e}" for v in lam))
